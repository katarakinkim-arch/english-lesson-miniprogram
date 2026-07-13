/**
 * gen-b2-u5.js — 必修第二册 Unit 5 Music (8课时)
 * 
 * 语篇: THE VIRTUAL CHOIR (Eric Whitacre's story)
 * 语法: 过去分词作状语 (Moved by..., Inspired by..., Known as...)
 * 写作: Write a Speech About How Music Has Changed Your Life
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
const UNIT = 5;
const UNIT_TITLE = 'Music';
const BOOK = '必修第二册';

const periods = [];
let pn = 0;

// ====== Period 1: Listening and Speaking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u5-ls', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-speaking', lessonTypeName: '听与说',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与说', '音乐', '音乐类型', '人教版必修二U5', '第一节课'],
  textbookAnalysis: '本课为必修第二册 Unit 5 Music 第一课时（Listening and Speaking），属单元导入+输入环节。语篇为一段关于音乐偏好的对话与不同音乐类型的介绍音频，功能语境是"谈论音乐偏好与感受"。语言重点为音乐类型词汇（classical, pop, rock, jazz, folk, hip-hop, electronic, orchestra）及表达偏好句型（I prefer... / I\'m a fan of... / ... moves me. / ... gives me energy.）。为 Reading 语篇"THE VIRTUAL CHOIR"中音乐与科技结合的叙事做词汇与话题预热。',
  overview: '【学情分析】A班：对音乐话题有浓厚兴趣，知道 pop/rock/classical 等常见类型但 electronic/orchestra 等较生疏。B班：部分音乐类型英文名不会读（如 genre /ʒɒnrə/）。共同问题：描述音乐感受时只会说 good 和 nice，缺乏 moves/energizes/calms 等情感动词。',
  objectives: [
    '语言能力：听懂关于音乐偏好的对话，提取关键信息（类型/感受/原因），准确使用 8-10 个音乐相关词汇。',
    '文化意识：了解不同音乐类型的文化背景，形成对多元音乐文化的欣赏态度。',
    '思维品质：通过"听前预测—听中分类—听后反思"训练音乐主题听力策略。',
    '学习能力：能用 I prefer... because... / ... moves me. / ... gives me energy. 描述自己的音乐偏好与感受。'
  ],
  keyPoints: '① 音乐类型核心词汇：classical / pop / rock / jazz / folk / hip-hop / electronic / orchestra / genre ② 表达偏好与感受句型：I prefer... / I\'m a fan of... / ... moves me. / ... calms me down. / ... gives me energy. ③ 听力微技能：听前看歌名预测音乐类型、听中抓感受词。',
  difficulties: '① genre /ʒɒnrə/ 发音 — 法语外来词，g 读 /ʒ/ 不读 /dʒ/，结尾 e 不发音。② orchestra /ɔːkɪstrə/ 拼写 — 学生易写成 orchastra。③ move（使感动）的用法 — 学生只知"移动"义。"The music moved me." = 音乐打动了我。',
  teachingMethods: '① 任务型（TBL）：以制作"班级音乐推荐歌单"为终任务。② 听前预测+听中分类：音乐类型+感受配对。③ 对子互问操练偏好表达。',
  preparation: '【PPT课件】P1 单元封面（Music）；P2 音乐类型图标九宫格（古典/流行/摇滚/爵士/民谣/嘻哈/电子/管弦乐/合唱）；P3-4 听力任务题；P5 偏好表达句型板；P6 歌单任务卡。【实物教具】音乐类型信息卡 printed 每组一套；音响/音频播放设备。【音频】听力两段音频+每种音乐类型的30秒片段。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P2 九宫格+音乐片段】教师播放 8 种音乐类型各 15 秒片段。教师：Can you guess the genre? Which one do you like? 预设回答：That\'s rock! I love it. / That\'s classical — it\'s so calm. 板书时机：右侧板书 genre / classical / pop / rock / jazz / folk / hip-hop / electronic / orchestra。差异化提示：B班指图说音乐类型；A班用 This sounds like... / I think this is... 表达。易错点提醒：genre /ʒɒnrə/ — 这是从法语借来的词，读法和拼写不同步。' },
    { step: '词汇输入', time: '8', content: '【PPT P3 词卡】教师领读 music genre 词汇+感受动词。感受动词：move（使感动）/ energize（使充满能量）/ calm down（使平静）/ cheer up（使振奋）/ bring back memories（唤起回忆）。教师：How does pop music make you feel? 预设回答：It gives me energy! / It cheers me up when I\'m sad. 板书时机：左栏板书词+短注释。差异化提示：B班配情绪表情符号记忆；A班用每个感受词造一句。易错点提醒：energize /enədʒaɪz/ — 重音在第一音节，来自 energy（能量）。' },
    { step: '听前预测', time: '5', content: '【PPT P4 题支】教师：We will listen to people talking about their music preferences. Predict: What genres will they mention? How will they describe the feeling? 预设回答：Pop and rock — they\'ll say it\'s energetic. Classical — they\'ll say it\'s calming. 板书时机：预测词写在黑板中部。差异化提示：B班给中文提示词；A班用英文说预测+自己的类似经验。易错点提醒：听力中感受词的近义替换——"energetic" 可能被说成 "gives me energy" / "lively" / "makes me want to dance"。' },
    { step: '听中分类', time: '10', content: '【PPT P5 分类表】【音频 段一】播放听力，学生按"类型—感受—原因"填表。教师：What genre does Speaker 1 prefer? How does it make them feel? Why? 预设回答：Classical music — it calms them down when they\'re stressed. It helps them focus when studying. 板书时机：核对答案时填表于黑板中部。差异化提示：B班给配对连线（speaker→genre→feeling）；A班一遍填全+写自己的共鸣。易错点提醒：calm down 中 down 不能省——"calms me" 语法上可以但不如 "calms me down" 地道。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师：How to talk about music preferences? I prefer... because... / I\'m a big fan of... / ... really moves me. / When I listen to..., I feel... / ... is the perfect music for... 教师示范后用同桌互问。预设回答：I prefer pop music because it gives me energy when I exercise. I\'m a big fan of Jay Chou — his lyrics really move me. 板书时机：句型板书于中央。差异化提示：B班套用模板替换音乐类型+感受；A班追加"什么时候听/为什么"的场景描述。易错点提醒：prefer 后接名词或 doing — "I prefer to listen" 和 "I prefer listening" 都可以，但 "I prefer listen" 不可以。' },
    { step: '歌单任务', time: '5', content: '【PPT P6 任务卡】学生两人一组，互相采访后为对方推荐一首歌。用：You might like... because... / If you enjoy..., try... / This song always... 教师：Recommend a song to your partner based on their music taste. 预设回答：You said you like calming music — you might like "River Flows in You" because the piano melody is so peaceful. 板书时机：留句型供参考。差异化提示：B班用填空式推荐卡；A班自由推荐+说为什么适合对方。易错点提醒：推荐时用 might —— "You might like..." 比 "You should listen to..." 更礼貌，给对方选择空间。' }
  ],
  blackboard: '┌─ U5 Listening & Speaking ───────────┐\n│ Music Genres:                         │\n│  classical / pop / rock / jazz        │\n│  folk / hip-hop / electronic          │\n│  orchestra / choir / genre /ʒɒnrə/   │\n│                                       │\n│ Feelings:                             │\n│  ... moves me. (感动)                 │\n│  ... gives me energy. (充满能量)      │\n│  ... calms me down. (平静下来)        │\n│  ... cheers me up. (振奋)             │\n│                                       │\n│ Preferences:                          │\n│  I prefer... because...               │\n│  I\'m a fan of...                     │\n│  You might like... because...         │\n└───────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读听力文本 2 遍，圈出所有音乐类型与感受词。2. 用 prefer / move / give energy 各写 1 句关于自己音乐偏好的句子。【提高作业】用英文写 50 词介绍你最喜欢的一首歌或一位歌手——包含音乐类型/什么感受/为什么喜欢。【参考答案——教师用】基础2示例：I prefer folk music because it tells real stories. / The song "Hello" by Adele really moves me — her voice is so powerful. / Hip-hop gives me energy when I run.',
  reflection: '✅ 亮点：音乐片段让课堂气氛活跃，感受动词（move/energize/calm）学生印象深刻。⚠️ 需改进：genre 发音仍需反复纠正，下节阅读中出现 choir 可以类比。📌 下节课衔接：进入阅读 THE VIRTUAL CHOIR，从音乐偏好延伸到音乐+科技的创新形式。'
}));

// ====== Period 2: Reading I (快速阅读+主旨) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u5-r1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '音乐', '虚拟合唱团', 'Eric Whitacre', '人教版必修二U5', '第二节课'],
  textbookAnalysis: '本课为必修第二册 Unit 5 第二课时（Reading I），语篇 THE VIRTUAL CHOIR 是一篇人物+现象说明文，讲述美国作曲家 Eric Whitacre 如何从一个音乐少年、经历挫折后受到粉丝视频启发，创建虚拟合唱团——让全球数千人在线录制演唱同一首歌并合成震撼作品。结构为"个人经历→灵感时刻→虚拟合唱团诞生→全球影响"。语言重点为叙事时间顺序词（originally / then / over the next few years / since then）与音乐+科技动词（compose, conduct, perform, upload, combine, inspire）。',
  overview: '【学情分析】A班：对"虚拟合唱团"概念好奇，但视频合成技术原理的理解可能需要解释。B班：Eric Whitacre 是谁完全陌生，需照片+视频脚手架。共同问题：本文把"个人故事"和"科技解释"两种文体揉在一起——学生容易在两种文体间迷失。',
  objectives: [
    '语言能力：读懂人物+现象说明文，提取 Eric Whitacre 的人生转折点/虚拟合唱团的运作方式/全球影响；掌握 8-10 个核心动词。',
    '文化意识：理解音乐与科技结合可以跨越国界连接人类——"虚拟合唱团"是全球化的美好例证。',
    '思维品质：通过"个人梦想→挫折→科技灵感→全球影响"因果链分析培养叙事与非叙事混合阅读策略。',
    '学习能力：能用"梦想→挫折→转折→创造→影响"框架复述 Eric Whitacre 的故事。'
  ],
  keyPoints: '① 叙事弧线：Love for music → Setback → Fan video inspiration → Virtual Choir created → Global phenomenon ② 时间标志词：originally / then / in 2009 / over the next few years / since then / altogether ③ 核心短语：fall in love with / be inspired by / come up with / combine... into / prove to be',
  difficulties: '① virtual /vɜːtʃuəl/ 发音 — 重音在第一音节，virtue 词根。② choir /kwaɪə/ 拼写与发音完全不对应 — 学生易读成 /tʃɔɪə/ 或写成 quire。③ come up with（想出）— 学生易漏介词 with。',
  teachingMethods: '① 故事弧线阅读法：找转折点→画因果链。② 视频辅助：放一段 Virtual Choir 实际视频让学生感受。③ Jigsaw 拼图：分段读后拼合全故事。',
  preparation: '【PPT课件】P1 Eric Whitacre 照片+Virtual Choir 截图；P2 Virtual Choir 运作方式示意图；P3 故事弧线图；P4 时间轴；P5 因果链图；P6 词汇对比表；P7 总结回顾。【实物教具】故事弧线空白 work sheet 每人一份；分段阅读卡。',
  process: [
    { step: '导入设问+视频', time: '6', content: '【PPT P1 照片+截图】教师播放 30 秒 Virtual Choir 视频。教师：These people have never met. They recorded themselves singing alone at home. Together, they created THIS. How is this possible? 预设回答：They used the Internet! Someone combined all the videos! 板书时机：板书 virtual / choir / combine。差异化提示：B班中文描述看到的画面再翻英文；A班用英文说这个现象的特别之处。易错点提醒：choir /kwaɪə/ — ch 读 /k/，oir 读 /waɪə/。完全不符合拼读规则，必须特别记忆。' },
    { step: '快速阅读抓主线', time: '8', content: '【PPT P3 时间轴】教师：Read fast (3 min). Find: ① Who created the Virtual Choir? ② What inspired him? ③ How many people have joined so far? 预设回答：① Eric Whitacre. ② A video of a girl singing his song. ③ Millions of people from over 80 countries. 板书时机：填时间轴三个关键事件。差异化提示：B班给三选一选项；A班写完整句+数字。易错点提醒：come up with（想出）的主意——Eric came up with the idea after watching the fan video。' },
    { step: '精读段落1-2 个人故事', time: '10', content: '【PPT P4 分段卡】教师精讲：fall in love with / be inspired by / come up with。教师：Why didn\'t Eric become a professional singer? What did the fan video show him? 预设回答：He fell in love with Mozart but had setbacks. The fan video showed him that people loved his music and wanted to be part of it. 板书时机：左侧栏画"梦想→挫折→灵感"链。差异化提示：B班读后填关键词；A班用自己话描述 Eric 的情感变化。易错点提醒：fall in love with + sth = 爱上了某事物（不一定是人）——"He fell in love with Mozart\'s music" = 他爱上了莫扎特的音乐。' },
    { step: '精读段落3-4 虚拟合唱团', time: '10', content: '【PPT P5 运作方式图】教师：How does a virtual choir work? What makes it special? 学生用图表解释：①Eric composes & conducts → ②Video parts put online → ③People worldwide record themselves → ④Videos uploaded → ⑤Combined into one performance。教师：What does "virtual" mean here? 预设回答：It means "not physically together" — the choir exists on the Internet, not in one room. 板书时机：右侧画五步骤流程图。差异化提示：B班连线匹配（步骤—描述）；A班写完整步骤说明句。易错点提醒：virtual ≠ virtuous（有道德的）—— virtual 本意是"虚拟的/实质上的"。' },
    { step: '归纳意义', time: '4', content: '【PPT P6 全球影响】教师：What does the Virtual Choir prove? Why does the title just say "THE VIRTUAL CHOIR"? 预设回答：It proves that music can connect people across the world. The title is simple but powerful — it\'s THE virtual choir, a unique and revolutionary idea. 板书时机：写 global connection / music + technology。差异化提示：B班跟读关键词；A班用自己的话总结音乐+科技的意义。易错点提醒：prove to be（被证明是）—— "The Virtual Choir has proved to be a worldwide success." = 虚拟合唱团已被证明是一个全球性的成功。' },
    { step: '小结', time: '2', content: '【PPT P7 总结回顾】教师带学生回顾"爱音乐→受挫→被视频启发→创建虚拟合唱团→全球影响"故事弧线+核心词汇。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：altogether（总共）= in total，不要和 all together（全部在一起）混淆——虽然意思相近但用法有细微区别。' }
  ],
  blackboard: '┌─ U5 Reading I: THE VIRTUAL CHOIR ────────────┐\n│ Eric Whitacre\'s Journey:                       │\n│  Love music → Setback → Fan video → Idea!     │\n│  → Virtual Choir → 80+ countries, millions     │\n│                                                 │\n│ come up with / fall in love with                │\n│ be inspired by / combine... into                │\n│ prove to be / altogether                        │\n│                                                 │\n│ Virtual Choir = music + Internet + people       │\n│  "Virtual" = not physically together            │\n│  "Choir" = /kwaɪə/ (NOT /tʃɔɪə/!)              │\n└─────────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 朗读课文第2-4段 2 遍，圈出所有时间标志词。2. 用故事弧线的4个阶段各写1句描述 Eric 的经历。【提高作业】用 80 词写一段：If you could create a virtual project (not necessarily music), what would it be and why?（用 come up with / be inspired by / combine）【参考答案——教师用】基础2示例：Eric fell in love with classical music as a teenager. / He faced setbacks and couldn\'t become a professional singer. / A fan\'s video inspired him to create the Virtual Choir. / Since then, his idea has connected millions of people worldwide.',
  reflection: '✅ 亮点：视频导入让学生直观理解"虚拟合唱团"，故事弧线清晰。⚠️ 需改进：choir 发音和拼写仍需强化——几乎全班第一次都读错。📌 下节课衔接：进入精读语言+过去分词作状语在语篇中的功能分析。'
}));

// ====== Period 3: Reading II (精读+语言分析) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u5-r2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'reading', lessonTypeName: '阅读',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['阅读', '精读', '过去分词', '虚拟合唱团', '人教版必修二U5', '第三节课'],
  textbookAnalysis: '本课为必修第二册 Unit 5 第三课时（Reading II），聚焦语篇 THE VIRTUAL CHOIR 的精读与语言分析。重点分析文中过去分词作状语的用法——如 "Moved by Mozart\'s music, he began composing." "Inspired by a fan video, Eric came up with the idea." "Known as the father of the Virtual Choir, Eric has changed music." ——在人物报道中的功能：简洁地表达原因/时间/伴随状态，增强句式多样性。同时深化语篇中高频动词的用法辨析（compose / conduct / perform / upload / combine / inspire / prove）。',
  overview: '【学情分析】A班：已掌握过去分词作定语和宾补，但作状语（相当于省略的状语从句）是全新概念。B班：过去分词本身不熟，分不清现在分词与过去分词作状语的区别。共同问题：写作中习惯用完整状语从句（Because he was moved...），不会简化为过去分词作状语（Moved...）。',
  objectives: [
    '语言能力：能在课文语境中识别并分析至少 4 个过去分词作状语的句子，理解其"表示原因/时间/伴随"的状语功能。',
    '文化意识：通过过去分词作状语体会英语书面语的简洁优雅——这是中高级英文写作的标志。',
    '思维品质：分析过去分词作状语在人物报道中的修辞功能——使叙事更流畅、更精炼。',
    '学习能力：建立"从读到写"的语料库——积累课文中的过去分词作状语句型用于后续演讲稿写作。'
  ],
  keyPoints: '① 过去分词作状语结构：V-ed..., S+V...（相当于省略了 Because/When/If + be动词 的状语从句）② 语篇中分词作状语句的识别与功能分析 ③ 核心动词辨析：compose / conduct / perform / upload / combine / inspire / prove / enable',
  difficulties: '① 过去分词作状语 vs 现在分词作状语 — Moved by...（被动，被感动） vs Moving to...（主动，搬到）。原因：学生不会判断主语与分词的主被动关系。② 分词作状语时逻辑主语必须与主句主语一致——否则是 dangling participle（悬垂分词），严重语法错误。③ upload（上传）vs download（下载）— 方向相反。',
  teachingMethods: '① 标注发现法：圈出文中所有过去分词作状语的句子并还原为状语从句。② 对比辨析：现在分词 vs 过去分词作状语。③ 语料卡记录：分类摘录优质句子。',
  preparation: '【PPT课件】P1-2 课文中圈出的过去分词作状语示例；P3 分词作状语结构分解公式；P4 现在分词 vs 过去分词作状语对比表；P5 语料卡模板；P6 词汇辨析表；P7 总结回顾。【实物教具】课文复印件 printed 每人一份；高亮笔。',
  process: [
    { step: '课文回顾', time: '5', content: '【PPT P1 故事弧线】教师：Last class we met Eric Whitacre. Can you recall: What inspired him? What did he create? Why is it special? 预设回答：A fan\'s video inspired him. He created the Virtual Choir. It connects people worldwide through music. 板书时机：左栏写故事弧线关键词。差异化提示：B班看关键词复述；A班完整复述+加入感受。易错点提醒：inspire /ɪnspaɪə/ — 注意 /aɪə/ 双元音+弱读音节，不要读成 /ɪnspɪr/。' },
    { step: '过去分词作状语发现', time: '8', content: '【PPT P2 课文句子】发课文复印件。教师：Circle sentences that start with a past participle (V-ed) followed by a comma. 学生标记后核对：①Moved by Mozart, he began composing. ②Inspired by a fan video, Eric created the Virtual Choir. ③Known as the father of VC, Eric has changed music. 教师：What do these sentences have in common? 预设回答：They all start with V-ed. They explain WHY or HOW something happened. 板书时机：逐句板书，标注 V-ed + 逗号 + 主句。差异化提示：B班给划线句直接圈 V-ed；A班自己找+还原为状语从句。易错点提醒：这些 V-ed 短语不是修饰主语——而是整个句子的状语，表示原因/时间/伴随。' },
    { step: '分词作状语讲透', time: '10', content: '【PPT P3 结构公式】教师板书：V-ed..., S + V...。还原：①Moved by Mozart, he began... = Because he was moved by Mozart, he began... ②Inspired by a video, Eric created... = After he was inspired by a video, Eric created... ③Known as..., Eric has changed... = Eric is known as..., and he has changed... 教师：Why use V-ed instead of a full clause? 预设回答：It\'s shorter and more elegant. It sounds more professional. 板书时机：三句对比，红笔标还原。差异化提示：B班连线（V-ed 句 → 原状语从句）；A班自己还原+解释哪种更好。易错点提醒：分词作状语的逻辑主语必须 = 主句主语！"Moved by Mozart, music became his passion." 是错的 — 应该是 Moved by Mozart, HE made music his passion。' },
    { step: '现在分词 vs 过去分词对比', time: '7', content: '【PPT P4 对比表】教师对比：①Moved by the music, he cried.（被动→过去分词，他被音乐感动）②Hearing the music, he cried.（主动→现在分词，他听到音乐）。教师：How to choose V-ed or V-ing? 预设回答：If the subject DOES the action → V-ing. If the subject RECEIVES the action → V-ed. 板书时机：双栏对比板书。差异化提示：B班判对错选择；A班独立造一对对比句。易错点提醒：判断法——在分词前加上主语看是否合适。He was moved by the music ✓（过去分词）He was hearing the music（不自然）→ Hearing the music（现在分词）✓。' },
    { step: '语料库搭建', time: '7', content: '【PPT P5 语料库模板】学生分类填语料卡：①过去分词作状语句摘录（至少3句）②音乐+科技动词（compose/conduct/perform/upload/combine/inspire/prove/enable）③时间/过渡词。板书时机：巡视指导。差异化提示：B班填词+翻译；A班造句+标注"可用于演讲稿"。预设回答：按音乐语料库模板分类填写词条。易错点提醒：compose（作曲）≠ consist（组成）— compose 音乐语境 = write music。concert（音乐会）≠ consort（配偶）也不相关。' },
    { step: '小结', time: '3', content: '【PPT P7 总结回顾】回顾 V-ed 作状语（省略状语从句→更精炼）+ 与 V-ing 的区别 + 语料库。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读；A班自述。易错点提醒：下节课语法课系统讲练过去分词作状语的各种类型。' }
  ],
  blackboard: '┌─ U5 Reading II: Language Focus ─────────────┐\n│ Past Participle as Adverbial (状语):          │\n│  V-ed..., S + V...  =  状语从句简化           │\n│                                               │\n│  Moved by Mozart, he began composing.         │\n│  = Because he was moved by Mozart, ...         │\n│                                               │\n│  Inspired by a video, Eric created the VC.    │\n│  = After he was inspired by a video, ...       │\n│                                               │\n│  RULE: 分词逻辑主语 = 主句主语                 │\n│  V-ed (被动) vs V-ing (主动)                  │\n│  Moved by music, he... (他 被 感动)            │\n│  Hearing music, he...  (他 主动 听到)          │\n└───────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 从课文中找出3个过去分词作状语的句子并还原为状语从句。2. 选择 V-ed 或 V-ing：①___ (Inspire/Inspired) by her teacher, she started singing. ②___ (See/Seen) the concert, she felt excited.【提高作业】用过去分词作状语写3句关于你自己与音乐的故事（如 "Moved by a song, I learned to play the guitar."）。【参考答案——教师用】基础2：①Inspired ②Seeing.',
  reflection: '✅ 亮点：还原法（分词句→从句）让学生直观理解状语的省略规则。⚠️ 需改进：dangling participle 的错误仍需反复强调，语法课要作为重中之重。📌 下节课衔接：进入语法课，系统操练过去分词作状语的各种类型（原因/时间/条件/伴随）。'
}));

// ====== Period 4: Grammar (过去分词作状语) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u5-g', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'grammar', lessonTypeName: '语法',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['语法', '过去分词', '状语', '音乐', '人教版必修二U5', '第四节课'],
  textbookAnalysis: '本课为必修第二册 Unit 5 第四课时（Discovering Useful Structures），系统教学过去分词作状语（V-ed 作原因/时间/条件/伴随状语）。基于 Reading 语篇中提取的例句，引导学生归纳"何时用过去分词作状语"的规则——当状语从句的主语与主句主语一致且为被动关系时，可省略连词+主语+be。通过音乐主题的语境化练习巩固语法，为后续演讲稿写作做语言准备。这是高中阶段最重要的语法进阶之一——分词作状语是高考书面表达的加分项。',
  overview: '【学情分析】A班：能理解从句简化为分词的基本逻辑，但条件状语（If done...）和应用到自己的写作中仍有困难。B班：分词概念模糊，需从"找主语→判断主被动→选择 V-ed/V-ing"三步法开始。共同问题：最严重错误是分词逻辑主语与主句主语不一致（dangling participle）。这是高考改错和写作的高频扣分点。',
  objectives: [
    '语言能力：准确使用过去分词作原因/时间/条件/伴随状语，在音乐话题中产出 5 个以上正确句子。',
    '文化意识：通过过去分词作状语体会英语书面语的精炼美——这是中英语言思维差异的重要体现。',
    '思维品质：通过"发现例句→归纳规则→三步判断→应用输出"的归纳法培养语法学习策略。',
    '学习能力：建立"分词自查表"——写作后自行检查分词逻辑主语是否与主句主语一致。'
  ],
  keyPoints: '① 过去分词作状语四大类型：原因（Because done...）/ 时间（When done...）/ 条件（If done...）/ 伴随（...，done...）② 三步判断法：找主句主语→判断与分词的主被动关系→选择 V-ed（被动）或 V-ing（主动）③ 黄金法则：分词逻辑主语必须 = 主句主语！④ 不规则过去分词复习（write→written, sing→sung, know→known, give→given）',
  difficulties: '① dangling participle — "Walking down the street, the flowers were beautiful."（花在走路？）主语不一致是中式英语最典型错误。② 分词作状语的位置——句首最常见，句末也可以（表示伴随）。③ 分词否定形式—— Not knowing what to say（现在分词否定）/ Not moved by the music（过去分词否定），否定词 not/never 放在分词前。',
  teachingMethods: '① 归纳法（Guided Discovery）：例句→规则→三步法→练习。② 情境造句：给音乐场景图片用分词描述。③ 改错竞赛：Dangling participle 专项纠正。',
  preparation: '【PPT课件】P1 过去分词作状语四大类型表；P2 课文例句摘录；P3 三步判断流程图；P4 现在分词 vs 过去分词对比；P5 情境造句任务卡；P6 改错题（dangling participle专项）；P7 总结。【实物教具】改错卡每人一套；三步判断卡每人一张。',
  process: [
    { step: '例句发现+分类', time: '7', content: '【PPT P2 例句分类】展示 6 句，学生按原因/时间/条件/伴随分类：①Moved by the song, he cried.（原因）②Seen from the stage, the audience looked like a sea.（时间）③Given the chance, I would sing every day.（条件）④The singer stood on stage, surrounded by fans.（伴随）⑤Inspired by Eric, she joined a choir.（原因）⑥If invited, I will perform.（条件）。教师：What links all these sentences? 预设回答：They all use V-ed. You can add "Because/When/If" to make them full clauses. 板书时机：四象限分类板书。差异化提示：B班只分类不分析；A班分类+还原为状语从句。易错点提醒：条件状语（If done）中 if 有时保留有时省略——两者都可以，"If invited" = "Invited"。' },
    { step: '规则归纳+三步法', time: '10', content: '【PPT P3 三步法】教师教三步判断：Step 1: 找主句主语。Step 2: 主语是分词动作的发出者（V-ing）还是承受者（V-ed）？Step 3: 选择分词形式。用4个例句演示：①(Inspire) by music, he wrote a song. → 主句主语 he = 被启发 → Inspired ✓ ②(Hear) the music, she danced. → 主句主语 she = 主动听 → Hearing ✓。教师：Why can\'t we say "Walking down the street, the flowers were beautiful"? 预设回答：Because the flowers are not walking! 板书时机：三步法流程图板书。差异化提示：B班跟三步法逐个判断；A班独立判断+解释原因。易错点提醒：三步法黄金法则 = 分词逻辑主语必须等于主句主语。' },
    { step: '四大类型操练', time: '8', content: '【PPT P5 图片卡】展示 4 张音乐相关图（歌手感动流泪/观众鼓掌/被邀请上台/吉他手被粉丝围绕），学生用不同状语类型描述。教师：Use a different type for each picture! 预设回答：①Moved by the audience\'s response, the singer cried.（原因）②When asked to sing, she felt nervous.（时间）③If given a guitar, I would learn to play.（条件）④The guitarist sat there, surrounded by cheering fans.（伴随）板书时机：巡视指导。差异化提示：B班给分词提示（moved/asked/given/surrounded）；A班自由选择分词+说明什么状语类型。易错点提醒：伴随状语中过去分词常放在句末且前面有逗号——"He walked off stage, followed by applause."' },
    { step: '改错竞赛（Dangling Participle）', time: '8', content: '【PPT P6 改错专项】展示 5 个 dangling participle 典型错误：①Walking into the concert hall, the music was loud.（谁在走？）②Moved by the song, tears ran down her face.（谁的眼泪？）③Seen from the top, the city was tiny.（虽语法通但最好说 Seeing from the top 如果是"你"在看的话）④Inspired by Eric, the Virtual Choir was created.（谁被 inspire？）⑤Given more time, the song would be better.（虽可接受但最好明确主语）。学生纠错。预设回答纠错。板书时机：板书错误→改正+规则。差异化提示：B班判对错；A班解释为什么错+改正。易错点提醒：Dangling participle 高考必考——改错题中看到分词开头+逗号，立刻检查主句主语是否一致。' },
    { step: '小结', time: '7', content: '【PPT P7 总结】回顾四大类型+三步法+黄金法则+常见错误。教师带全班大声读三步法。预设回答跟读。板书时机：圈重点。差异化提示：B班跟读三步法；A班说出每步+给例句。易错点提醒：自查三问——①主句主语是谁？②主语是分词动作的发出者还是承受者？③如果是承受者→V-ed ✓ 如果是发出者→V-ing ✓ 如果不符→改主语！' }
  ],
  blackboard: '┌─ U5 Grammar: V-ed as Adverbial ──────────────┐\n│  V-ed 作状语 (原因/时间/条件/伴随)              │\n│                                                 │\n│  Cause:  Moved by..., he...                     │\n│  Time:   Seen from..., it...                     │\n│  Condition: Given..., I...                       │\n│  Manner: He stood, surrounded by...              │\n│                                                 │\n│  3-Step Check:                                  │\n│  ① Find main subject                            │\n│  ② Does subject DO or RECEIVE the action?       │\n│  ③ DO → V-ing  /  RECEIVE → V-ed               │\n│                                                 │\n│  ⚠️ Golden Rule: 分词逻辑主语 = 主句主语        │\n│  ❌ Walking in, the music was loud.             │\n│  ✓ Walking in, I heard loud music.              │\n│  ❌ Moved by the song, tears ran down her face. │\n│  ✓ Moved by the song, she burst into tears.     │\n└─────────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 用过去分词作状语造 5 句（覆盖原因/时间/条件/伴随四种类型）。2. 改错：Inspired by the concert, the guitar was bought. / Hearing the news, tears came to my eyes.【提高作业】写 60 词短文关于音乐如何影响你的情绪，至少用 3 个过去分词作状语。【参考答案——教师用】基础1示例：Moved by the melody, I started to cry. / When played softly, the piano sounds magical. / If given the choice, I would listen to jazz all day. / He sat in the corner, lost in the music.',
  reflection: '✅ 亮点：三步法让复杂的语法判断变为流程化操作，B班掌握率明显提升。⚠️ 需改进：dangling participle 仍是最顽固错误，后面听与谈和写作课都要持续纠错。📌 下节课衔接：听与谈聚焦音乐与情绪，口头运用分词作状语描述音乐感受。'
}));

// ====== Period 5: Listening and Talking ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u5-lt', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'listening-talking', lessonTypeName: '听与谈',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['听与谈', '音乐与情绪', '音乐推荐', '人教版必修二U5', '第五节课'],
  textbookAnalysis: '本课为必修第二册 Unit 5 第五课时（Listening and Talking），语境为"讨论音乐如何影响情绪与推荐歌曲"。听力材料为一段关于不同音乐对情绪影响的对话，口语输出任务为向朋友推荐一首能改变情绪的歌曲并解释原因。功能语言为描述音乐效果的句型（This song makes me feel... / Whenever I hear..., I... / It takes me back to... / The lyrics speak to me because...）。结合语法课的过去分词作状语，在口语中自然运用如"Moved by this song, I decided to learn piano."等结构。',
  overview: '【学情分析】A班：能表达简单音乐偏好，但对"音乐与情绪"的深层描述能力不足。B班：开口意愿低，但"推荐一首歌"是贴近生活的轻松任务。共同问题：描述音乐时只说"I like it"，不说音乐具体给你什么感受/让你想起什么。',
  objectives: [
    '语言能力：听懂关于音乐与情绪的对话，提取音乐类型/情绪效果/个人关联；能用至少 4 种句型推荐歌曲并描述其情绪影响。',
    '文化意识：理解音乐是人类共通的情感语言——一首歌可以跨越语言和文化触动人心。',
    '思维品质：在讨论中练习"描述感受→解释原因→建立个人关联"的完整表达链。',
    '学习能力：通过推荐对话训练"为听众量身推荐"的沟通策略——推荐的歌不是自己最喜欢的，而是对方可能需要的。'
  ],
  keyPoints: '① 音乐与情绪句型：This song makes me feel... / Whenever I hear..., I... / It takes me back to... / The lyrics speak to me because... ② 推荐句型：You should listen to... / I recommend... / If you like..., try... / This song is perfect for when you... ③ 听力重点：抓音乐—情绪—原因的配对。',
  difficulties: '① take sb back to（把某人带回到…记忆）— 学生按字面理解为"带回去"。提醒：固定短语 = remind sb of the past。② lyrics /lɪrɪks/ 永远用复数 — 学生易说 "a lyric"（指单独一句歌词可以，但泛指歌词用 lyrics）。③ speak to sb（打动/引起共鸣）— 不是"对某人说话"。',
  teachingMethods: '① 听前预测→听中配对→听后产出。② "情绪歌单"活动：给不同情绪（开心/伤心/需要动力/需要平静）各选一首歌。③ 歌曲推荐圆桌。',
  preparation: '【PPT课件】P1 情绪表情图标（😊😢💪😌）；P2 音乐与情绪句型板；P3 听力任务题；P4 听力任务卡；P5 推荐句型板；P6 "情绪歌单"活动卡；P7 总结。【实物教具】情绪歌单空白卡 printed 每人一份；歌曲推荐卡。',
  process: [
    { step: '导入激活', time: '5', content: '【PPT P1 表情图标】教师：Look at these emotions: happy, sad, need energy, need calm. What song would you play for each? 预设回答：Happy → "Happy" by Pharrell! / Sad → "Someone Like You" by Adele. / Energy → "We Will Rock You." / Calm → classical piano. 板书时机：左栏四情绪分栏，贴学生推荐的歌。差异化提示：B班中文说歌名再找英文名；A班英文说+一句话理由。易错点提醒：推荐歌名时——英文歌名每个实词首字母大写，"Someone Like You" 不是 "someone like you"。' },
    { step: '听力抓情绪', time: '10', content: '【PPT P3 听力任务】听对话，抓"什么歌/给什么情绪听/为什么这个情绪"。教师：Listen for: What song do they talk about? How does it make them feel? What memory does it bring back? 预设回答：The song "Fix You" by Coldplay makes the speaker feel hopeful. It takes them back to a difficult time when music helped them through. 板书时机：配对填表（歌曲|情绪|原因/记忆）。差异化提示：B班给配对连线题；A班听写关键词+写完整感受句。易错点提醒：take sb back to + 时间/地点/经历——"It takes me back to my high school days." = 它让我回想起高中时光。' },
    { step: '听中记录', time: '8', content: '【PPT P4 任务卡】【音频】重听，注意推荐者如何"推荐+感受+原因"三步走。教师：How does the speaker structure their recommendation? 预设回答：①Name the song → ②Describe the feeling → ③Give a personal reason or memory. 板书时机：板书推荐三步法。差异化提示：B班勾选听到的推荐句型；A班记录完整推荐链。易错点提醒：推荐时最打动人的不是"这首歌很好听"——而是"这首歌在你生命中的故事"。真实经历 > 任何形容词。' },
    { step: '句型操练', time: '7', content: '【PPT P5 句型板】教师带领操练音乐推荐三步链：A: I recommend "..." because it always cheers me up. / B: What does it make you feel? / A: Whenever I hear it, I feel like everything will be okay. It takes me back to my first concert. 预设回答跟读+仿造。板书时机：板书推荐三步法+句型。差异化提示：B班用填空脚本；A班自主对话+真实推荐。易错点提醒：过去分词作状语融入口语——"Inspired by this song, I started learning guitar." 让口语也高级。' },
    { step: '情绪歌单活动', time: '8', content: '【PPT P6 活动卡】学生各自制作"情绪歌单"：为 4 种情绪各选 1 首英文歌（或翻译中文歌名），写一句话为什么。然后同桌分享+互相推荐。教师巡视。预设回答：For "need energy": "Eye of the Tiger" — It makes me feel unstoppable. / For "sad": "Let Her Go" — The lyrics speak to me about loss. 板书时机：留句型供参考。差异化提示：B班用填空卡；A班自由写+用至少 1 个分词作状语。易错点提醒：英文歌名加引号——"Let Her Go" 或者斜体 Let Her Go。不加引号会被当成普通句子。' },
    { step: '小结', time: '2', content: '【PPT P7 总结】回顾音乐与情绪句型+推荐三步法+过去分词融入口语。教师：Remember: the best music recommendation is personal. 预设回答跟读。板书时机：圈重点句型。差异化提示：B班齐读；A班每人说一句自己歌单中最特别的推荐。易错点提醒：推荐歌曲时偶尔用被动语态分句——"This song was written for..." / "It was inspired by..." 展示音乐知识深度。' }
  ],
  blackboard: '┌─ U5 Listening & Talking ──────────────────┐\n│ Music & Emotions:                           │\n│  This song makes me feel...                 │\n│  Whenever I hear..., I...                   │\n│  It takes me back to...                     │\n│  The lyrics speak to me because...          │\n│                                             │\n│ Recommendation 3 Steps:                     │\n│  ① Name the song                            │\n│  ② Describe the feeling                     │\n│  ③ Share a personal reason / memory         │\n│                                             │\n│  Emotions: 😊 happy  😢 sad                 │\n│            💪 energized  😌 calm             │\n└─────────────────────────────────────────────┘',
  exercises: '【基础作业】1. 听录音跟读 2 遍，圈出所有描述音乐感受的句型。2. 用推荐三步法写 1 段完整的歌曲推荐（50词）。【提高作业】制作你的"情绪歌单"（4首歌+4句英文推荐理由），下节课分享。【参考答案——教师用】基础2示例：I recommend "Viva la Vida" by Coldplay. Whenever I hear it, I feel like I can conquer anything. Inspired by the powerful strings and lyrics about rising after a fall, I always play it before exams.',
  reflection: '✅ 亮点：情绪歌单活动让每个学生都有话可说，因为选的是自己喜欢的歌。⚠️ 需改进：take sb back to 的用法仍需强化——部分学生写成 take sb back from。📌 下节课衔接：进入写作 I，将音乐推荐升级为正式的演讲稿。'
}));

// ====== Period 6: Writing I (演讲稿结构+语料) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u5-w1', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '演讲稿', '音乐', '人教版必修二U5', '第六节课'],
  textbookAnalysis: '本课为必修第二册 Unit 5 第六课时（Reading for Writing I），写作体裁为写一篇关于音乐如何改变你生活的演讲稿（Write a Speech About How Music Has Changed Your Life）。演讲结构为：吸引注意的开场→你的音乐故事（具体经历）→音乐改变你的方式→结尾的呼吁/感悟。语言重点为演讲特有的修辞手法（rhetorical questions, repetition, personal anecdotes）与过去分词作状语（Moved by..., Inspired by...）在演讲稿中的运用——使演讲既有感染力又语言精炼。结合本单元 Reading 的人物叙事与语法课的分词作状语，实现"读-语法-写"闭环。',
  overview: '【学情分析】A班：有写作能力但演讲稿体裁不熟——演讲稿要能"读出来有感染力"，与书面作文不同。B班：句型储备少、公开演讲经验少，需大量范例+模板。共同问题：演讲稿写成"议论文"——缺少 rhetorical questions、故事叙述和个人情感。',
  objectives: [
    '语言能力：掌握演讲稿的"Hook→Story→Change→Closing"四段结构，在音乐话题中产出 100-120 词有感染力的英文演讲稿。',
    '文化意识：理解公开演讲在西方文化中的重要性——学习用英文表达个人故事和观点。',
    '思维品质：通过"选择故事→提炼感悟→设计修辞→构建演讲"训练从个人经历到公共表达的转化思维。',
    '学习能力：建立"演讲稿≠作文"的体裁意识——学会使用 rhetorical questions、repetition、storytelling。'
  ],
  keyPoints: '① 演讲稿四段结构：Engaging Opening → Your Music Story → How Music Changed You → Powerful Closing ② 演讲修辞手法：Rhetorical questions（"Have you ever felt...?"）、Repetition（"Music gives me... Music gives me..."）、Personal anecdote（"I remember the first time I..."）③ 过去分词作状语在演讲中的运用——增加语言精炼度与感染力。',
  difficulties: '① Rhetorical question（反问/设问）——学生不习惯在正式写作中问问题。② "演讲感"语气——需要反复朗读来检查是否"读出来自然"。③ 演讲结尾的力量——学生常以"That\'s all. Thank you."草草收尾。',
  teachingMethods: '① 范本解构法：读/听优秀演讲稿→提取结构+修辞→仿写。② 朗读测试：写完必须朗读——耳朵是最好的编辑器。③ 过程写作：outline→draft→read aloud→revise。',
  preparation: '【PPT课件】P1 优秀音乐演讲稿范例；P2 演讲稿四段结构图；P3 演讲修辞手法表；P4 演讲稿句型库；P5 头脑风暴工作单；P6 写作任务；P7 总结。【实物教具】演讲稿结构模板 printed 每人一份；演讲修辞手法卡每组一套。',
  process: [
    { step: '范本解构', time: '8', content: '【PPT P1 演讲稿范例】教师朗读一篇关于音乐的英文演讲稿（约100词），学生标注：①Hook（用什么开头？问了一个什么 rhetorical question？）②Story（讲了什么个人经历？）③Change（音乐如何改变了他？）④Closing（结尾用了什么让听众记住？）。教师：What makes this a speech and not an essay? 预设回答：The speaker asks questions to the audience. There\'s a personal story. The ending is powerful — it\'s not just "thank you." 板书时机：四段结构板书。差异化提示：B班给标注好的演讲稿只匹配段名；A班自己标注+圈出修辞手法。易错点提醒：演讲稿的 Hook 比议论文更重要——听众的前 10 秒决定他们是否继续听。用问句/惊人事实/小故事开头。' },
    { step: '四段结构+修辞讲透', time: '10', content: '【PPT P2 结构图+PPT P3 修辞表】教师逐段讲解：①Opening Hook — rhetorical question ("Have you ever heard a song that changed everything?") + 主题句。②Story — 你的具体音乐经历（"I remember the first time I heard..."）——越细节越有感染力。③Change — 音乐如何改变了你（"Music taught me that..." / "Since then, I have..."）——用至少 1 个过去分词作状语（"Moved by the lyrics, I..."）。④Closing — 有力的结尾句+呼吁/感悟（"Music isn\'t just sound. It\'s..."）——不要用"That\'s all"。教师用 Eric Whitacre 的故事做范例示范。预设回答跟做笔记。板书时机：逐段板书模板句+修辞手法。差异化提示：B班给每段填空模板；A班给关键词自己写+选一种修辞手法必须用到。易错点提醒：修辞手法不要滥用——100词演讲稿用 1-2 种修辞足够。最有效的通常是 1 个 rhetorical question + 1 个 personal anecdote。' },
    { step: '句型库', time: '5', content: '【PPT P4 句型库】教师领读演讲高频句型：Opening: Have you ever...? / Let me tell you about... / I\'ll never forget the moment when... / Story: I remember the first time I... / It was a cold winter evening when... / Change: Music has taught me that... / Looking back, I realize... / Closing: So I ask you... / Remember that... / Music is more than... — it\'s... 教师强调用过去分词作状语增加语言质量。预设回答跟读。板书时机：句型分类板书（开头/故事/改变/结尾）。差异化提示：B班齐读+每类背1句；A班选最喜欢的2句并说为什么适合演讲稿。易错点提醒：Looking back 是现在分词作状语（"当我回顾时"）——这是你主动回顾，所以用 V-ing 不是 V-ed。' },
    { step: '头脑风暴+提纲', time: '7', content: '【PPT P5 工作单】学生各自想一件音乐改变自己的经历：①学会了一种乐器？②一首歌帮你度过难关？③音乐会改变了你的一天？④一个歌手激励了你？用工作单记录：Hook 写什么？讲什么故事？音乐怎么改变你的？结尾用什么句子？教师巡视。预设回答：I learned to play guitar because of a song. / A song helped me when I failed an exam. / My first concert changed how I see live music. 板书时机：巡视指导。差异化提示：B班给选题目录（3选1）+每段填空；A班自己想+每个故事都要真实。易错点提醒：选最真实的故事——你不需要惊天动地的经历。对你来说是真实的，对听众来说就是动人的。' },
    { step: '起草+朗读', time: '8', content: '【PPT P6 写作任务】学生写 100-120 词演讲稿初稿。要求：四段完整、至少 1 个 rhetorical question、至少 1 个过去分词作状语、结尾有力。写完必须自己默读一遍——检查"读出来顺不顺"。教师：Read your speech quietly. Does it sound natural? 预设回答：（学生写作+默读中）板书时机：留结构+句型供参考。差异化提示：B班用模板框架填写；A班自由写+追求修辞效果。易错点提醒：演讲稿写完后至少朗读一次——如果某句话读起来别扭，改到它读起来自然为止。演讲稿是"写来读的"，不是"写来看的"。' },
    { step: '同伴初评', time: '2', content: '【PPT P6 写作任务】同桌互换演讲稿，check：有 rhetorical question？故事具体吗？有过去分词作状语吗？结尾有力吗（不是"That\'s all"）？读一遍给对方听，听后说"最打动你的一句"。教师：Listen to your partner\'s speech. What line stayed with you? 预设回答："Music is not just sound — it\'s the voice of my soul." That line really moved me. 板书时机：留 checklist。差异化提示：B班用 checklist 逐项打勾；A班听后给"最打动人的句子+一个改进建议"。易错点提醒：演讲的力量在于"让听众感受到你的感受"——如果你的演讲让别人无感，问自己"我是否真的在乎这个故事？"' }
  ],
  blackboard: '┌─ U5 Writing: Speech ──────────────────────┐\n│  ① ENGAGING OPENING                         │\n│     Rhetorical question / surprising fact    │\n│     "Have you ever...?"                     │\n│  ② YOUR MUSIC STORY (specific + real!)      │\n│     "I remember the first time I..."        │\n│  ③ HOW MUSIC CHANGED YOU                    │\n│     Use V-ed as adverbial:                   │\n│     "Moved by the lyrics, I..."             │\n│  ④ POWERFUL CLOSING                         │\n│     NOT "That\'s all"!                       │\n│     "Music is more than... — it\'s..."       │\n│                                              │\n│  Speech ≠ Essay: Ask questions / Tell story │\n│  Read aloud to test!                         │\n└──────────────────────────────────────────────┘',
  exercises: '【基础作业】按课堂初稿完成 100-120 词演讲稿。要求：四段完整、≥1 rhetorical question、≥1 过去分词作状语、结尾有力。【提高作业】对着镜子（或手机录像）练习演讲，直到能脱稿讲出 80% 的内容。录 1 分钟视频或音频。【参考答案——教师用】示例（节选）："Have you ever heard a song that made you feel like you weren\'t alone? I have. It was a rainy Tuesday evening when I first heard \'Fix You\' by Coldplay. I had just failed my math exam. Moved by the lyrics \'Lights will guide you home,\' I felt something shift inside me. Music taught me that failure is not the end — it\'s a new beginning. So I ask you: what song has changed YOUR life?"',
  reflection: '✅ 亮点：演讲稿四段结构+修辞手法让学生的写作首次有了"说出来的力量"。⚠️ 需改进：部分演讲结尾仍是"That\'s all"，下节课用范例对比强化。📌 下节课衔接：进入写作 II，互评修改+演讲展示。'
}));

// ====== Period 7: Writing II (互评+修改+演讲展示) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u5-w2', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'writing', lessonTypeName: '写作',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['写作', '互评', '修改', '演讲', '音乐', '人教版必修二U5', '第七节课'],
  textbookAnalysis: '本课为必修第二册 Unit 5 第七课时（Writing II），在 Writing I 演讲稿初稿的基础上完成"互评→修改→演讲展示→终稿"闭环。重点训练学生用同学反馈改进演讲稿的感染力和可演讲性——特别关注朗读流畅度、修辞效果和结尾力量。互评量表聚焦三维度：内容（四段完整/故事真实感人）、语言（分词作状语≥1/rhetorical question/演讲稿句型）、演讲效果（朗读是否流畅/节奏是否合适/结尾是否有力量）。本课也是本册教材最后一节写作课，具有收官意义。',
  overview: '【学情分析】A班：能辨别演讲稿好坏，但对"演讲效果"（朗读流畅度/节奏）的反馈能力不足。B班：上台演讲紧张，需提供安全的展示环境。共同问题：修改时只改语法不顾朗读——演讲稿改完后必须"读一遍"才知好坏。',
  objectives: [
    '语言能力：能根据互评量表给同伴的演讲稿提具体、可操作的修改建议，重点检查演讲效果（朗读流畅度/修辞效果/结尾力量）。',
    '文化意识：通过聆听同伴的音乐故事，体验音乐在不同人生命中的多样角色。',
    '思维品质：在互评中培养"识别演讲弱点→提出强化方案"的批判性反馈能力。',
    '学习能力：建立"写→读→评→改→讲"五步演讲稿制作流程，内化为个人演讲习惯。'
  ],
  keyPoints: '① 互评三维量表：内容（四段完整/故事具体真实/结尾有力）+ 语言（分词作状语≥1/rhetorical question/演讲稿句型）+ 演讲效果（读出来自然吗？/节奏有快慢变化吗？/最打动人的一句是什么？）② 演讲展示技巧：眼神交流/节奏变化/强调关键词',
  difficulties: '① 学生上台紧张——需创造"不评分"的安全环境，重点在"分享"而非"表演"。② 演讲稿修改时学生只改纸面不改口语——需强制"改完大声读一遍"。③ 演讲语速过快——紧张导致 2 分钟的稿 40 秒读完。',
  teachingMethods: '① 量表互评：用统一标准减少主观性。② "朗读测试"：改完必须读给同桌听。③ 微型演讲展示+最佳演讲评选。',
  preparation: '【PPT课件】P1 互评三维量表；P2 常见问题（结尾弱/修辞缺/读不顺/分词不会用）；P3 修改指南+演讲技巧；P4 最佳演讲范例；P5 自评表；P6 必修第二册整体回顾；P7 总结。【实物教具】互评量表 printed 每人一份；红笔。',
  process: [
    { step: '量表培训', time: '5', content: '【PPT P1 互评量表】教师逐维讲解：①内容（四段全？故事真实具体？结尾不是"That\'s all"？）②语言（分词作状语≥1？rhetorical question？演讲稿句型？）③演讲效果（读出来自然吗？有快慢变化吗？最打动你的一句是什么？）。教师用上节课自己写的演讲稿示范打分+大声朗读展示"朗读如何暴露问题"。预设回答跟学。板书时机：量表三维板书。差异化提示：B班按量表逐项打勾；A班还需评"如果这是 TED 演讲，你会鼓掌吗？" 易错点提醒：朗读测试是最重要的——一篇演讲稿如果读起来卡壳、用词别扭、句子太长喘不过气，需要改的不是朗读技巧而是文案本身。' },
    { step: '互评+朗读测试', time: '12', content: '【PPT P2 常见问题】先展示上节课常见问题：①结尾是"That\'s all. Thank you." ②无 rhetorical question ③无分词作状语 ④故事太笼统（"Music is important to me"没有具体经历）。然后同桌互换稿子：第一步——默读打分。第二步——大声读给对方听。第三步——听的人说"最打动人的一句"和"最卡顿的一句"。教师巡视。预设回答：The line "Music is the voice of my soul" is powerful, but the sentence "Furthermore, additionally, music has significantly impacted my emotional well-being" sounds like an essay, not a speech. 板书时机：留量表供参考。差异化提示：B班按 checklist 勾+标出最卡顿的句子；A班还写"如果是我，我会怎么改写这句"。易错点提醒：演讲句子不能太长——一口气能读完的句子最多 15-18 个词。超过就断句或用逗号让读者喘气。' },
    { step: '修改', time: '8', content: '【PPT P3 修改指南】学生根据互评+朗读反馈修改。顺序：①先改"读出来不顺"的句子（缩短/断句/换更口语的词）②再调结尾（去掉"That\'s all"，加一句有力量的总结）③最后查修辞（补 rhetorical question / 分词作状语）。教师：Read your revised speech aloud to yourself. Does it flow better now? 板书时机：留修改顺序。差异化提示：B班对照量表逐条改；A班改完再读一遍+微调节奏标记（在稿子上画 / 表示停顿）。易错点提醒：修改演讲稿的最高原则——"删除一切读出来别扭的词"。即使那个词写得很高级，如果读出来不行，换掉。' },
    { step: '微型演讲展示', time: '10', content: '【PPT P4 演讲技巧】4-5 位自愿者上台发表 1 分钟演讲。3 条技巧：①眼神交流——看观众 3 秒再回稿子 ②节奏——关键句放慢，过渡句正常 ③力量在最后——结尾句一字一顿。全班闭眼听或睁眼看。投票：最打动人的故事/最佳修辞/最佳演讲者。预设回答展示。板书时机：记录投票结果+最佳结尾句。差异化提示：B班可看稿演讲但放慢；A班尽量脱稿+用肢体语言。易错点提醒：紧张时语速会变快——在稿子上写"SLOW DOWN"提醒自己。1分钟演讲 = 约 120-150 词。' },
    { step: '结课+收官', time: '5', content: '【PPT P6 必修第二册整体回顾】教师回顾整册书 5 个单元的主题链：U1 文化遗产（我们保护什么）→ U2 野生动物（我们与自然）→ U3 互联网（我们如何连接）→ U4 历史与传统（我们从哪里来）→ U5 音乐（什么触动我们的灵魂）。学生自评整册书的学习收获。教师：What will you take away from Book 2? 预设回答：I learned to use relative clauses, passive voice, past participles, and sensory details. But more importantly, I learned to express myself in English about real-world topics. 板书时机：写五单元主题链。差异化提示：B班中文自评；A班英文自评。易错点提醒：恭喜大家完成必修第二册！这本书的5个主题从外（文化遗产/自然）到内（音乐/情感），从过去（历史）到未来（互联网）——这就是英语学习的意义：用另一种语言看完整的世界。' }
  ],
  blackboard: '┌─ U5 Writing II: Speech Showcase ─────────────┐\n│ Speech Checklist:                              │\n│  ✅ 4 parts (Hook/Story/Change/Closing)        │\n│  ✅ ≥1 rhetorical question                     │\n│  ✅ ≥1 V-ed as adverbial                       │\n│  ✅ Reads aloud naturally                      │\n│  ✅ Closing is powerful (not "That\'s all")     │\n│                                                │\n│ Book 2 Journey:                                │\n│  U1 Heritage → U2 Wildlife → U3 Internet      │\n│  → U4 History → U5 Music 🎵                    │\n│                                                │\n│ Speech Tips:                                   │\n│  Eye contact / Slow down on key lines          │\n│  End with power — one word at a time           │\n└────────────────────────────────────────────────┘',
  exercises: '【基础作业】根据课堂反馈修改演讲稿终稿，提交文字稿+录制 1 分钟演讲音频/视频。【提高作业】写 30 词英文反思：必修第二册 5 个单元中，哪个单元对你影响最大？为什么？【参考答案——教师用】反思示例：Unit 3 The Internet influenced me the most because it made me think about how technology can be a force for good — Jan\'s story of using the Internet to overcome loneliness inspired me to start a study group online.',
  reflection: '✅ 亮点：朗读测试让学生亲身体验"演讲稿是写来读的"——很多句子一读就发现问题。⚠️ 需改进：少数学生还是写了"That\'s all"，说明之前的强调仍不够——也许在评分标准中直接扣分会更有效。📌 下节课衔接：进入 Project，将本单元所学整合为"音乐与人生"展览，为必修第二册画上句号。'
}));

// ====== Period 8: Project (音乐与人生展览) ======
pn++;
periods.push(makeLesson({
  id: 'l-eng-b2-u5-p', book: BOOK, unitNumber: UNIT, unitTitle: UNIT_TITLE,
  lessonType: 'project', lessonTypeName: '项目复习',
  lessonNumber: pn, periodNumber: pn, duration: 40,
  tags: ['项目', '复习', '音乐', '展览', '人教版必修二U5', '第八节课'],
  textbookAnalysis: '本课为必修第二册 Unit 5 第八课时（Project），也是必修第二册的最终项目课。学生以 4 人小组为单位，整合本单元5种课型所学——听与说的音乐词汇+阅读的虚拟合唱团+语法的分词作状语+听与谈的音乐与情绪+写作的演讲稿——完成一份"音乐与人生"展览展板。综合考查语言能力（词汇/语法/写作/演讲）、思维品质（主题策划）和学习能力（合作分工）。作为 Book 2 收官之课，具有整合5个单元、展示整册学习成果的重要意义。',
  overview: '【学情分析】A班：能独立完成分工作品，但这个项目可以挑战"展板+微型演讲"的双产出。B班：group work 中需要更明确的模板和范例支持。共同问题：把音乐展板做成"歌单海报"——缺少"音乐与人生"的主题深度。',
  objectives: [
    '语言能力：综合运用本单元词汇、分词作状语、音乐与情绪表达、演讲稿写作，以英文完成一份"音乐与人生"主题展览展板。',
    '文化意识：通过展览形式展示音乐在不同文化、不同人生阶段中的角色。',
    '思维品质：在4人小组中合理分工、有效协作，在"选主题→策划→制作→展示"中培养项目全流程管理思维。',
    '学习能力：回顾本单元及整册书的学习内容，建立"从课本知识到真实项目"的迁移能力。'
  ],
  keyPoints: '① 展板四模块：Music & Identity（一首定义你的歌）→ Music & Emotion（音乐与情绪的科学/个人体验）→ Music & Connection（音乐如何连接人——引入 Virtual Choir 理念）→ Music & Future（音乐将如何继续影响你/世界）② 单元知识整合：音乐词汇/分词作状语/音乐推荐/演讲稿修辞 ③ 每组还需准备一段 1 分钟的"展板导览演讲"。',
  difficulties: '① 四模块的"人生叙事感"——从 identity→emotion→connection→future 要有一条成长线。② Music & Connection 模块最容易平淡——需要联系 Virtual Choir 的理念。③ 导览演讲的时间控制——1分钟很紧，只说亮点。',
  teachingMethods: '① PBL项目式学习：以音乐展为驱动问题。② 小组协作：角色分工+module checklist。③ 展览+导览演讲+最佳展板评选。',
  preparation: '【PPT课件】P1 单元回顾五课内容+整册书回顾（五单元思维导图）；P2 展板四模块结构；P3 角色分工卡；P4 范例参考；P5 评价量规；P6 自评表；P7 总结+Book 2 收官。【实物教具】A3白纸每组一张；彩笔/马克笔；角色分工卡 printed；Book 2 全册学习证书（可选，增加仪式感）。',
  process: [
    { step: 'Book 2 全册回顾', time: '6', content: '【PPT P1 全册思维导图】教师带学生回顾 Book 2 五个单元：U1 文化遗产保护（定语从句）→ U2 野生动物保护（进行时被动）→ U3 互联网改变生活（完成时被动）→ U4 历史与传统（过去分词作宾补）→ U5 音乐与人生（过去分词作状语）。教师：Today is our final project of Book 2 — let\'s make it unforgettable! 预设回答跟读回顾五单元主题。板书时机：左栏画五单元主题+语法链。差异化提示：B班看PPT读关键词；A班说出每单元最喜欢的课文+一句原因。易错点提醒：五个单元学了三类被动语态+两种分词用法——这些语法不是独立的知识点，而是一个"英语如何表达动作与状态"的完整系统。' },
    { step: '任务布置+分工', time: '6', content: '【PPT P2 展板结构】【PPT P3 角色卡】教师展示四模块：①Music & Identity — What song defines YOU? ②Music & Emotion — How does music affect your feelings? (science+personal) ③Music & Connection — How does music bring people together? (connect to Virtual Choir!) ④Music & Future — How will music continue to shape your life/world? 角色：Identity Writer / Emotion Researcher / Connection Designer / Future Visionary。教师：Choose what story your board will tell! 预设回答：We want to show how music changes from childhood to adulthood — the songs that define us at different ages. 板书时机：留模块结构和角色。差异化提示：B班给语言模板+主题建议；A班自由策划+要求有"一条故事线"串联四模块。易错点提醒：最好的展板不堆信息——它讲一个故事。四模块之间要有一条线串联（如"从童年儿歌到青年摇滚——我的人生配乐"）。' },
    { step: '制作展板', time: '15', content: '【PPT P4 范例参考】【实物 A3纸】小组制作。教师巡视提醒：①全英文！②每模块至少3句完整句 ③至少2个过去分词作状语 ④至少1个 rhetorical question ⑤最后3分钟准备导览演讲。预设回答：（小组制作中）板书时机：无。差异化提示：B班给每模块句型开头+范例参考；A班独立完成+追求设计美感。易错点提醒：展板不是"贴在墙上的PPT"——留白、对齐、字体层次这些设计元素跟文字同样重要。标题是读者最先看到的，必须最大最突出。' },
    { step: '导览演讲+评价', time: '10', content: '【PPT P5 量规】每组 1 分钟导览演讲——假装全班是展览参观者，你是策展人。全班投票：最佳主题策划/最佳设计/最佳导览演讲/最打动人的展板。教师：You are the curator — take us through your exhibition! 预设回答展示。板书时机：记录投票结果。差异化提示：B班可看展板导览；A班尽量脱稿+用手指展板引导观众视线。易错点提醒：导览演讲 ≠ 读展板上的字——说展板上没有的故事。"We chose this theme because..." "The most surprising thing we learned was..."' },
    { step: 'Book 2 收官+自评', time: '3', content: '【PPT P7 总结+收官】教师宣布最佳展板。学生完成 Book 2 最终自评：①必修第二册我最大的进步是？②我还需要加强的是？③暑假/下学期我的英语学习目标是？教师：Congratulations on completing Book 2! You\'ve come a long way. 预设回答：My biggest progress is that I can now use passive voice in different tenses. / I want to improve my speaking fluency over the summer. 板书时机：写 Best Board 的主题名+导览金句。差异化提示：B班中文写；A班英文写。易错点提醒：学完一册书的标志不是你做了多少题——而是你能不能用这册书学到的语言，讲一个你自己的故事。今天的展板就是你的答案。' }
  ],
  blackboard: '┌─ U5 Project: Music & Life Exhibition ──┐\n│ 🎵 Music Journey:                        │\n│  ① Music & Identity (your song)         │\n│  ② Music & Emotion (science+personal)   │\n│  ③ Music & Connection (Virtual Choir!)  │\n│  ④ Music & Future (your vision)         │\n│                                          │\n│ 👥 Roles: Identity Writer / Emotion      │\n│    Researcher / Connection Designer /    │\n│    Future Visionary                      │\n│                                          │\n│ ⭐ Must: ≥2 V-ed as adverbial            │\n│    ≥1 rhetorical question               │\n│    1-min curator tour speech            │\n│                                          │\n│ 🏆 Book 2 Complete! 🏆                   │\n│  U1 Heritage → U2 Wildlife → U3 Net     │\n│  → U4 History → U5 Music                │\n└──────────────────────────────────────────┘',
  exercises: '【基础作业】完成小组展板，拍照片提交。写 40 词英文 Book 2 学习反思：最大收获+暑假英语计划。【提高作业】暑假挑战：用英文写 3 篇日记，每篇用本册书一个单元的语法点（定语从句/被动语态/分词）。【参考答案——教师用】反思示例：My biggest takeaway from Book 2 is the past participle as adverbial — "Moved by the music, I started singing." Now I can write more elegantly. Over the summer, I plan to read one English article every day and collect 5 good sentences. My goal for next semester: speak English in class every day, even if just one sentence.',
  reflection: '✅ 亮点：作为 Book 2 收官课，"五单元主题链+语法系统化"回顾让学生看到完整的学习图景，展板产出质量高。⚠️ 需改进：1分钟导览时间太紧，下次可给 2 分钟。📌 学期衔接：暑期建议——每天 10 分钟英语听力/1 篇英语阅读，保持语感。期待必修第三册再见！'
}));

// ====== 写回 lessons.js ======
const lessonsPath = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(lessonsPath);

// 移除旧数据，追加新数据
const rest = lessons.filter(l => !l.id.startsWith('l-eng-b2-u5-'));
const updated = rest.concat(periods);

fs.writeFileSync(lessonsPath, 'module.exports = ' + JSON.stringify(updated, null, 2) + ';\n', 'utf-8');

console.log('OK: l-eng-b2-u5 generated (' + periods.length + ' lessons)');
console.log('  IDs: ' + periods.map(p => p.id).join(', '));
