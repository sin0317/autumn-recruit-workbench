#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日情报更新补丁：合并/新增 recruit-data.json 记录，更新 meta.updatedAt。"""
import json, datetime

PATH = r"D:\buddy工作空间\2026-08-31-08-29-37\秋招工作台\recruit-data.json"
TODAY = "2026-09-05"

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

records = {r["id"]: r for r in data["records"]}

# ---- 1) 已存在记录更新（以 id 为键合并） ----
updates = {
    "icbc-2027": {
        "deadline": "2026-10-08",
        "deadlineNote": "网上报名 2026.9.4-10.8；笔试 10 月下旬",
        "source": "工商银行招聘官网 job.icbc.com.cn",
        "publishedAt": "2026-09-04",
    },
    "abc-2027": {
        "deadline": "2026-10-08",
        "deadlineNote": "报名即日起-10.8 24时；笔试 10 月下旬或 11 月上旬",
        "source": "农业银行招聘官网 career.abchina.com.cn",
        "publishedAt": "2026-09-04",
    },
    "boc-2027": {
        "deadline": "2026-10-09",
        "deadlineNote": "报名截止 2026.10.9 24点；笔试 10 月中下旬",
        "source": "中国银行校招 campus.chinahr.com/pages/2027-boc",
        "publishedAt": "2026-09-03",
    },
    "ccb-2027": {
        "deadline": "2026-10-08",
        "deadlineNote": "报名截止 2026.10.8 24点；笔试 10 月底",
        "source": "建设银行招聘官网 job.ccb.com",
        "publishedAt": "2026-09-04",
    },
    "bocom-2027": {
        "deadlineNote": "六大行集中启动；交行预计 9-10 月网申（预测，以官网为准）",
    },
    "psbc-2027": {
        "deadlineNote": "六大行集中启动；邮储预计 9-10 月网申（预测，以官网为准）",
    },
    "chnenergy-2027": {
        "deadline": "2026-10-07",
        "deadlineNote": "统招网报 9.2-10.7；笔试 10.25；直招 9.19 截止",
        "source": "国家能源集团招聘 zhaopin.chnenergy.com.cn",
        "publishedAt": "2026-09-02",
    },
    "chinamobile-2027": {
        "deadline": "2026-10-08",
        "deadlineNote": "正式批网申 9 月初-10.8；笔试 10 月下旬（四川 10.24）",
        "source": "中国移动招聘官网 job.10086.cn",
        "publishedAt": "2026-09-02",
    },
    "cnpc-2027": {
        "deadlineNote": "预计 2026 年 9 月中旬开启网申（预测，以官网为准）",
    },
    "sinopec-2027": {
        "deadlineNote": "预计 2026 年 9 月下旬开启网申；笔试 11 月中下旬（预测，以官网为准）",
    },
    "sgcc-2027": {
        "deadlineNote": "提前批 9-10 月宣讲；一批预计 11 月初网申、12 月上旬笔试（预测，以官网为准）",
    },
}

for rid, fields in updates.items():
    if rid in records:
        records[rid].update(fields)
        print(f"[更新] {rid}")
    else:
        print(f"[跳过-不存在] {rid}")

# ---- 2) 新发现追加（2027届央国企，国聘网已列名） ----
new_recs = [
    {"id": "chinanuclear-2027", "org": "中国核电", "position": "2027届校园招聘（国企，中核集团旗下）",
     "category": "央国企", "batch": "正式批", "deadline": "", "deadlineNote": "招满即止（以官网为准）",
     "source": "国聘网 / 中国核电招聘", "publishedAt": TODAY, "url": "https://www.iguopin.com", "target": "2027届"},
    {"id": "citicbank-2027", "org": "中信银行", "position": "2027年校园招聘（科技 / 业务 / 职能）",
     "category": "央国企", "batch": "正式批", "deadline": "", "deadlineNote": "招满即止（以官网为准）",
     "source": "国聘网 / 中信银行招聘", "publishedAt": TODAY, "url": "https://www.iguopin.com", "target": "2027届"},
    {"id": "norinco-2027", "org": "中国兵器集团", "position": "2027届全球校园招聘",
     "category": "央国企", "batch": "正式批", "deadline": "", "deadlineNote": "招满即止（以官网为准）",
     "source": "国聘网", "publishedAt": TODAY, "url": "https://www.iguopin.com", "target": "2027届"},
    {"id": "faw-2027", "org": "中国一汽", "position": "2027届校园招聘",
     "category": "央国企", "batch": "正式批", "deadline": "", "deadlineNote": "招满即止（以官网为准）",
     "source": "国聘网 / 中国一汽招聘", "publishedAt": TODAY, "url": "https://www.iguopin.com", "target": "2027届"},
    {"id": "cccc-2027", "org": "中交集团", "position": "2027届全球校园招聘",
     "category": "央国企", "batch": "正式批", "deadline": "", "deadlineNote": "招满即止（以官网为准）",
     "source": "国聘网", "publishedAt": TODAY, "url": "https://www.iguopin.com", "target": "2027届"},
    {"id": "changan-2027", "org": "长安汽车", "position": "2027全球校园招聘",
     "category": "央国企", "batch": "正式批", "deadline": "", "deadlineNote": "招满即止（以官网为准）",
     "source": "国聘网 / 长安汽车招聘", "publishedAt": TODAY, "url": "https://www.iguopin.com", "target": "2027届"},
    {"id": "crland-2027", "org": "华润置地", "position": "2027届校园招聘",
     "category": "央国企", "batch": "正式批", "deadline": "", "deadlineNote": "招满即止（以官网为准）",
     "source": "国聘网 / 华润置地招聘", "publishedAt": TODAY, "url": "https://www.iguopin.com", "target": "2027届"},
    {"id": "cmsk-2027", "org": "招商蛇口", "position": "2027届校园招聘",
     "category": "央国企", "batch": "正式批", "deadline": "", "deadlineNote": "招满即止（以官网为准）",
     "source": "国聘网 / 招商蛇口招聘", "publishedAt": TODAY, "url": "https://www.iguopin.com", "target": "2027届"},
]

added = 0
for r in new_recs:
    if r["id"] not in records:
        data["records"].append(r)
        records[r["id"]] = r
        added += 1
        print(f"[新增] {r['id']} ({r['org']})")
    else:
        print(f"[已存在-跳过] {r['id']}")

# ---- 3) meta.updatedAt ----
data["meta"]["updatedAt"] = TODAY

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n[完成] 记录总数={len(data['records'])} 本次新增={added}")
