# 03 标题与副标题

> 按类别浏览 [199 组标题与副标题的语言键](../examples/original/tc4-research-catalog.md)。启用本体资源后可比较同一个键的中英写法。

## 1. 标题（`tc.research_name.*`）

### 1.1 基本规则

1. **与单个物品、方块强相关的研究，标题就是物品名**，须与目标项目显示名逐字一致。 [THAUMOMETER](source-keys.md#k-tc.research_name.THAUMOMETER)、[ARCANEBORE](source-keys.md#k-tc.research_name.ARCANEBORE)、[TRAVELTRUNK](source-keys.md#k-tc.research_name.TRAVELTRUNK)
2. **平行系列可用统一前缀**。现代中文用全角冒号区分系列与项目。
   - 核心系列。 [FOCUSFROST](source-keys.md#k-tc.research_name.FOCUSFROST)、[FOCUSSHOCK](source-keys.md#k-tc.research_name.FOCUSSHOCK)、[FOCUSPORTABLEHOLE](source-keys.md#k-tc.research_name.FOCUSPORTABLEHOLE)
   - 傀儡核心。 [COREHARVEST](source-keys.md#k-tc.research_name.COREHARVEST)、[COREGUARD](source-keys.md#k-tc.research_name.COREGUARD)
   - 升级系列。 [UPGRADEAIR](source-keys.md#k-tc.research_name.UPGRADEAIR)、[UPGRADEORDER](source-keys.md#k-tc.research_name.UPGRADEORDER)
   - 材料加工。 [TRANSIRON](source-keys.md#k-tc.research_name.TRANSIRON)、[PUREGOLD](source-keys.md#k-tc.research_name.PUREGOLD)
3. **概念性研究可用 2～6 字的名词短语**。 [ASPECTS](source-keys.md#k-tc.research_name.ASPECTS)、[NODES](source-keys.md#k-tc.research_name.NODES)、[ALCHEMICALDUPLICATION](source-keys.md#k-tc.research_name.ALCHEMICALDUPLICATION)、[VISPOWER](source-keys.md#k-tc.research_name.VISPOWER)、[CRIMSON](source-keys.md#k-tc.research_name.CRIMSON)、[OUTERREV](source-keys.md#k-tc.research_name.OUTERREV)
4. 标题中**不加**任何格式码、书名号、引号、句末标点，也**不加**元信息标签，如“［原作未完成］”“（联动）”。如果物品名本身带了这类标签，应先考虑修改物品名，再让标题跟随物品名。
5. 原版标题平均 4.8 字。超过 10 字的标题很少见。

### 1.2 何时修改已有标题

**大多数情况下不改。**只有以下情况才修改：

- 标题是功能描述而不是名称，例如“研究网络”只是功能概括，改为“融会贯通”。
- 标题与项目中的物品译名不一致时，以目标语言文件为准。旧版有对应物品时，可核对 [item.FocusPech.name](source-keys.md#k-item.FocusPech.name)。
- 标题冗长，或者带了元信息。

## 2. 副标题（`tc.research_text.*`）

### 2.1 它是做什么的

副标题是标题下的一行小字，相当于研究者在页眉写下的一句**眉批**：点出这项研究的气质、给出一个调侃或悬念、用一个成语概括它的精髓。它是全书最有个性的地方。

### 2.2 硬性规则

| 规则 | 依据 |
| --- | --- |
| **绝不与标题相同** | 原版 199 条中 0 条与标题相同 |
| **长度以 4～10 字为宜**，最长不宜超过 15 字 | 原版中位数 6 字，80% ≤ 8 字；超过 15 字的只有 5 条，且都是有意为之的长句梗 |
| **不含格式码、换行** | 个别附属曾用斜体做强调。 [thaumicenergistics.TEARCANETERM](source-keys.md#addon-ThaumicEnergistics-tc.research_text.thaumicenergistics.TEARCANETERM) |
| 句末一般**不加句号** | 可以用问号、感叹号、省略号：原版问号 10 条、感叹号 7 条、省略号 5 条 |
| **不相关的研究不共用同一句副标题** | 只有真正平行的系列可以共用平行句式（见 2.4） |
| 不含元信息 | 不写“本模组”“联动”“移植”“新增”“测试”等字样 |

### 2.3 原版副标题的手法分类

下表按手法分组。研究标识旁的链接分别定位同一研究的标题和副标题，均可查中英文。

**① 成语 / 四字格**（最常见，4 字副标题占 31%）

| 研究 | 副标题 |
| --- | --- |
| [NODEPRESERVE](source-keys.md#k-tc.research_name.NODEPRESERVE) | [副标题](source-keys.md#k-tc.research_text.NODEPRESERVE) |
| [PAVETRAVEL](source-keys.md#k-tc.research_name.PAVETRAVEL) | [副标题](source-keys.md#k-tc.research_text.PAVETRAVEL) |
| [BELLOWS](source-keys.md#k-tc.research_name.BELLOWS) | [副标题](source-keys.md#k-tc.research_text.BELLOWS) |
| [VISAMULET](source-keys.md#k-tc.research_name.VISAMULET) | [副标题](source-keys.md#k-tc.research_text.VISAMULET) |
| [ARMORFORTRESS](source-keys.md#k-tc.research_name.ARMORFORTRESS) | [副标题](source-keys.md#k-tc.research_text.ARMORFORTRESS) |
| [FOCUSWARDING](source-keys.md#k-tc.research_name.FOCUSWARDING) | [副标题](source-keys.md#k-tc.research_text.FOCUSWARDING) |
| [GOGGLES](source-keys.md#k-tc.research_name.GOGGLES) | [副标题](source-keys.md#k-tc.research_text.GOGGLES) |
| [COREFILL](source-keys.md#k-tc.research_name.COREFILL) | [副标题](source-keys.md#k-tc.research_text.COREFILL) |
| [CORESORTING](source-keys.md#k-tc.research_name.CORESORTING) | [副标题](source-keys.md#k-tc.research_text.CORESORTING) |

**② 对仗 / 双关 / 成对**

| 研究 | 副标题 |
| --- | --- |
| [RESEARCHER1](source-keys.md#k-tc.research_name.RESEARCHER1) / [RESEARCHER2](source-keys.md#k-tc.research_name.RESEARCHER2) | [副标题](source-keys.md#k-tc.research_text.RESEARCHER1) / [副标题](source-keys.md#k-tc.research_text.RESEARCHER2) |
| [CAP_gold](source-keys.md#k-tc.research_name.CAP_gold) / [CAP_silver](source-keys.md#k-tc.research_name.CAP_silver) | [副标题](source-keys.md#k-tc.research_text.CAP_gold) / [副标题](source-keys.md#k-tc.research_text.CAP_silver) |
| [HOVERHARNESS](source-keys.md#k-tc.research_name.HOVERHARNESS) / [HOVERGIRDLE](source-keys.md#k-tc.research_name.HOVERGIRDLE) | [副标题](source-keys.md#k-tc.research_text.HOVERHARNESS) / [副标题](source-keys.md#k-tc.research_text.HOVERGIRDLE) |
| [TINYBOWTIE](source-keys.md#k-tc.research_name.TINYBOWTIE) / [TINYFEZ](source-keys.md#k-tc.research_name.TINYFEZ) | [副标题](source-keys.md#k-tc.research_text.TINYBOWTIE) / [副标题](source-keys.md#k-tc.research_text.TINYFEZ) |
| [RUNICARMOR](source-keys.md#k-tc.research_name.RUNICARMOR) / [RUNICAUGMENTATION](source-keys.md#k-tc.research_name.RUNICAUGMENTATION) | [副标题](source-keys.md#k-tc.research_text.RUNICARMOR) / [副标题](source-keys.md#k-tc.research_text.RUNICAUGMENTATION) |

**③ 反问 / 设问 / 惊叹**

| 研究 | 副标题 |
| --- | --- |
| [ENTROPICPROCESSING](source-keys.md#k-tc.research_name.ENTROPICPROCESSING) | [副标题](source-keys.md#k-tc.research_text.ENTROPICPROCESSING) |
| [INFERNALFURNACE](source-keys.md#k-tc.research_name.INFERNALFURNACE) | [副标题](source-keys.md#k-tc.research_text.INFERNALFURNACE) |
| [JARVOID](source-keys.md#k-tc.research_name.JARVOID) | [副标题](source-keys.md#k-tc.research_text.JARVOID) |
| [BOTTLETAINT](source-keys.md#k-tc.research_name.BOTTLETAINT) | [副标题](source-keys.md#k-tc.research_text.BOTTLETAINT) |
| [SINSTONE](source-keys.md#k-tc.research_name.SINSTONE) | [副标题](source-keys.md#k-tc.research_text.SINSTONE) |
| [ESSENTIACRYSTAL](source-keys.md#k-tc.research_name.ESSENTIACRYSTAL) | [副标题](source-keys.md#k-tc.research_text.ESSENTIACRYSTAL) |
| [ARCANEEAR](source-keys.md#k-tc.research_name.ARCANEEAR) | [副标题](source-keys.md#k-tc.research_text.ARCANEEAR) |

**④ 冷幽默 / 仿警示语**

| 研究 | 副标题 |
| --- | --- |
| [LIQUIDDEATH](source-keys.md#k-tc.research_name.LIQUIDDEATH) | [副标题](source-keys.md#k-tc.research_text.LIQUIDDEATH) |
| [BANNERS](source-keys.md#k-tc.research_name.BANNERS) | [副标题](source-keys.md#k-tc.research_text.BANNERS) |
| [GOLEMTALLOW](source-keys.md#k-tc.research_name.GOLEMTALLOW) | [副标题](source-keys.md#k-tc.research_text.GOLEMTALLOW) |
| [ESSENTIARESERVOIR](source-keys.md#k-tc.research_name.ESSENTIARESERVOIR) | [副标题](source-keys.md#k-tc.research_text.ESSENTIARESERVOIR) |
| [TINYVISOR](source-keys.md#k-tc.research_name.TINYVISOR) | [副标题](source-keys.md#k-tc.research_text.TINYVISOR) |
| [COREBUTCHER](source-keys.md#k-tc.research_name.COREBUTCHER) | [副标题](source-keys.md#k-tc.research_text.COREBUTCHER) |

**⑤ 流行文化 / 网络梗**（中文译者多做了本地化替换）

| 研究 | 副标题 |
| --- | --- |
| [NODETAPPER2](source-keys.md#k-tc.research_name.NODETAPPER2) | [副标题](source-keys.md#k-tc.research_text.NODETAPPER2) |
| [FOCUSPORTABLEHOLE](source-keys.md#k-tc.research_name.FOCUSPORTABLEHOLE) | [副标题](source-keys.md#k-tc.research_text.FOCUSPORTABLEHOLE) |
| [ENTEROUTER](source-keys.md#k-tc.research_name.ENTEROUTER) | [副标题](source-keys.md#k-tc.research_text.ENTEROUTER) |
| [FOCUSFROST](source-keys.md#k-tc.research_name.FOCUSFROST) | [副标题](source-keys.md#k-tc.research_text.FOCUSFROST) |
| [GOLEMWOOD](source-keys.md#k-tc.research_name.GOLEMWOOD) | [副标题](source-keys.md#k-tc.research_text.GOLEMWOOD) |
| [MIRROR](source-keys.md#k-tc.research_name.MIRROR) | [副标题](source-keys.md#k-tc.research_text.MIRROR) |
| [PRIMNODE](source-keys.md#k-tc.research_name.PRIMNODE) | [副标题](source-keys.md#k-tc.research_text.PRIMNODE) |

**⑥ 诗意 / 神秘 / 古雅**

| 研究 | 副标题 |
| --- | --- |
| [NODES](source-keys.md#k-tc.research_name.NODES) | [副标题](source-keys.md#k-tc.research_text.NODES) |
| [ASPECTS](source-keys.md#k-tc.research_name.ASPECTS) | [副标题](source-keys.md#k-tc.research_text.ASPECTS) |
| [PRIMPEARL](source-keys.md#k-tc.research_name.PRIMPEARL) | [副标题](source-keys.md#k-tc.research_text.PRIMPEARL) |
| [CAP_void](source-keys.md#k-tc.research_name.CAP_void) | [副标题](source-keys.md#k-tc.research_text.CAP_void) |
| [ELDRITCHMINOR](source-keys.md#k-tc.research_name.ELDRITCHMINOR) | [副标题](source-keys.md#k-tc.research_text.ELDRITCHMINOR) |
| [ELDRITCHMAJOR](source-keys.md#k-tc.research_name.ELDRITCHMAJOR) | [副标题](source-keys.md#k-tc.research_text.ELDRITCHMAJOR) |
| [ELEMENTALSWORD](source-keys.md#k-tc.research_name.ELEMENTALSWORD) | [副标题](source-keys.md#k-tc.research_text.ELEMENTALSWORD) |
| [ELEMENTALSHOVEL](source-keys.md#k-tc.research_name.ELEMENTALSHOVEL) | [副标题](source-keys.md#k-tc.research_text.ELEMENTALSHOVEL) |
| [ELEMENTALHOE](source-keys.md#k-tc.research_name.ELEMENTALHOE) | [副标题](source-keys.md#k-tc.research_text.ELEMENTALHOE) |

**⑦ 带悬念的半句话**

| 研究 | 副标题 |
| --- | --- |
| [VOIDMETAL](source-keys.md#k-tc.research_name.VOIDMETAL) | [副标题](source-keys.md#k-tc.research_text.VOIDMETAL) |
| [ADVANCEDGOLEM](source-keys.md#k-tc.research_name.ADVANCEDGOLEM) | [副标题](source-keys.md#k-tc.research_text.ADVANCEDGOLEM) |
| [BONEBOW](source-keys.md#k-tc.research_name.BONEBOW) | [副标题](source-keys.md#k-tc.research_text.BONEBOW) |
| [OUTERREV](source-keys.md#k-tc.research_name.OUTERREV) | [副标题](source-keys.md#k-tc.research_text.OUTERREV) |

**⑧ 朴素的功能概括**（原版中约占三到四成，是允许的）

| 研究 | 副标题 |
| --- | --- |
| [ARCTABLE](source-keys.md#k-tc.research_name.ARCTABLE) | [副标题](source-keys.md#k-tc.research_text.ARCTABLE) |
| [TUBES](source-keys.md#k-tc.research_name.TUBES) | [副标题](source-keys.md#k-tc.research_text.TUBES) |
| [CENTRIFUGE](source-keys.md#k-tc.research_name.CENTRIFUGE) | [副标题](source-keys.md#k-tc.research_text.CENTRIFUGE) |
| [LAMPGROWTH](source-keys.md#k-tc.research_name.LAMPGROWTH) | [副标题](source-keys.md#k-tc.research_text.LAMPGROWTH) |
| [VISCHARGERELAY](source-keys.md#k-tc.research_name.VISCHARGERELAY) | [副标题](source-keys.md#k-tc.research_text.VISCHARGERELAY) |
| [CORELIQUID](source-keys.md#k-tc.research_name.CORELIQUID) | [副标题](source-keys.md#k-tc.research_text.CORELIQUID) |

朴素的副标题可以点明功能，也可以选用一个容易想象的场景。 [COREHARVEST](source-keys.md#k-tc.research_text.COREHARVEST)、[CORELUMBER](source-keys.md#k-tc.research_text.CORELUMBER)、[TRAVELTRUNK](source-keys.md#k-tc.research_text.TRAVELTRUNK)

### 2.4 平行系列

真正平行的系列可以使用平行句式，原版就是这样做的：

| 系列 | 副标题 |
| --- | --- |
| 元素杖柄 | [ROD_obsidian](source-keys.md#k-tc.research_text.ROD_obsidian)、[ROD_bone](source-keys.md#k-tc.research_text.ROD_bone)、[ROD_blaze](source-keys.md#k-tc.research_text.ROD_blaze)、[ROD_ice](source-keys.md#k-tc.research_text.ROD_ice)、[ROD_quartz](source-keys.md#k-tc.research_text.ROD_quartz)、[ROD_reed](source-keys.md#k-tc.research_text.ROD_reed) |
| 元素杖芯 | [ROD_obsidian_staff](source-keys.md#k-tc.research_text.ROD_obsidian_staff)、[ROD_bone_staff](source-keys.md#k-tc.research_text.ROD_bone_staff) |
| 嬗变术 | [TRANSIRON](source-keys.md#k-tc.research_text.TRANSIRON)、[TRANSGOLD](source-keys.md#k-tc.research_text.TRANSGOLD) |
| 晶簇化 | [PUREIRON](source-keys.md#k-tc.research_text.PUREIRON)、[PUREGOLD](source-keys.md#k-tc.research_text.PUREGOLD) |
| 傀儡升级 | [UPGRADEAIR](source-keys.md#k-tc.research_text.UPGRADEAIR)、[UPGRADEEARTH](source-keys.md#k-tc.research_text.UPGRADEEARTH)、[UPGRADEFIRE](source-keys.md#k-tc.research_text.UPGRADEFIRE)、[UPGRADEWATER](source-keys.md#k-tc.research_text.UPGRADEWATER)、[UPGRADEORDER](source-keys.md#k-tc.research_text.UPGRADEORDER)、[UPGRADEENTROPY](source-keys.md#k-tc.research_text.UPGRADEENTROPY) |
| 三种面具 | [MASKANGRYGHOST](source-keys.md#k-tc.research_text.MASKANGRYGHOST)、[MASKSIPPINGFIEND](source-keys.md#k-tc.research_text.MASKSIPPINGFIEND)、[MASKGRINNINGDEVIL](source-keys.md#k-tc.research_text.MASKGRINNINGDEVIL) |

**判断标准**：如果两个研究只有一个变量不同（元素、金属、阶数），平行句式是好选择。只要功能、玩法、物品类别不同，就必须写各自的副标题。

### 2.5 英文副标题如何译成中文

| 策略 | 例子 | 何时使用 |
| --- | --- | --- |
| 直译 | [NODES](source-keys.md#k-tc.research_text.NODES)、[ORE](source-keys.md#k-tc.research_text.ORE) | 原文本身简洁有力 |
| 成语替换 | [NODEPRESERVE](source-keys.md#k-tc.research_text.NODEPRESERVE)、[PAVETRAVEL](source-keys.md#k-tc.research_text.PAVETRAVEL) | 英文是俗语、平铺直叙 |
| 梗的本地化 | [HOVERGIRDLE](source-keys.md#k-tc.research_text.HOVERGIRDLE)、[FOCUSPORTABLEHOLE](source-keys.md#k-tc.research_text.FOCUSPORTABLEHOLE) | 英文用了英语圈的梗 |
| 保留名梗 | [ENTEROUTER](source-keys.md#k-tc.research_text.ENTEROUTER) | 梗本身在中文读者中也有认知度 |
| 意境重写 | [ELEMENTALSWORD](source-keys.md#k-tc.research_text.ELEMENTALSWORD)、[ELEMENTALHOE](source-keys.md#k-tc.research_text.ELEMENTALHOE) | 配合中文的命名体系（如神话名的元素工具） |
| 绕口令照搬 | [GOLEMWOOD](source-keys.md#k-tc.research_text.GOLEMWOOD) | 结构本身就是笑点 |

翻译附属任务中作者提供的英文副标题时，先判断原句笑点或信息重心，再决定如何在中文中表达。历史附属索引只标注出处。

### 2.6 拟写新副标题的步骤

1. **找一个抓手**，从以下几类中选一个：
   - 它最核心的功能。[副标题出处](source-keys.md#k-tc.research_text.TRAVELTRUNK)
   - 材料或外观。[副标题出处](source-keys.md#k-tc.research_text.ENCHFABRIC)
   - 使用者的心情。[副标题出处](source-keys.md#k-tc.research_text.RUNICHEALING)
   - 它的危险。[副标题出处](source-keys.md#k-tc.research_text.LIQUIDDEATH)
   - 它与前作或同类的关系。[副标题出处](source-keys.md#k-tc.research_text.CAP_copper)
   - 一个现成的成语或名句
2. **选手法**：成语、反问、警示、梗、诗意、朴素概括。
3. **压缩到 4～10 字**，读一遍。
4. **自检**：
   - 是否与标题相同或只是同义改写？比如标题“法杖充能器”配副标题“为法杖充能的装置”就不合格。
   - 是否与相邻研究重复？
   - 是否需要特定圈子的知识才能看懂？

### 2.7 重写实践中拟写的副标题（供参考）

下面是在 TC4Revival 中重写现代附属研究时拟写的副标题，配合 [examples/rewritten/](../examples/rewritten/) 阅读：

| 研究 | 原副标题（反例） | 重写后 |
| --- | --- | --- |
| 奥术马达 | 奥术马达（与标题相同） | 永动机？差不多吧 |
| 灵魂核心 | 让机械借用你的知识 | 灵魂出窍 |
| 法杖核心：动力 | 法杖核心：动力（与标题相同） | 转起来！ |
| 法杖核心：挪移 | 法杖核心：挪移（与标题相同） | 愚公移山，弹指之间 |
| 神秘机壳 | 神秘机壳（与标题相同） | 万丈高楼的第一块砖 |
| 奥术烈焰人燃烧室 | 同标题 | 笼中之火 |
| 奥术动力磁铁 | 同标题 | 异性相吸，结构亦然 |
| 神秘采血术（奥法献祭学） | 更高效地收集生命精华 | 血，统统收集起来！ · [英文出处](source-keys.md#addon-ArcaneArteries-tc.research_text.DAGGER) |
| 怪物之血 | 让怪物为血祭坛献出生命 | 切切剁剁，宝贝！ · [英文出处](source-keys.md#addon-ArcaneArteries-tc.research_text.SACRIFICEDAGGER) |
| 虚空钻头（奥法工程学） | 不受磨损的钻头 | 洞上加洞 · [英文出处](source-keys.md#addon-ArcaneEngineering-ArcaneEngineering.research_text.DRILLVOID) |
| 钢杖端 | 有序的合金 | 不是蓝钢 · [英文出处](source-keys.md#addon-ArcaneEngineering-ArcaneEngineering.research_text.CAP_steel) |
| 符文石（失落遗物学） | 失落的知识，重现的遗物（35 条共用） | 史上最强的雨伞 · [英文出处](source-keys.md#addon-ForgottenRelics-fr.tag.WeatherStone) |
| 纷争之书 | 同上 | 记得想好卡进墙里怎么办 |
| 初探污染（神秘基础学） | 危险的实验 | 饮鸩止渴 |
| 灌注笔与墨（神秘工匠） | 八倍墨水 | 墨水管够 |
| 时间认知（神秘远征） | 时间认知（与标题相同） | 逝者如斯 |
| 循环认知 | 同标题 | 周而复始 |
| T1：阶段突破（神秘旅程） | 制作法杖，完成研究，迈向新的阶段（T1～T6 共用） | 千里之行，始于足下（T2～T6 依次为：渐入佳境、登堂入室、更上一层楼、炉火纯青、凭虚御风） |
| 神秘捕蜂网 | 神秘养蜂器具（3 条共用） | 温柔地抓一只蜜蜂 |
| 浅墓精华 | 蜂巢中的炼金术（12 条共用） | 离坟墓只有一步之遥 |
| 研究网络 → 融会贯通（本体） | 将思路连成路径 | 牵一发而动全身 |

## 3. 速查清单

- [ ] 标题与物品名逐字一致；系列标题用“前缀：项目”。
- [ ] 标题不含标记或元信息。
- [ ] 副标题 ≠ 标题，也不是标题的同义改写。
- [ ] 副标题 4～10 字，最长不超过 15 字。
- [ ] 不相关的研究不共用副标题；平行系列使用平行句式。
- [ ] 句末不加句号；问号、感叹号、省略号可用。
- [ ] 有原作英文副标题时，按原作意译。
- [ ] 梗要大众化、不易过时；邪术类用诗意或不安的短句。
