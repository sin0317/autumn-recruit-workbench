#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026-09-23 一次性补丁：工作台转向「秋招正职」+ 补齐传媒/影视/文化类对口单位。
- 追加 4 条传媒影视类央国企正式批记录（deadline 留空，deadlineNote 标注待公告/预测）
- 更新 meta.scope 明确「正式岗位、排除实习」
- 更新 meta.updatedAt
不删除任何既有记录。
"""
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(DIR, 'recruit-data.json')

NEW = [
    {
        "id": "xinhua-2027",
        "org": "新华通讯社（新华社）",
        "position": "采编 / 融媒体 / 外文 / 经营职能 / 技术研发（总社及国内分社）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "2027届公告待官网发布；往年10月前后发布、招满即止（预测，以官网为准）",
        "source": "新华社人才招聘网 job.news.cn",
        "publishedAt": "",
        "url": "https://job.news.cn/",
        "target": "2027届（2027年7月底前取得学历学位；英语六级≥425）"
    },
    {
        "id": "cmg-cctv-2027",
        "org": "中央广播电视总台（含中国国际电视总公司）",
        "position": "编导 / 后期包装制作 / 内容运营 / 新媒体视觉（需提交作品集）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "2027届公告待官网发布；往年10-11月启动，须提交作品集（预测，以官网为准）",
        "source": "央视总台招聘官网 career.cntv.cn",
        "publishedAt": "",
        "url": "https://career.cntv.cn/",
        "target": "2027届本科及以上（本科≤25、硕士≤28）"
    },
    {
        "id": "mgtv-2027",
        "org": "芒果TV（湖南快乐阳光互动娱乐传媒）",
        "position": "内容运营（电视剧/综艺）/ 影视策划 / 市场营销 / 产品",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "2027届秋招正式批待公告；参考往年9-10月启动（预测，以官网为准）",
        "source": "芒果TV校招官网（Moka）",
        "publishedAt": "",
        "url": "https://app.mokahr.com/campus-recruitment/mgtv/44490",
        "target": "2027届（新闻/编导/影视文学等传媒类优先）"
    },
    {
        "id": "migu-2027",
        "org": "中国移动咪咕公司",
        "position": "内容类 / 运营类 / 产品类 / 研发类（视频、音乐、阅读、游戏）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "2027届秋招待公告；参考2026届网申9月上旬-10月中旬（预测，以官网为准）",
        "source": "咪咕招聘 job.migu.cn",
        "publishedAt": "",
        "url": "https://job.migu.cn",
        "target": "2027届本科及以上"
    },
]

SCOPE = ("仅面向 2027 届毕业生的秋季校园招聘【正式岗位】（毕业时间约 2026.9–2027.8）；"
         "排除社会招聘、社招通道与纯实习岗位。覆盖：央国企 + 互联网大厂，"
         "并重点补充传媒 / 影视 / 文化类对口单位（新华社、中央广播电视总台、芒果TV、咪咕等）。")


def main():
    with open(PATH, encoding='utf-8') as f:
        data = json.load(f)

    data.setdefault('meta', {})
    data['meta']['updatedAt'] = '2026-09-23'
    data['meta']['scope'] = SCOPE

    records = data.setdefault('records', [])
    existing = {r.get('id') for r in records}

    added = 0
    for rec in NEW:
        if rec['id'] in existing:
            # 已存在则只刷新字段，不新增
            for r in records:
                if r.get('id') == rec['id']:
                    r.update(rec)
            continue
        records.append(rec)
        added += 1

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print('[OK] 新增 %d 条，总计 %d 条；updatedAt=%s' % (added, len(records), data['meta']['updatedAt']))


if __name__ == '__main__':
    main()
