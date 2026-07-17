# -*- coding: utf-8 -*-
"""照片地图接口（best-effort）。

课堂版 PPT 的「真实照片 + 共识教学法」是精品层的两大支柱。
但 857 课做不了 857 次视频/图片调研，故本接口默认返回 {} ——
即每课走「学科色块 + 大字课文名」的优雅兜底（同设计系统，非偷懒空白）。

后续若要逐课富集真实照片：在 CURATED 里按 lesson id 填
{'cover': 绝对路径, 'bg': 绝对路径} 即可，mapper 会自动用真照片 + 正确遮罩。
"""
import os

CURATED = {
    # 例：'l-cn-bs-u1-1': {'cover': r'.../x.jpg', 'bg': r'.../y.jpg'},
}

def get_photos(lesson):
    """返回 {'cover': path, 'bg': path} 或 {}。"""
    lid = lesson.get('id')
    if lid and lid in CURATED:
        e = CURATED[lid]
        out = {}
        if e.get('cover') and os.path.exists(e['cover']):
            out['cover'] = e['cover']
        if e.get('bg') and os.path.exists(e['bg']):
            out['bg'] = e['bg']
        return out
    return {}
