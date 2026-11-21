# 神秘时代 4 魔导手册风格指引

[English README](README.md)

为想要使用 LLM Agent 创作神秘时代 4 附属的作者，提供一套全面的神秘时代 4 魔导手册描述风格指引。你可以用它从零写一项研究，翻译英文条目，或把一段功能说明改成研究者的笔记。指南涵盖简体中文标题、副标题与正文，帮助你在改写时保留数值、操作条件和例外。

## 首次使用

Agent 第一次使用这份仓库时，会请你明确选择下列一项。人类作者也可以在仓库根目录运行 `python scripts/tc4_resources.py setup`，在终端作出相同选择。

| Agent 显示的选项 | 选择后会发生什么 |
| --- | --- |
| **下载神秘时代 4 资源** | Agent 自动从 CurseForge 的 CDN 下载 **Minecraft 1.7.10 的 Thaumcraft 4.2.3.5 JAR**，校验文件大小和 SHA-256。查询器以只读方式打开 JAR，按键读取其中的 `assets/thaumcraft/lang/zh_CN.lang` 和 `en_US.lang`。 |
| **不使用神秘时代 4 资源** | 所有旧版文本引用均不可用。写作指南、手法注释、现代示例、模板和检查器仍可离线使用。 |

选择按当前用户和仓库路径保存，缓存位于仓库外。新的仓库副本会再次询问。校验通过的 JAR 可以离线复用，下载中断后可重新运行 `setup`。要改变决定，可运行 `setup --choice download` 或 `setup --choice skip`。停用后，即使已有缓存也无法查询旧文。查询器不运行模组，也不解包语言文件。[CurseForge 原作发布页（文件 2227552）](https://www.curseforge.com/minecraft/mc-mods/thaumcraft/files/2227552)

正文里的旧文链接会打开对应的语言键和查询命令。启用资源后，把键名或链接目标交给 `read`，即可对照原包中现有的中英文。**历史附属**的链接标明所属模组和键名。它们的语言文件属于各自的发行包，因此下载本体只启用本体的原文查询。[语言键索引](references/source-keys.md)

```sh
python scripts/tc4_resources.py status
python scripts/tc4_resources.py read tc.research_page.NITOR.1
python scripts/tc4_resources.py read "references/source-keys.md#k-tc.research_text.NITOR" --lang zh_CN
```

## 用这套指南写一页研究

从技能入口开始。先列出玩家需要知道的机制和例外，按研究位置选语气和页型，最后对照现代示例检查篇幅、排版与事实。脚本使用 Python 3.8 或更高版本的标准库。Windows 可用 `py -3`，Linux 或 macOS 可用 `python3`。Windows 上的 Python 若缺少 HTTPS 支持，下载器会调用系统的 `curl.exe`。[技能入口](SKILL.md)

| 写作时想解决的问题 | 对应材料 |
| --- | --- |
| 谁在说话，一页该怎样起笔和收尾？ | [叙事声音](references/01-voice.md) · [条目结构](references/02-structure.md) · [15 种页型](references/04-page-patterns.md) |
| 怎样拟标题、译副标题、核对名词？ | [标题与副标题](references/03-titles-subtitles.md) · [术语用法](references/05-terminology.md) · [译名键索引](references/appendix-glossary.md) |
| 怎样保住数值、按键、条件和排版？ | [格式与标记](references/06-formatting.md) · [事实与元信息](references/07-facts-and-meta.md) · [流程与自检](references/09-workflow.md) |
| 给某个附属或移植项目写作，要注意什么？ | [15 个附属的声音画像](references/08-addon-voices.md) · [TC4Revival 项目说明](references/10-tc4revival-notes.md) |
| 一段说明具体是怎么改的？ | [31 组带评注的改写](examples/rewritten/annotated.md) · [20 个模组、614 个键的前后对照](examples/rewritten/full-corpus/README.md) · [反例目录](examples/negative/catalog.md) |
| 怎样参照旧版篇幅和写法？ | [199 组标题与副标题引用](examples/original/tc4-research-catalog.md) · [101 个正文引用与手法注释](examples/original/tc4-annotated.md) · [篇幅与句式统计](references/appendix-statistics.md) |
| 从哪里开始写或审稿？ | [单条研究模板](templates/research-entry.md) · [批量改写说明](templates/rewrite-task-brief.md) · [工作包示例](templates/work-packet.example.json) · [中文检查器](scripts/lint_zh_text.py) |

使用 Claude、Codex 或其他能读文件的 Agent 时，将整个文件夹放入其技能目录，或在项目指令中指向 `SKILL.md`。本仓库也提供 [AGENTS.md](AGENTS.md)。人类写手可以沿用同一阅读顺序。写完后，可在仓库根目录检查单页，或比较两份语言文件。

```sh
python scripts/lint_zh_text.py --text "纸页背后还有一层薄薄的刻痕。" --kind page
python scripts/lint_zh_text.py --before old/zh_cn.json --after new/zh_cn.json
```

## 免责声明（Disclaimer）

本项目不包含未经授权的神秘时代 4 原始资源。作者与 Mojang AB/Azanor/Team CoFH 无任何关联。

写作指南、手法注释、模板与脚本为项目材料。现代改写示例来自 TC4Revival。补充历史样例时，请登记来源与语言键。
