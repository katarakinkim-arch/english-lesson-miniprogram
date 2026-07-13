/**
 * gen-b3-u2.js — 必修第三册 Unit 2 Morals and Virtues (8课时)
 *
 * 语篇: MOTHER OF TEN THOUSAND BABIES (林巧稚医生的人生抉择与医学奉献)
 * 语法: -ing形式作宾语补足语 (see sb doing / keep sb doing / find sb doing)
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
const UNIT = 2;
const UNIT_TITLE = 'Morals and Virtues';
const BOOK = '必修第三册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u2-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '道德', '抉择', '人教版必修三U2', '第一节课'],
  textbookAnalysis: '本课为必修第三册 Unit 2 Morals and Virtues 第一课时（Listening and Speaking），属单元导入+输入环节。听力材料为一段关于道德困境（moral dilemma）的对话与独白，功能语境是"讨论生活中的道德选择"。语言重点为道德词汇（moral, virtue, dilemma, choice, principle, sacrifice, responsible, honest）及表达抉择句型（If I were..., I would... / I think it is right to... / The dilemma is...）。为本单元 Reading 的"林巧稚人生抉择"传记做词汇与话题预热。',
  overview: '【学情分析】A班：对 moral/dilemma 等抽象词较生，但能理解简单道德情境。B班：对用英语讨论道德话题开口意愿低，听力抓细节弱。共同问题：讨论道德抉择时只说"对/错"二元判断，缺乏"权衡利弊"的多角度思维。',
  objectives: [
    '语言能力：听懂关于道德困境的听力材料，提取关键信息（情境/冲突/选择/结果），准确使用 6-8 个道德核心词汇。',
    '文化意识：了解中外道德观念的共通性，体会"利他奉献"的普世价值。',
    '思维品质：通过"听前预测—听中验证—听后权衡"形成系统听力策略与辩证思维。',
    '学习能力：能用 If I were..., I would... / I think it is right to... 就道德困境做简短发言。'
  ],
  keyPoints: '① 道德核心词汇：moral / virtue / dilemma / choice / principle / sacrifice / responsible / honest ② 抉择句型：If I were..., I would... / I think it is right to... / The dilemma is... ③ 听力微技能：听前读题支预测冲突点、听中抓选择与理由。',
  difficulties: '① dilemma（困境）拼写与发音。原因：词形特殊。易错点提醒：dilemma /dɪlemə/，双 m。② sacrifice（牺牲）抽象动词，学生易与 sacred 混淆。③ 道德困境无标准答案，听力时需听出多方观点。',
  teachingMethods: '① 任务型（TBL）：以讨论一个道德困境为终任务。② 听前预测+听中填卡：信息卡脚手架。③ 对子互问操练抉择句型。',
  preparation: '【PPT课件】P1 单元封面（Morals and Virtues）；P2 道德情境图片九宫格（让座/拾金不昧/见义勇为/诚实考试/帮助陌生人/遵守承诺/孝敬父母/保护弱者/公平竞争）；P3-4 听力任务题；P5 抉择句型板；P6 说话任务卡。【实物教具】道德困境信息卡 printed 每组一套。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine pictures. They all show moral choices. Which one have you experienced? 预设回答：Giving a seat to an old person! / Returning lost money! 板书时机：右侧板书 moral / virtue / dilemma。差异化提示：B班指图说中文再跟读英文；A班用 I once... 造句。易错点提醒：moral /mɒrəl/ — m 发 /m/ 不发 /n/，与 normal 区分。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 moral / virtue / dilemma / choice / principle / sacrifice / responsible / honest。教师：What does "sacrifice" mean? 预设回答：To give up something for others. 板书时机：左栏板书词+短注释。差异化提示：B班配图记忆+词性标注；A班用词造句。易错点提醒：sacrifice /sækrɪfaɪs/ — sac 不是 sack，注意重音在第一音节。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to a story about a moral dilemma. Predict: What is the conflict? (self vs others / money vs honesty / career vs family) 预设回答：Self vs others! 板书时机：预测词写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测理由。易错点提醒：听力常见陷阱 — 角色会先说一个选择再说"but actually"推翻。' },
    { step: '听中填卡', time: '10', content: '【PPT P5 表格】【音频 段一】播放听力，学生填信息卡（情境/冲突/选择/理由）。教师：What is the dilemma? What did the person choose? 预设回答：A student found a wallet. The dilemma is keep or return. He returned it. 板书时机：核对答案时填表于黑板中部。差异化提示：B班听两遍只填情境+选择；A班一遍填全。易错点提醒：principle /prɪnsɪpəl/ — 与 principal（校长）同音，需语境区分。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to express a moral choice? If I were..., I would... / I think it is right to... / The dilemma is... 教师示范后用一个情境造句。预设回答：If I were the student, I would return the wallet because honesty is a virtue. 板书时机：句型板书于中央。差异化提示：B班套用模板；A班替换情境+理由。易错点提醒：If I were 是虚拟语气，用 were 不用 was。' },
    { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，从信息卡中选一个道德困境互讨。教师：Discuss a moral dilemma with your partner. Use the sentence patterns. 预设回答：The dilemma is whether to tell the truth. If I were her, I would be honest. 板书时机：无。差异化提示：B班用填空式对话卡；A班自由讨论并追问理由。易错点提醒：whether（是否）与 weather（天气）同音，写作注意区分。' }
  ],
  blackboard: '┌─ U2 Listening & Speaking ──────┐\n│ moral / virtue / dilemma         │\n│ choice / principle / sacrifice   │\n│ responsible / honest             │\n│                                  │\n│ If I were..., I would...         │\n│ I think it is right to...        │\n│ The dilemma is...                │\n│                                  │\n│ Dilemma Card:                    │\n│  wallet | keep/return | honesty  │\n└──────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有道德词汇。2. 用 If I were..., I would... 写 3 句道德抉择。【提高作业】用英文写一段 50 词：描述一个你遇到或听说的道德困境，包含情境/冲突/你的选择/理由。【参考答案——教师用】基础2示例：If I were the student, I would return the wallet. / If I were the doctor, I would save the patient first. / If I were the witness, I would tell the truth.',
  reflection: '✅ 亮点：九宫格激活+信息卡脚手架有效降听力焦虑，B班填卡完成率高。⚠️ 需改进：sacrifice 发音仍有困难，下节需强化。📌 下节课衔接：进入阅读 MOTHER OF TEN THOUSAND BABIES，从道德困境延伸到林巧稚的人生抉择。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u2-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '道德', '传记', '林巧稚', '人教版必修三U2', '第二节课'],
  textbookAnalysis: '本课为必修第三册 Unit 2 第二课时（Reading I），语篇 MOTHER OF TEN THOUSAND BABIES 是一篇人物传记，讲述"万婴之母"林巧稚医生的人生抉择——放弃婚姻与留学机会，将一生奉献给妇产科事业，接生近五万婴儿。结构为背景引入→人生关键抉择（留学/婚姻/抗战/新中国）→奉献精神升华。语言重点为传记衔接词（however, instead, after all）与道德主题词汇（sacrifice, principle, responsible, devote, deliver, reject）。承接第一课时词汇，本课语篇中出现 -ing 形式作宾语补足语。',
  overview: '【学情分析】A班：能快速把握段落主旨，但对"个人牺牲vs社会奉献"的辩证思维训练不足。B班：对林巧稚历史背景了解少，需时间线+图片脚手架。共同问题：传记的"抉择链"结构感知不清晰，易忽略 however/instead 等转折标志词。',
  objectives: [
    '语言能力：读懂人物传记，提取林巧稚人生关键抉择的时间线/动机/结果；掌握 8-10 个论述类核心词汇。',
    '文化意识：理解林巧稚"医者仁心"的奉献精神，形成"个人价值与社会责任"的辩证观念。',
    '思维品质：通过"抉择链"分析培养传记结构思维与价值判断能力。',
    '学习能力：能用时间轴+抉择表复述林巧稚的人生主线。'
  ],
  keyPoints: '① 传记结构：background → choices (study/marriage/war/new China) → devotion → legacy ② 时间线词汇：in 1901 / as a young girl / instead / after all ③ 核心短语：devote... to... / give up / carry sb through / tend to',
  difficulties: '① sacrifice（牺牲）在文中的具体含义——林巧稚牺牲了婚姻而非生命。原因：学生易泛化理解。② devote... to...（致力于）的 to 是介词后接 doing。③ reject（拒绝）与 refuse 的区别——reject 更强调"主动排斥"。',
  teachingMethods: '① 时间轴阅读：构建林巧稚人生抉择进程。② 抉择链追问：每个抉择问"为什么/放弃了什么/结果如何"。③ 价值讨论：个人vs社会。',
  preparation: '【PPT课件】P1 林巧稚照片与协和医院；P2 时代背景时间线（1901-1983）；P3-4 抉择链表；P5 传记结构图；P6 词汇对比表；P7 总结回顾。【实物教具】时间轴空白工作单 printed 每人一份；段落拼图卡。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P1 林巧稚照片】教师：This is Dr. Lin Qiaozhi. She delivered over 50,000 babies but never married. Why? What choices did she make? 预设回答：Because she devoted her life to medicine? 板书时机：板书 choices? + 三个问号。差异化提示：B班中文猜；A班英文猜并给理由。易错点提醒：deliver /dɪlɪvə/ 在文中表"接生"，不是"递送"。' },
    { step: '快速阅读抓主干', time: '8', content: '【PPT P3 时间轴】教师：Read fast (3 min). Find: ① What were her major life choices? ② What did she give up? ③ What was her legacy? 预设回答：① She chose medicine over marriage. ② She gave up studying abroad and a family. ③ She saved many mothers and babies. 板书时机：填时间轴的三个关键抉择。差异化提示：B班给三选一选项；A班写完整句。易错点提醒：physician /fɪzɪʃən/ — ph 发 /f/，不是 /p/。' },
    { step: '精读段落1-3 背景与早期抉择', time: '10', content: '【PPT P4 抉择表】教师精讲：devote... to... = 致力于；give up = 放弃；carry sb through = 支撑某人度过。教师：Why did she choose medicine? 预设回答：Because her mother died and she wanted to help women. 板书时机：左侧栏补充"devote to / give up / carry through"。差异化提示：B班读后填关键词；A班读后用自己话解释。易错点提醒：devote to 中 to 是介词，后接 doing — "devoted to serving" 不是 "devoted to serve"。' },
    { step: '精读段落4-5 奉献与精神', time: '10', content: '【PPT P5 行动链】教师：What did she do during the war? And after new China? 学生填表匹配（war period / new China / retirement → actions）。教师：How did she show her devotion? 预设回答：She opened a clinic during the war. She worked until she died. 板书时机：右侧画行动链箭头图。差异化提示：B班连线匹配；A班写完整句。易错点提醒：tend to（照料）中的 to 是介词，后接 doing 或名词。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 传记结构】教师：What can we learn from Dr. Lin? (sacrifice for others / devotion to duty / principle over personal gain) 预设回答：She sacrificed personal happiness for the greater good. We should be responsible. 板书时机：圈出结构关键词。差异化提示：B班跟读关键词；A班用自己的话总结。易错点提醒：greater good（更大的善）不是"更大的好"而是"集体利益"。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾"背景→抉择→奉献→精神"结构+核心词汇。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：devotion /dɪvəʊʃən/ — 与 devotion（忠诚）同词，注意语境。' }
  ],
  blackboard: '┌─ U2 Reading I: MOTHER OF TEN THOUSAND ─┐\n│ BACKGROUND → CHOICES → DEVOTION → LEGACY │\n│                                          │\n│ Choices: medicine/marriage/war/retire    │\n│ Sacrifice: family, abroad, personal life │\n│ Legacy: 50,000 babies, medical ethics    │\n│                                          │\n│ devote to / give up / carry through      │\n│ tend to / reject / principle             │\n└──────────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-3段 2 遍，圈出所有转折词（however/instead/after all）。2. 用时间轴上的3个关键抉择各写1句事件描述。【提高作业】用 80 词左右写一段：你认为林巧稚最艰难的抉择是什么？为什么？（用 sacrifice / devote to / principle）【参考答案——教师用】基础2示例：As a young girl, she chose to study medicine. / Instead of marrying, she devoted her life to women\'s health. / During the war, she opened a clinic to tend to the poor.',
  reflection: '✅ 亮点：时间轴+抉择链表有效组织信息，B班完成率高。⚠️ 需改进：devote to 后接 doing 学生仍感吃力。📌 下节课衔接：进入精读语言+-ing 形式作宾语补足语在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u2-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '-ing宾补', '道德', '人教版必修三U2', '第三节课'],
  textbookAnalysis: '本课为必修第三册 Unit 2 第三课时（Reading II），聚焦语篇 MOTHER OF TEN THOUSAND BABIES 的精读与语言分析。重点分析文中 -ing 形式作宾语补足语（saw her mother suffering / kept her working / found people waiting）在传记中的功能——补充宾语的状态，使描写更生动。同时深化语篇中高频学术词汇的用法辨析（devote / reject / tend / deliver / sacrifice）。',
  overview: '【学情分析】A班：能识别 -ing 形式，但辨析其作宾语补足语还是其他功能仍有困难。B班：-ing 宾补概念感模糊，需大量语境例句支撑。共同问题：阅读中见到 -ing 结构会跳过不分析其功能——学生把 -ing 当"进行时一部分"而非"独立语法工具"。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 5 个 -ing 形式作宾语补足语的用法，准确辨析功能。',
    '文化意识：通过 -ing 宾补体会英语如何用简洁结构描写人物状态——不同于中文的习惯。',
    '思维品质：分析 -ing 宾补在传记中的"状态补充"功能，培养语法服务于意义的意识。',
    '学习能力：建立"从读到写"的语料库——积累课文中的优质 -ing 宾补句型用于后续写作。'
  ],
  keyPoints: '① 语篇中 -ing 作宾语补足语（see sb doing / keep sb doing / find sb doing / leave sb doing）② 传记高频动词：devote / reject / tend / deliver / sacrifice ③ -ing 宾补在传记中的修辞功能：补充状态→增强画面感',
  difficulties: '① -ing 宾补 vs 进行时的辨析。原因：形同功不同，需看句法位置。② reject（拒绝）与 refuse 的语感差异。③ tend（照料）与 tend to（倾向于）的区分 — 学生易混淆。',
  teachingMethods: '① 标注法：圈出文中所有 -ing 宾补结构并分析功能。② 替换练习：改写简单句为 -ing 宾补。③ 语料卡记录：分类摘录优质句子。',
  preparation: '【PPT课件】P1-2 课文中圈出的 -ing 宾补示例；P3 宾补结构对比表；P4 语料卡模板；P5 词汇辨析表；P6 句型改写练习；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 结构图】教师：Last class we learned Dr. Lin\'s life choices. Can you recall the key events? 预设回答：She chose medicine. She gave up marriage. She delivered 50,000 babies. 板书时机：左栏写 1901/study/war/new China 时间线。差异化提示：B班看时间轴读关键词；A班完整复述。易错点提醒：recall ≠ remember — recall 更强调"主动调取记忆"。' },
    { step: '-ing 宾补发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle all -ing forms after verbs like see/keep/find/leave. Decide what they describe. 学生标记后全班核对。教师：What does this -ing describe? 预设回答：It describes what the object is doing — it\'s an object complement. 板书时机：逐句板书圈出的 -ing 宾补结构。差异化提示：B班给划线句直接圈 -ing；A班自己找+标注功能。易错点提醒："saw her mother suffering" 中 suffering 补充说明 mother 的状态，是宾补不是进行时。' },
    { step: '宾补结构辨析', time: '10', content: '【PPT P3 对比表】教师对比：宾补——补充宾语状态（see sb doing / keep sb doing / find sb doing / leave sb doing）；进行时——谓语动词（She is working）。教师例句辨析。预设回答辨析。板书时机：两列对比板书。差异化提示：B班根据提示选择填空；A班独立造句。易错点提醒：see sb do（看见全过程）vs see sb doing（看见正在进行）——含义不同。' },
    { step: '语料库搭建', time: '10', content: '【PPT P4 模板】教师：Build your corpus. Categorize -ing complement sentences and key verbs. 学生分类填语料卡：①-ing 宾补优质句摘录 ②传记动词（devote/reject/tend/deliver/sacrifice）③转折衔接词。板书时机：巡视指导。差异化提示：B班填词；A班造句。预设回答：按道德主题语料库模板分类填写词条。易错点提醒：deliver 在文中表"接生"，与 deliver a speech（演讲）同词多义。' },
    { step: '句型改写', time: '5', content: '【PPT P6 练习】教师：Combine these sentences using -ing complement. 例：She was working. I saw her. → I saw her working. 预设回答造句。板书时机：板书改写公式。差异化提示：B班给改写框架；A班独立改。易错点提醒：合并后宾语+suffering/working 构成"宾语+宾补"结构，不要加 that。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】教师：Let\'s review -ing as object complement. 回顾 -ing 宾补功能+语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课深入讲 -ing 宾补的动词搭配规则。' }
  ],
  blackboard: '┌─ U2 Reading II: Language Focus ──────┐\n│ -ing as Object Complement (宾补):      │\n│  see sb doing (看见...正在做)           │\n│  keep sb doing (让...一直做)            │\n│  find sb doing (发现...正在做)          │\n│  leave sb doing (让...持续做)           │\n│                                        │\n│ Verbs: devote / reject / tend          │\n│        deliver / sacrifice             │\n│                                        │\n│ see sb do (全过程) vs see sb doing     │\n│        (正在进行)                       │\n└────────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出5个 -ing 宾补结构并标注动词+宾语。2. 将以下两句合并为 -ing 宾补：She was crying. I found her.【提高作业】用 -ing 宾补写3句描述一个医生工作的场景（用 see/find/keep）。【参考答案——教师用】基础2示例：I found her crying.',
  reflection: '✅ 亮点：标注发现法让学生主动探索语法，参与度高。⚠️ 需改进：see sb do vs see sb doing 区分仍有混淆，语法课需强化。📌 下节课衔接：进入语法课，系统讲 -ing 作宾语补足语的规则。'
}));

// ====== Period 4: Grammar (-ing形式作宾语补足语) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u2-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '-ing形式', '宾语补足语', '道德', '人教版必修三U2', '第四节课'],
  textbookAnalysis: '本课为必修第三册 Unit 2 第四课时（Discovering Useful Structures），系统教学 -ing 形式作宾语补足语的用法。基于 Reading 语篇中提取的例句，引导学生归纳出规则：常跟 -ing 宾补的动词（see/watch/hear/notice/observe 感官动词；keep/leave/find/send 使役状态动词）。-ing 宾补强调动作正在进行。通过道德主题的语境化练习巩固。',
  overview: '【学情分析】A班：知道 -ing 表进行时，但作宾补是语法新知。B班：-ing 宾补概念仍模糊，需大量语境化例句反复操练。共同问题：写作中要么不用 -ing 宾补，要么与 see sb do 混淆。',
  objectives: [
    '语言能力：准确识别并产出 -ing 形式作宾语补足语的句子，在道德主题话题中产出 5 个以上正确句子。',
    '文化意识：通过 -ing 宾补更生动地描写人物的行为状态。',
    '思维品质：通过"发现例句→归纳规则→应用规则"的归纳法培养语法学习策略。',
    '学习能力：建立"语法自查表"——写作后自行检查 -ing 宾补的动词搭配是否正确。'
  ],
  keyPoints: '① 感官动词+宾补：see/watch/hear/notice/observe sb doing ② 使役状态动词+宾补：keep/leave/find/send sb doing ③ -ing 宾补（正在进行）vs do 宾补（全过程）的区别',
  difficulties: '① see sb doing vs see sb do 的区别。原因：形近意不同。② keep sb doing（让…一直做）中 keep 的使役用法。③ -ing 宾补与 -ing 状语的辨析——位置和功能不同。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习 ② 改写对比：see sb do vs see sb doing ③ 改错练习：纠正典型错误',
  preparation: '【PPT课件】P1 感官vs使役动词对比表；P2 课文例句摘录；P3 规则归纳页；P4 do vs doing 对比；P5 改写任务卡；P6 改错题；P7 总结。【实物教具】句型卡一套；改写工作单。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中5个 -ing 宾补结构，学生圈动词+宾语+-ing。教师：What verb comes before -ing? What does -ing describe? 预设回答：The verb is see/keep/find. The -ing describes the object\'s action. 板书时机：左栏板书例句，标注动词+宾语+-ing。差异化提示：B班只圈词不分析功能；A班分析 -ing 补充什么。易错点提醒：-ing 宾补紧跟在宾语之后，补充说明宾语正在做什么。' },
    { step: '规则归纳', time: '12', content: '【PPT P3 对比表】教师引导学生归纳两类动词：①感官动词 see/watch/hear/notice/observe sb doing ②使役状态动词 keep/leave/find/send sb doing。教师：When do we use -ing after these verbs? 预设回答：When the action is happening — in progress! 板书时机：板书完整两类动词对比表。差异化提示：B班填已给框架表；A班自己画表填。易错点提醒：keep sb doing 表"让某人一直做"，强调持续——"keep me waiting"（让我一直等）。' },
    { step: 'do vs doing 讲练', time: '8', content: '【PPT P4 结构】教师：see sb do = 看见全过程（已结束）；see sb doing = 看见正在进行（未结束）。例句：I saw her cross the street. (全过程) / I saw her crossing the street. (正在进行) 预设回答辨析：第一句强调看完整个过马路，第二句强调路过时看到。板书时机：板书 do vs doing 对比公式。差异化提示：B班选词填空（do/doing）；A班改写句子。易错点提醒：hear sb do（听见全过程）vs hear sb doing（听见正在发生）——同理。' },
    { step: '改写操练', time: '8', content: '【PPT P5 改写卡】教师：Combine the sentences using -ing complement. 例：The doctor was working. I watched her. → I watched the doctor working. 教师抽学生板演。预设回答造句。板书时机：板书改写公式。差异化提示：B班给句型框；A班自由改写并追加道德主题细节。易错点提醒：改写后检查——宾语+-ing 构成宾补，不要加 that 或 who。' },
    { step: '改错巩固', time: '3', content: '【PPT P6 改错】教师：Find the mistakes. 展示 3 个典型错误：①I saw him to run.（应去掉 to）②She kept me wait.（应 waiting）③I found that he was reading a book → I found him reading a book.（简化）。学生纠错并解释。预设回答纠错。板书时机：板书错误→改正公式。差异化提示：B班辨别对错选；A班解释为什么错。易错点提醒：最常犯——感官动词后加 to do（错），应为 do 或 doing。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Let\'s review. 回顾 -ing 宾补两类动词+do vs doing+改错要诀。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述规则。易错点提醒：写作后自查——感官/使役动词后宾补是否用了 -ing？' }
  ],
  blackboard: '┌─ U2 Grammar: -ing as Object Complement ───┐\n│ 感官动词:                                   │\n│  see/watch/hear/notice/observe sb doing     │\n│ 使役状态动词:                               │\n│  keep/leave/find/send sb doing              │\n│                                             │\n│ see sb do (全过程) vs see sb doing (进行)   │\n│ hear sb do vs hear sb doing                 │\n│                                             │\n│ ⚠️ No "to" after sense verbs!               │\n│ ✗ I saw him to run. → ✓ I saw him running.  │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 用 see/find/keep + sb doing 各造 2 句关于医生工作的句子。2. 将以下两句合并为 -ing 宾补：The nurse was caring for patients. I watched her.【提高作业】写 60 词短文描述一次医院见闻，要求至少用 3 个 -ing 宾补结构。【参考答案——教师用】基础1示例：I saw the doctor operating on a patient. / I found the nurse caring for a baby. / The long shift kept her working all night. 基础2示例：I watched the nurse caring for patients.',
  reflection: '✅ 亮点：改写对比让语法操练不再枯燥，课堂活跃度高。⚠️ 需改进：do vs doing 区分仍是难点，听与谈课可融入练习。📌 下节课衔接：听与谈聚焦道德情境讨论，用语篇巩固 -ing 宾补。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u2-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '道德情境', '讨论', '人教版必修三U2', '第五节课'],
  textbookAnalysis: '本课为必修第三册 Unit 2 第五课时（Listening and Talking），语境为"讨论道德伦理情境"。听力材料为一段关于诚信/责任/利他等伦理场景的讨论对话，口语输出任务为就一个道德情境做辩论与表态。功能语言为表达观点与权衡（I believe... / On one hand... / On the other hand... / It depends on...）。结合语法课所学的 -ing 宾补，在口语中自然运用描述他人行为状态。',
  overview: '【学情分析】A班：能表达简单观点，但缺乏"正反权衡"的辩证表达链。B班：开口意愿低、辩证句型储备少。共同问题：只说观点不权衡，缺少 On the other hand... 使表达片面。',
  objectives: [
    '语言能力：听懂关于道德情境讨论的对话，提取观点与理由；能用至少 4 种句型表达观点并权衡。',
    '文化意识：体会"道德选择需要权衡利弊"的理性思辨精神。',
    '思维品质：在讨论中练习"表态→正方→反方→结论"的完整对话链。',
    '学习能力：通过辩论对话训练批判性倾听——听懂后回应而非只等自己说。'
  ],
  keyPoints: '① 观点句型：I believe... / In my opinion... / I think it is right to... ② 权衡句型：On one hand... / On the other hand... / It depends on... / However... ③ 听力重点：抓住观点+理由的配对信息',
  difficulties: '① On one hand... On the other hand... 是权衡不是对立 — 学生易理解为完全对立。原因：母语干扰。② depend on（取决于）的介词 on 易漏。③ 回应时 only say "I agree" no weighing — 需培养 However 跟进的意识。',
  teachingMethods: '① 听前预测→听中配对→听后产出 ② 角色扮演：三人一组（支持者+反对者+中立方）③ 道德情境辩论圆桌',
  preparation: '【PPT课件】P1 待讨论道德情境（诚信考试/见义勇为/帮助陌生人）；P2 观点句型板；P3 听力任务题；P4 听力任务卡；P5 权衡句型板；P6 角色卡。【实物教具】道德情境建议卡 printed；角色卡。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 道德情境】教师：Your friend is cheating in an exam. You saw him cheating. What should you do? 预设回答：Tell the teacher! / Pretend not to see. 板书时机：左栏板书动词 tell / report / ignore / confront。差异化提示：B班中文说再翻英文；A班直接英文。易错点提醒：cheat（作弊）≠ cheat on（对…不忠），语境区分。' },
    { step: '听力抓观点', time: '10', content: '【PPT P3 听力任务】听对话，抓"谁持什么观点+什么理由"。教师：Listen for: What is the opinion? What is the reason? 预设回答：She believes honesty matters because trust is the foundation. 板书时机：配对填表（观点|理由）。差异化提示：B班给配对连线题；A班听写关键词。易错点提醒：listen for（有目的地听）≠ listen to（泛听）——引导学生带问题听。' },
    { step: '听中记录', time: '8', content: '【PPT P4 听力任务卡】【音频】重听，学生填完整观点+权衡链。教师：How did they weigh both sides? 预设回答：On one hand, honesty matters. On the other hand, friendship matters too. 板书时机：核对填表。差异化提示：B班听两遍；A班一遍+复述权衡。易错点提醒：On the other hand 中的 the 不可省——固定搭配。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练观点+权衡链：A: I believe we should tell the truth. / B: On one hand, honesty matters. On the other hand, friendship is important too. / A: It depends on the situation. 预设回答跟读+仿造。板书时机：板书观点→权衡链条。差异化提示：B班用填空脚本；A班自主对话。易错点提醒：depend on 后接 doing 或名词 — "depends on the situation" 不是 "depends the situation"。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】三人一组：Supporter A（支持者）、Opponent B（反对者）、Mediator C（中立方）。就"是否应该举报朋友作弊"辩论。教师巡视。预设回答：A: I believe we should report it. / B: On the other hand, he is my friend. / C: It depends on whether it\'s the first time. 板书时机：留观点句型和权衡链供参考。差异化提示：B班照卡读；A班脱稿加即兴内容。易错点提醒：角色扮演中注意用 -ing 宾补描述行为 — "I saw him copying answers."' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Remember to weigh both sides. 回顾观点句型+权衡策略。预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一句收获。易错点提醒：给观点后记得加"on the other hand"——辩证才完整。' }
  ],
  blackboard: '┌─ U2 Listening & Talking ─────────┐\n│ Opinions:                          │\n│  I believe...                      │\n│  In my opinion...                  │\n│  I think it is right to...         │\n│                                    │\n│ Weighing:                          │\n│  On one hand...                    │\n│  On the other hand...              │\n│  It depends on...                  │\n│  However...                        │\n│                                    │\n│ Chain: Opinion → Pro → Con → Concl │\n└────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有观点句型。2. 用至少 2 种观点句型各写 1 句道德表态+权衡。【提高作业】写 60 词对话：三人讨论"是否应该帮助摔倒的陌生人"（至少 4 轮，含观点与权衡）。【参考答案——教师用】基础2示例：I believe we should help. On one hand, kindness matters. On the other hand, we must protect ourselves. / In my opinion, it depends on the situation.',
  reflection: '✅ 亮点：角色扮演三角色设置让学生理解真实辩论中的多元声音。⚠️ 需改进：On the other hand 使用率仍需提高，写作课可设置强制格式。📌 下节课衔接：进入写作，将道德困境写成记叙文。'
}));

// ====== Period 6: Writing I (结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u2-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '记叙文', '道德困境', '人教版必修三U2', '第六节课'],
  textbookAnalysis: '本课为必修第三册 Unit 2 第六课时（Reading for Writing I），写作体裁为记叙文——写一次道德困境经历。结构为：背景设定（when/where/who）→ 困境冲突（what was the dilemma）→ 抉择经过（what did you do, in order）→ 感悟升华（what you learned）。语言重点为记叙文时间连接词（first, then, after that, finally）与道德描写词（honest, responsible, sacrifice, principle）。结合本单元 Reading 的抉择精神与语法课的 -ing 宾补，实现读-语法-写的闭环。',
  overview: '【学情分析】A班：有基本叙事能力，但缺乏"冲突→抉择→感悟"的升华意识——常写成流水账。B班：句型储备少、时态混乱，需大量脚手架。共同问题：记叙文不知如何收尾——缺少"这次经历让我明白…"的感悟句。',
  objectives: [
    '语言能力：掌握"背景—困境—抉择—感悟"四段式记叙文结构，在道德困境话题中产出 80-100 词结构完整的短文。',
    '文化意识：通过书写道德抉择体会"诚信/责任/利他"的道德价值。',
    '思维品质：通过"先叙事再感悟"训练事件—冲突—抉择—意义的递进逻辑思维。',
    '学习能力：建立"写作前先搭结构框架"的习惯——用 outline 而非直接开写。'
  ],
  keyPoints: '① 记叙文四段结构：Background (when/where/who) → Dilemma (what was the conflict) → Choice (what did you do) → Reflection (what you learned) ② 时间连接词：First / Then / After that / Finally ③ 核心句型：I was faced with... / I decided to... / It taught me that...',
  difficulties: '① 记叙文时态——主体用过去时，感悟升华可用现在时。原因：学生易全文现在时。② dilemma 描写要具体——不能只说"很难"。③ 感悟升华句不知道怎么写——需给模板。',
  teachingMethods: '① 范文解构法：读范文→画结构图→仿写 ② 语料卡搭建：从本单元5课积累词汇/句型。③ 过程写作：outline→draft→peer review→revise',
  preparation: '【PPT课件】P1 范文（关于一次诚信考验的记叙文）；P2 四段结构图；P3 时间连接词表；P4 语料库模板；P5 写作提纲；P6 写作任务；P7 总结。【实物教具】四段结构空白工作单 printed 每人一份；语料卡模板。',
  process: [
    { step: '范文解构', time: '8', content: '【PPT P1 范文】教师展示范文，学生标注四段（背景/困境/抉择/感悟）。教师：Which paragraph describes the dilemma? Which tells the lesson? 预设回答：Paragraph 2 — the dilemma. Paragraph 4 — the lesson. 板书时机：画四段结构框。差异化提示：B班给标注好的范文只匹配段号；A班自己画结构+标注连接词。易错点提醒：最后一段必须有"It taught me that..."才算完整升华。' },
    { step: '四段结构讲透', time: '8', content: '【PPT P2 结构图】教师逐段讲解：P1 2句设定背景（when/where/who）→ P2 2句描述困境（what was the conflict）→ P3 3-4句叙述抉择经过（first/then/finally）→ P4 2句写感悟（what you learned）。教师示范写一段。预设回答跟读结构要点。板书时机：逐段板书模板句。差异化提示：B班给每段填空模板；A班给关键词自己写。易错点提醒：P2 的困境要具体 — 不要只说"it was hard"，要说"I was torn between honesty and friendship."' },
    { step: '连接词+句型', time: '5', content: '【PPT P3 词表】教师领读时间连接词：First / Then / After that / Finally / At last。教师示例句：First, I found the wallet. Then, I hesitated. After that, I decided to return it. Finally, the owner thanked me. 预设回答跟读。板书时机：板书连接词于侧栏。差异化提示：B班选词填空；A班用全级连接词写一段。易错点提醒：after that 后接逗号 — "After that, I..." 不是 "After that I..."' },
    { step: '积语料', time: '5', content: '【PPT P4 语料库】教师：Build your word bank. Extract moral verbs, dilemma words, and -ing patterns. 学生从本单元5课中提取：①道德动词（sacrifice/devote/reject/tend）②困境描写词（torn/conflicted/hesitate）③-ing 宾补模板（I saw him... / I found her...）。板书时机：巡视。差异化提示：B班填词；A班造句。预设回答：按道德主题语料库分类卡填写词条。易错点提醒：同一意思用不同词替换避免重复——第一段说 hard，第三段说 difficult / challenging。' },
    { step: '提纲+起草', time: '10', content: '【PPT P5 写作提纲】选一次道德困境经历，写 80 词记叙文 outline（四段各写关键词）。教师巡视指导 outline。教师：Don\'t write sentences yet — just key words. 预设回答：P1: last exam / classroom / me / P2: found wallet / keep or return / P3: hesitated / returned / thanked / P4: honesty matters. 板书时机：留结构框供参考。差异化提示：B班用填空 outline；A班独立列提纲。易错点提醒：outline 不是草稿——用短语不是完整句。这是写前最重要的一步。' },
    { step: '互评提纲', time: '4', content: '【PPT P6 写作任务】同桌互换提纲，检查：四段都有吗？困境段具体吗？感悟段有升华句吗？教师：Your partner\'s outline: does it have all 4 parts? 预设回答：Yes, but the reflection is too short. 板书时机：留 checklist。差异化提示：B班用 checklist 表逐项打勾；A班口头给改进建议。易错点提醒：互评不是挑刺——给一个赞美+一个建议。"Good outline! Maybe add a lesson sentence in paragraph 4."' }
  ],
  blackboard: '┌─ U2 Writing: Moral Dilemma Story ────┐\n│ P1 Background: Last..., at..., with...│\n│ P2 Dilemma: I was torn between...     │\n│ P3 Choice: First,... Then,... Finally │\n│ P4 Reflection: It taught me that...   │\n│                                       │\n│ Linkers: First / Then / After that    │\n│         Finally / At last             │\n│                                       │\n│ Word Bank: sacrifice / devote / reject│\n│  torn / conflicted / hesitate / honest│\n└───────────────────────────────────────┘',
  exercises: '【基础作业】按课堂 outline 写完 80 词道德困境记叙文初稿。要求：四段结构完整、至少 2 个时间连接词、至少 1 个 -ing 宾补。【提高作业】就同一困境写一则 30 词以内的反思语（英文），要求有哲理性有感染力。【参考答案——教师用】基础示例（节选）：Last week, I was faced with a dilemma. I found a wallet in the classroom. I was torn between keeping it and returning it. First, I hesitated. Then, I thought about the owner. After that, I decided to return it. Finally, the owner thanked me warmly. It taught me that honesty is always the right choice.',
  reflection: '✅ 亮点：四段结构框架让学生从"不知道写什么"变为"知道每段写什么"。⚠️ 需改进：时态混用仍需纠正，下节课用改错题强化。📌 下节课衔接：进入写作 II，互评修改+誊抄终稿。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u2-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '道德', '人教版必修三U2', '第七节课'],
  textbookAnalysis: '本课为必修第三册 Unit 2 第七课时（Writing II），在 Writing I 提纲+初稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进写作的能力。互评量表聚焦三维度：结构完整（4段）、语言质量（连接词/-ing 宾补/词汇）、语法准确（时态/三单/标点）。',
  overview: '【学情分析】A班：能辨别别人文章的好坏，但给反馈时只说"写得不错"缺乏具体点。B班：改自己的稿时不知从何下手。共同问题：互评流于表面，不会用检查量表逐项给分。',
  objectives: [
    '语言能力：能根据互评量表给同伴的道德记叙文初稿提具体、可操作的修改建议。',
    '文化意识：通过阅读同伴的道德经历了解不同价值取向。',
    '思维品质：在互评中培养"识别问题→提出方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步写作流程，内化为个人写作习惯。'
  ],
  keyPoints: '① 互评三维量表：结构（4段完整）+ 语言（连接词≥2 / -ing宾补≥1 / 词汇多样性）+ 语法（时态/三单/标点） ② 改稿有侧重：先改结构再改语法 ③ 展示礼仪：大声/清晰/目视听众',
  difficulties: '① 学生互评时不好意思提缺点 — 需引导"给建议就是帮助对方进步"。② 时态混用重复出错——主体过去时，感悟现在时。③ 修改时学生只改拼写不改结构 — 需强制"先查四段是否完整"。',
  teachingMethods: '① 量表互评：用统一标准减少主观性 ② 对子互评→修改→展示 ③ 最佳记叙文评选',
  preparation: '【PPT课件】P1 互评三维量表；P2 共性错误（时态混用/连接词缺/升华弱）；P3 修改指南；P4 展示礼仪；P5 最佳记叙文范例；P6 写作提纲回顾；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①结构（4段都给√/缺→标出）②语言（圈连接词≥2？-ing宾补≥1？词汇重复？）③语法（时态？三单？标点？）。教师用上节课自己写的范文示范打分。预设回答跟学。板书时机：量表三维板书于黑板。差异化提示：B班按量表逐项打勾即可；A班还需写一句"最需要改进的地方"。易错点提醒：互评不是打分比高低——是帮对方变得更好。' },
    { step: '起草+互评', time: '12', content: '【PPT P2 共性错误】教师：First, look at common mistakes. 先展示上节课共性错：①时态混用②感悟段缺"It taught me"③连接词缺。然后同桌互换初稿，用红笔按量表标注。教师巡视。教师：Give one praise and one suggestion. 预设回答：Your structure is good, but the tense is mixed. 板书时机：留量表供参考。差异化提示：B班按checklist勾；A班在稿上写具体修改建议。易错点提醒：提建议时用"I suggest..."而非"You should..."——更礼貌。' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改初稿。顺序：①先补结构（缺哪段补哪段）②再加语言（插入连接词/-ing宾补）③最后查语法（时态统一）。教师：Don\'t just fix spelling — check structure first! 预设回答：I fixed the tense and added an -ing complement in paragraph 3. 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色词汇替换。易错点提醒：修改不是重写——保留原文好的部分，只在薄弱处补强。' },
    { step: '展示评选', time: '8', content: '【PPT P4 展示礼仪】教师：Read loudly and look at the audience. 2-3 组自愿上台读记叙文。全班投票：最感人的抉择/结构最完整的/最有哲理性的。预设回答展示。板书时机：留展示评分维度。差异化提示：B班可看稿读；A班尽量脱稿。易错点提醒：上台读稿不要太快——你写了100词不等于听众能消化100词。' },
    { step: '结课', time: '5', content: '【PPT P7 总结】教师：Next time you write, remember this process. 回顾写作闭环：outline→draft→peer review→revise→final。预设回答：I will make an outline first. 板书时机：画闭环流程图。差异化提示：B班齐读流程；A班说自己的收获。易错点提醒：最好的写作习惯是"先结构后语言"——不要跳跃步骤。' }
  ],
  blackboard: '┌─ U2 Writing II: Peer Review ────────┐\n│ WRITING PROCESS:                      │\n│  Outline → Draft → Peer → Revise →   │\n│  → Final → SHARE                     │\n│                                       │\n│ Review Checklist:                     │\n│  ✅ 4 paragraphs?                     │\n│  ✅ ≥2 linkers?                       │\n│  ✅ ≥1 -ing complement?               │\n│  ✅ Reflection sentence?              │\n│  ✅ Grammar (tense / 3rd p / ;)       │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改终稿，誊抄提交。自评：在稿末写 1 句"这次写作最大的进步是…" 【提高作业】调查另一个道德困境案例（可基于新闻），用"背景—困境—抉择—感悟"框架写 80 词记叙文。【参考答案——教师用】参考 Writing I 的 exercises 答案。终稿评估标准：结构4段完整（2分）+连接词≥2（2分）+-ing宾补≥1（2分）+升华有力（2分）+语法准确（2分）= 10分。',
  reflection: '✅ 亮点：量表培训解决了"不知道评什么"的问题，B班互评质量明显提升。⚠️ 需改进：修改环节时间偏紧，下次可给15分钟。📌 下节课衔接：进入 Project，将本单元5课所学整合为道德楷模展览。'
}));

// ====== Period 8: Project (道德楷模展览) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u2-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '道德', '展览', '人教版必修三U2', '第八节课'],
  textbookAnalysis: '本课为必修第三册 Unit 2 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的道德词汇+阅读的"抉择链"结构+语法的 -ing 宾补+听与谈的辩论句型+写作的记叙文——完成一份"道德楷模展览"海报/展板。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确任务清单。B班：group work 中有同学"搭便车"不干活，需明确定人定责。共同问题：小组合作时语言切换回中文——需设立"英文监督员"角色。',
  objectives: [
    '语言能力：综合运用本单元词汇、-ing 宾补、辩论句型，以英文完成一份道德楷模展览海报（标题/简介/抉择/精神/感悟）。',
    '文化意识：通过展览形式向同伴传播道德楷模的奉献精神。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 海报四模块：Figure Introduction（楷模简介）→ Dilemma（关键抉择）→ Spirit（精神品质）→ Reflection（你的感悟） ② 单元知识整合：词汇/-ing 宾补/辩论句型/记叙文结构 ③ 小组分工：Writer / Designer / Editor / Presenter各司其职',
  difficulties: '① 小组分工时 Editor 常没事做 — 需明确所有角色都有事。提醒：editor不是"挑错"而是"润色语言"。② 海报语言过简（仅单词无句）— 要求每板块至少2句完整英文句。③ 展示时间控制 — 1.5分钟/组，超时扣分。',
  teachingMethods: '① PBL项目式学习：以展览为驱动问题 ② 小组协作：角色分工+checklist ③ 画廊漫步：全班互评',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 海报四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师：Let\'s review. What did we learn this unit? 教师带学生回顾本单元5课：听与说（道德词汇+抉择）→阅读（林巧稚抉择链+-ing宾补）→语法（-ing宾补）→听与谈（辩论权衡）→写作（道德记叙文）。预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出来。易错点提醒：每个版块至少用一次 -ing 宾补——这是单元核心语法。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 海报结构】【PPT P3 角色卡】教师：Choose a moral figure and a role. 教师展示海报四模块：①Introduction（选一位道德楷模+简介）②Dilemma（关键抉择是什么）③Spirit（精神品质）④Reflection（你的感悟）。角色分工：Writer写文案 / Designer设计排版 / Editor检查语言+语法 / Presenter准备展示。预设回答：We choose Dr. Lin. I am the writer. 板书时机：留模块结构和角色。差异化提示：B班给语言模板（填空式）；A班自由写。易错点提醒：Designer 也是团队一员——和 Writer 商量文案长度才能排出好看版。' },
    { step: '制作海报', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】教师：Use English! At least 2 sentences per module, 1 -ing complement. 小组制作。教师要巡视提醒：①用英文！②每模块至少2句完整句 ③至少1个 -ing 宾补 ④最后5分钟 Editor 检查语言。预设回答：（小组讨论制作中，教师巡视指导）板书时机：无。差异化提示：B班给句子开头提示（The figure is... / She chose...）；A班独立完成。易错点提醒：不要把所有内容挤在一起——留白是设计的一部分。标题要大、内容要分块。' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】教师：You have 90 seconds. Go fast but clear! 每组 1.5 分钟展示。全班投票：最佳内容/最佳设计/最佳展示。预设回答展示。板书时机：记投票结果。差异化提示：B班可看海报读；A班脱稿补充。易错点提醒：1.5分钟很短——只讲最精彩的部分，不要逐字念。' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】教师：Be honest. This is for yourself. 学生勾选四维薄弱项：词汇记不住？-ing 宾补不会用？辩论句型忘了？写作结构不熟？写1条补强计划。预设回答：I need to practice -ing complements. I will review the grammar table tonight. 板书时机：留自评四维。差异化提示：B班中文写、A班英文写。易错点提醒：计划要具体到"做什么"+"什么时候"——不是"我会复习"，而是"今晚复习 -ing 宾补并造5句"。' }
  ],
  blackboard: '┌─ U2 Project: Moral Figure Exhibition ─┐\n│ 🌟 Poster 4 Modules:                   │\n│  ① Introduction (figure + brief)       │\n│  ② Dilemma (key choice?)                │\n│  ③ Spirit (what virtue?)                │\n│  ④ Reflection (your lesson)             │\n│                                        │\n│ 👥 Roles: Writer / Designer / Editor   │\n│          / Presenter                   │\n│                                        │\n│ ⭐ Must: English / ≥2 sentences per    │\n│         module / ≥1 -ing complement    │\n└────────────────────────────────────────┘',
  exercises: '【基础作业】完成小组海报（未完成的继续做），拍照片提交。写 30 词英文反思：我在小组中的贡献是…我从这个项目中学到了…【提高作业】选一位新闻中的道德楷模，用英文写 50 词简报介绍抉择+精神。【参考答案——教师用】反思示例：My role was the writer. I wrote the introduction and the dilemma. I learned how to use -ing complements to describe actions. What I can improve next time: check grammar before the deadline.',
  reflection: '✅ 亮点：海报四模块整合了全单元，学生产出有成就感。⚠️ 需改进：16分钟制作时间紧，下次可给20分钟。📌 下节课衔接：进入 Unit 3 Diverse Cultures，从道德抉择转向文化多样性。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b3-u2-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b3-u2 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
