---
name: thaumonomicon-style-zh
description: 用神秘时代 4（Thaumcraft 4）原版魔导手册（Thaumonomicon）的风格撰写、重写或翻译简体中文研究文本，包括研究标题、副标题和正文页。适用于 TC4 本体、TC4 附属（神秘工匠、禁忌魔法、自动化魔法等）及其现代移植或原创扩展（如 TC4Revival）。凡是要编写、润色、审校魔导手册或研究笔记的中文文本，或把功能说明改写成手册口吻时都应使用；也适用于检查已有手册文本是否符合 TC4 风格。
---

# 神秘时代 4 魔导手册风格指导（简体中文）

本技能教你写出**读起来像神秘时代 4 原版魔导手册**的中文研究文本。它总结自对 1.7.10 神秘时代 4（4.2.3.5）全部 307 段研究正文、199 条标题与副标题的逐条阅读与统计，以及对 15 个原作附属手册的阅读；同时附带一次约 600 个键的实际重写经验，包括反例、改写示范和自我批评。

需要深入时，按第 7 节索引查阅 `references/` 和 `examples/`。

## 首次使用与旧文引用

每次开始使用本技能，先在技能根目录运行 `python scripts/tc4_resources.py status`。

- `undecided`：先在对话中请用户明确选择 **下载神秘时代 4 资源** 或 **不使用神秘时代 4 资源**，等待答复。安装本技能、请求写作、目录里已有 JAR 或用户未答复，均不能代替选择。
- 用户选择下载后，Agent 立即运行 `python scripts/tc4_resources.py setup --choice download`。它自动下载并校验 Minecraft 1.7.10 的 Thaumcraft 4.2.3.5。以后在 `enabled` 状态下，用 `python scripts/tc4_resources.py read KEY` 直接从包内只读查询。可传多个键或完整的 Markdown 链接目标。下载失败时说明原因，有效缓存建立后才可引用旧文。
- 用户选择不使用后，运行 `python scripts/tc4_resources.py setup --choice skip`。以后在 `disabled` 状态下跳过所有旧文引用，使用指南、现代示例、模板与检查器继续写作。用户明确更改决定时再更新选择。

网页上的旧文链接只展示语言键。查询使用指定本体 JAR 内的 `zh_CN.lang` 与 `en_US.lang`。独立附属的键只记录出处。不要从网上、其他已安装模组或源仓库补取引文，不要把语言文件、查询结果或 JAR 写入仓库。没有执行工具的 Agent 同样先询问；选择下载时请具备文件访问能力的运行环境完成设置，并如实说明引用是否可用。


---

## 1. 工作流程（每次都照做）

1. **确认任务类型**：从零撰写、风格重写，还是翻译原作？见 [references/09-workflow.md](references/09-workflow.md)。
2. **列事实清单**：功能、数值、操作、条件、例外、依赖与配置、物品名。**风格可以改，事实不能改。**
3. **确认页面模式**：旧式页（`<BR>`、`<LINE>`、`<IMG>`、`§`）还是原生组件页（只能用 `\n`）？不确定就看原文里用的是哪种换行。
4. **确定语气**：看研究分类与前置研究。为附属写作时，可参考[各附属的声音](references/08-addon-voices.md)和对应的现代改写。
5. **选页型并写正文**：参照第 4 节和 [references/04-page-patterns.md](references/04-page-patterns.md)。
6. **拟副标题**，核对标题：参照第 5 节。
7. **自检**：对照第 8 节的清单，再运行 `python3 scripts/lint_zh_text.py`。
8. **交付**：提交改写结果、逐键对照、删减清单、冲突清单和标题变更清单。

## 2. 核心原则（十二条）

1. **说话者是研究者本人。**魔导手册是神秘使自己的研究记录，“你”就是正在阅读的研究者。它在回顾你的发现，而不是教导陌生人。
2. **混用四种开篇。**首页约半数先描写物件，约四分之一讲述发现，其余多为世界观、教学或情绪开场。让相邻研究有不同的起笔。 [CAP_silver.1](references/source-keys.md#k-tc.research_page.CAP_silver.1)、[FOCUSFIRE.1](references/source-keys.md#k-tc.research_page.FOCUSFIRE.1)
3. **四拍结构，可以省略。**引子（来由 / 定义）→ 原理 / 材料 → 用法与数值 → 余韵（局限 / 代价 / 展望 / 平实收束）。内容少就写短，原版也有一句话的页面。
4. **机制写进句子里。**说清操作、条件和结果。比较容量时交代基准，写开关时交代触发后的状态。 [ROD_greatwood.1](references/source-keys.md#k-tc.research_page.ROD_greatwood.1)、[NODESTABILIZER.2](references/source-keys.md#k-tc.research_page.NODESTABILIZER.2)
5. **研究可以留下问题。**写清现有方案已经解决什么，再交代损耗或待验证的改进。 [WANDPEDFOC.1](references/source-keys.md#k-tc.research_page.WANDPEDFOC.1)
6. **幽默克制。**原版大约每四五页才有一处笑点，多放在副标题或段末。最常见的结尾是**平实的补充说明**。邪术类不搞笑，而是阴郁、轻描淡写、自我合理化。
7. **事实保真。**保留每个数值、条件与例外，物品名跟随目标项目。版本或译文之间的数字有出入时，按当前实现核实并报告。 [SCEPTRE.1](references/source-keys.md#k-tc.research_page.SCEPTRE.1)
8. **清除元信息。**不出现“实现说明 / 本模组 / 本移植 / 原作代码 / 服务端 / JEI / 您 / 请”。能改成世界内说法的就改（“你从未找到在生存中制作它的方法”）；玩家必须知道的配置、依赖、仅创造等信息，写成段末的一句**括号旁白**。
9. **副标题是眉批。**副标题绝不等于标题，4～10 字（原版中位数 6），不加句号；不相关的研究不共用副标题，只有真正平行的系列可用平行句式。
10. **标题从简。**单个物品的研究标题要与目标项目的物品名逐字一致。平行系列可用“前缀：项目”。 [FOCUSFROST](references/source-keys.md#k-tc.research_name.FOCUSFROST)
11. **格式正确。**旧式页用 `<BR>`，原生页用 `\n`；占位符（`%s`、`%1$s`）的数量和编号不变；已有 `<IMG>` 原样保留；每个格式码都要用 `§r` 或 `§0` 收尾；使用全角中文标点（原版的半角标点是旧译习惯，不要模仿）。
12. **篇幅贴近原版。**原版单页中位数约 100 字，90% 不超过 175 字。重写时以原文的 1.0～1.5 倍为宜；超过约 250 字就拆页，每个键都必须是完整段落。

## 3. 语气速查

| 分类 / 主题 | 语气 | 样例出处 |
| --- | --- | --- |
| 基本信息 | 引导、留白的世界观 | [NODES.1](references/source-keys.md#k-tc.research_page.NODES.1) |
| 神秘学（法杖、核心） | 工匠的自豪、品评材料 | [CAP_gold.1](references/source-keys.md#k-tc.research_page.CAP_gold.1) |
| 炼金术 | 实验者的冒险 | [ENTROPICPROCESSING.1](references/source-keys.md#k-tc.research_page.ENTROPICPROCESSING.1) |
| 炼化学（设备） | 发明家的满足、展望 | [BELLOWS.2](references/source-keys.md#k-tc.research_page.BELLOWS.2) |
| 傀儡学 | 宠物主人般的吐槽 | [TINYGLASSES.1](references/source-keys.md#k-tc.research_page.TINYGLASSES.1) |
| 邪术 / 禁忌 | 不安、诡秘、自我合理化 | [OCULUS.2](references/source-keys.md#k-tc.research_page.OCULUS.2) |
| 跨模组联动 | 从神秘使的视角看待对方流派 | [thaumicenergistics.research_page.TERESEARCH.1](references/source-keys.md#addon-ThaumicEnergistics-thaumicenergistics.research_page.TERESEARCH.1) |

## 4. 页型速查

| 页型 | 骨架 |
| --- | --- |
| 物件描述 | 这种【物品】【有魔法味道的定义 / 材料性质】。它能够【功能 + 数值】。【限制 / 比较 / 感受】。 |
| 发现叙事 | 【前置经历 / 麻烦 / 观察】。你【发现 / 研究出】【原理】，于是【造出】【物品】。【功能 + 数值】。【局限 / 展望】。 |
| 说明 / 世界观 | 【现象与定义】。写下两种可能成因，指出哪一种更符合观察。结尾标明操作风险。 |
| 属性表 | 【一两句描述】<BR>§l§n【名称】属性§r<BR>§l【属性】:§r 【值】…… |
| 解锁 / 隐藏页 | §n【某升级】解锁§r【可选图标】装有它的【X】现在还能……。 |
| 结构搭建 | §n【搭建 X】§r<BR>【一句来由】<BR>【逐层摆放 + 尺寸 + 材料；示意图逐行 `<BR>`】<BR>【启动方式与消耗】 |
| 补记（追加页） | §n补记§r 或 §n【主题】§r<BR>【机制 + 数值】<BR>【条件 / 例外】。**轮换小标题，避免千篇一律** |
| 使用方式 | §n使用方式§r<BR>作为【位置】佩戴时，【效果 + 数值】。【操作】可【效果】。 |
| 邪术 | 【不安的开场】<BR>【能力与机制】<LINE>【代价】<BR>【自我合理化的余韵】 |
| 元信息旁白 | 段末：（服务器可在配置中关闭此功能。）（此物目前只能在创造模式中取得。） |

## 5. 标题与副标题速查

**副标题的八种写法**。每类后附本体对照键。

- 成语 / 四字格。[NODEPRESERVE](references/source-keys.md#k-tc.research_text.NODEPRESERVE)、[PAVETRAVEL](references/source-keys.md#k-tc.research_text.PAVETRAVEL)、[BELLOWS](references/source-keys.md#k-tc.research_text.BELLOWS)、[VISAMULET](references/source-keys.md#k-tc.research_text.VISAMULET)、[ARMORFORTRESS](references/source-keys.md#k-tc.research_text.ARMORFORTRESS)
- 对仗 / 成对。[RESEARCHER1](references/source-keys.md#k-tc.research_text.RESEARCHER1)、[RESEARCHER2](references/source-keys.md#k-tc.research_text.RESEARCHER2)、[CAP_gold](references/source-keys.md#k-tc.research_text.CAP_gold)、[CAP_silver](references/source-keys.md#k-tc.research_text.CAP_silver)
- 反问 / 惊叹。[ENTROPICPROCESSING](references/source-keys.md#k-tc.research_text.ENTROPICPROCESSING)、[INFERNALFURNACE](references/source-keys.md#k-tc.research_text.INFERNALFURNACE)、[JARVOID](references/source-keys.md#k-tc.research_text.JARVOID)
- 仿警示语 / 冷幽默。[LIQUIDDEATH](references/source-keys.md#k-tc.research_text.LIQUIDDEATH)、[BANNERS](references/source-keys.md#k-tc.research_text.BANNERS)、[GOLEMTALLOW](references/source-keys.md#k-tc.research_text.GOLEMTALLOW)、[ESSENTIARESERVOIR](references/source-keys.md#k-tc.research_text.ESSENTIARESERVOIR)
- 梗的本地化。[FOCUSPORTABLEHOLE](references/source-keys.md#k-tc.research_text.FOCUSPORTABLEHOLE)、[NODETAPPER2](references/source-keys.md#k-tc.research_text.NODETAPPER2)、[HOVERGIRDLE](references/source-keys.md#k-tc.research_text.HOVERGIRDLE)
- 诗意 / 神秘。[NODES](references/source-keys.md#k-tc.research_text.NODES)、[PRIMPEARL](references/source-keys.md#k-tc.research_text.PRIMPEARL)、[CAP_void](references/source-keys.md#k-tc.research_text.CAP_void)
- 悬念半句。[VOIDMETAL](references/source-keys.md#k-tc.research_text.VOIDMETAL)、[ADVANCEDGOLEM](references/source-keys.md#k-tc.research_text.ADVANCEDGOLEM)
- 朴素概括（约三到四成，允许）。[ARCTABLE](references/source-keys.md#k-tc.research_text.ARCTABLE)、[TUBES](references/source-keys.md#k-tc.research_text.TUBES)、[TRAVELTRUNK](references/source-keys.md#k-tc.research_text.TRAVELTRUNK)

**禁止**：

- 副标题等于标题，例如“奥术马达 / 奥术马达”。
- 35 个功能各异的研究共用“失落的知识，重现的遗物”。
- 副标题超过 15 字。
- 副标题句末加句号。
- 冷门或过时的梗。

## 6. 一个完整的改写示例

**改写前**（功能说明，副标题与标题相同，是典型反例）：

> 标题：奥术马达　副标题：奥术马达
>
> 被动提供 256 su，转速 16 rpm。经中继器每 tick 提供的每点 ignis cv 产生 1024 su，此时不再加被动产出；每点 ordo cv 增加 25% 产出，每两点 aer cv 使转速翻倍。每种最多使用 8 cv/t。

**改写后**：

> 标题：奥术马达　副标题：永动机？差不多吧
>
> 机械师们的齿轮与传动轴总让你觉得有些笨拙——它们离不开水车、风车，或是一大堆熊熊燃烧的燃料。直到某天你意识到，节点中继器里流淌的厘魔同样能推动这些齿轮。<BR>即便无人照看，奥术马达也会缓缓转动，提供 256 su 的应力与 16 rpm 的转速。一旦经由中继器为它输送§cIgnis§0厘魔，每 tick 每点 Ignis cv 便能产生 1024 su——此时那份被动产出便不再计入。<BR>额外的§7Ordo§0让运转更加有条不紊：每点 Ordo cv 提升 25% 的产出；而每两点§6Aer§0 cv 则能让转速翻倍。<LINE>每种魔力每 tick 最多只能使用 8 cv，再多它也吞不下了。

**手法**：

- 从神秘使的视角看待机械动力，作为引子。
- 用“你意识到”交代原理。
- 每种魔力单独一句，并加上颜色码。
- 把上限写成拟人化的余韵。
- 所有数值都保留下来：256、16、1024、25%、两点、8。

更多示例见 [examples/rewritten/annotated.md](examples/rewritten/annotated.md)（31 组，含自我批评）和 [examples/original/tc4-annotated.md](examples/original/tc4-annotated.md)（101 个正文引用，附手法注释）。

## 7. 文件索引（按需查阅）

| 何时读 | 文件 |
| --- | --- |
| 想理解“谁在说话、什么口气” | [references/01-voice.md](references/01-voice.md) |
| 安排一页或一个条目的结构、篇幅、拆页 | [references/02-structure.md](references/02-structure.md) |
| 拟标题和副标题 | [references/03-titles-subtitles.md](references/03-titles-subtitles.md)、[examples/original/tc4-research-catalog.md](examples/original/tc4-research-catalog.md)（199 组标题与副标题键） |
| 套用页型模板 | [references/04-page-patterns.md](references/04-page-patterns.md) |
| 查术语、要素、物品译名、数值写法 | [references/05-terminology.md](references/05-terminology.md)、[references/appendix-glossary.md](references/appendix-glossary.md) |
| 确认格式标记、换行、占位符、标点 | [references/06-formatting.md](references/06-formatting.md) |
| 处理元信息、核对事实 | [references/07-facts-and-meta.md](references/07-facts-and-meta.md) |
| 为某个附属写作 | [references/08-addon-voices.md](references/08-addon-voices.md)、[examples/original/addons-annotated.md](examples/original/addons-annotated.md) |
| 批量重写、常见错误、自检清单 | [references/09-workflow.md](references/09-workflow.md) |
| 在 TC4Revival 仓库里工作 | [references/10-tc4revival-notes.md](references/10-tc4revival-notes.md) |
| 原版统计数据（校准篇幅与套路） | [references/appendix-statistics.md](references/appendix-statistics.md) |
| 反例 | [examples/negative/catalog.md](examples/negative/catalog.md) |
| 改写示范与完整语料 | [examples/rewritten/annotated.md](examples/rewritten/annotated.md)、[examples/rewritten/full-corpus/](examples/rewritten/full-corpus/) |
| 模板 | [templates/research-entry.md](templates/research-entry.md)、[templates/rewrite-task-brief.md](templates/rewrite-task-brief.md)、[templates/work-packet.example.json](templates/work-packet.example.json) |
| 写作检查与只读查询 | [scripts/lint_zh_text.py](scripts/lint_zh_text.py)、[scripts/tc4_resources.py](scripts/tc4_resources.py) |

## 8. 交付前自检

- [ ] 事实清单逐条在新文本中，数字、否定、例外一个不少；物品名一致；没有新增机制。
- [ ] 开篇方式有变化；语气与分类相称；玩笑不超过三分之一，邪术类不搞笑。
- [ ] 副标题 ≠ 标题，4～10 字，不加句号；不相关研究不共用副标题。
- [ ] 标题与物品名一致，或使用“前缀：项目”；没有标记或元标签。
- [ ] 页面模式正确（`<BR>` 或 `\n`）；占位符与 `<IMG>` 原样保留；格式码有结束；使用全角标点。
- [ ] 没有元信息词；必要的配置、依赖、仅创造信息已写成括号旁白。
- [ ] 单页不超过约 250 字，超出则拆页；整体篇幅为原文的 1.0～1.5 倍。
- [ ] `python3 scripts/lint_zh_text.py …` 的 ERROR 为 0，WARN 已逐条处理。
- [ ] 交付说明列出：范围、删减项、冲突、标题变更、未验证项（例如未在游戏中查看分页效果）。

```
# 比较改写前后的语言文件（JSON 或 .lang）
python3 scripts/lint_zh_text.py --before old/zh_cn.json --after new/zh_cn.json
# 检查单段文本
python3 scripts/lint_zh_text.py --text "……" --kind page            # 原生页再加 --native
python3 scripts/lint_zh_text.py --text "……" --kind subtitle
```
