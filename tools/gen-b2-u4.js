/**
 * gen-b2-u4.js — 必修第二册 Unit 4 History and Traditions (8课时)
 * 
 * 语篇: WHAT'S IN A NAME? (UK history, the four countries)
 * 语法: 过去分词作宾语补足语 (have/get sth done; see/hear sth done)
 * 写作: Describe a Place That You Like (using sensory details)
 */

const fs = require('fs');
const path = require('path');

function esc(s) { return s.replace(/'/g, "\'").replace(/\n/g, '\\n'); }

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
const UNIT = 4;
const UNIT_TITLE = 'History and Traditions';
const BOOK = '必修第二册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u4-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '历史与传统', '英国', '地标', '人教版必修二U4', '第一节课'],
  textbookAnalysis: '本课为必修第二册 Unit 4 History and Traditions 第一课时（Listening and Speaking），属单元导入+输入环节。语篇为一段关于英国历史地标的对话与介绍，功能语境是"分享你对一个历史地标的了解"。语言重点为历史与传统词汇（ancient, tradition, landmark, historic, belong to, fascinating）及分享知识句型（Did you know that...? / I\'ve read that... / As far as I know...）。为 Reading 语篇"WHAT\'S IN A NAME?"中英国四国历史做词汇与话题预热。',
  overview: '【学情分析】A班：对英国有一定背景知识（London, Big Ben, Queen），但对苏格兰/威尔士/北爱尔兰了解少。B班：英国历史背景几乎为零，需地图+图片大量脚手架。共同问题：描述历史地标时只会说 old 和 beautiful，缺乏 historical/significant/fascinating 等高阶形容词。',
  objectives: [
    '语言能力：听懂关于英国历史地标的介绍，提取关键信息（名称/地点/历史意义），准确使用 8-10 个历史与传统相关词汇。',
    '文化意识：了解英国主要历史地标及其文化意义，形成对世界多元历史文化的尊重。',
    '思维品质：通过"听前预测—听中核实—听后比较"训练听力策略。',
    '学习能力：能用 Did you know that...? / As far as I know... 分享历史地标知识。'
  ],
  keyPoints: '① 历史与传统核心词汇：ancient / tradition / landmark / historic / belong to / fascinating / cultural / ancestor ② 分享知识句型：Did you know (that)...? / I\'ve read that... / As far as I know... ③ 听力微技能：听前看图片预测信息、听中抓地名+年代。',
  difficulties: '① historic（有历史意义的）vs historical（与历史相关的）——学生混淆。易错点提醒：historic 强调"有重大历史意义的"，historical 仅表示"与历史有关的"。② ancient /eɪnʃənt/ — c 不发音。③ landmark 拆开不是 land+mark 的字面意思而是"地标"。',
  teachingMethods: '① 任务型（TBL）：以介绍一处历史地标为终任务。② 听前预测+听中填表：信息卡脚手架。③ 对子互问操练分享句型。',
  preparation: '【PPT课件】P1 单元封面（History and Traditions）；P2 英国历史地标九宫格（巨石阵/伦敦塔/爱丁堡城堡/温莎城堡/巴斯罗马浴场/卡迪夫城堡/巨人堤道/威斯敏斯特教堂/牛津大学）；P3-4 听力任务题；P5 分享知识句型板；P6 说话任务卡。【实物教具】英国地图一张；历史地标信息卡 printed 每组一套。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine places. Which ones do you recognize? Which country of the UK is each in? 预设回答：Stonehenge is in England! Edinburgh Castle is in Scotland! 板书时机：右侧板书 ancient / landmark / historic。差异化提示：B班指图说国家名再跟读地标名；A班用 the one in... 说出地点（"The one in England is..."）。易错点提醒：the UK（联合王国）包含 4 个 countries: England / Scotland / Wales / Northern Ireland。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 ancient / tradition / landmark / historic / belong to / fascinating / cultural / ancestor。教师：What is the difference between "historic" and "historical"? 预设回答：Historic means very important in history. Historical just means related to history. 板书时机：左栏板书词+短注释。差异化提示：B班配图记忆+中英对照；A班用词造句并区分 historic vs historical。易错点提醒：fascinating /fæsɪneɪtɪŋ/ — 重音在第一音节，不是 /fæsɪneɪʃn/ (fascination)。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to an introduction about a UK landmark. Predict: What landmark? Where is it? How old is it? 预设回答：Maybe Stonehenge, in England, about 5,000 years old. 板书时机：预测信息写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测+理由。易错点提醒：听力常见陷阱——同一个 landmark 会先给猜测的年份再给确认的年份。"People thought it was 3,000 years old, but research shows it\'s actually over 4,500."' },
    { step: '听中填卡', time: '10', content: '【PPT P5 信息卡】【音频 段一】播放听力，学生填信息卡（名称/地点/年代/为什么重要/有趣事实）。教师：Why is this place important in British history? 预设回答：It is a symbol of ancient British culture. It belongs to all of Britain. 板书时机：核对答案时填表于黑板中部。差异化提示：B班听两遍只填名称+地点+年代；A班一遍填全+写有趣事实。易错点提醒：belong to（属于）没有被动语态！"It is belonged to..." 是错的，必须是 "It belongs to..."。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to share knowledge about history? Did you know (that)...? / I\'ve read that... / As far as I know... / It is said that... 教师示范后学生用听力信息造句。预设回答：Did you know that Stonehenge is over 4,500 years old? As far as I know, it was built as a temple. 板书时机：句型板书于中央。差异化提示：B班套用模板替换地标名；A班替换地标+追加2个有趣事实。易错点提醒：As far as I know（据我所知）— 不是 "As far as I know about" 或 "As my knowledge"。' },
    { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，从信息卡中选一处地标互相介绍。教师：Tell your partner about a landmark. Use at least one "Did you know...?" 预设回答：Did you know that Edinburgh Castle sits on an ancient volcano? It has been a royal residence for centuries! 板书时机：留句型供参考。差异化提示：B班用填空式对话卡；A班自由问答+用定语从句补充信息。易错点提醒：介绍地标时用一般现在时（除非说建造年代用过去时）——"The castle is on a hill" 不是 "was on a hill"。' }
  ],
  blackboard: '┌─ U4 Listening & Speaking ─────────────┐\n│ History & Traditions:                   │\n│  ancient / tradition / landmark         │\n│  historic / belong to / fascinating     │\n│  cultural / ancestor                    │\n│                                         │\n│ Sharing knowledge:                      │\n│  Did you know (that)...?               │\n│  I\'ve read that...                     │\n│  As far as I know...                   │\n│  It is said that...                    │\n│                                         │\n│ British Landmark Card: Stonehenge       │\n│  Location: England | Age: >4,500 yrs   │\n│  Significance: ancient temple/calendar │\n└─────────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有历史词汇。2. 用 Did you know...? / As far as I know... 各写 1 句关于一个历史地标的介绍。【提高作业】用英文写 50 词介绍一处你了解的中国历史地标（如故宫/长城/兵马俑），用至少 2 个分享知识句型。【参考答案——教师用】基础2示例：Did you know that the Great Wall is over 2,000 years old? / As far as I know, the Forbidden City has 9,999 rooms.',
  reflection: '✅ 亮点：九宫格+地图激活了学生的地理+历史双重背景知识。⚠️ 需改进：historic vs historical 区分仍困难，下节阅读中会反复出现以强化。📌 下节课衔接：进入阅读 WHAT\'S IN A NAME?，从地标延伸到英国四个国家的历史形成。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u4-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '英国历史', '四个国家', '人教版必修二U4', '第二节课'],
  textbookAnalysis: '本课为必修第二册 Unit 4 第二课时（Reading I），语篇 WHAT\'S IN A NAME? 是一篇历史文化说明文，解释"United Kingdom"这个名称背后的历史：四个国家（England/Scotland/Wales/Northern Ireland）如何在不同历史时期联合形成今天的 UK。结构为"名称困惑→逐国形成史→共同点与差异→现代意义"。语言重点为历史时间表达（in the 16th century / over the next few hundred years / finally）与联合/归属动词（join, be linked to, be added to, break away from）。',
  overview: '【学情分析】A班：有基本世界史知识但"UK vs GB vs England"这些概念的英文表述会混淆。B班：对英国历史完全陌生，需时间轴+地图大量脚手架。共同问题：英语中朝代/世纪的表达（the 16th century = 1500s）不习惯，容易算错。',
  objectives: [
    '语言能力：读懂历史文化说明文，提取 UK 四国形成的时间线与关键事件；掌握 8-10 个历史描述核心词汇。',
    '文化意识：理解 UK 的多元历史构成，体会"差异中的统一"这一文化主题。',
    '思维品质：通过时间轴+因果关系分析培养历史叙事阅读策略。',
    '学习能力：能用时间轴+四国关系图复述 UK 的形成过程。'
  ],
  keyPoints: '① 说明文结构：Name confusion → History of each country → Similarities & differences → Modern meaning ② 历史时间表达：in the 16th century / over the next few hundred years / finally / in the 20th century ③ 核心短语：be linked to / be added to / break away from / result in / belong to',
  difficulties: '① 世纪表达——the 16th century = 1501-1600，学生易以为 16th century = 1600s。原因：中文"十六世纪"对应 1500s，但英文同样规则。提醒：nth century = (n-1)00s。② be added to（被加入）vs join（主动加入）——语篇中用被动突出"被并入"的历史事实。③ break away from（脱离）— 不及物动词短语，后面直接接宾语。',
  teachingMethods: '① KWL 阅读法：已知→想知→学到的。② 时间轴+地图双脚手架：历史+地理同步构建。③ Jigsaw拼图：分组读不同国家后拼合全貌。',
  preparation: '【PPT课件】P1 UK 地图四色标注四国；P2 "UK vs GB vs England" 概念辨析图；P3 时间轴（从 10 世纪到 20 世纪）；P4 分段任务卡；P5 四国关系图；P6 词汇对比表；P7 总结回顾。【实物教具】UK 地图空白 work sheet 每人一份；时间轴空白工作单。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P2 概念辨析】教师：What\'s the difference between the UK, Great Britain, and England? Many people (even British people!) get confused. Let\'s find out! 预设回答：England is a country. The UK includes four countries? 板书时机：板书 UK / Great Britain / England 三圈 Venn 图。差异化提示：B班中文猜；A班英文猜+理由。易错点提醒：UK = United Kingdom of Great Britain and Northern Ireland（四个国家）。Great Britain = England + Scotland + Wales（三个，不含 Northern Ireland）。England ≠ UK！' },
    { step: '快速阅读抓主线', time: '8', content: '【PPT P3 时间轴】教师：Read fast (3 min). Find: ① When did Wales join England? ② When did Scotland join? ③ When did Ireland join? ④ When did Southern Ireland break away? 预设回答：① 16th century ② 18th century (1707) ③ 1801 ④ 20th century (1922). 板书时机：填时间轴四个关键点。差异化提示：B班给年份找对应事件（连线）；A班写完整句。易错点提醒：16th century = 1500s，但 Wales 是在 1500s 被正式并入（具体 1536/1543 年 Acts of Union）。' },
    { step: '精读段落1-2 名称困惑+Wales', time: '10', content: '【PPT P4 分段卡】教师精讲：be linked to / be added to。教师：Why does the title say "What\'s in a name?" What confusion is the author talking about? 预设回答：People confuse the UK, Great Britain, and England. The names have different meanings. 板书时机：左侧栏补 be linked to / be added to。差异化提示：B班读后填关键词；A班用自己话解释名称困惑。易错点提醒：莎士比亚戏剧《罗密欧与朱丽叶》中有 "What\'s in a name?" ——本文借用此句暗示名称背后有丰富历史。' },
    { step: '精读段落3-5 Scotland+Ireland', time: '10', content: '【PPT P5 四国关系图】教师：How was Scotland added? What happened to Ireland? 学生填表（国家/加入时间/方式）。教师：Why did Southern Ireland break away? 预设回答：Scotland was linked to England in 1603 (same king) and joined in 1707. Ireland was added in 1801, but the south broke away in 1922. 板书时机：右侧画四国关系演变箭头图。差异化提示：B班连线匹配（国家—时间—事件）；A班写完整原因+结果句。易错点提醒：break away from（脱离）= become independent from。Southern Ireland 脱离后成为 Republic of Ireland（独立国家），Northern Ireland 留在 UK。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 现代意义】教师：Why is it important to understand this history? What do the four countries share? What makes them different? 预设回答：They share a flag (Union Jack), currency, and military. But they have different flags, languages (Welsh, Gaelic), and sports teams. 板书时机：写 Shared vs Different 两栏。差异化提示：B班跟读关键词；A班用自己的话总结。易错点提醒：Welsh（威尔士的/威尔士语）— 不要和 wealth（财富）混淆，发音完全不同 /welʃ/ vs /welθ/。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾 UK 形成史时间轴+核心词汇+四国关系。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述时间轴。易错点提醒：UK 国旗 Union Jack 由三面旗帜叠加：England (St George\'s Cross) + Scotland (St Andrew\'s Cross) + Ireland (St Patrick\'s Cross)。Wales 的龙旗不在上面。' }
  ],
  blackboard: '┌─ U4 Reading I: WHAT\'S IN A NAME? ──────────┐\n│ UK Formation Timeline:                       │\n│  16th c → Wales linked to England            │\n│  18th c (1707) → Scotland joined → GB        │\n│  1801 → Ireland added → UK                   │\n│  1922 → Southern Ireland broke away          │\n│  → Today: UK = Eng+Sco+Wal+NI               │\n│                                               │\n│ be linked to / be added to / break away from │\n│ result in / belong to                         │\n│                                               │\n│ UK ≠ Great Britain ≠ England!                │\n└───────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-4段 2 遍，圈出所有时间表达。2. 用时间轴上的4个关键年份各写1句 UK 历史事件。【提高作业】用 80 词写一段：Choose one of the four countries and introduce its unique tradition or symbol.（用 be linked to / belong to / however）【参考答案——教师用】基础2示例：In the 16th century, Wales was linked to England. / In 1707, Scotland was joined with England and Wales to form Great Britain.',
  reflection: '✅ 亮点：时间轴+地图双脚手架让抽象历史变具体，B班参与率高。⚠️ 需改进：世纪表达（16th century = 1500s）仍有学生算错，精读课将强化。📌 下节课衔接：进入精读语言+过去分词作宾语补足语在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u4-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '过去分词', '英国历史', '人教版必修二U4', '第三节课'],
  textbookAnalysis: '本课为必修第二册 Unit 4 第三课时（Reading II），聚焦语篇 WHAT\'S IN A NAME? 的精读与语言分析。重点分析文中过去分词作宾语补足语的用法——如 "They had castles built" "People saw the country linked to England"——在历史说明文中的功能：描述"使某事被做"或"看到/听到某事被做"的结果状态。同时深化语篇中高频动词的用法辨析（join / link / add / break / result / belong）。',
  overview: '【学情分析】A班：已掌握过去分词作定语和表语，但作宾语补足语（have/get sth done）是全新用法。B班：过去分词概念模糊，需大量例句感知"done"作补足语的功能。共同问题：翻译成中文时"have sth done"容易和 have done（完成时）混淆。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 4 个过去分词作宾语补足语的句子，理解"have/get sth done"的"使某事被做"语义。',
    '文化意识：通过过去分词补足语体会英语如何表达"动作的结果状态"——不同于中文的"把字句"。',
    '思维品质：分析过去分词作宾语补足语在历史文本中的功能——描述历史事件的完成状态。',
    '学习能力：建立"从读到写"的语料库——积累课文中的过去分词补足语句型用于后续地点描写写作。'
  ],
  keyPoints: '① 过去分词作宾语补足语结构：have/get + O + V-ed（使某事被做）；see/hear + O + V-ed（看到/听到某事被做）② 语篇中补足语句的识别与功能分析 ③ 核心动词辨析：join / link / add / break / result / belong / defend',
  difficulties: '① have sth done（使某事被做）vs have done（完成时）——学生看到 have + V-ed 第一反应是完成时。原因：表层结构相同，深层结构不同。② see sth done（看到某事被做）vs see sb do（看到全过程）vs see sb doing（看到正在做）——三个结构语义不同。③ result in（导致）vs result from（由…导致）——方向相反。',
  teachingMethods: '① 标注发现法：圈出文中所有过去分词作宾补的句子并分析结构。② 对比辨析：have done vs have sth done。③ 语料卡记录：分类摘录优质句子。',
  preparation: '【PPT课件】P1-2 课文中圈出的过去分词作宾补示例；P3 结构分解公式；P4 have done vs have sth done 对比；P5 语料卡模板；P6 词汇辨析表；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 时间轴回顾】教师：Last class we learned how the UK was formed. Can you recall the four key events on the timeline? 预设回答：Wales linked, Scotland joined, Ireland added, Southern Ireland broke away. 板书时机：左栏写时间轴关键词。差异化提示：B班看时间轴读关键词；A班完整复述四事件。易错点提醒：added 是 add 的过去分词——"Ireland was added"（被动）表示爱尔兰是被并入的，不是自愿加入的。' },
    { step: '过去分词作宾补发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle sentences where a past participle (V-ed) follows an object. 学生标记后全班核对：①They had castles built. ②They saw the country linked. ③They got the kingdom united. 教师：What does "had castles built" mean? 预设回答：They caused castles to be built by someone. 板书时机：逐句板书，标注 O + V-ed。差异化提示：B班给划线句直接圈 O+V-ed；A班自己找+解释语义。易错点提醒：had castles built ≠ 自己建城堡。是"使/让城堡被建造"——通常是让别人建的。' },
    { step: 'have sth done 讲透', time: '10', content: '【PPT P3 结构公式】教师板书：have/get + O + V-ed。对比：①Kings built castles.（主动，国王自己建）②Kings have built castles.（现在完成时，国王已建完）③Kings had castles built.（过去分词作宾补，国王让人建）。教师：Which sentence means the kings didn\'t do the building themselves? 预设回答：Sentence ③ — "had castles built" means they ordered or arranged for it to be done. 板书时机：三句对比板书。差异化提示：B班填空（had + O + ___）；A班独立造句。易错点提醒：have sth done 的 have 可以有时态变化 —— had（过去）/ will have（将来）/ have had（完成）sth done。' },
    { step: '语料库搭建', time: '10', content: '【PPT P5 语料库模板】学生分类填语料卡：①过去分词作宾补句摘录（至少3句）②历史动词（join/link/add/break/result/belong/defend）③世纪/年代表达。板书时机：巡视指导。差异化提示：B班填词+翻译；A班造句+标注"此句可用于地点描写"。预设回答：按历史与传统语料库模板分类填写词条。易错点提醒：result in（导致= lead to）≠ result from（由…导致 = be caused by）。"The war resulted in many deaths" vs "Many deaths resulted from the war"。' },
    { step: '句型转换', time: '5', content: '【PPT P6 练习】教师给句子，学生改写：The king ordered people to build a wall. → The king had a wall built. / I saw that the flag was raised. → I saw the flag raised. 预设回答造句。板书时机：板书转换公式。差异化提示：B班跟做每一步；A班独立完成+给转换后的句子造句境。易错点提醒：see/hear + O + V-ed 强调"动作的结果"——"I saw the flag raised"（看到旗已升起）≠ "I saw the flag being raised"（看到旗正在被升起）。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】回顾 have/get sth done + see/hear sth done + 语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课系统讲练过去分词作宾语补足语。' }
  ],
  blackboard: '┌─ U4 Reading II: Language Focus ───────────┐\n│ Past Participle as Object Complement:      │\n│  have/get + O + V-ed  (使…被做)           │\n│  see/hear + O + V-ed (看到/听到…被做)    │\n│                                            │\n│  Kings built castles. (they did it)        │\n│  Kings have built castles. (completed now) │\n│  Kings had castles built. (arranged it!)   │\n│                                            │\n│ Text examples:                             │\n│  "They had castles built around the coast."│\n│  "People saw the country linked to..."     │\n│  "They got the kingdom united."            │\n└────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出3个过去分词作宾补的句子并标注结构。2. 改写：The queen ordered workers to paint the palace. → The queen had...【提高作业】用 have/get sth done 写 3 句关于你（或你认识的人）的生活（如理发/修手机/拍照）。【参考答案——教师用】基础2示例：The queen had the palace painted.',
  reflection: '✅ 亮点：have done vs have sth done 三句对比让学生直观感受区别。⚠️ 需改进：see sth done 的用法仍需强化，语法课将系统操练。📌 下节课衔接：进入语法课，系统操练过去分词作宾语补足语。'
}));

// ====== Period 4: Grammar (过去分词作宾语补足语) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u4-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '过去分词', '宾补', '英国历史', '人教版必修二U4', '第四节课'],
  textbookAnalysis: '本课为必修第二册 Unit 4 第四课时（Discovering Useful Structures），系统教学过去分词作宾语补足语（have/get sth done; see/hear/find/feel sth done; make oneself understood 等）。基于 Reading 语篇中提取的例句，引导学生归纳出"何时用过去分词作宾补"的规则——宾语是动作的承受者且强调结果状态。通过历史与日常生活主题的语境化练习巩固语法，为后续地点描写写作做语言准备。',
  overview: '【学情分析】A班：能理解 have sth done 的概念，但 see/hear sth done 与 see/hear sb doing 易混淆。B班：过去分词本身不熟+宾补概念模糊=双重困难。共同问题：写作中几乎不主动使用过去分词作宾补——习惯用从句代替（"I had someone repair my phone" 而非 "I had my phone repaired"）。',
  objectives: [
    '语言能力：准确使用过去分词作宾语补足语，在历史与日常话题中产出 5 个以上正确句子。',
    '文化意识：通过 have sth done 理解英语中"委托/使役"的文化表达习惯。',
    '思维品质：通过"发现例句→归纳规则→对比辨析→应用输出"的归纳法培养语法学习策略。',
    '学习能力：建立"宾补自查表"——写作后自行检查宾语与补足语的逻辑关系是否正确。'
  ],
  keyPoints: '① 过去分词作宾补的核心结构：V + O + V-ed（宾语是动作的承受者）② 常用动词：have / get / see / hear / find / feel / make ③ 与现在分词作宾补的区别：V-ed（被动/完成）vs V-ing（主动/进行）④ 不规则过去分词复习（build→built, make→made, write→written, speak→spoken）',
  difficulties: '① have sth done vs have sb do（让某人做）— 学生混淆宾语是人还是物。原因：中文都用"让/使"。② see sth done（看到被做）vs see sb doing（看到正在做）vs see sb do（看到全过程）——三种宾补语义不同。③ make oneself understood（使自己被理解）— 固定搭配。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习。② 场景造句：给生活场景图片用宾补描述。③ 改错竞赛。',
  preparation: '【PPT课件】P1 过去分词作宾补公式分解；P2 课文例句摘录；P3 V-ed vs V-ing 做宾补对比表；P4 生活场景图片（理发/修车/拍照/装修）；P5 情境造句卡；P6 改错题；P7 总结。【实物教具】场景图片卡一套；改错卡每人一套。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中3个句子+新给3个：①The king had a wall built. ②I saw the flag raised. ③She found her bag stolen. ④He got his hair cut. ⑤We heard our names called. ⑥She made herself understood. 学生圈 O + V-ed。教师：What is the relationship between the object and the past participle? 预设回答：The object receives the action. The wall was built. The flag was raised. 板书时机：左栏板书6句，圈 O + V-ed。差异化提示：B班只圈 V-ed；A班分析"宾语是动作的发出者还是承受者"。易错点提醒：宾语补足语的关键逻辑——宾语是 V-ed 这个动作的承受者。如果不是，不能用过去分词！' },
    { step: '规则归纳', time: '10', content: '【PPT P3 对比表】教师对比两种宾补：①V-ing（宾语发出动作，主动）：I saw him running.（他在跑）②V-ed（宾语承受动作，被动）：I saw him caught by the police.（他被抓）。教师：How to decide V-ing or V-ed? 预设回答：If the object does the action → V-ing. If the object receives the action → V-ed. 板书时机：双栏对比板书。差异化提示：B班填已给表格（动词/结构/宾语是施事还是受事）；A班自己画表+各造2句。易错点提醒：判断公式——在宾语后加"被"字。如果通顺→用 V-ed。"I saw him（被）running"不通→用 running。"I had my car（被）wash"通→用 washed。' },
    { step: '生活场景操练', time: '8', content: '【PPT P5 图片卡】展示4张图（理发/修手机/拍照/装修房间），学生用 have/get sth done 描述。教师：What is happening in this picture? Use "have/get sth done"! 预设回答：He is having his hair cut. / She got her phone repaired. / They had their photo taken. / We are having our room painted. 板书时机：巡视指导。差异化提示：B班给动词提示（cut/repair/take/paint）；A班不给提示自由造句+说时态。易错点提醒：have sth done 可以有时态变化——is having（正在）/ had（已经）/ will have（将要）/ has had（已完成）。' },
    { step: 'make oneself done 固定搭配', time: '6', content: '【PPT P6 固定搭配卡】教师介绍特殊搭配：make oneself understood（使别人理解自己）/ heard（使别人听见自己）/ known（使自己出名）。教师：If you go to France and don\'t speak French, how can you make yourself understood? 预设回答：I can use gestures. I can use a translation app. 板书时机：板书三个固定搭配。差异化提示：B班背搭配+造句；A班翻译成中文并体会"让自己被..."的含义。易错点提醒：make oneself understood ≠ 自己理解自己。是自己"被（别人）"理解。' },
    { step: '改错巩固', time: '6', content: '【PPT P7 改错】展示 4 个典型错误：①I had my room cleaning.（应用 cleaned）②She saw the boy caught the ball.（the boy caught 应用 catching — 男孩主动接球）③He got his report writing.（应用 written）④We heard the song sang.（应用 sung）。学生纠错并解释。预设回答纠错。板书时机：板书错误→改正+规则。差异化提示：B班判对错；A班解释为什么错。易错点提醒：不规则过去分词最常见错误——sing→sang→sung（过去分词是 sung 不是 sang）。' },
    { step: '小结', time: '3', content: '【PPT P8 总结】回顾 have/get + O + V-ed + see/hear + O + V-ed + 与 V-ing 的区别 + 固定搭配。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班说出3条规则。易错点提醒：自查——宾语是动作的承受者吗？如果是→V-ed；如果不是→用 V-ing 或 do。' }
  ],
  blackboard: '┌─ U4 Grammar: Past Participle as OC ────────┐\n│  V + Object + V-ed (宾语承受动作)          │\n│                                             │\n│  have/get + O + V-ed (使…被做)             │\n│    I had my hair cut. (别人给我剪的)        │\n│  see/hear + O + V-ed (看到/听到…被做)      │\n│    I saw the flag raised. (旗已被升起)      │\n│  make + oneself + V-ed                      │\n│    make oneself understood (使自己被理解)   │\n│                                             │\n│  V-ed (被动/完成) vs V-ing (主动/进行)      │\n│  saw him caught (他被抓) vs saw him running │\n│                                             │\n│  ❌ had my room cleaning → ✓ cleaned        │\n│  ❌ heard the song sang → ✓ sung            │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 用 have/get sth done 造 5 句。2. 改错：I had my bike repairing. / She saw the bird flew away. / We heard the window breaking.【提高作业】写 60 词短文描述你理想中的一天（从早到晚，至少用 3 个 have/get sth done）。【参考答案——教师用】基础1示例：I had my phone screen replaced yesterday. / She gets her nails done every two weeks.',
  reflection: '✅ 亮点：生活场景图片让 have sth done 立即能用在生活中。⚠️ 需改进：V-ed vs V-ing 选择仍需要更多辨析练习。📌 下节课衔接：听与谈聚焦英国传统与节日，口头运用宾补结构描述传统活动。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u4-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '英国传统', '节日', '历史', '人教版必修二U4', '第五节课'],
  textbookAnalysis: '本课为必修第二册 Unit 4 第五课时（Listening and Talking），语境为"讨论英国传统与节日"。听力材料为一段关于英国传统节日与习俗的对话，口语输出任务为介绍一个中国传统节日并比较中英文化异同。功能语言为表达惊讶与兴趣（Really? / That\'s interesting! / I didn\'t know that! / Tell me more!）及比较句型（Similarly,... / In contrast,... / While...,...）。结合语法课的过去分词作宾补，在口语中自然运用如"I\'ve seen this festival celebrated"等结构。',
  overview: '【学情分析】A班：能说出中国主要节日英文名，但描述习俗的英文词汇有限。B班：对中国节日习俗的英文表达几乎空白。共同问题：介绍节日时只列活动不解释文化意义。',
  objectives: [
    '语言能力：听懂关于英国传统节日的对话，提取节日名称/日期/习俗/意义；能用英文介绍一个中国传统节日并比较中英异同。',
    '文化意识：通过中英节日比较体会文化多样性，增强本土文化自信。',
    '思维品质：在比较中练习"找出相似→指出差异→解释原因"的三步比较思维。',
    '学习能力：通过比较对话训练双向文化视角——既看别人也反思自己。'
  ],
  keyPoints: '① 节日词汇：celebration / custom / tradition / originate from / symbolise / mark ② 表达惊讶/兴趣：Really? / That\'s fascinating! / I didn\'t know that! / Tell me more about... ③ 比较句型：Similarly,... / In contrast,... / While...,... / Both... share...',
  difficulties: '① originate from（起源于）— 学生易少写 from。② celebrate /selɪbreɪt/ 发音 — 重音在第一音节，不是 /səlebreɪt/。③ 比较时只列相同不说不同、或反之——需训练"相同+不同+原因"的完整比较。',
  teachingMethods: '① 听前预测→听中配对→听后产出。② Think-Pair-Share：先自己想中英节日比较→同桌讨论→全班分享。③ 文化大使角色扮演：向外国朋友介绍中国节日。',
  preparation: '【PPT课件】P1 英国节日图片（Bonfire Night / St Patrick\'s Day / Burns Night / Pancake Day）；P2 表达兴趣句型板；P3 听力任务题；P4 听力任务卡；P5 比较句型板；P6 角色卡。【实物教具】节日信息卡 printed；角色卡（中国学生/英国朋友）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 英国节日图片】教师：Look at these festivals. Have you heard of any of them? What Chinese festivals do you know? 预设回答：Spring Festival, Mid-Autumn Festival, Dragon Boat Festival! 板书时机：左栏板书 celebration / custom / tradition / originate from。差异化提示：B班中文说再翻英文；A班用英文说出至少一个节日的习俗。易错点提醒：Dragon Boat Festival — 不要说成 "Dragon Festival" 或 "Boat Festival"，三个词一个不能少。' },
    { step: '听力抓信息', time: '10', content: '【PPT P3 听力任务】听对话，抓"什么节日/什么时候/什么习俗/什么意义"。教师：Listen for: festival name / date / what people do / what it celebrates. 预设回答：Bonfire Night is on November 5. People have bonfires and fireworks. It marks the failure of the Gunpowder Plot. 板书时机：配对填表（节日|日期|习俗|意义）。差异化提示：B班给配对连线题；A班听写关键词+写完整信息句。易错点提醒：mark（标志/纪念）作动词——"the festival marks..." 不常见但很地道。' },
    { step: '听中录回应', time: '8', content: '【PPT P4 任务卡】【音频】重听，注意对话中的回应句："Really?" "That\'s fascinating!" "I didn\'t know that!" 教师：How does the listener show interest? 预设回答：By asking follow-up questions — "Tell me more!" / "Why do they do that?" 板书时机：板书回应句型。差异化提示：B班听出回应句勾选；A班记录并分析"哪种回应最能让对方继续讲"。易错点提醒：表达兴趣不只是说 "Oh" 或 "Interesting"——最能鼓励对方的是追问 "Tell me more about..."。' },
    { step: '句型操练+比较', time: '7', content: '【PPT P5 比较句型】教师带领操练中英节日比较：Spring Festival vs Christmas — Similarly, both are family reunions. In contrast, Spring Festival lasts 15 days while Christmas is mainly one day. 教师：Compare a British and Chinese festival with your partner. 预设回答：Mid-Autumn Festival and Thanksgiving — Similarly, both celebrate harvest. In contrast, Mid-Autumn Festival is about the moon. 板书时机：板书比较句型。差异化提示：B班用填空式比较框架；A班自主比较+说原因。易错点提醒：While 表对比时放在句首或句中——"While Christmas is in winter, Spring Festival is also in winter."（相似比较用 while 不太合适，应用 Similarly）。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】两人一组：Chinese Student 和 British Friend。英国朋友问"What\'s your favourite Chinese festival?"，中国学生介绍+比较。教师巡视。预设回答：My favourite is the Dragon Boat Festival. It originates from a poet named Qu Yuan. Similarly to your Remembrance Day, we honour a historical figure. 板书时机：留句型供参考。差异化提示：B班照卡读；A班脱稿加即兴互动。易错点提醒：介绍中国节日时，如果习俗没有英文对应词，用简单英文描述即可——"zongzi = sticky rice wrapped in bamboo leaves"。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾节日词汇+表达兴趣句型+比较句型。教师：Remember: When comparing, say what\'s similar AND what\'s different. 预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一个中英节日异同。易错点提醒：比较的本意不是判断好坏——不要说"ours is better"，说"they are different because..."。' }
  ],
  blackboard: '┌─ U4 Listening & Talking ────────────────┐\n│ Festivals:                                │\n│  celebration / custom / tradition         │\n│  originate from / symbolise / mark        │\n│                                           │\n│ Showing interest:                         │\n│  Really? / That\'s fascinating!            │\n│  I didn\'t know that! / Tell me more!      │\n│                                           │\n│ Comparing:                                │\n│  Similarly, both... share...              │\n│  In contrast, ... while ...               │\n│  Unlike..., ...                            │\n└───────────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有节日词汇。2. 用比较句型写 3 句比较一个中国节日和一个英国节日。【提高作业】写 60 词对话：向一位外国朋友介绍端午节（或你最喜欢的节日），含至少 1 次兴趣回应和 1 个比较。【参考答案——教师用】基础2示例：Similarly, both the Spring Festival and Christmas are times for family reunion. / In contrast, the Dragon Boat Festival involves racing, while Thanksgiving is more about eating.',
  reflection: '✅ 亮点：文化大使角色扮演让学生有真实交流目的，开口率很高。⚠️ 需改进：originate from 的 from 遗漏率高，写作课需强化。📌 下节课衔接：进入写作 I，将从比较转向用感官细节描述一个喜欢的地方。'
}));

// ====== Period 6: Writing I (感官描写+结构) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u4-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '感官描写', '地点描写', '英国', '人教版必修二U4', '第六节课'],
  textbookAnalysis: '本课为必修第二册 Unit 4 第六课时（Reading for Writing I），写作体裁为用感官细节描述一个你喜欢的地方（Describe a Place That You Like）。结构为：引人入胜的开头→视觉描写→听觉/嗅觉/触觉描写→历史/文化背景→个人感受与结尾。语言重点为感官动词（see, hear, smell, feel, taste）与形容词（magnificent, peaceful, ancient, breathtaking, charming）。结合本单元 Reading 的历史叙事与语法课的过去分词作宾补，实现"读-语法-写"闭环。',
  overview: '【学情分析】A班：能写简单的地点描述，但只用视觉缺少其他感官。B班：句型储备少，描述地点时只会说 beautiful, big, old 三个词。共同问题：地点描写变成"导游词"——只列事实（建于XX年/有XX米高）而没有个人感受和感官体验。',
  objectives: [
    '语言能力：掌握感官描写的"五感+感受"框架，在历史地点话题中产出 80-100 词感官丰富、有个人情感的地点描写文。',
    '文化意识：通过用英文描写中国/世界历史文化地点，向世界讲述本土故事。',
    '思维品质：通过"选感官细节→组织描写顺序→融入个人感受"训练从感知到文字表达的转化思维。',
    '学习能力：建立"五感 checklist"——写作前问自己：读者能"看到、听到、闻到、感觉到"这个地方吗？'
  ],
  keyPoints: '① 地点描写结构：Opening Hook → Visual description → Other senses (sound/smell/touch) → History/Culture → Personal feelings ② 感官表达：I can see... / The air smells of... / I can hear... echoing... / The stone feels... ③ 过去分词作宾补在地点描写中的应用：I\'ve seen the temple restored. / You can have your photo taken here.',
  difficulties: '① 嗅觉/触觉描写的英文表达——学生词汇储备几乎为零（musty / crisp / damp / rough / smooth）。② 感官描写的顺序——不能东一句西一句，要有空间顺序（由远及近/由下到上/由外到内）。③ 个人感受不能只写"I like it"——要具体说明为什么。',
  teachingMethods: '① 范本解构法：读优秀地点描写→提取五感词→仿写。② 五感头脑风暴：选一个地点，用五感思维导图积累词汇。③ 过程写作：outline→draft→peer review。',
  preparation: '【PPT课件】P1 优秀地点描写范例（如描述爱丁堡城堡的段落）；P2 五感+感受结构图；P3 五感词汇库；P4 五感头脑风暴工作单；P5 写作任务；P6 写作提纲；P7 总结。【实物教具】五感思维导图 work sheet 每人一份；五感词汇卡每组一套。',
  process: [
    { step: '范本解构', time: '8', content: '【PPT P1 地点描写范例】教师展示一段描述爱丁堡城堡的范文，学生标注五感：视觉（ancient stone walls, misty skyline）/ 听觉（bagpipes echoing, wind howling）/ 嗅觉（damp stone, fresh Scottish air）/ 触觉（rough walls, cold wind）/ 感受（It feels like stepping back 500 years.）。教师：How many senses can you find? 预设回答：Sight, sound, smell, touch — and the writer\'s feelings. 板书时机：五感五列板书。差异化提示：B班给标注好的范文只圈感官词；A班自己标注+评语哪个感官最有效。易错点提醒：感官描写的秘诀——用具体而不是笼统的形容词。不说 "good smell"，说 "the sweet smell of freshly baked bread"。"Good" kills writing.' },
    { step: '五感词汇库', time: '8', content: '【PPT P3 词汇库】教师分类提供五感词汇：Sight（magnificent/ancient/crumbling/towering/gleaming）Sound（echo/roar/whisper/chime/bustling）Smell（musty/fragrant/crisp/smoky/damp）Touch（rough/smooth/chilly/worn/polished）Feeling（awe-struck/peaceful/nostalgic/humbled/inspired）。教师领读+示例句。预设回答跟读+标记自己最想用的词。板书时机：五列词汇板书。差异化提示：B班每类选3个词背；A班每类选1个词造一段。易错点提醒：musty（霉味的）≠ dusty（有灰尘的）— 老建筑常有 musty smell，不是 dirty 而是"古老的味道"。' },
    { step: '结构讲透', time: '5', content: '【PPT P2 结构图】教师讲五段结构：①Opening Hook — 让读者想去这个地方（"If you want to feel history alive, visit..."）②Visual — 你看到的第一印象 ③Other senses — 至少再写一种感觉（声音/气味/触感）④History/Culture — 1-2句背景（可用过去分词作宾补："I\'ve seen this place restored to its former glory."）⑤Personal feeling — 这个地方对你的意义。预设回答跟做结构笔记。板书时机：五段结构板书。差异化提示：B班给每段填空模板；A班给关键词自己写。易错点提醒：⑤个人感受是最重要的——没有感受的地点描写只是维基百科，不是好文章。' },
    { step: '五感头脑风暴+提纲', time: '7', content: '【PPT P4 工作单】学生各自选一个喜欢的地方（当地/中国/世界均可），画五感思维导图：看到什么/听到什么/闻到什么/摸到什么/感觉如何。教师巡视建议：Try to include at least THREE senses. 预设回答：For the Great Wall: sight (snaking along mountains), touch (rough ancient bricks), sound (wind whistling), feeling (awe at human achievement). 板书时机：巡视指导。差异化提示：B班给每感1个提示词；A班独立完成所有五感。易错点提醒：选你真正去过的地方——虚拟的地点写不出真实感官细节，读者一眼就能看出。' },
    { step: '起草+同伴初评', time: '10', content: '【PPT P5 写作任务】学生写 80-100 词地点描写初稿。要求：五段结构、至少包含3种感官、至少1个过去分词作宾补、有个人感受。教师巡视。写完同桌互换check：感官≥3？结构完整？有个人感受？有过去分词作宾补？预设回答：（学生写作+互评中）板书时机：留结构+词汇供参考。差异化提示：B班用模板框架填写；A班自由写+追求文学性。易错点提醒：感官描写不要堆砌——选最有特色的2-3个感官深度描写，比五种全写但每种只有2个词好得多。' },
    { step: '同伴初评', time: '2', content: '【PPT P6 写作提纲】同桌互换，用五感 checklist 互查。教师：Can you "see" this place when you read it? Which sense is missing? 预设回答：I can see it clearly but I want to hear something too — maybe add a sound. 板书时机：留checklist。差异化提示：B班用 checklist 逐项打勾；A班写"最打动我的句子"和"再加一种感官的建议"。易错点提醒：互评时闭上眼睛听对方读——如果能"看到"那个地方，说明描写成功了。' }
  ],
  blackboard: '┌─ U4 Writing: Describe a Place ────────────────┐\n│  ① Hook (make reader want to go)               │\n│  ② Visual (what you SEE — be specific!)        │\n│  ③ Other Senses (sound/smell/touch — ≥1 more) │\n│  ④ History/Culture (1-2 sentences)             │\n│  ⑤ Personal Feeling (what it means to YOU)     │\n│                                                 │\n│  Five Senses Word Bank:                         │\n│  👁️ magnificent / ancient / towering / gleaming │\n│  👂 echo / roar / whisper / chime / bustling    │\n│  👃 musty / fragrant / crisp / smoky / damp     │\n│  ✋ rough / smooth / chilly / worn / polished    │\n│  ❤️ awe-struck / peaceful / nostalgic / humbled │\n└─────────────────────────────────────────────────┘',
  exercises: '【基础作业】按课堂初稿完成 80-100 词地点描写。要求：五段结构、≥3 种感官、≥1 个过去分词作宾补、有真实个人感受。【提高作业】用手机拍一张你描写的地点的照片，将照片+英文描写文案做成一张明信片（手绘或数字均可）。【参考答案——教师用】示例（故宫节选）："If you want to feel the weight of 600 years under your feet, visit the Forbidden City. I can see the golden roofs gleaming in the afternoon sun. The air smells of ancient wood and incense. I run my hand over the weathered stone — it feels cold, as if the past is still holding on..."',
  reflection: '✅ 亮点：五感词汇库解决了"只会说beautiful"的瓶颈。⚠️ 需改进：部分学生只写视觉，需在下节课互评中强制检查"是否有第二种感官"。📌 下节课衔接：进入写作 II，互评修改+地点描写展示分享。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u4-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '感官描写', '英国历史', '人教版必修二U4', '第七节课'],
  textbookAnalysis: '本课为必修第二册 Unit 4 第七课时（Writing II），在 Writing I 地点描写初稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进感官描写的丰富度和感染力。互评量表聚焦三维度：感官丰富（≥3种感官且具体）、结构完整（五段+有Hook+有个人感受）、语言质量（过去分词作宾补/感官词汇多样/语法准确）。',
  overview: '【学情分析】A班：能辨别感官描写好坏，但给反馈时只说"写得美"而缺乏"哪个感官最打动人"的具体分析。B班：改自己的描写时不知如何"再加一种感官"。共同问题：互评时只读不改——不会在别人的稿子上标"这里可以加一种声音/气味"。',
  objectives: [
    '语言能力：能根据互评量表给同伴的地点描写提具体、可操作的修改建议，重点检查感官丰富度和语言多样性。',
    '文化意识：通过阅读同伴的地点描写了解世界各地不同的历史文化地点。',
    '思维品质：在互评中培养"识别感官空白→提出补充方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步写作流程，内化为个人写作习惯。'
  ],
  keyPoints: '① 互评三维量表：感官（≥3种且描写具体 / 有没有一种感官特别打动人）+ 结构（五段完整 / Hook有力 / 个人感受真实）+ 语言（宾补≥1 / 感官词汇多样 / 语法准确）② 修改策略：先加感官再修语言',
  difficulties: '① 学生互评时不好意思说"感官不够"——需示范"I want to HEAR this place too"的表达方式。② 修改时不知如何加气味/声音——需重新激活五感词汇库。③ 展示时读得太快——地点描写需要让听众"想象"出来，语速要慢。',
  teachingMethods: '① 量表互评：用统一标准减少主观性。② 感官补充工作坊：专门加一种新感官。③ 闭眼听读展示。',
  preparation: '【PPT课件】P1 互评三维量表；P2 常见问题（只有视觉/无Hook/无个人感受/无宾补）；P3 修改指南；P4 展示技巧（慢读+想象）；P5 最佳地点描写范例；P6 自评表；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①感官（≥3种？描写具体还是笼统？最打动你的是哪种感官？）②结构（五段全？Hook抓人？个人感受真实？）③语言（宾补≥1？感官词汇多样？语法准确？）。教师用上节课自己写的地点评分示范。预设回答跟学。板书时机：量表三维板书。差异化提示：B班按量表逐项打勾；A班还需评"如果这是旅游宣传文案，你会想去吗？" 易错点提醒：互评时最有用的问题是——"闭上眼，你能\'到\'那个地方吗？如果缺了什么感觉，那就是作者需要加的。"' },
    { step: '互评+感官补充', time: '12', content: '【PPT P2 常见问题】先展示上节课常见问题：①只有视觉 ②Hook是"I want to introduce..." ③个人感受是"I like it very much"（太空泛）④无过去分词作宾补。同桌互换初稿，用红笔标注感官空白处+写"这里加点声音/气味"。教师：Find one place where your partner can add a new sense. 预设回答：I marked "smell" — the writer describes a temple but doesn\'t tell us what it smells like. 板书时机：留量表供参考。差异化提示：B班用 checklist 勾+写"加声音/气味/触感"提示；A班还写一句"如果是我，我会加什么具体的感官细节"。易错点提醒：提修改建议时最好给出具体例子——"Maybe add: The air is thick with the scent of incense and old wood." 而不是只说"加点气味"。' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改。顺序：①先加缺的感官（至少补1种）②再调结构（Hook改得更吸引人/个人感受更具体）③最后查语言（插入宾补/替换笼统形容词为具体描写）。教师：Don\'t just fix grammar — ADD a sense! 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色语句流畅度。易错点提醒：加感官不等于加一个词——加一句完整的感官描写。"The air smells musty" 比只加 "smelly" 好。' },
    { step: '展示+闭眼听读', time: '8', content: '【PPT P4 展示技巧】3-4 位自愿者上台读自己的地点描写。独特规则：全班闭眼听——读完后，听众说出自己"看到/听到/闻到/感觉到"了什么。教师：Listen with your eyes closed. What do you see in your mind? 预设回答：I saw ancient stone walls. I felt the cold wind. I heard birds. 板书时机：记录听众反馈的感官词。差异化提示：B班可看稿读但放慢；A班脱稿+用语气传达感受。易错点提醒：描写文的朗读速度是议论文的 3/4——读者需要时间在脑中构建画面。' },
    { step: '结课+自评', time: '5', content: '【PPT P7 总结+自评】全班投票：最想去的地方/感官最丰富的描写/最动人的个人感受。学生自评：①我加了哪种新感官？②下次写地点描写我会先做什么？教师：What makes a place description come alive? 预设回答：Sensory details. Not just "beautiful" — but what you actually see, hear, smell, and feel. 板书时机：写最佳描写的 Hook 作为范例。差异化提示：B班中文自评；A班英文自评。易错点提醒：最好的地点描写让读者感觉自己去过那里——哪怕只读了100个词。' }
  ],
  blackboard: '┌─ U4 Writing II: Sensory Review ─────────────┐\n│ Review Checklist:                             │\n│  ✅ ≥3 senses (not just sight!)               │\n│  ✅ Specific, not general (not "good smell")  │\n│  ✅ 5-part structure (Hook→Visual→Senses→    │\n│     History→Feeling)                          │\n│  ✅ ≥1 past participle as OC                  │\n│  ✅ Personal feeling is REAL                   │\n│                                                │\n│  Fix Order: 1. Add sense  2. Fix structure    │\n│             3. Polish language                 │\n└────────────────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改终稿，配图提交。写 20 词英文反思：我的描写中最打动人的感官细节是…【提高作业】用同样的"五感+感受"框架描写另一处你去过的历史地点（80词）。【参考答案——教师用】反思示例：The most powerful sensory detail in my description is the cold, rough stone under my fingers — I think it makes the reader feel like they are touching history.',
  reflection: '✅ 亮点：闭眼听读展示让学生直观感受"好描写就是能让读者\'看见\'"。⚠️ 需改进：嗅觉词汇仍需大量积累，建议建班级感官词库墙。📌 下节课衔接：进入 Project，将本单元所学整合为"世界历史文化探索"展。'
}));

// ====== Period 8: Project (世界历史文化探索展) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u4-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '历史与传统', '展览', '人教版必修二U4', '第八节课'],
  textbookAnalysis: '本课为必修第二册 Unit 4 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的历史词汇+阅读的 UK 形成史+语法的过去分词作宾补+听与谈的节日比较+写作的感官地点描写——完成一份"世界历史文化探索"展板。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确评分标准和模块间的逻辑联系。B班：group work 中容易"搭便车"，需明确定人定责+模块 checklist。共同问题：展板信息罗列而没有"探索"的叙事感——4个模块应该串成一个"旅程"。',
  objectives: [
    '语言能力：综合运用本单元词汇、过去分词作宾补、比较句型、感官描写，以英文完成一份"世界历史文化探索"展板。',
    '文化意识：通过展览形式展示各国历史文化的多样性，培养跨文化理解与尊重。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 展板四模块：Country Spotlight（选一个国家+UK 形成史类似的历史概述）→ Landmark Feature（一个地标的感官描写）→ Tradition Highlight（一个节日/传统+与中国的比较）→ Travel Tip（用宾补写实用建议）② 单元知识整合：历史词汇/过去分词作宾补/比较句型/五感描写 ③ 小组分工：Historian / Landmark Writer / Tradition Expert / Travel Advisor',
  difficulties: '① 四个模块的衔接——不是四个独立的块，而是"一个国家/一个地标/一个传统/一条建议"的探索旅程。② Country Spotlight 模块模仿 UK 形成史写法——学生容易只列事实没有叙事。③ 展板语言密度——要在有限空间平衡文字与视觉。',
  teachingMethods: '① PBL项目式学习：以探索展为驱动问题。② 小组协作：角色分工+module checklist。③ 展览+最佳展板评选。',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 展板四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师带学生回顾本单元5课学了什么：听与说（历史词汇+地标分享）→阅读（UK形成史+时间轴）→语法（have/get sth done+see sth done）→听与谈（节日比较+兴趣表达）→写作（五感地点描写）。教师：Today we become cultural explorers! 预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出每课核心内容+一个例句。易错点提醒：展板每模块至少用一次过去分词作宾语补足语。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 展板结构】【PPT P3 角色卡】教师展示四模块：①Country Spotlight（选一个国家模仿 UK 形成史写法概述历史）②Landmark Feature（一个地标的五感描写）③Tradition Highlight（一个节日/传统+与中国比较）④Travel Tip（用 have sth done 等宾补写实用旅行建议）。角色：Historian 写历史概述 / Landmark Writer 写感官描写 / Tradition Expert 写节日比较 / Travel Advisor 写旅行建议。教师：Choose your country and role! 预设回答：We choose Italy. I\'m the Landmark Writer — I\'ll describe the Colosseum! 板书时机：留模块结构和角色。差异化提示：B班给语言模板+国家建议（意大利/法国/日本/埃及）；A班自由选国家。易错点提醒：4个模块要用同一种颜色/风格的排版——Designer 负责统一视觉，不要让展板看起来像4个人各做各的。' },
    { step: '制作展板', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】小组制作。教师巡视提醒：①全英文！②每模块至少3句完整句 ③至少2个过去分词作宾补 ④至少1个比较句型 ⑤至少2种感官描写。预设回答：（小组制作中）板书时机：无。差异化提示：B班给每模块句型开头；A班独立完成+追求语言质量。易错点提醒：四模块要有"探索"的旅行感——可以设计为一张"虚拟机票"+"四个旅行日志"。让读者感觉跟着你一起去探索了那个国家。' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】每组 2 分钟展示。全班投票：最想去的目的地/最佳感官描写/最佳历史叙事/最佳展板设计。教师：Take us on a journey to your country! 预设回答展示。板书时机：记录投票。差异化提示：B班可看展板讲；A班脱稿+模仿导游语气。易错点提醒：展示时不要念展板——讲展板背后的故事。"We chose Italy because I was fascinated by how a country with so much ancient history stays so alive today."' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】学生勾选四维薄弱项：历史词汇不熟？过去分词作宾补不会用？比较句型忘了？五感描写写不出？写1条补强计划。教师：Which skill from this unit do you want to improve? 预设回答：I need to practice past participle as object complement. I will review the grammar table and write 5 sentences about my daily life. 板书时机：留自评四维。差异化提示：B班中文写；A班英文写。易错点提醒：补强计划要有产出——不是"复习语法"，而是"用 have sth done 写5句关于周末安排"。' }
  ],
  blackboard: '┌─ U4 Project: Cultural Explorer ────────┐\n│ 🗺️ Exploration Board:                    │\n│  ① Country Spotlight (history overview) │\n│  ② Landmark Feature (5-sense desc.)     │\n│  ③ Tradition Highlight (compare+contrast│\n│     with China)                          │\n│  ④ Travel Tip (use have sth done, etc.) │\n│                                          │\n│ 👥 Roles: Historian / Landmark Writer /  │\n│    Tradition Expert / Travel Advisor     │\n│                                          │\n│ ⭐ Must: ≥2 past participles as OC       │\n│    ≥1 comparison / ≥2 senses            │\n└──────────────────────────────────────────┘',
  exercises: '【基础作业】完成小组展板（未完成的继续做），拍照提交。写 30 词英文反思：如果我真的去这个国家旅行，我最想看什么？我的展板会让别人想去吗？【提高作业】选展板中没有提到的那个国家的另一面（如美食/音乐/运动），写 50 词英文简报。【参考答案——教师用】反思示例：If I really went to Italy, I would first visit the Colosseum because our Landmark Feature made it sound so powerful. I think our board would make people curious because the sensory details about the ancient stone and the sounds of the piazza feel real.',
  reflection: '✅ 亮点：四模块"旅程"框架让展板有了叙事感而非信息堆砌。⚠️ 需改进：部分小组比较句型使用不足（只写相同不写不同），下次可强制要求至少2个比较。📌 下节课衔接：进入 Unit 5 Music，从历史文化探索转向音乐的情感世界。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b2-u4-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b2-u4 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
