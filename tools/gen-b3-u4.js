/**
 * gen-b3-u4.js — 必修第三册 Unit 4 Space Exploration (8课时)
 *
 * 语篇: SPACE: THE FINAL FRONTIER (太空探索史: Sputnik/ISS/火星任务)
 * 语法: 不定式作定语和状语 (something to eat / I went there to study)
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
const UNIT = 4;
const UNIT_TITLE = 'Space Exploration';
const BOOK = '必修第三册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u4-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '太空', '航天', '人教版必修三U4', '第一节课'],
  textbookAnalysis: '本课为必修第三册 Unit 4 Space Exploration 第一课时（Listening and Speaking），属单元导入+输入环节。听力材料为一段介绍太空探索历程（人造卫星/宇航员/空间站/火星任务）的对话与独白，功能语境是"描述太空科技与航天成就"。语言重点为太空词汇（space, explore, astronaut, satellite, launch, orbit, mission, galaxy）及描述成就句型（It was the first to... / The mission aimed to... / Scientists have managed to...）。为本单元 Reading 的"太空探索史"说明文做词汇与话题预热。',
  overview: '【学情分析】A班：对卫星/宇航员等词较熟，但 orbit/galaxy/launch 等词较生。B班：对太空科技背景了解少，听力抓细节弱。共同问题：描述太空成就停留在"very great"表层，缺乏"里程碑意义"表达。',
  objectives: [
    '语言能力：听懂关于太空探索的听力材料，提取关键信息（事件/时间/成就/意义），准确使用 6-8 个太空核心词汇。',
    '文化意识：了解人类太空探索的伟大成就，增强科技自信与探索精神。',
    '思维品质：通过"听前预测—听中验证—听后推理"形成系统听力策略。',
    '学习能力：能用 It was the first to... / The mission aimed to... 就太空成就做简短描述。'
  ],
  keyPoints: '① 太空核心词汇：space / explore / astronaut / satellite / launch / orbit / mission / galaxy ② 描述句型：It was the first to... / The mission aimed to... / Scientists have managed to... ③ 听力微技能：听前读题支预测关键词、听中抓时间与事件。',
  difficulties: '① launch（发射）拼写与发音。原因：au 发 /ɔː/。易错点提醒：launch /lɔːntʃ/，不是 /lɑːntʃ/。② orbit（轨道）作名词与动词的双重用法。③ galaxy（星系）抽象词，学生易与 planet 混淆。',
  teachingMethods: '① 任务型（TBL）：以介绍一个太空成就为终任务。② 听前预测+听中填卡：信息卡脚手架。③ 对子互问操练描述句型。',
  preparation: '【PPT课件】P1 单元封面（Space Exploration）；P2 太空成就图片九宫格（Sputnik/阿波罗登月/ISS/火星探测器/航天飞机/中国空间站/哈勃望远镜/宇航员出舱/火箭发射）；P3-4 听力任务题；P5 描述句型板；P6 说话任务卡。【实物教具】太空成就信息卡 printed 每组一套；太阳系图一张。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine space achievements. Which ones have you heard of? Can you name them? 预设回答：The moon landing! The space station! 板书时机：右侧板书 space / explore / astronaut。差异化提示：B班指图说中文再跟读英文；A班用 I know... 造句。易错点提醒：astronaut /æstrənɔːt/ — as 发 /æs/ 不发 /eɪs/。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 space / explore / astronaut / satellite / launch / orbit / mission / galaxy。教师：What does a satellite do? 预设回答：It orbits the Earth and sends information. 板书时机：左栏板书词+短注释。差异化提示：B班配图记忆+词性标注；A班用词造句。易错点提醒：satellite /sætəlaɪt/ — te 发 /tə/ 不发 /teɪ/。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to an introduction about the history of space exploration. Predict: What will be mentioned? (first satellite / moon landing / space station / Mars) 预设回答：First satellite and moon landing! 板书时机：预测词写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测理由。易错点提醒：听力常见陷阱 — 时间信息会先给错误再修正。"in 1957" 可能被"actually in 1961"推翻。' },
    { step: '听中填卡', time: '10', content: '【PPT P5 表格】【音频 段一】播放听力，学生填信息卡（事件/时间/国家/成就/意义）。教师：When was the first satellite launched? What was its name? 预设回答：In 1957. It was Sputnik. 板书时机：核对答案时填表于黑板中部。差异化提示：B班听两遍只填事件+时间；A班一遍填全。易错点提醒：Sputnik /spʊtnɪk/ — 俄语借词，pu 发 /pʊ/ 不发 /pjuː/。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to describe a space achievement? It was the first to... / The mission aimed to... / Scientists have managed to... 教师示范后用登月信息造句。预设回答：Apollo 11 was the first to land on the moon. The mission aimed to explore the lunar surface. 板书时机：句型板书于中央。差异化提示：B班套用模板；A班替换事件名+成就细节。易错点提醒：the first to 后接动词原形 — "the first to land" 不是 "the first to landing"。' },
    { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，从信息卡中选一个太空成就互介。教师：Introduce a space achievement to your partner. Use the sentence patterns. 预设回答：I want to introduce the ISS. It was built to allow astronauts to live in space. Scientists have managed to keep it running for over 20 years. 板书时机：无。差异化提示：B班用填空式对话卡；A班自由描述并追问意义。易错点提醒：orbit /ɔːbɪt/ — or 发 /ɔː/ 不发 /ɒ/。' }
  ],
  blackboard: '┌─ U4 Listening & Speaking ──────┐\n│ space / explore / astronaut      │\n│ satellite / launch / orbit       │\n│ mission / galaxy                 │\n│                                  │\n│ It was the first to...           │\n│ The mission aimed to...          │\n│ Scientists have managed to...    │\n│                                  │\n│ Achievement Card:                │\n│  Sputnik | 1957 | USSR | 1st sat │\n│  Apollo 11 | 1969 | US | moon    │\n└──────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有太空词汇。2. 用 It was the first to... 写 3 句太空成就描述。【提高作业】用英文写一段 50 词介绍：介绍一个你了解的太空成就，包含事件/时间/至少 2 点意义。【参考答案——教师用】基础2示例：Sputnik was the first to orbit the Earth. / Apollo 11 was the first to land humans on the moon. / The ISS was the first to host a long-term space lab.',
  reflection: '✅ 亮点：九宫格激活+信息卡脚手架有效降听力焦虑，B班填卡完成率高。⚠️ 需改进：satellite 发音仍有困难，下节需强化。📌 下节课衔接：进入阅读 SPACE: THE FINAL FRONTIER，从太空认知延伸到探索历程。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u4-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '太空', '说明文', '探索史', '人教版必修三U4', '第二节课'],
  textbookAnalysis: '本课为必修第三册 Unit 4 第二课时（Reading I），语篇 SPACE: THE FINAL FRONTIER 是一篇说明文，讲述人类太空探索的历程——从Sputnik到阿波罗登月、国际空间站、火星任务，展望未来探索。结构为早期突破→载人航天→空间站时代→深空探测→未来展望。语言重点为说明文衔接词（first, then, after, before long, finally）与太空探索词汇（explore, launch, orbit, mission, frontier, vehicle, distant）。承接第一课时词汇，本课语篇中出现不定式作定语和状语。',
  overview: '【学情分析】A班：能快速把握段落主旨，但对"时间链"的说明文结构训练不足。B班：对Sputnik/ISS等背景知识少，需时间线脚手架。共同问题：说明文的"按时间推进"结构感知不清晰，易忽略 first/then 等顺序标志词。',
  objectives: [
    '语言能力：读懂说明文，提取太空探索的时间线/里程碑/成就/挑战；掌握 8-10 个论述类核心词汇。',
    '文化意识：理解人类太空探索的伟大征程与协作精神，形成"探索未知"的科学观念。',
    '思维品质：通过"时间链+里程碑"分析培养说明文结构思维与科学归纳能力。',
    '学习能力：能用时间轴+里程碑表复述文章主线。'
  ],
  keyPoints: '① 说明文结构：early breakthroughs → manned flight → space stations → deep space → future ② 时间线词汇：in 1957 / in 1961 / after that / before long / finally ③ 核心短语：manage to / aim to / carry... to / dream of',
  difficulties: '① frontier（前沿/边疆）比喻义——学生易按字面理解。原因：多义词。② manage to（设法做到）与 try to（试图）的区别。③ vehicle（运载工具）在文中指航天器，不是"车辆"。',
  teachingMethods: '① 时间轴阅读：构建太空探索进程。② 里程碑填图法：标注关键事件。③ 科学归纳：成就vs挑战。',
  preparation: '【PPT课件】P1 Sputnik与阿波罗登月图片；P2 太空探索时间线（1957-至今）；P3-4 里程碑表；P5 说明文结构图；P6 词汇对比表；P7 总结回顾。【实物教具】时间轴空白工作单 printed 每人一份；段落拼图卡。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P1 登月图片】教师：This is the moon landing in 1969. But space exploration began earlier. What do you think was the first step? 预设回答：A satellite? / A rocket? 板书时机：板书 first step? + 三个问号。差异化提示：B班中文猜；A班英文猜并给理由。易错点提醒：frontier /frʌntɪə/ — r 发 /r/ 不发 /f/，与 front 区分。' },
    { step: '快速阅读抓主干', time: '8', content: '【PPT P3 时间轴】教师：Read fast (3 min). Find: ① What was the first breakthrough? ② What are the major milestones? ③ What is the future goal? 预设回答：① Sputnik in 1957. ② Moon landing, ISS, Mars missions. ③ To explore Mars and beyond. 板书时机：填时间轴的三个关键里程碑。差异化提示：B班给三选一选项；A班写完整句。易错点提醒：vehicle /viːɪkəl/ — ve 发 /viː/ 不发 /ve/。' },
    { step: '精读段落1-3 早期突破与载人航天', time: '10', content: '【PPT P4 里程碑表】教师精讲：manage to = 设法做到；aim to = 旨在。教师：How did space exploration begin? 预设回答：It began with Sputnik in 1957. Then humans managed to go to space. 板书时机：左侧栏补充"manage to / aim to / carry to"。差异化提示：B班读后填关键词；A班读后用自己话解释。易错点提醒：manage to（设法做成）≠ try to（试图，未必成功）——考试高频陷阱。' },
    { step: '精读段落4-5 空间站与深空探测', time: '10', content: '【PPT P5 成就表】教师：What comes after the moon landing? 学生填表匹配（ISS / Mars rovers / telescopes → achievements）。教师：What is the ISS for? 预设回答：It allows astronauts to live and work in space for long periods. 板书时机：右侧画"moon→ISS→Mars→future"箭头图。差异化提示：B班连线匹配；A班写完整句。易错点提醒：allow sb to do（允许某人做）中 to 不可省——"allow astronauts to live" 不是 "allow astronauts live"。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 说明文结构】教师：What can we learn? (Space exploration pushes human limits. / It requires global cooperation.) 预设回答：Space exploration shows human courage. It requires countries to work together. 板书时机：圈出结构关键词。差异化提示：B班跟读关键词；A班用自己的话总结。易错点提醒：require（需要）后接 to do — "require countries to work" 不是 "require countries working"。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾"突破→载人→空间站→深空→未来"结构+核心词汇。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：cooperation /kəʊɒpəreɪʃən/ — co- 前缀"共同"，不是 cooperation /kɒpəreɪʃən/。' }
  ],
  blackboard: '┌─ U4 Reading I: SPACE FINAL FRONTIER ─┐\n│ BREAKTHROUGH → MANNED → STATIONS →     │\n│ DEEP SPACE → FUTURE                    │\n│                                         │\n│ Milestones: Sputnik(1957)/Apollo(1969)  │\n│            ISS / Mars rovers            │\n│ Future: Mars and beyond                 │\n│                                         │\n│ manage to / aim to / carry to           │\n│ allow... to / require... to / frontier  │\n└─────────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-3段 2 遍，圈出所有顺序词（first/then/after/before long）。2. 用时间轴上的3个关键里程碑各写1句成就描述。【提高作业】用 80 词左右写一段：你认为太空探索对人类有什么意义？为什么？（用 explore / manage to / frontier）【参考答案——教师用】基础2示例：In 1957, Sputnik became the first satellite. / In 1969, Apollo 11 managed to land on the moon. / The ISS allows astronauts to live in space for months.',
  reflection: '✅ 亮点：时间轴+里程碑表有效组织信息，B班完成率高。⚠️ 需改进：manage to vs try to 仍是难点，精读课需澄清。📌 下节课衔接：进入精读语言+不定式在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u4-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '不定式', '太空', '人教版必修三U4', '第三节课'],
  textbookAnalysis: '本课为必修第三册 Unit 4 第三课时（Reading II），聚焦语篇 SPACE: THE FINAL FRONTIER 的精读与语言分析。重点分析文中不定式作定语（something to eat / the first to land / a mission to explore）和作状语（I went there to study / Scientists work hard to discover）在说明文中的功能——定语修饰名词表用途，状语表目的。同时深化语篇中高频学术词汇的用法辨析（explore / launch / orbit / mission / frontier）。',
  overview: '【学情分析】A班：能识别不定式，但辨析其作定语还是状语仍有困难。B班：不定式概念感模糊，需大量语境例句支撑。共同问题：阅读中见到不定式会跳过不分析其功能——学生把 to do 当"固定搭配"而非"语法工具"。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 5 个不定式作定语或状语的用法，准确辨析功能。',
    '文化意识：通过不定式体会英语如何用简洁结构表达用途与目的——不同于中文的习惯。',
    '思维品质：分析不定式在说明文中的"用途/目的"功能，培养语法服务于意义的意识。',
    '学习能力：建立"从读到写"的语料库——积累课文中的优质不定式句型用于后续写作。'
  ],
  keyPoints: '① 语篇中不定式作定语（something to eat / the first to land / a mission to explore）与作状语（went there to study / work hard to discover）② 说明文高频动词：explore / launch / orbit / mission / frontier ③ 不定式在说明文中的修辞功能：表用途/目的→增强逻辑性',
  difficulties: '① 不定式作定语 vs 作状语的辨析。原因：形同功不同，需看句法位置。② the first/last/best + to do 结构。③ frontier（前沿）比喻义在文中的含义。',
  teachingMethods: '① 标注法：圈出文中所有不定式结构并分析功能。② 替换练习：改写从句为不定式。③ 语料卡记录：分类摘录优质句子。',
  preparation: '【PPT课件】P1-2 课文中圈出的不定式示例；P3 定语vs状语对比表；P4 语料卡模板；P5 词汇辨析表；P6 句型改写练习；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 结构图】教师：Last class we learned the timeline of space exploration. Can you recall the milestones? 预设回答：Sputnik, Apollo, ISS, Mars. The future goal is to explore Mars. 板书时机：左栏写 1957/1969/ISS/Mars 时间线。差异化提示：B班看时间轴读关键词；A班完整复述。易错点提醒：recall ≠ remember — recall 更强调"主动调取记忆"。' },
    { step: '不定式发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle all "to + verb" structures. Decide: is it an attribute (定语) or an adverbial (状语)? 学生标记后全班核对。教师：Why does the author use "to + verb" here? 预设回答：To show purpose or to modify a noun. 板书时机：逐句板书圈出的不定式结构。差异化提示：B班给划线句直接圈 to；A班自己找+标注功能。易错点提醒："something to eat" 中 to eat 作定语修饰 something，不是目的状语。' },
    { step: '定语vs状语辨析', time: '10', content: '【PPT P3 对比表】教师对比：定语——修饰名词（something to eat / the first to land / a mission to explore）；状语——表目的（went there to study / work hard to discover）。教师例句辨析。预设回答辨析。板书时机：两列对比板书。差异化提示：B班根据提示选择填空；A班独立造句。易错点提醒：不定式作定语常跟在名词后——the first to land 中 to land 修饰 the first。' },
    { step: '语料库搭建', time: '10', content: '【PPT P4 模板】教师：Build your corpus. Categorize to-do sentences and key verbs. 学生分类填语料卡：①不定式作定语优质句摘录 ②不定式作状语优质句摘录 ③太空动词（explore/launch/orbit/mission/frontier）。板书时机：巡视指导。差异化提示：B班填词；A班造句。预设回答：按太空探索语料库模板分类填写词条。易错点提醒：frontier 在文中表"前沿领域"，不是"边境线"。' },
    { step: '句型改写', time: '5', content: '【PPT P6 练习】教师：Rewrite these sentences using infinitive. 例：I went there because I wanted to study. → I went there to study. 预设回答造句。板书时机：板书改写公式。差异化提示：B班给改写框架；A班独立改。易错点提醒：改写后检查——不定式状语表目的，主句主语应是不定式动作的发出者。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】教师：Let\'s review infinitive as attribute and adverbial. 回顾不定式作定语/状语功能+语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课深入讲不定式作定语和状语的规则。' }
  ],
  blackboard: '┌─ U4 Reading II: Language Focus ──────┐\n│ Infinitive as Attribute (定语):       │\n│  something to eat                      │\n│  the first to land                     │\n│  a mission to explore                  │\n│ Infinitive as Adverbial (状语):        │\n│  I went there to study. (purpose)      │\n│  work hard to discover                 │\n│                                        │\n│ Verbs: explore / launch / orbit        │\n│        mission / frontier              │\n└────────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出5个不定式结构并标注定语/状语。2. 将以下句子改写为不定式状语：She studies hard because she wants to be an astronaut.【提高作业】用不定式作定语和状语各写2句关于太空探索的句子。【参考答案——教师用】基础2示例：She studies hard to be an astronaut.',
  reflection: '✅ 亮点：标注发现法让学生主动探索语法，参与度高。⚠️ 需改进：不定式定语vs状语辨析仍有混淆，语法课需强化。📌 下节课衔接：进入语法课，系统讲不定式作定语和状语的规则。'
}));

// ====== Period 4: Grammar (不定式作定语和状语) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u4-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '不定式', '定语', '状语', '人教版必修三U4', '第四节课'],
  textbookAnalysis: '本课为必修第三册 Unit 4 第四课时（Discovering Useful Structures），系统教学不定式作定语和状语的用法。基于 Reading 语篇中提取的例句，引导学生归纳出规则：作定语（修饰名词表用途/未做，常跟在名词后，如 something to eat / the first to land）和作状语（表目的，如 went there to study / work hard to discover）。通过太空探索主题的语境化练习巩固。',
  overview: '【学情分析】A班：知道 to do 表目的，但作定语是新知。B班：不定式概念仍模糊，需大量语境化例句反复操练。共同问题：写作中要么不用不定式，要么乱用导致功能不清。',
  objectives: [
    '语言能力：准确识别并产出不定式作定语和状语的句子，在太空话题中产出 5 个以上正确句子。',
    '文化意识：通过不定式更精准地表达太空探索的用途与目的。',
    '思维品质：通过"发现例句→归纳规则→应用规则"的归纳法培养语法学习策略。',
    '学习能力：建立"语法自查表"——写作后自行检查不定式的功能是否正确。'
  ],
  keyPoints: '① 不定式作定语：修饰名词表用途/未做（something to eat / the first to land / a mission to explore / no place to live）② 不定式作状语：表目的（went there to study / work hard to discover）③ the first/last/best + to do 结构',
  difficulties: '① 不定式作定语 vs 作状语的辨析。原因：形同功不同，需看位置。② something/anything/nothing + to do 结构。③ 不定式状语与 -ing 状语的区分——to do 表目的，-ing 表伴随。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习 ② 改写对比：从句 vs 不定式 ③ 改错练习：纠正典型错误',
  preparation: '【PPT课件】P1 定语vs状语对比表；P2 课文例句摘录；P3 规则归纳页；P4 the first to do 结构；P5 改写任务卡；P6 改错题；P7 总结。【实物教具】句型卡一套；改写工作单。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中5个不定式结构，学生圈 to+verb 并判断定语/状语。教师：What does this to-verb modify? A noun or a verb? 预设回答：It modifies a noun — it\'s an attribute. / It shows purpose — it\'s an adverbial. 板书时机：左栏板书例句，标注功能。差异化提示：B班只圈词不分析功能；A班分析 to-do 修饰什么。易错点提醒：不定式作定语修饰名词，作状语修饰动词或全句——看修饰对象定功能。' },
    { step: '规则归纳', time: '12', content: '【PPT P3 对比表】教师引导学生归纳：定语——修饰名词表用途/未做（something to eat / a mission to explore / no place to live）；状语——表目的（went there to study / work hard to discover）。教师：When to-verb follows a noun, what is it? 预设回答：An attribute! 板书时机：板书完整对比表。差异化提示：B班填已给框架表；A班自己画表填。易错点提醒：something/anything/nothing + to do 是常见定语结构——"I have something to tell you" 中 to tell 修饰 something。' },
    { step: 'the first to do 讲练', time: '8', content: '【PPT P4 结构】教师：After the first/last/best/only, use to do. 例：Apollo 11 was the first to land on the moon. / She was the last to leave. 预设回答辨析。板书时机：板书 the first to do 公式。差异化提示：B班选词填空（to do/doing）；A班造句。易错点提醒：the first 后接 to do 不接 doing — "the first to land" 不是 "the first landing"。' },
    { step: '改写操练', time: '8', content: '【PPT P5 改写卡】教师：Rewrite using infinitive. 例：I went there because I wanted to study. → I went there to study. / I have a mission. I want to explore Mars. → I have a mission to explore Mars. 教师抽学生板演。预设回答造句。板书时机：板书改写公式。差异化提示：B班给句型框；A班自由改写并追加太空主题细节。易错点提醒：改写后检查——不定式状语的主语应=主句主语，表目的。' },
    { step: '改错巩固', time: '3', content: '【PPT P6 改错】教师：Find the mistakes. 展示 3 个典型错误：①I went there for studying.（应 to study）②She was the first landing.（应 to land）③I have something to eat it.（多余 it）。学生纠错并解释。预设回答纠错。板书时机：板书错误→改正公式。差异化提示：B班辨别对错选；A班解释为什么错。易错点提醒：最常犯——表目的用 for doing（错），应为 to do。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Let\'s review infinitive rules. 回顾不定式定语/状语比较表+the first to do+改错要诀。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述规则。易错点提醒：写作后自查——每个不定式是定语还是状语？功能是否正确？' }
  ],
  blackboard: '┌─ U4 Grammar: Infinitive as Attr & Adv ─┐\n│ Attribute (定语):                         │\n│  something to eat                          │\n│  a mission to explore                      │\n│  no place to live                          │\n│  the first/last/best + to do               │\n│ Adverbial (状语 - purpose):                │\n│  I went there to study.                    │\n│  work hard to discover                     │\n│                                            │\n│ ⚠️ Purpose = to do (NOT for doing!)        │\n│ ✗ I went there for studying.               │\n└────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 用不定式作定语和状语各造 2 句关于太空探索的句子。2. 将以下句子改写为不定式状语：They work hard because they want to reach Mars.【提高作业】写 60 词短文描述一个太空任务，要求至少用 3 个不定式结构（含1个定语、1个状语）。【参考答案——教师用】基础1示例：The mission to explore Mars is challenging. (定语) / Scientists work hard to discover new planets. (状语) 基础2示例：They work hard to reach Mars.',
  reflection: '✅ 亮点：改写对比让语法操练不再枯燥，课堂活跃度高。⚠️ 需改进：to do vs for doing 区分仍是难点，听与谈课可融入练习。📌 下节课衔接：听与谈聚焦太空探索价值辩论，用语篇巩固不定式。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u4-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '太空探索', '辩论', '人教版必修三U4', '第五节课'],
  textbookAnalysis: '本课为必修第三册 Unit 4 第五课时（Listening and Talking），语境为"辩论太空探索是否值得"。听力材料为一段关于太空探索投入与回报的辩论对话，口语输出任务为就"太空探索是否值得"做正反辩论与表态。功能语言为表达立场与论据（I strongly believe... / The main reason is... / On the contrary... / Despite..., I think...）。结合语法课所学的不定式，在口语中自然运用 to do 表目的。',
  overview: '【学情分析】A班：能表达简单立场，但缺乏"论据+反论"的辩论表达链。B班：开口意愿低、辩论句型储备少。共同问题：只说立场不给论据，缺少 The main reason is... 使论证空洞。',
  objectives: [
    '语言能力：听懂关于太空探索辩论的对话，提取立场与论据；能用至少 4 种句型表达立场并论证。',
    '文化意识：体会"科技投入需要理性辩论"的思辨精神。',
    '思维品质：在讨论中练习"立场→论据→反论→结论"的完整辩论链。',
    '学习能力：通过辩论对话训练批判性倾听——听懂后回应而非只等自己说。'
  ],
  keyPoints: '① 立场句型：I strongly believe... / In my opinion... / I am convinced that... ② 论据句型：The main reason is... / For one thing... / For another... ③ 反论句型：On the contrary... / Despite..., I think... / However...',
  difficulties: '① On the contrary（相反）表反驳 — 学生易与 on the other hand（另一方面）混。原因：形近意近。② Despite（尽管）后接名词/doing，不接句子。③ 回应时 only say "I disagree" no reason — 需培养 The main reason 跟进的意识。',
  teachingMethods: '① 听前预测→听中配对→听后产出 ② 角色扮演：三人一组（正方+反方+裁判）③ 太空探索辩论圆桌',
  preparation: '【PPT课件】P1 辩题（太空探索是否值得投入）；P2 立场句型板；P3 听力任务题；P4 听力任务卡；P5 论据句型板；P6 角色卡。【实物教具】辩论论据卡 printed；角色卡。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 辩题】教师：Space exploration costs billions. Is it worth it? Or should we spend the money on Earth? 预设回答：It\'s worth it! / No, we have problems on Earth. 板书时机：左栏板书动词 worth / spend / invest / waste。差异化提示：B班中文说再翻英文；A班直接英文。易错点提醒：worth（值得）后接 doing — "worth investing" 不是 "worth to invest"。' },
    { step: '听力抓立场', time: '10', content: '【PPT P3 听力任务】听对话，抓"谁持什么立场+什么论据"。教师：Listen for: What is the opinion? What is the reason? 预设回答：He believes it\'s worth it. The main reason is that technology benefits daily life. 板书时机：配对填表（立场|论据）。差异化提示：B班给配对连线题；A班听写关键词。易错点提醒：listen for（有目的地听）≠ listen to（泛听）——引导学生带问题听。' },
    { step: '听中记录', time: '8', content: '【PPT P4 听力任务卡】【音频】重听，学生填完整立场+论据链。教师：How did they support their views? 预设回答：For one thing, satellites help weather forecasting. For another, it inspires young people. 板书时机：核对填表。差异化提示：B班听两遍；A班一遍+复述论据。易错点提醒：For one thing... For another... 是递进不是对立——两个论据同向。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练立场+论据链：A: I strongly believe space exploration is worth it. / B: The main reason is that technology benefits us. / A: For one thing, satellites help us. For another, it inspires us. / B: On the contrary, the money could help the poor. 预设回答跟读+仿造。板书时机：板书立场→论据链条。差异化提示：B班用填空脚本；A班自主对话。易错点提醒：Despite 后接名词/doing — "Despite the cost, I think..." 不是 "Despite it costs, I think..."。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】三人一组：Pro A（正方）、Con B（反方）、Judge C（裁判）。就"太空探索是否值得"辩论。教师巡视。预设回答：A: I strongly believe it\'s worth it. / B: On the contrary, we have problems on Earth. / C: Both sides have valid points. 板书时机：留立场句型和论据链供参考。差异化提示：B班照卡读；A班脱稿加即兴内容。易错点提醒：角色扮演中注意用不定式表目的 — "We explore space to discover new possibilities."' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Remember to give reasons after your opinion. 回顾立场句型+论据策略。预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一句收获。易错点提醒：给立场后记得加"The main reason is..."——论证才完整。' }
  ],
  blackboard: '┌─ U4 Listening & Talking ─────────┐\n│ Position:                          │\n│  I strongly believe...             │\n│  In my opinion...                  │\n│  I am convinced that...            │\n│ Reasons:                           │\n│  The main reason is...             │\n│  For one thing... For another...   │\n│ Rebuttal:                          │\n│  On the contrary...                │\n│  Despite..., I think...            │\n│                                    │\n│ Chain: Position → Reason → Rebuttal│\n└────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有立场句型。2. 用至少 2 种立场句型各写 1 句太空探索表态+论据。【提高作业】写 60 词对话：三人辩论"太空探索是否值得"（至少 4 轮，含立场与论据）。【参考答案——教师用】基础2示例：I strongly believe space exploration is worth it. The main reason is that technology benefits daily life. / On the contrary, the money could solve problems on Earth. Despite the cost, I think it inspires us.',
  reflection: '✅ 亮点：角色扮演三角色设置让学生理解真实辩论中的多元声音。⚠️ 需改进：Despite 后接名词仍易错，写作课可设置强制格式。📌 下节课衔接：进入写作，将太空探索观点写成议论文。'
}));

// ====== Period 6: Writing I (结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u4-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '议论文', '太空探索', '人教版必修三U4', '第六节课'],
  textbookAnalysis: '本课为必修第三册 Unit 4 第六课时（Reading for Writing I），写作体裁为议论文——论述太空探索是否值得。结构为：引出话题（背景+争议）→ 正方论据（值得的理由）→ 反方论据（不值得的理由）→ 个人立场与结论。语言重点为议论文衔接词（firstly, moreover, however, in conclusion）与论证句型（I believe... / The main reason is... / Despite..., I think...）。结合本单元 Reading 的探索精神与语法课的不定式，实现读-语法-写的闭环。',
  overview: '【学情分析】A班：有基本论证能力，但缺乏"正反兼顾"的辩证框架——常写成一边倒。B班：句型储备少、论证空洞，需大量脚手架。共同问题：议论文不知如何收尾——缺少"综上所述，我认为…"的结论句。',
  objectives: [
    '语言能力：掌握"话题—正方—反方—结论"四段式议论文结构，在太空探索话题中产出 80-100 词结构完整的短文。',
    '文化意识：通过书写议论文体会"理性辩证"的思辨精神。',
    '思维品质：通过"先正方再反方后结论"训练辩证逻辑思维。',
    '学习能力：建立"写作前先搭结构框架"的习惯——用 outline 而非直接开写。'
  ],
  keyPoints: '① 议论文四段结构：Topic (background+debate) → Pro (reasons for) → Con (reasons against) → Conclusion (your stance) ② 衔接词：Firstly / Moreover / However / In conclusion ③ 核心句型：I believe... / The main reason is... / Despite..., I think...',
  difficulties: '① 议论文与说明文的区别 — 议论文必须有明确立场。原因：学生易混体裁。② However 的正确标点——句首或分号后。③ 结论句不知道怎么写——需给模板。',
  teachingMethods: '① 范文解构法：读范文→画结构图→仿写 ② 语料卡搭建：从本单元5课积累词汇/句型。③ 过程写作：outline→draft→peer review→revise',
  preparation: '【PPT课件】P1 范文（关于太空探索是否值得的议论文）；P2 四段结构图；P3 衔接词表；P4 语料库模板；P5 写作提纲；P6 写作任务；P7 总结。【实物教具】四段结构空白工作单 printed 每人一份；语料卡模板。',
  process: [
    { step: '范文解构', time: '8', content: '【PPT P1 范文】教师展示范文，学生标注四段（话题/正方/反方/结论）。教师：Which paragraph gives reasons for? Which gives the conclusion? 预设回答：Paragraph 2 — reasons for. Paragraph 4 — conclusion. 板书时机：画四段结构框。差异化提示：B班给标注好的范文只匹配段号；A班自己画结构+标注衔接词。易错点提醒：最后一段必须有"In conclusion, I believe..."才算完整结论。' },
    { step: '四段结构讲透', time: '8', content: '【PPT P2 结构图】教师逐段讲解：P1 2句引出话题（background+debate）→ P2 3句正方论据（firstly/moreover）→ P3 2句反方论据（however）→ P4 2句结论（your stance）。教师示范写一段。预设回答跟读结构要点。板书时机：逐段板书模板句。差异化提示：B班给每段填空模板；A班给关键词自己写。易错点提醒：P3 的反方论据要客观 — 不要只写正方，要"however, some argue that..."' },
    { step: '连接词+句型', time: '5', content: '【PPT P3 词表】教师领读衔接词：Firstly / Moreover / However / Furthermore / In conclusion。教师示例句：Firstly, space tech benefits daily life. Moreover, it inspires us. However, some argue it\'s too costly. In conclusion, I believe it\'s worth it. 预设回答跟读。板书时机：板书衔接词于侧栏。差异化提示：B班选词填空；A班用全级衔接词写一段。易错点提醒：However 前用分号或句号 — "It\'s costly; however, it\'s worth it." 不是 "It\'s costly, however it\'s worth it."' },
    { step: '积语料', time: '5', content: '【PPT P4 语料库】教师：Build your word bank. Extract space verbs, argument words, and infinitive patterns. 学生从本单元5课中提取：①太空动词（explore/launch/orbit/discover）②论证词（believe/argue/despite/worth）③不定式模板（to explore / to discover）。板书时机：巡视。差异化提示：B班填词；A班造句。预设回答：按太空探索语料库分类卡填写词条。易错点提醒：同一意思用不同词替换避免重复——第一段说 worth，第三段说 valuable / beneficial。' },
    { step: '提纲+起草', time: '10', content: '【PPT P5 写作提纲】教师：Don\'t write sentences yet — just key words. 就"太空探索是否值得"写 80 词议论文 outline（四段各写关键词）。预设回答：P1: space / costly / debate / P2: tech benefits / inspires / P3: too expensive / Earth problems / P4: worth it / balance. 板书时机：留结构框供参考。差异化提示：B班用填空 outline；A班独立列提纲。易错点提醒：outline 不是草稿——用短语不是完整句。这是写前最重要的一步。' },
    { step: '互评提纲', time: '4', content: '【PPT P6 写作任务】同桌互换提纲，检查：四段都有吗？正反方都有吗？结论段有立场吗？教师：Your partner\'s outline: does it have all 4 parts? 预设回答：Yes, but the conclusion is weak. 板书时机：留 checklist。差异化提示：B班用 checklist 表逐项打勾；A班口头给改进建议。易错点提醒：互评不是挑刺——给一个赞美+一个建议。"Good outline! Maybe add a reason in paragraph 3."' }
  ],
  blackboard: '┌─ U4 Writing: Space Exploration ─────┐\n│ P1 Topic: Space exploration is...    │\n│ P2 Pro: Firstly,... Moreover,...      │\n│ P3 Con: However, some argue...        │\n│ P4 Conclusion: In conclusion, I...    │\n│                                       │\n│ Linkers: Firstly / Moreover / However │\n│         Furthermore / In conclusion   │\n│                                       │\n│ Word Bank: explore / launch / discover│\n│  believe / argue / despite / worth    │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】按课堂 outline 写完 80 词太空探索议论文初稿。要求：四段结构完整、至少 2 个衔接词、至少 1 个不定式结构。【提高作业】就同一话题写一则 30 词以内的辩论开场白（英文），要求有立场有感染力。【参考答案——教师用】基础示例（节选）：Space exploration is a topic of debate. Firstly, space technology benefits our daily life, such as satellites for weather. Moreover, it inspires young people to dream big. However, some argue that the money could solve problems on Earth. In conclusion, I believe it is worth it because it pushes human limits.',
  reflection: '✅ 亮点：四段结构框架让学生从"不知道写什么"变为"知道每段写什么"。⚠️ 需改进：However 标点仍需纠正，下节课用改错题强化。📌 下节课衔接：进入写作 II，互评修改+誊抄终稿。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u4-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '太空', '人教版必修三U4', '第七节课'],
  textbookAnalysis: '本课为必修第三册 Unit 4 第七课时（Writing II），在 Writing I 提纲+初稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进写作的能力。互评量表聚焦三维度：结构完整（4段）、语言质量（衔接词/不定式/词汇）、语法准确（时态/三单/标点）。',
  overview: '【学情分析】A班：能辨别别人文章的好坏，但给反馈时只说"写得不错"缺乏具体点。B班：改自己的稿时不知从何下手。共同问题：互评流于表面，不会用检查量表逐项给分。',
  objectives: [
    '语言能力：能根据互评量表给同伴的太空议论文初稿提具体、可操作的修改建议。',
    '文化意识：通过阅读同伴的议论文了解不同立场与论据。',
    '思维品质：在互评中培养"识别问题→提出方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步写作流程，内化为个人写作习惯。'
  ],
  keyPoints: '① 互评三维量表：结构（4段完整）+ 语言（衔接词≥2 / 不定式≥1 / 词汇多样性）+ 语法（时态/三单/标点） ② 改稿有侧重：先改结构再改语法 ③ 展示礼仪：大声/清晰/目视听众',
  difficulties: '① 学生互评时不好意思提缺点 — 需引导"给建议就是帮助对方进步"。② However 标点重复出错。③ 修改时学生只改拼写不改结构 — 需强制"先查四段是否完整"。',
  teachingMethods: '① 量表互评：用统一标准减少主观性 ② 对子互评→修改→展示 ③ 最佳议论文评选',
  preparation: '【PPT课件】P1 互评三维量表；P2 共性错误（However标点/衔接词缺/结论弱）；P3 修改指南；P4 展示礼仪；P5 最佳议论文范例；P6 写作提纲回顾；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①结构（4段都给√/缺→标出）②语言（圈衔接词≥2？不定式≥1？词汇重复？）③语法（时态？三单？However标点？）。教师用上节课自己写的范文示范打分。预设回答跟学。板书时机：量表三维板书于黑板。差异化提示：B班按量表逐项打勾即可；A班还需写一句"最需要改进的地方"。易错点提醒：互评不是打分比高低——是帮对方变得更好。' },
    { step: '起草+互评', time: '12', content: '【PPT P2 共性错误】教师：First, look at common mistakes. 先展示上节课共性错：①However标点②结论段缺"In conclusion"③反方论据缺。然后同桌互换初稿，用红笔按量表标注。教师巡视。教师：Give one praise and one suggestion. 预设回答：Your structure is good, but the conclusion is weak. 板书时机：留量表供参考。差异化提示：B班按checklist勾；A班在稿上写具体修改建议。易错点提醒：提建议时用"I suggest..."而非"You should..."——更礼貌。' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改初稿。顺序：①先补结构（缺哪段补哪段）②再加语言（插入衔接词/不定式）③最后查语法（However标点）。教师：Don\'t just fix spelling — check structure first! 预设回答：I fixed the However punctuation and added an infinitive in paragraph 2. 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色词汇替换。易错点提醒：修改不是重写——保留原文好的部分，只在薄弱处补强。' },
    { step: '展示评选', time: '8', content: '【PPT P4 展示礼仪】教师：Read loudly and look at the audience. 2-3 组自愿上台读议论文。全班投票：论据最充分的/结构最完整的/最有说服力的。预设回答展示。板书时机：留展示评分维度。差异化提示：B班可看稿读；A班尽量脱稿。易错点提醒：上台读稿不要太快——你写了100词不等于听众能消化100词。' },
    { step: '结课', time: '5', content: '【PPT P7 总结】教师：Next time you write, remember this process. 回顾写作闭环：outline→draft→peer review→revise→final。预设回答：I will make an outline first. 板书时机：画闭环流程图。差异化提示：B班齐读流程；A班说自己的收获。易错点提醒：最好的写作习惯是"先结构后语言"——不要跳跃步骤。' }
  ],
  blackboard: '┌─ U4 Writing II: Peer Review ────────┐\n│ WRITING PROCESS:                      │\n│  Outline → Draft → Peer → Revise →   │\n│  → Final → SHARE                     │\n│                                       │\n│ Review Checklist:                     │\n│  ✅ 4 paragraphs?                     │\n│  ✅ ≥2 linkers?                       │\n│  ✅ ≥1 infinitive?                    │\n│  ✅ Conclusion stance?                │\n│  ✅ Grammar (However / tense / ;)     │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改终稿，誊抄提交。自评：在稿末写 1 句"这次写作最大的进步是…" 【提高作业】就"是否应该殖民火星"写 80 词议论文，用"话题—正方—反方—结论"框架。【参考答案——教师用】参考 Writing I 的 exercises 答案。终稿评估标准：结构4段完整（2分）+衔接词≥2（2分）+不定式≥1（2分）+结论有力（2分）+语法准确（2分）= 10分。',
  reflection: '✅ 亮点：量表培训解决了"不知道评什么"的问题，B班互评质量明显提升。⚠️ 需改进：修改环节时间偏紧，下次可给15分钟。📌 下节课衔接：进入 Project，将本单元5课所学整合为太空探索展览。'
}));

// ====== Period 8: Project (太空探索展览) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u4-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '太空', '展览', '人教版必修三U4', '第八节课'],
  textbookAnalysis: '本课为必修第三册 Unit 4 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的太空词汇+阅读的"时间链"结构+语法的不定式+听与谈的辩论句型+写作的议论文——完成一份"太空探索展览"海报/展板。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确任务清单。B班：group work 中有同学"搭便车"不干活，需明确定人定责。共同问题：小组合作时语言切换回中文——需设立"英文监督员"角色。',
  objectives: [
    '语言能力：综合运用本单元词汇、不定式、辩论句型，以英文完成一份太空探索展览海报（标题/历程/成就/挑战/展望）。',
    '文化意识：通过展览形式向同伴传播太空探索的科学精神。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 海报四模块：Timeline（探索历程）→ Achievements（主要成就）→ Challenges（面临挑战）→ Future（未来展望） ② 单元知识整合：词汇/不定式/辩论句型/议论文结构 ③ 小组分工：Writer / Designer / Editor / Presenter各司其职',
  difficulties: '① 小组分工时 Editor 常没事做 — 需明确所有角色都有事。提醒：editor不是"挑错"而是"润色语言"。② 海报语言过简（仅单词无句）— 要求每板块至少2句完整英文句。③ 展示时间控制 — 1.5分钟/组，超时扣分。',
  teachingMethods: '① PBL项目式学习：以展览为驱动问题 ② 小组协作：角色分工+checklist ③ 画廊漫步：全班互评',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 海报四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师：Let\'s review. What did we learn this unit? 教师带学生回顾本单元5课：听与说（太空词汇+描述）→阅读（探索时间链+不定式）→语法（不定式定语状语）→听与谈（辩论论证）→写作（太空议论文）。预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出来。易错点提醒：每个版块至少用一次不定式——这是单元核心语法。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 海报结构】【PPT P3 角色卡】教师：Choose a space milestone and a role. 教师展示海报四模块：①Timeline（选一个里程碑+历程）②Achievements（主要成就）③Challenges（面临挑战）④Future（未来展望）。角色分工：Writer写文案 / Designer设计排版 / Editor检查语言+语法 / Presenter准备展示。预设回答：We choose the Mars mission. I am the writer. 板书时机：留模块结构和角色。差异化提示：B班给语言模板（填空式）；A班自由写。易错点提醒：Designer 也是团队一员——和 Writer 商量文案长度才能排出好看版。' },
    { step: '制作海报', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】教师：Use English! At least 2 sentences per module, 1 infinitive. 小组制作。教师要巡视提醒：①用英文！②每模块至少2句完整句 ③至少1个不定式 ④最后5分钟 Editor 检查语言。预设回答：（小组讨论制作中，教师巡视指导）板书时机：无。差异化提示：B班给句子开头提示（The mission was... / It aimed to...）；A班独立完成。易错点提醒：不要把所有内容挤在一起——留白是设计的一部分。标题要大、内容要分块。' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】教师：You have 90 seconds. Go fast but clear! 每组 1.5 分钟展示。全班投票：最佳内容/最佳设计/最佳展示。预设回答展示。板书时机：记投票结果。差异化提示：B班可看海报读；A班脱稿补充。易错点提醒：1.5分钟很短——只讲最精彩的部分，不要逐字念。' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】教师：Be honest. This is for yourself. 学生勾选四维薄弱项：词汇记不住？不定式不会用？辩论句型忘了？写作结构不熟？写1条补强计划。预设回答：I need to practice infinitives. I will review the grammar table tonight. 板书时机：留自评四维。差异化提示：B班中文写、A班英文写。易错点提醒：计划要具体到"做什么"+"什么时候"——不是"我会复习"，而是"今晚复习不定式并造5句"。' }
  ],
  blackboard: '┌─ U4 Project: Space Exploration Expo ─┐\n│ 🚀 Poster 4 Modules:                  │\n│  ① Timeline (milestones)               │\n│  ② Achievements (what was done?)       │\n│  ③ Challenges (what is hard?)          │\n│  ④ Future (what is next?)              │\n│                                       │\n│ 👥 Roles: Writer / Designer / Editor  │\n│          / Presenter                  │\n│                                       │\n│ ⭐ Must: English / ≥2 sentences per   │\n│         module / ≥1 infinitive        │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】完成小组海报（未完成的继续做），拍照片提交。写 30 词英文反思：我在小组中的贡献是…我从这个项目中学到了…【提高作业】选一个新闻中的太空任务，用英文写 50 词简报介绍历程+成就。【参考答案——教师用】反思示例：My role was the writer. I wrote the timeline and the achievements. I learned how to use infinitives to show purpose. What I can improve next time: check grammar before the deadline.',
  reflection: '✅ 亮点：海报四模块整合了全单元，学生产出有成就感。⚠️ 需改进：16分钟制作时间紧，下次可给20分钟。📌 下节课衔接：进入 Unit 5 The Value of Money，从太空探索转向金钱价值。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b3-u4-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b3-u4 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
