/**
 * gen-b2-u3.js — 必修第二册 Unit 3 The Internet (8课时)
 * 
 * 语篇: STRONGER TOGETHER: HOW WE HAVE BEEN CHANGED BY THE INTERNET
 *       (Jan Tchamani's story, online community)
 * 语法: 现在完成时的被动语态 (have/has been + past participle)
 * 写作: Write a Blog Post about online experience
 */

const fs = require('fs');
const path = require('path');

function esc(s) { return s.replace(/'/g, "\\'").replace(/\n/g, '\\n'); }

function makeLesson(l) {
  return {
    id: l.id, lessonId: l.id, title: l.title,
    book: l.book, unitNumber: l.unitNumber, unitTitle: l.unitTitle,
    lessonType: l.lessonType, lessonTypeName: l.lessonTypeName,
    lessonNumber: l.lessonNumber, periodNumber: l.periodNumber, duration: l.duration,
    grade: '高一', subject: '英语', tags: l.tags,
    textbookAnalysis: l.textbookAnalysis, overview: l.overview,
    objectives: l.objectives, keyPoints: l.keyPoints,
    difficulties: l.difficulties, teachingMethods: l.teachingMethods,
    preparation: l.preparation, process: l.process,
    blackboard: l.blackboard, exercises: l.exercises,
    reflection: l.reflection,
    aiModel: 'claude-opus', viewCount: 0, downloadCount: 0
  };
}

const BC = 'b2';
const UNIT = 3;
const UNIT_TITLE = 'The Internet';
const BOOK = '必修第二册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u3-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '互联网', '上网习惯', '人教版必修二U3', '第一节课'],
  textbookAnalysis: '本课为必修第二册 Unit 3 The Internet 第一课时（Listening and Speaking），属单元导入+输入环节。语篇为一段关于青少年上网习惯的调查对话与一则介绍互联网用途的听力材料，功能语境是"询问并描述上网活动"。语言重点为互联网相关词汇（browse, stream, download, update, blog, account, network）及询问上网习惯句型（How much time do you spend online? / What do you usually do on the Internet?）。为 Reading 语篇"STRONGER TOGETHER"中互联网改变人生的叙事做词汇与话题预热。',
  overview: '【学情分析】A班：对互联网话题熟悉，日常上网词汇（WiFi, app, online）会，但 browse/stream/update 等动词不熟。B班：部分英文网络术语发音不准（如 browser /braʊzə/ 读成 /bruːzə/）。共同问题：讨论上网时只会说 play games 和 watch videos，缺乏描述多样网络活动的词汇。',
  objectives: [
    '语言能力：听懂关于上网习惯的调查对话，提取关键信息（时长/活动/偏好），准确使用 8-10 个互联网相关词汇。',
    '文化意识：了解不同国家青少年上网习惯的异同，形成对互联网使用的批判性认知。',
    '思维品质：通过"听前预测—听中分类—听后比较"形成系统听力策略。',
    '学习能力：能用 How much time do you spend...? / What do you usually do...? 询问并描述自己的上网习惯。'
  ],
  keyPoints: '① 互联网核心词汇：browse / stream / download / update / blog / account / network / search engine ② 询问上网习惯句型：How much time do you spend online? / What do you use the Internet for? / I usually... / I also... ③ 听力微技能：听前预测活动类型、听中分类（娱乐/学习/社交）。',
  difficulties: '① browse（浏览）与 browser（浏览器）词性混淆。原因：形近。易错点提醒：browse 是动词，browser 是名词（浏览器软件）。② download /daʊnləʊd/ 发音重音在第一音节——学生易读成 /daʊnˈləʊd/。③ spend time doing（花时间做某事）— 学生易写成 spend time to do。',
  teachingMethods: '① 任务型（TBL）：以做"班级上网习惯调查"为终任务。② 听前预测+听中填表：分类表脚手架。③ 对子互问操练上网习惯句型。',
  preparation: '【PPT课件】P1 单元封面（The Internet）；P2 网络活动图标九宫格（搜索/视频/音乐/社交/购物/游戏/学习/新闻/博客）；P3-4 听力任务题；P5 上网习惯句型板；P6 调查任务卡。【实物教具】上网习惯调查表 printed 每人一份；网络活动词汇卡每组一套。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine icons. How many of these do you do online? Which ones? 预设回答：I watch videos, play games, and chat with friends. / I also search for information. 板书时机：右侧板书 browse / stream / download / chat / search。差异化提示：B班指图说中文再跟读英文；A班用 I use the Internet to... 造句。易错点提醒：Internet 首字母永远大写，前面用 the — "the Internet" 不是 "internet"。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 browse / stream / download / update / blog / account / network / search engine。教师：What does "stream" mean when we talk about the Internet? 预设回答：It means watching or listening online without downloading. 板书时机：左栏板书词+短注释，标注动词/名词。差异化提示：B班配图标记忆+中英对照；A班用词造句。易错点提醒：stream 作动词（在线播放/流媒体）与名词（溪流）完全不同——本文只讲动词义。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to a survey about teenagers\' online habits. Predict: What activities will be mentioned? (entertainment / study / social / shopping) 预设回答：Entertainment — like watching videos and playing games. And social — chatting with friends. 板书时机：预测分类写在黑板中部（四象限）。差异化提示：B班给中文提示词；A班用英文说预测+给例子。易错点提醒：听力中活动频率词（often/sometimes/never）— 是听力的关键区分信息。' },
    { step: '听中分类', time: '10', content: '【PPT P5 分类表】【音频 段一】播放听力，学生按"娱乐/学习/社交/购物"四象限分类填表。教师：What is the most popular online activity? How much time do they spend? 预设回答：Watching videos is the most popular. They spend about 3 hours a day. 板书时机：核对答案时填分类表于黑板中部。差异化提示：B班给活动列表只分类；A班一遍填全+写频率词。易错点提醒：hour 前面用 an — "an hour" 不是 "a hour"，因为 h 不发音。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to ask about online habits? How much time do you spend online? / What do you usually do on the Internet? / How often do you...? 教师示范后同桌互问。预设回答：I spend about two hours online every day. I usually stream music and browse social media. 板书时机：句型板书于中央。差异化提示：B班套用模板替换时间+活动；A班追加 Why 追问。易错点提醒：spend time doing — "I spend time to surf" 是错的，应为 "I spend time surfing"。' },
    { step: '调查任务', time: '5', content: '【PPT P6 调查表】学生采访 3 位同学的上网习惯，记录并准备简短汇报。教师：Ask three classmates about their online habits. Be ready to report one interesting finding. 预设回答：Most of my classmates stream music every day. Only one person uses the Internet for study! 板书时机：留句型供参考。差异化提示：B班用填空式调查表；A班自由采访+追问。易错点提醒：做调查报告时说 "Most of my classmates..." 不具体的数字用 most/some/a few/none，比编造精确数字更地道。' }
  ],
  blackboard: '┌─ U3 Listening & Speaking ──────────┐\n│ Internet Activities:                 │\n│  browse / stream / download / update │\n│  blog / account / network / search   │\n│  engine / social media               │\n│                                      │\n│ Asking about habits:                 │\n│  How much time do you spend online?  │\n│  What do you usually do on the Net?  │\n│  How often do you...?                │\n│                                      │\n│ Survey Results (top 3):              │\n│  1. Stream videos/music  2. Chat    │\n│  3. Browse social media              │\n└──────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有网络活动词汇。2. 用 How much time...? / What do you usually...? 写 3 个关于上网习惯的问答。【提高作业】用英文写 50 词关于自己的上网习惯自述，包含时长/主要活动/最喜欢的一个网站或App。【参考答案——教师用】基础2示例：Q: How much time do you spend online each day? A: I spend about two hours online, mostly in the evening. Q: What do you usually do on the Internet? A: I usually stream music and browse the news.',
  reflection: '✅ 亮点：调查任务让句型操练有真实交流目的，学生参与度高。⚠️ 需改进：spend time doing 句式仍有部分学生写 to do，下节需在阅读语境中强化。📌 下节课衔接：进入阅读 STRONGER TOGETHER，从上网习惯延伸到互联网如何改变人生。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u3-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '互联网', '在线社区', '人物故事', '人教版必修二U3', '第二节课'],
  textbookAnalysis: '本课为必修第二册 Unit 3 第二课时（Reading I），语篇 STRONGER TOGETHER: HOW WE HAVE BEEN CHANGED BY THE INTERNET 是一篇人物报道/叙事文，讲述英国伯明翰 61 岁女性 Jan Tchamani 因病失业后通过互联网学习新技能、创办在线社区帮助他人、最终改变自己与许多人生活的故事。结构为"困境→互联网启蒙→建立社区→影响扩散"。语言重点为叙事时间顺序词（at first / then / later / so far）与互联网赋能动词（access, inspire, remove, connect, benefit）。',
  overview: '【学情分析】A班：能快速把握人物叙事线索，但对"互联网的社会影响力"缺乏深入思考。B班：人物报道的背景（英国/疾病/孤独感）可能引起共鸣但词汇量不够。共同问题：叙述类文本中"改变"的多种表达（change/transform/improve）不会区分。',
  objectives: [
    '语言能力：读懂人物报道类叙事文，提取 Jan Tchamani 的人生转折点/互联网如何改变她/在线社区的影响；掌握 8-10 个核心动词。',
    '文化意识：理解互联网在消除孤独、赋能弱势群体方面的积极社会作用。',
    '思维品质：通过"困境→转折→行动→影响"故事弧线分析培养叙事结构思维。',
    '学习能力：能用"Before→Turning Point→After→Impact"框架复述人物故事。'
  ],
  keyPoints: '① 叙事弧线：Loneliness→Discover Internet→Learn Skills→Create Community→Help Others ② 时间标志词：at first / then / later / after a while / so far / now ③ 核心短语：be out of work / access the Internet / apply for / benefit from / bridge the gap',
  difficulties: '① access（使用/访问）作动词与名词用法。原因：学生只知名词义"通道"。提醒：本文中 access the Internet = 上网。② apply for（申请）与 apply to（适用于）区别。③ benefit from（从…获益）— 学生易写成 benefit by。',
  teachingMethods: '① 故事弧线阅读法：找转折点→画情绪曲线。② Jigsaw拼图：分段阅读后拼合全故事。③ 问题链追问：训练共情与批判思维。',
  preparation: '【PPT课件】P1 Jan Tchamani 照片与报道截图；P2 故事弧线图（情绪曲线）；P3 时间轴填表；P4 分段任务卡；P5 词汇对比表；P6 互联网影响力讨论；P7 总结回顾。【实物教具】分段阅读卡 printed 每组一套；故事弧线空白工作单。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P1 人物照片】教师：This is Jan Tchamani. She is 61 years old and lives in Birmingham, UK. A few years ago, she felt very lonely. Today, thousands of people know her. What do you think happened? 预设回答：She met people online? / She started a YouTube channel? / She used the Internet to connect with others. 板书时机：板书 lonely → ??? → thousands of people，问号处留给学生填。差异化提示：B班中文猜；A班英文猜+说理由。易错点提醒：lonely（孤独的，心理感受）≠ alone（独自的，物理状态）—— 一个人可以 alone 但不 lonely。' },
    { step: '快速阅读抓主线', time: '8', content: '【PPT P3 时间轴】教师：Read fast (3 min). Find: ① Why was Jan lonely? ② What did she discover? ③ What did she create? ④ What is the result? 预设回答：① She was out of work and had an illness. ② She discovered the Internet. ③ She created an online community. ④ Many people\'s lives have been improved. 板书时机：填时间轴四个关键点。差异化提示：B班给四选一选项；A班写完整句+段落号。易错点提醒：out of work = unemployed（失业），不是"在外面工作"。' },
    { step: '精读段落1-2 困境与转折', time: '10', content: '【PPT P4 分段卡】教师精讲：be out of work / access the Internet / apply for。教师：How did Jan feel before discovering the Internet? What was her turning point? 预设回答：She felt lonely and bored. The turning point was when she applied for an online course. 板书时机：左侧栏画情绪曲线（从低→上升）。差异化提示：B班读后填关键词；A班用自己话描述 Jan 的心理变化。易错点提醒：apply for + 你想要的东西（job/course/visa），apply to + 机构/人/情况（company/university/situation）。' },
    { step: '精读段落3-5 社区与影响', time: '10', content: '【PPT P5 行动链】教师：What did Jan do after learning IT skills? Who did she help? How did her community grow? 学生填表（行动→受益者→效果）。教师：Why is the title "Stronger Together"? 预设回答：She started an online community for older people. It helped them feel less lonely. Together, they are stronger. 板书时机：右侧画行动→影响扩散图。差异化提示：B班连线匹配（行动—效果）；A班写"cause and effect"句。易错点提醒：together（一起）≠ altogether（总共）——标题"Stronger Together"意为"在一起更强大"。' },
    { step: '归纳主题', time: '4', content: '【PPT P6 互联网影响力】教师：What does this story teach us about the Internet? (It\'s not just for fun — it can change lives, connect people, bridge gaps.) 预设回答：The Internet can help people who are lonely or disabled. It can make the world a better place if used well. 板书时机：圈出"bridge the gap"并释义。差异化提示：B班跟读关键词；A班用自己的话总结网络的双面性。易错点提醒：bridge the gap = 弥合差距（比喻），此处指弥合数字鸿沟和人与人之间的隔阂。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾"孤独→上网→学技能→建社区→帮更多人"故事弧线+核心词汇。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：so far（迄今为止）常与现在完成时连用，标志词。' }
  ],
  blackboard: '┌─ U3 Reading I: STRONGER TOGETHER ──────┐\n│ Jan\'s Story Arc:                         │\n│  Lonely → Discover Internet → Learn IT   │\n│  → Create Community → Help Thousands    │\n│                                           │\n│ out of work / access / apply for         │\n│ inspire / connect / benefit from         │\n│ bridge the gap / so far                   │\n│                                           │\n│ Title: "Stronger Together"                │\n│  = Internet connects → community builds  │\n│    → together we overcome loneliness     │\n└───────────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-5段 2 遍，圈出所有时间标志词。2. 用故事弧线的4个阶段各写1句描述 Jan 的经历。【提高作业】用 80 词左右写一段：How has the Internet changed YOUR life?（用 access / benefit from / connect）【参考答案——教师用】基础2示例：Jan felt lonely and bored after losing her job. / Then she discovered the Internet and learned IT skills. / Later, she started an online community for older people. / So far, thousands of people have benefited from her work.',
  reflection: '✅ 亮点：故事弧线+情绪曲线让叙事结构可视化，B班理解率明显提升。⚠️ 需改进：apply for/apply to 区分仍需强化，精读课将深入。📌 下节课衔接：进入精读语言+现在完成时的被动语态在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u3-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '被动语态', '互联网', '人教版必修二U3', '第三节课'],
  textbookAnalysis: '本课为必修第二册 Unit 3 第三课时（Reading II），聚焦语篇 STRONGER TOGETHER 的精读与语言分析。重点分析文中现在完成时的被动语态（have/has been + past participle）——如 "People\'s lives have been improved" "An online community has been created"——在人物报道中的功能：强调结果状态的改变已经发生且持续至今。同时深化语篇中高频动词的用法辨析（access / inspire / remove / connect / bridge）。',
  overview: '【学情分析】A班：已学一般现在时/过去时/进行时被动，现在完成时被动（has been done）是全新时态组合。B班：被动语态+完成时双重挑战，需从 has been 开始拆解。共同问题：看到 has been done 时无法同时处理"完成"和"被动"两层信息。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 4 个现在完成时的被动语态句子，理解其"已经被…且结果持续至今"的语义。',
    '文化意识：通过被动语态体会英语如何聚焦"改变的结果"而非"谁造成的改变"。',
    '思维品质：分析现在完成时被动语态在人物报道中的修辞功能——强调个人/群体已被互联网赋权的结果状态。',
    '学习能力：建立"从读到写"的语料库——积累课文中的完成时被动句型用于后续博客写作。'
  ],
  keyPoints: '① 现在完成时被动语态结构：have/has + been + past participle ② 语篇中被动句的识别与功能分析 ③ 核心动词辨析：access / inspire / remove / connect / bridge / benefit / apply',
  difficulties: '① has been done 与 is being done 的区别——学生混淆完成时被动（已发生+结果持续）与进行时被动（正在被做）。② been 的拼写——学生写成 ben / bean。③ 不规则过去分词记错——take→taken, write→written, give→given。',
  teachingMethods: '① 标注发现法：圈出文中所有现在完成时被动语态并分析时态结构。② 对比辨析：vs 一般过去时被动 vs 现在进行时被动。③ 语料卡记录：分类摘录优质被动句。',
  preparation: '【PPT课件】P1-2 课文中圈出的被动语态示例；P3 现在完成时被动结构分解公式；P4 三时态被动对比表；P5 语料卡模板；P6 词汇辨析表；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔两支（黄=被动/蓝=时间词）。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 故事弧线】教师：Last class we read Jan\'s story. Can you recall: What was her problem? What did the Internet help her do? What is the result? 预设回答：She was lonely and out of work. The Internet helped her learn IT skills. She created an online community that has helped thousands. 板书时机：左栏写故事弧线关键词。差异化提示：B班看关键词复述；A班完整说出5个以上要点。易错点提醒：thousands of（成千上万的）— thousand 不加 s，但 thousands of 加 s。' },
    { step: '被动语态发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle all sentences with "has/have been + past participle." 学生标记后全班核对。教师：Why does the author use this structure? 预设回答：To show that a change has happened and the result is still important now. 板书时机：逐句板书圈出的被动语态。差异化提示：B班给划线句直接圈 has/have been + V-ed；A班自己找+分析"结果是什么，持续到现在了吗"。易错点提醒：has been + V-ed 中 been 不能少！"People\'s lives have improved"（主动）= 生活自己变好了；"People\'s lives have been improved"（被动）= 生活被（互联网）改善了。' },
    { step: '被动语态讲透', time: '10', content: '【PPT P3 结构公式】教师板书：have/has + been + V-ed。对比三个时态被动：①The community was created in 2015.（一般过去时，时间点明确）②The community is being created now.（现在进行时，正在创建中）③The community has been created.（现在完成时，已创建且现在存在）。教师：Which sentence tells us the community still exists? 预设回答：Sentence ③ — "has been created" means it was created and is still here. 板书时机：三句对比板书，用红笔标注时间差异。差异化提示：B班填空（has/have ___ + V-ed）；A班独立造句+解释时态选择。易错点提醒：has been done 和 was done 的最大区别——前者强调结果持续到现在（所以常与 so far / already / yet 连用），后者只陈述过去事实。' },
    { step: '语料库搭建', time: '10', content: '【PPT P5 语料库模板】学生分类填语料卡：①完成时被动句摘录（至少3句）②互联网赋能动词（access/inspire/remove/connect/bridge/benefit/apply）③时间/改变表达（so far / now that / as a result）。板书时机：巡视指导。差异化提示：B班填词+翻译；A班造句并写一句"我可以在博客中这样用"。预设回答：按互联网语料库模板分类填写词条。易错点提醒：benefit 作动词时用法——benefit from（获益于）和 benefit sb（使某人受益）方向相反。"The Internet benefits her." = 互联网使她受益。' },
    { step: '句型转换', time: '5', content: '【PPT P6 练习】教师给句子，学生改时态：The Internet has changed her life.（主动）→ Her life has been changed by the Internet.（被动）。Jan has helped many people. → Many people have been helped by Jan. 预设回答造句。板书时机：板书转换公式。差异化提示：B班跟做每一步；A班独立完成+说明语义区别。易错点提醒：by + 施事者在被动句中可省略——当施事者不重要或不想强调时。"Her life has been changed." 比 "Her life has been changed by the Internet." 更聚焦于改变本身。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】回顾 have/has been done 结构+与 was/were done 的区别+语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课系统讲练现在完成时的被动语态。' }
  ],
  blackboard: '┌─ U3 Reading II: Language Focus ───────────┐\n│ Present Perfect Passive:                    │\n│  have/has + BEEN + past participle          │\n│                                             │\n│ Passive Voice Comparison:                   │\n│  was created (past, done)                   │\n│  is being created (present, in progress)    │\n│  has been created (past→now, result lasts!) │\n│                                             │\n│ Text examples:                              │\n│  "People\'s lives have been improved."       │\n│  "An online community has been created."    │\n│  "Many people have been helped by Jan."     │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出4个现在完成时被动语态句子并标注 has/have + been + V-ed。2. 将以下句子改为被动：The Internet has connected millions of people. 【提高作业】用现在完成时的被动语态写3句关于互联网改变你周围生活的句子。【参考答案——教师用】基础2示例：Millions of people have been connected by the Internet.',
  reflection: '✅ 亮点：三时态对比让学生直观感受"has been done"的独特功能。⚠️ 需改进：been 遗漏/拼错仍是常见问题，语法课需大量操练。📌 下节课衔接：进入语法课，系统操练现在完成时的被动语态。'
}));

// ====== Period 4: Grammar (现在完成时的被动语态) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u3-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '被动语态', '现在完成时', '互联网', '人教版必修二U3', '第四节课'],
  textbookAnalysis: '本课为必修第二册 Unit 3 第四课时（Discovering Useful Structures），系统教学现在完成时的被动语态（have/has been + past participle）。基于 Reading 语篇中提取的例句，引导学生归纳出"何时使用完成时被动"的规则——强调动作已完成、结果持续到现在且受事者比施事者更重要。通过互联网主题的语境化练习（在线社区被创建/信息被分享/生活被改变）巩固语法，为后续博客写作做语言准备。',
  overview: '【学情分析】A班：掌握一般时被动，但完成时被动（has been done）易与进行时被动（is being done）混淆——都是"be + V-ed"但有不同助动词。B班：被动语态整体不熟+完成时不熟=双重困难。共同问题：看到 has been 后面的 done 忘了加 -ed 变过去分词。',
  objectives: [
    '语言能力：准确构建现在完成时的被动语态句子，在互联网话题中产出 5 个以上正确句子。',
    '文化意识：通过被动语态聚焦"互联网已带来的改变"，形成用英语描述科技影响的能力。',
    '思维品质：通过"发现例句→归纳规则→对比辨析→应用输出"的归纳法培养语法学习策略。',
    '学习能力：建立"被动语态自查表"——写作后自行检查 been 是否遗漏、过去分词形式是否正确。'
  ],
  keyPoints: '① 现在完成时被动语态：have/has + been + V-ed（过去分词）② 使用场景：强调动作已完成且结果持续 → 常与 already / just / so far / yet / ever / never 连用 ③ 与一般过去时被动的区别：was done=过去某时间点完成，has been done=过去完成+影响到现在 ④ 不规则过去分词复习（write→written, give→given, take→taken, build→built）',
  difficulties: '① has been done vs was done — 学生难以判断"影响是否持续到现在"。原因：中文没有对应的时体区别。② been 拼写与发音 /biːn/ — 学生写成 ben 或 bean。③ already 在完成时被动句中的位置 — "has already been done" 不是 "has been already done"。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习。② 情境造句：给网络场景图片用被动描述。③ 改错竞赛：找出典型错误。',
  preparation: '【PPT课件】P1 现在完成时被动公式分解；P2 课文例句摘录；P3 与一般过去时被动对比表；P4 时间轴图（过去→现在→将来）；P5 情境造句任务卡；P6 改错题；P7 总结。【实物教具】改错卡每人一套；情境图片卡一套。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中3个被动句+新给3个：①Online courses have been accessed by millions. ②New skills have been learned. ③A strong network has been built. 学生圈"has/have + been + V-ed"。教师：What signal words tell us it\'s "present perfect"? 预设回答：so far / already / ever / never. "Has/have been" shows the action connects past to now. 板书时机：左栏板书3句，红笔标 been + V-ed + 时间信号词。差异化提示：B班只圈 been；A班分析"这个动作是什么时候发生的，现在结果是什么"。易错点提醒：been 是 be 的过去分词——be→was/were→been。不要和 being（be 的现在分词）混淆。' },
    { step: '规则归纳', time: '10', content: '【PPT P3 对比表】教师对比两种被动：①The website was built in 2020.（一般过去时，时间点明确，网站现在可能已不存在）②The website has been built.（现在完成时，已建成且现在可以使用）。教师：When do we use present perfect passive? 预设回答：When the action was done before now, but the result is still important now. We care about the present result. 板书时机：两列对比板书。差异化提示：B班填已给表格；A班自己画表+每个造1句。易错点提醒：has been done 不能与具体过去时间连用——"has been built in 2020" 是错的，应为 "was built in 2020"。' },
    { step: '时间轴讲解', time: '8', content: '【PPT P4 时间轴】教师用时间轴讲解：过去某点（动作发生）→ 箭头持续 → 现在（结果仍存在）。对比：was done（动作在过去完成，可能无现在联系）vs has been done（动作在过去完成，结果延伸到现在）。教师：Which one would you use for "The Internet has changed our lives"? 预设回答：has been done — because the change is still with us. 板书时机：画时间轴对比。差异化提示：B班看时间轴指认时态；A班解释选择原因。易错点提醒：判断技巧——如果前面加上"so far / up to now"，只能用现在完成时被动。' },
    { step: '情境造句', time: '8', content: '【PPT P5 图片卡】展示4张图（App被下载/网课被完成/群聊被创建/文章被分享），学生用完成时被动描述。教师：Look at this picture. What has been done? 预设回答：The app has been downloaded by millions. / The online class has been completed. / A group chat has been created. 板书时机：巡视指导。差异化提示：B班给动词提示（download/complete/create/share）；A班不给提示自由造句。易错点提醒：不规则过去分词要准确——download→downloaded（规则），write→written（不规则）。' },
    { step: '改错竞赛', time: '5', content: '【PPT P6 改错】展示 4 个典型错误：①The website has been create.（create 缺 -d → created）②Many lives have been change.（change 缺 -d → changed）③Information has been wrote online.（wrote 应为 written）④The community has been already helped many people.（already 位置错 → has already been）。学生组间竞赛纠错。预设回答纠错。板书时机：板书错误→改正+规则。差异化提示：B班判对错；A班解释为什么错。易错点提醒：already 在完成时被动中的位置——放在 has/have 之后，been 之前。"has already been done" ✓。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾公式 have/has been + V-ed + 使用场景 + 常见错误。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班说出3条规则。易错点提醒：自查三问——①has/have 用对了吗（单数has复数have）？②been 写了吗？③动词过去分词拼对了吗？' }
  ],
  blackboard: '┌─ U3 Grammar: Present Perfect Passive ────┐\n│  have/has + BEEN + past participle         │\n│                                            │\n│  Signal words: so far / already / just     │\n│                yet / ever / never          │\n│                                            │\n│  was done → past only (2020)              │\n│  has been done → past → present (now!)    │\n│                                            │\n│  🕐 - - - [was done] - - - -              │\n│  🕐 - - - [has been done] → → → NOW       │\n│                                            │\n│  ❌ has been in 2020 → ✓ was done in 2020 │\n│  ❌ has been wrote  → ✓ has been written  │\n└────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 用现在完成时被动语态造 5 句关于互联网影响的句子。2. 改错：The network has been build. / Information has been share. / The app has been already downloaded.【提高作业】写 60 词短文描述互联网如何改变了你们班（用至少 3 个现在完成时被动语态）。【参考答案——教师用】基础1示例：A class website has been created. / Many useful resources have been shared online. / Students have been connected through group chats.',
  reflection: '✅ 亮点：时间轴让"完成"概念可视化，B班理解度明显提升。⚠️ 需改进：already 位置仍需反复纠正，听与谈课可融入被动语态口头练习。📌 下节课衔接：听与谈聚焦网络安全与网络礼仪讨论，口头运用被动语态描述网络现象。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u3-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '网络安全', '网络礼仪', '互联网', '人教版必修二U3', '第五节课'],
  textbookAnalysis: '本课为必修第二册 Unit 3 第五课时（Listening and Talking），语境为"讨论网络安全与网络礼仪"。听力材料为一段关于网络安全建议的对话，口语输出任务为就如何安全、文明地使用互联网给出建议。功能语言为给出建议（You should... / It\'s a good idea to... / Make sure you... / Be careful about...）及表达赞同（I agree. / That makes sense. / I hadn\'t thought of that.）。结合语法课的被动语态，在口语中自然运用完成时被动描述已实施的网络措施。',
  overview: '【学情分析】A班：有基本的上网安全意识，但英文表达"网络风险"的词汇不足。B班：开口意愿低，但网络安全话题贴近生活可激发兴趣。共同问题：给建议时只说"You should be careful"过于笼统——缺乏具体措施。',
  objectives: [
    '语言能力：听懂关于网络安全与礼仪的对话，提取具体建议与理由；能用至少 4 种句型给出网络安全建议并说明原因。',
    '文化意识：了解网络礼仪（netiquette）的概念，形成文明上网的公民意识。',
    '思维品质：在讨论中练习"给出建议→解释理由→回应同伴建议"的完整对话链。',
    '学习能力：通过建议对话训练批判性倾听——听懂同伴的关切后给有针对性的建议。'
  ],
  keyPoints: '① 给建议句型：You should... / It\'s a good idea to... / Make sure you... / Be careful about... ② 赞同/补充句型：I agree. / That makes sense. / I hadn\'t thought of that. / Also... ③ 网络风险词汇：privacy / password / scam / cyberbully / personal information',
  difficulties: '① Make sure you + 动词原形（确保你…）— 学生易写成 Make sure to do（非正式口语可接受但在正式语境用 you + do 更自然）。② cyberbully（网络欺凌）— 发音 /saɪbəbʊli/，cyber- 前缀读 /saɪbə/。③ privacy /prɪvəsi/ 英式 /prɪvəsi/ vs 美式 /praɪvəsi/ — 教材用英式。',
  teachingMethods: '① 听前预测→听中配对→听后产出。② 角色扮演：给一位"网络新手"提建议。③ 网络安全圆桌讨论。',
  preparation: '【PPT课件】P1 网络安全图标（密码锁/隐私盾牌/网络欺凌）；P2 给建议句型板；P3 听力任务题；P4 听力任务卡；P5 回应句型板；P6 角色卡。【实物教具】网络安全建议卡 printed；角色卡（新手/顾问）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 安全图标】教师：Look at these icons. What online problems do they represent? Have you ever had any of these problems? 预设回答：Password stolen. / Someone posted mean comments. / I received a strange message from a stranger. 板书时机：左栏板书 privacy / password / scam / cyberbully。差异化提示：B班中文描述再翻英文；A班用英文简述自己的经历。易错点提醒：privacy 重音在第一音节 /prɪvəsi/ — 不要读成 /praɪvəsi/（美式发音在考试中判错）。' },
    { step: '听力抓建议', time: '10', content: '【PPT P3 听力任务】听对话，抓"谁给了什么建议+为什么"。教师：Listen for: What advice is given? What is the reason? 预设回答：The speaker advises to use strong passwords because weak passwords are easily hacked. 板书时机：配对填表（建议|理由）。差异化提示：B班给配对连线题；A班听写关键词。易错点提醒：hack（黑客攻击）— 既作动词也作名词，"my account was hacked"（被动！）。' },
    { step: '听中记录', time: '8', content: '【PPT P4 听力任务卡】【音频】重听，学生填完整建议+理由+赞同/质疑回应。教师：How did the other person react to the advice? 预设回答：He said "I agree. That makes sense." / "I hadn\'t thought of that before." 板书时机：核对填表。差异化提示：B班给回应选项（A/B/C选）；A班写完整回应句。易错点提醒：I hadn\'t thought of that = 我没想到那个。用过去完成时，表示"在你说之前我没想过"——非常地道的英式回应。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练建议+回应链：A: You should use a different password for each account. / B: I agree. That makes sense because if one is hacked, the others are still safe. / A: Also, make sure you don\'t share your password with anyone. 预设回答跟读+仿造。板书时机：板书建议→回应链条。差异化提示：B班用填空脚本；A班自主对话。易错点提醒：Make sure you + 动词原形 — "Make sure you to use" 是错的，去掉 to。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】两人一组：Newbie（网络新手）和 Advisor（顾问）。新手提出问题（"I\'m worried about..."），顾问给建议。教师巡视。预设回答：A: I\'m worried about my privacy online. / B: You should set your profile to private. Make sure you only accept friend requests from people you know. 板书时机：留句型供参考。差异化提示：B班照卡读；A班脱稿加即兴内容。易错点提醒：给多条建议时用 First / Also / Finally 串起来——"First, use a strong password. Also, don\'t click strange links. Finally, be careful about what you share."' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾给建议句型+赞同回应+网络风险词汇。教师：Remember: one specific tip is better than "be careful." 预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一条最重要的安全建议。易错点提醒：网络礼仪不只是"小心"——还包括尊重他人、不传播假消息、不网络欺凌。' }
  ],
  blackboard: '┌─ U3 Listening & Talking ──────────────────┐\n│ Giving Advice:                              │\n│  You should / shouldn\'t + do...             │\n│  It\'s a good idea to + do...               │\n│  Make sure you + do...                     │\n│  Be careful about + n./doing...            │\n│                                             │\n│ Agreeing / Adding:                          │\n│  I agree. / That makes sense.              │\n│  I hadn\'t thought of that. / Also...        │\n│                                             │\n│ Online Risks:                               │\n│  privacy / password / scam / cyberbully     │\n│  personal information / stranger            │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有建议句型。2. 用至少 2 种建议句型各写 1 句网络安全建议+理由。【提高作业】写 60 词对话：两人讨论如何安全使用社交媒体（至少 4 轮，含建议+回应+补充）。【参考答案——教师用】基础2示例：You should use a strong password with letters, numbers, and symbols. / It\'s a good idea to check your privacy settings every month.',
  reflection: '✅ 亮点：角色扮演"新手vs顾问"让学生有真实的建议目的感。⚠️ 需改进：Make sure you + do 的否定形式 Make sure you don\'t... 仍需强化。📌 下节课衔接：进入写作 I，将讨论中的建议写成博客文章。'
}));

// ====== Period 6: Writing I (博客结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u3-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '博客', '互联网', '人教版必修二U3', '第六节课'],
  textbookAnalysis: '本课为必修第二册 Unit 3 第六课时（Reading for Writing I），写作体裁为关于网络经历的博客文章（Write a Blog Post）。博客结构为：吸引人的标题→开头Hook→主体（你的经历+感受+学到的）→结尾（思考/邀请评论）。语言重点为博客特有的口语化但正式的语气（I\'d like to share... / Here\'s what happened... / Have you ever...?）及互联网词汇。结合本单元 Reading 的人物叙事与语法课的被动语态，实现"读-语法-写"闭环。',
  overview: '【学情分析】A班：有写作能力但博客体裁不熟——博客介于日记和文章之间，语气要亲切但不随意。B班：句型储备少、不知如何开头，需大量范例+模板。共同问题：写博客像写作文——缺少"作者声音"和读者互动感。',
  objectives: [
    '语言能力：掌握博客文章的"Hook→Body→Reflection→Closing"四段结构，在互联网话题中产出 80-100 词语气自然、有互动感的博客文章。',
    '文化意识：理解博客作为数字时代个人表达与社区交流的工具价值。',
    '思维品质：通过"选择经历→提炼感悟→邀请回应"训练从个人经历到普遍意义的思维提炼。',
    '学习能力：建立"博客≠作文"的体裁意识——学会使用 Hook、提问读者、非正式但礼貌的语气。'
  ],
  keyPoints: '① 博客四段结构：Catchy Title → Hook（吸引注意）→ Body（经历+感受）→ Reflection + Call for Comments ② 博客句型：I\'d like to share... / Here\'s what I learned... / Have you ever experienced...? / What about you? ③ 语气：亲切、个人、有互动感但不随意。',
  difficulties: '① 博客标题的技巧——和海报标题不同，博客标题可以长一点但要有好奇心。② Hook 的写法——开头第一句决定读者是否继续。③ 博客结尾的"Call for Comments"——学生不习惯在文章结尾向读者提问。',
  teachingMethods: '① 范本解构法：读优秀博客→提取结构→仿写。② 头脑风暴：选一件互联网相关的个人经历。③ 过程写作：outline→draft→peer review。',
  preparation: '【PPT课件】P1 优秀学生博客范例；P2 博客四段结构图；P3 博客句型库；P4 头脑风暴工作单；P5 写作任务；P6 写作提纲；P7 总结。【实物教具】博客结构模板 printed 每人一份；头脑风暴工作单。',
  process: [
    { step: '范本解构', time: '8', content: '【PPT P1 博客范例】教师展示一篇英文博客范文，学生标注四段：Hook（有趣的开头问题）→ Body（发生了什么+感受）→ Reflection（学到了什么）→ Closing（邀请评论）。教师：What makes this feel like a blog and not a school essay? 预设回答：The writer asks questions to the reader. The tone is friendly. It has "What do you think?" at the end. 板书时机：四段结构板书。差异化提示：B班给标注好的范文只匹配段名；A班自己标注+圈出互动句。易错点提醒：博客的灵魂是"像在和读者聊天"——用 you 称呼读者、问问题、分享真实感受。' },
    { step: '四段结构讲透', time: '8', content: '【PPT P2 结构图】教师逐段讲解：①Title: 有趣+清晰（"How the Internet Changed My World" vs "My Internet Experience"）②Hook: 1-2句抓注意力——可用问题/惊人事实/小故事开头。③Body: 具体经历+你的感受+使用了哪些网络工具。④Closing: 反思+邀请评论——"Have you had a similar experience?" "I\'d love to hear your thoughts!" 教师用 Jan Tchamani 的故事做示范。预设回答跟做。板书时机：逐段板书模板句。差异化提示：B班给每段填空模板；A班给关键词自己写。易错点提醒：Hook 不能用"This is a blog about..."——那是最无聊的开头。试试"Have you ever felt like the Internet saved your life?"' },
    { step: '博客句型库', time: '5', content: '【PPT P3 句型库】教师领读博客高频句型：I\'d like to share a story about... / Here\'s what happened... / At first... but then... / Looking back, I realize... / What I learned is... / What about you? / Have you ever...? / I\'d love to hear your thoughts! 教师强调"用提问建立与读者的连接"。预设回答跟读。板书时机：句型分类板书（开头句/叙述句/反思句/互动句）。差异化提示：B班齐读+背3句；A班选最喜欢的一句说为什么有效。易错点提醒：Looking back, I realize... 中 looking 是分词作状语，主语是 I。不要写成 "Look back, I realize..."（缺 ing）。' },
    { step: '头脑风暴', time: '5', content: '【PPT P4 工作单】学生各自想一件互联网相关的个人经历：第一次上网/在网上交到朋友/在线学习新技能/遇到网络安全问题。用工作单记录：①What happened? ②How did you feel? ③What did you learn? 教师巡视。预设回答：I learned to code from YouTube tutorials. / I made a friend from another city through an online game. 板书时机：巡视指导。差异化提示：B班给选题目录（3选1）；A班自己想。易错点提醒：选你最有感触的经历——真诚比"厉害"更重要。读者能感受到你是否真的在乎这个故事。' },
    { step: '起草博客', time: '10', content: '【PPT P5 写作任务】学生写 80-100 词博客初稿。要求：四段完整、至少 1 个现在完成时被动语态、至少 2 个博客句型、结尾有互动提问。教师巡视提醒：Don\'t write like an essay! Talk to your reader! 预设回答：（学生写作中）板书时机：留四段模板供参考。差异化提示：B班用模板框架填写；A班自由写+追求语气自然。易错点提醒：博客最怕"假大空"——具体细节比泛泛而谈好100倍。不说"The Internet is useful"，说你"学会了什么具体技能/认识了谁"。' },
    { step: '同伴初评', time: '4', content: '【PPT P6 写作提纲】同桌互换博客初稿，check：有四段吗？Hook 抓人吗？有完成时被动吗？结尾有互动提问吗？语气像在聊天吗？教师：Does this blog feel like a real person is talking to you? 预设回答：Yes, but the ending could be more interactive. 板书时机：留 checklist。差异化提示：B班用 checklist 逐项打勾；A班口头给改进建议。易错点提醒：互评时关注"有没有打动我"——如果一篇博客让你读完没感觉，告诉对方哪里可以加真情实感。' }
  ],
  blackboard: '┌─ U3 Writing: Blog Post ─────────────────┐\n│  ① CATCHY TITLE                           │\n│  ② HOOK (question / surprising fact)       │\n│  ③ BODY (what happened + feelings)         │\n│  ④ CLOSING (reflection + ask readers!)     │\n│                                            │\n│  Blog Voice Tips:                          │\n│   Talk TO reader (you / your)             │\n│   Ask questions                            │\n│   Be real & personal                       │\n│   Use: I\'d like to share... / Have you...  │\n│        Looking back... / What about you?   │\n└────────────────────────────────────────────┘',
  exercises: '【基础作业】按课堂初稿完成 80-100 词博客。要求：四段完整、至少 1 个完成时被动、至少 2 个博客句型、结尾有互动提问。【提高作业】将博客发布到班级英语学习群（或打印出来贴在教室），并回复至少 1 位同学的博客评论（英文）。【参考答案——教师用】示例（节选）：Title: "How YouTube Taught Me to Cook" / Hook: "Have you ever learned something life-changing from a video?" / Body: "Last year, I couldn\'t even boil an egg. Then I discovered cooking channels on YouTube..." / Closing: "What skill has the Internet helped YOU learn? Share in the comments!"',
  reflection: '✅ 亮点：博客四段结构让学生从"写作文"变为"写博客"，语气明显更自然。⚠️ 需改进：Hook 仍有学生写"This is a blog about..."，下节课用范文对比强化。📌 下节课衔接：进入写作 II，互评修改+博客展示分享。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u3-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '博客', '互联网', '人教版必修二U3', '第七节课'],
  textbookAnalysis: '本课为必修第二册 Unit 3 第七课时（Writing II），在 Writing I 博客初稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进博客文案的能力——特别关注语气是否自然、是否有读者互动。互评量表聚焦三维度：结构完整（四段）、语言质量（被动语态/博客句型/语气亲切）、读者吸引力（Hook抓人/内容真诚/结尾有互动）。',
  overview: '【学情分析】A班：能辨别博客好坏，但给反馈时只说"写得不错"缺乏具体点（如"Hook 够不够吸引"）。B班：改自己博客时不知从何下手。共同问题：互评时不好意思说真话——博客最需要真实反馈。',
  objectives: [
    '语言能力：能根据互评量表给同伴的博客初稿提具体、可操作的修改建议，重点检查语气是否自然、是否有读者互动。',
    '文化意识：通过阅读同伴的博客了解互联网对不同同学的不同影响。',
    '思维品质：在互评中培养"识别读者体验→提出优化方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步博客写作流程，内化为个人写作习惯。'
  ],
  keyPoints: '① 互评三维量表：结构（四段完整 / 标题吸引）+ 语言（被动≥1 / 博客句型≥2 / 语气亲切）+ 读者体验（Hook抓人？内容真诚？结尾有互动？）② 博客展示技巧：用"读+讲"的方式，先读一段最好的句子，再说写作心得。',
  difficulties: '① 学生互评时不好意思说语气不自然——需示范如何给建设性反馈。② 博客结尾的互动提问太敷衍——"What about you?" 太泛，应更具体。③ 展示时照本宣科没有抑扬顿挫——博客应该读出"聊天感"。',
  teachingMethods: '① 量表互评：用统一标准减少主观性。② 对子互评→修改→展示。③ 最佳博客评选+博客墙展示。',
  preparation: '【PPT课件】P1 互评三维量表；P2 常见问题（Hook弱/语气像作文/无互动/被动语态缺）；P3 修改指南；P4 展示技巧（30秒读+讲）；P5 最佳博客范例；P6 自评表；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①结构（四段全？标题吸引人？）②语言（完成时被动≥1？博客句型≥2？语气亲切？）③读者体验（Hook抓人？内容真诚可信？结尾让读者想回应？）。教师用上节课自己写的博客示范打分。预设回答跟学。板书时机：量表三维板书。差异化提示：B班按量表逐项打勾；A班还需写一句最想对作者说的话。易错点提醒：博客互评最重要的标准是——"你想继续读下去吗？"如果不想，告诉作者为什么。' },
    { step: '互评', time: '12', content: '【PPT P2 常见问题】先展示上节课常见问题：①Hook是"This is a blog about..." ②语气像作文（Therefore / In conclusion）③结尾无互动提问 ④无完成时被动。然后同桌互换初稿，用红笔按量表标注。教师巡视。教师：What is the BEST sentence in this blog? What is one thing to improve? 预设回答：The story about learning to code is great, but the title is boring. 板书时机：留量表供参考。差异化提示：B班按 checklist 勾；A班在稿上写具体修改建议。易错点提醒：给反馈时先说你最喜欢的部分——作者需要知道什么应该保留。' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改博客。顺序：①先调语气（把"Therefore"改成"So"、加 you 称呼读者）②再加语言（插入被动语态/博客句型）③最后检查 Hook 和互动结尾。教师：Does your blog sound like YOU talking? 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色句子多样性。易错点提醒：修改时大声读出自己的博客——耳朵能听出眼睛看不出的不自然。' },
    { step: '博客展示', time: '8', content: '【PPT P4 展示技巧】3-4 位自愿者上台：①先说"我最满意的是…"②再读最精彩的 2-3 句 ③最后说"我是怎么想到这个主题的"。全班投票：最想关注的博客/最真诚的故事/最好的 Hook。预设回答展示。板书时机：记投票结果。差异化提示：B班可看稿读；A班讲写作心得。易错点提醒：展示时语速放慢——你写了80词，但听众需要时间消化。读关键句时停顿+眼神交流。' },
    { step: '结课+自评', time: '5', content: '【PPT P7 总结+自评】宣布最佳博客前三名。学生自评：①我的博客最打动人的地方是？②下次写博客我会注意什么？教师：What makes a good blog post? 预设回答：A good hook, a real story, a friendly tone, and asking the reader something. 板书时机：写最佳博客标题作为范例。差异化提示：B班中文自评；A班英文自评。易错点提醒：博客写作的终极秘诀——写的时候想象你最好的朋友正在读。你会怎么对TA说话，就怎么写。' }
  ],
  blackboard: '┌─ U3 Writing II: Blog Review ─────────┐\n│ Blog Checklist:                        │\n│  ✅ 4 parts (Title/Hook/Body/Close)    │\n│  ✅ ≥1 present perfect passive         │\n│  ✅ ≥2 blog-style phrases              │\n│  ✅ Friendly, personal tone            │\n│  ✅ Engages reader (you/questions)     │\n│  ✅ Ends with call for comments        │\n│                                        │\n│ Blog ≠ Essay:                          │\n│  ✗ Therefore / In conclusion           │\n│  ✓ So... / Here\'s what I think...      │\n└────────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改博客终稿，发布到班级英语学习平台。写 20 词英文评论回复给一位同学的博客。【提高作业】写第二篇博客（50-80词）：主题为"How to Stay Safe Online"，用建议句型给读者提3条具体安全建议。【参考答案——教师用】参考 Writing I 的 exercises 答案。终稿评估标准：结构四段（2分）+完成时被动≥1（2分）+博客句型≥2（2分）+语气亲切有互动（2分）+语法准确（2分）= 10分。',
  reflection: '✅ 亮点：量表培训让学生知道"好博客长什么样"，互评质量显著提升。⚠️ 需改进：部分博客结尾互动提问太泛（"What about you?"），下次可要求加更具体的邀请。📌 下节课衔接：进入 Project，将本单元所学整合为"互联网改变生活"数字展。'
}));

// ====== Period 8: Project (互联网改变生活数字展) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u3-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '互联网', '数字展', '人教版必修二U3', '第八节课'],
  textbookAnalysis: '本课为必修第二册 Unit 3 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的网络词汇+阅读的人物叙事+语法的完成时被动+听与谈的安全建议+写作的博客——完成一份"互联网改变生活"数字展览展板。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确评分标准。B班：group work 中易"搭便车"，需明确定人定责。共同问题：展板变成"贴图片+几个单词"——需强制每模块有完整英文句。',
  objectives: [
    '语言能力：综合运用本单元词汇、完成时被动语态、建议句型、博客句型，以英文完成一份"互联网改变生活"数字展览展板。',
    '文化意识：通过展览形式展示互联网在生活各个方面（教育/社交/工作/健康）的积极影响。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 展板四模块：How the Internet Has Changed... Education / Social Life / Work / Health（至少选2个）② 每个模块：Before→Change→Impact（用完成时被动）③ 单元知识整合：网络词汇/完成时被动/建议句型/博客风格 ④ 小组分工：Researcher / Writer / Designer / Presenter',
  difficulties: '① "改变"的英文表达多样性——学生全篇用 change 一词。提醒：可用 transform / improve / reshape / revolutionize。② 展板中的完成时被动——每个模块至少一个。③ 展板不是"好的方面"列表——也要提挑战（privacy / addiction / misinformation）。',
  teachingMethods: '① PBL项目式学习：以数字展为驱动问题。② 小组协作：角色分工+module checklist。③ 展览+最佳展板评选。',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 展板四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师带学生回顾本单元5课学了什么：听与说（网络活动词汇+上网习惯）→阅读（Jan的故事+互联网赋能）→语法（has been done）→听与谈（安全建议+网络礼仪）→写作（博客文章）。教师：Today we show how the Internet changes lives! 预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出每课核心内容。易错点提醒：每个模块至少用一次现在完成时被动语态——"has been changed / have been connected / has been improved"。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 展板结构】【PPT P3 角色卡】教师展示展板四模块：①Education（在线学习如何改变教育）②Social Life（社交网络如何连接人）③Work（互联网如何改变工作方式）④Health（健康类App如何帮助人）。每组选2-3个模块深挖。角色：Researcher找数据+案例 / Writer写文案 / Designer设计排版 / Presenter准备展示。教师：Pick your modules and role! 预设回答：We choose Education and Social Life. I\'m the researcher. 板书时机：留模块结构和角色。差异化提示：B班给语言模板+数据参考；A班自己找数据和案例。易错点提醒：每个模块都要用"Before→Change→Impact"逻辑——不是列优点，是讲故事。' },
    { step: '制作展板', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】小组制作。教师巡视提醒：①全英文！②每模块至少3句完整句 ③至少2个完成时被动 ④要提挑战（不是只说好话）⑤最后3分钟 Presenter 准备。预设回答：（小组讨论制作中，教师巡视指导）板书时机：无。差异化提示：B班给句型开头提示（Before the Internet,... / Now,... / As a result,...）；A班独立完成。易错点提醒：挑战部分不是"否定互联网"——是提出需要解决的问题，让展板更有深度。例："However, online privacy has not been fully protected."' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】每组 2 分钟展示。全班投票：最佳内容/最佳设计/最佳展示/最有启发性的展板。教师：Make us see the Internet differently! 预设回答展示。板书时机：记投票结果。差异化提示：B班可看展板讲；A班脱稿补充。易错点提醒：2分钟展示结构——30秒概述+30秒模块1+30秒模块2+30秒结论。每个模块一个关键数据+一个被动句。' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】学生勾选四维薄弱项：网络词汇不熟？完成时被动不会用？建议句型忘了？博客结构不熟？写1条补强计划。教师：Which part of this unit do you need more practice on? 预设回答：I need to practice the present perfect passive with irregular verbs. I will make a list of 10 irregular past participles and write sentences. 板书时机：留自评四维。差异化提示：B班中文写；A班英文写。易错点提醒：补强计划要有时间节点——"这周末前完成"，而不是"有空再做"。' }
  ],
  blackboard: '┌─ U3 Project: Internet Changes Lives ──┐\n│ 🌐 Exhibition Modules:                  │\n│  ① Education (online learning)         │\n│  ② Social Life (connection)            │\n│  ③ Work (remote work / skills)         │\n│  ④ Health (apps / information)         │\n│                                         │\n│  Each Module:                           │\n│  Before → Internet Change → Impact     │\n│  + Challenge (privacy / addiction)     │\n│                                         │\n│ 👥 Roles: Researcher / Writer /         │\n│            Designer / Presenter         │\n│                                         │\n│ ⭐ Must: ≥2 present perfect passive     │\n│          per board                      │\n└─────────────────────────────────────────┘',
  exercises: '【基础作业】完成小组展板（未完成的继续做），拍照片提交。写 30 词英文反思：我的角色是…从这个项目我学到了互联网的…【提高作业】选一个不在此次展板中的互联网话题（如AI/电商/在线医疗），写 50 词英文简报。【参考答案——教师用】反思示例：I was the writer for the Education module. I learned that the Internet has transformed how we learn — online courses have been accessed by millions who couldn\'t go to school before. What surprised me most is that the digital divide still exists as a major challenge.',
  reflection: '✅ 亮点：Before→Change→Impact 框架让展板有逻辑深度。⚠️ 需改进：部分小组"挑战"部分太空泛，下次可要求举具体例子。📌 下节课衔接：进入 Unit 4 History and Traditions，从数字世界转向历史文化探索。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b2-u3-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b2-u3 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
