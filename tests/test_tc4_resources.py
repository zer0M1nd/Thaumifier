"""Exercise first-use choices without downloading or distributing any mod assets."""

from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
from io import BytesIO, StringIO
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import tc4_resources as resources


class ResourceChoices(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name) / "profile"
        fixture = BytesIO()
        with ZipFile(fixture, "w") as archive:
            archive.writestr(resources.LANG_FILES["zh_CN"], "fixture.key=测试用句子。\n")
            archive.writestr(resources.LANG_FILES["en_US"], "fixture.key=Fixture = value\n")
            archive.writestr("assets/other/lang/en_US.lang", "fixture.other=Unrelated member\n")
        self.fixture = fixture.getvalue()
        self.jar = self.directory / resources.FILENAME
        self.replace(resources, "data_directory", return_value=self.directory)
        self.replace(resources, "SIZE", len(self.fixture))
        self.replace(resources, "SHA256", sha256(self.fixture).hexdigest())
        # Exercise the HTTPS path even on a Python installation missing OpenSSL.
        self.replace(resources.http.client, "HTTPSConnection", object(), create=True)
        self.http = self.replace(resources, "urlopen", side_effect=lambda *a, **kw: BytesIO(self.fixture))
        self.terminal = self.replace(sys, "stdin", StringIO(""))

    def replace(self, target, name, *args, **kwargs):
        replacement = patch.object(target, name, *args, **kwargs)
        self.addCleanup(replacement.stop)
        return replacement.start()

    def run_cli(self, *args):
        out, err = StringIO(), StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = resources.main(list(args))
        return code, out.getvalue().strip(), err.getvalue().strip()

    def test_undecided_has_no_implicit_default(self):
        self.assertEqual(self.run_cli("status"), (0, "undecided", ""))
        code, prompt, _ = self.run_cli("setup")
        self.assertNotEqual(code, 0)
        self.assertIn(resources.DOWNLOAD_LABEL, prompt)
        self.assertIn(resources.SKIP_LABEL, prompt)
        self.assertNotEqual(self.run_cli("read", "fixture.key")[0], 0)
        self.assertFalse(self.directory.exists())
        self.http.assert_not_called()

    def test_skip_persists_and_blocks_even_a_populated_cache(self):
        self.replace(sys, "stdin", StringIO("2\n"))
        self.assertEqual(self.run_cli("setup")[0], 0)
        self.jar.write_bytes(self.fixture)
        self.assertEqual(self.run_cli("setup"), (0, "disabled", ""))
        self.assertEqual(self.run_cli("status"), (0, "disabled", ""))
        with patch.object(resources, "ZipFile", side_effect=AssertionError("opened disabled cache")):
            code, output, _ = self.run_cli("read", "references/source-keys.md#k-fixture.key")
            self.assertNotEqual(code, 0)
            self.assertEqual(output, "")
        self.http.assert_not_called()

    def test_download_resolves_both_locales_and_reuses_verified_bytes(self):
        self.replace(sys, "stdin", StringIO(resources.DOWNLOAD_LABEL + "\n"))
        self.assertEqual(self.run_cli("setup")[0], 0)
        self.assertEqual(self.http.call_args.args[0].full_url, resources.DOWNLOAD_URL)
        self.assertEqual(self.run_cli("status"), (0, "enabled", ""))
        code, out, _ = self.run_cli("read", "references/source-keys.md#k-fixture.key")
        self.assertEqual(code, 0)
        self.assertIn("测试用句子。", out)
        self.assertIn("Fixture = value", out)
        self.assertNotIn("zh_CN", self.run_cli("read", "fixture.key", "--lang", "en_US")[1])
        self.assertNotEqual(self.run_cli("read", "fixture.other")[0], 0)
        self.assertNotEqual(self.run_cli("read", "source-keys.md#addon-Test-fixture.key")[0], 0)
        self.assertEqual(self.jar.read_bytes(), self.fixture)
        self.assertEqual({p.name for p in self.directory.iterdir()}, {"choice", resources.FILENAME})
        self.assertEqual(self.http.call_count, 1)
        self.run_cli("setup", "--choice", "skip")
        self.assertNotEqual(self.run_cli("read", "fixture.key")[0], 0)

    def test_an_existing_jar_cannot_grant_consent(self):
        self.directory.mkdir()
        self.jar.write_bytes(self.fixture)
        for invalid_choice in (None, b"", b"yes", b"\xff"):
            if invalid_choice is not None:
                (self.directory / "choice").write_bytes(invalid_choice)
            self.assertEqual(self.run_cli("status"), (0, "undecided", ""))
            self.assertNotEqual(self.run_cli("read", "fixture.key")[0], 0)
        self.http.assert_not_called()

    def test_interactive_first_lookup_honors_the_choice(self):
        stream = StringIO("2\n")
        self.replace(stream, "isatty", return_value=True)
        self.replace(sys, "stdin", stream)
        code, out, _ = self.run_cli("read", "fixture.key")
        self.assertIn(resources.DOWNLOAD_LABEL, out)
        self.assertNotEqual(code, 0)
        self.assertEqual(self.run_cli("status"), (0, "disabled", ""))
        self.http.assert_not_called()

    @unittest.skipUnless(os.name == "nt", "Windows fallback")
    def test_windows_without_ssl_uses_curl_and_checks_download(self):
        self.replace(resources.http.client, "HTTPSConnection", None)
        self.replace(resources.shutil, "which", return_value="curl.exe")

        def fake_curl(args, *, check):
            self.assertTrue(check)
            self.assertEqual(args[-1], resources.DOWNLOAD_URL)
            Path(args[args.index("--output") + 1]).write_bytes(b"wrong bytes")

        self.replace(resources.subprocess, "run", side_effect=fake_curl)
        self.assertNotEqual(self.run_cli("setup", "--choice", "download")[0], 0)
        self.assertFalse(self.jar.exists())
        self.http.assert_not_called()

    def test_failed_or_invalid_download_can_be_retried(self):
        broken = self.fixture[:-1] + bytes([self.fixture[-1] ^ 1])
        self.http.side_effect = [URLError("offline"), BytesIO(broken), BytesIO(self.fixture)]
        self.assertNotEqual(self.run_cli("setup", "--choice", "download")[0], 0)
        self.assertNotEqual(self.run_cli("setup")[0], 0)
        self.assertFalse(self.jar.exists())
        self.assertFalse(any(self.directory.glob("*.part")))
        self.assertEqual(self.run_cli("setup"), (0, "enabled", ""))
        self.assertEqual(self.jar.read_bytes(), self.fixture)

    def test_corrupt_cache_is_replaced_before_reading(self):
        self.run_cli("setup", "--choice", "download")
        self.jar.write_bytes(b"!" * len(self.fixture))
        self.assertEqual(self.run_cli("read", "fixture.key")[0], 0)
        self.assertEqual(self.jar.read_bytes(), self.fixture)
        self.assertEqual(self.http.call_count, 2)


if __name__ == "__main__":
    unittest.main()
