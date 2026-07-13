// tools/gen-u4.js
// 必修一 Unit 4 Natural Disasters —— 8 课时金标准教案生成
const fs = require('fs');
const path = require('path');
const { replaceUnit } = require('./unit-template');

const SPEC = {
  book: '必修第一册', bookLabel: '必修一', unitNumber: 4, unitTitle: 'Natural Disasters',
  periods: [
    // ===== P1 听与说 =====
    {
      periodNumber: 1, lessonType: 'listening-speaking', duration: 40,
      title: 'Listening and Speaking: Natural Disasters & News Report — 灾害类型与新闻播报',
      textbookAnalysis: '本课为必修第一册 Unit 4 Natural Disasters 第一课时（Listening and Speaking），单元导入。主题为自然灾害类型与新闻播报。听力为灾害新闻报道，提取时间、地点、影响。本课为后续读唐山大地震、写灾情摘要奠定话题与词汇基础。',
      overview: '【学情分析】A班：初中已掌握 earthquake/flood，但 drought/landslide/tsunami/tornado/hurricane 拼写与区分不熟。B班：听数字（伤亡、损失）易错，需预教。共同问题：新闻播报语言特征（5W）不熟，描述灾害缺 affect/damage/destroy 等动词。',
      objectives: [
        '语言能力：听懂灾害新闻的主旨与关键细节（时间、地点、影响），用 affect/damage/destroy 描述灾害。',
        '文化意识：认识自然灾害的破坏力，树立防灾减灾与互助意识。',
        '思维品质：按 5W（when/where/what/who/how）分类梳理新闻信息。',
        '学习能力：借助新闻信息卡自主记录听力要点并复述。'
      ],
      keyPoints: '① 灾害词：earthquake / flood / drought / landslide / tsunami / tornado / hurricane。② 动词：affect / damage / destroy / rescue / survive。③ 新闻 5W：when/where/what/who/how。',
      difficulties: '① drought /draʊt/ 与 drought 拼写，易混 draft。原因：形近。② tsunami /tsuːnɑːmi/ 音译词发音。③ damage（部分损坏）vs destroy（彻底毁坏）程度差异。',
      teachingMethods: '① 任务型：以播报一则灾害新闻为终任务。② 听前预教词与数字。③ 新闻信息卡记录。',
      preparation: '【PPT课件】P1 单元封面；P2 灾害类型九宫格；P3-4 听力任务；P5 新闻句型板；P6 播报任务卡。【实物教具】新闻信息卡 printed；灾害词条卡。【音频】新闻听力音频。',
      process: [
        { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：What disasters can you see? Have you experienced any? 预设回答：Earthquake, flood! 板书时机：板书灾害词。差异化提示：B班指图说中文；A班用英语。易错点提醒：drought /draʊt/。' },
        { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读并辨析 damage vs destroy。教师：Which means totally ruined? 预设回答：Destroy! 板书时机：板书动词。差异化提示：B班配图记忆；A班造句。易错点提醒：tsunami /tsuːnɑːmi/。' },
        { step: '听前预测', time: '5', content: '【PPT P4 信息卡】教师：What 5W will you hear? 预设回答：When, where, what. 板书时机：信息卡留空。差异化提示：B班勾选；A班自列。易错点提醒：留意数字。' },
        { step: '听中填卡', time: '10', content: '【音频】播放新闻，学生填 5W。教师：When and where did it happen? 预设回答：July, in the south. 板书时机：核对填卡。差异化提示：B班听两遍；A班一遍。易错点提醒：affect /əfekt/ 重音。' },
        { step: '句型输入', time: '7', content: '【PPT P5 句型板】教师：A flood hit the city. It affected 1,000 people. 预设回答跟读。板书时机：板书句型。差异化提示：B班套用；A班扩展。易错点提醒：hit 过去式仍 hit。' },
        { step: '播报任务', time: '5', content: '【PPT P6 任务卡】学生用信息卡播报一则灾害新闻。教师：Report the disaster. 预设回答：An earthquake hit the town. It damaged many houses. 板书时机：无。差异化提示：B班读卡；A班脱稿。易错点提醒：用 5W 完整。' }
      ],
      blackboard: '┌─ U4 Listening & Speaking ┐\n│ Disasters: earthquake/flood/  │\n│  drought/landslide/tsunami    │\n│  tornado/hurricane            │\n│ affect/damage/destroy/rescue  │\n│ → 新闻 5W(when/where/what/who)│\n└────────────────────────────────┘',
      exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有灾害词与动词。2. 用 5W 写一则 5 句灾害新闻。【提高作业】为本地一种多发灾害写一段 60 词防灾提示。【参考答案——教师用】基础2示例：A flood hit the south in July. It affected 500 people. The water damaged many houses. Rescue teams helped the survivors. People moved to shelters.',
      reflection: '✅ 亮点：九宫格+5W 卡让新闻结构清晰，B班填卡完成率高。⚠️ 需改进：damage/destroy 区分仍混。📌 下节课衔接：进入阅读唐山大地震，从新闻延伸到深度叙事。'
    },
    // ===== P2 阅读 Ⅰ =====
    {
      periodNumber: 2, lessonType: 'reading', duration: 45,
      title: 'Reading and Thinking: The Night the Earth Didn\'t Sleep (Ⅰ) — 整体理解',
      textbookAnalysis: '第二课时，语篇 The Night the Earth Didn\'t Sleep 叙述 1976 年 7 月 28 日唐山大地震。文本按震前异常—震时毁灭—震后救援与重建展开。本节聚焦整体理解与事件时间线。',
      overview: '【学情分析】A班：能读叙事但时间线易混，忽视震前征兆。B班：长难句（定语从句修饰物）吃力。共同问题：对震前异常现象（井水升降、动物反常）理解浅，in ruins/in shock 等短语不熟。',
      objectives: [
        '语言能力：用略读获取文本主旨与段落大意，用扫读提取震前/震时/震后关键信息。',
        '文化意识：认识地震破坏力与团结互助精神，致敬救援者。',
        '思维品质：用时间线梳理事件发展（征兆—爆发—救援—重建），培养时序梳理能力。',
        '学习能力：借助时间线图表自主梳理并复述。'
      ],
      keyPoints: '① 结构：before（征兆）— during（爆发）— after（救援/重建）。② 短语：in ruins / in shock / as if / rescue / shelter。③ 词汇：crack, smelly, shake, destroy, survive。',
      difficulties: '① as if 后接虚拟语气（as if the world were ending），学生用 was。② in ruins（成废墟）短语义，学生漏 s。③ 震前征兆的 -ing 后置定语（gas coming out of it）识别困难。',
      teachingMethods: '① 图式激活：地震前预测。② 略读+扫读分层。③ 时间线梳理。',
      preparation: '【PPT课件】P1 唐山地图+时间轴；P2 语篇；P3 段落大意卡；P4 时间线表；P5 复述脚手架。【实物教具】时间线表 printed。【音频】无。',
      process: [
        { step: '图式激活', time: '5', content: '【PPT P1 地图】教师：What happens before an earthquake? 预设回答：Animals act strange. 板书时机：板书征兆。差异化提示：B班说中文；A班用英语。易错点提醒：earthquake /ɜːθkweɪk/。' },
        { step: '略读段落', time: '8', content: '【PPT P2 语篇】教师：Match each paragraph to before/during/after. 预设回答匹配。板书时机：板书三阶段。差异化提示：B班匹配；A班归纳。易错点提醒：paragraph /pærəgrɑːf/。' },
        { step: '扫读时间线', time: '12', content: '【PPT P4 时间线】学生填震前征兆/震时现象/震后救援。教师：What happened at 3:42? 预设回答：Everything began to shake. 板书时机：核对填表。差异化提示：B班给填空表；A班自填。易错点提醒：in ruins 加 s。' },
        { step: '短语提炼', time: '8', content: '【PPT P3 词卡】教师圈 in ruins/in shock/as if。预设回答跟读。板书时机：板书短语。差异化提示：B班认读；A班造句。易错点提醒：as if + were（虚拟）。' },
        { step: '复述', time: '7', content: '【PPT P5 脚手架】学生用时间线复述。教师：Retell the event. 预设回答：Before the quake, strange things happened. At 3:42, everything shook. 板书时机：无。差异化提示：B班照表读；A班脱稿。易错点提醒：shake→shook 过去式。' },
        { step: '小结', time: '5', content: '【总结】回顾三阶段+团结互助。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：rescue /reskjuː/。' }
      ],
      blackboard: '┌─ U4 Reading Ⅰ: 唐山大地震 ┐\n│ before: 征兆(井水/动物)   │\n│ during: 3:42 爆发, in ruins │\n│ after: 救援/重建/希望       │\n│ in ruins / in shock / as if │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 完成时间线表（征兆/爆发/救援各≥3 点）。2. 用 5 句话复述事件。【提高作业】写一段 60 词震后救援描述。【参考答案——教师用】基础2示例：Strange things happened before the quake. At 3:42 a.m., everything began to shake. The city was in ruins. Soon rescue teams arrived. People helped each other and rebuilt the city.',
      reflection: '✅ 亮点：时间线让叙事清晰，A班复述流畅。⚠️ 需改进：as if 虚拟语气讲解偏快。📌 下节课衔接：进入语言深度，赏析 -ing 后置定语与长难句。'
    },
    // ===== P3 阅读 Ⅱ =====
    {
      periodNumber: 3, lessonType: 'reading', duration: 45,
      title: 'Reading and Thinking: The Night the Earth Didn\'t Sleep (Ⅱ) — 语言深度',
      textbookAnalysis: '第三课时，沿用唐山地震语篇，聚焦语言深度：赏析 -ing 后置定语、as if 虚拟语气、主+系+表+to do 结构与定语从句，为写作积累语料。',
      overview: '【学情分析】A班：能懂大意但 -ing 后置定语不熟。B班：as if 虚拟语气与定语从句识别困难。共同问题：描述灾害仍用 very big，缺 in ruins/devastating 等地道表达。',
      objectives: [
        '语言能力：识别并运用 -ing 后置定语、as if 虚拟语气与灾害描述地道表达。',
        '文化意识：体会叙事文本的感染力与情感表达。',
        '思维品质：辨析 -ing 作定语与作状语的功能差异。',
        '学习能力：建立灾害描写语料库供写作调用。'
      ],
      keyPoints: '① -ing 后置定语：gas coming out of it / mice looking for places。② as if + 虚拟（were）。③ 结构：主+系+表+to do（It seemed as if the world were coming to an end）。④ 词汇：devastating, ruins, shelter, trap, bury。',
      difficulties: '① -ing 后置定语与进行时混淆。原因：形式相同功能不同。② as if 后用 were（虚拟），学生用 was。③ trap（困住）过去式 trapped 双写 p，学生漏。',
      teachingMethods: '① 语篇研读圈画。② 结构对比：-ing 定语 vs 进行时。③ 语料库搭建。',
      preparation: '【PPT课件】P1 语篇高亮；P2 -ing 结构对比；P3 as if 虚拟；P4 语料库模板；P5 仿写。【实物教具】语料卡 printed。【音频】无。',
      process: [
        { step: '圈画-ing', time: '8', content: '【PPT P1 高亮】教师：Find -ing phrases after nouns. 预设回答：gas coming out of it. 板书时机：板书结构。差异化提示：B班找已高亮；A班自找。易错点提醒：-ing 作定语表主动进行。' },
        { step: '结构对比', time: '10', content: '【PPT P2 对比】教师：gas coming out（定语）vs It was coming（进行时）. 预设回答辨析。板书时机：双栏对比。差异化提示：B班选填；A班解释。易错点提醒：定语紧接名词后。' },
        { step: 'as if虚拟', time: '10', content: '【PPT P3 虚拟】教师：It seemed as if the world were ending. — as if 后用 were. 预设回答跟读。板书时机：板书结构。差异化提示：B班套用；A班仿写。易错点提醒：虚拟用 were 不用 was。' },
        { step: '语料库', time: '8', content: '【PPT P4 模板】学生填灾害词/短语/句式语料卡。板书时机：巡视。差异化提示：B班填词；A班造句。易错点提醒：trap→trapped 双写。' },
        { step: '仿写', time: '9', content: '【PPT P5 练习】学生用语库仿写一句灾害描写。教师：Describe a disaster scene. 预设回答：The city lay in ruins, with people looking for shelter. 板书时机：展示佳句。差异化提示：B班填空；A班自由。易错点提醒：-ing 后置定语。' }
      ],
      blackboard: '┌─ U4 Reading Ⅱ: 语言深度 ┐\n│ -ing 后置定语: gas coming…  │\n│ as if + 虚拟(were)          │\n│ 主+系+表+to do              │\n│ in ruins / trap→trapped     │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 整理语料库（灾害词≥5、短语≥4）。2. 用 -ing 后置定语造 3 句。【提高作业】用语料库写一段 50 词灾害场景（含 as if 虚拟 1 处）。【参考答案——教师用】基础2示例：The river rising fast flooded the village. / People running out of buildings screamed. / The dog barking loudly warned the family.',
      reflection: '✅ 亮点：结构对比让 -ing 功能清晰，A班仿写提升。⚠️ 需改进：as if 虚拟 B 班仍用 was。📌 下节课衔接：进入语法——限制性定语从句，为精确描述奠基。'
    },
    // ===== P4 语法 =====
    {
      periodNumber: 4, lessonType: 'grammar', duration: 45,
      title: 'Discovering Useful Structures: 限制性定语从句（that/which/who/whom/whose）',
      textbookAnalysis: '第四课时，语法点：限制性定语从句，用 that/which 修饰物，who/whom 修饰人，whose 表所属。本节聚焦关系代词选择与先行词一致性。',
      overview: '【学情分析】A班：知道 that/which 但选择混乱，whose 属新学。B班：定语从句中缺成分判断不清。共同问题：逗号后（非限制性）误用 that。',
      objectives: [
        '语言能力：识别并正确使用 that/which/who/whom/whose 引导的限制性定语从句。',
        '文化意识：体会定语从句使表达精确简洁的价值。',
        '思维品质：按先行词（人/物）与从句成分（主/宾）选择关系代词。',
        '学习能力：用关系代词选择表归纳规则。'
      ],
      keyPoints: '① that/which 修饰物，who/whom 修饰人，whose 表所属。② 从句缺主语用 who/that（人）或 that/which（物）；缺宾语可省略。③ whose + 名词 表所属。',
      difficulties: '① that 与 which 选择：限制性从句两者皆可，非限制性只用 which。② whom 作宾格用于人，学生误用 who。③ whose 既可指人也可指物，学生以为只指人。',
      teachingMethods: '① 归纳法：从例句发现规则。② 选择表：先行词×成分。③ 情境操练：描述灾后场景。',
      preparation: '【PPT课件】P1 例句；P2 关系代词选择表；P3 that vs which；P4 whose 用法；P5 操练题。【实物教具】选择表卡 printed。【音频】无。',
      process: [
        { step: '观察例句', time: '7', content: '【PPT P1 例句】教师：The cracks that appeared in the walls... — that 修饰 cracks. 预设回答找先行词。板书时机：板书例句。差异化提示：B班找先行词；A班说成分。易错点提醒：that 修饰物。' },
        { step: '归纳选择表', time: '10', content: '【PPT P2 表】师生归纳：人→who/whom/whose；物→that/which。教师：Which for a person? 预设回答：who/whom. 板书时机：填表。差异化提示：B班填代词；A班补例句。易错点提醒：who 主格，whom 宾格。' },
        { step: 'that vs which', time: '8', content: '【PPT P3 对比】教师：限制性从句 that/which 皆可；非限制性（逗号后）只用 which. 预设回答辨析。板书时机：板书规则。差异化提示：B班选填；A班解释。易错点提醒：逗号后不用 that。' },
        { step: 'whose用法', time: '8', content: '【PPT P4 whose】教师：The boy whose leg was injured... — whose 表所属. 预设回答跟读。板书时机：板书结构。差异化提示：B班套用；A班仿写。易错点提醒：whose + 名词。' },
        { step: '操练', time: '12', content: '【PPT P5 题】学生用关系代词填空并合并句子。教师：The man ___ helped us... 预设回答：who. 板书时机：展示。差异化提示：B班选择式；A班合并句。易错点提醒：缺宾语可省略。' }
      ],
      blackboard: '┌─ U4 Grammar: 限制性定语从句 ┐\n│ 人: who(主)/whom(宾)/whose  │\n│ 物: that/which              │\n│ 限制性 that/which 皆可      │\n│ 非限制性(逗号)只用 which    │\n│ whose + 名词(人/物皆可)     │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 用关系代词填空 10 题。2. 合并 5 对句子为定语从句。【提高作业】写一段 50 词灾后场景，含 3 处定语从句（that/who/whose 各 1）。【参考答案——教师用】基础1示例：The quake that hit the city was terrible. / The man who rescued the boy was brave. / The house whose roof fell was old.',
      reflection: '✅ 亮点：选择表让关系代词清晰，A班合并句准确。⚠️ 需改进：that/which 选择与 whom 仍混。📌 下节课衔接：进入听与谈——用定语从句讨论防灾准备。'
    },
    // ===== P5 听与谈 =====
    {
      periodNumber: 5, lessonType: 'listening-talking', duration: 40,
      title: 'Listening and Talking: Disaster Preparedness — 防灾准备与应对',
      textbookAnalysis: '第五课时，听说结合。听力为防灾准备对话；口语为用定语从句与指令性语言介绍应急包与避险措施。',
      overview: '【学情分析】A班：能说单句但指令语不熟。B班：听物品清单易遗漏。共同问题：应急物品英文名（first-aid kit, flashlight, whistle）不熟。',
      objectives: [
        '语言能力：听懂防灾准备对话中的物品与措施；用定语从句与指令语介绍应急包。',
        '文化意识：树立防灾意识与自救互助能力。',
        '思维品质：按物品—措施—步骤分类组织防灾说明。',
        '学习能力：用应急清单记录并复述。'
      ],
      keyPoints: '① 物品：first-aid kit / flashlight / whistle / blanket / water / radio。② 指令语：Keep... / Do not... / Make sure...。③ 定语从句：a kit that contains...。',
      difficulties: '① first-aid 连字符与读音。② whistle /wɪsl/ 中 t 不发音。③ 指令语与定语从句混用易乱。',
      teachingMethods: '① 情境模拟：介绍应急包。② 听前预教物品词。③ 清单记录。',
      preparation: '【PPT课件】P1 应急包图；P2 物品词；P3 听力任务；P4 指令句型；P5 介绍卡。【实物教具】应急清单 printed；物品图卡。【音频】听力音频。',
      process: [
        { step: '物品预教', time: '6', content: '【PPT P2 物品】教师领读 first-aid kit/flashlight/whistle。预设回答跟读。板书时机：板书物品词。差异化提示：B班配图；A班造句。易错点提醒：whistle /wɪsl/。' },
        { step: '听前预测', time: '5', content: '【PPT P3 任务】教师：What items will you hear? 预设回答：Water, flashlight. 板书时机：清单留空。差异化提示：B班勾选；A班自列。易错点提醒：留意数量。' },
        { step: '听中记录', time: '10', content: '【音频】播放，学生填应急清单。教师：What should you keep? 预设回答：A first-aid kit. 板书时机：核对填表。差异化提示：B班听两遍；A班一遍。易错点提醒：first-aid 连字符。' },
        { step: '指令句型', time: '6', content: '【PPT P4 句型】教师：Keep a kit ready. Do not panic. Make sure you have water. 预设回答跟读。板书时机：板书指令语。差异化提示：B班套用；A班扩展。易错点提醒：祈使句无主语。' },
        { step: '介绍任务', time: '13', content: '【PPT P5 卡】学生用定语从句+指令语介绍应急包。教师：Introduce your emergency kit. 预设回答：This is a kit that contains bandages. Keep it ready. 板书时机：无。差异化提示：B班用脚本；A班自由。易错点提醒：定语从句修饰物品。' }
      ],
      blackboard: '┌─ U4 Listening & Talking ┐\n│ Items: first-aid kit/     │\n│  flashlight/whistle/water │\n│ 指令: Keep…/Do not…/      │\n│       Make sure…          │\n│ a kit that contains…      │\n└────────────────────────────┘',
      exercises: '【基础作业】1. 听录音补全应急清单。2. 用定语从句写 3 句介绍应急物品。【提高作业】写一段 60 词防灾指南（含指令语与定语从句各 2 处）。【参考答案——教师用】基础2示例：This is a flashlight that works without power. / Keep a whistle that can be heard far away. / Prepare water that is safe to drink.',
      reflection: '✅ 亮点：清单+指令语让防灾说明真实，B班参与度高。⚠️ 需改进：whistle 发音仍弱。📌 下节课衔接：进入写作——写灾害事件摘要。'
    },
    // ===== P6 写作 Ⅰ =====
    {
      periodNumber: 6, lessonType: 'writing', duration: 45,
      title: 'Reading for Writing: A Disaster Summary (Ⅰ) — 读析与语料',
      textbookAnalysis: '第六课时，写作第一课时。读模型灾害摘要（含事件—影响—救援），分析结构与语言，积累语料。',
      overview: '【学情分析】A班：能写单句但摘要结构松散，缺影响与救援。B班：时态混乱（叙事用过去，学生混现在）。共同问题：摘要易成流水账，缺数据与感受。',
      objectives: [
        '语言能力：识别灾害摘要结构（事件—影响—救援—启示）与衔接手段，积累语料。',
        '文化意识：在摘要中体现对受灾者的关切与互助精神。',
        '思维品质：按事件逻辑与时序组织摘要。',
        '学习能力：用提纲模板搭建写作骨架。'
      ],
      keyPoints: '① 结构：event → impact → rescue → reflection。② 时态：叙事用过去时。③ 语料：hit/affect/damage/rescue/in ruins/survive。',
      difficulties: '① 时态：叙事须用过去时。② impact（影响）抽象词。③ 数据表达（affected 1,000 people）格式。',
      teachingMethods: '① 范文研读圈结构。② 提纲搭建。③ 语料积累。',
      preparation: '【PPT课件】P1 范文分段；P2 结构图；P3 时态标注；P4 语料库；P5 提纲模板。【实物教具】提纲卡 printed。【音频】无。',
      process: [
        { step: '读范文', time: '8', content: '【PPT P1 范文】教师：What disaster is it about? 预设回答：A flood. 板书时机：板书主题。差异化提示：B班抓大意；A班找结构。易错点提醒：summary /sʌməri/。' },
        { step: '析结构', time: '10', content: '【PPT P2 结构图】师生分四段。教师：Which part tells the impact? 预设回答：Impact. 板书时机：填结构图。差异化提示：B班匹配；A班归纳。易错点提醒：impact /ɪmpækt/。' },
        { step: '时态标注', time: '8', content: '【PPT P3 时态】教师圈过去时动词。预设回答辨析。板书时机：板书时态。差异化提示：B班标时态；A班解释。易错点提醒：hit→hit 过去式不变。' },
        { step: '积语料', time: '7', content: '【PPT P4 语料库】学生填事件/影响/救援语料卡。板书时机：巡视。差异化提示：B班填词；A班造句。易错点提醒：affect+数字。' },
        { step: '搭提纲', time: '12', content: '【PPT P5 模板】学生用提纲卡搭摘要骨架。教师：Outline your summary. 预设回答展示。板书时机：展示提纲。差异化提示：B班填空；A班自列。易错点提醒：叙事用过去时。' }
      ],
      blackboard: '┌─ U4 Writing Ⅰ: 灾害摘要 ┐\n│ 结构: event→impact        │\n│        →rescue→reflection │\n│ 时态: 叙事过去时          │\n│ 语料: hit/affect/damage/  │\n│       rescue/in ruins     │\n└────────────────────────────┘',
      exercises: '【基础作业】1. 完成摘要提纲（四部分各≥2 点）。2. 整理事件动词与影响短语各 5 个。【提高作业】用提纲写一段 80 词灾害摘要初稿。【参考答案——教师用】基础1示例：Event: a flood hit the south；Impact: affected 1,000 people, damaged houses；Rescue: teams saved survivors；Reflection: we should prepare better.',
      reflection: '✅ 亮点：结构图+提纲让写作有骨架，B班提纲完成率高。⚠️ 需改进：时态仍混。📌 下节课衔接：下节起草成文+互评。'
    },
    // ===== P7 写作 Ⅱ =====
    {
      periodNumber: 7, lessonType: 'writing', duration: 45,
      title: 'Reading for Writing: A Disaster Summary (Ⅱ) — 起草与互评',
      textbookAnalysis: '第七课时，写作第二课时。基于提纲起草成文，运用过去时与定语从句，经同伴互评修改定稿。',
      overview: '【学情分析】A班：能成段但时态偶尔滑回现在。B班：句子碎片化。共同问题：互评不知评什么，需量规引导。',
      objectives: [
        '语言能力：依据提纲写 80 词灾害摘要，正确使用过去时与定语从句，段落连贯。',
        '文化意识：在摘要中体现对受灾者的关切。',
        '思维品质：依据量规评价同伴作品并提出建议。',
        '学习能力：通过互评-修改循环提升自我修改能力。'
      ],
      keyPoints: '① 成段：四结构+衔接词。② 时态：叙事过去时。③ 互评量规：结构/时态/语言/衔接。',
      difficulties: '① 时态滑回现在。② 定语从句关系代词选错。③ 互评流于表面。',
      teachingMethods: '① 过程写作：起草-互评-修改。② 量规引导互评。③ 教师面批聚焦时态。',
      preparation: '【PPT课件】P1 范文回顾；P2 量规表；P3 互评流程；P4 佳句展示；P5 常见问题。【实物教具】互评量规卡 printed。【音频】无。',
      process: [
        { step: '回顾要求', time: '5', content: '【PPT P1 范文】教师回顾结构+时态。预设回答跟读。板书时机：板书要点。差异化提示：B班跟读；A班复述。易错点提醒：叙事用过去时。' },
        { step: '起草', time: '15', content: '【写作】学生依提纲起草 80 词。教师巡视面批。板书时机：无。差异化提示：B班给句型框；A班自由。易错点提醒：时态一致。' },
        { step: '互评', time: '12', content: '【PPT P2 量规】学生依量规评同伴。教师：Give one suggestion. 预设回答：Check the tense. 板书时机：展示量规。差异化提示：B班勾选；A班写建议。易错点提醒：评时态。' },
        { step: '修改', time: '8', content: '【修改】学生据互评修改。教师聚焦时态。板书时机：无。差异化提示：B班改错；A班润色。易错点提醒：滑回现在须改过去。' },
        { step: '展示', time: '5', content: '【PPT P4 佳句】展示佳句与修改对比。预设回答赏析。板书时机：圈亮点。差异化提示：B班跟读；A班点评。易错点提醒：定语从句关系代词。' }
      ],
      blackboard: '┌─ U4 Writing Ⅱ: 起草+互评 ┐\n│ 量规: 结构/时态/语言/衔接   │\n│ 时态: 叙事过去时           │\n│ 流程: 起草→互评→修改→定稿   │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 定稿灾害摘要（≥80 词，四结构齐全）。2. 用红笔标出过去时与定语从句。【提高作业】为摘要配一段 30 词防灾启示。【参考答案——教师用】基础1示范段：A flood hit the south in July. It affected 1,000 people and damaged many houses that stood near the river. Rescue teams arrived and saved the survivors. We should prepare emergency kits to stay safe.',
      reflection: '✅ 亮点：量规让互评有抓手，A班时态准确率提升。⚠️ 需改进：B班句子碎片化。📌 下节课衔接：进入项目——综合单元产出防灾指南海报。'
    },
    // ===== P8 项目复习 =====
    {
      periodNumber: 8, lessonType: 'project', duration: 45,
      title: 'Project & Unit Review: Disaster Survival Guide — 防灾生存指南海报',
      textbookAnalysis: '第八课时，单元综合产出。小组为一种多发灾害制作防灾生存指南海报，综合运用灾害词汇、定语从句、指令语与摘要语料，并展示推介。',
      overview: '【学情分析】A班：综合运用能力可，但展示语言需规范。B班：表达碎片，需模板与分工支持。共同问题：海报文体特征（标题+清单+指令+号召）体现不足。',
      objectives: [
        '语言能力：综合运用单元词汇与定语从句，以海报文体制作防灾生存指南。',
        '文化意识：在指南中体现防灾意识与互助精神。',
        '思维品质：统筹物品—措施—步骤，做可行防灾方案。',
        '学习能力：通过小组协作完成从策划到展示的完整项目。'
      ],
      keyPoints: '① 文体：海报（标题+物品清单+指令语+号召）。② 语言：定语从句+指令语+过去时事例。③ 产出：海报+口头推介。',
      difficulties: '① 文体退化成流水账。② 小组分工不均。③ 口头推介缺指令与号召。',
      teachingMethods: '① 项目式学习（PBL）。② 小组分工+量规。③ 展示互评。',
      preparation: '【PPT课件】P1 项目说明+样例；P2 海报模板；P3 评价量规；P4 展示流程；P5 单元知识图。【实物教具】A4 海报纸 printed 每组；彩笔。【音频】无。',
      process: [
        { step: '任务发布', time: '6', content: '【PPT P1 说明】教师发布任务：为一种灾害制作生存指南海报。预设回答讨论。板书时机：板书要求。差异化提示：B班用模板；A班自创。易错点提醒：海报四要素。' },
        { step: '小组策划', time: '12', content: '【PPT P2 模板】小组分工：灾害/物品/措施/文案。教师巡视。预设回答讨论。板书时机：无。差异化提示：B班填模板；A班设计。易错点提醒：用定语从句。' },
        { step: '制作海报', time: '12', content: '【实物 海报】小组图文制作。教师指导文体与语言。板书时机：无。差异化提示：B班配图；A班写文案。易错点提醒：指令语收尾。' },
        { step: '展示', time: '10', content: '【PPT P4 流程】各组用指令语+定语从句推介。教师：Present your guide. 预设回答展示。板书时机：无。差异化提示：B班读卡；A班脱稿。易错点提醒：用 Keep…/Do not… 指令。' },
        { step: '评价+回顾', time: '5', content: '【PPT P3 量规+P5 知识图】互评+单元回顾。预设回答跟读。板书时机：圈重点。差异化提示：B班勾选；A班自评。易错点提醒：单元核心定语从句/灾害词回顾。' }
      ],
      blackboard: '┌─ U4 Project & Review ┐\n│ 任务: 防灾生存指南海报 │\n│ 文体: 标题+清单+指令+号召│\n│ 语言: 定语从句+指令语  │\n│ 产出: 海报 + 口头推介   │\n└──────────────────────────┘',
      exercises: '【基础作业】1. 完善海报（含四要素）。2. 写一段 60 词防灾指南（含 2 处定语从句与 2 处指令语）。【提高作业】为海报设计家庭疏散路线并说明。【参考答案——教师用】基础2示范：When an earthquake comes, keep calm. Prepare a kit that contains water and a flashlight. Do not use the lift. Help the people who are trapped. Stay safe together!',
      reflection: '✅ 亮点：海报产出综合性强，A班文体特征明显。⚠️ 需改进：B班分工不均。📌 下节课衔接：进入 Unit 5 Languages Around the World，话题转向语言与文化。'
    }
  ]
};

const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const oldLessons = require('../data/lessons.js');
const newLessons = replaceUnit(oldLessons, SPEC);
fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(newLessons, null, 2) + ';\n', 'utf8');

const u4 = newLessons.filter(l => l.book === SPEC.book && l.unitNumber === SPEC.unitNumber);
const ids = newLessons.map(l => l.id);
const dup = ids.filter((x, i) => ids.indexOf(x) !== i);
console.log('U4 periods:', u4.length, '(expect 8)');
console.log('Total lessons:', newLessons.length);
console.log('Duplicate ids:', dup.length ? dup : 'none');
u4.forEach(l => console.log('  p' + l.periodNumber, l.lessonType, '|', l.title.slice(0, 40)));
