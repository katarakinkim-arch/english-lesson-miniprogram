/**
 * gen-b2-u2.js — 必修第二册 Unit 2 Wildlife Protection (8课时)
 * 
 * 语篇: A DAY IN THE CLOUDS (Tibetan antelopes, Changtang Reserve)
 * 语法: 现在进行时的被动语态 (am/is/are being + past participle)
 * 写作: Make an Effective Poster for wildlife protection
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
const UNIT = 2;
const UNIT_TITLE = 'Wildlife Protection';
const BOOK = '必修第二册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u2-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '野生动物保护', '濒危动物', '人教版必修二U2', '第一节课'],
  textbookAnalysis: '本课为必修第二册 Unit 2 Wildlife Protection 第一课时（Listening and Speaking），属单元导入+输入环节。语篇为一段关于濒危动物保护的对话与一则野生动物保护组织志愿者的介绍音频，功能语境是"谈论濒危动物现状与保护措施"。语言重点为野生动物保护词汇（endangered, species, habitat, extinct, poaching, reserve）及表达关切与建议句型（We must... / It is worrying that... / I\'m concerned about...）。为Reading语篇"A DAY IN THE CLOUDS"中藏羚羊保护话题做词汇与话题预热。',
  overview: '【学情分析】A班：对濒危动物话题有兴趣，知道panda/tiger等常见动物英文名，但extinct/habitat/poaching等保护术语生疏。B班：部分濒危动物英文名不熟，听力抓具体数据弱。共同问题：讨论动物保护时只会说"we should protect animals"而缺乏具体措施表达。',
  objectives: [
    '语言能力：听懂关于濒危动物保护的听力材料，提取关键信息（物种名/数量/威胁/措施），准确使用 8-10 个野生动物保护词汇。',
    '文化意识：了解全球濒危野生动物现状，形成"保护野生动物就是保护人类自己"的生态意识。',
    '思维品质：通过"听前预测—听中核实—听后推理"训练听力策略，培养信息筛选能力。',
    '学习能力：能用 We must... / It is worrying that... / I\'m concerned about... 就濒危动物保护做简短发言。'
  ],
  keyPoints: '① 野生动物保护核心词汇：endangered / species / habitat / extinct / poaching / reserve / illegal / conservation ② 表达关切句型：We must... / It is worrying that... / I\'m concerned about... ③ 听力微技能：听前读图表预测数据、听中抓数字与原因。',
  difficulties: '① endangered（濒危的）与 dangerous（危险的）学生易混淆。原因：词形相近。易错点提醒：endangered = 被危及的（需要被保护），dangerous = 危险的（会伤害人）。② species /spiːʃiːz/ 单复数同形 — 学生易误加 -s 变 specieses。③ poaching /pəʊtʃɪŋ/ 与 poach /pəʊtʃ/ 的发音——ch 读 /tʃ/ 不是 /k/。',
  teachingMethods: '① 任务型（TBL）：以推荐一种濒危动物并说明保护措施为终任务。② 听前预测+听中填表格：数据卡脚手架。③ 对子互问操练关切表达句型。',
  preparation: '【PPT课件】P1 单元封面（Wildlife Protection）；P2 濒危动物图片九宫格（藏羚羊/大熊猫/华南虎/雪豹/金丝猴/北极熊/非洲象/蓝鲸/朱鹮）；P3-4 听力任务题+数据表；P5 表达关切句型板；P6 说话任务卡。【实物教具】濒危动物信息卡 printed 每组一套；世界地图一张标出濒危动物分布。【音频】听力两段音频（教材配套）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格】教师：Look at these nine animals. Which ones are endangered? Can you name them in English? 预设回答：Panda, tiger, elephant! The Tibetan antelope! 板书时机：右侧板书 endangered / species / extinct。差异化提示：B班指图说中文再跟读英文；A班用 I think... is endangered because... 造句。易错点提醒：endangered /ɪndeɪndʒəd/ — danger 是 /deɪndʒə/，endanger 加前缀 en- + 后缀 -ed。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 endangered / species / habitat / extinct / poaching / reserve / illegal / conservation。教师：What does "habitat" mean? Why do animals become extinct? 预设回答：Habitat is where animals live. Because people hunt them or cut down forests. 板书时机：左栏板书词+短注释，标注重音。差异化提示：B班配图记忆+中英对照；A班用词造句并解释词根（如 con- "共同"+ serve "保护"= conservation）。易错点提醒：habitat /hæbɪtæt/ — 重音在第一音节，不是 /həbɪtæt/。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to a talk about endangered animals. Predict: What animals will be mentioned? What threats do they face? 预设回答：Tigers, pandas? Humans hunt them. Their homes are destroyed. 板书时机：预测词写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测+理由。易错点提醒：听力常见陷阱 — 先提一个错误数字再纠正。"the population dropped from 100,000 to 50,000" 注意两个数字。' },
    { step: '听中填数据', time: '10', content: '【PPT P5 数据表】【音频 段一】播放听力，学生填数据卡（物种名/现存数量/主要威胁/保护措施）。教师：How many Tibetan antelopes are left? What threatens them? 预设回答：About 300,000. Poaching and habitat loss. 板书时机：核对答案时填表于黑板中部。差异化提示：B班听两遍只填物种名+数量；A班一遍填全+写至少一个保护措施。易错点提醒：数字中 thousand / hundred 不加 s — "three hundred thousand" not "three hundreds thousands"。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to express concern about wildlife? We must... / It is worrying that... / I\'m concerned about... 教师示范后用藏羚羊信息造句。预设回答：I\'m concerned about the Tibetan antelope because poaching is still happening. 板书时机：句型板书于中央。差异化提示：B班套用模板替换关键词；A班替换动物名+追加2个理由。易错点提醒：concerned about + 名词/代词 — I\'m concerning about 是错误，用形容词 concerned。' },
    { step: '说话任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，从信息卡中选一种濒危动物互相介绍+表达关切。教师：Choose one endangered animal. Tell your partner about it and express your concern. 预设回答：The snow leopard is endangered. Only about 4,000 are left. I\'m concerned because their habitat is disappearing. 板书时机：留句型供参考。差异化提示：B班用填空式对话卡；A班自由问答并追加 We must... 建议。易错点提醒：species 单复数同形 — "one species, many species" 绝对不说 specieses。' }
  ],
  blackboard: '┌─ U2 Listening & Speaking ──────────┐\n│ Wildlife: endangered / species       │\n│ habitat / extinct / poaching / IUCN │\n│ reserve / illegal / conservation    │\n│                                      │\n│ Expressing concern:                  │\n│  We must + do...                    │\n│  It is worrying that...             │\n│  I\'m concerned about + n.          │\n│                                      │\n│ Data Card: Tibetan Antelope         │\n│  Population: ~300,000               │\n│  Threats: poaching / habitat loss   │\n└──────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有野生动物保护词汇。2. 用 I\'m concerned about... 写 3 句关于不同濒危动物的关切表达。【提高作业】用英文写一段 50 词介绍一种你关心的濒危动物，包含名称/现存数量/威胁/你的关切感受。【参考答案——教师用】基础2示例：I\'m concerned about the African elephant because poaching for ivory is still serious. / I\'m concerned about the blue whale because ocean pollution threatens its habitat.',
  reflection: '✅ 亮点：九宫格激活+数据卡脚手架有效降听力焦虑，B班填卡完成率高。⚠️ 需改进：species 单复数同形仍需强化，下节需在阅读语境中反复出现。📌 下节课衔接：进入阅读 A DAY IN THE CLOUDS，从藏羚羊听力延伸到作者在羌塘保护区的亲身经历。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u2-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '野生动物保护', '藏羚羊', '羌塘保护区', '人教版必修二U2', '第二节课'],
  textbookAnalysis: '本课为必修第二册 Unit 2 第二课时（Reading I），语篇 A DAY IN THE CLOUDS 是一篇旅行日志/记叙文，作者记述在西藏羌塘自然保护区观察藏羚羊的经历，穿插保护成效（种群恢复）与现存挑战（盗猎、栖息地缩减）的对比。结构为"到达→观察→反思→行动呼吁"。语言重点为记叙文时间顺序词（in the evening / after a while / at dawn）与野生动物保护描述词汇（graceful, observe, recover, threaten, reserve）。',
  overview: '【学情分析】A班：能快速把握记叙文叙事线索，但对"保护成效vs挑战"的辩证思维不足。B班：对西藏/羌塘地理背景陌生，需地图+图片脚手架。共同问题：记叙文中插入议论（保护区工作的意义）时，学生难以区分"叙述"与"议论"段落。',
  objectives: [
    '语言能力：读懂旅行日志类记叙文，提取作者在羌塘保护区的见闻/藏羚羊保护成效/现存挑战；掌握 8-10 个描述类核心词汇。',
    '文化意识：了解中国在藏羚羊保护上取得的成就，增强民族自豪感与野生动物保护意识。',
    '思维品质：通过"叙述—反思"双层结构分析培养记叙文深层阅读策略。',
    '学习能力：能用"所见—所感—所思"框架复述文章主体内容。'
  ],
  keyPoints: '① 记叙文结构：Arrival → Observation → Reflection → Call to action ② 时间顺序词：at dawn / in the evening / after a while / later ③ 核心短语：make out / watch over / day and night / be struck by / remind sb of',
  difficulties: '① make out（辨认出）学生易按字面理解为"做出来"。原因：多义词块。提醒：本文指 in the distance 能隐约看清。② watch over（守护/照看）≠ look at（看）— 前者有"负责保护"的含义。③ be struck by（被…打动）≠ be hit by（被打）— struck 是 strike 的过去分词。',
  teachingMethods: '① KWL阅读法：已知→想知→学到的。② 对比表格：藏羚羊过去 vs 现在。③ 问题链追问：训练批判性思维。',
  preparation: '【PPT课件】P1 羌塘草原与藏羚羊图片；P2 地图（西藏/羌塘保护区位置）；P3 KWL表；P4 过去vs现在对比表；P5 叙述—反思结构图；P6 词汇对比表；P7 总结回顾。【实物教具】KWL工作单 printed 每人一份；藏羚羊信息卡。',
  process: [
    { step: '导入设问', time: '5', content: '【PPT P1 藏羚羊图片】教师：This is the Tibetan antelope, also called "chiru." It lives on the Changtang grassland — 4,000-5,000 meters above sea level. What do you want to know about it? 预设回答：How many are there? Why are they endangered? Can we visit them? 板书时机：板书 K / W / L 三栏表头。差异化提示：B班中文提问教师帮翻译；A班英文提问。易错点提醒：antelope /æntɪləʊp/ — 注意重音在第一音节，结尾不读 /eɪt/。' },
    { step: '快速阅读抓主线', time: '8', content: '【PPT P3 KWL表】教师：Read fast (3 min). Find: ① Where is the author? ② What animal does he see? ③ What is the good news? 预设回答：① Changtang National Nature Reserve. ② Tibetan antelopes. ③ Their population has recovered. 板书时机：填 KWL 表 L 栏关键点。差异化提示：B班给三选一选项；A班写完整句+段落号。易错点提醒：reserve /rɪzɜːv/ — re- 前缀"再"+ serve "保持"= 保护区（保持原生态的地方）。' },
    { step: '精读段落1-2 到达与观察', time: '10', content: '【PPT P4 对比表】教师精讲：make out = 辨认出（at a distance）；be struck by = 被…打动。教师：What did the author see at dawn? How did he feel? 预设回答：He saw a herd of Tibetan antelopes moving across the grassland. He was struck by their beauty and grace. 板书时机：左侧栏补充"make out / be struck by / graceful"。差异化提示：B班读后填关键词；A班用自己话描述画面。易错点提醒：a herd of + 动物（一群）— herd 指食草动物群，flock 指鸟群，pack 指狼群。' },
    { step: '精读段落3-4 反思与挑战', time: '10', content: '【PPT P5 行动链】教师：What did Zhaxi and other volunteers do? Why was their work important? 学生找细节。教师：Is conservation successful? What challenges remain? 预设回答：Yes, the population recovered from 1990s to today. But poaching and habitat loss still threaten them. 板书时机：右侧画"过去→现在→挑战"对比图。差异化提示：B班连线匹配（措施—效果）；A班写"cause and effect"句。易错点提醒：threaten /θretn/ — 不读 /θriːtn/，ea 读 /e/ 不是 /iː/。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 叙述反思结构】教师：What does "A Day in the Clouds" really mean? (literal: high altitude; symbolic: a dream-like, inspiring experience) 预设回答：It means the high altitude (4,000m+). Also, it feels like a dream to see these beautiful animals saved. 板书时机：圈出标题的 literal vs symbolic 含义。差异化提示：B班跟读关键词；A班用自己的话解释双层含义。易错点提醒：clouds 不是"云朵"表面意思，还暗示高原缺氧如在云中，以及看到藏羚羊如梦境般美好。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】教师带学生回顾"到达→观察→反思→呼吁"结构+核心词汇+藏羚羊保护成效。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：conservation（保护自然资源）≠ reservation（预订）—— 两个词截然不同。' }
  ],
  blackboard: '┌─ U2 Reading I: A DAY IN THE CLOUDS ──────┐\n│ Arrival → Observation → Reflection → Call  │\n│                                             │\n│ make out / watch over / be struck by        │\n│ graceful / recover / threaten / observe     │\n│                                             │\n│ Tibetan Antelope: Past vs Now               │\n│  1990s: population ↓ (poaching)            │\n│  Today: ~300,000 (conservation success)     │\n│  Challenges: habitat loss, illegal hunting  │\n│                                             │\n│ Title: "Clouds" = high altitude + dreamlike │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-4段 2 遍，圈出所有时间顺序词。2. 用对比表写 3 句话描述藏羚羊保护前后的变化。【提高作业】用 80 词左右写一段：What can we learn from the success of Tibetan antelope conservation?（用 make out / be struck by / recover）【参考答案——教师用】基础2示例：In the 1990s, the population dropped sharply because of poaching. / Today, thanks to conservation efforts, their numbers have recovered. / However, habitat loss still threatens their survival.',
  reflection: '✅ 亮点：KWL表+对比表有效组织信息，B班完成率高。⚠️ 需改进：make out 和 be struck by 的用法仍需强化，精读课将深入。📌 下节课衔接：进入精读语言+现在进行时的被动语态在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u2-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '被动语态', '野生动物保护', '人教版必修二U2', '第三节课'],
  textbookAnalysis: '本课为必修第二册 Unit 2 第三课时（Reading II），聚焦语篇 A DAY IN THE CLOUDS 的精读与语言分析。重点分析文中现在进行时的被动语态（is/are being + past participle）——如 "Their habitats are being destroyed" "Measures are being taken"——在记叙文中的功能：强调动作正在被施加于受事者、突出紧迫性。同时深化语篇中高频动词的用法辨析（observe / recover / reserve / remind）。',
  overview: '【学情分析】A班：初中已接触一般现在时/一般过去时的被动语态，但进行时被动（is being done）是全新语法点。B班：被动语态概念模糊，经常混淆 be + done 中的 be 动词形式。共同问题：写作中几乎不使用被动语态，主语永远是人。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 4 个现在进行时的被动语态句子，理解其"正在被…"的紧迫语义。',
    '文化意识：通过被动语态体会英语如何突出受事者（动物/环境）而非施事者，形成"以保护对象为中心"的表达习惯。',
    '思维品质：分析现在进行时被动语态在保护类文本中的修辞功能——强调问题的紧迫性。',
    '学习能力：建立"从读到写"的语料库——积累课文中的被动语态句型用于后续海报写作。'
  ],
  keyPoints: '① 现在进行时被动语态结构：am/is/are + being + past participle ② 语篇中被动句的识别与功能分析 ③ 核心动词辨析：observe / recover / reserve / remind / remove / intend',
  difficulties: '① being 在被动语态中的角色 — 学生容易漏掉 being 写成 is destroyed（一般现在时被动，语义变为"总是被破坏"）。② reserve 作名词"保护区"与作动词"预订/保留"的区别。③ recover（恢复）是及物还是不及物 — "The population recovered"（不及物，不用被动）vs "The species was recovered by conservationists"（及物，但很少这样说）。',
  teachingMethods: '① 标注发现法：圈出文中所有被动语态并分析结构。② 句型转换：主动→被动，体会语义变化。③ 语料卡记录：分类摘录优质被动句。',
  preparation: '【PPT课件】P1-2 课文中圈出的被动语态示例；P3 被动语态结构分解公式；P4 主动→被动转换对比；P5 语料卡模板；P6 词汇辨析表；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔两支（黄=被动/绿=时间词）。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 结构图】教师：Last class we read "A Day in the Clouds." Can you recall: Where did the author go? What did he see? What conservation message did he leave? 预设回答：He went to Changtang Reserve. He saw Tibetan antelopes. Conservation is working but challenges remain. 板书时机：左栏写 KWL 三栏关键词。差异化提示：B班看关键词复述；A班完整说出5个以上要点。易错点提醒：Changtang /tʃæŋtæŋ/ — 注意 /æ/ 嘴张大，不要读成 /e/。' },
    { step: '被动语态发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle all sentences with "is/are being + past participle." 学生标记后全班核对。教师：Why does the author use passive voice? 预设回答：To focus on what is happening to the animals, not who is doing it. 板书时机：逐句板书圈出的被动语态。差异化提示：B班给划线句直接圈 being + done；A班自己找+分析主语是谁。易错点提醒：被动语态中 being 不能省！"Their habitat is destroyed"（已破坏完了）≠ "Their habitat is being destroyed"（正在被破坏中）。' },
    { step: '被动语态讲透', time: '10', content: '【PPT P3 结构公式】教师板书公式：am/is/are + being + V-ed。对比：①People destroy habitats.（主动，强调人）→ ②Habitats are destroyed.（一般现在时被动，常态）→ ③Habitats are being destroyed.（现在进行时被动，正在发生，紧急）。教师：Which sentence sounds more urgent? 预设回答：Sentence ③ — it sounds like it is happening RIGHT NOW. 板书时机：三句对比板书，用红笔圈 being。差异化提示：B班填空（is/are ___ + V-ed）；A班独立造句。易错点提醒：being 后面必须用过去分词，不是现在分词 — "is being destroying" 是严重语法错误。' },
    { step: '语料库搭建', time: '10', content: '【PPT P5 语料库模板】学生分类填语料卡：①被动语态优质句摘录（至少3句）②野生动物保护动词（observe/recover/reserve/remind/remove/intend）③时间/空间描述词。板书时机：巡视指导。差异化提示：B班填词+翻译；A班造句并在句末注明该句在写作中的用途。预设回答：按野生动物保护语料库模板分类填写词条。易错点提醒：remind sb of sth（使某人想起某事）— 不是 remind sb sth！of 不能省。"reminds me the importance" ❌ → "reminds me of the importance" ✓。' },
    { step: '句型转换', time: '5', content: '【PPT P6 练习】教师给主动句，学生改为被动。例：Poachers are killing antelopes. → Antelopes are being killed by poachers. / Volunteers are watching over the animals. → Animals are being watched over by volunteers. 预设回答造句。板书时机：板书转换公式。差异化提示：B班给转换框架；A班独立改并说语义变化。易错点提醒：转换后看主语—谓语是否一致：单数用 is being done，复数用 are being done。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】回顾被动语态功能（突出受事+强调紧迫）+语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节语法课系统讲练现在进行时的被动语态，预习课文中的被动句。' }
  ],
  blackboard: '┌─ U2 Reading II: Language Focus ───────────┐\n│ Present Continuous Passive:                │\n│  am/is/are + BEING + past participle (V-ed)│\n│                                            │\n│ Active → Passive (urgency ↑):              │\n│  People destroy habitats. (fact)           │\n│  Habitats are destroyed. (state)           │\n│  Habitats are BEING destroyed. (URGENT!)   │\n│                                            │\n│ Text examples:                             │\n│  "Their habitats are being destroyed."     │\n│  "Measures are being taken to protect..."  │\n│  "The antelopes are being watched over..." │\n└────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出4个现在进行时被动语态句子并标注 being + V-ed。2. 将以下句子改为被动：Poachers are hunting the antelopes illegally. 【提高作业】用现在进行时的被动语态写3句关于其他濒危动物处境的句子（如老虎/大象/鲸鱼）。【参考答案——教师用】基础2示例：The antelopes are being hunted illegally by poachers.',
  reflection: '✅ 亮点：主动→被动三句对比让学生直观感受"紧迫感"，参与度高。⚠️ 需改进：being 遗漏仍是常见问题，语法课需大量操练。📌 下节课衔接：进入语法课，系统操练现在进行时的被动语态在各种语境下的运用。'
}));

// ====== Period 4: Grammar (现在进行时的被动语态) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u2-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '被动语态', '现在进行时', '野生动物保护', '人教版必修二U2', '第四节课'],
  textbookAnalysis: '本课为必修第二册 Unit 2 第四课时（Discovering Useful Structures），系统教学现在进行时的被动语态（am/is/are being + past participle）。基于 Reading 语篇中提取的例句，引导学生归纳出"何时使用进行时被动"的规则——强调动作正在发生、突出受事者的紧迫处境。通过野生动物保护主题的语境化练习（栖息地被破坏、保护措施正在实施）巩固语法，为后续海报写作做语言准备。',
  overview: '【学情分析】A班：掌握一般现在时被动，但进行时被动（is being done）易与进行时主动（is doing）混淆。B班：被动语态结构整体不熟，需从 be + done 基础复习再引入 being。共同问题：写作中要么从来不用被动，要么一用就漏 being。',
  objectives: [
    '语言能力：准确构建现在进行时的被动语态句子，在野生动物保护话题中产出 5 个以上正确句子。',
    '文化意识：通过被动语态聚焦"正在受威胁的动物与栖息地"，强化生态保护意识。',
    '思维品质：通过"发现例句→归纳规则→对比辨析→应用输出"的归纳法培养语法学习策略。',
    '学习能力：建立"被动语态自查表"——写作后自行检查 being 是否遗漏、过去分词形式是否正确。'
  ],
  keyPoints: '① 现在进行时被动语态：am/is/are + being + V-ed（过去分词）② 使用场景：强调动作"正在被进行"且受事者比施事者更重要 ③ 与一般现在时被动的区别：一般现在时=常态/事实，进行时=此刻/紧迫 ④ 不规则过去分词复习（take→taken, make→made, put→put, set→set）',
  difficulties: '① being 的发音与拼写 — 学生写 is been done（错用 been）或 is being destroy（忘加 -ed）。原因：being/been 混淆。② 某些动词无进行时被动（如 belong / cost / have）— 学生强行套用。③ 不规则过去分词记错 — take→taken 不是 took，make→made 不是 maked。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→练习 ② 情境造句：给保护区管理图片用被动描述 ③ 改错+竞赛：找出被动语态典型错误。',
  preparation: '【PPT课件】P1 现在进行时被动公式分解；P2 课文例句摘录；P3 与一般现在时被动对比表；P4 主动→被动转换流程图；P5 情境造句任务卡；P6 改错题；P7 总结。【实物教具】改错卡每人一套；情境图片卡一套。',
  process: [
    { step: '例句发现', time: '7', content: '【PPT P2 例句】展示课文中3个被动句+新给3个：①The reserve is being expanded. ②More volunteers are being trained. ③Illegal traps are being removed. 学生圈"is/are + being + V-ed"。教师：What is the pattern? What does "being" mean? 预设回答：is/are + being + past participle. "Being" means something is happening right now. 板书时机：左栏板书3句，红笔标 being + V-ed。差异化提示：B班只圈 being；A班分析主语是单数还是复数。易错点提醒：being 在这里是助动词，不是名词"存在/生物"——不要混淆。' },
    { step: '规则归纳', time: '10', content: '【PPT P3 对比表】教师对比三种时态被动：①Habitats are destroyed.（一般现在时=常态事实）②Habitats were destroyed.（一般过去时=已发生）③Habitats are being destroyed.（现在进行时=正在被破坏，更紧急）。教师：When do we use the present continuous passive? 预设回答：When we want to say something is happening right now and we care about the thing/person affected. 板书时机：三列对比板书，being 用红色。差异化提示：B班填已给表格（时态/结构/含义）；A班自己画表+每个句型造1句。易错点提醒：一般现在时被动≠现在进行时被动！is destroyed = 已被破坏（无了），is being destroyed = 正在被破坏（还剩点）。' },
    { step: '主动→被动转换', time: '8', content: '【PPT P4 转换流程】教师示范转换五步：①找宾语→②宾语变主语→③确定be形式（is/am/are）→④加being→⑤动词变过去分词。例：They are training volunteers. → Volunteers are being trained. 预设回答跟做。板书时机：板书五步流程图。差异化提示：B班跟做每一步；A班独立完成后再设计一个自己的例句。易错点提醒：主动句如果没有宾语，不能变被动！"The antelopes are running"（不及物）→ 无法变被动。' },
    { step: '情境造句', time: '8', content: '【PPT P5 图片卡】展示4张图（巡逻员设陷阱保护、志愿者记录数据、游客拍照、栖息地修复），学生用被动描述。教师：What is happening in this picture? Use passive voice! 预设回答：Illegal traps are being removed by rangers. / Data is being collected. / The habitat is being restored. 板书时机：巡视指导。差异化提示：B班给动词提示（remove/collect/restore）；A班不给提示自由造句。易错点提醒：restore → restored（加 -d，不是 -ed），注意不规则拼写。' },
    { step: '改错竞赛', time: '5', content: '【PPT P6 改错】展示 4 个典型错误：①The animals is being protect.（protect 缺 -ed）②Habitats are been destroyed.（been 应为 being）③Measures are being took.（took 应为 taken）④The reserve is being belonged to the state.（belong 无被动）。学生组间竞赛纠错。预设回答纠错。板书时机：板书错误→改正+规则。差异化提示：B班判对错；A班解释为什么错+给出规则。易错点提醒：无被动动词（belong/cost/happen/appear/last）不能被用于被动语态，不管什么时态。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾公式 am/is/are + being + V-ed + 使用场景 + 常见错误。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班说出今天学到的3条规则。易错点提醒：写作后自查——每句被动是否漏了 being？过去分词拼对了吗？' }
  ],
  blackboard: '┌─ U2 Grammar: Present Continuous Passive ──┐\n│  am/is/are + BEING + past participle (V-ed)│\n│                                             │\n│  Tense Comparison:                          │\n│   Simple Present:  is/are + V-ed (常态)     │\n│   Simple Past:     was/were + V-ed (已发生) │\n│   Present Cont.:   is/are + BEING + V-ed    │\n│                    (正在被… → 紧迫!!)       │\n│                                             │\n│  Active→Passive 5 Steps:                    │\n│   宾→主 + be (is/are) + being + V-ed        │\n│                                             │\n│  ❌ is been done  → ✓ is being done         │\n│  ❌ is being took → ✓ is being taken        │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 用现在进行时被动语态造 5 句关于动物保护的句子。2. 改错：The reserve is being expand / Measures are been taken / The animals are being protect.【提高作业】写 60 词短文描述当地一个正在进行的环保项目（用至少 3 个现在进行时被动语态）。【参考答案——教师用】基础1示例：The wetland is being restored. / More trees are being planted. / Volunteers are being trained to protect the birds.',
  reflection: '✅ 亮点：三时态对比表+改错竞赛让语法操练有趣有效。⚠️ 需改进：being/been 混淆仍需反复纠正，听与谈课可以融入被动语态口头练习。📌 下节课衔接：听与谈聚焦野生动物保护的讨论，口头运用被动语态描述保护措施。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u2-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '野生动物保护', '讨论', '人教版必修二U2', '第五节课'],
  textbookAnalysis: '本课为必修第二册 Unit 2 第五课时（Listening and Talking），语境为"讨论如何帮助保护濒危野生动物"。听力材料为一段关于野生动物保护组织活动的对话，口语输出任务为就某种濒危动物的保护措施进行讨论。功能语言为表达意图与计划（I intend to... / I plan to... / I\'m going to...）及回应建议（That sounds great! / That\'s a wonderful idea! / I\'d love to, but...）。结合语法课的被动语态，在口语中自然运用 is/are being done 描述保护行动。',
  overview: '【学情分析】A班：能提出保护建议，但缺乏"计划+目的"的完整表达链。B班：开口意愿低、intend/plan 等动词不熟。共同问题：只说想做什么但不说为什么——缺少 so that / in order to 目的表达。',
  objectives: [
    '语言能力：听懂关于野生动物保护计划的对话，提取活动内容与目的；能用至少 4 种句型表达保护意图并说明目的。',
    '文化意识：体会"个人行动也能为野生动物保护做出贡献"的参与意识。',
    '思维品质：在讨论中练习"表达计划→说明目的→邀请/回应同伴"的完整对话链。',
    '学习能力：通过意图表达对话训练批判性倾听——听懂同伴的计划后给出有针对性的回应。'
  ],
  keyPoints: '① 表达意图句型：I intend to... / I plan to... / I\'m going to... / I\'m thinking of + doing ② 目的表达：so that... / in order to... / to help... ③ 回应句型：That sounds great! / What a brilliant idea! / I\'d love to join you.',
  difficulties: '① intend to do（打算做）学生易写成 intend doing（少见用法，to do 更自然）。原因：plan to do 的干扰。② so that + 从句（有主语+谓语）≠ in order to + 动词原形——学生混用。③ 回应时只说 "OK" 不给具体回应——需培养说"为什么好"或"有什么顾虑"的意识。',
  teachingMethods: '① 听前预测→听中配对→听后产出。② 角色扮演：志愿者招募面试。③ 野生动物保护计划圆桌讨论。',
  preparation: '【PPT课件】P1 野生动物保护组织活动图片（志愿巡逻/筹款/宣传教育）；P2 意图表达句型板；P3 听力任务题；P4 听力任务卡；P5 回应句型板；P6 角色卡。【实物教具】保护计划信息卡 printed；角色卡（申请人/面试官）。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 活动图片】教师：Look at these pictures. What are these people doing for wildlife? If you had a free weekend, what would you do to help animals? 预设回答：Pick up trash. / Tell people about endangered animals. / Volunteer at a reserve. 板书时机：左栏板书 intend to / plan to / volunteer / donate。差异化提示：B班中文说再翻英文；A班直接英文+说原因。易错点提醒：volunteer /vɒləntɪə/ 重音在最后一个音节，-teer 读 /tɪə/ 不是 /tɪr/。' },
    { step: '听力抓计划', time: '10', content: '【PPT P3 听力任务】听对话，抓"谁计划做什么+什么目的"。教师：Listen for: What does each speaker intend to do? Why? 预设回答：Speaker A intends to volunteer at a bird reserve. Speaker B plans to donate money. 板书时机：配对填表（人物|计划|目的）。差异化提示：B班给配对连线题；A班听写关键词+写目的句。易错点提醒：intend to do — to 不能少，不是 "intend doing" 虽然语法上可接受但在高中阶段推荐用 to do。' },
    { step: '听中记录', time: '8', content: '【PPT P4 听力任务卡】【音频】重听，学生填完整意图+目的+回应链。教师：How did the other person respond? Were they interested? 预设回答：Yes! She said "That\'s a wonderful idea! I\'d love to join." 板书时机：核对填表。差异化提示：B班给回应选项（A/B/C选）；A班写完整回应句。易错点提醒：I\'d love to = I would love to — 后面省略了上文提到的动词，是英语中最自然的接受邀请方式。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练意图+目的链：A: I intend to volunteer at the reserve this Saturday. / B: Why? / A: Because I want to help protect the birds. So that more chicks can survive. / B: That sounds great! Can I join you? 预设回答跟读+仿造。板书时机：板书意图→目的→回应链条。差异化提示：B班用填空脚本；A班自主对话+替换活动名。易错点提醒：so that 后面跟完整句子（有主语+谓语），而 in order to 后面跟动词原形——"so that to help" 是错的。' },
    { step: '角色扮演', time: '8', content: '【PPT P6 角色卡】两人一组：Interviewer（面试官）和 Volunteer（申请者）。面试官问"你有什么计划？为什么想加入？"，申请者回答。教师巡视。预设回答：I intend to help count the antelopes. I plan to use my photography skills to document wildlife. 板书时机：留句型供参考。差异化提示：B班照卡读；A班脱稿加即兴问题。易错点提醒：角色扮演中用被动语态描述活动——"The data is being collected by volunteers every weekend." 增加语言质量。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾表达意图句型+目的连接词+回应策略。教师：Remember: Say what you plan AND why. 预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一句自己的保护计划。易错点提醒：I\'m thinking of + doing（考虑做某事）不是 I\'m thinking to do。' }
  ],
  blackboard: '┌─ U2 Listening & Talking ───────────┐\n│ Intentions:                          │\n│  I intend to + do...                │\n│  I plan to + do...                  │\n│  I\'m thinking of + doing...         │\n│  I\'m going to + do...               │\n│                                      │\n│ Purpose:                             │\n│  so that + clause                   │\n│  in order to + do...                │\n│  to help + do...                    │\n│                                      │\n│ Responses:                           │\n│  That sounds great! / Wonderful!    │\n│  I\'d love to join you!              │\n└──────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有表达意图的句型。2. 用 I intend to... / I plan to... 各写 1 句自己的野生动物保护计划+目的。【提高作业】写 60 词对话：两人讨论周末一起去参加野生动物保护志愿活动（至少 4 轮，含意图+目的+回应）。【参考答案——教师用】基础2示例：I intend to volunteer at the local wildlife rescue center so that I can help injured birds. / I plan to donate 100 yuan every month in order to support panda conservation.',
  reflection: '✅ 亮点：意图+目的+回应三段链让学生表达更完整，不再只说半句话。⚠️ 需改进：so that / in order to 的区分仍需单独练习。📌 下节课衔接：进入写作 I，将讨论中的保护计划写成正式的海报。'
}));

// ====== Period 6: Writing I (海报结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u2-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '海报', '野生动物保护', '人教版必修二U2', '第六节课'],
  textbookAnalysis: '本课为必修第二册 Unit 2 第六课时（Reading for Writing I），写作体裁为制作有效的野生动物保护海报（Make an Effective Poster）。海报结构为：醒目标题→震撼图片/数据→问题陈述→行动号召→联系方式。语言重点为海报特有的简短有力句型（Help us save...! / Don\'t let... disappear! / Act now!）及数据引述。结合本单元 Reading 的记叙文细节与语法课的被动语态，实现"读-语法-写"闭环。',
  overview: '【学情分析】A班：有写作能力但不知道海报文案和普通作文的区别——海报需要极简有力的语言。B班：句型储备少、不知从何写起，需大量范例+模板。共同问题：海报标题不够"抓人"——写成长句而非口号式标题。',
  objectives: [
    '语言能力：掌握海报文案的"标题→问题→数据→呼吁"四要素结构，产出 60-80 词结构完整、有感染力的野生动物保护海报。',
    '文化意识：理解海报在公众传播中的力量，能用英文制作有影响力的保护倡议。',
    '思维品质：通过"先选动物→再找数据→提炼标题→组织文案"训练从信息到传播的设计思维。',
    '学习能力：建立"海报文案≠作文"的意识——学会极简有力、口号式的英文表达。'
  ],
  keyPoints: '① 海报四要素：Catchy Title → Shocking Fact/Data → Why It Matters → Call to Action ② 海报句型：Help us save...! / Don\'t let... disappear! / ... are being killed every day. / Act now before it\'s too late! ③ 被动语态在海报中的应用：强调受威胁的动物。',
  difficulties: '① 海报标题的"口号化"——学生习惯写完整句"This is a poster about protecting tigers"而非"Save the Tigers!"。② 数据引述格式——数字+单位+来源。③ 被动语态在海报中的语气控制——不要太学术，要保持情感冲击力。',
  teachingMethods: '① 范本解构法：分析优秀海报→提取要素→仿写。② 头脑风暴：各组选一种动物列关键信息。③ 过程写作：outline→draft→peer review（下节课）。',
  preparation: '【PPT课件】P1 优秀野生动物保护海报范例（WWF等）；P2 海报四要素结构图；P3 海报句型库；P4 头脑风暴工作单；P5 写作任务；P6 写作提纲；P7 总结。【实物教具】A4纸每人一张；彩笔；海报范例打印版。',
  process: [
    { step: '范本解构', time: '8', content: '【PPT P1 海报范例】教师展示 2-3 张经典野生动物保护海报（英文），学生标注四要素：标题/数据/原因/呼吁。教师：Which poster makes you want to act? Why? 预设回答：The one with the tiger — the title "Save the Tigers!" is powerful. The data "Only 3,900 left" is shocking. 板书时机：四要素板书于黑板。差异化提示：B班给标注好的范例只匹配要素名称；A班自己标注+评语"为什么有效"。易错点提醒：海报标题的核心技巧——用动词开头（Save/Stop/Protect/Help），比名词标题有力 10 倍。' },
    { step: '四要素讲透', time: '8', content: '【PPT P2 结构图】教师逐要素讲解：①Title: 简短口号（3-5词），动词开头。②Data: 震撼数字 —— "Only ___ left." "___ are killed every ___." ③Why: 1-2句说明为什么重要（生态价值/人类责任）。④Call: 行动号召 —— "Act now!" "Join us!" "Donate at..." 教师用藏羚羊示范各要素。预设回答跟做。板书时机：逐要素板书模板句。差异化提示：B班给每要素填空模板；A班给关键词自己写。易错点提醒：③Why 不要写成议论文——1-2句足够。海报读者注意力只有 3 秒，长句直接被忽略。' },
    { step: '海报句型库', time: '5', content: '【PPT P3 句型库】教师领读海报高频句型：Help us save...! / Don\'t let... disappear! / ... are being killed every day. / If we don\'t act now, ... / Every ... counts! / Join the fight! 教师强调被动语态在海报中的情感效果："are being killed"比"people kill"更能让读者同情动物。预设回答跟读+感受。板书时机：句型分类板书（标题句/数据句/呼吁句）。差异化提示：B班齐读+背3句；A班选最打动自己的1句说为什么。易错点提醒：感叹号在海报中可以用，但要节制——1个标题用就够，全文不超过3个感叹号。' },
    { step: '头脑风暴', time: '5', content: '【PPT P4 工作单】学生各自选一种濒危动物思考：①What is a catchy title? ②What is the most shocking fact? ③Why should people care? ④What should people do? 教师巡视指导。预设回答：Title: "Save the Snow Leopards!" / Fact: "Only 4,000 remain in the wild." / Why: "They are the guardians of the mountains." / Call: "Adopt a snow leopard today!" 板书时机：巡视指导。差异化提示：B班用填空式工作单；A班独立填。易错点提醒：数字一定要准确——不要编数据。"about 4,000" 可以用，但不要随便说"only 100"。' },
    { step: '起草海报', time: '10', content: '【PPT P5 写作任务】学生用 A4纸起草海报。要求：四要素齐全、至少 1 个被动语态、至少 1 个数据。教师巡视提醒：标题要大！数据要显眼！教师：Your title should be the BIGGEST thing on the page. 预设回答：（学生制作海报草稿中）板书时机：留四要素模板供参考。差异化提示：B班用模板写文字；A班还考虑字体大小/颜色对比等设计。易错点提醒：海报文字不在多而在精——全文字数控制在 60-80 词，不要写小作文。' },
    { step: '同伴初评', time: '4', content: '【PPT P6 写作提纲】同桌互换海报草稿，check：有四要素吗？标题够吸引吗？数字准确吗？有被动语态吗？教师：Give your partner one compliment and one suggestion. 预设回答：Your title is catchy! Maybe add a data point. 板书时机：留 checklist。差异化提示：B班用 checklist 表逐项打勾；A班口头给改进建议。易错点提醒：互评不是比谁画得好看——重点评文案内容和信息传达力。' }
  ],
  blackboard: '┌─ U2 Writing: Effective Poster ──────────────┐\n│  ① CATCHY TITLE (3-5 words, verb first!)     │\n│     Save the...! / Protect...! / Stop...!     │\n│  ② SHOCKING DATA                              │\n│     Only ___ left. / ___ killed every ___.    │\n│  ③ WHY IT MATTERS (1-2 short sentences)       │\n│  ④ CALL TO ACTION                              │\n│     Act now! / Join us! / Donate at...!        │\n│                                                │\n│  Voice: Use passive for emotional impact!      │\n│  "are being killed" > "people kill"            │\n└────────────────────────────────────────────────┘',
  exercises: '【基础作业】按课堂草稿完成 60-80 词野生动物保护海报文字稿。要求：四要素完整、至少 1 个被动语态、至少 1 个数据。【提高作业】将文字稿设计成 A4 海报（可手绘+彩笔或用 Canva），下节课展示。【参考答案——教师用】示例（藏羚羊海报）：Title: "SAVE THE TIBETAN ANTELOPE!" / Data: "Once reduced to 50,000 — now recovering, but still threatened." / Why: "These graceful creatures are symbols of the Tibetan Plateau. Their survival depends on us." / Call: "Join Changtang conservation! Donate at www.wildlifechina.org."',
  reflection: '✅ 亮点：四要素结构让海报制作有章可循，不再"不知从何写起"。⚠️ 需改进：数据引述的准确性仍需强调，部分学生编造数据。📌 下节课衔接：进入写作 II，完善海报设计+展示评选。'
}));

// ====== Period 7: Writing II (互评+修改+展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u2-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '海报', '野生动物保护', '人教版必修二U2', '第七节课'],
  textbookAnalysis: '本课为必修第二册 Unit 2 第七课时（Writing II），在 Writing I 海报草稿的基础上完成"互评→修改→展示→终稿"闭环。重点训练学生用同学反馈改进海报文案的能力。互评量表聚焦三维度：内容完整（四要素齐全）、语言质量（被动语态/海报句型/数据准确）、视觉冲击力（标题够大/数据显眼/图文搭配）。',
  overview: '【学情分析】A班：能辨别海报好坏，但给反馈时只说"画得好看"缺乏对文案的具体建议。B班：改自己的海报时不知从何下手。共同问题：互评流于表面（只看图不读文字），不会用检查量表逐项给分。',
  objectives: [
    '语言能力：能根据互评量表给同伴的海报文案提具体、可操作的修改建议，重点检查被动语态和海报句型的使用。',
    '文化意识：通过阅读同伴的海报了解不同濒危动物的保护需求，扩展保护视野。',
    '思维品质：在互评中培养"识别传播效果→提出优化方案"的批判性反馈能力。',
    '学习能力：建立"写→评→改→展"四步海报制作流程，内化为个人创作习惯。'
  ],
  keyPoints: '① 互评三维量表：内容（四要素齐全 / 数据准确）+ 语言（被动语态≥1 / 海报句型≥2 / 词汇恰当）+ 视觉（标题突出 / 数据显眼 / 排版清晰）② 海报展示技巧：30 秒内讲清"什么动物/什么问题/读者该做什么"',
  difficulties: '① 学生互评海报时只关注图画不关注语言——需强制"先读文字再评设计"。② 海报数据错误的纠正——学生常写"Only 10 left"无依据。③ 展示节奏控制——海报展示不等于读海报，而是用口语解释海报为什么有效。',
  teachingMethods: '① 量表互评：用统一标准减少主观性。② 画廊漫步：海报贴墙上全班巡评。③ 最佳海报评选+颁奖。',
  preparation: '【PPT课件】P1 互评三维量表；P2 常见问题（标题弱/缺数据/无被动/数据不准）；P3 修改指南；P4 展示技巧（30秒公式）；P5 最佳海报范例；P6 自评表；P7 总结。【实物教具】互评量表 printed 每人一份；红笔/便利贴；投票贴纸。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①内容（四要素全？数据有来源？）②语言（被动语态≥1？海报句型≥2？拼写正确？）③视觉效果（标题最大？数据突出？不拥挤？）。教师用上节课自己的海报示范打分。预设回答跟学。板书时机：量表三维板书于黑板。差异化提示：B班按量表逐项打勾；A班还需写一句"如果这是我的海报，我会改哪里"。易错点提醒：互评不是比谁画得好——是帮对方把文案改得更有传播力。' },
    { step: '互评', time: '12', content: '【PPT P2 常见问题】先展示上节课常见问题：①标题太弱（"This is a poster about pandas" 而非 "Save Pandas!"）②无被动语态 ③数据无来源。然后同桌互换海报，用红笔按量表标注。教师巡视。教师：Give one compliment and one suggestion about the LANGUAGE. 预设回答：Your title is strong, but you didn\'t use passive voice. Try "are being hunted." 板书时机：留量表供参考。差异化提示：B班按 checklist 勾；A班在稿上写具体修改建议。易错点提醒：提建议时先夸后改——"I love your title! Maybe add a shocking number in the data section?"' },
    { step: '修改', time: '10', content: '【PPT P3 修改指南】学生根据互评反馈修改海报。顺序：①先补内容（缺哪要素补哪）②再调语言（插入被动语态/海报句型）③最后调视觉（标题加粗/数据放大）。教师：Fix content first, then language, then design. 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完还润色句型多样性。易错点提醒：修改不是重做——保留好的部分，只改薄弱处。最好的海报改 2-3 处就能提升很多。' },
    { step: '画廊漫步+投票', time: '8', content: '【PPT P4 展示技巧】海报贴墙上，全班用便利贴给每张海报打分（内容/语言/设计 各1星）。教师：Write one thing you learned from another poster. 预设回答：I learned that "only 3,900 left" is a very powerful way to present data. 板书时机：留投票维度。差异化提示：B班用贴纸投票；A班还写一句学习笔记。易错点提醒：从别人的海报中学习——记下你觉得有效的句型和设计，下次用在自己的作品中。' },
    { step: '结课+自评', time: '5', content: '【PPT P7 总结+自评】宣布最佳海报前三名。学生自评：①我的海报最大的优点是？②如果再做一张，我会怎么改进？教师：What did you learn about making an effective poster? 预设回答：Titles must be short and powerful. Data makes it real. Passive voice makes people feel for the animals. 板书时机：写最优海报的标题作为范例。差异化提示：B班中文自评；A班英文自评。易错点提醒：海报的终极测试——给一个没听过这个话题的人看 3 秒，他能记住什么？你的标题就是那个答案。' }
  ],
  blackboard: '┌─ U2 Writing II: Poster Gallery ──────┐\n│ Review Checklist:                      │\n│  ✅ Content: Title / Data / Why / Call │\n│  ✅ Language: ≥1 passive / ≥2 poster   │\n│     phrases / accurate data            │\n│  ✅ Visual: Title BIG / Data VISIBLE    │\n│                                        │\n│ Poster Pitch (30 sec):                 │\n│  "This poster is about...              │\n│   They are being threatened by...      │\n│   You can help by..."                  │\n└────────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改海报终稿，拍照提交。写 20 词英文反思：我的海报最打动人的是哪部分？【提高作业】选另一濒危动物再设计一张海报文字稿（60-80词），比较两种动物的保护需求有何不同。【参考答案——教师用】反思示例：The most powerful part of my poster is the data "Only 4,000 snow leopards remain." I learned that numbers make people care more than general statements.',
  reflection: '✅ 亮点：画廊漫步让互评可视化，便利贴打分参与率高。⚠️ 需改进：部分海报数据仍不准确，下次写作前可要求标注数据来源。📌 下节课衔接：进入 Project，将本单元所学整合为"濒危动物保护宣传展"。'
}));

// ====== Period 8: Project (濒危动物保护宣传展) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u2-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '野生动物保护', '展览', '人教版必修二U2', '第八节课'],
  textbookAnalysis: '本课为必修第二册 Unit 2 第八课时（Project），为单元终极产出课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的保护词汇+阅读的叙述与数据+语法的被动语态+听与谈的意图表达+写作的海报——完成一份"濒危动物保护宣传展"展板/多媒体展示。综合考查语言能力（词汇/语法/写作）、思维品质（信息组织）和学习能力（合作分工）。',
  overview: '【学情分析】A班：能独立完成分工作品，但需要明确评分标准。B班：group work 中易"搭便车"，需明确定人定责+互评贡献度。共同问题：小组合作时语言切换回中文——需设立"英文监督员"角色。',
  objectives: [
    '语言能力：综合运用本单元词汇、被动语态、意图表达句型、海报句型，以英文完成一份濒危动物保护宣传展板（动物介绍/威胁/保护措施/呼吁/海报）。',
    '文化意识：通过展览形式向同伴传播野生动物保护理念，理解生物多样性保护的重要性。',
    '思维品质：在4人小组中合理分工、有效协作，培养项目管理思维。',
    '学习能力：回顾本单元5课学习内容，建立"一个单元学什么、怎么用"的整体框架感。'
  ],
  keyPoints: '① 展板五模块：Animal Profile（简介）→ Threats（威胁+数据）→ Conservation（正在实施的保护措施）→ How to Help（读者可以做什么）→ Mini Poster（海报） ② 单元知识整合：保护词汇/被动语态/意图表达/海报句型 ③ 小组分工：Researcher / Writer / Designer / Presenter各司其职',
  difficulties: '① 展板的 Conservation 模块需用现在进行时被动语态描述正在实施的措施——学生容易忘用被动。② 五模块之间的逻辑衔接——不是五个独立的块，而是一条说服链。③ 展示时间控制——2分钟/组，超时扣分。',
  teachingMethods: '① PBL项目式学习：以宣传展为驱动问题。② 小组协作：角色分工+模块checklist。③ 展览+最佳展板评选。',
  preparation: '【PPT课件】P1 单元回顾五课内容（思维导图）；P2 展板五模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed；积分卡。',
  process: [
    { step: '单元回顾', time: '5', content: '【PPT P1 思维导图】教师带学生回顾本单元5课学了什么：听与说（濒危动物词汇+关切表达）→阅读（A DAY IN THE CLOUDS叙事+数据）→语法（is/are being done）→听与谈（意图+目的+计划）→写作（海报四要素）。教师：Today we bring it all together — make an exhibition! 预设回答跟读回顾。板书时机：左栏画五课链接图。差异化提示：B班看PPT读关键词；A班自己说出每课学到的核心内容。易错点提醒：展板每模块至少用一次现在进行时被动语态——这是单元核心语法。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 展板结构】【PPT P3 角色卡】教师展示展板五模块：①Animal Profile（选一濒危动物+简介+照片）②Threats（威胁+震撼数据）③Conservation（正在实施的保护措施——用被动语态！）④How to Help（读者能做的3件事）⑤Mini Poster（完整的号召海报）。角色分工：Researcher查信息 / Writer写文案 / Designer设计排版 / Presenter准备展示。教师：Choose your animal and role! 预设回答：We choose the snow leopard. I\'ll be the researcher. 板书时机：留模块结构和角色。差异化提示：B班给语言模板；A班自由创作。易错点提醒：Researcher 的数据必须真实——百度/WWF 官网查，不要编。' },
    { step: '制作展板', time: '16', content: '【PPT P4 范例参考】【实物 A3纸】小组制作。教师要巡视提醒：①全英文！②每模块至少2句完整句 ③至少2个被动语态 ④数据要标注来源 ⑤最后3分钟 Presenter 准备展示。预设回答：（小组讨论制作中，教师巡视指导）板书时机：无。差异化提示：B班给每模块句型开头提示；A班独立完成+追求语言多样性。易错点提醒：五模块要有逻辑流——不是五个独立块，而是"这是什么动物→为什么危险→正在做什么→你该做什么→记住我们的话"。' },
    { step: '展示评价', time: '10', content: '【PPT P5 量规】每组 2 分钟展示。全班投票：最佳内容/最佳设计/最佳展示/最想行动起来的。教师：You have 2 minutes. Make us care about your animal! 预设回答展示。板书时机：记投票结果。差异化提示：B班可看展板讲；A班脱稿补充。易错点提醒：2分钟分配——30秒介绍动物+30秒说威胁+30秒说保护+30秒呼吁。不要在某一部分拖太久。' },
    { step: '单元自评', time: '3', content: '【PPT P6 自评表】学生勾选四维薄弱项：保护词汇记不住？被动语态不会用？意图表达忘了？海报结构不熟？写1条补强计划。教师：Be honest. What will you review this weekend? 预设回答：I need to practice the present continuous passive. I will review the grammar table and do 5 exercises. 板书时机：留自评四维。差异化提示：B班中文写；A班英文写。易错点提醒：补强计划要具体——"复习被动语态"太笼统，应该写"用 is/are being done 造5句关于老虎的句子"。' }
  ],
  blackboard: '┌─ U2 Project: Wildlife Exhibition ────┐\n│ 🦌 Exhibition 5 Modules:               │\n│  ① Animal Profile (who is it?)        │\n│  ② Threats (what\'s happening?)        │\n│  ③ Conservation (what\'s being done?)  │\n│  ④ How to Help (what can YOU do?)     │\n│  ⑤ Mini Poster (call to action!)      │\n│                                        │\n│ 👥 Roles: Researcher / Writer /        │\n│            Designer / Presenter        │\n│                                        │\n│ ⭐ Must: English / ≥2 passive / data   │\n│          with source / 5 modules       │\n└────────────────────────────────────────┘',
  exercises: '【基础作业】完成小组展板（未完成的继续做），拍照片提交。写 30 词英文反思：我的角色是…从项目中我学到了…【提高作业】搜索了解 IUCN Red List（世界自然保护联盟红色名录），找一种"极危"（Critically Endangered）动物写 50 词英文简介。【参考答案——教师用】反思示例：I was the writer. I wrote the threats and conservation modules. I learned how to use present continuous passive to describe ongoing protection efforts. Next time I will double-check data sources before writing.',
  reflection: '✅ 亮点：五模块展板整合全单元，学生产出有成就感。⚠️ 需改进：16分钟制作时间偏紧，下次可给20分钟+提前布置数据查找作业。📌 下节课衔接：进入 Unit 3 The Internet，从自然保护转向数字世界的连接与改变。'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b2-u2-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b2-u2 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
