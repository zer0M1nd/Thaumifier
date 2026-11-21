# Thaumonomicon Style Guide for Thaumcraft 4

[简体中文 README](README.zh-CN.md)

This repository gives authors who use LLM agents to create **Thaumcraft 4 add-ons** a comprehensive guide to writing descriptions in the style of the **Thaumonomicon**, the in-game research book. It focuses on Simplified Chinese research titles, subtitles and pages. Authors can use it to draft a new entry, translate a page, or turn a list of mechanics into a research note while preserving its numbers, conditions and controls.

## First use

The first time an agent uses this checkout, it asks you to choose one of the following options. You can make the same choice yourself from the repository root with `python scripts/tc4_resources.py setup`.

| Choice shown by the agent | What happens |
| --- | --- |
| **下载神秘时代 4 资源** (Download Thaumcraft 4 resources) | The agent automatically downloads **Thaumcraft 4.2.3.5 for Minecraft 1.7.10** from CurseForge’s CDN and verifies its size and SHA-256. It opens the JAR read-only and looks up keys in `assets/thaumcraft/lang/zh_CN.lang` and `en_US.lang`. |
| **不使用神秘时代 4 资源** (Do not use Thaumcraft 4 resources) | All references to legacy text are unavailable. The writing guides, annotations, modern examples, templates and linter remain available offline. |

The choice is saved for the current user and checkout, outside the repository. A new checkout asks again. A verified download is reused offline. If the transfer fails, run `setup` again to retry. An explicit change to `--choice skip` also blocks reads from a previously cached JAR. The reader never runs the mod or extracts language files. [CurseForge release, file 2227552](https://www.curseforge.com/minecraft/mc-mods/thaumcraft/files/2227552)

Legacy citations throughout the guide lead to a language key. After opting in, pass the key or the link target to `read` to view the available Chinese and English text. Citations to historical **add-ons** identify the add-on and its key. Their language files belong to separate releases and are outside the base-mod download. [Language-key index](references/source-keys.md)

```sh
python scripts/tc4_resources.py status
python scripts/tc4_resources.py read tc.research_page.NITOR.1
python scripts/tc4_resources.py read "references/source-keys.md#k-tc.research_text.NITOR" --lang en_US
```

## Using the guide

Start with the skill instructions. Gather the item’s mechanics and exceptions, choose a page type and voice, then compare the draft with a modern example. The scripts require Python 3.8+ and its standard library. On Windows you can use `py -3`, and on Linux or macOS you can use `python3`. Windows Python installations without HTTPS support can use the system’s `curl.exe` for the download. [Skill instructions](SKILL.md)

| What you are working on | Where to look |
| --- | --- |
| Narrator, pacing and page type | [Voice](references/01-voice.md) · [Structure](references/02-structure.md) · [15 page patterns](references/04-page-patterns.md) |
| Titles, subtitles and terminology | [Naming and translation](references/03-titles-subtitles.md) · [Terminology](references/05-terminology.md) · [Glossary key index](references/appendix-glossary.md) |
| Formatting and accuracy | [Formatting](references/06-formatting.md) · [Fact checking](references/07-facts-and-meta.md) · [Workflow and checklist](references/09-workflow.md) |
| An add-on’s voice or a TC4Revival project | [Add-on profiles](references/08-addon-voices.md) · [Project notes](references/10-tc4revival-notes.md) |
| Examples to compare | [31 annotated rewrites](examples/rewritten/annotated.md) · [Before-and-after examples across 20 mods](examples/rewritten/full-corpus/README.md) · [Common mistakes](examples/negative/catalog.md) |
| Historical style and length | [199 title and subtitle pairs by key](examples/original/tc4-research-catalog.md) · [101 annotated page references](examples/original/tc4-annotated.md) · [Statistics](references/appendix-statistics.md) |
| Starting or reviewing a draft | [Research entry template](templates/research-entry.md) · [Batch task brief](templates/rewrite-task-brief.md) · [Work packet](templates/work-packet.example.json) · [Chinese text linter](scripts/lint_zh_text.py) |

For a file-capable agent, point its project instructions at `SKILL.md`. Agents that discover skills can load the entire folder from their skill directory. A human writer can follow the same guide. To check a draft or compare two localization files, run the linter from the repository root.

```sh
python scripts/lint_zh_text.py --text "纸页背后还有一层薄薄的刻痕。" --kind page
python scripts/lint_zh_text.py --before old/zh_cn.json --after new/zh_cn.json
```

## Disclaimer

This project does not include any unauthorized original Thaumcraft 4 assets. The author is not affiliated with Mojang AB, Azanor, or Team CoFH.

The writing guidance, annotations, templates and scripts are project materials. The modern rewrite examples come from TC4Revival. When adding a historical citation, record its source and localization key.
