import json

P = r"D:\buddy工作空间\2026-08-31-08-29-37\秋招工作台\recruit-data.json"
data = json.load(open(P, encoding='utf-8'))
recs = data['records']

def upd(rid, **kw):
    for r in recs:
        if r['id'] == rid:
            r.update(kw)
            return True
    return False

# —— 中广核：预测 -> 真实已启动 ——
upd('cgn-2027',
    batch='正式批',
    deadline='',
    deadlineNote='2027届秋招已启动（简历投递2026-09-04起，官网 cgn.hotjob.cn），招满即止；笔试约10月中旬（以官网为准）',
    source='中广核招聘 cgn.hotjob.cn / 北大就业网',
    publishedAt='2026-09-09',
    url='https://cgn.hotjob.cn',
    position='核电技术类 / 电气自动化与数字类（AI、网安）/ 机械材料土建类 / 综合职能类 / 核工程运行维修',
    target='2027届（含2026届未就业；统招应届，本科≤25/硕士≤28/博士≤33）')

# —— 中国华能：预测 -> 真实已启动 ——
upd('chng-2027',
    batch='正式批',
    deadline='',
    deadlineNote='2027届秋招已启动（集团官网9月中旬开放网申，持续至11月上旬；总部及在京单位网申截止约10-31，各子公司陆续截止，招满即止，以官网为准）',
    source='中国华能招聘 zhaopin.chng.com.cn / 高顿·上岸鸭',
    publishedAt='',
    url='https://zhaopin.chng.com.cn',
    position='电力/能源（核电、新能源、火电等）/ 工程 / 职能（含华能核电专项、英才/优才管培）',
    target='2027届（2026届未就业亦可）')

# —— 交通银行：预测 -> 真实（拿截止）——
upd('bocom-2027',
    batch='正式批',
    deadline='2026-10-12',
    deadlineNote='网申2026.9.5-10.12；笔试各分行自行组织（以官网为准）',
    source='交行招聘官网 job.bankcomm.com / 银行招聘网',
    publishedAt='2026-09-05',
    position='2027届校园招聘（总行 / 境内分行 / 子公司，科技/业务/职能）')

# —— 邮储银行：预测 -> 真实（拿截止）——
upd('psbc-2027',
    batch='正式批',
    deadline='2026-09-30',
    deadlineNote='网申2026.9.1-9.30（六大行截止最早）；笔试2026.10.26（以官网为准）',
    source='邮储银行招聘官网 / 银行招聘网',
    publishedAt='2026-09-01',
    position='2027届校园招聘（总行 / 各分行 / 控股子公司，金融科技/管培/基层）')

# —— 新增 4 家（国聘网列名 2027届央国企校招）——
new_recs = [
    {
        "id": "ceec-2027",
        "org": "中国能建",
        "position": "规划咨询 / 勘测设计 / 工程建设 / 装备制造 / 资本金融 / 国际业务 / 人工智能 / 数字信息 / 市场运营 / 通用职能（近1200岗位、5000+人）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "2027-06-30",
        "deadlineNote": "网申2026.9-2027.6，招满即止（全球校招，覆盖100+城市及海外）",
        "source": "国聘网 / 中国能建招聘 ceec.iguopin.com",
        "publishedAt": "2026-09-09",
        "url": "https://ceec.iguopin.com/",
        "target": "2027届（国内外高校）"
    },
    {
        "id": "cam-2027",
        "org": "中国机械科学研究总院集团",
        "position": "2027届校园招聘（科研 / 工程 / 职能方向）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "招满即止（以官网为准）",
        "source": "国聘网 https://www.iguopin.com",
        "publishedAt": "2026-09-09",
        "url": "https://www.iguopin.com",
        "target": "2027届"
    },
    {
        "id": "yalongjiang-2027",
        "org": "雅砻江水电",
        "position": "2027届校园招聘（水电 / 新能源 / 工程 / 职能方向）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "招满即止（以官网为准）",
        "source": "国聘网 https://www.iguopin.com",
        "publishedAt": "2026-09-09",
        "url": "https://www.iguopin.com",
        "target": "2027届"
    },
    {
        "id": "guoxin-2027",
        "org": "中国国新",
        "position": "2027届校园招聘（投资 / 金融 / 综合职能方向）",
        "category": "央国企",
        "batch": "正式批",
        "deadline": "",
        "deadlineNote": "招满即止（以官网为准）",
        "source": "国聘网 https://www.iguopin.com",
        "publishedAt": "2026-09-09",
        "url": "https://www.iguopin.com",
        "target": "2027届"
    },
]

ids = {r['id'] for r in recs}
added = []
for nr in new_recs:
    if nr['id'] not in ids:
        recs.append(nr)
        added.append(nr['id'])

data['meta']['updatedAt'] = '2026-09-11'
json.dump(data, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('records total:', len(recs))
print('updated: cgn, chng, bocom, psbc')
print('added:', added)
