# 教案生产 SOP（人教版 2019 高中英语）

> 目标：每一份教案「拿去就能用」，减少老师重复劳动。U1 为金标准，U2–U5 及后续单元须逐字对齐本 SOP。

## 一、单元 = 8 课时结构

每单元按人教版教师用书拆为 8 节，`periodNumber` 1–8，`lessonType` 与导航标签、`id` 后缀如下：

| 课时 | lessonType | lessonTypeName | id 后缀 |
|------|------------|----------------|---------|
| 1 | listening-speaking | 听与说 | `ls` |
| 2 | reading | 阅读 | `r1` |
| 3 | reading | 阅读 | `r2` |
| 4 | grammar | 语法 | `g` |
| 5 | listening-talking | 听与谈 | `lt` |
| 6 | writing | 写作 | `w1` |
| 7 | writing | 写作 | `w2` |
| 8 | project | 项目复习 | `p` |

`id` / `lessonId` 格式：`l-eng-{册码}-u{单元}-{后缀}`，册码 b1/b2/b3。
`duration`：听说类 40，其余 45。`grade` 固定 `高一`，`subject` 固定 `英语`。
`tags`：`[lessonTypeName, 话题词×2, "人教版必修X U{n}", "第{n}节课"]`。

## 二、完整字段清单与规范

每课对象含以下字段，缺一不可（除非该课型确实无对应内容，须显式留空字符串）：

- **title**：`板块英文名: 主题 — 子标题`（中文子标题点明本节定位）
- **textbookAnalysis**：教材分析。本课在单元中的位置、语篇/语法点、与前后课衔接。
- **overview**：以「【学情分析】」开头，写 A/B 班分层（已有基础、薄弱点、共同问题）。
- **objectives**：4 条字符串数组，依次为 语言能力 / 文化意识 / 思维品质 / 学习能力，每条以维度名+冒号开头。
- **keyPoints**：用 ①②③ 编号，列核心词汇/句型/语篇结构。
- **difficulties**：用 ①②③ 编号，每条含「易错点 + 原因 + 提醒」。
- **teachingMethods**：用 ①②③ 编号，列教学法（任务型/支架/合作等）。
- **preparation**：含【PPT课件】（逐页编号+内容）+【实物教具】+【音频】三段。
- **process**：5–6 步数组，每步 `{ step, time, content }`。content 内须含：
  - 【PPT P? 页名】教师台词「…」
  - 预设回答「…」
  - 板书时机：…
  - 差异化提示：B班…；A班…
  - 易错点提醒：…
- **blackboard**：ASCII 框图，呈现本节板书布局。
- **exercises**：含【基础作业】+【提高作业】+【参考答案——教师用】三段。
- **reflection**：含 ✅亮点 + ⚠️需改进 + 📌下节课衔接 三段。

## 三、质量红线（自检）

1. 每条 process step 的 content 必须同时出现「PPT页号 / 教师台词 / 预设回答 / 板书时机 / 差异化提示 / 易错点提醒」六要素。
2. objectives 必须 4 条且维度齐全。
3. 作业必须有参考答案（教师用）。
4. 单元名（unitTitle）须与人教版实体书逐字一致（大小写、单复数）。
5. 同册内 id 全局唯一；reading 用 r1/r2、writing 用 w1/w2 区分。

## 四、生成流程

1. 复制 `tools/gen-u2.js` → `gen-u{n}.js`，替换单元号、unitTitle、8 课时内容。
2. 运行 `node tools/gen-u{n}.js`（自动替换该单元旧课、写回 lessons.js）。
3. 运行 `node tools/generate-preview.js` 重新生成预览。
4. 校验：`node -e "require('./data/lessons.js')"` 通过；分组=15、目标单元=8 课时、id 无重复。
5. `git add -A && git commit`，按单元一个 commit。
