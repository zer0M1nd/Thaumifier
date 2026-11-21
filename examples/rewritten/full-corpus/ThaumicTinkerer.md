# ThaumicTinkerer：改写前后对照

共 7 个键。译名优先对齐项目物品，本体历史术语可查 [FOCUSPOUCH](../../../references/source-keys.md#k-tc.research_name.FOCUSPOUCH)。

## thaumic_tinkerer:INFUSED_INKWELL

**`tc.research_text.thaumic_tinkerer:INFUSED_INKWELL`**

- 改写前：八倍墨水
- 改写后：墨水管够

**`tc.research_page.thaumic_tinkerer:INFUSED_INKWELL.0`**

- 改写前：灌注墨水瓶可容纳 800 单位墨水。将它放在合成网格中央，周围放入八个墨囊即可重新灌满。
- 改写后：研究做到一半墨水见底，大概是神秘使生涯中最令人沮丧的时刻之一——仅次于研究做到一半纸用完了。<BR>你决定一劳永逸地解决这个问题。§5灌注笔与墨§0能够容纳整整 800 单位墨水，是普通墨水瓶的八倍。<BR>墨水用光后，把它放在合成网格中央，周围摆上八个墨囊，就能重新灌满。<LINE>附近的鱿鱼们最好开始担心了。

## thaumic_tinkerer:ICHOR_POUCH

**`ttmodern.pouch.upgrade_note`**

- 改写前：注魔前请先清空焦点袋，避免升级时遗失袋内物品。无底袋可存放 117 叠物品，不可套装其他袋子。
- 改写后：§n升级须知§r<BR>在把核心手袋注魔升级之前，务必先将袋里的东西倒干净——灵宝之力在重塑布料时可不会替你照看里面的物品。<BR>升级后的§5无底袋§0能装下 117 组物品，真不愧是“无底”。不过，它不肯装下别的袋子：袋中套袋这种事，就连灵宝也觉得太过分了。

## thaumic_tinkerer:PLACEMENT_MIRROR

**`ttmodern.mirror.upgrade_note`**

- 改写前：注魔前请先清空方块护符。潜行右键实心方块绑定，潜行对空气使用切换 3、5、7、9、11 格边长。建造消耗背包中的普通方块或同类方块护符储量，也支持已装备的戒指。受保护的放置会跳过，不消耗材料。
- 改写后：§n升级须知§r<BR>注魔之前，先把方块护符里的储量清空。<BR>潜行右击一个实心方块即可绑定；潜行对着空气使用，可以在 3、5、7、9、11 格的边长之间切换。建造时会消耗背包里的普通方块，或同类方块护符中的储量，已经装备的戒指也算数。<LINE>遇到受保护的位置，它会礼貌地跳过，也不会白白吃掉你的材料。

## thaumic_tinkerer:FOCUS_XP_DRAIN

**`ttmodern.xp_focus.upgrade_note`**

- 改写前：注魔前请清空经验护符，避免升级损失储存的经验。焦点消耗实际经验点；法杖接近充满时会按实际补充量减少扣费。
- 改写后：§n升级须知§r<BR>注魔之前请清空经验护符，否则升级过程会吞掉其中储存的经验。<BR>这枚核心消耗的是你实实在在的经验点。法杖快要充满时，它会按实际补充的分量少扣一些——精打细算，正是神秘使的美德。

## thaumic_tinkerer:PERIPHERALS

**`ttmodern.peripherals.analyzer`**

- 改写前：CC: Tweaked 将分析仪识别为 tt_aspectanalyzer。可调用 hasItem()、itemHasAspects()、getAspects() 和 getAspectCount()。要素列表从 1 开始编号，数量表以要素 ID 为键，返回单件物品的要素数量。读取不会消耗样品；界面仅显示已经扫描过的物品要素。
- 改写后：§n要素分析仪§r<BR>在 CC: Tweaked 的电脑看来，这台分析仪的外设类型是 tt_aspectanalyzer。你可以调用 hasItem()、itemHasAspects()、getAspects() 和 getAspectCount()。<BR>要素列表从 1 开始编号；数量表以要素 ID 为键，返回单件物品所含的要素数量。<LINE>读取并不会消耗样品。不过界面上只显示你已经扫描过的物品要素——电脑再聪明，也不能替你做研究。

## thaumic_tinkerer:GOLEM_CONNECTOR

**`ttmodern.peripherals.golem`**

- 改写前：用连接工具右键此方块，再潜行右键自己的傀儡。傀儡须处于每个坐标轴 30 格范围内。CC: Tweaked 外设类型为 tt_golemconnector。家位置和标记的更改即时生效；标记编号统一从 1 开始，dim 使用 minecraft:overworld 等维度资源 ID。批量替换先验证所有数据，失败不会修改原有标记。
- 改写后：§n傀儡连接器§r<BR>先用连接工具右击这个方块，再潜行右击你自己的傀儡，两者便会建立联系。傀儡必须处于每个坐标轴 30 格的范围之内。<BR>在 CC: Tweaked 看来，它的外设类型是 tt_golemconnector。对家位置和标记所做的更改会即时生效；标记编号统一从 1 开始，dim 使用 minecraft:overworld 之类的维度资源 ID。<LINE>批量替换标记时，连接器会先核对全部数据——只要有一项出错，原有的标记便原封不动。傀儡可经不起朝令夕改。
