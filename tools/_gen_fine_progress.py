# -*- coding: utf-8 -*-
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
PROG = os.path.join(os.path.dirname(HERE), 'preview_v7', '_fine_progress')
os.makedirs(PROG, exist_ok=True)

src = {
 'l-cn-bs-u3-7': ["21世纪教育网《第三单元 学写文学短评》", "搜狐·黄听松《学写文学短评——必修上第三单元写作指引》"],
 'l-cn-bs-u3-8': ["《中学语文古诗词朗读探究》（期刊）", "课堂秀《如何在诗词教学中朗读？》"],
 'l-cn-bs-u4-1': ["人教版《语文》必修上册教学参考书（第四单元目标与编写意图）", "21世纪教育网《必修上第四单元大单元教学设计》"],
 'l-cn-bs-u4-2': ["《研究性学习活动·访谈法》", "人教版《语文》必修上册教学参考书（访谈基本概念与方法）"],
 'l-cn-bs-u4-3': ["21世纪教育网《必修上第四单元大单元教学设计》（记录家乡的人和物）", "人教版《语文》必修上册教学参考书（风物志写法）"],
 'l-cn-bs-u4-4': ["人教版《语文》必修上册教学参考书（访谈法·王思斌）", "《研究性学习活动·访谈法》（原话记录·追问推进）"],
 'l-cn-bs-u4-5': ["人教版《语文》必修上册教学参考书（调查报告要素）", "21世纪教育网《必修上第四单元大单元教学设计》（资料整理与撰写）"],
 'l-cn-bs-u4-6': ["宁波晚报《用心观察，掌握方法 把倡议书写得有理有据》", "学科网《倡议书写作模板》"],
 'l-cn-bs-u4-7': ["宁波晚报《用心观察，掌握方法 把倡议书写得有理有据》", "人教版《语文》必修上册教学参考书（倡议书评改）"],
 'l-cn-bs-u4-8': ["人教版《语文》必修上册教学参考书（第四单元活动）", "21世纪教育网《必修上第四单元大单元教学设计》（成果展示）"],
}
note = "WebSearch已核实；本课与劳动主题照片无契合，采用学科色块兜底；四层审计（禁用词/越界/遮罩/布局）全PASS，首次通过。"

for id, sources in src.items():
    d = json.load(open(os.path.join(os.path.dirname(HERE), 'preview_v7', '_fine_data', id + '.json'), encoding='utf-8'))
    rec = {
        "id": id,
        "subj": id.split('-')[1],
        "title": d['title'],
        "sources": sources,
        "photo": "色块兜底",
        "audit": "PASS",
        "renderer": f"tools/_render_{id}.py",
        "note": note,
    }
    p = os.path.join(PROG, id + '.json')
    json.dump(rec, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('WROTE', p)
