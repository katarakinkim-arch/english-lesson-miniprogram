/**
 * gen-b2-u1.js — 必修第二册 Unit 1 Cultural Heritage (8课时)
 * 
 * 语篇: FROM PROBLEMS TO SOLUTIONS (Aswan Dam/Abu Simbel temples)
 * 语法: 限制性定语从句 (that/which/who/whom/whose) — 复习必修一U4，扩展应用
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
const UNIT = 1;
const UNIT_TITLE = 'Cultural Heritage';
const BOOK = '必修第二册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u1-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '文化遗产', '世界遗产', '人教版必修二U1', '第一节课'],
  textbookAnalysis: '本课为必修第二册 Unit 1 Cultural Heritage 第一课时（Listening and Speaking），属单元导入+输入环节。语篇为一段关于世界遗产地的对话与一段介绍泰山文化遗产的听力材料，功能语境是"识别与描述文化遗产"。语言重点为遗产保护词汇（heritage, preserve, relic, temple, ancient, UNESCO）及提出建议句型（I suggest that... / It is a good idea to...）。承接必修一U4定语从句基础，为Reading的"问题-解决方案"议论文做词汇与话题预热。',
  overview: '【学情分析】A班：初中已接触简单文化遗产名词（Great Wall, pyramid），能听懂慢速介绍；但 preserve/relic 等词较生。B班：对中国文化遗产名称的英文表达不熟，听力抓细节弱。共同问题：习惯用简单形容词描述文化遗产（big, old），缺乏"价值意义"表达。',
  objectives: [
    '语言能力：听懂关于泰山文化遗产的听力材料，提取关键信息（名称/地点/价值），准确使用 6-8 个遗产保护词汇。',
    '文化意识：了解中国及世界文化遗产的多样性，增强文化遗产保护意识。',
    '思维品质：通过"听前预测—听中验证—听后推理"形成系统听力策略。',
    '学习能力：能用 I suggest that... / It is worth protecting because... 就文化遗产保护做简短发言。'
  ],
  keyPoints: '① 文化遗产核心词汇：heritage / preserve / relic / temple / ancient / UNESCO ② 提建议句型：I suggest (that)... / It is a good idea to... / We should... ③ 听力微技能：听前读题支预测关键词、听中抓数字与地点名。',
  difficulties: '① preserve（保护/保存）与 protect（保护/防护）的用法区别。原因：中文均译"保护"，需语境区分。易错点提醒：preserve 强调保持原有状态，protect 强调防止伤害。② 听力中数字+地名叠加 — 学生易混淆年份与海拔。③ temple /templ/ 发音 — 学生易读成 /tempəl/。',
  teachingMethods: '① 任务型（TBL）：以推荐一处世界遗产为终任务。② 听前预测+听中填卡：信息卡脚手架。③ 对子互问操练建议句型。',
  preparation: '【PPT课件】P1 单元封面（Cultural Heritage）；P2 世界遗产图片九宫格（长城/故宫/兵马俑/泰山/金字塔/吴哥窟/自由女神像/大堡礁/马丘比丘）；P3-4 听力任务题；P5 建议句型板；P6 说话任务卡。【实物教具】世界遗产信息卡 printed 每组一套；世界地图一张。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine pictures. Which ones are in China? Can you name them? 预设回答：The Great Wall, the Forbidden City, Mount Tai! 板书时机：右侧板书 heritage / ancient / UNESCO。差异化提示：B班指图说中文再跟读英文；A班用 I can see... 造句。易错点提醒：ancient /eɪnʃənt/ 的 c 不发音。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 heritage / preserve / relic / temple / UNESCO。教师：Why is the Great Wall a heritage site? 预设回答：Because it is very old and important to history. 板书时机：左栏板书词+短注释。差异化提示：B班配图记忆+词性标注；A班用词造句。易错点提醒：UNESCO 全称 United Nations Educational, Scientific and Cultural Organization，注意拼写。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to an introduction about Mount Tai. Predict: What will be mentioned? (age / location / historical value / visiting tips) 预设回答：Age and location! 板书时机：预测词写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测理由。易错点提醒：听力常见陷阱 — 数字信息会先给错误再修正。"over 3,000 years" ≠ "exactly 3,000 years"。' },
    { step: '听中填卡', time: '10', content: '【PPT P5 表格】【音频 段一】播放听力，学生填信息卡（名称/地点/年代/价值/特色）。教师：How old is Mount Tai? What makes it special? 预设回答：Over 3,000 years old. It is a symbol of Chinese culture. 板书时机：核对答案时填表于黑板中部。差异化提示：B班听两遍只填名称+年代；A班一遍填全。易错点提醒：symbol /sɪmbəl/ — 与 simple /sɪmpəl/ 区分。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to suggest a heritage site? I suggest (that)... / It is a good idea to... / I recommend... 教师示范后用泰山信息造句。预设回答：I suggest visiting Mount Tai because it represents Chinese culture. 板书时机：句型板书于中央。差异化提示：B班套用模板；A班替换地点名+理由。易错点提醒：suggest 后接 doing 或 that 从句（动词原形），不接 to do。' },
    { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，从信息卡中选一处遗产互荐。教师：Recommend a heritage site to your partner. Use suggest / recommend. 预设回答：I recommend the Terracotta Warriors. It is a wonder of the ancient world. 板书时机：无。差异化提示：B班用填空式对话卡；A班自由问答追加理由。易错点提醒：wonder 作名词"奇迹"，不混淆 wonder 动词"想知道"。' }
  ],
  blackboard: '┌─ U1 Listening & Speaking ──────┐\n│ Heritage: ancient / UNESCO       │\n│ preserve / relic / temple / symbol│\n│                                  │\n│ I suggest (that)...              │\n│ It is a good idea to...          │\n│ I recommend + doing...           │\n│                                  │\n│ Mount Tai Symbol Card:           │\n│  Age: >3000y | Value: symbol of  │\n│  Chinese civilization            │\n└──────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有遗产保护词汇。2. 用 I suggest that... 写 3 句遗产保护建议。【提高作业】用英文写一段 50 词推荐语：推荐一处你了解的世界遗产（中英文均可），包含名称/地点/至少 2 点价值。【参考答案——教师用】基础2示例：I suggest that we protect the Great Wall. / I suggest that visitors not take away bricks. / I suggest that the government limit tourist numbers.',
  reflection: '✅ 亮点：九宫格激活+信息卡脚手架有效降听力焦虑，B班填卡完成率高。⚠️ 需改进：UNESCO 发音仍有困难，下节需强化。📌 下节课衔接：进入阅读 FROM PROBLEMS TO SOLUTIONS，从遗产认知延伸到保护方式。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u1-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '文化遗产', '埃及神庙', '阿斯旺大坝', '人教版必修二U1', '第二节课'],
  textbookAnalysis: '本课为必修第二册 Unit 1 第二课时（Reading I），语篇 FROM PROBLEMS TO SOLUTIONS 是一篇问题—解决型议论文，讲述埃及阿斯旺大坝建设与阿布辛贝神庙搬迁的案例，展示了"发展vs保护"的全球协作解决方案。结构为问题引入→各方行动→解决成果→意义升华。语言重点为议论文衔接词（however, finally, over the next 20 years）与文化遗产保护术语（damage, rescue, contribution, committee）。承接必修一U4定语从句，本课语篇中大量出现限制性定语从句。',
  overview: '【学情分析】A班：能快速把握段落主旨，但对"发展vs保护"的辩证思维训练不足。B班：对 UNESCO/国际协作话题背景知识少，需地图+时间线脚手架。共同问题：议论文的"问题→措施→意义"三段论结构感知不清晰，易忽略 however 等转折标志词。',
  objectives: [
    '语言能力：读懂"问题—解决"型议论文，提取阿斯旺大坝项目的时间线/各方行动/成果；掌握 8-10 个论述类核心词汇。',
    '文化意识：理解文化遗产保护的国际协作意义，形成"发展不能以牺牲文化为代价"的观念。',
    '思维品质：通过"问题—措施—意义"三段论分析培养议论文结构思维。',
    '学习能力：能用时间轴+Who-What-Why表格复述文章主体事件。'
  ],
  keyPoints: '① 议论文结构：problem → challenges → solutions → significance ② 时间线词汇：in 1959 / in 1960 / over the next 20 years / finally ③ 核心短语：give way to / lead to / turn to / take down / bring together',
  difficulties: '① give way to（让位于）学生易按字面理解。原因：多义词块。提醒：本文指"新旧更替"。② take down（拆卸）与 take apart（拆开）的区别。③ contribute（贡献/捐献）与 contribution（贡献/捐款）的词性转换。',
  teachingMethods: '① Jigsaw阅读：分组读不同段落后拼图整合。② 时间轴填图法：构建项目进程。③ 问题链追问：训练批判性思维。',
  preparation: '【PPT课件】P1 阿斯旺大坝与阿布辛贝神庙图片；P2 地图（Nile/Aswan/Abu Simbel）；P3-4 时间轴/Who-What-Why表；P5 议论文结构图；P6 词汇对比表；P7 总结回顾。【实物教具】时间轴空白工作单 printed 每人一份；段落拼图卡。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P1 神庙图片】教师：This is Abu Simbel temple, 3,000 years old. But in the 1960s, it faced a problem — what do you think happened? 预设回答：A dam was built? / Water would destroy it. 板书时机：板书 problem? / solution? 双问号。差异化提示：B班中文猜；A班英文猜。易错点提醒：temple /templ/，注意结尾不读完整 /pel/。' },
    { step: '快速阅读抓主干', time: '8', content: '【PPT P3 时间轴】教师：Read fast (3 min). Find: ① What is the problem? ② Who helped? ③ What happened in the end? 预设回答：① Aswan Dam would damage temples. ② UN + 50 countries. ③ Temples were moved and saved. 板书时机：填时间轴的三个关键点。差异化提示：B班给三选一选项；A班写完整句。易错点提醒：proposal /prəpəʊzəl/ — pro- 前缀，pose 词根"放置"。' },
    { step: '精读段落1-2 问题与冲突', time: '10', content: '【PPT P4 问题分析表】教师精讲：give way to = 让位于；led to protests = 引发抗议。教师：Why did people protest? 预设回答：Because the dam could damage temples and cultural relics. 板书时机：左侧栏补充"give way to / lead to / turn to"。差异化提示：B班读后填关键词；A班读后用自己话解释。易错点提醒：relics 复数 — 单数 relic，类似 physics (s并非复数)。' },
    { step: '精读段落3-4 行动与成果', time: '10', content: '【PPT P5 行动链】教师：Who did what? 学生填表匹配（government / committee / UN / engineers → actions）。教师：How was the problem solved? 预设回答：Temples were taken down piece by piece, moved, and put back together. 板书时机：右侧画行动链箭头图。差异化提示：B班连线匹配；A班写完整句。易错点提醒：put back together — back 不是方位而是"恢复原状"。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 议论文结构】教师：What can we learn from this story? (balance between development and protection / global cooperation) 预设回答：We should balance progress and heritage protection. Countries can work together. 板书时机：圈出结构关键词。差异化提示：B班跟读关键词；A班用自己的话总结。易错点提醒：balance /bæləns/ — ba 不是 /beɪ/。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾"问题→行动→方案"结构+核心词汇。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：global cooperation 不是 global corporation（公司）。' }
  ],
  blackboard: '┌─ U1 Reading I: PROBLEMS TO SOLUTIONS ──────┐\n│ PROBLEM → ACTIONS → SOLUTION → SIGNIFICANCE │\n│                                              │\n│ give way to / lead to / turn to / take down  │\n│ rescue / contribution / balance              │\n│                                              │\n│ 1959 UN→1960 work→1961 first temple→20 yrs  │\n│ 50 countries = $80M → 22 temples saved       │\n└──────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-3段 2 遍，圈出所有转折词（however/but/although）。2. 用时间轴上的3个关键年份各写1句事件描述。【提高作业】用 80 词左右写一段：你认为在城市建设中如何平衡"发展"与"保护文物"？（用 give way to / balance / protect）【参考答案——教师用】基础2示例：In 1959, Egypt turned to the UN for help. / In 1960, the work to save temples began. / Over 20 years, 22 temples were rescued.',
  reflection: '✅ 亮点：时间轴+Who-What-Why表有效组织信息，B班完成率高。⚠️ 需改进：议论文结构术语（proposal/committee）学生仍感吃力。📌 下节课衔接：进入精读语言+定语从句在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u1-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '定语从句', '文化遗产', '人教版必修二U1', '第三节课'],
  textbookAnalysis: '本课为必修第二册 Unit 1 第三课时（Reading II），聚焦语篇 FROM PROBLEMS TO SOLUTIONS 的精读与语言分析。重点分析文中限制性定语从句（The dam that was built / temples that were an important part...）在议论文中的功能——提供限定性信息、增强论述说服力。同时深化语篇中高频学术词汇的用法辨析（establish / investigate / conduct / propose）。',
  overview: '【学情分析】A班：必修一U4已接触限制性定语从句，能识别 that/which/who，但辨 when to use which 仍有困难。B班：定语从句概念感模糊，需大量语境例句支撑。共同问题：阅读中见到定语从句会跳过不分析其功能——学生把定语从句当"长难句"而非"信息工具"。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 5 个限制性定语从句的功能，准确辨析关系代词。',
    '文化意识：通过定语从句体会英语如何用子句修饰限定——不同于中文前置定语的习惯。',
    '思维品质：分析定语从句在议论文中的"信息限定"功能，培养语法服务于意义的意识。',
    '学习能力：建立"从读到写"的语料库——积累课文中的优质定语从句句型用于后续写作。'
  ],
  keyPoints: '① 语篇中定语从句的识别与关系代词选择 ② 议论文高频动词：establish / investigate / conduct / propose ③ 定语从句在议论文中的修辞功能：提供证据→增强说服力',
  difficulties: '① a number of（许多）vs the number of（…的数量）。原因：形近意远，考试高频陷阱。② 关系代词 that vs which 的选用。提醒：限制性中 that 更通用，但介词后只能用 which。③ proposal 与 propose 的词性转换 — 学生易混淆拼写。',
  teachingMethods: '① 标注法：圈出文中所有定语从句并分析先行词+关系代词。② 替换练习：改写简单句为定语从句。③ 语料卡记录：分类摘录优质句子。',
  preparation: '【PPT课件】P1-2 课文中圈出的定语从句示例；P3 关系代词对比表；P4 语料卡模板；P5 词汇辨析表；P6 句型改写练习；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 结构图】教师：Last class we learned the "problem-solution" structure. Can you recall the key events? 预设回答：Egypt built a dam. Temples were in danger. UN and 50 countries helped. 板书时机：左栏写 1959/1960/1961/20years 时间线。差异化提示：B班看时间轴读关键词；A班完整复述。易错点提醒：recall ≠ remember — recall 更强调"调取记忆"。' },
    { step: '定语从句发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle all clauses starting with that / which / who / whose. 学生标记后全班核对。教师：Why does the author use these clauses? 预设回答：To give more information about the nouns. 板书时机：逐句板书圈出的定语从句。差异化提示：B班给划线句直接圈关系词；A班自己找+写先行词。易错点提醒："temples that were an important part" — that 指 temples（物），不是 part。' },
    { step: '关系代词辨析', time: '10', content: '【PPT P3 对比表】教师对比：that指人物均可，which 仅指物，who 指人，whose 表所有。教师例句：The temple that/which was moved... / The engineers who rescued... / The country whose donation helped... 预设回答辨析。板书时机：四列对比板书。差异化提示：B班根据提示选择填空；A班独立造句。易错点提醒：介词后用 which 不用 that — "a place in which they were safe" 不是 in that。' },
    { step: '语料库搭建', time: '10', content: '【PPT P4 模板】学生分类填语料卡：①定语从句优质句摘录 ②议论文动词（establish/investigate/conduct/propose）③转折衔接词。板书时机：巡视指导。差异化提示：B班填词；A班造句。预设回答：按文化遗产语料库模板分类填写词条。易错点提醒：establish（建立）≠ publish（出版）—— 论文用语 distinguish。' },
    { step: '句型改写', time: '5', content: '【PPT P6 练习】教师给两个简单句，学生合并为定语从句。例：The temples were 3,000 years old. They faced a new dam. → The temples that were 3,000 years old faced a new dam. 预设回答造句。板书时机：板书改写公式。差异化提示：B班给改写框架；A班独立改。易错点提醒：合并后句子仍为一个完整的 SVO 结构，不要重复主语。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】回顾定语从句功能（限定信息→增强说服力）+语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课深入讲关系代词的选用规则。' }
  ],
  blackboard: '┌─ U1 Reading II: Language Focus ──────┐\n│ that → 人/物   which → 物 only       │\n│ who → 人       whose → ...的         │\n│ 介词 + which (not that!)             │\n│                                      │\n│ Verbs: establish / investigate       │\n│        conduct / propose / rescue    │\n│                                      │\n│ Clauses in text (excerpts):          │\n│  temples that were an important part │\n│  scientists who had studied...       │\n│  a place in which they were safe     │\n└──────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出5个定语从句并标注先行词+关系代词。2. 将以下两句合并为定语从句：The government turned to the UN. The UN had experts in heritage protection. 【提高作业】用定语从句写3句介绍一处你了解的文化遗产（用 that / which / where）。【参考答案——教师用】基础2示例：The government turned to the UN which/that had experts in heritage protection.',
  reflection: '✅ 亮点：标注发现法让学生主动探索语法，参与度高。⚠️ 需改进：whose 用法仍有混淆，语法课需强化。📌 下节课衔接：进入语法课，系统对比所有关系代词。'
}));

// ====== Period 4: Grammar (限制性定语从句系统讲练) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u1-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '定语从句', '关系代词', '文化遗产', '人教版必修二U1', '第四节课'],
  textbookAnalysis: '本课为必修第二册 Unit 1 第四课时（Discovering Useful Structures），系统教学限制性定语从句中关系代词（that/which/who/whom/whose）的用法与选择规则。基于 Reading 语篇中提取的例句，引导学生归纳出规则，并通过文化遗产主题的语境化练习巩固。衔接必修一U4已学的 that/which/who 基础，本课新增 whose 和介词+which 结构。',
  overview: '【学情分析】A班：知道 that/which/who 的区别，但介词+which 和 whose 是全新内容。B班：定语从句概念仍模糊，需大量语境化例句反复操练。共同问题：写作中要么不用定语从句，要么乱用 that 覆盖所有情况。',
  objectives: [
    '语言能力：准确选择限制性定语从句的关系代词（that/which/who/whom/whose），在文化遗产话题中产出 5 个以上正确句子。',
    '文化意识：通过定语从句更精准地描述文化遗产的属性和特征。',
    '思维品质：通过"发现例句→归纳规则→应用规则"的归纳法培养语法学习策略。',
    '学习能力：建立"语法自查表"——写作后自行检查定语从句关系代词是否正确。'
  ],
  keyPoints: '① 关系代词对比：that（人+物通用）/ which（仅物）/ who（人主语）/ whom（人宾语）/ whose（所属） ② 介词+which 结构 ③ 限制性定语从句中关系代词的省略条件（作宾语时可省）',
  difficulties: '① whose 中文无直接对应"…的"，学生写作中极少主动使用。原因：母语负迁移。② 介词+which 中介词选择（in which=where 但更正式）。③ that 在 all/everything 等不定代词后必须用 that 不用 which。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习 ② Bingo 游戏：随机抽卡造句 ③ 改错练习：纠正典型错误',
  preparation: '【PPT课件】P1 关系代词对比表（五列）；P2 课文例句摘录；P3 规则归纳页；P4 介词+which 结构；P5 Bingo 任务卡；P6 改错题；P7 总结。【实物教具】关系代词 Bingo 卡每人一张；句型卡一套。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中5个定语从句，学生圈关系代词和先行词。教师：What do these words connect? What do they refer to? 预设回答：They connect two sentences and refer to the noun before. 板书时机：左栏板书例句，标注先行词→关系代词。差异化提示：B班只圈词不分析功能；A班分析关系代词在从句中做什么成分。易错点提醒：关系代词在从句中一定充当成分（主语/宾语/定语），不是摆设。' },
    { step: '规则归纳', time: '12', content: '【PPT P3 对比表】教师引导学生归纳五格对比表：that/which/who/whom/whose + 指人还是物？+ 在从句中做什么成分？教师：When do we use "whose"? 预设回答：When we want to say something belongs to someone/something. 板书时机：板书完整五列对比表。差异化提示：B班填已给框架表；A班自己画表填。易错点提醒：whose 后面跟的名词通常不带冠词——whose name, not whose the name。' },
    { step: '介词+which 讲练', time: '8', content: '【PPT P4 结构】教师：in which = where, for which, to which... 例句：This is the temple in which the ceremony was held. = This is the temple where the ceremony was held. 预设回答辨析：in which 更正式，where 更口语。板书时机：板书 in which / for which / to which 公式。差异化提示：B班选词填空（in/for/to which）；A班改写句子。易错点提醒：介词+which 中的介词来自搭配短语 — "the group to which he belongs" (belong to)。' },
    { step: 'Bingo 造句', time: '8', content: '【PPT P5 Bingo卡】每人一卡，格内为先行词（heritage site / temple / expert / committee / country）。教师抽关系代词，学生用该栏造正确句。教师：Draw "whose" — make a sentence! 预设回答：This is the heritage site whose symbol is the Great Wall. 板书时机：巡视指导。差异化提示：B班给句型框；A班自由造句并追加文化遗产主题细节。易错点提醒：每句造完后检查——先行词+关系代词+从句+主句是否完整。' },
    { step: '改错巩固', time: '3', content: '【PPT P6 改错】展示 3 个典型错误：①The temple which I visited it.（多余it）②The country whom helped Egypt.（应该用 that/which）③The temple which roof is golden.（应该用 whose）。学生纠错并解释。预设回答纠错。板书时机：板书错误→改正公式。差异化提示：B班辨别对错选；A班解释为什么错。易错点提醒：最常犯——从句中重复主语或宾语（it/them 多余）。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾五关系代词比较表+介词+which+改错要诀。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述规则。易错点提醒：写作后自查——每句定语从句是否多插入了 it/them？' }
  ],
  blackboard: '┌─ U1 Grammar: Restrictive Relative Clauses ────┐\n│        指人      指物      在从句中成分      │\n│ that    ✓         ✓       S/O              │\n│ which   ✗         ✓       S/O              │\n│ who     ✓         ✗       S                │\n│ whom    ✓         ✗       O                │\n│ whose   ✓         ✓       attribute(...的)  │\n│                                             │\n│ 介词+which: in which / for which / to which│\n│ 省略条件: 作宾语时可省                      │\n│ ❌ The temple which I visited it. (No "it"!) │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 用 that/which/who/whose 各造 2 句关于文化遗产的句子。2. 从课文中找出3个介词+which结构并翻译。【提高作业】写 60 词短文介绍一处中国文化遗产，要求至少用 3 个定语从句（含1个 whose）。【参考答案——教师用】基础1示例：The Great Wall is a heritage site that attracts millions of visitors. / The guide who showed us the temple was very knowledgeable. / The temple whose history spans 3,000 years is in Egypt.',
  reflection: '✅ 亮点：Bingo 游戏让语法操练不再枯燥，课堂活跃度高。⚠️ 需改进：介词+which 中如何选介词仍是难点，听与谈课可融入练习。📌 下节课衔接：听与谈聚焦文化遗产保护建议，用语篇巩固定语从句。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u1-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '文化遗产保护', '建议', '人教版必修二U1', '第五节课'],
  textbookAnalysis: '本课为必修第二册 Unit 1 第五课时（Listening and Talking），语境为"讨论如何保护文化遗产"。听力材料为一段关于当地古迹保护措施的对话，口语输出任务为就一处待保护的遗产地给出建议。功能语言为提出和回应建议（How about...? / Why don\'t we...? / That\'s a good idea because...）。结合语法课所学的定语从句，在口语中自然运用关系代词做信息补充。',
  overview: '【学情分析】A班：能提出简单建议，但缺乏"建议+理由"的完整表达链。B班：开口意愿低、建议句型储备少。共同问题：只说建议不说原因，缺少 because 从句使表达不完整。',
  objectives: [
    '语言能力：听懂关于文化遗产保护建议的对话，提取建议内容与理由；能用至少 4 种句型提出保护建议并给出理由。',
    '文化意识：体会"每个人都可以为文化遗产保护出力"的参与意识。',
    '思维品质：在讨论中练习"提出建议→给出理由→回应同伴建议"的完整对话链。',
    '学习能力：通过建议对话训练批判性倾听——听懂后回应而非只等自己说。'
  ],
  keyPoints: '① 建议句型：How about doing...? / Why don\'t we...? / I suggest we... / We should... ② 回应句型：That\'s a good idea because... / I agree, but... / I\'m not sure, because... ③ 听力重点：抓住建议+理由的配对信息',
  difficulties: '① Why don\'t we... 是建议不是疑问 — 学生易用 Why not we...（错误）。原因：母语直译干扰。② protect / preserve 在口语中混用 — 听力中需听出语境区别。③ 回应时 only say "yes" or "no" no reason — 需培养 because 跟进的意识。',
  teachingMethods: '① 听前预测→听中配对→听后产出 ② 角色扮演：三人一组（提议者+支持者+质疑者）③ 文化遗产保护圆桌讨论',
  preparation: '【PPT课件】P1 待保护遗产图片（平遥古城/丽江/周庄）；P2 建议句型板；P3 听力任务题；P4 听力任务卡；P5 回应句型板；P6 角色卡。【实物教具】遗产保护建议卡 printed；角色卡。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 遗产图片】教师：Look at these heritage sites. One of them is in danger because too many tourists visit. What can we do to protect it? 预设回答：Limit the number of tourists. / Make rules. 板书时机：左栏板书动词 protect / preserve / limit / restore。差异化提示：B班中文说再翻英文；A班直接英文。易错点提醒：limit（限制）≠ limited（有限的），词性区别。' },
    { step: '听力抓建议', time: '10', content: '【PPT P3 听力任务】听对话，抓"谁提了什么建议+什么理由"。教师：Listen for: What is the suggestion? What is the reason? 预设回答：They suggest making a website because it can spread awareness. 板书时机：配对填表（建议|理由）。差异化提示：B班给配对连线题；A班听写关键词。易错点提醒：listen for（有目的地听）≠ listen to（泛听）——引导学生带问题听。' },
    { step: '听中记录', time: '8', content: '【PPT P4 听力任务卡】【音频】重听，学生填完整建议+回应链。教师：How did the other person respond? 预设回答：That\'s a good idea, but it will cost a lot. 板书时机：核对填表。差异化提示：B班听两遍；A班一遍+复述回应。易错点提醒：回应中出现的 but 不是否定而是补充条件 — "good idea, but..." 是肯定+担忧。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练建议+回应链：A: How about building a website? / B: That\'s a good idea because it reaches many people. / A: I agree, but we need money. 预设回答跟读+仿造。板书时机：板书建议→回应链条。差异化提示：B班用填空脚本；A班自主对话。易错点提醒：How about 后接 doing — "How about build" 是错的。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】三人一组：Citizen A（提议者）、Official B（支持者）、Expert C（质疑者）。就平遥古城游客过多问题讨论。教师巡视。预设回答：A: We should limit daily visitors. / B: That\'s a good idea because it reduces damage. / C: But what about local businesses? 板书时机：留建议句型和回应链供参考。差异化提示：B班照卡读；A班脱稿加即兴内容。易错点提醒：角色扮演中注意用定语从句补充信息 — "tourists who don\'t follow rules should be fined."' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾提建议句型+回应策略。教师：Remember: give a reason after your idea. 预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一句收获。易错点提醒：给别人建议后记得问"what do you think?"——对话是双向的。' }
  ],
  blackboard: '┌─ U1 Listening & Talking ─────────┐\n│ Suggestions:                      │\n│  How about + doing...?            │\n│  Why don\'t we + do...?           │\n│  I suggest we + do...             │\n│  We should / could + do...        │\n│                                   │\n│ Responses:                        │\n│  That\'s a good idea because...    │\n│  I agree, but...                  │\n│  I\'m not sure, because...        │\n│                                   │\n│ Chain: Suggest → Reason → Respond │\n└───────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有建议句型。2. 用至少 2 种建议句型各写 1 句保护遗产的建议+理由。【提高作业】写 60 词对话：两人讨论如何保护一处当地古迹（至少 4 轮，含建议与回应）。【参考答案——教师用】基础2示例：How about limiting the number of tourists to the ancient town? / I suggest that we put up signs to remind visitors not to touch the relics.',
  reflection: '✅ 亮点：角色扮演三角色设置让学生理解真实讨论中的多元声音。⚠️ 需改进：because 跟进率仍需提高，写作课可设置"建议+理由"强制格式。📌 下节课衔接：进入写作，将建议链写成正式的遗产保护倡议书。'
}));

// ====== Period 6: Writing I (结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u1-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '议论文', '文化遗产', '倡议书', '人教版必修二U1', '第六节课'],
  textbookAnalysis: '本课为必修第二册 Unit 1 第六课时（Reading for Writing I），写作体裁为就文化遗产保护写一篇简短倡议书/报告。结构为：问题陈述→保护价值→建议措施→呼吁行动。语言重点为议论文衔接词（firstly, moreover, therefore, in conclusion）与建议动词（suggest, recommend, propose, urge）。结合本单元 Reading 的"问题-方案"结构与语法课的定语从句，实现读-语法-写的闭环。',
  overview: '【学情分析】A班：有基本写作能力，但缺乏议论文结构的框架意识——常写成"想到什么写什么"。B班：句型储备少、语法错误多，需大量脚手架（模板+语料卡）。共同问题：倡议书不知道写给谁——缺少"读者意识"导致语体不正式。',
  objectives: [
    '语言能力：掌握"问题—价值—建议—呼吁"四段式倡议书结构，在文化遗产保护话题中产出 80-100 词结构完整的短文。',
    '文化意识：理解倡议书在推动社会参与遗产保护中的作用。',
    '思维品质：通过"先分析问题再提建议"训练因果逻辑思维。',
    '学习能力：建立"写作前先搭结构框架"的习惯——用 outline 而非直接开写。'
  ],
  keyPoints: '① 倡议书四段结构：Problem → Value → Suggestions → Call to action ② 衔接词：Firstly / Moreover / Therefore / In conclusion ③ 核心句型：It is important to... / I strongly suggest that... / If we..., we can...',
  difficulties: '① 倡议书与议论文的区别 — 倡议书收尾必须有呼吁（Let\'s.../It\'s time to...）。原因：学生习惯写"我认为"而非"我们一起"。② therefore 的正确标点 — therefore 前加分号或句号，不是逗号。③ persuade 与 convince 在写作中的选用。',
  teachingMethods: '① 范文解构法：读范文→画结构图→仿写 ② 语料卡搭建：从本单元5课积累词汇/句型。③ 过程写作：outline→draft→peer review→revise',
  preparation: '【PPT课件】P1 范文（关于某古城的保护倡议书）；P2 四段结构图；P3 衔接词表；P4 语料库模板；P5 写作提纲；P6 写作任务；P7 总结。【实物教具】四段结构空白工作单 printed 每人一份；语料卡模板。',
  process: [
    { step: '范文解构', time: '8', content: '【PPT P1 范文】教师展示范文，学生标注四段（问题/价值/建议/呼吁）。教师：Which paragraph tells us what to do? 预设回答：Paragraph 3 — it gives suggestions. 板书时机：画四段结构框。差异化提示：B班给标注好的范文只匹配段号；A班自己画结构+标注衔接词。易错点提醒：最后一段必须有"Let\'s... / It\'s time to..."才算完整。' },
    { step: '四段结构讲透', time: '8', content: '【PPT P2 结构图】教师逐段讲解：P1 1-2句陈述问题（what is the heritage? what is the problem?）→ P2 2句说明价值（why should we care?）→ P3 3-4句提建议（what can we do?）→ P4 1-2句呼吁（call to action）。教师示范写一段。预设回答跟读结构要点。板书时机：逐段板书模板句。差异化提示：B班给每段填空模板；A班给关键词自己写。易错点提醒：P2 的价值要具体 — 不要只说"it\'s important"，要说"it shows our history / attracts tourists / educates young people"。' },
    { step: '衔接词+句型', time: '5', content: '【PPT P3 词表】教师领读衔接词：Firstly / Moreover / Furthermore / Therefore / In conclusion。教师示例句：Firstly, the ancient town is losing its original look. Moreover, too many shops are replacing old houses. Therefore, we must take action. 预设回答跟读。板书时机：板书衔接词于侧栏。差异化提示：B班选词填空；A班用全级衔接词写一段。易错点提醒：therefore 前用分号或句号 — "The problem is serious; therefore, we must act." 不是 "The problem is serious, therefore we must act."' },
    { step: '积语料', time: '5', content: '【PPT P4 语料库】学生从本单元5课中提取：①遗产保护动词（preserve/rescue/limit/restore）②建议句型（I suggest that...）③定语从句模板（The site that needs protection is...）。板书时机：巡视。差异化提示：B班填词；A班造句。预设回答：按文化遗产语料库分类卡填写词条。易错点提醒：同一意思用不同词替换避免重复——第一段说 important，第二段说 significant / valuable。' },
    { step: '提纲+起草', time: '10', content: '【PPT P5 写作提纲】选一处本地文化遗产（如当地古桥/庙宇/老街），写 80 词倡议书 outline（四段各写关键词）。教师巡视指导 outline。教师：Don\'t write sentences yet — just key words for each paragraph. 预设回答：P1: old bridge / cars damage / P2: 200 years / local symbol / P3: limit cars / put signs / P4: Let\'s protect... 板书时机：留结构框供参考。差异化提示：B班用填空 outline；A班独立列提纲。易错点提醒：outline 不是草稿——用短语不是完整句。这是写前最重要的一步。' },
    { step: '互评提纲', time: '4', content: '【PPT P6 写作任务】同桌互换提纲，检查：四段都有吗？价值段有具体内容吗？呼吁段有 Let\'s 吗？教师：Your partner\'s outline: does it have all 4 parts? 预设回答：Yes, but the value part is too short. 板书时机：留 checklist。差异化提示：B班用 checklist 表逐项打勾；A班口头给改进建议。易错点提醒：互评不是挑刺——给一个赞美+一个建议。"Good outline! Maybe add a reason in paragraph 2."' }
  ],
  blackboard: '┌─ U1 Writing: Proposal for Heritage ────────┐\n│ P1 Problem: The... is in danger because... │\n│ P2 Value: It is valuable because...        │\n│ P3 Suggestions: Firstly,... Moreover,...   │\n│ P4 Call: Let\'s... / It\'s time to...        │\n│                                             │\n│ Linkers: Firstly / Moreover / Therefore    │\n│          Furthermore / In conclusion        │\n│                                             │\n│ Word Bank: preserve / rescue / limit        │\n│           restore / suggest / protect       │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】按课堂 outline 写完 80 词倡议书初稿。要求：四段结构完整、至少 2 个衔接词、至少 1 个定语从句。【提高作业】就同一遗产地写一则 30 词以内的社交媒体宣传语（英文），要求有号召力有感染力。【参考答案——教师用】基础示例（节选）：The old stone bridge in our town is facing a serious problem. Too many heavy trucks cross it every day, and the stones are cracking. This bridge is valuable because it has stood here for over 200 years. It tells the story of our town. Therefore, I strongly suggest that we limit vehicles and put up warning signs. Let\'s protect our bridge before it is too late!',
  reflection: '✅ 亮点：四段结构框架让学生从"不知道写什么"变为"知道每段写什么"。⚠️ 需改进：therefore 标点仍需纠正，下节课用改错题强化。📌 下节课衔接：进入写作 II，互评修改+誊抄终稿。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u1-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '文化遗产', '人教版必修二U1', '第七节课'],
  textbookAnalysis: '本课为必修第二册 Unit 1 第七课时（Writing II），在 Writing I 提纲+初稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进写作的能力——这是新课标强调的学习能力。互评量表聚焦三维度：结构完整（4段）、语言质量（衔接词/定语从句/词汇）、语法准确（三单/时态/标点）。',
  overview: '【学情分析】A班：能辨别别人文章的好坏，但给反馈时只说"写得不错"缺乏具体点。B班：改自己的稿时不知从何下手。共同问题：互评流于表面，不会用检查量表逐项给分。',
  objectives: [
    '语言能力：能根据互评量表给同伴的倡议书初稿提具体、可操作的修改建议。',
    '文化意识：通过阅读同伴的倡议书了解不同文化遗产地的保护需求。',
    '思维品质：在互评中培养"识别问题→提出方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步写作流程，内化为个人写作习惯。'
  ],
  keyPoints: '① 互评三维量表：结构（4段完整）+ 语言（衔接词≥2 / 定语从句≥1 / 词汇多样性）+ 语法（三单/时态/标点） ② 改稿有侧重：先改结构再改语法 ③ 展示礼仪：大声/清晰/目视听众',
  difficulties: '① 学生互评时不好意思提缺点 — 需引导"给建议就是帮助对方进步"。② therefore 标点重复出错。③ 修改时学生只改拼写不改结构 — 需强制"先查四段是否完整"。',
  teachingMethods: '① 量表互评：用统一标准减少主观性 ② 对子互评→修改→展示 ③ 最佳倡议书评选',
  preparation: '【PPT课件】P1 互评三维量表；P2 共性错误（therefore标点/衔接词缺/呼吁弱）；P3 修改指南；P4 展示礼仪；P5 最佳倡议书范例；P6 写作提纲回顾；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①结构（4段都给√/缺→标出）②语言（圈衔接词≥2？定语从句≥1？词汇重复？）③语法（三单？时态？therefore标点？）。教师用上节课自己写的范文示范打分。预设回答跟学。板书时机：量表三维板书于黑板。差异化提示：B班按量表逐项打勾即可；A班还需写一句"最需要改进的地方"。易错点提醒：互评不是打分比高低——是帮对方变得更好。' },
    { step: '起草+互评', time: '12', content: '【PPT P2 共性错误】先展示上节课共性错：①therefore前用逗号②呼吁段缺Let\'s③价值段太笼统。然后同桌互换初稿，用红笔按量表标注。教师巡视。教师：Give one praise and one suggestion. 预设回答：Your structure is good, but the call to action is missing. 板书时机：留量表供参考。差异化提示：B班按checklist勾；A班在稿上写具体修改建议。易错点提醒：提建议时用"I suggest..."而非"You should..."——更礼貌。' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改初稿。顺序：①先补结构（缺哪段补哪段）②再加语言（插入衔接词/定语从句）③最后查语法。教师：Don\'t just fix spelling — check structure first! 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色词汇替换。易错点提醒：修改不是重写——保留原文好的部分，只在薄弱处补强。' },
    { step: '展示评选', time: '8', content: '【PPT P4 展示礼仪】2-3 组自愿上台读倡议书。全班投票：最打动人的倡议/结构最完整的/最想行动起来的。教师：Read loudly and look at the audience. 预设回答展示。板书时机：留展示评分维度。差异化提示：B班可看稿读；A班尽量脱稿。易错点提醒：上台读稿不要太快——你写了100词不等于听众能消化100词。' },
    { step: '结课', time: '5', content: '【PPT P7 总结】回顾写作闭环：outline→draft→peer review→revise→final。教师：Next time you write, remember this process. 预设回答：I will make an outline first. 板书时机：画闭环流程图。差异化提示：B班齐读流程；A班说自己的收获。易错点提醒：最好的写作习惯是"先结构后语言"——不要跳跃步骤。' }
  ],
  blackboard: '┌─ U1 Writing II: Peer Review ────────┐\n│ WRITING PROCESS:                     │\n│  Outline → Draft → Peer → Revise →  │\n│  → Final → SHARE                    │\n│                                      │\n│ Review Checklist:                    │\n│  ✅ 4 paragraphs?                    │\n│  ✅ ≥2 linkers?                      │\n│  ✅ ≥1 relative clause?              │\n│  ✅ Call to action?                  │\n│  ✅ Grammar (3rd p / tense / ;)      │\n└──────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改终稿，誊抄提交。自评：在稿末写 1 句"这次写作最大的进步是…" 【提高作业】调查另一处你不太熟悉的文化遗产，用"问题—价值—建议"框架写 80 词保护倡议书。【参考答案——教师用】参考 Writing I 的 exercises 答案。终稿评估标准：结构4段完整（2分）+衔接词≥2（2分）+定语从句≥1（2分）+呼吁有力（2分）+语法准确（2分）= 10分。',
  reflection: '✅ 亮点：量表培训解决了"不知道评什么"的问题，B班互评质量明显提升。⚠️ 需改进：修改环节时间偏紧，下次可给15分钟。📌 下节课衔接：进入 Project，将本单元5课所学整合为文化遗产保护展览。'
}));

// ====== Period 8: Project (文化遗产保护展览) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u1-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '文化遗产', '展览', '人教版必修二U1', '第八节课'],
  textbookAnalysis: '本课为必修第二册 Unit 1 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的遗产词汇+阅读的"问题—方案"结构+语法的定语从句+听与谈的建议句型+写作的倡议书——完成一份"文化遗产保护展览"海报/展板。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确任务清单。B班：group work 中有同学"搭便车"不干活，需明确定人定责。共同问题：小组合作时语言切换回中文——需设立"英文监督员"角色。',
  objectives: [
    '语言能力：综合运用本单元词汇、定语从句、建议句型，以英文完成一份文化遗产保护展览海报（标题/介绍/问题/方案/呼吁）。',
    '文化意识：通过展览形式向同伴传播文化遗产保护意识。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 海报四模块：Heritage Introduction（简介+价值）→ Threats（问题）→ Protection Measures（措施）→ Call to Action（呼吁） ② 单元知识整合：词汇/定语从句/建议句型/倡议书结构 ③ 小组分工：Writer / Designer / Editor / Presenter各司其职',
  difficulties: '① 小组分工时 Editor 常没事做 — 需明确所有角色都有事。提醒：editor不是"挑错"而是"润色语言"。② 海报语言过简（仅单词无句）— 要求每板块至少2句完整英文句。③ 展示时间控制 — 1.5分钟/组，超时扣分。',
  teachingMethods: '① PBL项目式学习：以展览为驱动问题 ② 小组协作：角色分工+checklist ③ 画廊漫步：全班互评',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 海报四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师带学生回顾本单元5课学了什么：听与说（遗产词汇+建议）→阅读（问题方案+定语从句）→语法（that/which/who/whose）→听与谈（建议+回应）→写作（倡议书四段）。教师：Today we put it all together! 预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出来。易错点提醒：每个版块至少用一次定语从句——这是单元核心语法。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 海报结构】【PPT P3 角色卡】教师展示海报四模块：①Introduction（选一处遗产+简介+价值）②Threats（问题是什么）③Protection（措施建议）④Call to Action（呼吁）。角色分工：Writer写文案 / Designer设计排版 / Editor检查语言+语法 / Presenter准备展示。教师：Choose your heritage site and role. 预设回答：We choose the Great Wall. I am the writer. 板书时机：留模块结构和角色。差异化提示：B班给语言模板（填空式）；A班自由写。易错点提醒：Designer 也是团队一员——和 Writer 商量文案长度才能排出好看版。' },
    { step: '制作海报', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】小组制作。教师要巡视提醒：①用英文！②每模块至少2句完整句 ③至少1个定语从句 ④最后5分钟 Editor 检查语言。预设回答：（小组讨论制作中，教师巡视指导）板书时机：无。差异化提示：B班给句子开头提示（The heritage is... / It is threatened by...）；A班独立完成。易错点提醒：不要把所有内容挤在一起——留白是设计的一部分。标题要大、内容要分块。' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】每组 1.5 分钟展示。全班投票：最佳内容/最佳设计/最佳展示。教师：You have 90 seconds. Go fast but clear! 预设回答展示。板书时机：记投票结果。差异化提示：B班可看海报读；A班脱稿补充。易错点提醒：1.5分钟很短——只讲最精彩的部分，不要逐字念。' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】学生勾选四维薄弱项：词汇记不住？定语从句不会用？建议句型忘了？写作结构不熟？写1条补强计划。教师：Be honest. This is for yourself, not for a grade. 预设回答：I need to practice relative clauses. I will review the grammar table tonight. 板书时机：留自评四维。差异化提示：B班中文写、A班英文写。易错点提醒：计划要具体到"做什么"+"什么时候"——不是"我会复习"，而是"今晚复习关系代词表并造5句"。' }
  ],
  blackboard: '┌─ U1 Project: Heritage Exhibition ────┐\n│ 🏛️ Poster 4 Modules:                  │\n│  ① Introduction (heritage + value)    │\n│  ② Threats (what is the problem?)     │\n│  ③ Protection (what can we do?)       │\n│  ④ Call to Action (let\'s...)          │\n│                                       │\n│ 👥 Roles: Writer / Designer / Editor  │\n│            / Presenter                │\n│                                       │\n│ ⭐ Must: English / ≥2 sentences per   │\n│          module / ≥1 relative clause  │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】完成小组海报（未完成的继续做），拍照片提交。写 30 词英文反思：我在小组中的贡献是…我从这个项目中学到了…【提高作业】选一个新闻中正在面临威胁的文化遗产（不限中国），用英文写 50 词简报介绍问题+你的保护建议。【参考答案——教师用】反思示例：My role was the writer. I wrote the introduction and the protection measures. I learned how to use relative clauses to describe heritage sites. What I can improve next time: check grammar before the deadline.',
  reflection: '✅ 亮点：海报四模块整合了全单元，学生产出有成就感。⚠️ 需改进：16分钟制作时间紧，下次可给20分钟。📌 下节课衔接：进入 Unit 2 Wildlife Protection，从人类遗产转向自然遗产保护。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b2-u1-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b2-u1 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
