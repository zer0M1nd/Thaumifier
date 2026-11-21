# 10 TC4Revival 项目专用说明

> 本篇只适用于 TC4Revival（Minecraft 1.20.1 / Forge 的神秘时代 4 移植及其附属）。为其他项目写作时可以跳过，但其中“如何判断哪些文本该改”的思路是通用的。以下内容记录于 2026-11，路径相对于仓库根目录。项目结构可能变化，动手前请先阅读仓库的 `AGENTS.md` 与 `Docs/START-HERE.md`。

## 1. 文本放在哪里

| 内容 | 位置 |
| --- | --- |
| 研究定义（分类、坐标、前置） | `Code/<模组>/src/{main,generated}/resources/data/<ns>/research_catalog/*.json` |
| 研究页面（每页类型、引用的语言键、是否 legacy） | `.../data/<ns>/research_pages/*.json` |
| 中文语言文件 | `.../assets/<ns>/lang/zh_cn.json`；神秘注魔另有 `src/main/localization/zh_cn.json`，与 generated 版内容相同，两份都要改 |
| 本体新增文本 | `Code/TC4/src/generated/resources/assets/thaumcraft/lang/zh_cn.json`。**这是 datagen 产物**，源头是 `Code/TC4/src/main/java/tc4revival/data/TCDataGeneration.java` 中的字符串，改文本时两处都要同步，否则重跑 `runData` 会被覆盖 |
| 历史本体参考 | 在本技能中按[资源选择](../README.zh-CN.md)处理，启用后由只读查询器按键查阅。 |

## 2. 哪些文本在范围内

- 本体与附属的原作文本（原版研究正文等）由本体在**运行时从玩家目录外部加载**，不在工作区内，也**不改**。
- **只改工作区语言文件中、被研究页面实际引用的键**：
  - 本体：移植版新增的研究，以及在原研究后追加的新页。
  - 现代原创附属（神秘万象、神秘时代：未来、神秘旅程、神秘远征）：全部研究文本。
  - 移植附属：移植时写的说明页、补记页、新研究；原作忠实译文保持不变。
- **不要改**：
  - `book_text/zh_cn.json`：对外部原文的错别字修补，格式为 find / replace。
  - `data/thaumcraft/research_changes/`：承续版差异提示，刻意写得简短。
  - `data/thaumcraft/research_text_replacements/`：删除线纠错数据。
  - 界面文本、提示框、Ponder、Patchouli 页。
- **神秘旅程、神秘远征**有部署排除规则：可以改文本，但不要安装或发布。

## 3. 页面 JSON 的关键字段

```json
{
  "id": "thaumicomniverse:AIRSHIPS/assembly",
  "type": "TEXT",
  "text": {"translate": "omniverse.page.airships.assembly"},
  "page_break": true,
  "import_legacy": true
}
```

- `import_legacy: true` 表示按旧格式解析 `<BR>`、`<LINE>`、`<IMG>`、`§`；不带此字段的页面只认 `\n`。
- `page_break: true` 表示另起一页，所以每个键都应是完整段落。
- `TEXT_CONCEALED` 表示隐藏页，`research` 字段写明解锁它所需的研究。
- 页面 JSON 中的 `text` 也可能是字面字符串或组件数组，不一定引用语言键。

## 4. 共享键与动态键

- 神秘万象和神秘时代：未来的语言文件中，有 36 个 `thaumicomniverse:*` 研究名和副标题重复出现（这些研究已迁移到未来）。两份必须同步，由未来负责。
- `omniverse.page.extremely_primordial_pearl`、`omniverse.page.akashic_record` 在两个模组中各有一份，合并成同一文本。
- `omniverse.page.arcane_crafter` 属于神秘万象的研究，但文本只存在于未来的语言文件中。
- `omniverse.research.universal_enchantment` 和 `omniverse.page.universal_enchantment` 供旧存档中按附魔拆分的研究使用，由 `DynamicResearchLanguageMixin` 动态取用。标题是附魔名本身，副标题与正文仍需改写。

## 5. 新版阅读器的特性

- 文字使用 Minecraft 原生字体排版，正文宽 139 像素，自动分页。
- 原作译文导入时，会把完整的拉丁要素名、“某要素 / 某之要素”和研究名称**自动转为可悬停的链接组件**。因此提到要素时，写标准拉丁名或标准中文名效果最好。
- 原生组件页支持 `{"aspect":"aer"}`、`{"research":"KEY"}`、`{"item":"id"}` 等扩展组件，见 `Docs/Projects/TC4/docs/BOOK-COMPONENTS.md`。只改语言文件时用不到。

## 6. 推荐的交付方式

如果用户要求仓库只读：

```
<输出文件夹>/
  files/Code/...            ← 与仓库路径一致的完整 zh_cn.json，可直接覆盖
  datagen-source/...        ← 如涉及本体，附上同步修改后的 TCDataGeneration.java
  REVIEW/<模组>.md           ← 逐键“改写前 / 改写后”
  README.md                 ← 范围、规模、删减、冲突、标题变更、未验证项
```

如果需要写入仓库，先遵循仓库规则：认领模块，必要时修改 datagen 源码并重新生成，按测试规范在游戏内抽查分页效果。

## 7. 2026-11 重写的结论摘要

- 共重写 20 个模组、636 个键（614 个键的值发生变化）。
- 重写后单页中位数约 105 字，与原版约 100 字接近；90 分位约 217 字，比原版的 175 字略长。副标题中位数 7 字。
- 上次仅更改两项标题。一项把研究网络改成与解谜更贴切的说法，另一项让核心名称与物品显示名一致。后一项的历史对照见 [item.FocusPech.name](source-keys.md#k-item.FocusPech.name)。
- 已知的不足见 [examples/rewritten/annotated.md](../examples/rewritten/annotated.md) 末尾的“总体自我批评”：补记页的开头千篇一律、少数句子冗余、个别页面偏长；神秘万象“奥术马达”页有一处 `§fOrdo§0`（白字），建议改为 `§7Ordo§0`。
- 2026-11-21 复查时，仓库语言文件已合入上述重写（688 处改动中有 684 处与交付一致，其余 4 个键后来被移除或迁移），并新增了引导类研究（`GUIDE_*`、`M_*`、`TUT_ADDON_*` 等）。这些新增文本不在上次重写范围内，可以用本技能另行处理。
