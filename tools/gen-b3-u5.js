/**
 * gen-b3-u5.js — 必修第三册 Unit 5 The Value of Money (8课时)
 *
 * 语篇: THE MILLION POUND BANK NOTE (Act 1, Scene 3 — 马克·吐温戏剧, Henry Adams 获百万英镑)
 * 语法: 情态动词+have done (must have done / should have done / could have done)
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
const UNIT = 5;
const UNIT_TITLE = 'The Value of Money';
const BOOK = '必修第三册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u5-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '金钱', '消费', '人教版必修三U5', '第一节课'],
  textbookAnalysis: '本课为必修第三册 Unit 5 The Value of Money 第一课时（Listening and Speaking），属单元导入+输入环节。听力材料为一段关于金钱观与消费习惯（spending habits）的对话与独白，功能语境是"讨论金钱的价值与消费选择"。语言重点为金钱词汇（money, value, spend, save, cost, afford, worth, expense, budget）及表达消费观句型（I think it is worth... / I would rather... / It is a waste to...）。为本单元 Reading 的"百万英镑"戏剧做词汇与话题预热。',
  overview: '【学情分析】A班：对 spend/save/cost 等词较熟，但 afford/budget/expense 等词较生。B班：对用英语讨论金钱观开口意愿低，听力抓细节弱。共同问题：讨论金钱停留在"贵/便宜"表层，缺乏"价值判断"表达。',
  objectives: [
    '语言能力：听懂关于金钱观与消费的听力材料，提取关键信息（物品/价格/态度/选择），准确使用 6-8 个金钱核心词汇。',
    '文化意识：了解中外金钱观的差异，体会"理性消费"的价值观。',
    '思维品质：通过"听前预测—听中验证—听后推理"形成系统听力策略。',
    '学习能力：能用 I think it is worth... / I would rather... 就消费选择做简短发言。'
  ],
  keyPoints: '① 金钱核心词汇：money / value / spend / save / cost / afford / worth / expense / budget ② 消费观句型：I think it is worth... / I would rather... / It is a waste to... ③ 听力微技能：听前读题支预测关键词、听中抓价格与态度。',
  difficulties: '① afford（负担得起）拼写与用法。原因：学生易与 effort 混淆。易错点提醒：afford /əfɔːd/，后接 to do 或名词。② worth（值得）后接 doing 或名词，不用 to do。③ budget（预算）作名词与动词的双重用法。',
  teachingMethods: '① 任务型（TBL）：以讨论一个消费选择为终任务。② 听前预测+听中填卡：信息卡脚手架。③ 对子互问操练消费句型。',
  preparation: '【PPT课件】P1 单元封面（The Value of Money）；P2 消费情境图片九宫格（买手机/存钱/捐赠/奢侈品/二手货/投资/请客/旅行/账单）；P3-4 听力任务题；P5 消费句型板；P6 说话任务卡。【实物教具】消费信息卡 printed 每组一套。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine spending situations. Which ones do you often do? How do you decide? 预设回答：I save money! / I buy things on sale. 板书时机：右侧板书 money / value / spend。差异化提示：B班指图说中文再跟读英文；A班用 I usually... 造句。易错点提醒：afford /əfɔːd/ — af 发 /əf/ 不发 /æf/。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 money / value / spend / save / cost / afford / worth / expense / budget。教师：What does "afford" mean? 预设回答：To have enough money to buy something. 板书时机：左栏板书词+短注释。差异化提示：B班配图记忆+词性标注；A班用词造句。易错点提醒：worth 后接 doing — "worth buying" 不是 "worth to buy"。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to a dialogue about spending habits. Predict: What will be mentioned? (item / price / attitude / choice) 预设回答：Item and price! 板书时机：预测词写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测理由。易错点提醒：听力常见陷阱 — 态度会先说一个再说"but actually"转变。' },
    { step: '听中填卡', time: '10', content: '【PPT P5 表格】【音频 段一】播放听力，学生填信息卡（物品/价格/态度/选择）。教师：What did the person buy? Was it worth it? 预设回答：A phone. It cost a lot but it was worth it. 板书时机：核对答案时填表于黑板中部。差异化提示：B班听两遍只填物品+价格；A班一遍填全。易错点提醒：expense /ɪkspens/ — ex 发 /ɪks/ 不发 /eks/。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to express a spending choice? I think it is worth... / I would rather... / It is a waste to... 教师示范后用一个消费情境造句。预设回答：I think it is worth buying because it lasts long. I would rather save the money. 板书时机：句型板书于中央。差异化提示：B班套用模板；A班替换物品+理由。易错点提醒：would rather 后接动词原形 — "would rather save" 不是 "would rather saving"。' },
    { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，从信息卡中选一个消费情境互讨。教师：Discuss a spending choice with your partner. Use the sentence patterns. 预设回答：The dilemma is whether to buy a new phone. I think it is worth it. It is a waste to keep the old one. 板书时机：无。差异化提示：B班用填空式对话卡；A班自由讨论并追问理由。易错点提醒：rather /rɑːðə/ — th 发 /ð/，不是 /θ/。' }
  ],
  blackboard: '┌─ U5 Listening & Speaking ──────┐\n│ money / value / spend / save      │\n│ cost / afford / worth / expense   │\n│ budget                            │\n│                                   │\n│ I think it is worth...            │\n│ I would rather...                 │\n│ It is a waste to...               │\n│                                   │\n│ Spending Card:                    │\n│  phone | expensive | worth buying │\n│  save | budget | smart choice     │\n└───────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有金钱词汇。2. 用 I think it is worth... 写 3 句消费选择。【提高作业】用英文写一段 50 词：描述一次你的消费经历，包含物品/价格/态度/是否值得。【参考答案——教师用】基础2示例：I think it is worth buying a good dictionary. / I think it is worth saving money for college. / I think it is a waste to buy luxury brands.',
  reflection: '✅ 亮点：九宫格激活+信息卡脚手架有效降听力焦虑，B班填卡完成率高。⚠️ 需改进：afford 发音仍有困难，下节需强化。📌 下节课衔接：进入阅读 THE MILLION POUND BANK NOTE，从消费观延伸到金钱与人性的戏剧。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u5-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '金钱', '戏剧', '百万英镑', '人教版必修三U5', '第二节课'],
  textbookAnalysis: '本课为必修第三册 Unit 5 第二课时（Reading I），语篇 THE MILLION POUND BANK NOTE (Act 1, Scene 3) 是马克·吐温戏剧的节选，讲述穷困潦倒的 Henry Adams 被两个富豪兄弟打赌——给他一张百万英镑钞票，看他会否饿死或暴富。结构为背景引入（Henry 落难）→ 兄弟打赌→ Henry 获钞→ 店主态度转变→ 悬念留白。语言重点为戏剧对话词汇（bet, permit, seek, stare, spot, indeed, manner）与人物描写词。承接第一课时词汇，本课语篇中出现情态动词+have done 结构。',
  overview: '【学情分析】A班：能快速把握剧情，但对"戏剧冲突"的分析训练不足。B班：对马克·吐温及19世纪背景了解少，需脚手架。共同问题：戏剧的"对话推进剧情"结构感知不清晰，易忽略人物态度转变。',
  objectives: [
    '语言能力：读懂戏剧节选，提取 Henry 的境遇/打赌内容/钞票获得/态度转变；掌握 8-10 个论述类核心词汇。',
    '文化意识：理解"金钱考验人性"的主题，形成"金钱不是万能"的辩证观念。',
    '思维品质：通过"冲突链+态度转变"分析培养戏剧结构思维与人物分析能力。',
    '学习能力：能用冲突链+态度表复述文章主线。'
  ],
  keyPoints: '① 戏剧结构：background (Henry lost) → bet (brothers) → bank note (Henry gets) → attitude change (shop owner) → suspense ② 核心短语：make a bet / permit sb to / stare at / spot sb / indeed ③ 戏剧冲突：金钱如何改变人际关系',
  difficulties: '① make a bet（打赌）的用法——bet 既动词又名词。原因：多词性。② permit sb to do（允许某人做）的 to 不可省。③ indeed（确实）的语用功能——表强调确认。',
  teachingMethods: '① 角色朗读：分组读不同人物台词。② 冲突链填图法：标注态度转变。③ 主题讨论：金钱vs人性。',
  preparation: '【PPT课件】P1 马克·吐温与百万英镑钞票；P2 19世纪伦敦背景；P3-4 冲突链表；P5 戏剧结构图；P6 词汇对比表；P7 总结回顾。【实物教具】冲突链空白工作单 printed 每人一份；角色卡。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P1 钞票图片】教师：This is a million pound bank note. If a poor stranger got it, what would happen? Would he survive? 预设回答：He would be rich! / No one could change it. 板书时机：板书 what if? + 三个问号。差异化提示：B班中文猜；A班英文猜并给理由。易错点提醒：pound /paʊnd/ — ou 发 /aʊ/ 不发 /uː/。' },
    { step: '快速阅读抓主干', time: '8', content: '【PPT P3 冲突链】教师：Read fast (3 min). Find: ① Who is Henry? ② What is the bet? ③ What happens at the end? 预设回答：① A poor sailor. ② Whether a man with a million pound note can survive. ③ Henry gets the note and the shop owner changes attitude. 板书时机：填冲突链的三个关键点。差异化提示：B班给三选一选项；A班写完整句。易错点提醒：sailor /seɪlə/ — sai 发 /seɪ/ 不发 /saɪ/。' },
    { step: '精读段落1-2 背景与打赌', time: '10', content: '【PPT P4 冲突表】教师精讲：make a bet = 打赌；permit sb to = 允许。教师：Why did the brothers make a bet? 预设回答：To test whether money can change a person\'s fate. 板书时机：左侧栏补充"make a bet / permit to / stare at"。差异化提示：B班读后填关键词；A班读后用自己话解释。易错点提醒：permit sb to do 中 to 不可省——"permit him to leave" 不是 "permit him leave"。' },
    { step: '精读段落3-4 获钞与转变', time: '10', content: '【PPT P5 态度表】教师：How did Henry feel? How did the shop owner react? 学生填表匹配（Henry / brothers / shop owner → attitudes）。教师：How did money change the relationship? 预设回答：The shop owner was rude at first but became respectful after seeing the note. 板书时机：右侧画"rude→respectful"态度转变图。差异化提示：B班连线匹配；A班写完整句。易错点提醒：stare（凝视）是不及物动词——"stare at" 不是 "stare"。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 戏剧结构】教师：What is the theme? (Money tests human nature. / Wealth changes relationships.) 预设回答：Money can change how people treat you. It tests human nature. 板书时机：圈出结构关键词。差异化提示：B班跟读关键词；A班用自己的话总结。易错点提醒：human nature（人性）是固定搭配，不是"人类自然"。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾"背景→打赌→获钞→转变→悬念"结构+核心词汇。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：indeed /ɪndiːd/ — in 发 /ɪn/ 不发 /aɪn/。' }
  ],
  blackboard: '┌─ U5 Reading I: MILLION POUND NOTE ─┐\n│ BACKGROUND → BET → BANK NOTE →        │\n│ ATTITUDE CHANGE → SUSPENSE            │\n│                                       │\n│ Henry: poor sailor → gets note        │\n│ Brothers: make a bet                  │\n│ Shop owner: rude → respectful         │\n│                                       │\n│ make a bet / permit to / stare at     │\n│ spot / indeed / manner / human nature │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-3段 2 遍，圈出所有戏剧词汇（bet/permit/stare/spot/indeed）。2. 用冲突链上的3个关键事件各写1句剧情描述。【提高作业】用 80 词左右写一段：你认为金钱能改变人性吗？为什么？（用 bet / stare / human nature）【参考答案——教师用】基础2示例：Henry was a poor sailor who lost his way. / The brothers made a bet about whether money could change his fate. / The shop owner stared at the note and changed his attitude.',
  reflection: '✅ 亮点：冲突链+态度表有效组织信息，B班完成率高。⚠️ 需改进：permit sb to do 用法学生仍感吃力。📌 下节课衔接：进入精读语言+情态动词+have done 在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u5-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '情态动词', '金钱', '人教版必修三U5', '第三节课'],
  textbookAnalysis: '本课为必修第三册 Unit 5 第三课时（Reading II），聚焦语篇 THE MILLION POUND BANK NOTE 的精读与语言分析。重点分析文中情态动词+have done 结构（He must have been hungry. / You should have told me. / They could have helped.）在戏剧中的功能——表对过去的推测/责备/可能性。同时深化语篇中高频学术词汇的用法辨析（bet / permit / stare / spot / indeed / manner）。',
  overview: '【学情分析】A班：能识别情态动词，但辨析其+have done 的推测/责备功能仍有困难。B班：情态动词+have done 概念感模糊，需大量语境例句支撑。共同问题：阅读中见到 must have done 会理解为"必须"而非"一定"——学生把情态动词当现在时而非对过去的推测。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 5 个情态动词+have done 的用法，准确辨析功能。',
    '文化意识：通过情态动词+have done 体会英语如何表达对过去的推测与评价——不同于中文的习惯。',
    '思维品质：分析情态动词+have done 在戏剧中的"推测/责备"功能，培养语法服务于意义的意识。',
    '学习能力：建立"从读到写"的语料库——积累课文中的优质句型用于后续写作。'
  ],
  keyPoints: '① 语篇中情态动词+have done：must have done（一定做了）/ should have done（本该做）/ could have done（本可以做）② 戏剧高频动词：bet / permit / stare / spot / indeed / manner ③ 情态动词+have done 在戏剧中的修辞功能：表推测/责备→增强戏剧张力',
  difficulties: '① must have done（一定做了）vs must do（必须做）的区分。原因：时态不同。② should have done（本该做但没做）的责备含义。③ spot（发现/认出）与 stare（凝视）的语境区别。',
  teachingMethods: '① 标注法：圈出文中所有情态动词+have done 并分析功能。② 替换练习：改写简单句为情态动词+have done。③ 语料卡记录：分类摘录优质句子。',
  preparation: '【PPT课件】P1-2 课文中圈出的情态动词+have done 示例；P3 推测vs责备对比表；P4 语料卡模板；P5 词汇辨析表；P6 句型改写练习；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 结构图】教师：Last class we learned the plot. Can you recall the key events? 预设回答：Henry was poor. The brothers made a bet. Henry got the note. The shop owner changed. 板书时机：左栏写 背景打赌/获钞/转变 故事线。差异化提示：B班看冲突链读关键词；A班完整复述。易错点提醒：recall ≠ remember — recall 更强调"主动调取记忆"。' },
    { step: '情态动词+have done 发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle all "modal verb + have + done" structures. What do they express? 学生标记后全班核对。教师：Does "must have been" mean "must be" or "certainly was"? 预设回答：It means "certainly was" — a guess about the past. 板书时机：逐句板书圈出的情态动词+have done 结构。差异化提示：B班给划线句直接圈结构；A班自己找+标注功能。易错点提醒："He must have been hungry" 中 must have been 表对过去的肯定推测，不是"必须"。' },
    { step: '推测vs责备辨析', time: '10', content: '【PPT P3 对比表】教师对比：推测——must have done（一定做了）/ could have done（可能做了）；责备——should have done（本该做但没做）/ shouldn\'t have done（本不该做但做了）。教师例句辨析。预设回答辨析。板书时机：两列对比板书。差异化提示：B班根据提示选择填空；A班独立造句。易错点提醒：should have done 含"责备"——"You should have told me" 意思是"你本该告诉我（但没告诉）"。' },
    { step: '语料库搭建', time: '10', content: '【PPT P4 模板】教师：Build your corpus. Categorize modal+have done sentences and key verbs. 学生分类填语料卡：①推测类（must/could have done）优质句摘录 ②责备类（should/shouldn\'t have done）优质句摘录 ③戏剧动词（bet/permit/stare/spot/indeed/manner）。板书时机：巡视指导。差异化提示：B班填词；A班造句。预设回答：按金钱主题语料库模板分类填写词条。易错点提醒：spot 在文中表"发现/认出"（spot sb in the crowd），不是"斑点"。' },
    { step: '句型改写', time: '5', content: '【PPT P6 练习】教师：Rewrite using modal + have done. 例：I am sure he was hungry. → He must have been hungry. / You didn\'t tell me. That was wrong. → You should have told me. 预设回答造句。板书时机：板书改写公式。差异化提示：B班给改写框架；A班独立改。易错点提醒：改写后检查——have+done 是过去分词，不是原形。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】教师：Let\'s review modal + have done. 回顾推测/责备功能+语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课深入讲情态动词+have done 的规则。' }
  ],
  blackboard: '┌─ U5 Reading II: Language Focus ──────┐\n│ Modal + have done:                     │\n│  推测: must have done (一定做了)        │\n│        could have done (可能做了)       │\n│  责备: should have done (本该做)        │\n│        shouldn\'t have done (本不该做)   │\n│                                        │\n│ Verbs: bet / permit / stare            │\n│        spot / indeed / manner          │\n│                                        │\n│ must have done ≠ must do (必须)        │\n└────────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出5个情态动词+have done 结构并标注推测/责备。2. 将以下句子改写为情态动词+have done：I am sure he was surprised.【提高作业】用情态动词+have done 写3句描述剧中人物的心理（用 must/should/could have done）。【参考答案——教师用】基础2示例：He must have been surprised.',
  reflection: '✅ 亮点：标注发现法让学生主动探索语法，参与度高。⚠️ 需改进：must have done vs must do 区分仍有混淆，语法课需强化。📌 下节课衔接：进入语法课，系统讲情态动词+have done 的规则。'
}));

// ====== Period 4: Grammar (情态动词+have done) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u5-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '情态动词', 'have done', '金钱', '人教版必修三U5', '第四节课'],
  textbookAnalysis: '本课为必修第三册 Unit 5 第四课时（Discovering Useful Structures），系统教学情态动词+have done 的用法。基于 Reading 语篇中提取的例句，引导学生归纳出规则：must have done（一定做了——肯定推测）/ can\'t have done（不可能做了——否定推测）/ should have done（本该做——责备）/ shouldn\'t have done（本不该做——责备）/ could have done（本可以做——可能性/遗憾）。通过金钱主题的语境化练习巩固。',
  overview: '【学情分析】A班：知道情态动词表推测，但+have done 表对过去的推测是新知。B班：情态动词+have done 概念仍模糊，需大量语境化例句反复操练。共同问题：写作中要么不用，要么 must/should 混淆。',
  objectives: [
    '语言能力：准确识别并产出情态动词+have done 的句子，在金钱话题中产出 5 个以上正确句子。',
    '文化意识：通过情态动词+have done 更精准地表达对过去的推测与评价。',
    '思维品质：通过"发现例句→归纳规则→应用规则"的归纳法培养语法学习策略。',
    '学习能力：建立"语法自查表"——写作后自行检查情态动词+have done 的功能是否正确。'
  ],
  keyPoints: '① 推测类：must have done（一定做了）/ can\'t have done（不可能做了）/ could have done（可能做了）② 责备类：should have done（本该做）/ shouldn\'t have done（本不该做）③ 结构：modal + have + 过去分词',
  difficulties: '① must have done（肯定推测）vs should have done（责备）的区分。原因：形近意不同。② can\'t have done（否定推测）的用法——can\'t 表"不可能"。③ could have done 兼表"可能"和"本可以（遗憾）"——需语境判断。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习 ② 改写对比：肯定句 vs 情态动词+have done ③ 改错练习：纠正典型错误',
  preparation: '【PPT课件】P1 推测vs责备对比表；P2 课文例句摘录；P3 规则归纳页；P4 could have done 双义；P5 改写任务卡；P6 改错题；P7 总结。【实物教具】句型卡一套；改写工作单。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中5个情态动词+have done 结构，学生圈 modal+have+done 并判断推测/责备。教师：Does this express a guess or a blame? 预设回答：A guess — must have done. / A blame — should have done. 板书时机：左栏板书例句，标注功能。差异化提示：B班只圈结构不分析功能；A班分析表推测还是责备。易错点提醒：情态动词+have done 一定是对"过去"的推测或评价，不是现在。' },
    { step: '规则归纳', time: '12', content: '【PPT P3 对比表】教师引导学生归纳两类：推测——must have done（一定）/ can\'t have done（不可能）/ could have done（可能）；责备——should have done（本该做）/ shouldn\'t have done（本不该做）。教师：What does "should have done" imply? 预设回答：It means you didn\'t do it but you should have! 板书时机：板书完整对比表。差异化提示：B班填已给框架表；A班自己画表填。易错点提醒：should have done 隐含"没做"——"You should have told me" = 你本该告诉我（但你没告诉）。' },
    { step: 'could have done 讲练', time: '8', content: '【PPT P4 结构】教师：could have done has two meanings: ① possibility (可能做了) ② missed chance (本可以做但没做). 例：He could have left. (可能走了) / He could have helped but didn\'t. (本可以帮但没帮) 预设回答辨析：看语境判断。板书时机：板书 could have done 双义公式。差异化提示：B班选词填空（判断含义）；A班造句。易错点提醒：could have done 表"本可以"时含遗憾——"I could have won" = 我本可以赢（但没赢）。' },
    { step: '改写操练', time: '8', content: '【PPT P5 改写卡】教师：Rewrite using modal + have done. 例：I am sure he stole it. → He must have stolen it. / You didn\'t help. That was wrong. → You should have helped. 教师抽学生板演。预设回答造句。板书时机：板书改写公式。差异化提示：B班给句型框；A班自由改写并追加金钱主题细节。易错点提醒：改写后检查——have 后接过去分词，不是原形。' },
    { step: '改错巩固', time: '3', content: '【PPT P6 改错】教师：Find the mistakes. 展示 3 个典型错误：①He must has done it.（应 have）②You should went there.（应 have gone）③He can\'t did that.（应 have done）。学生纠错并解释。预设回答纠错。板书时机：板书错误→改正公式。差异化提示：B班辨别对错选；A班解释为什么错。易错点提醒：最常犯——have 后用原形或过去式（错），应为过去分词。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Let\'s review modal + have done rules. 回顾推测/责备比较表+could 双义+改错要诀。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述规则。易错点提醒：写作后自查——每个情态动词+have done 是推测还是责备？have 后是否过去分词？' }
  ],
  blackboard: '┌─ U5 Grammar: Modal + have done ─────┐\n│ 推测 (Guess about past):              │\n│  must have done (一定做了)             │\n│  can\'t have done (不可能做了)          │\n│  could have done (可能做了)            │\n│ 责备 (Blame about past):              │\n│  should have done (本该做但没做)       │\n│  shouldn\'t have done (本不该做但做了)  │\n│                                       │\n│ ⚠️ Structure: modal + have + P.P.     │\n│ ✗ must has done → ✓ must have done    │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】1. 用 must/can\'t/should/could have done 各造 2 句关于金钱的句子。2. 将以下句子改写为情态动词+have done：I am sure she spent all the money.【提高作业】写 60 词短文描述一次"后悔的消费决定"，要求至少用 3 个情态动词+have done 结构。【参考答案——教师用】基础1示例：He must have spent all his money. (推测) / You shouldn\'t have bought that. (责备) / She could have saved more. (遗憾) 基础2示例：She must have spent all the money.',
  reflection: '✅ 亮点：改写对比让语法操练不再枯燥，课堂活跃度高。⚠️ 需改进：must vs should 推测/责备区分仍是难点，听与谈课可融入练习。📌 下节课衔接：听与谈聚焦"百万英镑你怎么花"讨论，用语篇巩固情态动词+have done。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u5-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '百万英镑', '讨论', '人教版必修三U5', '第五节课'],
  textbookAnalysis: '本课为必修第三册 Unit 5 第五课时（Listening and Talking），语境为"讨论如果你有一百万英镑会怎么做"。听力材料为一段关于中彩票/获赠巨款后不同选择的对话，口语输出任务为就"百万英镑怎么花"做假设性讨论与表态。功能语言为假设与推理（If I had..., I would... / I would probably... / I might... / That would be...）。结合语法课所学的情态动词+have done，在口语中自然运用对过去的推测。',
  overview: '【学情分析】A班：能做简单假设，但缺乏"假设+推理+后果"的完整表达链。B班：开口意愿低、假设句型储备少。共同问题：只说假设不给推理，缺少 because 使表达空洞。',
  objectives: [
    '语言能力：听懂关于"百万英镑怎么花"的对话，提取选择与理由；能用至少 4 种句型做假设与推理。',
    '文化意识：体会"金钱使用反映价值观"的反思精神。',
    '思维品质：在讨论中练习"假设→推理→后果→评价"的完整对话链。',
    '学习能力：通过假设对话训练批判性倾听——听懂后回应而非只等自己说。'
  ],
  keyPoints: '① 假设句型：If I had..., I would... / I would probably... / I might... ② 推理句型：That would be... / The reason is... / Because... ③ 听力重点：抓住假设+理由的配对信息',
  difficulties: '① If I had（虚拟语气）用 had 不用 have — 学生易错。原因：母语干扰。② would/might 的概率区分。③ 回应时 only say "me too" no reasoning — 需培养 because 跟进的意识。',
  teachingMethods: '① 听前预测→听中配对→听后产出 ② 角色扮演：三人一组（花钱者/存钱者/捐献者）③ "百万英镑"圆桌讨论',
  preparation: '【PPT课件】P1 待讨论情境（中彩票/继承遗产/捡到巨款）；P2 假设句型板；P3 听力任务题；P4 听力任务卡；P5 推理句型板；P6 角色卡。【实物教具】选择建议卡 printed；角色卡。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 情境】教师：If you suddenly got a million pounds, what would you do first? 预设回答：Buy a house! / Travel the world! / Save it all. 板书时机：左栏板书动词 buy / save / invest / donate。差异化提示：B班中文说再翻英文；A班直接英文。易错点提醒：donate（捐赠）与 dedicate（奉献）拼写区分——do- vs de-。' },
    { step: '听力抓假设', time: '10', content: '【PPT P3 听力任务】听对话，抓"谁会怎么花钱+什么理由"。教师：Listen for: What would they do? What is the reason? 预设回答：He would travel because life is short. She would save for the future. 板书时机：配对填表（选择|理由）。差异化提示：B班给配对连线题；A班听写关键词。易错点提醒：listen for（有目的地听）≠ listen to（泛听）——引导学生带问题听。' },
    { step: '听中记录', time: '8', content: '【PPT P4 听力任务卡】【音频】重听，学生填完整假设+推理链。教师：How did they support their choices? 预设回答：If I had a million, I would invest. The reason is that money should grow. 板书时机：核对填表。差异化提示：B班听两遍；A班一遍+复述推理。易错点提醒：If I had 是虚拟语气——主句用 would，从句用过去式。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练假设+推理链：A: If I had a million, I would travel. / B: The reason is? / A: Because experiences matter more than things. / B: I might save instead. That would be safer. 预设回答跟读+仿造。板书时机：板书假设→推理链条。差异化提示：B班用填空脚本；A班自主对话。易错点提醒：might（可能）比 would（会）概率更低——语气区分。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】三人一组：Spender A（花钱者）、Saver B（存钱者）、Giver C（捐献者）。就"百万英镑怎么花"讨论。教师巡视。预设回答：A: If I had it, I would buy a house. / B: I would rather save. Because the future is uncertain. / C: I might donate to charity. That would help many people. 板书时机：留假设句型和推理链供参考。差异化提示：B班照卡读；A班脱稿加即兴内容。易错点提醒：角色扮演中注意用情态动词+have done 推测 — "He must have been tempted to spend it all."' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Remember to give a reason after your assumption. 回顾假设句型+推理策略。预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一句收获。易错点提醒：给假设后记得加"because"——推理才完整。' }
  ],
  blackboard: '┌─ U5 Listening & Talking ─────────┐\n│ Assumption:                        │\n│  If I had..., I would...           │\n│  I would probably...               │\n│  I might...                         │\n│ Reasoning:                         │\n│  The reason is...                  │\n│  Because...                         │\n│  That would be...                  │\n│                                    │\n│ Chain: Assume → Reason → Consequen │\n└────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有假设句型。2. 用 If I had..., I would... 写 2 句百万英镑假设+理由。【提高作业】写 60 词对话：三人讨论"百万英镑怎么花"（至少 4 轮，含假设与推理）。【参考答案——教师用】基础2示例：If I had a million pounds, I would travel the world because experiences matter. / If I had the money, I would invest it because money should grow.',
  reflection: '✅ 亮点：角色扮演三角色设置让学生理解真实讨论中的多元价值观。⚠️ 需改进：虚拟语气 If I had 仍易错，写作课可设置强制格式。📌 下节课衔接：进入写作，将金钱与选择的戏剧场景写成剧本。'
}));

// ====== Period 6: Writing I (结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u5-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '戏剧', '金钱选择', '人教版必修三U5', '第六节课'],
  textbookAnalysis: '本课为必修第三册 Unit 5 第六课时（Reading for Writing I），写作体裁为戏剧场景——写一个关于金钱与选择的戏剧片段。结构为：场景设定（when/where/who）→ 冲突引入（what is the dilemma）→ 对话推进（characters debate）→ 结局悬念（open ending）。语言重点为戏剧对话标点（引号/舞台指示）与冲突描写词（hesitate, argue, insist, refuse, compromise）。结合本单元 Reading 的戏剧精神与语法课的情态动词+have done，实现读-语法-写的闭环。',
  overview: '【学情分析】A班：有基本叙事能力，但缺乏"冲突→对话→悬念"的戏剧结构意识——常写成记叙文。B班：句型储备少、对话格式不熟，需大量脚手架。共同问题：戏剧不知如何收尾——缺少"留白悬念"的开放结局。',
  objectives: [
    '语言能力：掌握"场景—冲突—对话—悬念"四段式戏剧结构，在金钱话题中产出 80-100 词结构完整的戏剧片段。',
    '文化意识：通过书写戏剧体会"金钱考验人性"的戏剧张力。',
    '思维品质：通过"先设冲突再推进对话"训练戏剧冲突逻辑思维。',
    '学习能力：建立"写作前先搭结构框架"的习惯——用 outline 而非直接开写。'
  ],
  keyPoints: '① 戏剧四段结构：Setting (when/where/who) → Conflict (dilemma) → Dialogue (debate) → Ending (suspense) ② 戏剧对话格式：引号+舞台指示 (in brackets) ③ 核心句型：I insist that... / You should have... / What if...?',
  difficulties: '① 戏剧对话格式——引号与舞台指示。原因：学生不熟。② 冲突要具体——不能只说"they argued"。③ 悬念结局不知道怎么写——需给模板。',
  teachingMethods: '① 范文解构法：读范文→画结构图→仿写 ② 语料卡搭建：从本单元5课积累词汇/句型。③ 过程写作：outline→draft→peer review→revise',
  preparation: '【PPT课件】P1 范文（关于金钱选择的戏剧片段）；P2 四段结构图；P3 对话格式表；P4 语料库模板；P5 写作提纲；P6 写作任务；P7 总结。【实物教具】四段结构空白工作单 printed 每人一份；语料卡模板。',
  process: [
    { step: '范文解构', time: '8', content: '【PPT P1 范文】教师展示范文，学生标注四段（场景/冲突/对话/悬念）。教师：Which part is the dialogue? Which is the suspense? 预设回答：The middle — dialogue. The end — suspense. 板书时机：画四段结构框。差异化提示：B班给标注好的范文只匹配段号；A班自己画结构+标注对话格式。易错点提醒：最后必须有悬念——"What will he do?" 而非直接给答案。' },
    { step: '四段结构讲透', time: '8', content: '【PPT P2 结构图】教师逐段讲解：P1 2句场景设定（when/where/who）→ P2 2句冲突引入（what is the dilemma）→ P3 4-6句对话推进（characters debate with quotes）→ P4 1-2句悬念结局（open ending）。教师示范写一段。预设回答跟读结构要点。板书时机：逐段板书模板句。差异化提示：B班给每段填空模板；A班给关键词自己写。易错点提醒：P3 的对话要具体 — 不要只说"they argued"，要写出实际台词。' },
    { step: '对话格式+句型', time: '5', content: '【PPT P3 格式表】教师领读对话格式：台词用引号，舞台指示用括号。教师示例：Tom: "I would keep it!" (angrily) / Lisa: "You should return it." (calmly) 预设回答跟读。板书时机：板书对话格式于侧栏。差异化提示：B班选词填空；A班用全格式写对话。易错点提醒：舞台指示用现在分词或副词——"(angrily)" 或 "(walking away)" 不是 "(angry)"。' },
    { step: '积语料', time: '5', content: '【PPT P4 语料库】教师：Build your word bank. Extract drama words, conflict words, and modal patterns. 学生从本单元5课中提取：①戏剧动词（bet/permit/stare/spot/insist）②冲突描写词（hesitate/argue/refuse/compromise）③情态动词+have done 模板（should have done / must have done）。板书时机：巡视。差异化提示：B班填词；A班造句。预设回答：按金钱主题语料库分类卡填写词条。易错点提醒：同一意思用不同词替换避免重复——第一句说 argue，第三句说 debate / dispute。' },
    { step: '提纲+起草', time: '10', content: '【PPT P5 写作提纲】教师：Don\'t write sentences yet — just key words. 选一个金钱困境，写 80 词戏剧片段 outline（四段各写关键词）。预设回答：P1: shop / two friends / find wallet / P2: keep or return / P3: Tom: keep! / Lisa: return! / P4: what will they do? 板书时机：留结构框供参考。差异化提示：B班用填空 outline；A班独立列提纲。易错点提醒：outline 不是草稿——用短语不是完整句。这是写前最重要的一步。' },
    { step: '互评提纲', time: '4', content: '【PPT P6 写作任务】同桌互换提纲，检查：四段都有吗？冲突段具体吗？悬念段有开放结局吗？教师：Your partner\'s outline: does it have all 4 parts? 预设回答：Yes, but the ending is not open. 板书时机：留 checklist。差异化提示：B班用 checklist 表逐项打勾；A班口头给改进建议。易错点提醒：互评不是挑刺——给一个赞美+一个建议。"Good outline! Maybe make the ending more suspenseful."' }
  ],
  blackboard: '┌─ U5 Writing: Drama Scene ───────────┐\n│ P1 Setting: (When/Where/Who)          │\n│ P2 Conflict: The dilemma is...        │\n│ P3 Dialogue: A: "..." / B: "..."       │\n│ P4 Ending: What will...? (suspense)   │\n│                                       │\n│ Format: "quotes" + (stage directions)  │\n│                                       │\n│ Word Bank: bet / permit / stare / spot│\n│  hesitate / argue / insist / refuse   │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】按课堂 outline 写完 80 词金钱选择戏剧片段初稿。要求：四段结构完整、至少 2 轮对话、至少 1 个情态动词+have done。【提高作业】就同一困境写一则 30 词以内的戏剧海报宣传语（英文），要求有悬念有张力。【参考答案——教师用】基础示例（节选）：(Setting: A shop. Tom and Lisa find a wallet full of money.) Tom: "We should keep it!" (excitedly) Lisa: "You shouldn\'t have said that. We must return it." (firmly) Tom: "But no one saw us..." What will they do in the end?',
  reflection: '✅ 亮点：四段结构框架让学生从"不知道写什么"变为"知道每段写什么"。⚠️ 需改进：对话格式仍需纠正，下节课用改错题强化。📌 下节课衔接：进入写作 II，互评修改+誊抄终稿。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u5-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '金钱', '人教版必修三U5', '第七节课'],
  textbookAnalysis: '本课为必修第三册 Unit 5 第七课时（Writing II），在 Writing I 提纲+初稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进写作的能力。互评量表聚焦三维度：结构完整（4段）、语言质量（对话格式/情态动词+have done/词汇）、语法准确（时态/标点/引号）。',
  overview: '【学情分析】A班：能辨别别人文章的好坏，但给反馈时只说"写得不错"缺乏具体点。B班：改自己的稿时不知从何下手。共同问题：互评流于表面，不会用检查量表逐项给分。',
  objectives: [
    '语言能力：能根据互评量表给同伴的戏剧片段初稿提具体、可操作的修改建议。',
    '文化意识：通过阅读同伴的戏剧了解不同金钱观。',
    '思维品质：在互评中培养"识别问题→提出方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步写作流程，内化为个人写作习惯。'
  ],
  keyPoints: '① 互评三维量表：结构（4段完整）+ 语言（对话格式/情态动词+have done≥1 / 词汇多样性）+ 语法（时态/引号/标点） ② 改稿有侧重：先改结构再改语法 ③ 展示礼仪：大声/清晰/目视听众',
  difficulties: '① 学生互评时不好意思提缺点 — 需引导"给建议就是帮助对方进步"。② 对话引号格式重复出错。③ 修改时学生只改拼写不改结构 — 需强制"先查四段是否完整"。',
  teachingMethods: '① 量表互评：用统一标准减少主观性 ② 对子互评→修改→展示 ③ 最佳戏剧片段评选',
  preparation: '【PPT课件】P1 互评三维量表；P2 共性错误（引号格式/情态动词缺/悬念弱）；P3 修改指南；P4 展示礼仪；P5 最佳戏剧范例；P6 写作提纲回顾；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①结构（4段都给√/缺→标出）②语言（圈对话格式对？情态动词+have done≥1？词汇重复？）③语法（时态？引号？标点？）。教师用上节课自己写的范文示范打分。预设回答跟学。板书时机：量表三维板书于黑板。差异化提示：B班按量表逐项打勾即可；A班还需写一句"最需要改进的地方"。易错点提醒：互评不是打分比高低——是帮对方变得更好。' },
    { step: '起草+互评', time: '12', content: '【PPT P2 共性错误】教师：First, look at common mistakes. 先展示上节课共性错：①引号格式②悬念段缺"What will"③情态动词缺。然后同桌互换初稿，用红笔按量表标注。教师巡视。教师：Give one praise and one suggestion. 预设回答：Your dialogue is good, but the ending is not suspenseful. 板书时机：留量表供参考。差异化提示：B班按checklist勾；A班在稿上写具体修改建议。易错点提醒：提建议时用"I suggest..."而非"You should..."——更礼貌。' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改初稿。顺序：①先补结构（缺哪段补哪段）②再加语言（插入情态动词+have done/修正引号）③最后查语法（时态统一）。教师：Don\'t just fix spelling — check structure first! 预设回答：I fixed the quotes and added a modal+have done in the dialogue. 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色词汇替换。易错点提醒：修改不是重写——保留原文好的部分，只在薄弱处补强。' },
    { step: '展示评选', time: '8', content: '【PPT P4 展示礼仪】教师：Read loudly and look at the audience. 2-3 组自愿上台读戏剧片段（可分角色朗读）。全班投票：最有张力的/结构最完整的/最有悬念的。预设回答展示。板书时机：留展示评分维度。差异化提示：B班可看稿读；A班尽量脱稿分角色。易错点提醒：上台读稿不要太快——你写了100词不等于听众能消化100词。' },
    { step: '结课', time: '5', content: '【PPT P7 总结】教师：Next time you write, remember this process. 回顾写作闭环：outline→draft→peer review→revise→final。预设回答：I will make an outline first. 板书时机：画闭环流程图。差异化提示：B班齐读流程；A班说自己的收获。易错点提醒：最好的写作习惯是"先结构后语言"——不要跳跃步骤。' }
  ],
  blackboard: '┌─ U5 Writing II: Peer Review ────────┐\n│ WRITING PROCESS:                      │\n│  Outline → Draft → Peer → Revise →   │\n│  → Final → SHARE                     │\n│                                       │\n│ Review Checklist:                     │\n│  ✅ 4 paragraphs?                     │\n│  ✅ Dialogue format?                  │\n│  ✅ ≥1 modal+have done?               │\n│  ✅ Suspense ending?                  │\n│  ✅ Grammar (tense / quotes / ;)      │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改终稿，誊抄提交。自评：在稿末写 1 句"这次写作最大的进步是…" 【提高作业】就"如果捡到巨款"写 80 词戏剧片段，用"场景—冲突—对话—悬念"框架。【参考答案——教师用】参考 Writing I 的 exercises 答案。终稿评估标准：结构4段完整（2分）+对话格式（2分）+情态动词+have done≥1（2分）+悬念有力（2分）+语法准确（2分）= 10分。',
  reflection: '✅ 亮点：量表培训解决了"不知道评什么"的问题，B班互评质量明显提升。⚠️ 需改进：修改环节时间偏紧，下次可给15分钟。📌 下节课衔接：进入 Project，将本单元5课所学整合为金钱价值观展览。'
}));

// ====== Period 8: Project (金钱价值观展览) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u5-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '金钱', '展览', '人教版必修三U5', '第八节课'],
  textbookAnalysis: '本课为必修第三册 Unit 5 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的金钱词汇+阅读的"冲突链"结构+语法的情态动词+have done+听与谈的假设句型+写作的戏剧片段——完成一份"金钱价值观展览"海报/展板。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确任务清单。B班：group work 中有同学"搭便车"不干活，需明确定人定责。共同问题：小组合作时语言切换回中文——需设立"英文监督员"角色。',
  objectives: [
    '语言能力：综合运用本单元词汇、情态动词+have done、假设句型，以英文完成一份金钱价值观展览海报（标题/剧情/冲突/主题/反思）。',
    '文化意识：通过展览形式向同伴传播"理性金钱观"的反思精神。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 海报四模块：Plot Summary（剧情简介）→ Conflict（金钱冲突）→ Theme（主题思考）→ Reflection（你的反思） ② 单元知识整合：词汇/情态动词+have done/假设句型/戏剧结构 ③ 小组分工：Writer / Designer / Editor / Presenter各司其职',
  difficulties: '① 小组分工时 Editor 常没事做 — 需明确所有角色都有事。提醒：editor不是"挑错"而是"润色语言"。② 海报语言过简（仅单词无句）— 要求每板块至少2句完整英文句。③ 展示时间控制 — 1.5分钟/组，超时扣分。',
  teachingMethods: '① PBL项目式学习：以展览为驱动问题 ② 小组协作：角色分工+checklist ③ 画廊漫步：全班互评',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 海报四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师：Let\'s review. What did we learn this unit? 教师带学生回顾本单元5课：听与说（金钱词汇+消费观）→阅读（百万英镑+情态动词）→语法（情态动词+have done）→听与谈（假设讨论）→写作（戏剧片段）。预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出来。易错点提醒：每个版块至少用一次情态动词+have done——这是单元核心语法。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 海报结构】【PPT P3 角色卡】教师：Choose a money dilemma and a role. 教师展示海报四模块：①Plot Summary（选一个金钱困境+剧情）②Conflict（金钱冲突是什么）③Theme（主题思考）④Reflection（你的反思）。角色分工：Writer写文案 / Designer设计排版 / Editor检查语言+语法 / Presenter准备展示。预设回答：We choose the million pound story. I am the writer. 板书时机：留模块结构和角色。差异化提示：B班给语言模板（填空式）；A班自由写。易错点提醒：Designer 也是团队一员——和 Writer 商量文案长度才能排出好看版。' },
    { step: '制作海报', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】教师：Use English! At least 2 sentences per module, 1 modal+have done. 小组制作。教师要巡视提醒：①用英文！②每模块至少2句完整句 ③至少1个情态动词+have done ④最后5分钟 Editor 检查语言。预设回答：（小组讨论制作中，教师巡视指导）板书时机：无。差异化提示：B班给句子开头提示（The story is... / The conflict is...）；A班独立完成。易错点提醒：不要把所有内容挤在一起——留白是设计的一部分。标题要大、内容要分块。' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】教师：You have 90 seconds. Go fast but clear! 每组 1.5 分钟展示。全班投票：最佳内容/最佳设计/最佳展示。预设回答展示。板书时机：记投票结果。差异化提示：B班可看海报读；A班脱稿补充。易错点提醒：1.5分钟很短——只讲最精彩的部分，不要逐字念。' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】教师：Be honest. This is for yourself. 学生勾选四维薄弱项：词汇记不住？情态动词+have done 不会用？假设句型忘了？写作结构不熟？写1条补强计划。预设回答：I need to practice modal+have done. I will review the grammar table tonight. 板书时机：留自评四维。差异化提示：B班中文写、A班英文写。易错点提醒：计划要具体到"做什么"+"什么时候"——不是"我会复习"，而是"今晚复习情态动词+have done 并造5句"。' }
  ],
  blackboard: '┌─ U5 Project: Value of Money Expo ──┐\n│ 💰 Poster 4 Modules:                 │\n│  ① Plot Summary (story + brief)      │\n│  ② Conflict (money dilemma?)         │\n│  ③ Theme (what does it teach?)       │\n│  ④ Reflection (your lesson)          │\n│                                      │\n│ 👥 Roles: Writer / Designer / Editor │\n│          / Presenter                 │\n│                                      │\n│ ⭐ Must: English / ≥2 sentences per  │\n│        module / ≥1 modal+have done   │\n└──────────────────────────────────────┘',
  exercises: '【基础作业】完成小组海报（未完成的继续做），拍照片提交。写 30 词英文反思：我在小组中的贡献是…我从这个项目中学到了…【提高作业】选一个新闻中的金钱故事，用英文写 50 词简报介绍冲突+主题。【参考答案——教师用】反思示例：My role was the writer. I wrote the plot summary and the conflict. I learned how to use modal+have done to express guesses about the past. What I can improve next time: check grammar before the deadline.',
  reflection: '✅ 亮点：海报四模块整合了全单元，学生产出有成就感。⚠️ 需改进：16分钟制作时间紧，下次可给20分钟。📌 下节课衔接：必修第三册全部完成，进入选修课程，从金钱价值延伸到更广阔的人文思考。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b3-u5-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b3-u5 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
