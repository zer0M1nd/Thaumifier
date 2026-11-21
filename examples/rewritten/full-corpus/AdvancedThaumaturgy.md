# AdvancedThaumaturgy：改写前后对照

共 47 个键。说明：保留 .originalN 原作译文；.0/.1“实现说明”改为“补记”。标题（含［原作未完成］，与物品名一致）保留。

## advancedthaumaturgy:MERCURIALROD

**`tc.research_text.advancedthaumaturgy:MERCURIALROD`**

- 改写前：水银杖芯
- 改写后：五、五、五合一！

**`advancedthaumaturgy.research.MERCURIALROD.0`**

- 改写前：实现说明：将下界之星、水银和四根银树杖芯注魔，得到能够容纳大量 vis 的水银杖芯。注魔需要大量源质，务必充分准备。
- 改写后：§n补记§r<BR>简单说来：把下界之星、水银和四根银树杖芯一同注魔，便能得到可容纳大量 vis 的水银杖芯。这次注魔吞噬的源质多得吓人，开工之前务必备足储量。

**`advancedthaumaturgy.research.MERCURIALROD.1`**

- 改写前：实现说明：容量取已注册杖芯的最大值，并限制在每种原始要素 500～1000 vis。容量由服务器计算并同步。
- 改写后：§n补记§r<BR>它的容量会向世间已知最好的杖芯看齐——取所有已登记杖芯中的最大值，但始终限制在每种元始要素 500～1000 vis 之间。（容量由服务器计算并同步。）

## advancedthaumaturgy:MERCURIALWAND

**`tc.research_text.advancedthaumaturgy:MERCURIALWAND`**

- 改写前：水银水晶法杖
- 改写后：（几乎）所有的魔力！

**`advancedthaumaturgy.research.MERCURIALWAND.0`**

- 改写前：实现说明：水银杖芯搭配两枚相同杖端，可在奥术工作台装配成水银法杖。它支持六种水晶升级，已有升级会保存在法杖上。
- 改写后：§n补记§r<BR>水银杖芯配上两枚相同的杖端，就能在奥术工作台中装配成水银法杖。它可以接受六种水晶升级，装上的升级会一直保存在法杖上。

**`advancedthaumaturgy.research.MERCURIALWAND.1`**

- 改写前：实现说明：装配支持已注册的杖端，基础消耗为每种原始要素 10 加杖端制作成本；节能效果由提供 vis 的法杖计算。
- 改写后：§n补记§r<BR>世间已登记的杖端都可以用来装配它。基础消耗为每种元始要素 10 vis，再加上杖端本身的制作成本；节能效果则按提供 vis 的那根法杖来计算。

## advancedthaumaturgy:ARCANECRYSTAL

**`tc.research_text.advancedthaumaturgy:ARCANECRYSTAL`**

- 改写前：惰性奥术水晶
- 改写后：世上没有“过强”这回事

**`advancedthaumaturgy.research.ARCANECRYSTAL.0`**

- 改写前：实现说明：用末地石、绿宝石和任意原始碎片制作注魔末地石碎块，再熔炼成惰性奥术水晶。它是法杖升级和微晶器水晶的共同基础。
- 改写后：§n补记§r<BR>用末地石、绿宝石和任意一种元始碎片制作注魔末地石碎块，再将其熔炼，便能得到惰性奥术水晶。往后的法杖升级与微晶器水晶，都要从它开始。

## advancedthaumaturgy:NODEMODIFIER

**`tc.research_text.advancedthaumaturgy:NODEMODIFIER`**

- 改写前：节点修改器
- 改写后：它们并非全都无可救药……

**`advancedthaumaturgy.research.NODEMODIFIER.0`**

- 改写前：实现说明：把瓶中节点放在修改器上方，将源质罐放在附近，节点精华摆在与修改器同高的奥术基座上。基座扫描范围为 X、Z 偏移 -4 到 +3。右击选择操作，悬停查看源质与精华成本。
- 改写后：§n补记§r<BR>把瓶中节点放在修改器上方，源质罐放在附近，节点精华则摆在与修改器同一高度的奥术基座上。基座的扫描范围为 X、Z 偏移 -4 到 +3。右击修改器选择操作，鼠标悬停即可查看所需的源质与精华。

**`advancedthaumaturgy.research.NODEMODIFIER.1`**

- 改写前：实现说明：处理先每秒吸入 1 源质，再每 10 秒消耗 1 精华。增添要素须四份相同精华，节点最多六种要素；提高容量只提高第一种要素 1 点。换走或改变目标节点会中止，已消耗材料不返还。
- 改写后：§n补记§r<BR>处理时，修改器先每秒吸入 1 点源质，再每 10 秒消耗 1 份精华。增添一种要素需要四份相同的精华，节点最多拥有六种要素；提高容量只会让第一种要素提升 1 点。<BR>中途若换走或改变目标节点，处理便会中止，已经消耗的材料也不会返还——节点可不会感谢半途而废的医生。

## advancedthaumaturgy:ETHEREALJAR

**`tc.research_text.advancedthaumaturgy:ETHEREALJAR`**

- 改写前：天域瓶
- 改写后：*破墙而入* 哦耶——！

**`advancedthaumaturgy.research.ETHEREALJAR.0`**

- 改写前：实现说明：用银树木、水银、四只源质罐和任意晶簇合成天域瓶。它可储存 256 源质，吸力比普通同类罐子高 5，支持标签、试管和管道。拆放会保留内容与标签。空瓶最多堆叠四个，有内容或标签的瓶子不能堆叠。
- 改写后：§n补记§r<BR>用银树木、水银、四只源质罐和任意晶簇，即可合成天域瓶。它能储存 256 点源质，吸力比同类的普通罐子高 5，支持标签、试管和管道。拆下再放置时，内容与标签都会保留。<BR>空瓶最多堆叠四个；装有内容或贴了标签的瓶子则不能堆叠——它们实在太沉了。

## advancedthaumaturgy:FERTILIZER

**`tc.research_text.advancedthaumaturgy:FERTILIZER`**

- 改写前：神秘肥料
- 改写后：天哪，是洒——水——器！

**`advancedthaumaturgy.research.FERTILIZER.0`**

- 改写前：实现说明：设备扫描同一高度的 17×17 区域，每两 tick 检查一格。作物或耕地须与设备同高，附近罐子供应 Aqua 与 Herba，各缓存 64。每次催熟消耗半单位 Herba；按原作实现，补水不会扣除 Aqua。
- 改写后：§n补记§r<BR>这台设备会扫描与自身同一高度的 17×17 区域，每两 tick 检查一格，因此作物或耕地必须与它同高。附近的罐子为它供应 Aqua 与 Herba，两者各缓存 64 点。每催熟一次消耗半单位 Herba；奇怪的是，补水时并不会扣除 Aqua——你决定不去深究。

## advancedthaumaturgy:ESSENTIAENGINE

**`tc.research_text.advancedthaumaturgy:ESSENTIAENGINE`**

- 改写前：源质引擎
- 改写后：源质驱动，几乎免费！

**`advancedthaumaturgy.research.ESSENTIAENGINE.0`**

- 改写前：实现说明：将燃料源质转换为 Forge Energy。默认缓存 32000 FE，上方输出 80 FE/t，每点燃料价值提供 1000 FE。Ignis、Ordo 价值 4，其他原始要素 2；Arbor、Herba、Metallum 为 1，Potentia 为 8。红石信号启用主动向上推送。默认从管道输入，可在服务端配置改为吸取附近罐子。
- 改写后：§n补记§r<BR>它把作为燃料的源质转换为 Forge Energy，默认缓存 32000 FE，从上方以 80 FE/t 输出，每点燃料价值提供 1000 FE。<BR>Ignis 与 Ordo 的燃料价值为 4，其他元始要素为 2；Arbor、Herba、Metallum 为 1；Potentia 则高达 8。<BR>通入红石信号时，它会主动向上方推送能量。默认通过管道输入源质，也可以在服务器配置中改为直接吸取附近的罐子。

## advancedthaumaturgy:UPGRADERECHARGE

**`tc.research_text.advancedthaumaturgy:UPGRADERECHARGE`**

- 改写前：充能水晶
- 改写后：它一直走啊走啊走啊……

**`advancedthaumaturgy.research.UPGRADERECHARGE.0`**

- 改写前：实现说明：每 30 tick 随机恢复一种原始要素 1 vis，恢复到容量约 15%。倍增水晶也会影响这次充能。 可通过注魔应用，或在魔杖台上花费每种原始要素 42 基础 vis。相同升级不能重复应用。
- 改写后：§n补记§r<BR>每 30 tick，它会随机为一种元始要素恢复 1 vis，直到约为容量的 15%。倍增水晶也会影响这份充能。<BR>这颗水晶可以通过注魔装进水银法杖，也可以在魔杖台上花费每种元始要素 42 基础 vis 来安装。同一种升级不能重复安装。

## advancedthaumaturgy:UPGRADEDRAIN

**`tc.research_text.advancedthaumaturgy:UPGRADEDRAIN`**

- 改写前：倍增吸取水晶
- 改写后：一份付出，两份收获

**`advancedthaumaturgy.research.UPGRADEDRAIN.0`**

- 改写前：实现说明：吸收 1 原始 vis 可获得 2 vis，源节点只扣 1。容量上限仍然有效。 可通过注魔应用，或在魔杖台上花费每种原始要素 42 基础 vis。相同升级不能重复应用。
- 改写后：§n补记§r<BR>每吸收 1 点元始 vis，法杖便能得到 2 vis，而源节点只被扣去 1 点。不过，容量上限依然有效。<BR>这颗水晶可以通过注魔装进水银法杖，也可以在魔杖台上花费每种元始要素 42 基础 vis 来安装。同一种升级不能重复安装。

## advancedthaumaturgy:UPGRADECOMPOUND

**`tc.research_text.advancedthaumaturgy:UPGRADECOMPOUND`**

- 改写前：复合吸取水晶
- 改写后：化繁为简，以一当十

**`advancedthaumaturgy.research.UPGRADECOMPOUND.0`**

- 改写前：实现说明：从节点吸收复合要素，按要素组成递归拆为原始要素。只有各分量均有空间时才吸收，源节点只扣实际接受的数量。 可通过注魔应用，或在魔杖台上花费每种原始要素 42 基础 vis。相同升级不能重复应用。
- 改写后：§n补记§r<BR>它能从节点中吸收复合要素，并按要素的组成层层拆解为元始要素。只有当每一个组分都有空间容纳时，它才会吸收；源节点也只扣除实际被接受的数量。<BR>这颗水晶可以通过注魔装进水银法杖，也可以在魔杖台上花费每种元始要素 42 基础 vis 来安装。同一种升级不能重复安装。

## advancedthaumaturgy:UPGRADEDISCOUNT

**`tc.research_text.advancedthaumaturgy:UPGRADEDISCOUNT`**

- 改写前：节能水晶
- 改写后：省下的就是赚到的

**`advancedthaumaturgy.research.UPGRADEDISCOUNT.0`**

- 改写前：实现说明：法杖 vis 消耗倍率减少 0.1，与杖端、装备和核心的节能效果共同计算。 可通过注魔应用，或在魔杖台上花费每种原始要素 42 基础 vis。相同升级不能重复应用。
- 改写后：§n补记§r<BR>它会让法杖的 vis 消耗倍率减少 0.1，并与杖端、装备和核心的节能效果一同计算。<BR>这颗水晶可以通过注魔装进水银法杖，也可以在魔杖台上花费每种元始要素 42 基础 vis 来安装。同一种升级不能重复安装。

## advancedthaumaturgy:UPGRADESTABILIZER

**`tc.research_text.advancedthaumaturgy:UPGRADESTABILIZER`**

- 改写前：稳定水晶
- 改写后：蜡烛和头骨？用不着！

**`advancedthaumaturgy.research.UPGRADESTABILIZER.0`**

- 改写前：实现说明：使用装有稳定水晶的水银法杖启动注魔后，将不稳定值限制在初始值的 75%。此处修复了原作标为 WIP 的失效反射写入。 可通过注魔应用，或在魔杖台上花费每种原始要素 42 基础 vis。相同升级不能重复应用。
- 改写后：§n补记§r<BR>用装有稳定水晶的水银法杖启动注魔后，不稳定度会被限制在初始值的 75%。<BR>旧日的手稿里，这颗水晶的设想从未真正奏效；如今你补全了缺失的那一环。<BR>这颗水晶可以通过注魔装进水银法杖，也可以在魔杖台上花费每种元始要素 42 基础 vis 来安装。同一种升级不能重复安装。

## advancedthaumaturgy:UPGRADEPOTENCY

**`tc.research_text.advancedthaumaturgy:UPGRADEPOTENCY`**

- 改写前：效能水晶
- 改写后：效能 V，有何不可？

**`advancedthaumaturgy.research.UPGRADEPOTENCY.0`**

- 改写前：实现说明：法杖核心的效能增加 2，与核心已有的效能升级叠加。 可通过注魔应用，或在魔杖台上花费每种原始要素 42 基础 vis。相同升级不能重复应用。
- 改写后：§n补记§r<BR>它让法杖核心的效能提升 2 级，并与核心原有的效能升级叠加。<BR>这颗水晶可以通过注魔装进水银法杖，也可以在魔杖台上花费每种元始要素 42 基础 vis 来安装。同一种升级不能重复安装。

## advancedthaumaturgy:MINILITHBASE

**`tc.research_text.advancedthaumaturgy:MINILITHBASE`**

- 改写前：微晶器基座
- 改写后：万丈高楼平地起

**`advancedthaumaturgy.research.MINILITHBASE.0`**

- 改写前：实现说明：以黑曜石图腾和底座制作微晶器基座，再在上方装配专用水晶。不同水晶决定设备用途；需要开关的设备可空手右击启停。
- 改写后：§n补记§r<BR>用黑曜石图腾和底座制作微晶器基座，再在上方装配专门的水晶。装上哪种水晶，基座便会成为哪种设备；需要开关的设备，空手右击即可启用或停用。

## advancedthaumaturgy:MINILITHFLUX

**`tc.research_text.advancedthaumaturgy:MINILITHFLUX`**

- 改写前：咒波耗散器
- 改写后：扫除咒波的烦恼

**`advancedthaumaturgy.research.MINILITHFLUX.0`**

- 改写前：实现说明：将附近咒波粘浆转为气体，再消除气体，并有机会回收 Vitium。回收源质可从管道或试管取出。
- 改写后：§n补记§r<BR>它会把附近的咒波粘浆转为气体，再将气体消除，并有一定机会把其中的腐化以 Vitium 的形式回收。回收的源质可以通过管道或试管取出。

## advancedthaumaturgy:MINILITHWATCHFUL

**`tc.research_text.advancedthaumaturgy:MINILITHWATCHFUL`**

- 改写前：警惕之眼
- 改写后：有人在看着

**`advancedthaumaturgy.research.MINILITHWATCHFUL.0`**

- 改写前：实现说明：空手右击启用后保持所在区块运行；停用或拆除会释放加载票据。AT2-30r 实际代码只加载一个区块，旧说明的九区块不适用。
- 改写后：§n补记§r<BR>空手右击启用后，它会让所在的区块保持运行；停用或拆除时，便会松开对区块的掌控。<BR>（你曾以为它能看守周围九个区块。实际观察表明，它只盯得住脚下这一个。）

## advancedthaumaturgy:MINILITHHEAL

**`tc.research_text.advancedthaumaturgy:MINILITHHEAL`**

- 改写前：治疗哨兵
- 改写后：哨兵也懂怜悯

**`advancedthaumaturgy.research.MINILITHHEAL.0`**

- 改写前：实现说明：启用后每 41 tick 为五格内受伤玩家治疗 1 生命值，消耗 1 Sano。由源质管道或试管补充。
- 改写后：§n补记§r<BR>启用之后，它每 41 tick 为五格内受伤的玩家恢复 1 点生命值，每次消耗 1 点 Sano。源质可由管道或试管补充。

## advancedthaumaturgy:MINILITHZAP

**`tc.research_text.advancedthaumaturgy:MINILITHZAP`**

- 改写前：雷电哨兵［原作未完成］
- 改写后：一个未完成的念头

**`advancedthaumaturgy.research.MINILITHZAP.0`**

- 改写前：实现说明：原作仅有配方与研究，没有对应的工作逻辑。本移植保留这一未完成条目，不具备攻击能力。
- 改写后：§n补记§r<BR>你在旧手稿中找到了这件装置的配方和研究记录，却怎么也找不到让它运转起来的方法。它就静静地立在那里，没有任何攻击能力。<BR>也许它的发明者也同样卡在了这一步。

## advancedthaumaturgy:MINILITHFIRE

**`tc.research_text.advancedthaumaturgy:MINILITHFIRE`**

- 改写前：燃烧哨兵
- 改写后：小心火烛

**`advancedthaumaturgy.research.MINILITHFIRE.0`**

- 改写前：实现说明：启用后每 1 Ignis 提供十发火球，命中造成 5 点伤害并点燃目标五秒。火球不会点燃地形。
- 改写后：§n补记§r<BR>启用后，每 1 点 Ignis 可以提供十发火球，每发命中造成 5 点伤害，并让目标燃烧五秒。好在火球不会点燃地形——你的木屋安然无恙。

## advancedthaumaturgy:MINILITHFROST

**`tc.research_text.advancedthaumaturgy:MINILITHFROST`**

- 改写前：冰霜哨兵［原作未完成］
- 改写后：另一个未完成的念头

**`advancedthaumaturgy.research.MINILITHFROST.0`**

- 改写前：实现说明：原作仅有配方与研究，没有对应的工作逻辑。本移植保留这一未完成条目，不具备攻击能力。
- 改写后：§n补记§r<BR>和雷电哨兵一样，旧手稿只留下了这件装置的配方和研究记录，却没有说明它该如何工作。它看起来冷冰冰的，但实际上什么也不会做，没有任何攻击能力。

## advancedthaumaturgy:VOIDCAGE

**`tc.research_text.advancedthaumaturgy:VOIDCAGE`**

- 改写前：法杖核心：空笼
- 改写后：装进口袋里

**`advancedthaumaturgy.research.VOIDCAGE.0`**

- 改写前：实现说明：原作没有生存配方的创造核心。捕获视线内生物需 50 Ordo 和 50 Perditio vis，随后对方块使用可放出。玩家、乘客及载有实体的坐骑不能捕获。释放地点阻塞或生成失败时，生物仍保留在核心内。原作未实现长期腐化计时，收纳的生物不会因存放时间而受伤。
- 改写后：§n补记§r<BR>这枚核心只存在于创造之中——你从未找到在生存中制作它的方法。<BR>捕获视线内的生物需要 50 点 Ordo 与 50 点 Perditio vis，之后对方块使用即可将其放出。玩家、乘客以及载有实体的坐骑都无法捕获。若释放地点被阻塞，或生物未能成功生成，它会继续留在核心之中。<BR>据说被关久了的生物会慢慢被腐化侵蚀，但你从未见到过这种情况：收纳其中的生物不会因存放时间而受伤。

## advancedthaumaturgy:WANDBENCH

**`tc.research_text.advancedthaumaturgy:WANDBENCH`**

- 改写前：魔杖台
- 改写后：修修补补

**`advancedthaumaturgy.research.WANDBENCH.0`**

- 改写前：实现说明：AT2-30r 没有魔杖台的生存配方。左槽放待修改法杖，中间依次放升级水晶、杖芯及两枚同类杖端，右槽放支付 vis 的法杖。费用充足时显示结果。原名称、焦点、升级及 vis 会保留，容量降低时截去超出部分。拆台只掉落真实输入物，不掉预览结果。
- 改写后：§n补记§r<BR>你至今没有找到在生存中制作魔杖台的方法。<BR>左槽放入要修改的法杖，中间依次放升级水晶、杖芯以及两枚同类杖端，右槽放用来支付 vis 的法杖。费用足够时，便会显示改造的结果。<BR>法杖原有的名称、核心、升级与 vis 都会保留；若改造后容量降低，超出的部分会被截去。拆掉魔杖台时只会掉落真实放入的物品，不会掉落预览的结果。
