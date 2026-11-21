#!/usr/bin/env python3
"""Resolve a Thaumcraft 4 localization key after a per-user, per-checkout choice."""

import argparse
import hashlib
import http.client
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from urllib.request import Request, urlopen
from urllib.parse import unquote
from zipfile import BadZipFile, ZipFile


FILENAME = "Thaumcraft-1.7.10-4.2.3.5.jar"
DOWNLOAD_URL = "https://edge.forgecdn.net/files/2227/552/" + FILENAME
SIZE = 12565807
SHA256 = "3dba9786966974701578a658d1bb369bf35bdf5f363079f5ac9c4910a39113be"
LANG_FILES = {
    "zh_CN": "assets/thaumcraft/lang/zh_CN.lang",
    "en_US": "assets/thaumcraft/lang/en_US.lang",
}
DOWNLOAD_LABEL = "下载神秘时代 4 资源"
SKIP_LABEL = "不使用神秘时代 4 资源"
CHUNK = 256 * 1024


def data_directory():
    checkout = Path(__file__).resolve().parents[1]
    if os.name == "nt":
        base = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData/Local")
    elif sys.platform == "darwin":
        base = Path.home() / "Library/Application Support"
    else:
        base = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local/share")
    checkout_id = hashlib.sha256(os.fsencode(os.path.normcase(str(checkout)))).hexdigest()[:24]
    directory = (base / "thaumifier" / checkout_id).resolve()
    if checkout == directory or checkout in directory.parents:
        raise ValueError("用户数据目录位于本仓库内，请将其设到仓库外再使用资源。")
    return directory


def preference(directory):
    try:
        value = (directory / "choice").read_bytes()
    except FileNotFoundError:
        return "undecided"
    return {b"download\n": "enabled", b"skip\n": "disabled"}.get(value, "undecided")


def save_choice(directory, choice):
    directory.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=directory, delete=False) as temp:
        path = Path(temp.name)
    try:
        path.write_bytes((choice + "\n").encode("ascii"))
        os.replace(path, directory / "choice")
    finally:
        path.unlink(missing_ok=True)


def require_enabled(directory):
    state = preference(directory)
    if state == "undecided":
        raise ValueError(f"尚未选择。请先运行 setup 并选择「{DOWNLOAD_LABEL}」或「{SKIP_LABEL}」。")
    if state == "disabled":
        raise ValueError("旧版文本引用不可用。已选择「不使用神秘时代 4 资源」。")


def copy_and_hash(source, target=None):
    digest = hashlib.sha256()
    length = 0
    while True:
        block = source.read(CHUNK)
        if not block:
            break
        length += len(block)
        if length > SIZE:
            return False
        digest.update(block)
        if target is not None:
            target.write(block)
    return length == SIZE and digest.hexdigest() == SHA256


def download_to(path):
    if getattr(http.client, "HTTPSConnection", None) is not None:
        request = Request(DOWNLOAD_URL, headers={"User-Agent": "Thaumifier/1"})
        with urlopen(request, timeout=45) as source, path.open("wb") as target:
            return copy_and_hash(source, target)

    # Some Windows Python installations lack a working OpenSSL DLL.
    curl = shutil.which("curl.exe") if os.name == "nt" else None
    if not curl:
        raise ValueError("下载需要支持 HTTPS 的 Python 3；Windows 也可使用系统 curl.exe。")
    subprocess.run([curl, "--fail", "--location", "--silent", "--show-error",
                    "--proto", "=https", "--proto-redir", "=https", "--max-time", "120",
                    "--max-filesize", str(SIZE), "--output", str(path), DOWNLOAD_URL], check=True)
    with path.open("rb") as source:
        return copy_and_hash(source)


def ensure_archive(directory):
    require_enabled(directory)
    jar = directory / FILENAME
    if jar.is_file() and jar.stat().st_size == SIZE:
        with jar.open("rb") as source:
            if copy_and_hash(source):
                return jar

    require_enabled(directory)
    with tempfile.NamedTemporaryFile(dir=directory, prefix="download-", suffix=".part",
                                     delete=False) as temp:
        path = Path(temp.name)
    try:
        if not download_to(path):
            raise ValueError("下载文件的大小或 SHA-256 与固定版本不符，已放弃本次下载。")
        require_enabled(directory)
        os.replace(path, jar)
    finally:
        path.unlink(missing_ok=True)
    return jar


def ask_choice():
    print(f"1. {DOWNLOAD_LABEL}\n2. {SKIP_LABEL}", flush=True)
    try:
        answer = input("请选择 1 或 2 / Choose 1 or 2: ").strip()
    except EOFError:
        answer = ""
    choices = {"1": "download", DOWNLOAD_LABEL: "download", "2": "skip", SKIP_LABEL: "skip"}
    if answer not in choices:
        raise ValueError("需要用户明确选择，资源仍未启用。")
    return choices[answer]


def setup(directory, choice):
    if choice is None and preference(directory) == "undecided":
        choice = ask_choice()
    if choice is not None:
        save_choice(directory, choice)
    if preference(directory) == "disabled":
        print("disabled")
        return
    ensure_archive(directory)
    print("enabled")


def link_key(reference):
    if "#" not in reference:
        return reference
    fragment = unquote(reference.split("#", 1)[1])
    if fragment.startswith("user-content-"):
        fragment = fragment[len("user-content-"):]
    if fragment.startswith("addon-"):
        raise ValueError("此引用属于独立附属，神秘时代 4 本体 JAR 不含其语言文件。")
    if not fragment.startswith("k-"):
        raise ValueError("引用链接中没有语言键。")
    return fragment[2:]


def read_entries(directory, references, lang):
    require_enabled(directory)
    keys = list(dict.fromkeys(link_key(ref) for ref in references))
    wanted = set(keys)
    locales = list(LANG_FILES) if lang == "both" else [lang]
    found = {}
    with ZipFile(ensure_archive(directory), "r") as jar:
        for locale in locales:
            with jar.open(LANG_FILES[locale], "r") as source:
                for raw_line in source:
                    line = raw_line.decode("utf-8-sig").rstrip("\r\n")
                    if line.lstrip().startswith("#"):
                        continue
                    key, separator, value = line.partition("=")
                    key = key.strip()
                    if separator and key in wanted:
                        found[key, locale] = value
    require_enabled(directory)
    missing = [key for key in keys if all((key, loc) not in found for loc in locales)]
    if missing:
        raise ValueError("指定语言中没有这些键：" + ", ".join(missing))
    for key in keys:
        for locale in locales:
            if (key, locale) in found:
                print(f"[{locale}] {key} = {found[key, locale]}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="Print undecided, disabled or enabled without network access.")
    setup_parser = sub.add_parser("setup", help="Choose interactively on first use or apply a confirmed choice.")
    setup_parser.add_argument("--choice", choices=["download", "skip"],
                              help="For agents: use only after the user explicitly chooses.")
    read_parser = sub.add_parser("read", help="Read selected keys from the verified JAR.")
    read_parser.add_argument("references", metavar="KEY_OR_LINK", nargs="+")
    read_parser.add_argument("--lang", choices=[*LANG_FILES, "both"], default="both")
    args = parser.parse_args(argv)
    try:
        directory = data_directory()
        if args.command == "status":
            print(preference(directory))
        elif args.command == "setup":
            setup(directory, args.choice)
        else:
            if preference(directory) == "undecided" and sys.stdin.isatty():
                setup(directory, None)
            read_entries(directory, args.references, args.lang)
    except (ValueError, OSError, subprocess.CalledProcessError,
            http.client.HTTPException, BadZipFile, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    # Agents usually pipe the CLI. Windows otherwise falls back to the ANSI code page.
    if os.name == "nt":
        for stream in (sys.stdin, sys.stdout, sys.stderr):
            if not stream.isatty():
                stream.reconfigure(encoding="utf-8-sig" if stream is sys.stdin else "utf-8")
    sys.exit(main())
