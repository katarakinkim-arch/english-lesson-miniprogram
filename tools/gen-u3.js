// tools/gen-u3.js
// 必修一 Unit 3 Sports and Fitness —— 8 课时金标准教案生成
const fs = require('fs');
const path = require('path');
const { replaceUnit } = require('./unit-template');

const SPEC = {
  book: '必修第一册', bookLabel: '必修一', unitNumber: 3, unitTitle: 'Sports and Fitness',
  periods: [
    // ===== P1 听与说 =====
    {
      periodNumber: 1, lessonType: 'listening-speaking', duration: 40,
      title: 'Listening and Speaking: Sports Events & Invitation — 运动赛事与邀请',
      textbookAnalysis: '本课为必修第一册 Unit 3 Sports and Fitness 第一课时（Listening and Speaking），单元导入。主题为运动项目与邀请同伴观赛/参赛。听力为两段对话：邀请观看比赛、谈论健身计划。本课为后续读 Living Legends、写体育传奇奠定话题与词汇基础。',
      overview: '【学情分析】A班：初中已掌握 football/basketball/swim 等常见运动词，但 boxing/badminton/marathon/track and field/gymnastics 等拼写与搭配不熟。B班：能听单句但连续对话中时间地点信息易混。共同问题：邀请表达停留在 Can you...?，缺 Would you like to...? 的得体句式与婉拒礼貌语。',
      objectives: [
        '语言能力：听懂运动赛事对话的主旨与关键细节（项目、时间、地点），用 Would you like to...? 得体邀请并接受/婉拒。',
        '文化意识：了解常见运动项目与观赛礼仪，培养积极参与体育的态度。',
        '思维品质：按项目—时间—地点分类梳理赛事信息，培养条理记录能力。',
        '学习能力：借助赛事信息卡自主记录听力要点并复述邀请对话。'
      ],
      keyPoints: '① 运动词：boxing / badminton / marathon / track and field / gym / gymnastics / skiing。② 邀请句：Would you like to...? / That sounds great! / I would love to, but... ③ 听力策略：先读信息卡预测，再听验证。',
      difficulties: '① marathon /mærəθən/ 中 th 发 /θ/，易读成 /s/。原因：舌位不清。② track and field（田径）为固定搭配，学生望文生义。③ 婉拒时 but 后接理由，学生直说 No 易显生硬。',
      teachingMethods: '① 任务型（TBL）：以邀请同伴观赛为终任务。② 听前预测+听中填卡。③ 角色扮演操练邀请。',
      preparation: '【PPT课件】P1 单元封面；P2 运动项目九宫格；P3-4 听力任务；P5 邀请句型板；P6 说话任务卡。【实物教具】赛事信息卡 printed；运动项目词条卡。【音频】听力两段（教材配套）。',
      process: [
        { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Which sports can you see? Have you ever watched a match? 预设回答：Basketball, badminton! 板书时机：板书运动词。差异化提示：B班指图说中文再跟读；A班用 I like... 造句。易错点提醒：marathon /mærəθən/ 的 th。' },
        { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 boxing/badminton/marathon/track and field/gymnastics。教师：Which needs a court? 预设回答：Badminton! 板书时机：左栏板书词。差异化提示：B班配图记忆；A班造句。易错点提醒：track and field 不可拆分理解。' },
        { step: '听前预测', time: '5', content: '【PPT P4 信息卡】教师：What info will you hear? 预设回答：Sport, time, place. 板书时机：信息卡留空。差异化提示：B班勾选项；A班自列。易错点提醒：留意 AM/PM。' },
        { step: '听中填卡', time: '10', content: '【音频 段一】播放，学生填信息卡。教师：What sport and when? 预设回答：Badminton, Saturday morning. 板书时机：核对填卡。差异化提示：B班听两遍；A班一遍后复述。易错点提醒：Saturday 拼写。' },
        { step: '句型输入', time: '7', content: '【PPT P5 句型板】教师：Would you like to watch a match with me? — That sounds great! / I would love to, but I have to... 预设回答跟读。板书时机：板书句型。差异化提示：B班套用；A班替换项目。易错点提醒：Would you like to + 原形。' },
        { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组互邀观赛。教师：Invite your partner to a match. 预设回答：Would you like to watch the basketball game? That sounds great! 板书时机：无。差异化提示：B班用脚本；A班自由。易错点提醒：婉拒须给理由。' }
      ],
      blackboard: '┌─ U3 Listening & Speaking ─┐\n│ Sports: boxing/badminton/marathon │\n│        track and field/gymnastics │\n│ Would you like to…?              │\n│ → That sounds great! / I would    │\n│   love to, but…                  │\n└────────────────────────────────────┘',
      exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有运动项目词。2. 用 Would you like to… 写 3 句邀请并各给一种回应。【提高作业】编写一段 6 轮邀请观赛对话（含接受与婉拒各一次）。【参考答案——教师用】基础2示例：Would you like to watch the marathon? — That sounds great! / Would you like to play badminton? — I would love to, but I have homework.',
      reflection: '✅ 亮点：九宫格+信息卡激活充分，B班填卡完成率高。⚠️ 需改进：marathon 发音仍有人读错，下节强化。📌 下节课衔接：进入阅读 Living Legends，从运动项目延伸到体育精神。'
    },
    // ===== P2 阅读 Ⅰ =====
    {
      periodNumber: 2, lessonType: 'reading', duration: 45,
      title: 'Reading and Thinking: Living Legends (Ⅰ) — 整体理解',
      textbookAnalysis: '第二课时，语篇 Living Legends 介绍两位体育传奇：郎平（排球运动员/教练）与迈克尔·乔丹（篮球）。本节聚焦整体理解：提取人物事迹与品质（determination, mental strength, 团队精神）。',
      overview: '【学情分析】A班：能读懂人物介绍但易逐句翻译，忽视品质提炼。B班：长难句（定语从句修饰人物）吃力。共同问题：对 Lang Ping/Jordan 背景了解不均，determination/mental strength 等抽象词理解浅。',
      objectives: [
        '语言能力：用略读获取两位传奇主旨，用扫读提取事迹与品质细节（荣誉、挑战、应对）。',
        '文化意识：理解体育精神（坚韧、团队、分享），树立积极人生观。',
        '思维品质：用人物信息表对比郎平与乔丹（身份/成就/品质），培养比较归纳能力。',
        '学习能力：借助人物信息表自主梳理并复述。'
      ],
      keyPoints: '① 人物：Lang Ping（player/coach/person）、Michael Jordan（Air Jordan）。② 品质词：determination / mental strength / teamwork / share success。③ 词汇：honour, glory, champion, injury, fall apart, lose heart。',
      difficulties: '① determination /dɪtɜːmɪneɪʃn/ 多音节词拼读难。原因：构词 deter+min+ation。② fall apart（分崩离析）短语义，学生直译。③ lose heart（灰心）≠ lose one heart，易混。',
      teachingMethods: '① 图式激活：预测何为传奇。② 略读+扫读分层。③ 人物信息表对比。',
      preparation: '【PPT课件】P1 两位传奇图片+成就；P2 语篇；P3 人物信息表；P4 品质词卡；P5 复述脚手架。【实物教具】人物信息表 printed。【音频】无。',
      process: [
        { step: '图式激活', time: '5', content: '【PPT P1 图片】教师：What makes a living legend? 预设回答：Great skill, strong mind. 板书时机：板书 legend。差异化提示：B班说中文；A班用英语。易错点提醒：legend /ledʒənd/。' },
        { step: '略读主旨', time: '8', content: '【PPT P2 语篇】教师：Who are the two legends? 预设回答：Lang Ping and Michael Jordan. 板书时机：板书人名。差异化提示：B班找人名；A班记身份。易错点提醒：Jordan /dʒɔːdn/。' },
        { step: '扫读填表', time: '12', content: '【PPT P3 信息表】学生填身份/成就/挑战/品质。教师：What challenge did Lang Ping face? 预设回答：Players injured, team falling apart. 板书时机：核对填表。差异化提示：B班给填空表；A班自填。易错点提醒：fall apart 不直译。' },
        { step: '品质提炼', time: '8', content: '【PPT P4 品质卡】教师：What qualities do they share? 预设回答：Determination, mental strength. 板书时机：板书品质词。差异化提示：B班找已给词；A班归纳。易错点提醒：determination 拼写。' },
        { step: '复述', time: '7', content: '【PPT P5 脚手架】学生用表复述一位传奇。教师：Describe one legend. 预设回答：Lang Ping led the team to medals. She did not lose heart. 板书时机：无。差异化提示：B班照表读；A班脱稿。易错点提醒：led 是 lead 过去式。' },
        { step: '小结', time: '5', content: '【总结】回顾传奇=技艺+精神+榜样。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：set an example for 树立榜样。' }
      ],
      blackboard: '┌─ U3 Reading Ⅰ: Living Legends ┐\n│ Lang Ping: player/coach/person  │\n│ Jordan: Air Jordan, mental str. │\n│ 品质: determination/teamwork/    │\n│       share success              │\n└──────────────────────────────────┘',
      exercises: '【基础作业】1. 完成两位传奇信息表（身份/成就/挑战/品质）。2. 用 5 句话复述一位传奇。【提高作业】写一段 60 词短文：你心中的体育传奇及其品质。【参考答案——教师用】基础2示例：Lang Ping was a great player and coach. She led China to medals. When the team fell apart, she did not lose heart. Her players won as a team. She shows determination.',
      reflection: '✅ 亮点：人物表让对比清晰，A班品质归纳到位。⚠️ 需改进：抽象词 determination 拼写仍弱。📌 下节课衔接：进入语言深度，赏析 make sb.+adj、-ing 主语等结构。'
    },
    // ===== P3 阅读 Ⅱ =====
    {
      periodNumber: 3, lessonType: 'reading', duration: 45,
      title: 'Reading and Thinking: Living Legends (Ⅱ) — 语言深度',
      textbookAnalysis: '第三课时，沿用 Living Legends 语篇，聚焦语言深度：赏析 make sb.+adj、-ing 作主语、give up/share with 等表达与定语从句，为写作积累语料。',
      overview: '【学情分析】A班：能懂大意但 -ing 作主语不熟，写作少用。B班：定语从句 that/which 识别困难。共同问题：make sb.+adj 结构与 make sb. do 混淆。',
      objectives: [
        '语言能力：识别并运用 make sb.+adj、-ing 作主语、give up/share with 等表达。',
        '文化意识：体会失败中学习的积极态度（learning from failure）。',
        '思维品质：辨析 make sb.+adj 与 make sb. do 的结构差异。',
        '学习能力：建立人物描写语料库供写作调用。'
      ],
      keyPoints: '① 结构：make sb.+adj（made him unique）/ make sb. do。② -ing 作主语：Losing games taught him to practise harder。③ 短语：give up / share... with / set an example for。',
      difficulties: '① make sb.+adj 与 make sb. do 混淆。原因：宾补形式不同。② -ing 作主语谓语用单数，学生漏改。③ the secret to success 中 to 为介词，后接名词/doing。',
      teachingMethods: '① 语篇研读圈画。② 结构对比：make sb.+adj vs make sb. do。③ 语料库搭建。',
      preparation: '【PPT课件】P1 语篇（高亮结构）；P2 结构对比；P3 -ing 主语归纳；P4 语料库模板；P5 仿写。【实物教具】语料卡 printed。【音频】无。',
      process: [
        { step: '圈画结构', time: '8', content: '【PPT P1 高亮】教师：Find make sb.+adj. 预设回答：made him unique. 板书时机：板书结构。差异化提示：B班找已高亮；A班自找。易错点提醒：unique 前用 a。' },
        { step: '结构对比', time: '10', content: '【PPT P2 对比】教师：make him unique(adj) vs make him practise(do). 预设回答辨析。板书时机：双栏对比。差异化提示：B班选填；A班造句。易错点提醒：adj 表特征，do 表动作。' },
        { step: '-ing主语', time: '10', content: '【PPT P3 归纳】教师：Losing games taught him... — -ing 作主语，谓语单数。预设回答跟读。板书时机：板书例句。差异化提示：B班判断主语；A班仿写。易错点提醒：Losing 作主语，taught 用单数过去式。' },
        { step: '语料库', time: '8', content: '【PPT P4 模板】学生填语料卡：结构/短语/品质词。板书时机：巡视。差异化提示：B班填词；A班造句。易错点提醒：the secret to + 名词/doing。' },
        { step: '仿写', time: '9', content: '【PPT P5 练习】学生用语库仿写一句人物评价。教师：Describe an athlete you admire. 预设回答：Practising every day made her strong. 板书时机：展示佳句。差异化提示：B班填空；A班自由。易错点提醒：-ing 主语+单数谓语。' }
      ],
      blackboard: '┌─ U3 Reading Ⅱ: 语言深度 ┐\n│ make sb.+adj (made him unique) │\n│ make sb. do (made him practise) │\n│ -ing 主语 → 谓语单数           │\n│ give up / share…with / secret to│\n└────────────────────────────────┘',
      exercises: '【基础作业】1. 整理语料库（结构≥3、短语≥4）。2. 用 -ing 作主语造 3 句。【提高作业】用语料库写一段 50 词人物评价（含 make sb.+adj 与 -ing 主语各 1 处）。【参考答案——教师用】基础2示例：Losing the match taught him to work harder. / Practising every day made her confident. / Sharing success with others made him a legend.',
      reflection: '✅ 亮点：结构对比让 make 句型清晰，A班仿写质量提升。⚠️ 需改进：-ing 主语谓语单数 B 班仍漏。📌 下节课衔接：进入语法——附加疑问句，为日常交际奠基。'
    },
    // ===== P4 语法 =====
    {
      periodNumber: 4, lessonType: 'grammar', duration: 45,
      title: 'Discovering Useful Structures: 附加疑问句（反意疑问句）',
      textbookAnalysis: '第四课时，语法点：附加疑问句（tag question）。结构为 前肯后否/前否后肯，用 be/助/情态动词+主语代词，用于确认信息或寻求认同。',
      overview: '【学情分析】A班：知道句末加 is not it? 但助动词选择与主句不一致。B班：前肯后否规则不清，否定词（never/hardly）时易错。共同问题：Let us go 这类祈使句附加部分混乱。',
      objectives: [
        '语言能力：识别并正确构造附加疑问句，遵循前肯后否/前否后肯与助动词一致规则。',
        '文化意识：体会附加疑问句的语用功能（确认/求同）与升降调含义。',
        '思维品质：辨析特殊情形（否定词、祈使句）的附加部分。',
        '学习能力：用规则表归纳附加疑问句的构成。'
      ],
      keyPoints: '① 结构：前肯后否 / 前否后肯。② 助动词与主句一致（is/are/do/does/did/will/can）。③ 特殊：含 never/hardly/no 等否定词时后部分用肯定；Let us..., shall we?。',
      difficulties: '① 否定词（never/hardly）使主句表否定，后部分须用肯定。原因：学生忽视隐含否定。② 主句动词决定助动词（实义动词用 do/does/did），学生误用 be。③ Let us go, shall we? 与祈使句 Open the door, will you? 易混。',
      teachingMethods: '① 归纳法：从例句发现规则。② 对比法：肯否对称。③ 情境操练：日常确认对话。',
      preparation: '【PPT课件】P1 例句；P2 规则表；P3 否定词特殊；P4 祈使句特殊；P5 操练题。【实物教具】规则卡 printed。【音频】无。',
      process: [
        { step: '观察例句', time: '7', content: '【PPT P1 例句】教师：You like sports, do not you? — 前肯后否。预设回答跟读。板书时机：板书例句。差异化提示：B班判断肯否；A班说规则。易错点提醒：do not 缩写 do not→dont。' },
        { step: '归纳规则', time: '10', content: '【PPT P2 规则表】师生归纳：前肯后否/前否后肯，助动词与主句一致。教师：He is a champion, is not he? 预设回答补全。板书时机：填表。差异化提示：B班填助动词；A班补例句。易错点提醒：实义动词用 do/does/did。' },
        { step: '否定词特殊', time: '10', content: '【PPT P3 否定词】教师：He never gives up, does he? — never 表否定，后用肯定。预设回答辨析。板书时机：板书特例。差异化提示：B班选填；A班解释。易错点提醒：never/hardly/seldom 后用肯定。' },
        { step: '祈使句特殊', time: '8', content: '【PPT P4 祈使句】教师：Let us go, shall we? / Open the door, will you? 预设回答跟读。板书时机：板书特例。差异化提示：B班认读；A班仿写。易错点提醒：Let us 用 shall we，其他祈使句用 will you。' },
        { step: '操练', time: '10', content: '【PPT P5 题】学生补全附加疑问句。教师：She can swim, ___? 预设回答：can not she? 板书时机：展示。差异化提示：B班选择式；A班自填。易错点提醒：can not 缩写 cant。' }
      ],
      blackboard: '┌─ U3 Grammar: 附加疑问句 ┐\n│ 前肯后否 / 前否后肯       │\n│ 助动词与主句一致(be/do/will) │\n│ never/hardly→后部分用肯定 │\n│ Let us…, shall we?        │\n│ 祈使句, will you?         │\n└────────────────────────────┘',
      exercises: '【基础作业】1. 补全 10 句附加疑问句。2. 归纳否定词与祈使句两类特例各 2 例。【提高作业】编写一段 6 轮对话，含至少 4 处附加疑问句并标升降调。【参考答案——教师用】基础1示例：He is a legend, is not he? / They won the match, did not they? / She never gives up, does she? / Let us watch the game, shall we?',
      reflection: '✅ 亮点：规则表+特例对比清晰，A班操练准确率高。⚠️ 需改进：否定词特例 B 班仍漏，需专项。📌 下节课衔接：进入听与谈——用附加疑问句进行运动精神讨论。'
    },
    // ===== P5 听与谈 =====
    {
      periodNumber: 5, lessonType: 'listening-talking', duration: 40,
      title: 'Listening and Talking: Sportsmanship & Fitness — 运动精神与健康选择',
      textbookAnalysis: '第五课时，听说结合。听力为谈论运动精神与健康生活习惯；口语为用附加疑问句确认观点并讨论健身选择。',
      overview: '【学情分析】A班：能表达观点但附加疑问句不会用。B班：听细节（频度副词 always/never）易错。共同问题：讨论健康习惯缺句式支架。',
      objectives: [
        '语言能力：听懂运动精神与健康习惯对话细节；用附加疑问句确认观点并讨论健身选择。',
        '文化意识：理解公平竞争与坚持锻炼的价值。',
        '思维品质：在讨论中权衡利弊、提出建议。',
        '学习能力：用观点记录表梳理正反理由。'
      ],
      keyPoints: '① 句式：附加疑问句用于确认（You exercise every day, do not you?）。② 频度词：always/usually/often/sometimes/never。③ 健康表达：keep fit / work out / balanced diet。',
      difficulties: '① 附加疑问句在口语中的升降调（升=求答，降=求同）。② work out（锻炼）短语义，学生直译。③ balanced diet 搭配，学生漏 balanced。',
      teachingMethods: '① 情境讨论。② 听前预教频度词。③ 观点表记录。',
      preparation: '【PPT课件】P1 健康习惯图；P2 频度词；P3 听力任务；P4 讨论卡；P5 句型板。【实物教具】观点记录表 printed。【音频】听力音频。',
      process: [
        { step: '频度词预教', time: '6', content: '【PPT P2 频度词】教师领读 always→never。预设回答跟读。板书时机：板书频度词。差异化提示：B班认读；A班造句。易错点提醒：usually /juːʒuəli/ 发音。' },
        { step: '听前预测', time: '5', content: '【PPT P3 任务】教师：What habits will you hear? 预设回答：Exercise, diet. 板书时机：表留空。差异化提示：B班勾选；A班自列。易错点提醒：留意频度。' },
        { step: '听中记录', time: '10', content: '【音频】播放，学生填习惯+频度。教师：How often does he work out? 预设回答：Every day. 板书时机：核对填表。差异化提示：B班听两遍；A班一遍。易错点提醒：work out=锻炼。' },
        { step: '句型输入', time: '6', content: '【PPT P5 句型】教师：You keep fit, do not you? — 用于确认。预设回答跟读。板书时机：板书句型。差异化提示：B班套用；A班扩展。易错点提醒：升调=求答。' },
        { step: '讨论', time: '13', content: '【PPT P4 讨论卡】学生用附加疑问句+频度词讨论健身计划。教师：Discuss your fitness plan. 预设回答：You run every morning, do not you? Yes, I keep fit. 板书时机：无。差异化提示：B班用脚本；A班自由。易错点提醒：balanced diet 搭配。' }
      ],
      blackboard: '┌─ U3 Listening & Talking ┐\n│ 频度: always→never       │\n│ keep fit / work out      │\n│ balanced diet            │\n│ 附加疑问句(升=求答/降=求同)│\n└────────────────────────────┘',
      exercises: '【基础作业】1. 听录音补全习惯与频度表。2. 用附加疑问句写 3 句确认健康习惯的问句。【提高作业】写一段 60 词健身计划，含 2 处附加疑问句。【参考答案——教师用】基础2示例：You work out every day, do not you? / She keeps a balanced diet, does not she? / They never give up, do they?',
      reflection: '✅ 亮点：频度词+讨论卡让交际真实，B班参与度高。⚠️ 需改进：附加疑问句升降调练习不足。📌 下节课衔接：进入写作——写一位体育传奇。'
    },
    // ===== P6 写作 Ⅰ =====
    {
      periodNumber: 6, lessonType: 'writing', duration: 45,
      title: 'Reading for Writing: A Sports Legend (Ⅰ) — 读析与语料',
      textbookAnalysis: '第六课时，写作第一课时。读模型短文（介绍一位体育传奇），分析结构（引入—事迹—品质—启示）与语言，积累语料。',
      overview: '【学情分析】A班：能写单句但段落结构松散，缺品质与启示。B班：时态混乱（事迹用过去，学生混现在）。共同问题：传奇描写易成流水账，缺评价。',
      objectives: [
        '语言能力：识别传奇短文结构（引入—事迹—品质—启示）与衔接手段，积累人物描写语料。',
        '文化意识：在描写中体现对体育精神的敬意。',
        '思维品质：按时间与逻辑层级组织人物事迹。',
        '学习能力：用提纲模板搭建写作骨架。'
      ],
      keyPoints: '① 结构：introduction → achievements → qualities → inspiration。② 时态：事迹用过去时，品质评价用现在时。③ 语料：determination/mental strength/set an example/make sb.+adj。',
      difficulties: '① 时态切换：事迹过去 vs 品质现在。② inspiration（启示）抽象词拼写。③ -ing 主语与 make sb.+adj 运用不熟。',
      teachingMethods: '① 范文研读圈结构。② 提纲搭建。③ 语料积累。',
      preparation: '【PPT课件】P1 范文分段；P2 结构图；P3 时态标注；P4 语料库；P5 提纲模板。【实物教具】提纲卡 printed。【音频】无。',
      process: [
        { step: '读范文', time: '8', content: '【PPT P1 范文】教师：Who is it about? 预设回答：A sports legend. 板书时机：板书主题。差异化提示：B班抓大意；A班找结构。易错点提醒：legend /ledʒənd/。' },
        { step: '析结构', time: '10', content: '【PPT P2 结构图】师生分四段。教师：Which part tells achievements? 预设回答：Achievements. 板书时机：填结构图。差异化提示：B班匹配；A班归纳。易错点提醒：inspiration /ɪnspəreɪʃn/。' },
        { step: '时态标注', time: '8', content: '【PPT P3 时态】教师圈过去时事迹与现在时品质。预设回答辨析。板书时机：板书时态。差异化提示：B班标时态；A班解释。易错点提醒：led→lead 过去式。' },
        { step: '积语料', time: '7', content: '【PPT P4 语料库】学生填品质/事迹/启示语料卡。板书时机：巡视。差异化提示：B班填词；A班造句。易错点提醒：make sb.+adj。' },
        { step: '搭提纲', time: '12', content: '【PPT P5 模板】学生用提纲卡搭自己传奇的骨架。教师：Outline your legend. 预设回答展示。板书时机：展示提纲。差异化提示：B班填空；A班自列。易错点提醒：事迹用过去时。' }
      ],
      blackboard: '┌─ U3 Writing Ⅰ: 体育传奇 ┐\n│ 结构: intro→achievements   │\n│        →qualities→inspiration│\n│ 时态: 事迹过去 / 品质现在  │\n│ 语料: determination/make sb.│\n└────────────────────────────┘',
      exercises: '【基础作业】1. 完成传奇提纲（四部分各≥2 点）。2. 整理品质词与事迹动词各 5 个。【提高作业】用提纲写一段 80 词传奇初稿。【参考答案——教师用】基础1示例：Introduction: Yao Ming；Achievements: played in the NBA, led the team；Qualities: determination, teamwork；Inspiration: he set an example for young players.',
      reflection: '✅ 亮点：结构图+提纲让写作有骨架，B班提纲完成率高。⚠️ 需改进：时态切换仍混。📌 下节课衔接：下节起草成文+互评。'
    },
    // ===== P7 写作 Ⅱ =====
    {
      periodNumber: 7, lessonType: 'writing', duration: 45,
      title: 'Reading for Writing: A Sports Legend (Ⅱ) — 起草与互评',
      textbookAnalysis: '第七课时，写作第二课时。基于提纲起草成文，运用品质词、make sb.+adj 与时态切换，经同伴互评修改定稿。',
      overview: '【学情分析】A班：能成段但时态偶尔滑回现在。B班：句子碎片化，缺主语。共同问题：互评不知评什么，需量规引导。',
      objectives: [
        '语言能力：依据提纲写 80 词传奇短文，正确运用时态切换与品质词，段落连贯。',
        '文化意识：在描写中体现对体育精神的敬意。',
        '思维品质：依据量规评价同伴作品并提出建议。',
        '学习能力：通过互评-修改循环提升自我修改能力。'
      ],
      keyPoints: '① 成段：四结构+衔接词。② 时态：事迹过去/品质现在。③ 互评量规：结构/时态/语言/衔接。',
      difficulties: '① 时态滑回现在。② make sb.+adj 与 make sb. do 混用。③ 互评流于表面。',
      teachingMethods: '① 过程写作：起草-互评-修改。② 量规引导互评。③ 教师面批聚焦时态。',
      preparation: '【PPT课件】P1 范文回顾；P2 量规表；P3 互评流程；P4 佳句展示；P5 常见问题。【实物教具】互评量规卡 printed。【音频】无。',
      process: [
        { step: '回顾要求', time: '5', content: '【PPT P1 范文】教师回顾结构+时态。预设回答跟读。板书时机：板书要点。差异化提示：B班跟读；A班复述。易错点提醒：事迹用过去时。' },
        { step: '起草', time: '15', content: '【写作】学生依提纲起草 80 词。教师巡视面批。板书时机：无。差异化提示：B班给句型框；A班自由。易错点提醒：时态切换。' },
        { step: '互评', time: '12', content: '【PPT P2 量规】学生依量规评同伴。教师：Give one suggestion. 预设回答：Check the tense. 板书时机：展示量规。差异化提示：B班勾选；A班写建议。易错点提醒：评时态。' },
        { step: '修改', time: '8', content: '【修改】学生据互评修改。教师聚焦时态。板书时机：无。差异化提示：B班改错；A班润色。易错点提醒：滑回现在须改过去。' },
        { step: '展示', time: '5', content: '【PPT P4 佳句】展示佳句与修改对比。预设回答赏析。板书时机：圈亮点。差异化提示：B班跟读；A班点评。易错点提醒：make sb.+adj。' }
      ],
      blackboard: '┌─ U3 Writing Ⅱ: 起草+互评 ┐\n│ 量规: 结构/时态/语言/衔接   │\n│ 时态: 事迹过去/品质现在     │\n│ 流程: 起草→互评→修改→定稿   │\n└──────────────────────────────┘',
      exercises: '【基础作业】1. 定稿传奇短文（≥80 词，四结构齐全）。2. 用红笔标出过去时与品质词。【提高作业】为短文配一段 30 词启示结尾。【参考答案——教师用】基础1示范段：Yao Ming was a great basketball player. He played in the NBA and led his team. His determination made him unique. He set an example for young players. We can learn to never give up from him.',
      reflection: '✅ 亮点：量规让互评有抓手，A班时态准确率提升。⚠️ 需改进：B班句子碎片化。📌 下节课衔接：进入项目——综合单元产出体育传奇评选/健康倡议。'
    },
    // ===== P8 项目复习 =====
    {
      periodNumber: 8, lessonType: 'project', duration: 45,
      title: 'Project & Unit Review: Living Legends Election — 传奇评选与健康倡议',
      textbookAnalysis: '第八课时，单元综合产出。小组评选心中的体育传奇并制作推介海报，综合运用词汇、附加疑问句、人物描写语料，同时发起健康生活倡议。',
      overview: '【学情分析】A班：综合运用能力可，但展示语言需规范。B班：表达碎片，需模板与分工支持。共同问题：海报文体特征（标题+事迹+品质+号召）体现不足。',
      objectives: [
        '语言能力：综合运用单元词汇与附加疑问句，以海报文体介绍一位体育传奇并发出健康倡议。',
        '文化意识：在评选中体现对体育精神与公平竞争的尊重。',
        '思维品质：统筹事迹—品质—启示—倡议，做有说服力的表达。',
        '学习能力：通过小组协作完成从策划到展示的完整项目。'
      ],
      keyPoints: '① 文体：海报（标题+事迹+品质+号召）。② 语言：过去时事迹+现在时品质+附加疑问句互动。③ 产出：海报+口头推介。',
      difficulties: '① 文体退化成流水账。② 小组分工不均。③ 口头推介缺互动（附加疑问句）。',
      teachingMethods: '① 项目式学习（PBL）。② 小组分工+量规。③ 展示互评。',
      preparation: '【PPT课件】P1 项目说明+样例；P2 海报模板；P3 评价量规；P4 展示流程；P5 单元知识图。【实物教具】A4 海报纸 printed 每组；彩笔。【音频】无。',
      process: [
        { step: '任务发布', time: '6', content: '【PPT P1 说明】教师发布任务：评选传奇+健康倡议海报。预设回答讨论。板书时机：板书要求。差异化提示：B班用模板；A班自创。易错点提醒：海报四要素。' },
        { step: '小组策划', time: '12', content: '【PPT P2 模板】小组分工：事迹/品质/倡议/文案。教师巡视。预设回答讨论。板书时机：无。差异化提示：B班填模板；A班设计。易错点提醒：事迹用过去时。' },
        { step: '制作海报', time: '12', content: '【实物 海报】小组图文制作。教师指导文体与语言。板书时机：无。差异化提示：B班配图；A班写文案。易错点提醒：号召语收尾。' },
        { step: '展示', time: '10', content: '【PPT P4 流程】各组用附加疑问句互动推介。教师：Present your legend. 预设回答展示。板书时机：无。差异化提示：B班读卡；A班脱稿。易错点提醒：用 You know..., do not you? 互动。' },
        { step: '评价+回顾', time: '5', content: '【PPT P3 量规+P5 知识图】互评+单元回顾。预设回答跟读。板书时机：圈重点。差异化提示：B班勾选；A班自评。易错点提醒：单元核心附加疑问句/品质词回顾。' }
      ],
      blackboard: '┌─ U3 Project & Review ┐\n│ 任务: 传奇评选+健康倡议 │\n│ 文体: 海报(事迹+品质+号召)│\n│ 语言: 过去时+品质+附加疑问│\n│ 产出: 海报 + 口头推介   │\n└──────────────────────────┘',
      exercises: '【基础作业】1. 完善海报（含事迹+品质+号召）。2. 写一段 60 词传奇推介（含 2 处附加疑问句）。【提高作业】为健康倡议设计一周锻炼计划并说明理由。【参考答案——教师用】基础2示范：Yao Ming was a basketball legend. He led his team with determination. His teamwork made him unique. You admire him, do not you? Let us learn from him and keep fit!',
      reflection: '✅ 亮点：海报产出综合性强，A班文体特征明显。⚠️ 需改进：B班分工不均，下次设角色卡。📌 下节课衔接：进入 Unit 4 Natural Disasters，话题转向自然灾害与防灾。'
    }
  ]
};

const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const oldLessons = require('../data/lessons.js');
const newLessons = replaceUnit(oldLessons, SPEC);
fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(newLessons, null, 2) + ';\n', 'utf8');

const u3 = newLessons.filter(l => l.book === SPEC.book && l.unitNumber === SPEC.unitNumber);
const ids = newLessons.map(l => l.id);
const dup = ids.filter((x, i) => ids.indexOf(x) !== i);
console.log('U3 periods:', u3.length, '(expect 8)');
console.log('Total lessons:', newLessons.length);
console.log('Duplicate ids:', dup.length ? dup : 'none');
u3.forEach(l => console.log('  p' + l.periodNumber, l.lessonType, '|', l.title.slice(0, 40)));
