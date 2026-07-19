# 逐课精细化管线 · 运行说明（开放网络环境）

目标：把 **636 课**管线版（`preview_v7/_fine_progress/<id>.json` 标记 `数据驱动/pipeline`）升级为真正的
**§4.4 逐课精细化 = 联网核实 + 真实照片 + 手写精排**。

> 为什么不在本 Agent 沙箱做：沙箱代理封锁了所有真实图片源（Wikimedia / 维基 / Google / 图床 / 必应图均不可下载），
> 无法抓取每课真实照片。此管线需在**能直连外网**的机器（你的 Windows / Mac 终端）上运行。

## 前置（一次性）
```bash
# 1) 拿到最新仓库（SSH 已配置）
git clone git@github.com:katarakinkim-arch/english-lesson-miniprogram.git
cd english-lesson-miniprogram

# 2) Python 依赖（需要 python-pptx + Pillow；建议用 venv）
python -m venv .venv && source .venv/bin/activate
pip install python-pptx Pillow requests   # requests 非必须，urllib 已够用

# 3) 确认能访问外网
curl -s -o /dev/null -w "%{http_code}\n" https://commons.wikimedia.org/w/api.php?action=query&format=json&meta=siteinfo
# 期望 200
```

## 运行（主入口）
```bash
# 全量补齐 636 课（可中断，重跑自动续做）
python tools/_fine_driver.py

# 常用参数
python tools/_fine_driver.py --only-subj phy        # 先单科试点
python tools/_fine_driver.py --only-subj phy --batch 5 --limit 20   # 小批量试跑
python tools/_fine_driver.py --batch 15             # 每 15 课提交一次
```

驱动每课做的事：
1. 跳过已真正精细化的课（进度 JSON 来源不含 `数据驱动/pipeline`）。
2. `tools/_fetch_photo.py` 从 **Wikimedia Commons**（自由授权真实照片）按本课中/英查询词抓图 → `tools/_photos_<id>/cover.jpg`（英文查询兜底；Commons 没有则退回必应缩略图）。
3. `tools/_fetch_source.py` 从 **Wikipedia** 取权威摘要+来源 URL → `tools/_fine_src/<id>.txt`。
4. `tools/_fine_one.py` 用真实照片 + 来源引用渲染 **9 页手写精排 PPTX**（复用已验证结构，几何安全）。
5. `tools/_run_audit_one.py` 过**四层审计**（文本口吻/越界/遮罩/排版），必须 PASS。
6. 写进度 JSON（含真实来源）；每 `--batch` 课 `git add + commit + push`（SSH 带超时）。
7. 中断后重跑自动跳过已完成课。

## 产物
- 每课真实照片：`tools/_photos_<id>/cover.jpg`（建议后续 `.gitignore` 或单独管理，体积可控）
- 每课来源文本：`tools/_fine_src/<id>.txt`
- 每课 PPTX：`preview_v7/<subj>/<id>.pptx`（已含真实照片 + 来源引用）
- 进度：`preview_v7/_fine_progress/<id>.json`（`sources` 为真实核实来源，不再是 "数据驱动"）

## 已就绪的本地前置（无需外网即可生成）
- `tools/_build_fine_queries.py` → 已生成 `tools/_fine_queries.json`（636 课的中/英照片查询词 + 来源查询词）。
- 渲染器/抓取器/驱动脚本均已提交。
- 渲染器已用占位图验证：真实照片插槽 + 来源引用不影响四层审计（PASS）。

## 备注
- 若某课 Commons/必应都取不到图，`photo` 字段记 "未取到真实照片(需补)"，PPTX 照片位留空，可后续人工补。
- 完成后跑 `python tools/_sync_track.js` 同步进度表，并把 `_RESEARCH_TRACK.md` 的"待重做"归零。
