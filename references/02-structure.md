# 02 条目与页面结构

> 本篇介绍研究条目与单页的起承转合、篇幅和拆页方式。例句以原包语言键引用。

## 1. 研究条目的组成

一个研究条目（research）在魔导手册中由以下部分组成：

| 部分 | 语言键（TC4 惯例） | 说明 |
| --- | --- | --- |
| 标题 | `tc.research_name.<KEY>` | 研究树上悬停时显示，也是书页的大标题 |
| 副标题 | `tc.research_text.<KEY>` | 标题下的一行小字，见 [03-titles-subtitles.md](03-titles-subtitles.md) |
| 正文页 | `tc.research_page.<KEY>.1`、`.2`…… | 一个键一段文字；附属常用自己的前缀，如 `fr.text.X.1`、`Automagy.research_page.X.1` |
| 配方页 | 无文字 | 奥术合成、坩埚、注魔、普通合成、多方块结构等 |
| 隐藏页 | 正文键，但只在完成另一项研究后出现 | 原版用于“升级解锁”，例如收获核心在完成秩序升级研究后显示的补充页 |
| 要素页 | 无文字 | 由玩家已知要素自动生成（仅“魔力要素”条目） |

页面顺序的惯例：**先概念，后操作，再细节与注意事项**；配方页穿插在相关叙述之后。例如注魔条目是“原理 → 搭建 → 过程 → 风险 → 降低风险”，共 5 页；奥术钻探机是“介绍与核心槽 → 镐槽与安装 → 燃料加速”，共 3 页。

## 2. 单页的四拍结构

一页正文通常包含以下四拍，但**不必每拍都有**：

1. **引子**：为什么会有这件东西？来由、动机、灵感、前置研究，或者直接给物品一个生动的定义。
2. **原理 / 材料**：它是怎么做到的？材料的魔法性质、研究者的推理。
3. **用法与数值**：怎么用、能做什么、具体多少。
4. **余韵**：局限、代价、注意事项、展望，或一句俏皮话。

以早期法杖研究为例，第一页由实验引出加工原理，第二页写出按键操作与结果。

[FOCUSFIRE.1](source-keys.md#k-tc.research_page.FOCUSFIRE.1)

[FOCUSFIRE.2](source-keys.md#k-tc.research_page.FOCUSFIRE.2)

短条目可能只有一两拍：

[CAP_gold.1](source-keys.md#k-tc.research_page.CAP_gold.1)

[TINYHAMMER.1](source-keys.md#k-tc.research_page.TINYHAMMER.1)

**原则**：内容少时就写短。不要为了凑满“四拍”而注水。

## 3. 开篇手法目录

| 手法 | 正文出处 |
| --- | --- |
| 承接前置研究 | [GOGGLES.1](source-keys.md#k-tc.research_page.GOGGLES.1) |
| 动机 / 麻烦 | [FOCUSPOUCH.1](source-keys.md#k-tc.research_page.FOCUSPOUCH.1) |
| 亲身经历 | [FOCUSHELLBAT.1](source-keys.md#k-tc.research_page.FOCUSHELLBAT.1) |
| 偶然发现 | [WARDEDARCANA.1](source-keys.md#k-tc.research_page.WARDEDARCANA.1) |
| 物品定义 | [NITOR.1](source-keys.md#k-tc.research_page.NITOR.1)、[ALUMENTUM.1](source-keys.md#k-tc.research_page.ALUMENTUM.1) |
| 宏观陈述 | [VISPOWER.1](source-keys.md#k-tc.research_page.VISPOWER.1) |
| 对比旧物 | [ADVALCHEMYFURNACE.1](source-keys.md#k-tc.research_page.ADVALCHEMYFURNACE.1) |
| 反问 / 惊叹 | [FOCUSPRIMAL.1](source-keys.md#k-tc.research_page.FOCUSPRIMAL.1)、[BOTTLETAINT.1](source-keys.md#k-tc.research_page.BOTTLETAINT.1) |
| 梦境 / 直觉 | [VOIDMETAL.1](source-keys.md#k-tc.research_page.VOIDMETAL.1) |
| 情绪 / 心境 | [SANITYCHECK.1](source-keys.md#k-tc.research_page.SANITYCHECK.1)、[PRIMPEARL.1](source-keys.md#k-tc.research_page.PRIMPEARL.1) |
| 步骤列表 | [JARBRAIN.1](source-keys.md#k-tc.research_page.JARBRAIN.1) |

## 4. 中段：把机制写进叙述

原版写机制非常具体：按键、数值、范围、条件都会写清楚，但写在自然句子里。常用句式：

| 句式 | 正文出处 |
| --- | --- |
| 只需……就能…… | [THAUMONOMICON.1](source-keys.md#k-tc.research_page.THAUMONOMICON.1) |
| 手持 X 右击 Y | [JARLABEL.1](source-keys.md#k-tc.research_page.JARLABEL.1) |
| 按住潜行（键） | [ELEMENTALAXE.2](source-keys.md#k-tc.research_page.ELEMENTALAXE.2) |
| 首先……其次……最后…… | [SCEPTRE.1](source-keys.md#k-tc.research_page.SCEPTRE.1) |
| 数值直给 | [ROD_silverwood.1](source-keys.md#k-tc.research_page.ROD_silverwood.1)、[DISTILESSENTIA.2](source-keys.md#k-tc.research_page.DISTILESSENTIA.2) |
| 相对比较 | [ROD_greatwood.1](source-keys.md#k-tc.research_page.ROD_greatwood.1)、[NODETAPPER2.1](source-keys.md#k-tc.research_page.NODETAPPER2.1)、[ELEMENTALPICK.1](source-keys.md#k-tc.research_page.ELEMENTALPICK.1) |
| 条件 → 结果 | [RUNICARMOR.1](source-keys.md#k-tc.research_page.RUNICARMOR.1)、[LAMPFERTILITY.1](source-keys.md#k-tc.research_page.LAMPFERTILITY.1) |
| 优先级链 | [JARVOID.1](source-keys.md#k-tc.research_page.JARVOID.1) |
| 红石控制 | [NODESTABILIZER.2](source-keys.md#k-tc.research_page.NODESTABILIZER.2)、[LEVITATOR.1](source-keys.md#k-tc.research_page.LEVITATOR.1) |
| 冷却 / 限制 | [RUNICKINETIC.1](source-keys.md#k-tc.research_page.RUNICKINETIC.1)、[FOCALMANIPULATION.1](source-keys.md#k-tc.research_page.FOCALMANIPULATION.1) |
| 状态说明 | [PAVEWARD.2](source-keys.md#k-tc.research_page.PAVEWARD.2) |

技巧：

- 数字后可以附上比较基准，帮助读者判断容量差距。 [ROD_greatwood.1](source-keys.md#k-tc.research_page.ROD_greatwood.1)
- 操作和效果可以写成一对，交代指定工具能收回什么。 [GOLEMSTRAW.1](source-keys.md#k-tc.research_page.GOLEMSTRAW.1)
- **多项特性用“首先、其次、此外、最后”串起来**，比罗列分号更自然。
- **条件多时分段**：每个 `<BR>` 讲一件事。

## 5. 收尾手法目录

| 手法 | 正文出处 |
| --- | --- |
| 局限 + 希望 | [COREHARVEST.1](source-keys.md#k-tc.research_page.COREHARVEST.1) |
| 局限 + 好的开端 | [WANDPEDFOC.1](source-keys.md#k-tc.research_page.WANDPEDFOC.1) |
| 代价警示 | [VISPOWER.2](source-keys.md#k-tc.research_page.VISPOWER.2)、[VISPOWER.5](source-keys.md#k-tc.research_page.VISPOWER.5) |
| 回来查阅 | [ARCANELAMP.1](source-keys.md#k-tc.research_page.ARCANELAMP.1) |
| 冷笑话 / 吐槽 | [FOCUSHELLBAT.1](source-keys.md#k-tc.research_page.FOCUSHELLBAT.1)、[MASKANGRYGHOST.1](source-keys.md#k-tc.research_page.MASKANGRYGHOST.1)、[PRIMNODE.1](source-keys.md#k-tc.research_page.PRIMNODE.1) |
| 不安的疑问 | [MASKSIPPINGFIEND.1](source-keys.md#k-tc.research_page.MASKSIPPINGFIEND.1)、[PRIMPEARL.2](source-keys.md#k-tc.research_page.PRIMPEARL.2) |
| 号召 / 伏笔 | [PRIMPEARL.2](source-keys.md#k-tc.research_page.PRIMPEARL.2)、[OUTERREV.1](source-keys.md#k-tc.research_page.OUTERREV.1) |
| 平实收束 | [ELEMENTALPICK.2](source-keys.md#k-tc.research_page.ELEMENTALPICK.2) |

再次提醒：**平实收束是最常见的结尾**，不必每页都要“有梗”。

## 6. 段落节奏与小标题

- `<BR>` 换行：一行一个意思。原版平均每页 1.7 个 `<BR>`。
- `<LINE>` 用于在两个话题间加分隔线。 [CRUCIBLE.4](source-keys.md#k-tc.research_page.CRUCIBLE.4)
- `§n【小标题】§r` 适合在页内划分升级效果或数据小节。 [COREHARVEST.2](source-keys.md#k-tc.research_page.COREHARVEST.2)
- 原版在小标题前加若干空格实现“居中”，那是旧字体排版的产物；在现代原生字体下不要模仿。

## 7. 篇幅与拆页

数据（详见 [appendix-statistics.md](appendix-statistics.md)）：

- 单页中位数约 **100 字**，90% 不超过 **175 字**，最长约 250 字。
- 138 个研究只有 1 段正文，38 个有 2 段；超过 3 段的只有教学类和多升级的傀儡核心。

规则：

1. **一页一个主题**。机制密集的现代内容（结构搭建、按键、配置）应拆成“叙事页 + 补充页”，而不是把所有东西塞进一个 400 字的段落。
2. **每页自足**。旧式固定版面有时在句中换键，现代自动分页时应让每个键都能独立读通。 [PRIMALCRUSHER.1](source-keys.md#k-tc.research_page.PRIMALCRUSHER.1)、[PRIMALCRUSHER.2](source-keys.md#k-tc.research_page.PRIMALCRUSHER.2)
3. **重写时的篇幅**：保留全部事实的前提下，以原文的 1.0–1.5 倍为宜。超过 2 倍通常意味着注水，或者应当拆页。
4. **太短也不行**：只有“将虞美人转化为水银花。”这样一句的页面，至少要补上来由或判断（参见 [examples/negative/catalog.md](../examples/negative/catalog.md)）。但原版也确有一句话的页面（如金杖端），只要这句话本身有味道即可。

## 8. 系列条目

原版对**平行系列**大量使用固定骨架，这是允许的，也是风格的一部分：

| 系列 | 标题引用 | 副标题引用 | 正文引用 |
| --- | --- | --- | --- |
| 嬗变术 | [标题](source-keys.md#k-tc.research_name.TRANSIRON) | [副标题](source-keys.md#k-tc.research_text.TRANSIRON) | [正文](source-keys.md#k-tc.research_page.TRANSIRON.1) |
| 晶簇化 | [标题](source-keys.md#k-tc.research_name.PUREGOLD) | [副标题](source-keys.md#k-tc.research_text.PUREGOLD) | [正文](source-keys.md#k-tc.research_page.PUREGOLD.1) |
| 元素杖柄 | [标题](source-keys.md#k-tc.research_name.ROD_obsidian) | [副标题](source-keys.md#k-tc.research_text.ROD_obsidian) | [正文](source-keys.md#k-tc.research_page.ROD_obsidian.1) |
| 元素杖芯 | [标题](source-keys.md#k-tc.research_name.ROD_obsidian_staff) | [副标题](source-keys.md#k-tc.research_text.ROD_obsidian_staff) | [正文](source-keys.md#k-tc.research_page.ROD_obsidian_staff.1) |
| 傀儡材质 | [标题](source-keys.md#k-tc.research_name.GOLEMSTRAW) | [副标题](source-keys.md#k-tc.research_text.GOLEMSTRAW) | [正文](source-keys.md#k-tc.research_page.GOLEMSTRAW.1) |
| 傀儡升级 | [标题](source-keys.md#k-tc.research_name.UPGRADEAIR) | [副标题](source-keys.md#k-tc.research_text.UPGRADEAIR) | [正文](source-keys.md#k-tc.research_page.UPGRADEAIR.1) |
| 面具 | [标题](source-keys.md#k-tc.research_name.MASKANGRYGHOST) | [副标题](source-keys.md#k-tc.research_text.MASKANGRYGHOST) | [正文](source-keys.md#k-tc.research_page.MASKANGRYGHOST.1) |

判断标准：

- **真正平行**（只有一两个变量不同）的系列，可以共用骨架和平行的副标题。
- **不平行**的研究（功能各异、只是同属一个模组或分类）**不得**共用同一句副标题。反例：35 件功能各异的遗物都用“失落的知识，重现的遗物”；12 个养蜂研究都用“蜂巢中的炼金术”。
- 系列正文可以同骨架，但如果每一条有独特的事实（如不同的阶段意义），就要让措辞也有变化。

## 9. 隐藏页 / 解锁页

原版用隐藏页描述“完成另一项研究后才知道的用法”，格式固定：

[COREHARVEST.2](source-keys.md#k-tc.research_page.COREHARVEST.2)

要点：一个小标题、可选的图标，以及一两句“它现在还能做什么”。在补充现代联动内容时，也可以借用这种格式，比如“§n……联动§r”“§n补记§r”。

## 10. 教学页

“研究”条目是原版唯一的长篇教学。它的写法：

- 首页用编号预告完整流程。 [RESEARCH.1](source-keys.md#k-tc.research_page.RESEARCH.1)
- 具体步骤单独成页，在小标题里保留编号。 [RESEARCH.2](source-keys.md#k-tc.research_page.RESEARCH.2)
- 结合插图（`<IMG>`），并用 `§l1§r`、`§l2§r` 等编号指向图中区域。
- 告诉读者能通过哪些画面变化判断操作结果，顺带加入一点设定。 [RESEARCH.2](source-keys.md#k-tc.research_page.RESEARCH.2)

为新界面功能写说明（如研究台的搜索、自动连线）时，可以参照这种写法：把 UI 操作说成研究者养成的习惯或掌握的技巧，再把按键写清楚。
