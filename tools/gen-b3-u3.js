/**
 * gen-b3-u3.js — 必修第三册 Unit 3 Diverse Cultures (8课时)
 *
 * 语篇: A TRAVEL JOURNAL (旧金山多元文化: 唐人街/淘金热/移民史)
 * 语法: 省略 (ellipsis — 省略冗余词: Some went to the park, others to the museum)
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
const UNIT = 3;
const UNIT_TITLE = 'Diverse Cultures';
const BOOK = '必修第三册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u3-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '多元文化', '世界城市', '人教版必修三U3', '第一节课'],
  textbookAnalysis: '本课为必修第三册 Unit 3 Diverse Cultures 第一课时（Listening and Speaking），属单元导入+输入环节。听力材料为一段介绍世界多元文化城市（旧金山/伦敦/纽约/多伦多）的对话与独白，功能语境是"描述城市的文化多样性"。语言重点为多元文化词汇（diverse, culture, immigrant, melting pot, community, ethnic, variety, unique）及描述城市句型（It is known for... / The city features... / People from... gather here）。为本单元 Reading 的"旧金山旅行日记"做词汇与话题预热。',
  overview: '【学情分析】A班：对旧金山/纽约等城市名称较熟，但 diverse/immigrant/melting pot 等抽象词较生。B班：对移民史背景了解少，听力抓细节弱。共同问题：描述城市停留在"big, modern"表层，缺乏"文化多样性"表达。',
  objectives: [
    '语言能力：听懂关于多元文化城市的听力材料，提取关键信息（城市/族群/特色/意义），准确使用 6-8 个多元文化核心词汇。',
    '文化意识：了解世界城市的文化多样性，体会"多元共生"的包容精神。',
    '思维品质：通过"听前预测—听中验证—听后比较"形成系统听力策略。',
    '学习能力：能用 It is known for... / The city features... 就城市文化多样性做简短描述与对比。'
  ],
  keyPoints: '① 多元文化核心词汇：diverse / culture / immigrant / melting pot / community / ethnic / variety / unique ② 描述句型：It is known for... / The city features... / People from... gather here ③ 听力微技能：听前读题支预测关键词、听中抓族群与特色。',
  difficulties: '① diverse（多样的）与 diversity（多样性）的词性转换。原因：形近意近。易错点提醒：diverse 是形容词，diversity 是名词。② melting pot（大熔炉）比喻义，学生易按字面理解。③ immigrant（移民）与 emigrant（移出者）的方向区分。',
  teachingMethods: '① 任务型（TBL）：以介绍一个多元文化城市为终任务。② 听前预测+听中填卡：信息卡脚手架。③ 对子互问操练描述句型。',
  preparation: '【PPT课件】P1 单元封面（Diverse Cultures）；P2 世界城市图片九宫格（旧金山/伦敦/纽约/多伦多/悉尼/迪拜/新加坡/上海/巴黎）；P3-4 听力任务题；P5 描述句型板；P6 说话任务卡。【实物教具】城市信息卡 printed 每组一套；世界地图一张。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine world cities. Which ones are famous for diverse cultures? Can you name them? 预设回答：San Francisco, New York, London! 板书时机：右侧板书 diverse / culture / immigrant。差异化提示：B班指图说中文再跟读英文；A班用 I can see... 造句。易错点提醒：diverse /daɪvɜːs/ — di 发 /daɪ/ 不发 /dɪ/。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 diverse / culture / immigrant / melting pot / community / ethnic / variety / unique。教师：Why is New York called a melting pot? 预设回答：Because people from all over the world live there. 板书时机：左栏板书词+短注释。差异化提示：B班配图记忆+词性标注；A班用词造句。易错点提醒：immigrant /ɪmɪɡrənt/ — im- 前缀"进入"，与 emigrant（移出）方向相反。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to an introduction about San Francisco. Predict: What will be mentioned? (location / ethnic groups / food / history) 预设回答：Location and ethnic groups! 板书时机：预测词写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测理由。易错点提醒：听力常见陷阱 — 数字信息会先给错误再修正。"over 100 languages" 可能被修正。' },
    { step: '听中填卡', time: '10', content: '【PPT P5 表格】【音频 段一】播放听力，学生填信息卡（城市/位置/族群/特色/意义）。教师：Where is San Francisco? What ethnic groups live there? 预设回答：On the west coast of the US. Chinese, Mexican, and many others. 板书时机：核对答案时填表于黑板中部。差异化提示：B班听两遍只填城市+族群；A班一遍填全。易错点提醒：ethnic /eθnɪk/ — th 发 /θ/ 不发 /t/。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to describe a diverse city? It is known for... / The city features... / People from... gather here 教师示范后用旧金山信息造句。预设回答：San Francisco is known for its Chinatown. The city features diverse cultures. 板书时机：句型板书于中央。差异化提示：B班套用模板；A班替换城市名+特色细节。易错点提醒：be known for（因…出名）后接名词，be known as（作为…出名）后接身份。' },
    { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，从信息卡中选一个城市互介。教师：Introduce a diverse city to your partner. Use the sentence patterns. 预设回答：I want to introduce New York. It is known for its melting pot culture. People from all over the world gather here. 板书时机：无。差异化提示：B班用填空式对话卡；A班自由描述并追问理由。易错点提醒：gather /ɡæðə/ — th 发 /ð/，不是 /θ/。' }
  ],
  blackboard: '┌─ U3 Listening & Speaking ──────┐\n│ diverse / culture / immigrant    │\n│ melting pot / community / ethnic │\n│ variety / unique                 │\n│                                  │\n│ It is known for...               │\n│ The city features...             │\n│ People from... gather here       │\n│                                  │\n│ City Info Card:                  │\n│  SF | west coast | Chinatown     │\n│  NY | east coast | melting pot   │\n└──────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有多元文化词汇。2. 用 It is known for... 写 3 句城市描述。【提高作业】用英文写一段 50 词介绍：介绍一个你了解的多元文化城市，包含位置/族群/至少 2 点特色。【参考答案——教师用】基础2示例：San Francisco is known for its Chinatown. / New York is known for its melting pot culture. / London is known for its ethnic variety.',
  reflection: '✅ 亮点：九宫格激活+信息卡脚手架有效降听力焦虑，B班填卡完成率高。⚠️ 需改进：ethnic 发音仍有困难，下节需强化。📌 下节课衔接：进入阅读 A TRAVEL JOURNAL，从城市认知延伸到旧金山文化探索。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u3-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '多元文化', '旅行日记', '旧金山', '人教版必修三U3', '第二节课'],
  textbookAnalysis: '本课为必修第三册 Unit 3 第二课时（Reading I），语篇 A TRAVEL JOURNAL 是一篇旅行日记，讲述作者在旧金山的多元文化探索——唐人街、淘金热历史、移民社区、坎佩切区墨西哥文化。结构为抵达城市→唐人街探索→历史回顾（淘金热/移民）→多元社区体验→感悟升华。语言重点为日记衔接词（first, then, after, before long）与多元文化词汇（diverse, immigrant, ethnic, community, historical, district）。承接第一课时词汇，本课语篇中出现省略结构。',
  overview: '【学情分析】A班：能快速把握段落主旨，但对"旅行日记"的叙事结构训练不足。B班：对淘金热/移民史背景知识少，需地图+时间线脚手架。共同问题：日记的"按时间/地点推进"结构感知不清晰，易忽略 first/then 等顺序标志词。',
  objectives: [
    '语言能力：读懂旅行日记，提取旧金山多元文化的地点/族群/历史/特色；掌握 8-10 个论述类核心词汇。',
    '文化意识：理解旧金山作为"移民之城"的多元文化根源，形成"多元共生"的包容观念。',
    '思维品质：通过"地点链+时间链"分析培养日记结构思维与跨文化比较能力。',
    '学习能力：能用地点链+文化特色表复述文章主线。'
  ],
  keyPoints: '① 日记结构：arrival → Chinatown → history (gold rush/immigration) → diverse districts → reflection ② 顺序词：first / then / after / before long / finally ③ 核心短语：head to / used to / bring... to... / a mix of',
  difficulties: '① gold rush（淘金热）历史背景——学生缺乏背景知识。原因：美国历史不熟。② used to do（过去常常）与 be used to doing（习惯于）的区分。③ district（区）与 community（社区）的语境区别。',
  teachingMethods: '① 地图阅读：在旧金山地图上标注地点链。② 时间线填图法：构建历史进程。③ 跨文化比较：旧金山vs上海。',
  preparation: '【PPT课件】P1 旧金山地图与地标；P2 地点链路线图；P3-4 时间线/文化特色表；P5 日记结构图；P6 词汇对比表；P7 总结回顾。【实物教具】旧金山地图空白工作单 printed 每人一份；段落拼图卡。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P1 旧金山地图】教师：This is San Francisco. It has a famous Chinatown and a gold rush history. What do you think makes it diverse? 预设回答：Many immigrants? / Different cultures? 板书时机：板书 diverse? + 三个问号。差异化提示：B班中文猜；A班英文猜并给理由。易错点提醒：Francisco /frænsɪskəʊ/ — ci 发 /sɪ/ 不发 /sɪs/。' },
    { step: '快速阅读抓主干', time: '8', content: '【PPT P3 地点链】教师：Read fast (3 min). Find: ① What places did the author visit? ② What cultures are mentioned? ③ What is the author\'s final feeling? 预设回答：① Chinatown, Mission District. ② Chinese, Mexican. ③ The city is a mix of cultures. 板书时机：填地点链的三个关键点。差异化提示：B班给三选一选项；A班写完整句。易错点提醒：mission /mɪʃən/ — s 发 /ʃ/ 不发 /s/。' },
    { step: '精读段落1-2 抵达与唐人街', time: '10', content: '【PPT P4 地点分析表】教师精讲：head to = 前往；a mix of = 混合。教师：What did the author do in Chinatown? 预设回答：Ate at a Cantonese restaurant. Visited shops. 板书时机：左侧栏补充"head to / a mix of / used to"。差异化提示：B班读后填关键词；A班读后用自己话解释。易错点提醒：used to do（过去常常）≠ be used to doing（习惯于）——考试高频陷阱。' },
    { step: '精读段落3-4 历史与社区', time: '10', content: '【PPT P5 文化表】教师：What is the gold rush? How did it shape the city? 学生填表匹配（gold rush / immigrants / Mission District → contributions）。教师：How did immigrants shape San Francisco? 预设回答：They brought their food, language and traditions. 板书时机：右侧画"gold rush→immigrants→diversity"箭头图。差异化提示：B班连线匹配；A班写完整句。易错点提醒：shape（塑造）在文中是动词"影响/形成"，不是名词"形状"。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 日记结构】教师：What can we learn? (Diversity makes a city vibrant. / Cultures enrich each other.) 预设回答：Diversity makes the city special. Different cultures enrich each other. 板书时机：圈出结构关键词。差异化提示：B班跟读关键词；A班用自己的话总结。易错点提醒：vibrant /vaɪbrənt/ — vi 发 /vaɪ/ 不发 /vɪ/。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾"抵达→唐人街→历史→社区→感悟"结构+核心词汇。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：immigrant /ɪmɪɡrənt/ 与 emigrant 方向相反——im- 进入，em- 移出。' }
  ],
  blackboard: '┌─ U3 Reading I: A TRAVEL JOURNAL ────┐\n│ ARRIVAL → CHINATOWN → HISTORY →       │\n│ DISTRICTS → REFLECTION                │\n│                                       │\n│ Places: Chinatown / Mission District  │\n│ Cultures: Chinese / Mexican           │\n│ History: gold rush → immigrants       │\n│                                       │\n│ head to / a mix of / used to          │\n│ bring... to... / shape / vibrant      │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-3段 2 遍，圈出所有顺序词（first/then/after/before long）。2. 用地点链上的3个关键地点各写1句文化特色描述。【提高作业】用 80 词左右写一段：你认为多元文化对一个城市有什么影响？为什么？（用 diverse / immigrant / enrich）【参考答案——教师用】基础2示例：In Chinatown, the author tasted Cantonese food. / In the Mission District, the author saw Mexican murals. / In the historical museum, the author learned about the gold rush.',
  reflection: '✅ 亮点：地点链+文化特色表有效组织信息，B班完成率高。⚠️ 需改进：used to do vs be used to doing 仍是难点，精读课需澄清。📌 下节课衔接：进入精读语言+省略结构在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u3-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '省略', '多元文化', '人教版必修三U3', '第三节课'],
  textbookAnalysis: '本课为必修第三册 Unit 3 第三课时（Reading II），聚焦语篇 A TRAVEL JOURNAL 的精读与语言分析。重点分析文中省略结构（Some went to the park, others to the museum. / When in Rome, do as the Romans do.）在旅行日记中的功能——使语言更简洁、避免重复。同时深化语篇中高频学术词汇的用法辨析（diverse / immigrant / ethnic / district / historical）。',
  overview: '【学情分析】A班：能识别省略，但辨析省略了什么仍有困难。B班：省略概念感模糊，需大量语境例句支撑。共同问题：阅读中见到省略会补全理解但不知其语法功能——学生把省略当"口语随意"而非"修辞工具"。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 5 个省略结构的用法，准确辨析省略了什么。',
    '文化意识：通过省略体会英语如何用简洁结构避免重复——不同于中文的习惯。',
    '思维品质：分析省略在日记中的"信息压缩"功能，培养语法服务于意义的意识。',
    '学习能力：建立"从读到写"的语料库——积累课文中的优质省略句型用于后续写作。'
  ],
  keyPoints: '① 语篇中省略的类型：主语省略 / 谓语省略 / 主谓省略 / 介词省略 ② 议论文高频动词：diverse / immigrant / ethnic / district / historical ③ 省略在日记中的修辞功能：简洁流畅→增强节奏感',
  difficulties: '① 省略了什么的辨析——需还原完整句才能判断。原因：省略隐含。② Some..., others... 结构中的省略。③ historical（历史的）与 historic（有历史意义的）的区分 — 学生易混淆。',
  teachingMethods: '① 标注法：圈出文中所有省略结构并还原完整句。② 替换练习：改写完整句为省略句。③ 语料卡记录：分类摘录优质句子。',
  preparation: '【PPT课件】P1-2 课文中圈出的省略示例；P3 省略类型对比表；P4 语料卡模板；P5 词汇辨析表；P6 句型改写练习；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 结构图】教师：Last class we followed the author\'s travel route. Can you recall the key places? 预设回答：Chinatown, Mission District, the historical museum. The city is a mix of cultures. 板书时机：左栏写地点链。差异化提示：B班看路线图读关键词；A班完整复述。易错点提醒：recall ≠ remember — recall 更强调"主动调取记忆"。' },
    { step: '省略结构发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle sentences where words seem "missing". What is omitted? 学生标记后全班核对。教师：Why does the author omit words here? 预设回答：To make it shorter and avoid repetition. 板书时机：逐句板书圈出的省略结构。差异化提示：B班给划线句直接圈省略处；A班自己找+还原完整句。易错点提醒："Some went to the park, others to the museum" 中 others 后省略了 went。' },
    { step: '省略类型辨析', time: '10', content: '【PPT P3 对比表】教师对比四类省略：①主语省略 (When in Rome...) ②谓语省略 (Some..., others...) ③主谓省略 (Though tired, he continued) ④介词省略 (The same age as you)。教师例句辨析。预设回答辨析。板书时机：四列对比板书。差异化提示：B班根据提示选择填空；A班独立还原。易错点提醒：省略的前提是不引起歧义——不能省略关键信息。' },
    { step: '语料库搭建', time: '10', content: '【PPT P4 模板】教师：Build your corpus. Categorize ellipsis sentences and key words. 学生分类填语料卡：①省略结构优质句摘录 ②多元文化动词（diverse/immigrant/ethnic/district/historical）③顺序衔接词。板书时机：巡视指导。差异化提示：B班填词；A班造句。预设回答：按多元文化语料库模板分类填写词条。易错点提醒：historical（历史的，泛指）≠ historic（有历史意义的，特指）—— a historical novel vs a historic moment。' },
    { step: '句型改写', time: '5', content: '【PPT P6 练习】教师：Rewrite these full sentences using ellipsis. 例：Some people went to the park, and other people went to the museum. → Some went to the park, others to the museum. 预设回答造句。板书时机：板书改写公式。差异化提示：B班给改写框架；A班独立改。易错点提醒：改写后检查——省略的部分是否能从上下文补全，不能引起歧义。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】教师：Let\'s review ellipsis types. 回顾省略四类型+语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课深入讲省略的规则与应用。' }
  ],
  blackboard: '┌─ U3 Reading II: Language Focus ──────┐\n│ Ellipsis (省略):                      │\n│  主语省略: When in Rome, do as...     │\n│  谓语省略: Some..., others...         │\n│  主谓省略: Though tired, he continued │\n│  介词省略: the same age as you        │\n│                                       │\n│ Verbs: diverse / immigrant / ethnic   │\n│        district / historical          │\n│                                       │\n│ Rule: omit only what can be restored  │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出5个省略结构并还原完整句。2. 将以下完整句改写为省略句：Some people like Chinese food, and other people like Mexican food.【提高作业】用省略结构写3句描述一个多元文化城市的句子。【参考答案——教师用】基础2示例：Some like Chinese food, others Mexican.',
  reflection: '✅ 亮点：标注发现法让学生主动探索语法，参与度高。⚠️ 需改进：省略类型的辨析仍有混淆，语法课需强化。📌 下节课衔接：进入语法课，系统讲省略的规则。'
}));

// ====== Period 4: Grammar (省略) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u3-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '省略', 'ellipsis', '多元文化', '人教版必修三U3', '第四节课'],
  textbookAnalysis: '本课为必修第三册 Unit 3 第四课时（Discovering Useful Structures），系统教学省略（ellipsis）的用法。基于 Reading 语篇中提取的例句，引导学生归纳出规则：省略主语/谓语/主谓/介词等冗余成分，前提是不引起歧义。常见于日记、对话、谚语、并列结构中。通过多元文化主题的语境化练习巩固。',
  overview: '【学情分析】A班：知道口语会省略，但书面语省略的规则是新知。B班：省略概念仍模糊，需大量语境化例句反复操练。共同问题：写作中要么不省略（啰嗦），要么乱省略（引起歧义）。',
  objectives: [
    '语言能力：准确识别并产出省略结构的句子，在多元文化话题中产出 5 个以上正确省略句。',
    '文化意识：通过省略更简洁流畅地描述城市文化。',
    '思维品质：通过"发现例句→归纳规则→应用规则"的归纳法培养语法学习策略。',
    '学习能力：建立"语法自查表"——写作后自行检查省略是否引起歧义。'
  ],
  keyPoints: '① 省略类型：主语省略 / 谓语省略 / 主谓省略 / 介词省略 ② 并列结构中的省略（Some..., others...）③ 状语从句中的省略（When/While/Though + -ing/形容词）',
  difficulties: '① 省略的前提——不引起歧义。原因：学生易省略关键信息。② 状语从句省略（When in Rome...）中主语+be 的省略规则。③ 并列结构省略的位置——省略后半句的谓语。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习 ② 还原对比：省略句 vs 完整句 ③ 改错练习：纠正典型错误',
  preparation: '【PPT课件】P1 省略类型对比表；P2 课文例句摘录；P3 规则归纳页；P4 状语从句省略；P5 改写任务卡；P6 改错题；P7 总结。【实物教具】句型卡一套；改写工作单。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中5个省略结构，学生圈省略处并还原。教师：What is omitted here? Can you restore it? 预设回答：The subject "people" is omitted. / The verb "went" is omitted. 板书时机：左栏板书例句，标注省略处。差异化提示：B班只圈省略处不还原；A班还原完整句。易错点提醒：省略的成分必须能从上下文补全——不能凭空省略。' },
    { step: '规则归纳', time: '12', content: '【PPT P3 对比表】教师引导学生归纳四类省略：①主语省略 (When in Rome, do as...) ②谓语省略 (Some..., others...) ③主谓省略 (Though tired, he continued) ④介词省略 (the same age as you)。教师：When can we omit words safely? 预设回答：When the meaning is clear from context! 板书时机：板书完整四列对比表。差异化提示：B班填已给框架表；A班自己画表填。易错点提醒：状语从句省略规则——当主从句主语一致时，可省略从句主语+be：Though (he was) tired, he continued. ' },
    { step: '状语从句省略讲练', time: '8', content: '【PPT P4 结构】教师：When the subject of the adverbial clause = main clause subject, omit subject + be. 例：When (you are) in Rome, do as the Romans do. / While (she was) walking, she saw a parade. 预设回答辨析：主语一致才能省略。板书时机：板书省略公式。差异化提示：B班选词填空（判断能否省略）；A班改写句子。易错点提醒：主从句主语不一致时不能省略——"When in Rome, the food is great" 是错的（food 不能 in Rome 做动作）。' },
    { step: '改写操练', time: '8', content: '【PPT P5 改写卡】教师：Rewrite these full sentences using ellipsis. 例：Some people visited Chinatown, and other people visited the Mission District. → Some visited Chinatown, others the Mission District. 教师抽学生板演。预设回答造句。板书时机：板书改写公式。差异化提示：B班给句型框；A班自由改写并追加多元文化主题细节。易错点提醒：改写后检查——省略的部分能否从上下文补全？' },
    { step: '改错巩固', time: '3', content: '【PPT P6 改错】教师：Find the mistakes. 展示 3 个典型错误：①When in Rome, the buildings are beautiful.（主语不一致）②Some like Chinese food, others like Mexican food, too.（未省略谓语，啰嗦）③Though tired, the trip was fun.（主语不一致）。学生纠错并解释。预设回答纠错。板书时机：板书错误→改正公式。差异化提示：B班辨别对错选；A班解释为什么错。易错点提醒：最常犯——状语从句省略时主从句主语不一致。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Let\'s review ellipsis rules. 回顾省略四类型+状语从句规则+改错要诀。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述规则。易错点提醒：写作后自查——每个省略结构是否引起歧义？主从句主语是否一致？' }
  ],
  blackboard: '┌─ U3 Grammar: Ellipsis (省略) ───────┐\n│ Types:                                │\n│  ① Subject: When in Rome, do as...    │\n│  ② Predicate: Some..., others...      │\n│  ③ S+V: Though tired, he continued    │\n│  ④ Prep: the same age as you          │\n│                                       │\n│ Adverbial clause ellipsis:            │\n│  When/While/Though + (S+be) + ...     │\n│  Rule: main S = clause S              │\n│                                       │\n│ ⚠️ Don\'t omit if it causes ambiguity! │\n│ ✗ When in Rome, the food is great.    │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】1. 用省略结构各造 2 句关于多元文化城市的句子（含状语从句省略和并列省略）。2. 将以下完整句改写为省略句：When you are in San Francisco, you should visit Chinatown.【提高作业】写 60 词短文描述一个多元文化城市，要求至少用 3 个省略结构。【参考答案——教师用】基础1示例：Some love Chinese food, others Mexican. (并列省略) / When in San Francisco, visit Chinatown. (状语省略) 基础2示例：When in San Francisco, visit Chinatown.',
  reflection: '✅ 亮点：还原对比让语法操练不再枯燥，课堂活跃度高。⚠️ 需改进：状语从句省略主语一致性仍是难点，听与谈课可融入练习。📌 下节课衔接：听与谈聚焦文化比较讨论，用语篇巩固省略。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u3-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '文化比较', '讨论', '人教版必修三U3', '第五节课'],
  textbookAnalysis: '本课为必修第三册 Unit 3 第五课时（Listening and Talking），语境为"比较不同城市的文化特色"。听力材料为一段关于上海与旧金山文化比较的对话，口语输出任务为就两个城市做文化比较与讨论。功能语言为比较与对比（Both... and... / However, ... / Unlike..., ... / While..., ...）。结合语法课所学的省略结构，在口语中自然运用省略使表达简洁。',
  overview: '【学情分析】A班：能做简单比较，但缺乏"对比+转折"的完整表达链。B班：开口意愿低、比较句型储备少。共同问题：只说相同点不说差异，缺少 However/Unlike 使比较不完整。',
  objectives: [
    '语言能力：听懂关于城市文化比较的对话，提取相同点与差异；能用至少 4 种句型做比较与对比。',
    '文化意识：体会"不同文化各有特色"的包容比较精神。',
    '思维品质：在讨论中练习"相同→差异→评价"的完整比较链。',
    '学习能力：通过比较对话训练批判性倾听——听懂后回应而非只等自己说。'
  ],
  keyPoints: '① 比较句型：Both... and... / Similarly, ... / However, ... / Unlike..., ... / While..., ... ② 听力重点：抓住相同点与差异的配对信息 ③ 省略在口语比较中的运用',
  difficulties: '① Unlike（不像）后接名词/代词 — 学生易接句子。原因：词性不清。② While（然而）表对比不是时间 — 学生易混。③ 回应时 only say "yes" no comparison — 需培养 However 跟进的意识。',
  teachingMethods: '① 听前预测→听中配对→听后产出 ② 角色扮演：三人一组（支持者+对比者+评价者）③ 文化比较圆桌讨论',
  preparation: '【PPT课件】P1 待比较城市（上海vs旧金山/北京vs伦敦）；P2 比较句型板；P3 听力任务题；P4 听力任务卡；P5 对比句型板；P6 角色卡。【实物教具】城市比较卡 printed；角色卡。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 城市对比】教师：Compare Shanghai and San Francisco. What do they have in common? What is different? 预设回答：Both are diverse. But Shanghai is older. 板书时机：左栏板书动词 compare / contrast / differ / share。差异化提示：B班中文说再翻英文；A班直接英文。易错点提醒：compare（比较）强调找相同，contrast（对比）强调找不同。' },
    { step: '听力抓比较', time: '10', content: '【PPT P3 听力任务】听对话，抓"相同点+差异点"。教师：Listen for: What is similar? What is different? 预设回答：Both are port cities. However, SF has more ethnic groups. 板书时机：配对填表（相同|差异）。差异化提示：B班给配对连线题；A班听写关键词。易错点提醒：listen for（有目的地听）≠ listen to（泛听）——引导学生带问题听。' },
    { step: '听中记录', time: '8', content: '【PPT P4 听力任务卡】【音频】重听，学生填完整比较链。教师：How did they contrast the two cities? 预设回答：Unlike SF, Shanghai has a longer history. While SF is known for immigrants, Shanghai is known for trade. 板书时机：核对填表。差异化提示：B班听两遍；A班一遍+复述比较。易错点提醒：Unlike 后接名词 — "Unlike SF" 不是 "Unlike SF is"。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练比较链：A: Both cities are diverse. / B: However, their histories differ. / A: Unlike SF, Shanghai is older. / B: While SF is a melting pot, Shanghai is a trade hub. 预设回答跟读+仿造。板书时机：板书相同→差异链条。差异化提示：B班用填空脚本；A班自主对话。易错点提醒：While 表对比时放句首 — "While A is..., B is..." 不是 "While A is..., is B..."。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】三人一组：Supporter A（找相同）、Contraster B（找差异）、Judge C（做评价）。就北京vs伦敦文化比较讨论。教师巡视。预设回答：A: Both are capitals. / B: However, unlike Beijing, London has a monarchy. / C: While both are historic, their cultures differ. 板书时机：留比较句型供参考。差异化提示：B班照卡读；A班脱稿加即兴内容。易错点提醒：角色扮演中注意用省略使表达简洁 — "Some love Chinese food, others Mexican."' },
    { step: '小结', time: '2', content: '【PPT P7 总结】教师：Remember to compare both similarities and differences. 回顾比较句型+对比策略。预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一句收获。易错点提醒：给比较后记得加"however"或"unlike"——对比才完整。' }
  ],
  blackboard: '┌─ U3 Listening & Talking ─────────┐\n│ Similarities:                      │\n│  Both... and...                    │\n│  Similarly, ...                     │\n│ Differences:                       │\n│  However, ...                       │\n│  Unlike..., ...                     │\n│  While..., ...                      │\n│                                    │\n│ Chain: Similar → Different → Judge │\n└────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有比较句型。2. 用至少 2 种比较句型各写 1 句城市文化比较。【提高作业】写 60 词对话：三人比较两个城市的文化（至少 4 轮，含相同与差异）。【参考答案——教师用】基础2示例：Both Shanghai and SF are diverse. However, unlike SF, Shanghai has a longer history. / While SF is known for immigrants, Shanghai is known for trade.',
  reflection: '✅ 亮点：角色扮演三角色设置让学生理解真实比较中的多元视角。⚠️ 需改进：Unlike 后接名词仍易错，写作课可设置强制格式。📌 下节课衔接：进入写作，将多元城市介绍写成说明文。'
}));

// ====== Period 6: Writing I (结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u3-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '说明文', '城市介绍', '人教版必修三U3', '第六节课'],
  textbookAnalysis: '本课为必修第三册 Unit 3 第六课时（Reading for Writing I），写作体裁为说明文——介绍一个多元文化城市。结构为：城市概况（location/population）→ 文化特色（ethnic groups/landmarks/food）→ 历史背景（immigration/history）→ 意义感悟（why it matters）。语言重点为说明文衔接词（first, moreover, in addition, finally）与描述句型（It is located in... / The city is known for... / People from... gather here）。结合本单元 Reading 的旅行日记与语法课的省略结构，实现读-语法-写的闭环。',
  overview: '【学情分析】A班：有基本说明能力，但缺乏"概况→特色→历史→意义"的框架意识——常写成流水账。B班：句型储备少、语法错误多，需大量脚手架。共同问题：说明文不知如何收尾——缺少"这座城市让我感受到…"的意义句。',
  objectives: [
    '语言能力：掌握"概况—特色—历史—意义"四段式说明文结构，在多元城市话题中产出 80-100 词结构完整的短文。',
    '文化意识：通过书写城市介绍体会多元文化的包容价值。',
    '思维品质：通过"先介绍再感悟"训练事实—特色—意义的递进逻辑思维。',
    '学习能力：建立"写作前先搭结构框架"的习惯——用 outline 而非直接开写。'
  ],
  keyPoints: '① 说明文四段结构：Overview (location/population) → Features (ethnic/landmarks/food) → History (immigration) → Significance (meaning) ② 衔接词：First / Moreover / In addition / Finally ③ 核心句型：It is located in... / The city is known for... / People from... gather here',
  difficulties: '① 说明文与记叙文的区别 — 说明文重客观事实。原因：学生易混体裁。② Moreover 与 In addition 的用法——都是"此外"。③ 意义感悟句不知道怎么写——需给模板。',
  teachingMethods: '① 范文解构法：读范文→画结构图→仿写 ② 语料卡搭建：从本单元5课积累词汇/句型。③ 过程写作：outline→draft→peer review→revise',
  preparation: '【PPT课件】P1 范文（关于旧金山的说明文）；P2 四段结构图；P3 衔接词表；P4 语料库模板；P5 写作提纲；P6 写作任务；P7 总结。【实物教具】四段结构空白工作单 printed 每人一份；语料卡模板。',
  process: [
    { step: '范文解构', time: '8', content: '【PPT P1 范文】教师展示范文，学生标注四段（概况/特色/历史/意义）。教师：Which paragraph gives facts? Which gives meaning? 预设回答：Paragraphs 1-3 — facts. Paragraph 4 — meaning. 板书时机：画四段结构框。差异化提示：B班给标注好的范文只匹配段号；A班自己画结构+标注衔接词。易错点提醒：最后一段必须有"This city shows that..."才算完整意义。' },
    { step: '四段结构讲透', time: '8', content: '【PPT P2 结构图】教师逐段讲解：P1 2句概况（location/population）→ P2 3句特色（ethnic groups/landmarks/food）→ P3 2句历史（immigration/history）→ P4 2句意义（why it matters）。教师示范写一段。预设回答跟读结构要点。板书时机：逐段板书模板句。差异化提示：B班给每段填空模板；A班给关键词自己写。易错点提醒：P2 的特色要具体 — 不要只说"it\'s diverse"，要说"it has Chinatown, Mexican murals and diverse food"' },
    { step: '连接词+句型', time: '5', content: '【PPT P3 词表】教师领读衔接词：First / Moreover / In addition / Furthermore / Finally。教师示例句：First, SF is on the west coast. Moreover, it has a famous Chinatown. In addition, Mexican culture is strong. Finally, it is a true melting pot. 预设回答跟读。板书时机：板书衔接词于侧栏。差异化提示：B班选词填空；A班用全级衔接词写一段。易错点提醒：Moreover 后接逗号 — "Moreover, it..." 不是 "Moreover it..."' },
    { step: '积语料', time: '5', content: '【PPT P4 语料库】教师：Build your word bank. Extract city words, culture words, and ellipsis patterns. 学生从本单元5课中提取：①城市动词（locate/feature/gather/immigrate）②文化描写词（diverse/ethnic/unique/vibrant）③省略结构模板（Some..., others...）。板书时机：巡视。差异化提示：B班填词；A班造句。预设回答：按多元文化语料库分类卡填写词条。易错点提醒：同一意思用不同词替换避免重复——第一段说 diverse，第三段说 varied / multicultural。' },
    { step: '提纲+起草', time: '10', content: '【PPT P5 写作提纲】教师：Don\'t write sentences yet — just key words. 选一个多元文化城市，写 80 词说明文 outline（四段各写关键词）。预设回答：P1: SF / west coast / 800k / P2: Chinatown / Mexican food / diverse / P3: gold rush / immigrants / P4: melting pot / diversity matters. 板书时机：留结构框供参考。差异化提示：B班用填空 outline；A班独立列提纲。易错点提醒：outline 不是草稿——用短语不是完整句。这是写前最重要的一步。' },
    { step: '互评提纲', time: '4', content: '【PPT P6 写作任务】同桌互换提纲，检查：四段都有吗？特色段具体吗？意义段有升华句吗？教师：Your partner\'s outline: does it have all 4 parts? 预设回答：Yes, but the history part is too short. 板书时机：留 checklist。差异化提示：B班用 checklist 表逐项打勾；A班口头给改进建议。易错点提醒：互评不是挑刺——给一个赞美+一个建议。"Good outline! Maybe add a detail in paragraph 3."' }
  ],
  blackboard: '┌─ U3 Writing: Diverse City Intro ────┐\n│ P1 Overview: It is located in...     │\n│ P2 Features: Moreover, it has...     │\n│ P3 History: In addition, ...          │\n│ P4 Significance: This shows that...   │\n│                                       │\n│ Linkers: First / Moreover / In add    │\n│         Furthermore / Finally         │\n│                                       │\n│ Word Bank: locate / feature / gather  │\n│  diverse / ethnic / unique / vibrant  │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】按课堂 outline 写完 80 词多元城市说明文初稿。要求：四段结构完整、至少 2 个衔接词、至少 1 个省略结构。【提高作业】就同一城市写一则 30 词以内的旅游宣传语（英文），要求有吸引力有画面感。【参考答案——教师用】基础示例（节选）：San Francisco is located on the west coast of the United States. Moreover, it is known for its diverse cultures. The city features a famous Chinatown and vibrant Mexican communities. In addition, the gold rush brought many immigrants here. Finally, this city shows that diversity makes a place vibrant.',
  reflection: '✅ 亮点：四段结构框架让学生从"不知道写什么"变为"知道每段写什么"。⚠️ 需改进：说明文与记叙文混淆仍需纠正，下节课用改错题强化。📌 下节课衔接：进入写作 II，互评修改+誊抄终稿。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u3-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '多元文化', '人教版必修三U3', '第七节课'],
  textbookAnalysis: '本课为必修第三册 Unit 3 第七课时（Writing II），在 Writing I 提纲+初稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进写作的能力。互评量表聚焦三维度：结构完整（4段）、语言质量（衔接词/省略结构/词汇）、语法准确（时态/三单/标点）。',
  overview: '【学情分析】A班：能辨别别人文章的好坏，但给反馈时只说"写得不错"缺乏具体点。B班：改自己的稿时不知从何下手。共同问题：互评流于表面，不会用检查量表逐项给分。',
  objectives: [
    '语言能力：能根据互评量表给同伴的城市说明文初稿提具体、可操作的修改建议。',
    '文化意识：通过阅读同伴的城市介绍了解不同城市的多元文化。',
    '思维品质：在互评中培养"识别问题→提出方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步写作流程，内化为个人写作习惯。'
  ],
  keyPoints: '① 互评三维量表：结构（4段完整）+ 语言（衔接词≥2 / 省略结构≥1 / 词汇多样性）+ 语法（时态/三单/标点） ② 改稿有侧重：先改结构再改语法 ③ 展示礼仪：大声/清晰/目视听众',
  difficulties: '① 学生互评时不好意思提缺点 — 需引导"给建议就是帮助对方进步"。② 说明文时态——主体现在时，历史段用过去时。③ 修改时学生只改拼写不改结构 — 需强制"先查四段是否完整"。',
  teachingMethods: '① 量表互评：用统一标准减少主观性 ② 对子互评→修改→展示 ③ 最佳说明文评选',
  preparation: '【PPT课件】P1 互评三维量表；P2 共性错误（时态混用/衔接词缺/意义弱）；P3 修改指南；P4 展示礼仪；P5 最佳说明文范例；P6 写作提纲回顾；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①结构（4段都给√/缺→标出）②语言（圈衔接词≥2？省略结构≥1？词汇重复？）③语法（时态？三单？标点？）。教师用上节课自己写的范文示范打分。预设回答跟学。板书时机：量表三维板书于黑板。差异化提示：B班按量表逐项打勾即可；A班还需写一句"最需要改进的地方"。易错点提醒：互评不是打分比高低——是帮对方变得更好。' },
    { step: '起草+互评', time: '12', content: '【PPT P2 共性错误】教师：First, look at common mistakes. 先展示上节课共性错：①时态混用②意义段缺"This shows"③衔接词缺。然后同桌互换初稿，用红笔按量表标注。教师巡视。教师：Give one praise and one suggestion. 预设回答：Your structure is good, but the tense is mixed. 板书时机：留量表供参考。差异化提示：B班按checklist勾；A班在稿上写具体修改建议。易错点提醒：提建议时用"I suggest..."而非"You should..."——更礼貌。' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改初稿。顺序：①先补结构（缺哪段补哪段）②再加语言（插入衔接词/省略结构）③最后查语法（时态统一）。教师：Don\'t just fix spelling — check structure first! 预设回答：I fixed the tense and added an ellipsis in paragraph 2. 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色词汇替换。易错点提醒：修改不是重写——保留原文好的部分，只在薄弱处补强。' },
    { step: '展示评选', time: '8', content: '【PPT P4 展示礼仪】教师：Read loudly and look at the audience. 2-3 组自愿上台读说明文。全班投票：信息最丰富/结构最完整/最有画面感的。预设回答展示。板书时机：留展示评分维度。差异化提示：B班可看稿读；A班尽量脱稿。易错点提醒：上台读稿不要太快——你写了100词不等于听众能消化100词。' },
    { step: '结课', time: '5', content: '【PPT P7 总结】教师：Next time you write, remember this process. 回顾写作闭环：outline→draft→peer review→revise→final。预设回答：I will make an outline first. 板书时机：画闭环流程图。差异化提示：B班齐读流程；A班说自己的收获。易错点提醒：最好的写作习惯是"先结构后语言"——不要跳跃步骤。' }
  ],
  blackboard: '┌─ U3 Writing II: Peer Review ────────┐\n│ WRITING PROCESS:                      │\n│  Outline → Draft → Peer → Revise →   │\n│  → Final → SHARE                     │\n│                                       │\n│ Review Checklist:                     │\n│  ✅ 4 paragraphs?                     │\n│  ✅ ≥2 linkers?                       │\n│  ✅ ≥1 ellipsis?                      │\n│  ✅ Significance sentence?            │\n│  ✅ Grammar (tense / 3rd p / ;)       │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改终稿，誊抄提交。自评：在稿末写 1 句"这次写作最大的进步是…" 【提高作业】调查另一个你不熟悉的多元文化城市，用"概况—特色—历史—意义"框架写 80 词说明文。【参考答案——教师用】参考 Writing I 的 exercises 答案。终稿评估标准：结构4段完整（2分）+衔接词≥2（2分）+省略结构≥1（2分）+意义有力（2分）+语法准确（2分）= 10分。',
  reflection: '✅ 亮点：量表培训解决了"不知道评什么"的问题，B班互评质量明显提升。⚠️ 需改进：修改环节时间偏紧，下次可给15分钟。📌 下节课衔接：进入 Project，将本单元5课所学整合为多元文化城市展览。'
}));

// ====== Period 8: Project (多元文化城市展览) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b3-u3-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '多元文化', '展览', '人教版必修三U3', '第八节课'],
  textbookAnalysis: '本课为必修第三册 Unit 3 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的多元文化词汇+阅读的"地点链"结构+语法的省略结构+听与谈的比较句型+写作的说明文——完成一份"多元文化城市展览"海报/展板。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确任务清单。B班：group work 中有同学"搭便车"不干活，需明确定人定责。共同问题：小组合作时语言切换回中文——需设立"英文监督员"角色。',
  objectives: [
    '语言能力：综合运用本单元词汇、省略结构、比较句型，以英文完成一份多元文化城市展览海报（标题/概况/特色/历史/意义）。',
    '文化意识：通过展览形式向同伴传播多元文化的包容价值。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 海报四模块：City Overview（概况）→ Features（文化特色）→ History（移民历史）→ Significance（意义感悟） ② 单元知识整合：词汇/省略结构/比较句型/说明文结构 ③ 小组分工：Writer / Designer / Editor / Presenter各司其职',
  difficulties: '① 小组分工时 Editor 常没事做 — 需明确所有角色都有事。提醒：editor不是"挑错"而是"润色语言"。② 海报语言过简（仅单词无句）— 要求每板块至少2句完整英文句。③ 展示时间控制 — 1.5分钟/组，超时扣分。',
  teachingMethods: '① PBL项目式学习：以展览为驱动问题 ② 小组协作：角色分工+checklist ③ 画廊漫步：全班互评',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 海报四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师：Let\'s review. What did we learn this unit? 教师带学生回顾本单元5课：听与说（多元文化词汇+描述）→阅读（旅行日记+省略）→语法（省略四类型）→听与谈（比较讨论）→写作（城市说明文）。预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出来。易错点提醒：每个版块至少用一次省略结构——这是单元核心语法。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 海报结构】【PPT P3 角色卡】教师：Choose a diverse city and a role. 教师展示海报四模块：①Overview（选一个城市+位置+人口）②Features（文化特色是什么）③History（移民历史）④Significance（你的感悟）。角色分工：Writer写文案 / Designer设计排版 / Editor检查语言+语法 / Presenter准备展示。预设回答：We choose SF. I am the writer. 板书时机：留模块结构和角色。差异化提示：B班给语言模板（填空式）；A班自由写。易错点提醒：Designer 也是团队一员——和 Writer 商量文案长度才能排出好看版。' },
    { step: '制作海报', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】教师：Use English! At least 2 sentences per module, 1 ellipsis. 小组制作。教师要巡视提醒：①用英文！②每模块至少2句完整句 ③至少1个省略结构 ④最后5分钟 Editor 检查语言。预设回答：（小组讨论制作中，教师巡视指导）板书时机：无。差异化提示：B班给句子开头提示（The city is... / It features...）；A班独立完成。易错点提醒：不要把所有内容挤在一起——留白是设计的一部分。标题要大、内容要分块。' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】教师：You have 90 seconds. Go fast but clear! 每组 1.5 分钟展示。全班投票：最佳内容/最佳设计/最佳展示。预设回答展示。板书时机：记投票结果。差异化提示：B班可看海报读；A班脱稿补充。易错点提醒：1.5分钟很短——只讲最精彩的部分，不要逐字念。' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】教师：Be honest. This is for yourself. 学生勾选四维薄弱项：词汇记不住？省略结构不会用？比较句型忘了？写作结构不熟？写1条补强计划。预设回答：I need to practice ellipsis. I will review the grammar table tonight. 板书时机：留自评四维。差异化提示：B班中文写、A班英文写。易错点提醒：计划要具体到"做什么"+"什么时候"——不是"我会复习"，而是"今晚复习省略规则并造5句"。' }
  ],
  blackboard: '┌─ U3 Project: Diverse City Exhibition ┐\n│ 🌍 Poster 4 Modules:                  │\n│  ① Overview (city + location)         │\n│  ② Features (what cultures?)          │\n│  ③ History (immigration?)             │\n│  ④ Significance (your lesson)         │\n│                                       │\n│ 👥 Roles: Writer / Designer / Editor  │\n│          / Presenter                  │\n│                                       │\n│ ⭐ Must: English / ≥2 sentences per   │\n│         module / ≥1 ellipsis          │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】完成小组海报（未完成的继续做），拍照片提交。写 30 词英文反思：我在小组中的贡献是…我从这个项目中学到了…【提高作业】选一个新闻中的多元文化城市，用英文写 50 词简报介绍特色+历史。【参考答案——教师用】反思示例：My role was the writer. I wrote the overview and the features. I learned how to use ellipsis to make sentences concise. What I can improve next time: check grammar before the deadline.',
  reflection: '✅ 亮点：海报四模块整合了全单元，学生产出有成就感。⚠️ 需改进：16分钟制作时间紧，下次可给20分钟。📌 下节课衔接：进入 Unit 4 Space Exploration，从地球文化转向太空探索。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b3-u3-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b3-u3 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
