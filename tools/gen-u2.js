// tools/gen-u2.js
// 必修一 Unit 2 Travelling Around —— 8 课时金标准教案生成
// 运行: node tools/gen-u2.js  （自动替换该单元旧课、写回 data/lessons.js）
const fs = require('fs');
const path = require('path');
const { replaceUnit } = require('./unit-template');

const SPEC = {
  book: '必修第一册',
  bookLabel: '必修一',
  unitNumber: 2,
  unitTitle: 'Travelling Around',
  periods: [
    // ===== P1 听与说 =====
    {
      periodNumber: 1, lessonType: 'listening-speaking', duration: 40,
      title: 'Listening and Speaking: Getting Ready to Travel — 行前准备与旅行计划',
      textbookAnalysis: '本课为必修第一册 Unit 2 Travelling Around 第一课时（Listening and Speaking），位于单元导入。主题为出行前的准备（订票、办签证、租车、打包）。听力为两段对话：首段为行前清单核对，次段为讨论出行计划。本课为后续读秘鲁、写旅行计划奠定话题与词汇基础。',
      overview: '【学情分析】A班：初中已掌握 travel/trip/hotel 等基础词，能听懂慢速对话；但 apply for a visa、book a hotel room、rent a car 等短语搭配不熟，输出易逐词翻译。B班：能识别单句信息，但连续对话中多任务并列（订票+打包+租车）易遗漏。共同问题：口语表达多停留在 I go to...，缺 I am planning to / I would like to 的得体句式。',
      objectives: [
        '语言能力：听懂行前准备对话的主旨与关键细节（出行方式、必备物品），用 be going to / I would like to 表达旅行计划。',
        '文化意识：了解出境旅行的常规准备流程（护照、签证、订房），培养规划意识与守时守约态度。',
        '思维品质：按交通—住宿—物品分类梳理准备清单，培养条理化规划能力。',
        '学习能力：借助出行准备清单图表自主记录听力要点并复述。'
      ],
      keyPoints: '① 核心短语：apply for a visa / book a hotel room / rent a car / pack some clothes / get a passport / buy a guidebook。② 句式：I am planning to... / I would like to... / Have you booked... yet? ③ 听力策略：先看清单预测，再听验证。',
      difficulties: '① book 作动词预订与名词书混淆。原因：一词多义，需语境固化。② pack 与 package 形近意近易混。提醒：pack 打包(动词)/package 包裹(名词)。③ I am leaving next Monday 现在进行时表将来，学生易误用 will。',
      teachingMethods: '① 任务型（TBL）：以帮同伴列出行清单为终任务。② 听前预测+听中填表：用清单作脚手架。③ 小组合作：两两核对清单查漏补缺。',
      preparation: '【PPT课件】P1 单元封面（Travelling Around）；P2 出行准备图片九宫格（护照/签证/机票/酒店/行李箱/地图/相机/指南/租车）；P3-4 听力任务题；P5 句型板；P6 说话任务卡。【实物教具】空白出行准备清单表 printed 每组一份；护照/机票道具卡片。【音频】听力两段音频（教材配套）。',
      process: [
        { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine pictures. Which three do you need for a trip abroad? 预设回答：Passport, ticket, money! 板书时机：右侧板书 passport / visa / ticket。差异化提示：B班指图说中文再跟读；A班用 I need... 造句。易错点提醒：visa 读作 /viːzə/，注意 s 浊化。' },
        { step: '词汇输入', time: '8', content: '【PPT P3 短语卡】教师领读并造例：book a hotel room = 预订酒店房间。教师：What must you do before you fly? 预设回答：Book a ticket / get a passport. 板书时机：板书六短语于左栏。差异化提示：B班短语配图记忆；A班用短语造完整句。易错点提醒：book(预订) 不等于 book(书)，标词性 v./n.。' },
        { step: '听前预测', time: '5', content: '【PPT P4 清单表】教师：Before listening, guess what the speaker will pack. 预设回答：Clothes, camera, passport. 板书时机：清单表留空待填。差异化提示：B班只勾已给选项；A班自行补充。易错点提醒：预测不必全对，重在激活。' },
        { step: '听中填表', time: '10', content: '【音频 段一】播放听力，学生填清单。教师：What did he book? 预设回答：A hotel room and a flight. 板书时机：核对答案时板书关键词。差异化提示：B班听两遍；A班一遍后复述。易错点提醒：flight /flaɪt/ 与 fright 区分。' },
        { step: '听后核对+句型', time: '7', content: '【PPT P5 句型板】教师：How to talk about plans? — I am planning to... / I would like to... 预设回答跟读。板书时机：句型板书于中央。差异化提示：B班套用模板；A班替换动词扩展。易错点提醒：planning 双写 n。' },
        { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，用清单+句型互问出行计划。教师：Tell your partner your plan and what you have prepared. 预设回答：I am planning to visit Xi an. I have booked a hotel. 板书时机：无。差异化提示：B班用填空式对话；A班自由问答。易错点提醒：用现在进行时表将来计划。' }
      ],
      blackboard: '┌─ U2 Listening & Speaking ─┐\n│ Prepare: passport / visa / ticket │\n│ book a room · rent a car · pack   │\n│ I am planning to… / I would like to…   │\n│ → 清单(交通/住宿/物品)             │\n└────────────────────────────────────┘',
      exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有出行准备短语。2. 用 I am planning to… 写 3 句旅行计划。【提高作业】为一次三日游列中英文出行准备清单（交通/住宿/物品三类各≥3 项）。【参考答案——教师用】基础2示例：I am planning to visit Chengdu next month. / I am planning to rent a car there. / I am planning to book a hotel near the city center.',
      reflection: '✅ 亮点：九宫格激活+清单脚手架有效降听力焦虑，B班填表完成率高。⚠️ 需改进：短语 book 多义学生仍混，下节需强化语境。📌 下节课衔接：进入阅读 Peru，将准备延伸到了解目的地。'
    },
    // ===== P2 阅读 Ⅰ =====
    {
      periodNumber: 2, lessonType: 'reading', duration: 45,
      title: 'Reading and Thinking: Travel Peru (Ⅰ) — 整体理解',
      textbookAnalysis: '本课为第二课时，语篇为 Travel Peru 旅游手册（brochure），介绍秘鲁地理（Amazon Rainforest、Machu Picchu、Cusco、Lake Titicaca）与四条旅行路线。本节聚焦整体理解：识别语篇类型与文本特征，提取四条路线关键信息。',
      overview: '【学情分析】A班：能读懂描述性文字，但旅游手册的图文混排、标题-短段结构不熟，易逐句翻译。B班：长难句（定语从句修饰景点）理解吃力，需图表辅助。共同问题：对秘鲁地理陌生，Amazon/Andes 等专名发音与定位困难。',
      objectives: [
        '语言能力：用略读识别语篇类型（travel brochure）及四条路线主题，用扫读提取时长、交通、亮点细节。',
        '文化意识：了解秘鲁多元地貌与印加文明，尊重世界文化遗产。',
        '思维品质：用表格对比四条路线（时长/交通/亮点），培养分类比较能力。',
        '学习能力：借助路线对比表自主梳理信息并复述。'
      ],
      keyPoints: '① 语篇特征：brochure——标题+短段+图片+号召语。② 四路线：Amazon Rainforest Tour / Machu Picchu Tour / Cusco Tour / Lake Titicaca Tour。③ 词汇：destination, brochure, package tour, unique, ancient。',
      difficulties: '① ancient /eɪnʃənt/ 中 t 不发音，易误读。原因：字母组合规律不熟。② unique 以辅音音素 /j/ 开头，用 a unique 而非 an unique。③ 长难句 which runs along... 定语从句修饰景点，学生易断句错误。',
      teachingMethods: '① 图式激活：先看秘鲁地图预测。② 略读+扫读分层任务。③ 表格对比：四路线并列梳理。',
      preparation: '【PPT课件】P1 秘鲁地图（Amazon/Andes/Machu Picchu/Cusco/Lake Titicaca 标注）；P2 brochure 文本特征标注；P3 四路线卡片；P4 对比表；P5 复述脚手架。【实物教具】秘鲁地图挂图；四路线词条卡。【音频】无。',
      process: [
        { step: '图式激活', time: '5', content: '【PPT P1 地图】教师：Where is Peru? What do you know about it? 预设回答：South America. Machu Picchu. 板书时机：板书 Peru / South America。差异化提示：B班指图说中文；A班用英语描述位置。易错点提醒：Peru /pəruː/ 重音在尾。' },
        { step: '语篇类型识别', time: '7', content: '【PPT P2 文本特征】教师：What kind of text is this? How do you know? 预设回答：A travel brochure. It has titles and pictures. 板书时机：板书 brochure。差异化提示：B班看图片判断；A班找标题-短段结构。易错点提醒：brochure /brəʊʃʊr/ 发音。' },
        { step: '略读路线', time: '8', content: '【PPT P3 路线卡】教师：Skim and find the four tours. 预设回答列出四路线名。板书时机：左栏列四路线。差异化提示：B班只找路线名；A班记时长。易错点提醒：Machu Picchu /mætʃuː piːtʃuː/。' },
        { step: '扫读填表', time: '12', content: '【PPT P4 对比表】学生填四路线时长/交通/亮点。教师：How long is the Amazon tour? 预设回答：Four days. 板书时机：核对答案填表。差异化提示：B班给填空表；A班自填。易错点提醒：travel by boat / on foot 介词。' },
        { step: '复述', time: '8', content: '【PPT P5 脚手架】学生用表复述一条路线。教师：Describe one tour using the table. 预设回答：The Cusco Tour lasts four days. You can visit museums. 板书时机：无。差异化提示：B班照表读；A班脱稿。易错点提醒：lasts 第三人称单数加 s。' },
        { step: '小结', time: '5', content: '【总结】教师带学生回顾 brochure 特征+四路线。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：ancient /eɪnʃənt/ t 不发音。' }
      ],
      blackboard: '┌─ U2 Reading Ⅰ: Travel Peru ─┐\n│ Type: travel brochure           │\n│ ① Amazon ② Machu Picchu        │\n│ ③ Cusco  ④ Lake Titicaca       │\n│ (duration / transport / highlight)│\n└──────────────────────────────────┘',
      exercises: '【基础作业】1. 完成四路线对比表（时长/交通/亮点）。2. 用 5 句话复述一条路线。【提高作业】比较两条路线，写一段 60 词推荐语。【参考答案——教师用】基础2示例：The Machu Picchu Tour lasts four days. You travel on foot. The highlight is the ancient Inca city.',
      reflection: '✅ 亮点：地图+表格让陌生地理可视化，A班对比能力提升明显。⚠️ 需改进：专名发音练习不足，部分学生仍读错 Machu Picchu。📌 下节课衔接：进入语言深度，细读长难句与特色表达。'
    },
    // ===== P3 阅读 Ⅱ =====
    {
      periodNumber: 3, lessonType: 'reading', duration: 45,
      title: 'Reading and Thinking: Travel Peru (Ⅱ) — 语言深度',
      textbookAnalysis: '第三课时，沿用 Peru 语篇，聚焦语言深度：赏析描述性词汇与号召语，破解定语从句长难句，为写作积累语料。',
      overview: '【学情分析】A班：能懂大意但忽视语言地道性，描述景点仍用 very beautiful。B班：定语从句识别困难，which/that 指代不清。共同问题：号召语（Enjoy the beautiful countryside…）的语用功能不熟。',
      objectives: [
        '语言能力：识别并运用描述景点的地道表达（breathtaking, amazing, unique, ancient）与号召语句式。',
        '文化意识：体会旅游手册吸引读者的语用目的与表达策略。',
        '思维品质：辨析客观描述与主观评价用语差异。',
        '学习能力：建立景点描述语料库供写作调用。'
      ],
      keyPoints: '① 描述词：breathtaking / amazing / unique / ancient / spectacular。② 号召语：Enjoy… / Explore… / Discover…。③ 长难句拆解：主句+which/that 定语从句。',
      difficulties: '① breathtaking 由 breath+taking 复合，学生望文生义误读。原因：构词法不熟。② which 与 that 在非限制性定语从句中的取舍。③ 形容词修饰名词语序（a unique ancient city）。',
      teachingMethods: '① 语篇研读：圈画特色表达。② 句法拆解：长难句主干+从句分层。③ 语料库搭建：分类积累。',
      preparation: '【PPT课件】P1 语篇（高亮描述词）；P2 号召语集锦；P3 长难句拆解动画；P4 语料库模板；P5 仿写练习。【实物教具】语料卡 printed。【音频】无。',
      process: [
        { step: '圈画特色词', time: '8', content: '【PPT P1 高亮】教师：Find words that describe places. 预设回答：breathtaking, amazing, ancient. 板书时机：板书描述词。差异化提示：B班找已高亮词；A班自找。易错点提醒：breathtaking /breθteɪkɪŋ/。' },
        { step: '号召语赏析', time: '7', content: '【PPT P2 号召语】教师：How does the writer attract you? — Enjoy… / Explore… 预设回答跟读。板书时机：板书动词。差异化提示：B班套用模板；A班改写。易错点提醒：号召语用祈使句，无主语。' },
        { step: '长难句拆解', time: '12', content: '【PPT P3 拆解】教师取一句带 which 从句，先找主干再分从句：What does which refer to? 预设回答：The lake. 板书时机：画从句括号。差异化提示：B班只找指代；A班翻译全句。易错点提醒：which 指物，非限制定语从句只用 which。' },
        { step: '语料库搭建', time: '10', content: '【PPT P4 模板】学生分类填语料卡：描述词/号召语/句式。板书时机：巡视指导。差异化提示：B班填词；A班造句。易错点提醒：a unique（不是 an unique）。' },
        { step: '仿写', time: '8', content: '【PPT P5 练习】学生用语料库仿写一句景点介绍。教师：Describe a place you know. 预设回答：Discover the ancient city, which is breathtaking. 板书时机：展示佳句。差异化提示：B班填空式；A班自由写。易错点提醒：定语从句逗号+which。' }
      ],
      blackboard: '┌─ U2 Reading Ⅱ: 语言深度 ─┐\n│ 描述: breathtaking/amazing/unique │\n│ 号召: Enjoy… / Explore… / Discover… │\n│ 长难句: 主干 + (which…)            │\n└────────────────────────────────────┘',
      exercises: '【基础作业】1. 整理语料库（描述词≥5、号召语≥3）。2. 拆解并翻译文中一句 which 从句长难句。【提高作业】用语料库写一段 50 词景点介绍（含 1 句定语从句）。【参考答案——教师用】基础2示例：The Amazon Rainforest, which covers a large area, is a breathtaking destination.（主干: The Amazon Rainforest is a destination；从句: which covers a large area 修饰主语。）',
      reflection: '✅ 亮点：语料库让语言可迁移，A班仿写质量提升。⚠️ 需改进：which/that 取舍讲解偏快，B班仍混。📌 下节课衔接：进入语法——现在进行时表将来，为说计划奠基。'
    },
    // ===== P4 语法 =====
    {
      periodNumber: 4, lessonType: 'grammar', duration: 45,
      title: 'Discovering Useful Structures: 现在进行时表将来',
      textbookAnalysis: '第四课时，语法点：现在进行时（be doing）表示按计划即将发生的将来动作，常用于出行安排（I am leaving tomorrow / We are flying to Peru）。',
      overview: '【学情分析】A班：知道 be doing 表进行，但用于将来时易与 will 混。B班：be 动词随主语变化（am/is/are）仍出错。共同问题：缺时间状语时不敢用进行时表将来。',
      objectives: [
        '语言能力：识别并用现在进行时表达已安排的将来计划，区分其与 will 的语用差异。',
        '文化意识：体会计划性表达的得体性——已定 vs 预测。',
        '思维品质：对比 be doing（已安排）与 will（临决定/预测），培养语境判断力。',
        '学习能力：用时间轴图表归纳将来表达的多种形式。'
      ],
      keyPoints: '① 结构：主语 + am/is/are + doing。② 用法：已安排的将来计划，常配时间状语。③ 与 will 区别：be doing=已定，will=临决/预测。',
      difficulties: '① be 动词随主语：I am / He is / They are，学生漏改。原因：母语无形变化。② come/go/leave/arrive 等位移动词最常用进行时表将来。③ will 与 be doing 混用——前者无计划性。',
      teachingMethods: '① 归纳法：从例句发现规则。② 对比法：be doing vs will。③ 情境操练：用出行计划语境。',
      preparation: '【PPT课件】P1 例句（文中+生活）；P2 归纳表格；P3 be doing vs will 对比；P4 时间轴；P5 操练题。【实物教具】无。【音频】无。',
      process: [
        { step: '观察例句', time: '7', content: '【PPT P1 例句】教师：Read: I am leaving for Peru next week. What time does it express? 预设回答：Future. 板书时机：板书例句。差异化提示：B班判断时态；A班说理由。易错点提醒：leaving 表将来，非进行。' },
        { step: '归纳结构', time: '8', content: '【PPT P2 表格】师生归纳 主语+am/is/are+doing。教师：What form after I? after He? 预设回答：am / is. 板书时机：填表。差异化提示：B班填 be 动词；A班补例句。易错点提醒：He is coming（不是 He am）。' },
        { step: '对比 will', time: '10', content: '【PPT P3 对比】教师：I am flying tomorrow（已订票）vs I will fly tomorrow（打算/临决）. 预设回答辨析。板书时机：对比双栏。差异化提示：B班选填；A班解释差异。易错点提醒：be doing 强调已安排。' },
        { step: '时间轴归纳', time: '8', content: '【PPT P4 时间轴】归纳将来表达：be doing / will / be going to。板书时机：画轴。差异化提示：B班填词；A班举例。易错点提醒：be going to 表打算+迹象。' },
        { step: '操练', time: '12', content: '【PPT P5 题】学生用 be doing 改写出行计划句。教师：Rewrite: I will fly to Xi an tomorrow. → ? 预设回答：I am flying to Xi an tomorrow. 板书时机：展示。差异化提示：B班选择式；A班改写。易错点提醒：fly→flying 不双写。' }
      ],
      blackboard: '┌─ U2 Grammar: be doing → future ┐\n│ S + am/is/are + V-ing          │\n│ = 已安排的计划(配时间状语)       │\n│ be doing(已定) vs will(临决/预测)│\n│ come/go/leave/arrive 高频       │\n└──────────────────────────────────┘',
      exercises: '【基础作业】1. 用 be doing 改写 5 句将来计划。2. 辨析 be doing 与 will 各 3 例。【提高作业】写一段 50 词周末计划，至少 3 处 be doing。【参考答案——教师用】基础1示例：She is arriving at 8 tomorrow. / We are visiting the museum on Sunday. / He is leaving next Monday.',
      reflection: '✅ 亮点：时间轴+对比让语用差异清晰，A班改写准确率高。⚠️ 需改进：be 动词随主语 B 班仍漏改，需专项。📌 下节课衔接：进入听与谈——用 be doing 进行旅行预订角色扮演。'
    },
    // ===== P5 听与谈 =====
    {
      periodNumber: 5, lessonType: 'listening-talking', duration: 40,
      title: 'Listening and Talking: Book a Trip — 预订与咨询',
      textbookAnalysis: '第五课时，听说结合。听力为预订旅行（订票/订房/问交通）对话；口语为角色扮演客服与旅客，运用 be doing 与咨询句式。',
      overview: '【学情分析】A班：能说单句但角色扮演衔接生硬，缺礼貌用语。B班：听数字（价格、时间）易错，需预教。共同问题：How much / What time 句式熟练，但 I would like to book… 开场不熟。',
      objectives: [
        '语言能力：听懂预订对话中的价格、时间、房型等细节；用 I would like to book… / How much is…? 完成预订角色扮演。',
        '文化意识：体验英语国家电话预订的礼貌表达与确认习惯。',
        '思维品质：在信息不对称的交际中主动澄清与确认。',
        '学习能力：用预订信息卡记录关键信息并核对。'
      ],
      keyPoints: '① 句式：I would like to book… / How much is it? / What time does it leave? ② 听数字：价格、时间。③ 礼貌语：Could you…? / I would appreciate…',
      difficulties: '① -teen 与 -ty 数字（thirteen/thirty）听力混淆。原因：发音差异小。② I would like to 后接动词原形，学生加 to+ing。③ 预订确认时重复信息易遗漏。',
      teachingMethods: '① 情境模拟：电话预订角色扮演。② 听前预教数字。③ 信息卡记录。',
      preparation: '【PPT课件】P1 预订场景图；P2 数字辨析；P3 听力任务；P4 角色卡；P5 句型板。【实物教具】预订信息卡 printed；电话道具。【音频】听力音频。',
      process: [
        { step: '数字预教', time: '7', content: '【PPT P2 数字】教师辨析 thirteen/thirty, fourteen/forty。预设回答跟读。板书时机：板书对比。差异化提示：B班听辨；A班速读。易错点提醒：-teen 重音在后，-ty 重音在前。' },
        { step: '听前预测', time: '5', content: '【PPT P3 任务】教师：What info will you hear? 预设回答：Price, time, room. 板书时机：信息卡留空。差异化提示：B班勾选项；A班自列。易错点提醒：留意货币单位。' },
        { step: '听中记录', time: '10', content: '【音频】播放，学生填信息卡。教师：How much is the room? 预设回答：120 dollars. 板书时机：核对填卡。差异化提示：B班听两遍；A班一遍。易错点提醒：a hundred and twenty 连读。' },
        { step: '句型输入', time: '6', content: '【PPT P5 句型】教师：I would like to book a room. How much is it? 预设回答跟读。板书时机：板书句型。差异化提示：B班套用；A班扩展。易错点提醒：I would like to + 原形。' },
        { step: '角色扮演', time: '12', content: '【PPT P4 角色卡】学生分客服/旅客，用信息卡+句型完成预订。教师巡视。预设回答：I would like to book a double room for two nights. 板书时机：无。差异化提示：B班用脚本；A班自由。易错点提醒：确认信息时复述。' }
      ],
      blackboard: '┌─ U2 Listening & Talking ┐\n│ I would like to book…        │\n│ How much is it? / What time? │\n│ -teen vs -ty 数字辨析     │\n│ → 预订信息卡(房型/价格/时间)│\n└────────────────────────────┘',
      exercises: '【基础作业】1. 听录音补全预订信息卡。2. 用 I would like to… 写 3 句预订请求。【提高作业】编写一段 8 轮电话预订对话。【参考答案——教师用】基础2示例：I would like to book a single room for three nights. / I would like to reserve a table for two. / I would like to book a flight to Shanghai.',
      reflection: '✅ 亮点：角色卡+信息卡让交际真实，B班参与度高。⚠️ 需改进：-teen/-ty 听辨仍弱，需持续。📌 下节课衔接：进入写作——读模型后写旅行计划。'
    },
    // ===== P6 写作 Ⅰ =====
    {
      periodNumber: 6, lessonType: 'writing', duration: 45,
      title: 'Reading for Writing: A Travel Plan (Ⅰ) — 读析与语料',
      textbookAnalysis: '第六课时，写作第一课时。先读模型旅行计划（含目的地、交通、行程、期待），分析结构与语言，积累语料，为下节起草奠基。',
      overview: '【学情分析】A班：能写单句但段落结构松散，缺衔接词。B班：时态混乱（计划用 will/do 而非 be doing）。共同问题：旅行计划易写成流水账，缺期待与理由。',
      objectives: [
        '语言能力：识别旅行计划范文的结构（目的地-交通-行程-期待）与衔接手段，积累相关语料。',
        '文化意识：在计划中表达对目的地的合理期待与文化尊重。',
        '思维品质：按时间顺序与逻辑层级组织计划。',
        '学习能力：用计划提纲模板自主搭建写作骨架。'
      ],
      keyPoints: '① 结构：destination → transport → itinerary → expectation。② 衔接词：first, then, after that, finally。③ 时态：用 be doing 表已定行程。',
      difficulties: '① 时态选择：计划用 be doing/be going to，学生混 will。② itinerary 生词，拼写难。③ 期待句式 I am looking forward to + 名词/doing，学生加原形。',
      teachingMethods: '① 范文研读：圈结构+语言。② 提纲搭建。③ 语料积累。',
      preparation: '【PPT课件】P1 范文（分段）；P2 结构图；P3 衔接词；P4 语料库；P5 提纲模板。【实物教具】提纲卡 printed。【音频】无。',
      process: [
        { step: '读范文', time: '8', content: '【PPT P1 范文】教师：Read the model. What is it about? 预设回答：A travel plan to Xi an. 板书时机：板书主题。差异化提示：B班抓大意；A班找结构。易错点提醒：plan 作名词读 /plæn/。' },
        { step: '析结构', time: '10', content: '【PPT P2 结构图】师生分四段：destination/transport/itinerary/expectation。教师：Which part tells how to get there? 预设回答：Transport. 板书时机：填结构图。差异化提示：B班匹配；A班归纳。易错点提醒：itinerary /aɪtɪnərəri/。' },
        { step: '找衔接词', time: '7', content: '【PPT P3 衔接词】教师圈 first/then/after that/finally。预设回答跟读。板书时机：板书衔接词。差异化提示：B班认读；A班替换。易错点提醒：after that 后接句子。' },
        { step: '积语料', time: '8', content: '【PPT P4 语料库】学生填目的地/交通/活动/期待语料卡。板书时机：巡视。差异化提示：B班填词；A班造句。易错点提醒：look forward to + doing。' },
        { step: '搭提纲', time: '12', content: '【PPT P5 模板】学生用提纲卡搭自己计划的骨架。教师：Outline your own travel plan. 预设回答展示。板书时机：展示提纲。差异化提示：B班填空；A班自列。易错点提醒：行程用 be doing。' }
      ],
      blackboard: '┌─ U2 Writing Ⅰ: 旅行计划 ┐\n│ 结构: destination→transport   │\n│        →itinerary→expectation │\n│ 衔接: first/then/after that/finally │\n│ 时态: be doing(已定行程)       │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 完成旅行计划提纲（四部分各≥2 点）。2. 整理衔接词与期待表达各 5 个。【提高作业】用提纲写一段 80 词旅行计划初稿。【参考答案——教师用】基础1示例：Destination: Xi an；Transport: taking a high-speed train；Itinerary: visiting the Terracotta Warriors, cycling on the City Wall；Expectation: looking forward to the local food.',
      reflection: '✅ 亮点：结构图+提纲让写作有骨架，B班提纲完成率高。⚠️ 需改进：look forward to + doing 仍有人加原形。📌 下节课衔接：下节起草成文+互评。'
    },
    // ===== P7 写作 Ⅱ =====
    {
      periodNumber: 7, lessonType: 'writing', duration: 45,
      title: 'Reading for Writing: A Travel Plan (Ⅱ) — 起草与互评',
      textbookAnalysis: '第七课时，写作第二课时。基于上节提纲起草成文，运用衔接词与 be doing，经同伴互评修改定稿。',
      overview: '【学情分析】A班：能成段但衔接生硬、时态偶尔滑回。B班：句子碎片化，缺主语。共同问题：互评不知评什么，需量规引导。',
      objectives: [
        '语言能力：依据提纲写 80 词旅行计划，正确使用 be doing 与衔接词，段落连贯。',
        '文化意识：在计划中体现对目的地的尊重与合理期待。',
        '思维品质：依据量规评价同伴作品并提出改进建议。',
        '学习能力：通过互评-修改循环提升自我修改能力。'
      ],
      keyPoints: '① 成段：四结构+衔接词。② 时态：be doing 表已定。③ 互评量规：结构/语言/衔接/时态。',
      difficulties: '① 时态滑回 will/do。② 衔接词滥用（每句都加 first）。③ 互评流于表面，需量规引导深入。',
      teachingMethods: '① 过程写作：起草-互评-修改。② 量规引导互评。③ 教师面批聚焦。',
      preparation: '【PPT课件】P1 范文回顾；P2 量规表；P3 互评流程；P4 佳句展示；P5 常见问题。【实物教具】互评量规卡 printed。【音频】无。',
      process: [
        { step: '回顾要求', time: '5', content: '【PPT P1 范文】教师回顾结构+时态要求。预设回答跟读。板书时机：板书要点。差异化提示：B班跟读；A班复述。易错点提醒：be doing 表已定。' },
        { step: '起草', time: '15', content: '【写作】学生依提纲起草 80 词。教师巡视面批。板书时机：无。差异化提示：B班给句型框；A班自由。易错点提醒：衔接词适度。' },
        { step: '互评', time: '12', content: '【PPT P2 量规】学生依量规评同伴：结构/语言/衔接/时态各打分。教师：Give one suggestion. 预设回答：Add a transition. 板书时机：展示量规。差异化提示：B班勾选；A班写建议。易错点提醒：评具体不评笼统。' },
        { step: '修改', time: '8', content: '【修改】学生据互评修改。教师聚焦时态错误。板书时机：无。差异化提示：B班改错；A班润色。易错点提醒：滑回 will 须改 be doing。' },
        { step: '展示', time: '5', content: '【PPT P4 佳句】展示佳句与修改对比。预设回答赏析。板书时机：圈亮点。差异化提示：B班跟读；A班点评。易错点提醒：look forward to + doing。' }
      ],
      blackboard: '┌─ U2 Writing Ⅱ: 起草+互评 ┐\n│ 量规: 结构/语言/衔接/时态   │\n│ 时态: be doing(已定)        │\n│ 流程: 起草→互评→修改→定稿   │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 定稿旅行计划（≥80 词，四结构齐全）。2. 用红笔标出 be doing 与衔接词。【提高作业】为计划配一段 30 词期待结尾，含 look forward to。【参考答案——教师用】基础1示范段：I am travelling to Xi an next month. First, I am taking a high-speed train. Then, I am visiting the Terracotta Warriors. After that, I am cycling on the City Wall. Finally, I am looking forward to the local food.',
      reflection: '✅ 亮点：量规让互评有抓手，A班修改后时态准确率提升。⚠️ 需改进：B班句子碎片化，下单元需强化主谓完整。📌 下节课衔接：进入项目——综合单元产出旅行手册/路线。'
    },
    // ===== P8 项目复习 =====
    {
      periodNumber: 8, lessonType: 'project', duration: 45,
      title: 'Project & Unit Review: Design a Tourist Route — 设计旅行路线',
      textbookAnalysis: '第八课时，单元综合产出。小组为家乡或心仪城市设计一条 2–3 日旅行路线，综合运用词汇、be doing、brochure 文体与写作语料，制作图文路线卡并展示。',
      overview: '【学情分析】A班：综合运用能力可，但小组分工与展示语言需规范。B班：表达碎片，需模板与分工支持。共同问题：brochure 文体特征（标题+短段+号召语）在产出中体现不足。',
      objectives: [
        '语言能力：综合运用单元词汇与 be doing，以 brochure 文体介绍一条旅行路线。',
        '文化意识：在路线设计中呈现家乡/目的地的文化特色与价值。',
        '思维品质：统筹交通-住宿-活动-预算，做可行规划。',
        '学习能力：通过小组协作完成从策划到展示的完整项目。'
      ],
      keyPoints: '① 文体：brochure（标题+短段+号召语）。② 语言：be doing + 描述词 + 衔接词。③ 产出：路线卡+口头推介。',
      difficulties: '① 文体特征易退化成流水账。② 小组分工不均。③ 口头推介缺号召语。',
      teachingMethods: '① 项目式学习（PBL）：真实任务驱动。② 小组分工+量规。③ 展示互评。',
      preparation: '【PPT课件】P1 项目说明+样例；P2 路线卡模板；P3 评价量规；P4 展示流程；P5 单元知识图。【实物教具】A4 路线卡 printed 每组；彩笔；地图。【音频】无。',
      process: [
        { step: '任务发布', time: '6', content: '【PPT P1 说明】教师发布任务：为某城市设计 2–3 日路线卡。预设回答讨论。板书时机：板书要求。差异化提示：B班用模板；A班自创。易错点提醒：brochure 文体三要素。' },
        { step: '小组策划', time: '12', content: '【PPT P2 模板】小组分工：路线/交通/活动/文案。教师巡视。预设回答讨论。板书时机：无。差异化提示：B班填模板；A班设计。易错点提醒：be doing 写行程。' },
        { step: '制作路线卡', time: '12', content: '【实物 路线卡】小组图文制作。教师指导文体与语言。板书时机：无。差异化提示：B班配图；A班写文案。易错点提醒：号召语收尾。' },
        { step: '展示', time: '10', content: '【PPT P4 流程】各组用 be doing + 号召语口头推介。教师：Present your route. 预设回答展示。板书时机：无。差异化提示：B班读卡；A班脱稿。易错点提醒：用 Explore… / Discover… 收尾。' },
        { step: '评价+回顾', time: '5', content: '【PPT P3 量规+P5 知识图】互评+单元知识回顾。预设回答跟读。板书时机：圈重点。差异化提示：B班勾选；A班自评。易错点提醒：单元核心 be doing/词汇回顾。' }
      ],
      blackboard: '┌─ U2 Project & Review ┐\n│ 任务: 设计 2-3 日路线卡  │\n│ 文体: brochure(标题+短段+号召) │\n│ 语言: be doing+描述词+衔接 │\n│ 产出: 路线卡 + 口头推介   │\n└──────────────────────────┘',
      exercises: '【基础作业】1. 完善路线卡（含四结构+号召语）。2. 写一段 60 词路线推介（≥3 处 be doing）。【提高作业】为路线设计预算表并说明可行性。【参考答案——教师用】基础2示范：Discover Xi an in three days! First, we are visiting the Terracotta Warriors. Then, we are cycling on the City Wall. After that, we are tasting local food. Finally, we are looking forward to the amazing night view. Explore the ancient city with us!',
      reflection: '✅ 亮点：路线卡产出综合性强，A班文体特征明显。⚠️ 需改进：B班分工不均，下次须设角色卡。📌 下节课衔接：进入 Unit 3 Sports and Fitness，话题转向运动与健康。'
    }
  ]
};

// 执行替换并写回
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const oldLessons = require('../data/lessons.js');
const newLessons = replaceUnit(oldLessons, SPEC);
const out = 'module.exports = ' + JSON.stringify(newLessons, null, 2) + ';\n';
fs.writeFileSync(lessonsPath, out, 'utf8');

// 校验
const u2 = newLessons.filter(l => l.book === SPEC.book && l.unitNumber === SPEC.unitNumber);
const ids = newLessons.map(l => l.id);
const dup = ids.filter((x, i) => ids.indexOf(x) !== i);
console.log('U2 periods:', u2.length, '(expect 8)');
console.log('Total lessons:', newLessons.length);
console.log('Duplicate ids:', dup.length ? dup : 'none');
console.log('U2 titles:');
u2.forEach(l => console.log('  p' + l.periodNumber, l.lessonType, '|', l.title.slice(0, 40)));
