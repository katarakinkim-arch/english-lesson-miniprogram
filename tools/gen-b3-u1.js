/**
 * gen-b3-u1.js — 必修第三册 Unit 1 Festivals and Celebrations (8课时)
 *
 * 语篇: WHY DO WE CELEBRATE FESTIVALS? (节日的精神内核: harvest/ancestors/reunion/new year)
 * 语法: -ing形式作定语和状语 (a crying baby / Walking in the park, I saw...)
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

const BC = 'b3';
const UNIT = 1;
const UNIT_TITLE = 'Festivals and Celebrations';
const BOOK = '必修第三册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u1-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '节日', '庆祝', '人教版必修三U1', '第一节课'],
  textbookAnalysis: '本课为必修第三册 Unit 1 Festivals and Celebrations 第一课时（Listening and Speaking），属单元导入+输入环节。听力材料为一段介绍世界各地节日（春节/感恩节/排灯节/亡灵节）的对话与独白，功能语境是"描述节日及其庆祝方式"。语言重点为节日词汇（festival, celebrate, harvest, origin, gratitude, gather, costume, parade）及描述节日句型（It is celebrated to... / People usually... / The festival features...）。为本单元 Reading 的"节日精神内核"议论文做词汇与话题预热。',
  overview: '【学情分析】A班：对春节/中秋等中国节日英文表达较熟，但 harvest/gratitude/origin 等抽象词较生。B班：对外国节日（排灯节/亡灵节）几乎无背景，听力抓细节弱。共同问题：描述节日停留在"好吃好玩"表层，缺乏"节日的意义/精神"表达。',
  objectives: [
    '语言能力：听懂关于世界各地节日的听力材料，提取关键信息（名称/时间/活动/意义），准确使用 6-8 个节日核心词汇。',
    '文化意识：了解中外节日的多样性，体会节日背后的感恩/纪念/团聚等共通精神。',
    '思维品质：通过"听前预测—听中验证—听后比较"形成系统听力策略。',
    '学习能力：能用 It is celebrated to... / People usually... 就节日做简短描述与对比。'
  ],
  keyPoints: '① 节日核心词汇：festival / celebrate / harvest / origin / gratitude / gather / costume / parade ② 描述句型：It is celebrated to... / People usually... / The festival features... ③ 听力微技能：听前读题支预测关键词、听中抓活动与时间。',
  difficulties: '① harvest（丰收）与 festival（节日）的拼写与发音区分。原因：词形相近。易错点提醒：harvest /hɑːvɪst/，festival /festɪvəl/。② gratitude（感恩）抽象名词，学生易与 great 混淆。③ 排灯节(Diwali)/亡灵节(Day of the Dead)背景陌生，听力时影响理解。',
  teachingMethods: '① 任务型（TBL）：以介绍一个节日为终任务。② 听前预测+听中填卡：信息卡脚手架。③ 对子互问操练描述句型。',
  preparation: '【PPT课件】P1 单元封面（Festivals and Celebrations）；P2 世界节日图片九宫格（春节/中秋/清明/感恩节/圣诞节/万圣节/排灯节/亡灵节/狂欢节）；P3-4 听力任务题；P5 描述句型板；P6 说话任务卡。【实物教具】节日信息卡 printed 每组一套；世界地图一张。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine festival pictures. Which ones are Chinese festivals? Can you name them in English? 预设回答：Spring Festival, Mid-Autumn Festival, Tomb-Sweeping Day! 板书时机：右侧板书 festival / celebrate / harvest。差异化提示：B班指图说中文再跟读英文；A班用 I can see... 造句。易错点提醒：harvest /hɑːvɪst/ 的 a 发 /ɑː/ 不发 /æ/。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 festival / celebrate / harvest / origin / gratitude / gather / costume / parade。教师：Why do people celebrate the Spring Festival? 预设回答：To gather with family and welcome the new year. 板书时机：左栏板书词+短注释。差异化提示：B班配图记忆+词性标注；A班用词造句。易错点提醒：gratitude /ɡrætɪtjuːd/ — 与 great 完全无关，词根 grat 表"感激"。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to an introduction about Diwali and Day of the Dead. Predict: What will be mentioned? (time / activities / food / meaning) 预设回答：Time and activities! 板书时机：预测词写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测理由。易错点提醒：听力常见陷阱 — 信息会先给错误再修正。"in October" 可能被后面"actually in November"推翻。' },
    { step: '听中填卡', time: '10', content: '【PPT P5 表格】【音频 段一】播放听力，学生填信息卡（节日/时间/活动/意义）。教师：When is Diwali? What do people do? 预设回答：In autumn. People light lamps and celebrate light over darkness. 板书时机：核对答案时填表于黑板中部。差异化提示：B班听两遍只填名称+时间；A班一遍填全。易错点提醒：darkness /dɑːknəs/ — 与 darkness 拼写一致但注意 -ness 后缀。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to describe a festival? It is celebrated to... / People usually... / The festival features... 教师示范后用春节信息造句。预设回答：The Spring Festival is celebrated to welcome the new year. People usually gather and have a big dinner. 板书时机：句型板书于中央。差异化提示：B班套用模板；A班替换节日名+活动细节。易错点提醒：celebrate 后直接接节日名 — celebrate the Spring Festival，不加 to 或 for。' },
    { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，从信息卡中选一个节日互介。教师：Introduce a festival to your partner. Use the sentence patterns. 预设回答：I want to introduce the Day of the Dead. It is celebrated to remember ancestors. People usually dress in costumes and parade. 板书时机：无。差异化提示：B班用填空式对话卡；A班自由描述并追问理由。易错点提醒：parade /pəreɪd/ 重音在第二音节，不是第一音节。' }
  ],
  blackboard: '┌─ U1 Listening & Speaking ──────┐\n│ festival / celebrate / harvest    │\n│ origin / gratitude / gather       │\n│ costume / parade / darkness       │\n│                                   │\n│ It is celebrated to...            │\n│ People usually...                 │\n│ The festival features...          │\n│                                   │\n│ Festival Info Card:               │\n│  Diwali | autumn | lamps | light  │\n│  Day of Dead | Nov | costume|para │\n└───────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有节日词汇。2. 用 It is celebrated to... 写 3 句节日描述。【提高作业】用英文写一段 50 词介绍：介绍一个你了解的节日（中外均可），包含名称/时间/至少 2 点活动/1 点意义。【参考答案——教师用】基础2示例：The Spring Festival is celebrated to welcome the new year. / The Mid-Autumn Festival is celebrated to gather with family. / Thanksgiving is celebrated to express gratitude for the harvest.',
  reflection: '✅ 亮点：九宫格激活+信息卡脚手架有效降听力焦虑，B班填卡完成率高。⚠️ 需改进：gratitude 发音仍有困难，下节需强化。📌 下节课衔接：进入阅读 WHY DO WE CELEBRATE FESTIVALS?，从节日现象延伸到精神本质。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u1-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '节日', '议论文', '节日精神', '人教版必修三U1', '第二节课'],
  textbookAnalysis: '本课为必修第三册 Unit 1 第二课时（Reading I），语篇 WHY DO WE CELEBRATE FESTIVALS? 是一篇"现象—本质"型议论文，探讨世界各地节日背后的共同精神——丰收感恩、纪念先人、家庭团聚、迎接新年，并指出节日日趋商业化但核心精神未变。结构为现象引入→分类举例→本质归纳→商业化转折→精神升华。语言重点为议论文衔接词（however, after all, no matter how）与节日主题词汇（harvest, gratitude, origin, commercial, figure, gather）。承接第一课时词汇，本课语篇中出现 -ing 形式作定语与状语。',
  overview: '【学情分析】A班：能快速把握段落主旨，但对"现象→本质"的归纳思维训练不足。B班：对排灯节/亡灵节等外国节日背景知识少，需图片+视频脚手架。共同问题：议论文的"分类举例→本质归纳"结构感知不清晰，易忽略 however/no matter how 等转折标志词。',
  objectives: [
    '语言能力：读懂"现象—本质"型议论文，提取节日的四类精神内核及文中例证；掌握 8-10 个论述类核心词汇。',
    '文化意识：理解中外节日虽形式各异却共享感恩/纪念/团聚/希望的精神，增强文化自信与包容。',
    '思维品质：通过"分类举例→本质归纳"分析培养议论文结构思维与抽象概括能力。',
    '学习能力：能用四类精神内核表格+主旨句复述文章主线。'
  ],
  keyPoints: '① 议论文结构：phenomena → categories (harvest/ancestors/reunion/new year) → unity → commercial turn → spirit ② 衔接词：however / after all / no matter how / no matter who ③ 核心短语：range from... to... / have... in common / after all',
  difficulties: '① commercial / commercialised 的情感色彩——学生易误判为纯贬义，实际课文客观指出趋势。原因：母语"商业化"常含贬义。② no matter how/who/what 让步状语从句与 however/whoever/whatever 的转换。③ 从"读节日现象"到"写一句本质定义"的抽象概括。',
  teachingMethods: '① 分类阅读：按四类精神内核分组读段。② 主旨句定位法：每段首尾句抓核心。③ 问题链追问：训练批判性思维。',
  preparation: '【PPT课件】P1 各国节日拼图；P2 四类精神内核框架图；P3-4 文本结构时间线；P5 议论文结构图；P6 词汇对比表；P7 总结回顾。【实物教具】四类精神内核空白工作单 printed 每人一份；段落拼图卡。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P1 节日拼图】教师：We celebrated many festivals. But have you ever thought — why do we celebrate? What is the deepest reason? 预设回答：To have fun? / To remember family? / To give thanks? 板书时机：板书 Why? + 四个问号。差异化提示：B班中文猜；A班英文猜并给理由。易错点提醒：deepest reason 不是"最深的原因"而是"最根本的理由"——deepest 表程度。' },
    { step: '快速阅读抓主干', time: '8', content: '【PPT P3 结构线】教师：Read fast (3 min). Find: ① How many categories of festivals? ② What is the common spirit? ③ Does the author mention any change? 预设回答：① Four categories. ② Gratitude, love, hope. ③ Yes, festivals are more commercial now. 板书时机：填四类精神内核框架。差异化提示：B班给四选一选项；A班写完整句。易错点提醒：origin /ɒrɪdʒɪn/ — o 发 /ɒ/ 不发 /əʊ/。' },
    { step: '精读段落1-3 分类举例', time: '10', content: '【PPT P4 四类表】教师精讲：range from... to... = 范围从…到…；have... in common = 有共同点。教师：What are the four categories? Give an example for each. 预设回答：Harvest — Thanksgiving. Ancestors — Day of the Dead. Reunion — Spring Festival. New year — New Year\'s Day. 板书时机：左侧栏补充"range from / have in common / gratitude"。差异化提示：B班读后填关键词；A班读后用自己话解释。易错点提醒：common 作名词"共同点"，作形容词"普通的"——语境区分。' },
    { step: '精读段落4-5 本质与转折', time: '10', content: '【PPT P5 结构图】教师：What is the common spirit? And what change does the author mention? 预设回答：The spirit is about gratitude, love and hope. But festivals are becoming commercial. 板书时机：右侧画"unity→commercial turn→spirit"箭头图。差异化提示：B班连线匹配；A班写完整句。易错点提醒：commercial 在文中是客观描述不是批评——作者认为核心精神未变。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 议论文结构】教师：What can we learn? (Festivals reflect who we are. / The spirit matters more than the form.) 预设回答：Festivals are about who we are. The commercial part doesn\'t change the spirit. 板书时机：圈出结构关键词。差异化提示：B班跟读关键词；A班用自己的话总结。易错点提醒：reflect /rɪflekt/ — re- 前缀"回"，flect 词根"弯曲"=反射。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾"现象→分类→本质→转折→精神"结构+核心词汇。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：commercial /kəmɜːʃəl/ — 不是 /kəmɔːʃəl/。' }
  ],
  blackboard: '┌─ U1 Reading I: WHY DO WE CELEBRATE? ────┐\n│ PHENOMENA → CATEGORIES → UNITY → TURN   │\n│                                          │\n│ 4 spirits: Harvest / Ancestors /         │\n│            Reunion / New Year            │\n│ Common: gratitude, love, hope            │\n│                                          │\n│ range from... to... / have in common     │\n│ after all / no matter how                │\n│ commercial → but spirit unchanged        │\n└──────────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-3段 2 遍，圈出所有转折词（however/after all/no matter）。2. 用四类精神内核各写1句节日例证。【提高作业】用 80 词左右写一段：你认为节日的商业化是否削弱了其精神？为什么？（用 commercial / spirit / after all）【参考答案——教师用】基础2示例：Harvest festivals like Thanksgiving celebrate the gathering of crops. / Ancestor festivals like the Day of the Dead remember those who passed away. / Reunion festivals like the Spring Festival bring families together. / New year festivals welcome a fresh beginning.',
  reflection: '✅ 亮点：四类精神内核框架有效组织信息，B班完成率高。⚠️ 需改进：commercial 的情感色彩学生仍感困惑，精读课需澄清。📌 下节课衔接：进入精读语言+-ing 形式在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u1-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '-ing形式', '节日', '人教版必修三U1', '第三节课'],
  textbookAnalysis: '本课为必修第三册 Unit 1 第三课时（Reading II），聚焦语篇 WHY DO WE CELEBRATE FESTIVALS? 的精读与语言分析。重点分析文中 -ing 形式作定语（a crying baby, the singing children）和作状语（Walking in the park, I saw... / Celebrating together, families...）在议论文中的功能——使语言更简洁生动、表达伴随或原因。同时深化语篇中高频学术词汇的用法辨析（origin / figure / range / gather / commercial）。',
  overview: '【学情分析】A班：能识别 -ing 形式，但辨析其作定语还是状语仍有困难。B班：-ing 概念感模糊，需大量语境例句支撑。共同问题：阅读中见到 -ing 结构会跳过不分析其功能——学生把 -ing 当"现在进行时一部分"而非"独立语法工具"。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 5 个 -ing 形式作定语或状语的用法，准确辨析功能。',
    '文化意识：通过 -ing 形式体会英语如何用简洁结构表达伴随与原因——不同于中文的习惯。',
    '思维品质：分析 -ing 形式在议论文中的"信息压缩"功能，培养语法服务于意义的意识。',
    '学习能力：建立"从读到写"的语料库——积累课文中的优质 -ing 句型用于后续写作。'
  ],
  keyPoints: '① 语篇中 -ing 作定语（前置 a crying baby / 后置 the children singing）与作状语（Walking..., I saw / Celebrating..., we...） ② 议论文高频动词：origin / figure / range / gather / commercial ③ -ing 形式在议论文中的修辞功能：简洁生动→增强感染力',
  difficulties: '① -ing 作定语 vs 作状语的辨析。原因：形同功不同，需看句法位置。② figure（人物/数字/认为）多义词在文中的含义。③ origin（起源）与 original（原始的）的词性转换 — 学生易混淆拼写。',
  teachingMethods: '① 标注法：圈出文中所有 -ing 结构并分析功能。② 替换练习：改写从句为 -ing 状语。③ 语料卡记录：分类摘录优质句子。',
  preparation: '【PPT课件】P1-2 课文中圈出的 -ing 示例；P3 定语vs状语对比表；P4 语料卡模板；P5 词汇辨析表；P6 句型改写练习；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 结构图】教师：Last class we learned the four spirits of festivals. Can you recall them? 预设回答：Harvest, ancestors, reunion, new year. The common spirit is gratitude, love and hope. 板书时机：左栏写四类精神内核。差异化提示：B班看框架图读关键词；A班完整复述。易错点提醒：recall ≠ remember — recall 更强调"主动调取记忆"。' },
    { step: '-ing 形式发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle all -ing forms in the text. Decide: is it an attribute (定语) or an adverbial (状语)? 学生标记后全班核对。教师：Why does the author use -ing here? 预设回答：To make the sentence shorter and more vivid. 板书时机：逐句板书圈出的 -ing 结构。差异化提示：B班给划线句直接圈 -ing；A班自己找+标注功能。易错点提醒："a crying baby" 中 crying 作定语修饰 baby，不是进行时。' },
    { step: '定语vs状语辨析', time: '10', content: '【PPT P3 对比表】教师对比：定语——修饰名词（前置 a sleeping child / 后置 the people celebrating）；状语——修饰动词或全句（Walking home, I felt happy = When I walked home...）。教师例句辨析。预设回答辨析。板书时机：两列对比板书。差异化提示：B班根据提示选择填空；A班独立造句。易错点提醒：-ing 状语的逻辑主语必须与主句主语一致——"Walking home, the rain started" 是错的（rain 不能 walk）。' },
    { step: '语料库搭建', time: '10', content: '【PPT P4 模板】教师：Now build your corpus. Extract -ing examples and key verbs into three categories. 学生分类填语料卡：①-ing 作定语优质句摘录 ②-ing 作状语优质句摘录 ③议论文动词（origin/figure/range/gather/commercial）。板书时机：巡视指导。差异化提示：B班填词；A班造句。预设回答：按节日语料库模板分类填写词条。易错点提醒：figure 在文中表"人物"（a great figure），不是"数字"也不是"认为"。' },
    { step: '句型改写', time: '5', content: '【PPT P6 练习】教师给从句，学生改写为 -ing 状语。例：When they celebrate together, families feel close. → Celebrating together, families feel close. 预设回答造句。板书时机：板书改写公式。差异化提示：B班给改写框架；A班独立改。易错点提醒：改写后检查逻辑主语一致性——主句主语必须能发出 -ing 动作。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】教师：Let\'s review. What does -ing do as attribute and adverbial? 回顾 -ing 作定语/状语功能+语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课深入讲 -ing 的两种功能及改写规则。' }
  ],
  blackboard: '┌─ U1 Reading II: Language Focus ──────┐\n│ -ing as Attribute (定语):             │\n│  前置: a crying baby, sleeping child  │\n│  后置: the people celebrating         │\n│ -ing as Adverbial (状语):             │\n│  Walking home, I felt happy.          │\n│  Celebrating together, we feel close. │\n│                                       │\n│ Verbs: origin / figure / range        │\n│        gather / commercial            │\n│                                       │\n│ Rule: -ing 主语 = 主句主语!           │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出5个 -ing 结构并标注定语/状语。2. 将以下从句改写为 -ing 状语：When she walked in the park, she saw beautiful flowers.【提高作业】用 -ing 作定语和状语各写2句关于节日的句子。【参考答案——教师用】基础2示例：Walking in the park, she saw beautiful flowers.',
  reflection: '✅ 亮点：标注发现法让学生主动探索语法，参与度高。⚠️ 需改进：-ing 状语逻辑主语一致性仍有混淆，语法课需强化。📌 下节课衔接：进入语法课，系统讲 -ing 作定语和状语的规则。'
}));

// ====== Period 4: Grammar (-ing形式作定语和状语) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u1-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '-ing形式', '定语', '状语', '人教版必修三U1', '第四节课'],
  textbookAnalysis: '本课为必修第三册 Unit 1 第四课时（Discovering Useful Structures），系统教学 -ing 形式作定语和状语的用法。基于 Reading 语篇中提取的例句，引导学生归纳出规则：作定语（前置修饰名词表性质/状态，后置相当于定语从句）和作状语（表时间/原因/条件/伴随/让步，逻辑主语与主句主语一致）。通过节日主题的语境化练习巩固。',
  overview: '【学情分析】A班：知道 -ing 表进行时，但作定语和状语是语法新知。B班：-ing 概念仍模糊，需大量语境化例句反复操练。共同问题：写作中要么不用 -ing，要么乱用导致逻辑主语不一致。',
  objectives: [
    '语言能力：准确识别并产出 -ing 形式作定语和状语的句子，在节日话题中产出 5 个以上正确句子。',
    '文化意识：通过 -ing 形式更简洁生动地描述节日场景。',
    '思维品质：通过"发现例句→归纳规则→应用规则"的归纳法培养语法学习策略。',
    '学习能力：建立"语法自查表"——写作后自行检查 -ing 状语的逻辑主语是否一致。'
  ],
  keyPoints: '① -ing 作定语：前置（a crying baby 表性质）/ 后置（the boy crying there 相当于定语从句）② -ing 作状语：表时间/原因/条件/伴随/让步 ③ 逻辑主语一致性：-ing 状语的逻辑主语 = 主句主语',
  difficulties: '① -ing 状语逻辑主语一致性问题。原因：学生写作中常忽略，如"Walking home, the rain started"（错误）。② -ing 作定语前置 vs 后置的选择。③ -ing 状语与谓语动词的时间关系——同时还是先于。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习 ② 改写对比：从句 vs -ing 状语 ③ 改错练习：纠正典型错误',
  preparation: '【PPT课件】P1 定语vs状语对比表；P2 课文例句摘录；P3 规则归纳页；P4 逻辑主语一致性；P5 改写任务卡；P6 改错题；P7 总结。【实物教具】句型卡一套；改写工作单。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中5个 -ing 结构，学生圈 -ing 并判断定语/状语。教师：What does this -ing modify? A noun or a verb? 预设回答：It modifies a noun — it\'s an attribute. / It modifies the whole sentence — it\'s an adverbial. 板书时机：左栏板书例句，标注功能。差异化提示：B班只圈词不分析功能；A班分析 -ing 修饰什么。易错点提醒：-ing 作定语修饰名词，作状语修饰动词或全句——看修饰对象定功能。' },
    { step: '规则归纳', time: '12', content: '【PPT P3 对比表】教师引导学生归纳：定语——前置 a sleeping child（表性质状态）/ 后置 the child sleeping there（≈ who is sleeping there）；状语——Walking home, I felt happy（时间）/ Being tired, he rested（原因）。教师：When -ing is an adverbial, what must we check? 预设回答：The subject must be the same as the main clause! 板书时机：板书完整对比表。差异化提示：B班填已给框架表；A班自己画表填。易错点提醒：-ing 后置定语相当于缩减的定语从句——the boy crying there = the boy who is crying there。' },
    { step: '逻辑主语讲练', time: '8', content: '【PPT P4 结构】教师：The -ing adverbial\'s logical subject = main clause subject. 例句正误对比：✓ Walking home, I saw a rainbow. ✗ Walking home, the rain started. (rain can\'t walk!) 预设回答辨析：第二句错，rain 不是 walk 的主语。板书时机：板书正误对比公式。差异化提示：B班选词填空（判断对错）；A班改写句子。易错点提醒：检查 -ing 状语时永远问一句"谁在做 -ing 的动作？是否=主句主语？"' },
    { step: '改写操练', time: '8', content: '【PPT P5 改写卡】教师给从句，学生改写为 -ing 状语。例：When she celebrated the festival, she wore a costume. → Celebrating the festival, she wore a costume. 教师抽学生板演。预设回答造句。板书时机：板书改写公式。差异化提示：B班给句型框；A班自由改写并追加节日主题细节。易错点提醒：改写后必须检查逻辑主语——主句主语要能发出 -ing 动作。' },
    { step: '改错巩固', time: '3', content: '【PPT P6 改错】教师：Find the mistakes in these three sentences. 展示 3 个典型错误：①Walking home, the bus came.（逻辑主语不一致）②A crying baby is in the room is cute.（重复谓语）③The people celebrate in the square is happy.（缺 -ing）。学生纠错并解释。预设回答纠错。板书时机：板书错误→改正公式。差异化提示：B班辨别对错选；A班解释为什么错。易错点提醒：最常犯——逻辑主语不一致，写作后必须自查。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Let\'s review the -ing rules. 回顾 -ing 定语/状语比较表+逻辑主语要诀+改错公式。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述规则。易错点提醒：写作后自查——每个 -ing 状语的主语是否=主句主语？' }
  ],
  blackboard: '┌─ U1 Grammar: -ing as Attribute & Adverbial ─┐\n│ Attribute (定语):                              │\n│  前置: a crying baby (性质)                    │\n│  后置: the boy crying there (≈ who is crying)  │\n│ Adverbial (状语):                              │\n│  时间: Walking home, I saw a rainbow.          │\n│  原因: Being tired, he rested.                 │\n│  伴随: She sang, dancing happily.              │\n│                                                │\n│ ⚠️ Rule: -ing 主语 = 主句主语!                 │\n│ ✗ Walking home, the rain started.              │\n└────────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 用 -ing 作定语和状语各造 2 句关于节日的句子。2. 将以下从句改写为 -ing 状语：When they gathered for dinner, the family felt happy.【提高作业】写 60 词短文描述一个节日场景，要求至少用 3 个 -ing 结构（含1个定语、1个状语）。【参考答案——教师用】基础1示例：The dancing children brought joy to the festival. (定语) / Celebrating the harvest, farmers expressed gratitude. (状语) 基础2示例：Gathering for dinner, the family felt happy.',
  reflection: '✅ 亮点：改写对比让语法操练不再枯燥，课堂活跃度高。⚠️ 需改进：逻辑主语一致性仍是难点，听与谈课可融入练习。📌 下节课衔接：听与谈聚焦节日庆祝策划，用语篇巩固 -ing 形式。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u1-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '节日庆祝', '策划', '人教版必修三U1', '第五节课'],
  textbookAnalysis: '本课为必修第三册 Unit 1 第五课时（Listening and Talking），语境为"策划一个节日庆祝活动"。听力材料为一段关于学校文化节策划的对话，口语输出任务为就一个节日庆祝活动做策划与分工。功能语言为提议与分工（How about...? / Why don\'t we...? / I\'ll be responsible for... / Let\'s divide the tasks）。结合语法课所学的 -ing 形式，在口语中自然运用 -ing 描述伴随活动。',
  overview: '【学情分析】A班：能提出简单提议，但缺乏"提议+分工"的完整表达链。B班：开口意愿低、分工句型储备少。共同问题：只说提议不分工，缺少 I\'ll be responsible for... 使表达不完整。',
  objectives: [
    '语言能力：听懂关于节日庆祝策划的对话，提取活动内容与分工；能用至少 4 种句型提议并分工。',
    '文化意识：体会"集体策划节日庆祝"的协作精神与参与意识。',
    '思维品质：在讨论中练习"提议→分工→回应"的完整对话链。',
    '学习能力：通过策划对话训练批判性倾听——听懂后回应而非只等自己说。'
  ],
  keyPoints: '① 提议句型：How about doing...? / Why don\'t we...? / I suggest we... / We could... ② 分工句型：I\'ll be responsible for... / Let me handle... / You\'re in charge of... ③ 听力重点：抓住活动+负责人的配对信息',
  difficulties: '① Why don\'t we... 是提议不是疑问 — 学生易用 Why not we...（错误）。原因：母语直译干扰。② responsible for（负责）的介词 for 易漏。③ 回应时 only say "ok" no follow-up — 需培养 I\'ll... 跟进的意识。',
  teachingMethods: '① 听前预测→听中配对→听后产出 ② 角色扮演：三人一组（策划者+执行者+协调者）③ 节日庆祝策划圆桌讨论',
  preparation: '【PPT课件】P1 待策划节日场景（学校文化节/班级中秋 party）；P2 提议句型板；P3 听力任务题；P4 听力任务卡；P5 分工句型板；P6 角色卡。【实物教具】节日策划建议卡 printed；角色卡。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 节日场景】教师：Our class will hold a Mid-Autumn Festival party. What should we prepare? 预设回答：Mooncakes! / Lanterns! / Poems about the moon! 板书时机：左栏板书动词 prepare / organize / arrange / decorate。差异化提示：B班中文说再翻英文；A班直接英文。易错点提醒：prepare（准备）≠ prepare for（为…做准备），前者接物后者接事件。' },
    { step: '听力抓提议', time: '10', content: '【PPT P3 听力任务】听对话，抓"谁提了什么提议+谁负责什么"。教师：Listen for: What is the suggestion? Who is responsible? 预设回答：They suggest making lanterns. Li Ming is responsible for buying materials. 板书时机：配对填表（活动|负责人）。差异化提示：B班给配对连线题；A班听写关键词。易错点提醒：listen for（有目的地听）≠ listen to（泛听）——引导学生带问题听。' },
    { step: '听中记录', time: '8', content: '【PPT P4 听力任务卡】【音频】重听，学生填完整提议+分工链。教师：How did they divide the tasks? 预设回答：Wang Fang will handle decorations. Zhang Lei is in charge of music. 板书时机：核对填表。差异化提示：B班听两遍；A班一遍+复述分工。易错点提醒：be in charge of（负责）与 be responsible for（对…负责）可互换，但介词不同。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练提议+分工链：A: How about making lanterns? / B: That\'s a great idea! I\'ll be responsible for buying paper. / A: Good. You\'re in charge of design. 预设回答跟读+仿造。板书时机：板书提议→分工链条。差异化提示：B班用填空脚本；A班自主对话。易错点提醒：be responsible for 后接 doing — "responsible for buying" 不是 "responsible for buy"。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】三人一组：Planner A（策划者）、Doer B（执行者）、Coordinator C（协调者）。就班级中秋 party 策划讨论。教师巡视。预设回答：A: How about a poem contest? / B: I\'ll handle the prizes! / C: I\'ll coordinate the schedule. 板书时机：留提议句型和分工链供参考。差异化提示：B班照卡读；A班脱稿加即兴内容。易错点提醒：角色扮演中注意用 -ing 描述伴随活动 — "Celebrating together, we will sing and dance."' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾提议句型+分工策略。教师：Remember: after suggesting, assign a task. 预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一句收获。易错点提醒：给同伴分工后记得确认"can you handle that?"——对话是双向的。' }
  ],
  blackboard: '┌─ U1 Listening & Talking ─────────┐\n│ Suggestions:                       │\n│  How about + doing...?             │\n│  Why don\'t we + do...?             │\n│  I suggest we + do...              │\n│  We could + do...                  │\n│                                    │\n│ Division of labor:                 │\n│  I\'ll be responsible for + doing   │\n│  Let me handle + n./doing          │\n│  You\'re in charge of + n./doing    │\n│                                    │\n│ Chain: Suggest → Assign → Confirm  │\n└────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有提议句型。2. 用至少 2 种提议句型各写 1 句节日庆祝提议+分工。【提高作业】写 60 词对话：三人讨论如何策划班级春节联欢（至少 4 轮，含提议与分工）。【参考答案——教师用】基础2示例：How about making dumplings together? I\'ll be responsible for buying ingredients. / Why don\'t we have a talent show? You\'re in charge of the stage.',
  reflection: '✅ 亮点：角色扮演三角色设置让学生理解真实策划中的协作分工。⚠️ 需改进：be responsible for 介词 for 仍漏，写作课可设置强制格式。📌 下节课衔接：进入写作，将节日经历写成记叙文。'
}));

// ====== Period 6: Writing I (结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u1-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '记叙文', '节日经历', '人教版必修三U1', '第六节课'],
  textbookAnalysis: '本课为必修第三册 Unit 1 第六课时（Reading for Writing I），写作体裁为记叙文——写一次难忘的节日经历。结构为：背景设定（when/where/who）→ 活动经过（what happened, in order）→ 感受升华（feelings + meaning）。语言重点为记叙文时间连接词（first, then, after that, finally）与情感描写词（excited, joyful, grateful, moved）。结合本单元 Reading 的节日精神与语法课的 -ing 形式，实现读-语法-写的闭环。',
  overview: '【学情分析】A班：有基本叙事能力，但缺乏"经过→感受"的升华意识——常写成流水账。B班：句型储备少、时态混乱，需大量脚手架（模板+语料卡）。共同问题：记叙文不知如何收尾——缺少"这次经历让我明白…"的感悟句。',
  objectives: [
    '语言能力：掌握"背景—经过—感受"三段式记叙文结构，在节日经历话题中产出 80-100 词结构完整的短文。',
    '文化意识：通过书写节日经历体会节日的精神内核与个人情感联结。',
    '思维品质：通过"先叙事再感悟"训练事件—情感—意义的递进逻辑思维。',
    '学习能力：建立"写作前先搭结构框架"的习惯——用 outline 而非直接开写。'
  ],
  keyPoints: '① 记叙文三段结构：Background (when/where/who) → Process (what, in order) → Feelings (meaning) ② 时间连接词：First / Then / After that / Finally ③ 核心句型：I will never forget... / It made me realize... / The most unforgettable part was...',
  difficulties: '① 记叙文时态——主体用过去时，感受升华可用现在时。原因：学生易全文现在时。② after that 与 afterwards 的区别。③ 感受升华句不知道怎么写——需给模板。',
  teachingMethods: '① 范文解构法：读范文→画结构图→仿写 ② 语料卡搭建：从本单元5课积累词汇/句型。③ 过程写作：outline→draft→peer review→revise',
  preparation: '【PPT课件】P1 范文（关于一次春节经历的记叙文）；P2 三段结构图；P3 时间连接词表；P4 语料库模板；P5 写作提纲；P6 写作任务；P7 总结。【实物教具】三段结构空白工作单 printed 每人一份；语料卡模板。',
  process: [
    { step: '范文解构', time: '8', content: '【PPT P1 范文】教师展示范文，学生标注三段（背景/经过/感受）。教师：Which paragraph tells us what happened? Which tells feelings? 预设回答：Paragraph 2 — the process. Paragraph 3 — the feelings. 板书时机：画三段结构框。差异化提示：B班给标注好的范文只匹配段号；A班自己画结构+标注连接词。易错点提醒：最后一段必须有"It made me realize..."才算完整升华。' },
    { step: '三段结构讲透', time: '8', content: '【PPT P2 结构图】教师逐段讲解：P1 2句设定背景（when/where/who）→ P2 3-4句叙述经过（first/then/after that/finally）→ P3 2句写感受与意义（feelings + meaning）。教师示范写一段。预设回答跟读结构要点。板书时机：逐段板书模板句。差异化提示：B班给每段填空模板；A班给关键词自己写。易错点提醒：P3 的感受要具体 — 不要只说"I was happy"，要说"I felt grateful because my family was together."' },
    { step: '连接词+句型', time: '5', content: '【PPT P3 词表】教师领读时间连接词：First / Then / After that / Finally / At last。教师示例句：First, we made dumplings. Then, we had a big dinner. After that, we watched the gala. Finally, we set off fireworks. 预设回答跟读。板书时机：板书连接词于侧栏。差异化提示：B班选词填空；A班用全级连接词写一段。易错点提醒：after that 后接逗号 — "After that, we..." 不是 "After that we..."' },
    { step: '积语料', time: '5', content: '【PPT P4 语料库】教师：Build your word bank from this unit. Extract festival verbs, feeling words, and -ing patterns. 学生从本单元5课中提取：①节日动词（celebrate/gather/parade/decorate）②情感描写词（excited/joyful/grateful/moved）③-ing 结构模板（Celebrating together, we...）。板书时机：巡视。差异化提示：B班填词；A班造句。预设回答：按节日语料库分类卡填写词条。易错点提醒：同一意思用不同词替换避免重复——第一段说 happy，第三段说 joyful / grateful。' },
    { step: '提纲+起草', time: '10', content: '【PPT P5 写作提纲】选一次难忘的节日经历，写 80 词记叙文 outline（三段各写关键词）。教师巡视指导 outline。教师：Don\'t write sentences yet — just key words for each paragraph. 预设回答：P1: last Spring Festival / home / family / P2: make dumplings / dinner / fireworks / P3: grateful / family matters. 板书时机：留结构框供参考。差异化提示：B班用填空 outline；A班独立列提纲。易错点提醒：outline 不是草稿——用短语不是完整句。这是写前最重要的一步。' },
    { step: '互评提纲', time: '4', content: '【PPT P6 写作任务】同桌互换提纲，检查：三段都有吗？经过段有时间连接词吗？感受段有升华句吗？教师：Your partner\'s outline: does it have all 3 parts? 预设回答：Yes, but the feeling part is too short. 板书时机：留 checklist。差异化提示：B班用 checklist 表逐项打勾；A班口头给改进建议。易错点提醒：互评不是挑刺——给一个赞美+一个建议。"Good outline! Maybe add a feeling sentence in paragraph 3."' }
  ],
  blackboard: '┌─ U1 Writing: Festival Experience ──────┐\n│ P1 Background: Last..., at..., with... │\n│ P2 Process: First,... Then,... After   │\n│    that,... Finally,...                │\n│ P3 Feelings: I felt... It made me      │\n│    realize...                          │\n│                                         │\n│ Linkers: First / Then / After that     │\n│         Finally / At last              │\n│                                         │\n│ Word Bank: celebrate / gather / parade │\n│  excited / joyful / grateful / moved   │\n└─────────────────────────────────────────┘',
  exercises: '【基础作业】按课堂 outline 写完 80 词节日经历记叙文初稿。要求：三段结构完整、至少 2 个时间连接词、至少 1 个 -ing 结构。【提高作业】就同一节日写一则 30 词以内的社交媒体分享语（英文），要求有感染力有画面感。【参考答案——教师用】基础示例（节选）：I will never forget last Spring Festival. First, my family gathered to make dumplings. Then, we had a big dinner together. After that, we watched the Spring Festival gala. Finally, we set off fireworks at midnight. Celebrating together, I felt so grateful. It made me realize that family is the most important thing.',
  reflection: '✅ 亮点：三段结构框架让学生从"不知道写什么"变为"知道每段写什么"。⚠️ 需改进：时态混用仍需纠正，下节课用改错题强化。📌 下节课衔接：进入写作 II，互评修改+誊抄终稿。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u1-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '节日', '人教版必修三U1', '第七节课'],
  textbookAnalysis: '本课为必修第三册 Unit 1 第七课时（Writing II），在 Writing I 提纲+初稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进写作的能力——这是新课标强调的学习能力。互评量表聚焦三维度：结构完整（3段）、语言质量（连接词/-ing 结构/词汇）、语法准确（时态/三单/标点）。',
  overview: '【学情分析】A班：能辨别别人文章的好坏，但给反馈时只说"写得不错"缺乏具体点。B班：改自己的稿时不知从何下手。共同问题：互评流于表面，不会用检查量表逐项给分。',
  objectives: [
    '语言能力：能根据互评量表给同伴的节日记叙文初稿提具体、可操作的修改建议。',
    '文化意识：通过阅读同伴的节日经历了解不同家庭的文化传统。',
    '思维品质：在互评中培养"识别问题→提出方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步写作流程，内化为个人写作习惯。'
  ],
  keyPoints: '① 互评三维量表：结构（3段完整）+ 语言（连接词≥2 / -ing结构≥1 / 词汇多样性）+ 语法（时态/三单/标点） ② 改稿有侧重：先改结构再改语法 ③ 展示礼仪：大声/清晰/目视听众',
  difficulties: '① 学生互评时不好意思提缺点 — 需引导"给建议就是帮助对方进步"。② 时态混用重复出错——主体过去时，感受现在时。③ 修改时学生只改拼写不改结构 — 需强制"先查三段是否完整"。',
  teachingMethods: '① 量表互评：用统一标准减少主观性 ② 对子互评→修改→展示 ③ 最佳记叙文评选',
  preparation: '【PPT课件】P1 互评三维量表；P2 共性错误（时态混用/连接词缺/升华弱）；P3 修改指南；P4 展示礼仪；P5 最佳记叙文范例；P6 写作提纲回顾；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①结构（3段都给√/缺→标出）②语言（圈连接词≥2？-ing结构≥1？词汇重复？）③语法（时态？三单？标点？）。教师用上节课自己写的范文示范打分。预设回答跟学。板书时机：量表三维板书于黑板。差异化提示：B班按量表逐项打勾即可；A班还需写一句"最需要改进的地方"。易错点提醒：互评不是打分比高低——是帮对方变得更好。' },
    { step: '起草+互评', time: '12', content: '【PPT P2 共性错误】先展示上节课共性错：①时态混用②升华段缺"I felt..."③连接词缺。然后同桌互换初稿，用红笔按量表标注。教师巡视。教师：Give one praise and one suggestion. 预设回答：Your structure is good, but the tense is mixed. 板书时机：留量表供参考。差异化提示：B班按checklist勾；A班在稿上写具体修改建议。易错点提醒：提建议时用"I suggest..."而非"You should..."——更礼貌。' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改初稿。顺序：①先补结构（缺哪段补哪段）②再加语言（插入连接词/-ing结构）③最后查语法（时态统一）。教师：Don\'t just fix spelling — check structure first! 预设回答：I fixed the tense and added an -ing sentence in paragraph 2. 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色词汇替换。易错点提醒：修改不是重写——保留原文好的部分，只在薄弱处补强。' },
    { step: '展示评选', time: '8', content: '【PPT P4 展示礼仪】2-3 组自愿上台读记叙文。全班投票：最感人的经历/结构最完整的/最有画面感的。教师：Read loudly and look at the audience. 预设回答展示。板书时机：留展示评分维度。差异化提示：B班可看稿读；A班尽量脱稿。易错点提醒：上台读稿不要太快——你写了100词不等于听众能消化100词。' },
    { step: '结课', time: '5', content: '【PPT P7 总结】回顾写作闭环：outline→draft→peer review→revise→final。教师：Next time you write, remember this process. 预设回答：I will make an outline first. 板书时机：画闭环流程图。差异化提示：B班齐读流程；A班说自己的收获。易错点提醒：最好的写作习惯是"先结构后语言"——不要跳跃步骤。' }
  ],
  blackboard: '┌─ U1 Writing II: Peer Review ────────┐\n│ WRITING PROCESS:                      │\n│  Outline → Draft → Peer → Revise →   │\n│  → Final → SHARE                     │\n│                                       │\n│ Review Checklist:                     │\n│  ✅ 3 paragraphs?                     │\n│  ✅ ≥2 linkers?                       │\n│  ✅ ≥1 -ing structure?                │\n│  ✅ Feeling sentence?                 │\n│  ✅ Grammar (tense / 3rd p / ;)       │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改终稿，誊抄提交。自评：在稿末写 1 句"这次写作最大的进步是…" 【提高作业】调查另一个你不熟悉的节日，用"背景—经过—感受"框架写 80 词节日经历记叙文（可基于资料想象）。【参考答案——教师用】参考 Writing I 的 exercises 答案。终稿评估标准：结构3段完整（2分）+连接词≥2（2分）+-ing结构≥1（2分）+升华有力（2分）+语法准确（2分）= 10分。',
  reflection: '✅ 亮点：量表培训解决了"不知道评什么"的问题，B班互评质量明显提升。⚠️ 需改进：修改环节时间偏紧，下次可给15分钟。📌 下节课衔接：进入 Project，将本单元5课所学整合为节日文化展览。'
}));

// ====== Period 8: Project (节日文化展览) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u1-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '节日', '展览', '人教版必修三U1', '第八节课'],
  textbookAnalysis: '本课为必修第三册 Unit 1 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的节日词汇+阅读的"现象—本质"结构+语法的 -ing 形式+听与谈的策划句型+写作的记叙文——完成一份"节日文化展览"海报/展板。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确任务清单。B班：group work 中有同学"搭便车"不干活，需明确定人定责。共同问题：小组合作时语言切换回中文——需设立"英文监督员"角色。',
  objectives: [
    '语言能力：综合运用本单元词汇、-ing 形式、策划句型，以英文完成一份节日文化展览海报（标题/介绍/精神内核/活动/感悟）。',
    '文化意识：通过展览形式向同伴传播节日文化的多样性与共通精神。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 海报四模块：Festival Introduction（简介+时间）→ Spirit（精神内核）→ Activities（庆祝活动）→ Reflection（感悟） ② 单元知识整合：词汇/-ing 形式/策划句型/记叙文结构 ③ 小组分工：Writer / Designer / Editor / Presenter各司其职',
  difficulties: '① 小组分工时 Editor 常没事做 — 需明确所有角色都有事。提醒：editor不是"挑错"而是"润色语言"。② 海报语言过简（仅单词无句）— 要求每板块至少2句完整英文句。③ 展示时间控制 — 1.5分钟/组，超时扣分。',
  teachingMethods: '① PBL项目式学习：以展览为驱动问题 ② 小组协作：角色分工+checklist ③ 画廊漫步：全班互评',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 海报四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师带学生回顾本单元5课学了什么：听与说（节日词汇+描述）→阅读（现象本质+-ing）→语法（-ing定语状语）→听与谈（策划分工）→写作（节日记叙文）。教师：Today we put it all together! 预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出来。易错点提醒：每个版块至少用一次 -ing 结构——这是单元核心语法。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 海报结构】【PPT P3 角色卡】教师展示海报四模块：①Introduction（选一个节日+简介+时间）②Spirit（精神内核是什么）③Activities（怎么庆祝）④Reflection（你的感悟）。角色分工：Writer写文案 / Designer设计排版 / Editor检查语言+语法 / Presenter准备展示。教师：Choose your festival and role. 预设回答：We choose the Spring Festival. I am the writer. 板书时机：留模块结构和角色。差异化提示：B班给语言模板（填空式）；A班自由写。易错点提醒：Designer 也是团队一员——和 Writer 商量文案长度才能排出好看版。' },
    { step: '制作海报', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】小组制作。教师要巡视提醒：①用英文！②每模块至少2句完整句 ③至少1个 -ing 结构 ④最后5分钟 Editor 检查语言。预设回答：（小组讨论制作中，教师巡视指导）板书时机：无。差异化提示：B班给句子开头提示（The festival is... / It is about...）；A班独立完成。易错点提醒：不要把所有内容挤在一起——留白是设计的一部分。标题要大、内容要分块。' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】每组 1.5 分钟展示。全班投票：最佳内容/最佳设计/最佳展示。教师：You have 90 seconds. Go fast but clear! 预设回答展示。板书时机：记投票结果。差异化提示：B班可看海报读；A班脱稿补充。易错点提醒：1.5分钟很短——只讲最精彩的部分，不要逐字念。' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】学生勾选四维薄弱项：词汇记不住？-ing 形式不会用？策划句型忘了？写作结构不熟？写1条补强计划。教师：Be honest. This is for yourself, not for a grade. 预设回答：I need to practice -ing adverbials. I will review the grammar table tonight. 板书时机：留自评四维。差异化提示：B班中文写、A班英文写。易错点提醒：计划要具体到"做什么"+"什么时候"——不是"我会复习"，而是"今晚复习 -ing 规则并造5句"。' }
  ],
  blackboard: '┌─ U1 Project: Festival Exhibition ────┐\n│ 🎉 Poster 4 Modules:                   │\n│  ① Introduction (festival + time)      │\n│  ② Spirit (what is the core?)          │\n│  ③ Activities (how to celebrate?)      │\n│  ④ Reflection (your feeling)           │\n│                                        │\n│ 👥 Roles: Writer / Designer / Editor   │\n│          / Presenter                   │\n│                                        │\n│ ⭐ Must: English / ≥2 sentences per    │\n│         module / ≥1 -ing structure     │\n└────────────────────────────────────────┘',
  exercises: '【基础作业】完成小组海报（未完成的继续做），拍照片提交。写 30 词英文反思：我在小组中的贡献是…我从这个项目中学到了…【提高作业】选一个新闻中正在庆祝的外国节日，用英文写 50 词简报介绍时间+活动+精神。【参考答案——教师用】反思示例：My role was the writer. I wrote the introduction and the activities. I learned how to use -ing forms to describe festival scenes. What I can improve next time: check grammar before the deadline.',
  reflection: '✅ 亮点：海报四模块整合了全单元，学生产出有成就感。⚠️ 需改进：16分钟制作时间紧，下次可给20分钟。📌 下节课衔接：进入 Unit 2 Morals and Virtues，从节日文化转向道德抉择。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b3-u1-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b3-u1 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
