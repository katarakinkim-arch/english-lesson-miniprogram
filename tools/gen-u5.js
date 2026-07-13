// tools/gen-u5.js
// 必修一 Unit 5 Languages Around the World —— 8 课时金标准教案生成
const fs = require('fs');
const path = require('path');
const { replaceUnit } = require('./unit-template');

const SPEC = {
  book: '必修第一册', bookLabel: '必修一', unitNumber: 5, unitTitle: 'Languages Around the World',
  periods: [
    // ===== P1 听与说 =====
    {
      periodNumber: 1, lessonType: 'listening-speaking', duration: 40,
      title: 'Listening and Speaking: Languages of the World — 世界语言与学习理由',
      textbookAnalysis: '本课为必修第一册 Unit 5 Languages Around the World 第一课时（Listening and Speaking），单元导入。主题为世界语言多样性与学习外语的理由。听力为不同人谈论所学语言与原因。本课为后续读汉字书写体系、写语言学习博客奠定话题与词汇基础。',
      overview: '【学情分析】A班：初中已掌握 language/English，但 accent/dialect/official/native/fluent 等词不熟。B班：听语言名（Arabic, Russian, Portuguese）易错。共同问题：表达学习理由停留在 I like it，缺 broaden horizons/connect with others 等表达。',
      objectives: [
        '语言能力：听懂语言学习对话的主旨与理由细节，用 I learn... because... / It helps me... 表达学习动机。',
        '文化意识：了解世界语言多样性，尊重不同语言与文化。',
        '思维品质：按语言—理由—收获分类梳理信息，培养多角度思考。',
        '学习能力：借助语言信息卡自主记录听力要点并复述。'
      ],
      keyPoints: '① 词汇：accent / dialect / official / native / fluent / vocabulary。② 语言名：Arabic / Russian / Portuguese / Spanish / French。③ 句式：I learn... because... / It helps me connect with...。',
      difficulties: '① fluent /fluːənt/ 与 fluid 易混。② Portuguese /pɔːtʃʊɡiːz/ 音节多。③ broaden horizons（开阔视野）短语义，学生直译。',
      teachingMethods: '① 任务型：以介绍学习一种语言的理由为终任务。② 听前预教词与语言名。③ 信息卡记录。',
      preparation: '【PPT课件】P1 单元封面+世界地图；P2 语言名卡；P3-4 听力任务；P5 句型板；P6 说话任务卡。【实物教具】语言信息卡 printed；语言名词条。【音频】听力音频。',
      process: [
        { step: '导入激活', time: '5', content: '【PPT P1 地图】教师：How many languages are there in the world? Why learn a foreign one? 预设回答：To talk to people. 板书时机：板书 languages。差异化提示：B班说中文；A班用英语。易错点提醒：foreign /fɒrən/。' },
        { step: '词汇输入', time: '8', content: '【PPT P2 词卡】教师领读 accent/dialect/official/native/fluent。教师：What is your native language? 预设回答：Chinese. 板书时机：板书词。差异化提示：B班配图；A班造句。易错点提醒：fluent /fluːənt/。' },
        { step: '听前预测', time: '5', content: '【PPT P3 信息卡】教师：What info will you hear? 预设回答：Language, reason. 板书时机：信息卡留空。差异化提示：B班勾选；A班自列。易错点提醒：留意语言名。' },
        { step: '听中填卡', time: '10', content: '【音频】播放，学生填语言+理由。教师：Why does she learn Spanish? 预设回答：To travel. 板书时机：核对填卡。差异化提示：B班听两遍；A班一遍。易错点提醒：Portuguese 拼读。' },
        { step: '句型输入', time: '7', content: '【PPT P5 句型板】教师：I learn French because it helps me connect with people. 预设回答跟读。板书时机：板书句型。差异化提示：B班套用；A班扩展。易错点提醒：broaden horizons 短语。' },
        { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生介绍学习某语言的理由。教师：Share your reason. 预设回答：I learn English because it broadens my horizons. 板书时机：无。差异化提示：B班用脚本；A班自由。易错点提醒：reasons 用复数。' }
      ],
      blackboard: '┌─ U5 Listening & Speaking ┐\n│ Words: accent/dialect/     │\n│  official/native/fluent    │\n│ Languages: Arabic/Russian/ │\n│  Portuguese/Spanish        │\n│ I learn… because…          │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有语言名与理由词。2. 用 I learn... because... 写 3 句学习理由。【提高作业】写一段 60 词短文：我最想学的一门外语及理由。【参考答案——教师用】基础2示例：I learn Spanish because it helps me travel. / I learn French because it broadens my horizons. / I learn Japanese because I love its culture.',
      reflection: '✅ 亮点：地图+信息卡激活充分，B班填卡完成率高。⚠️ 需改进：语言名发音仍弱。📌 下节课衔接：进入阅读汉字书写体系，从语言延伸到文字。'
    },
    // ===== P2 阅读 Ⅰ =====
    {
      periodNumber: 2, lessonType: 'reading', duration: 45,
      title: 'Reading and Thinking: The Chinese Writing System (Ⅰ) — 整体理解',
      textbookAnalysis: '第二课时，语篇 The Chinese Writing System: Connecting the Past and the Present 介绍汉字书写体系的历史（甲骨文—金文—隶书—楷书）及其如何连接古今、团结民族、传承文化。本节聚焦整体理解与时间线。',
      overview: '【学情分析】A班：能读但时间线易混，忽视书写体系的文化意义。B班：长难句（定语从句）吃力。共同问题：date back to / symbol / carve / represent 等词不熟，对汉字英文表述陌生。',
      objectives: [
        '语言能力：用略读获取文本主旨，用扫读提取汉字发展各阶段关键信息。',
        '文化意识：理解汉字书写体系的文化价值与民族凝聚力。',
        '思维品质：用时间线梳理汉字演变，培养时序与文化梳理能力。',
        '学习能力：借助时间线图表自主梳理并复述。'
      ],
      keyPoints: '① 时间线：Shang Dynasty (oracle bones) → later forms → today。② 词汇：date back to / symbol / carve / represent / classic / appreciate。③ 意义：connect past and present / unite the nation / spread culture。',
      difficulties: '① date back to 后接时间，学生加 from。② carve（雕刻）过去式 carved，学生漏 e。③ represent /reprɪzent/ 多音节发音。',
      teachingMethods: '① 图式激活：汉字演变预测。② 略读+扫读分层。③ 时间线梳理。',
      preparation: '【PPT课件】P1 汉字演变图（甲骨文→楷书）；P2 语篇；P3 段落大意卡；P4 时间线表；P5 复述脚手架。【实物教具】时间线表 printed。【音频】无。',
      process: [
        { step: '图式激活', time: '5', content: '【PPT P1 演变图】教师：How old is the Chinese writing system? 预设回答：Thousands of years. 板书时机：板书 oracle bones。差异化提示：B班说中文；A班用英语。易错点提醒：oracle /ɒrəkl/。' },
        { step: '略读段落', time: '8', content: '【PPT P2 语篇】教师：Match paragraphs to time periods. 预设回答匹配。板书时机：板书阶段。差异化提示：B班匹配；A班归纳。易错点提醒：dynasty /dɪnəsti/。' },
        { step: '扫读时间线', time: '12', content: '【PPT P4 时间线】学生填各阶段书写形式与意义。教师：What did people carve on bones? 预设回答：Symbols. 板书时机：核对填表。差异化提示：B班给填空表；A班自填。易错点提醒：carve→carved。' },
        { step: '意义提炼', time: '8', content: '【PPT P3 词卡】教师圈 connect/unite/spread。预设回答跟读。板书时机：板书意义词。差异化提示：B班认读；A班造句。易错点提醒：date back to + 时间。' },
        { step: '复述', time: '7', content: '【PPT P5 脚手架】学生用时间线复述。教师：Retell the history. 预设回答：The system dates back to the Shang Dynasty. People carved symbols on bones. 板书时机：无。差异化提示：B班照表读；A班脱稿。易错点提醒：dates back to 单三。' },
        { step: '小结', time: '5', content: '【总结】回顾演变+文化意义。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：represent /reprɪzent/。' }
      ],
      blackboard: '┌─ U5 Reading Ⅰ: 汉字书写体系 ┐\n│ Shang: oracle bones (carve)  │\n│ → later forms → today        │\n│ date back to / represent     │\n│ 连接古今 / 团结民族 / 传文化 │\n└────────────────────────────────┘',
      exercises: '【基础作业】1. 完成时间线表（阶段/形式/意义各≥3 点）。2. 用 5 句话复述汉字历史。【提高作业】写一段 60 词短文：汉字的文化意义。【参考答案——教师用】基础2示例：The Chinese writing system dates back to the Shang Dynasty. People carved symbols on animal bones. Over time, the forms changed. Today, it connects the past and the present. It unites the nation.',
      reflection: '✅ 亮点：演变图+时间线让历史清晰，A班复述流畅。⚠️ 需改进：date back to 用法仍混。📌 下节课衔接：进入语言深度，赏析定语从句与地道表达。'
    },
    // ===== P3 阅读 Ⅱ =====
    {
      periodNumber: 3, lessonType: 'reading', duration: 45,
      title: 'Reading and Thinking: The Chinese Writing System (Ⅱ) — 语言深度',
      textbookAnalysis: '第三课时，沿用汉字书写体系语篇，聚焦语言深度：赏析 date back to、-ing 作主语/宾语、定语从句与地道表达，为写作积累语料。',
      overview: '【学情分析】A班：能懂大意但 -ing 主语与定语从句运用少。B班：which/that 识别困难。共同问题：描述文化仍用 very important，缺 significant/appreciate 等词。',
      objectives: [
        '语言能力：识别并运用 date back to、-ing 主语与定语从句等表达。',
        '文化意识：体会汉字书写体系的文化自豪感。',
        '思维品质：辨析 -ing 作主语与作宾语的功能差异。',
        '学习能力：建立文化描写语料库供写作调用。'
      ],
      keyPoints: '① -ing 主语：By doing so, it has connected... / Learning it helps...。② 定语从句：a system which/that...。③ 词汇：significant / appreciate / classic / represent / pass down。',
      difficulties: '① -ing 主语谓语用单数。② which 与 that 选择（非限制性只用 which）。③ appreciate /əpriːʃieɪt/ 拼读。',
      teachingMethods: '① 语篇研读圈画。② 结构对比：-ing 主语 vs 宾语。③ 语料库搭建。',
      preparation: '【PPT课件】P1 语篇高亮；P2 -ing 结构；P3 定语从句；P4 语料库模板；P5 仿写。【实物教具】语料卡 printed。【音频】无。',
      process: [
        { step: '圈画-ing', time: '8', content: '【PPT P1 高亮】教师：Find -ing as subject. 预设回答：Learning it helps... 板书时机：板书结构。差异化提示：B班找已高亮；A班自找。易错点提醒：-ing 主语谓语单数。' },
        { step: '结构对比', time: '10', content: '【PPT P2 对比】教师：-ing 作主语 vs 作宾语（enjoy learning）. 预设回答辨析。板书时机：双栏对比。差异化提示：B班选填；A班解释。易错点提醒：主语位 vs 宾语位。' },
        { step: '定语从句', time: '10', content: '【PPT P3 从句】教师：a system which connects... — which 修饰 system. 预设回答跟读。板书时机：板书结构。差异化提示：B班套用；A班仿写。易错点提醒：非限制性用 which。' },
        { step: '语料库', time: '8', content: '【PPT P4 模板】学生填文化词/短语/句式语料卡。板书时机：巡视。差异化提示：B班填词；A班造句。易错点提醒：appreciate /əpriːʃieɪt/。' },
        { step: '仿写', time: '9', content: '【PPT P5 练习】学生用语库仿写一句文化描写。教师：Describe a cultural symbol. 预设回答：The writing system, which dates back thousands of years, represents our culture. 板书时机：展示佳句。差异化提示：B班填空；A班自由。易错点提醒：定语从句逗号+which。' }
      ],
      blackboard: '┌─ U5 Reading Ⅱ: 语言深度 ┐\n│ -ing 主语 → 谓语单数      │\n│ -ing 宾语(enjoy learning)  │\n│ 定语从句: which/that 修饰物 │\n│ date back to / appreciate  │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 整理语料库（文化词≥5、短语≥4）。2. 用 -ing 作主语造 3 句。【提高作业】用语料库写一段 50 词文化描写（含定语从句 1 处）。【参考答案——教师用】基础2示例：Learning Chinese connects us to our history. / Writing the characters helps us think. / Appreciating our culture makes us proud.',
      reflection: '✅ 亮点：结构对比让 -ing 功能清晰，A班仿写提升。⚠️ 需改进：appreciate 拼写仍弱。📌 下节课衔接：进入语法——定语从句关系副词，为精确表达奠基。'
    },
    // ===== P4 语法 =====
    {
      periodNumber: 4, lessonType: 'grammar', duration: 45,
      title: 'Discovering Useful Structures: 定语从句（关系副词 where/when/why + 介词+which/whom）',
      textbookAnalysis: '第四课时，语法点：定语从句关系副词 where（地点）、when（时间）、why（原因），以及 介词+which/whom 结构。承接 U4 关系代词，扩展至关系副词与介词结构。',
      overview: '【学情分析】A班：会用 that/which 但 where/when 作关系副词与作连词混淆。B班：介词+which 结构陌生。共同问题：where/when/why 与 which+介词的转换不熟。',
      objectives: [
        '语言能力：识别并正确使用 where/when/why 引导的定语从句，及 介词+which/whom 结构。',
        '文化意识：体会关系副词使表达精确简洁的价值。',
        '思维品质：按先行词（时间/地点/原因）选择关系副词，并能与介词+which 转换。',
        '学习能力：用关系副词选择表归纳规则。'
      ],
      keyPoints: '① where 修饰地点先行词（= at/in/on + which）。② when 修饰时间先行词（= at/in/on + which）。③ why 修饰 reason（= for which）。④ 介词+which/whom 用于正式表达。',
      difficulties: '① where 与 which 选择：先行词是地点且从句缺状语用 where，缺主/宾用 which。② when 与 which 同理。③ 介词选择（in which / on which / for which）依赖搭配。',
      teachingMethods: '① 归纳法：从例句发现规则。② 转换练习：where↔介词+which。③ 情境操练：描述语言与文化。',
      preparation: '【PPT课件】P1 例句；P2 关系副词选择表；P3 where↔介词+which；P4 when/why；P5 操练题。【实物教具】选择表卡 printed。【音频】无。',
      process: [
        { step: '观察例句', time: '7', content: '【PPT P1 例句】教师：This is the place where people carved symbols. — where 修饰 place. 预设回答找先行词。板书时机：板书例句。差异化提示：B班找先行词；A班说成分。易错点提醒：where 作状语。' },
        { step: '归纳选择表', time: '10', content: '【PPT P2 表】师生归纳：地点→where，时间→when，原因→why。教师：Which for time? 预设回答：when. 板书时机：填表。差异化提示：B班填副词；A班补例句。易错点提醒：缺状语才用关系副词。' },
        { step: '转换练习', time: '10', content: '【PPT P3 转换】教师：the place where = the place in which. 预设回答转换。板书时机：板书等式。差异化提示：B班选填；A班改写。易错点提醒：介词依赖搭配。' },
        { step: 'when/why', time: '8', content: '【PPT P4 when/why】教师：the time when / the reason why(=for which). 预设回答跟读。板书时机：板书结构。差异化提示：B班套用；A班仿写。易错点提醒：why = for which。' },
        { step: '操练', time: '10', content: '【PPT P5 题】学生用关系副词填空并转换。教师：This is the city ___ Chinese began. 预设回答：where. 板书时机：展示。差异化提示：B班选择式；A班转换。易错点提醒：缺主宾用 which。' }
      ],
      blackboard: '┌─ U5 Grammar: 关系副词 ┐\n│ 地点→where(=介词+which) │\n│ 时间→when(=介词+which)  │\n│ 原因→why(=for which)    │\n│ 介词+which/whom(正式)   │\n│ 缺状语→副词;缺主宾→代词│\n└──────────────────────────┘',
      exercises: '【基础作业】1. 用关系副词填空 10 题。2. 将 5 句 where/when/why 改写为 介词+which。【提高作业】写一段 50 词文化介绍，含 where/when/why 各 1 处。【参考答案——教师用】基础1示例：This is the place where people first wrote. / I remember the day when I learned my first character. / That is the reason why I love Chinese.',
      reflection: '✅ 亮点：选择表+转换让规则清晰，A班操练准确。⚠️ 需改进：介词搭配 B 班仍混。📌 下节课衔接：进入听与谈——用关系副句讨论语言学习。'
    },
    // ===== P5 听与谈 =====
    {
      periodNumber: 5, lessonType: 'listening-talking', duration: 40,
      title: 'Listening and Talking: Explore Foreign Languages — 探索外语与学习经验',
      textbookAnalysis: '第五课时，听说结合。听力为不同人分享外语学习经验与困难；口语为用关系副词与建议句式谈论学习策略。',
      overview: '【学情分析】A班：能说单句但建议句式不熟。B班：听困难描述易遗漏。共同问题：学习策略表达（practice, immerse, review）不熟。',
      objectives: [
        '语言能力：听懂外语学习经验与困难；用关系副词与建议句式谈论学习策略。',
        '文化意识：体会多语言学习的价值与坚持精神。',
        '思维品质：在讨论中提出可行学习建议。',
        '学习能力：用策略卡记录并复述。'
      ],
      keyPoints: '① 策略词：practice / immerse / review / memorize / communicate。② 建议句：You should... / It helps to... / The best way is...。③ 关系副词：the way in which / the time when。',
      difficulties: '① immerse /ɪmɜːs/ 拼读。② memorize /meməraɪz/ 与 memory 关系。③ the way in which 正式结构。',
      teachingMethods: '① 情境讨论。② 听前预教策略词。③ 策略卡记录。',
      preparation: '【PPT课件】P1 学习场景图；P2 策略词；P3 听力任务；P4 建议句型；P5 讨论卡。【实物教具】策略卡 printed。【音频】听力音频。',
      process: [
        { step: '策略词预教', time: '6', content: '【PPT P2 策略词】教师领读 practice/immerse/review/memorize。预设回答跟读。板书时机：板书策略词。差异化提示：B班配图；A班造句。易错点提醒：immerse /ɪmɜːs/。' },
        { step: '听前预测', time: '5', content: '【PPT P3 任务】教师：What difficulties will you hear? 预设回答：Pronunciation, vocabulary. 板书时机：卡留空。差异化提示：B班勾选；A班自列。易错点提醒：留意策略。' },
        { step: '听中记录', time: '10', content: '【音频】播放，学生填困难+策略。教师：How does she memorize words? 预设回答：By reviewing often. 板书时机：核对填卡。差异化提示：B班听两遍；A班一遍。易错点提醒：memorize /meməraɪz/。' },
        { step: '建议句型', time: '6', content: '【PPT P4 句型】教师：You should practice daily. It helps to immerse yourself. 预设回答跟读。板书时机：板书句型。差异化提示：B班套用；A班扩展。易错点提醒：It helps to + 原形。' },
        { step: '讨论', time: '13', content: '【PPT P5 卡】学生用关系副词+建议句讨论策略。教师：Discuss your learning ways. 预设回答：The way in which I learn is practice. You should review daily. 板书时机：无。差异化提示：B班用脚本；A班自由。易错点提醒：the way in which 正式。' }
      ],
      blackboard: '┌─ U5 Listening & Talking ┐\n│ 策略: practice/immerse/   │\n│  review/memorize          │\n│ 建议: You should…/        │\n│  It helps to…/The best way│\n│ the way in which…         │\n└────────────────────────────┘',
      exercises: '【基础作业】1. 听录音补全困难与策略卡。2. 用建议句式写 3 条学习建议。【提高作业】写一段 60 词语言学习经验，含 2 处关系副词。【参考答案——教师用】基础2示例：You should practice every day. / It helps to immerse yourself in the language. / The best way to memorize words is to review often.',
      reflection: '✅ 亮点：策略卡+建议句让讨论真实，B班参与度高。⚠️ 需改进：immerse 发音仍弱。📌 下节课衔接：进入写作——写语言学习博客。'
    },
    // ===== P6 写作 Ⅰ =====
    {
      periodNumber: 6, lessonType: 'writing', duration: 45,
      title: 'Reading for Writing: A Language-Learning Blog (Ⅰ) — 读析与语料',
      textbookAnalysis: '第六课时，写作第一课时。读模型博客（分享语言学习经历：起因—方法—收获—建议），分析结构与语言，积累语料。',
      overview: '【学情分析】A班：能写单句但博客结构松散，缺收获与建议。B班：时态混乱（经历用过去，学生混现在）。共同问题：博客语气不亲切，缺 I think / In my view。',
      objectives: [
        '语言能力：识别博客结构（起因—方法—收获—建议）与衔接手段，积累语料。',
        '文化意识：在分享中体现开放与坚持的学习态度。',
        '思维品质：按逻辑组织学习经历。',
        '学习能力：用提纲模板搭建写作骨架。'
      ],
      keyPoints: '① 结构：why I learn → how I learn → what I gained → my advice。② 时态：经历过去，建议现在。③ 语料：immerse/review/connect with/broaden horizons。',
      difficulties: '① 时态切换：经历过去 vs 建议现在。② gained（收获）抽象。③ 博客语气与正式文差异。',
      teachingMethods: '① 范文研读圈结构。② 提纲搭建。③ 语料积累。',
      preparation: '【PPT课件】P1 范文分段；P2 结构图；P3 时态标注；P4 语料库；P5 提纲模板。【实物教具】提纲卡 printed。【音频】无。',
      process: [
        { step: '读范文', time: '8', content: '【PPT P1 范文】教师：What language does the blogger learn? 预设回答：English. 板书时机：板书主题。差异化提示：B班抓大意；A班找结构。易错点提醒：blog /blɒɡ/。' },
        { step: '析结构', time: '10', content: '【PPT P2 结构图】师生分四段。教师：Which part gives advice? 预设回答：Advice. 板书时机：填结构图。差异化提示：B班匹配；A班归纳。易错点提醒：advice 不可数。' },
        { step: '时态标注', time: '8', content: '【PPT P3 时态】教师圈经历过去与建议现在。预设回答辨析。板书时机：板书时态。差异化提示：B班标时态；A班解释。易错点提醒：gained 过去式。' },
        { step: '积语料', time: '7', content: '【PPT P4 语料库】学生填起因/方法/收获语料卡。板书时机：巡视。差异化提示：B班填词；A班造句。易错点提醒：broaden horizons 短语。' },
        { step: '搭提纲', time: '12', content: '【PPT P5 模板】学生用提纲卡搭博客骨架。教师：Outline your blog. 预设回答展示。板书时机：展示提纲。差异化提示：B班填空；A班自列。易错点提醒：建议用现在时。' }
      ],
      blackboard: '┌─ U5 Writing Ⅰ: 语言博客 ┐\n│ 结构: why→how→gain→advice │\n│ 时态: 经历过去/建议现在   │\n│ 语料: immerse/review/     │\n│  connect with/broaden…    │\n└────────────────────────────┘',
      exercises: '【基础作业】1. 完成博客提纲（四部分各≥2 点）。2. 整理方法词与收获表达各 5 个。【提高作业】用提纲写一段 80 词博客初稿。【参考答案——教师用】基础1示例：Why: to connect with people；How: practicing daily, immersing myself；Gained: made friends, broadened horizons；Advice: never give up.',
      reflection: '✅ 亮点：结构图+提纲让写作有骨架，B班提纲完成率高。⚠️ 需改进：时态仍混。📌 下节课衔接：下节起草成文+互评。'
    },
    // ===== P7 写作 Ⅱ =====
    {
      periodNumber: 7, lessonType: 'writing', duration: 45,
      title: 'Reading for Writing: A Language-Learning Blog (Ⅱ) — 起草与互评',
      textbookAnalysis: '第七课时，写作第二课时。基于提纲起草成文，运用时态切换与关系副词，经同伴互评修改定稿。',
      overview: '【学情分析】A班：能成段但时态偶尔滑回。B班：句子碎片化。共同问题：互评不知评什么，需量规引导。',
      objectives: [
        '语言能力：依据提纲写 80 词博客，正确使用时态切换与关系副词，段落连贯。',
        '文化意识：在分享中体现开放与坚持。',
        '思维品质：依据量规评价同伴作品并提出建议。',
        '学习能力：通过互评-修改循环提升自我修改能力。'
      ],
      keyPoints: '① 成段：四结构+衔接词。② 时态：经历过去/建议现在。③ 互评量规：结构/时态/语言/衔接。',
      difficulties: '① 时态滑回。② 关系副词选错。③ 博客语气与正式文不分。',
      teachingMethods: '① 过程写作：起草-互评-修改。② 量规引导互评。③ 教师面批聚焦时态。',
      preparation: '【PPT课件】P1 范文回顾；P2 量规表；P3 互评流程；P4 佳句展示；P5 常见问题。【实物教具】互评量规卡 printed。【音频】无。',
      process: [
        { step: '回顾要求', time: '5', content: '【PPT P1 范文】教师回顾结构+时态。预设回答跟读。板书时机：板书要点。差异化提示：B班跟读；A班复述。易错点提醒：经历用过去时。' },
        { step: '起草', time: '15', content: '【写作】学生依提纲起草 80 词。教师巡视面批。板书时机：无。差异化提示：B班给句型框；A班自由。易错点提醒：时态切换。' },
        { step: '互评', time: '12', content: '【PPT P2 量规】学生依量规评同伴。教师：Give one suggestion. 预设回答：Check the tense. 板书时机：展示量规。差异化提示：B班勾选；A班写建议。易错点提醒：评时态。' },
        { step: '修改', time: '8', content: '【修改】学生据互评修改。教师聚焦时态。板书时机：无。差异化提示：B班改错；A班润色。易错点提醒：滑回现在须改过去。' },
        { step: '展示', time: '5', content: '【PPT P4 佳句】展示佳句与修改对比。预设回答赏析。板书时机：圈亮点。差异化提示：B班跟读；A班点评。易错点提醒：关系副词。' }
      ],
      blackboard: '┌─ U5 Writing Ⅱ: 起草+互评 ┐\n│ 量规: 结构/时态/语言/衔接   │\n│ 时态: 经历过去/建议现在     │\n│ 流程: 起草→互评→修改→定稿   │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 定稿博客（≥80 词，四结构齐全）。2. 用红笔标出过去时与关系副词。【提高作业】为博客配一段 30 词结尾建议。【参考答案——教师用】基础1示范段：I started learning English to connect with people. I practiced every day and immersed myself in the language. The time when I made my first foreign friend was exciting. My advice is to never give up.',
      reflection: '✅ 亮点：量规让互评有抓手，A班时态准确率提升。⚠️ 需改进：B班句子碎片化。📌 下节课衔接：进入项目——综合单元产出外语节/语言文化海报。'
    },
    // ===== P8 项目复习 =====
    {
      periodNumber: 8, lessonType: 'project', duration: 45,
      title: 'Project & Unit Review: Foreign Language Festival — 外语节与语言文化海报',
      textbookAnalysis: '第八课时，单元综合产出。小组为一种外语或汉字文化制作介绍海报，综合运用词汇、关系副词、博客语料，并策划迷你外语节展示。',
      overview: '【学情分析】A班：综合运用能力可，但展示语言需规范。B班：表达碎片，需模板与分工支持。共同问题：海报文体特征（标题+简介+亮点+号召）体现不足。',
      objectives: [
        '语言能力：综合运用单元词汇与关系副词，以海报文体介绍一门语言或文字文化。',
        '文化意识：在介绍中体现对语言多样性的尊重与自豪。',
        '思维品质：统筹简介—亮点—建议，做有吸引力的表达。',
        '学习能力：通过小组协作完成从策划到展示的完整项目。'
      ],
      keyPoints: '① 文体：海报（标题+简介+亮点+号召）。② 语言：关系副词+建议句+时态切换。③ 产出：海报+口头推介。',
      difficulties: '① 文体退化成流水账。② 小组分工不均。③ 口头推介缺互动。',
      teachingMethods: '① 项目式学习（PBL）。② 小组分工+量规。③ 展示互评。',
      preparation: '【PPT课件】P1 项目说明+样例；P2 海报模板；P3 评价量规；P4 展示流程；P5 单元知识图。【实物教具】A4 海报纸 printed 每组；彩笔。【音频】无。',
      process: [
        { step: '任务发布', time: '6', content: '【PPT P1 说明】教师发布任务：制作语言/文字文化海报。预设回答讨论。板书时机：板书要求。差异化提示：B班用模板；A班自创。易错点提醒：海报四要素。' },
        { step: '小组策划', time: '12', content: '【PPT P2 模板】小组分工：简介/亮点/建议/文案。教师巡视。预设回答讨论。板书时机：无。差异化提示：B班填模板；A班设计。易错点提醒：用关系副词。' },
        { step: '制作海报', time: '12', content: '【实物 海报】小组图文制作。教师指导文体与语言。板书时机：无。差异化提示：B班配图；A班写文案。易错点提醒：号召语收尾。' },
        { step: '展示', time: '10', content: '【PPT P4 流程】各组用关系副词+建议句推介。教师：Present your language. 预设回答展示。板书时机：无。差异化提示：B班读卡；A班脱稿。易错点提醒：用 Discover…/Learn… 号召。' },
        { step: '评价+回顾', time: '5', content: '【PPT P3 量规+P5 知识图】互评+单元回顾。预设回答跟读。板书时机：圈重点。差异化提示：B班勾选；A班自评。易错点提醒：单元核心关系副词/语言词回顾。' }
      ],
      blackboard: '┌─ U5 Project & Review ┐\n│ 任务: 语言/文字文化海报 │\n│ 文体: 标题+简介+亮点+号召│\n│ 语言: 关系副词+建议句   │\n│ 产出: 海报 + 口头推介   │\n└──────────────────────────┘',
      exercises: '【基础作业】1. 完善海报（含四要素）。2. 写一段 60 词语言推介（含 2 处关系副词）。【提高作业】为海报设计迷你外语节活动方案。【参考答案——教师用】基础2示范：Chinese is a language that dates back thousands of years. The place where it began is full of history. Learning it connects you with a rich culture. Discover the beauty of Chinese characters with us!',
      reflection: '✅ 亮点：海报产出综合性强，A班文体特征明显。⚠️ 需改进：B班分工不均。📌 下节课衔接：必修一全部完成，进入必修二 Cultural Heritage，话题转向文化遗产保护。'
    }
  ]
};

const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const oldLessons = require('../data/lessons.js');
const newLessons = replaceUnit(oldLessons, SPEC);
fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(newLessons, null, 2) + ';\n', 'utf8');

const u5 = newLessons.filter(l => l.book === SPEC.book && l.unitNumber === SPEC.unitNumber);
const ids = newLessons.map(l => l.id);
const dup = ids.filter((x, i) => ids.indexOf(x) !== i);
console.log('U5 periods:', u5.length, '(expect 8)');
console.log('Total lessons:', newLessons.length);
console.log('Duplicate ids:', dup.length ? dup : 'none');
console.log('必修第一册 total:', newLessons.filter(l => l.book === '必修第一册').length);
u5.forEach(l => console.log('  p' + l.periodNumber, l.lessonType, '|', l.title.slice(0, 40)));
