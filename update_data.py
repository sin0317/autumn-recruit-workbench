#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日校招情报合并脚本：更新 recruit-data.json（仅 2027 届，排除社招）。"""
import json, os

DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(DIR, "recruit-data.json")

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---- 1) 更新已存在记录（以 id 为键）----
updates = {
    "bytedance-2027": {
        "deadline": "2027-05-31",
        "deadlineNote": "全年滚动招聘，岗位招满即下架（网申开放至2027-05-31）",
        "source": "字节跳动招聘官网 jobs.bytedance.com / 中公网校",
        "publishedAt": "2026-08-03",
    },
    "tencent-2027": {
        "deadlineNote": "招满即止；官方建议8-10月集中面试与录用，尽早投递",
        "source": "腾讯招聘官网 join.qq.com / 光明网",
    },
    "meituan-2027": {
        "deadlineNote": "网申8.17-10.31，部分岗位招满即提前结束；9月起面试",
        "source": "美团校招官网 zhaopin.meituan.com / 南京本地宝",
    },
    "chinaunicom-2027": {
        "deadline": "2026-09-22",
        "deadlineNote": "网申窗口约8.25-9.22（新苗计划），招满即止；11月上旬笔试（以官网为准）",
        "source": "中国联通官网(人力资源专区) / 牛企直聘(企业公众号)",
        "publishedAt": "2026-08-27",
    },
    "sgcc-2027": {
        "deadlineNote": "提前批预计2026年9月发布（面向硕博）；一批预计11月中旬公告、12月上旬笔试（预测，以官网为准）",
        "source": "国家电网人力资源招聘平台 zhaopin.sgcc.com.cn",
    },
    "china-railway-2027": {
        "deadlineNote": "各局时间不同；集中公告预计2026年10月31日前后（预测，以铁路人才网为准）",
        "source": "中国铁路人才招聘网 rczp.china-railway.com.cn",
    },
    "chinamobile-2027": {
        "deadlineNote": "正式批网申8月底-9月开启，持续至10月中下旬，10月底集团统一笔试（预测，以官网为准）",
        "source": "中国移动招聘官网 job.10086.cn / 北理工就业网",
    },
    "chinatelecom-2027": {
        "deadlineNote": "8月底启动网申，持续至11月，各省分公司截止不同，招满即止（以分公司公告为准）",
        "source": "中国电信招贤纳士专栏 / 高顿",
    },
}

by_id = {r["id"]: r for r in data["records"]}
for rid, patch in updates.items():
    if rid in by_id:
        by_id[rid].update(patch)
    else:
        print(f"[warn] 未找到记录 {rid}")

# ---- 2) 追加新发现记录（去重）----
new_records = [
    {
        "id": "vivo-2027",
        "org": "vivo",
        "position": "算法 / 软件 / 硬件 / 通信 / 测试 / 营销 / 市场 / 设计 / 产品运营 / 供应链（10大类别250+方向）",
        "category": "互联网大厂",
        "batch": "正式批",
        "deadline": "2026-09-15",
        "deadlineNote": "网申即日起-9月15日12:00；9月20-24日线下面试",
        "source": "vivo招聘官网 hr-campus.vivo.com / 中国科大就业网",
        "publishedAt": "2026-09-01",
        "url": "https://hr-campus.vivo.com/",
        "target": "2027届（2026.8-2027.7毕业）",
    },
    {
        "id": "horizon-2027",
        "org": "地平线",
        "position": "算法 / 芯片 / 软件 / 硬件 / 测试 / 业务拓展（智能驾驶与机器人，物理AI）",
        "category": "互联网大厂",
        "batch": "正式批",
        "deadline": "2026-10-30",
        "deadlineNote": "网申8.10-10.30；9月1日空中宣讲（多平台直播）",
        "source": "地平线招聘 / 北京大学就业信息网",
        "publishedAt": "2026-08-10",
        "url": "https://wecruit.hotjob.cn/SU62d915040dcad43c775ec12c/mc/position/campus?channelId=149807",
        "target": "2027届（2026.9.1-2027.8.31毕业）",
    },
    {
        "id": "didi-2027",
        "org": "滴滴",
        "position": "工程 / 算法 / 机器人 / 产品 / 安全技术 / 运营 / 数据 / 商分 / 金融业务",
        "category": "互联网大厂",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "招满即止",
        "source": "滴滴校招官网 campus.didiglobal.com",
        "publishedAt": "2026-08-13",
        "url": "http://campus.didiglobal.com",
        "target": "2027届（2026.9-2027.8毕业）",
    },
    {
        "id": "cmb-tech-2027",
        "org": "招商银行·招银网络科技",
        "position": "2027秋季校园招聘（科技 / 研发方向，金融科技岗）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "2026-09-20",
        "deadlineNote": "第一批网申7.30-9.3 18时已截止；第二批至9.20 18时；技术测评9.21，面试9.29-10.20",
        "source": "招银网络科技招聘 / 华北电力大学就业指导中心",
        "publishedAt": "2026-07-30",
        "url": "https://career.cmbchina.com",
        "target": "2027届",
    },
    {
        "id": "icbc-2027",
        "org": "中国工商银行",
        "position": "2027年度校园招聘（总行及境内分行，管培 / 科技菁英 / 客户经理等）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "预计2026年9月5日-10月9日网申，11月2日笔试（预测，以官网为准）",
        "source": "工行招聘官网 job.icbc.com.cn / 今日头条",
        "publishedAt": "",
        "url": "https://job.icbc.com.cn",
        "target": "2027届（2026届未就业亦可）",
    },
    {
        "id": "abc-2027",
        "org": "中国农业银行",
        "position": "2027年度校园招聘（总行 / 境内分行 / 子公司，管培 / 科技英才等）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "预计2026年9月5日-10月9日网申，11月1日笔试（预测，以官网为准）",
        "source": "农行招聘官网 career.abchina.com.cn / 今日头条",
        "publishedAt": "",
        "url": "https://career.abchina.com.cn",
        "target": "2027届（2026届未就业亦可）",
    },
    {
        "id": "boc-2027",
        "org": "中国银行",
        "position": "2027年全球校园招聘（总行 / 境内分行 / 海外及综合经营公司）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "预计2026年9月5日-10月10日网申，笔试分批次（预测，以官网为准）",
        "source": "中国银行官网人才招聘专栏 / 今日头条",
        "publishedAt": "",
        "url": "https://www.boc.cn",
        "target": "2027届（2026届未就业亦可）",
    },
    {
        "id": "ccb-2027",
        "org": "中国建设银行",
        "position": "2027年度校园招聘（总行直属机构 / 各省市分行）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "预计2026年9月上旬发公告，网申约至10月10日（预测，以官网为准）",
        "source": "建行招聘官网 job.ccb.com / 高顿",
        "publishedAt": "",
        "url": "http://job.ccb.com",
        "target": "2027届（2026届未就业亦可）",
    },
    {
        "id": "bocom-2027",
        "org": "交通银行",
        "position": "2027届校园招聘（总行 / 境内分行 / 子公司）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "预计2026年9-10月网申（预测，以官网为准）",
        "source": "交行招聘官网 job.bankcomm.com / 国聘网",
        "publishedAt": "",
        "url": "https://job.bankcomm.com",
        "target": "2027届（2026届未就业亦可）",
    },
    {
        "id": "psbc-2027",
        "org": "中国邮政储蓄银行",
        "position": "2027届校园招聘（总行 / 各分行）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "预计2026年9-10月网申（预测，以官网为准）",
        "source": "邮储银行招聘官网 / 国聘网",
        "publishedAt": "",
        "url": "https://www.psbc.com",
        "target": "2027届（2026届未就业亦可）",
    },
]

added = []
for rec in new_records:
    if rec["id"] not in by_id:
        data["records"].append(rec)
        added.append(rec["id"])
    else:
        print(f"[skip] 已存在 {rec['id']}，跳过追加")

# ---- 3) 更新 meta ----
data["meta"]["updatedAt"] = "2026-09-03"

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"[OK] records 总数 = {len(data['records'])}，本次新增 = {len(added)} -> {added}")
