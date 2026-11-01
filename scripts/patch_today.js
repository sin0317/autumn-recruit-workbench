const fs = require('fs');
const path = 'D:/buddy工作空间/2026-08-31-08-29-37/秋招工作台/recruit-data.json';
const data = JSON.parse(fs.readFileSync(path, 'utf8'));

const today = '2026-09-12';
data.meta.updatedAt = today;

function byId(id) { return data.records.find(r => r.id === id); }

// 1) 中石油 cnpc：官方确认截止 2026-10-15
const cnpc = byId('cnpc-2027');
if (cnpc) {
  cnpc.position = '2027校园招聘（正式批，油气勘探开发/炼化/新能源/数字化/经管等多方向）';
  cnpc.deadline = '2026-10-15';
  cnpc.deadlineNote = '官方确认2026秋招9.9启动，报名截止2026-10-15 23:59（中国石油高校毕业生招聘平台为唯一渠道）';
  cnpc.source = '中国石油网 cnpc.com.cn / 中国石油高校毕业生招聘平台 zhaopin.cnpc.com.cn';
  cnpc.publishedAt = '2026-09-09';
  cnpc.target = '2027届（2026届未就业亦可）';
}

// 2) 中国国新 guoxin：真实截止 2026-10-23
const guoxin = byId('guoxin-2027');
if (guoxin) {
  guoxin.deadline = '2026-10-23';
  guoxin.deadlineNote = '网申截止2026-10-23（国聘网列名国脉新星计划，14家子企业）';
}

// 3) 中国海油 cnooc：细化预测节点
const cnooc = byId('cnooc-2027');
if (cnooc) {
  cnooc.deadlineNote = '网上报名预计2026年9月21日左右启动、持续至10月底（预测，以官网为准）；统一笔试约11月中旬';
}

// 4) 新增 4 家 2027届央企校招
const additions = [
  {
    id: 'cec-2027',
    org: '中国电子',
    position: '2027届校园招聘（集成电路 / 计算机 / 电子信息 / 自动化 / 软件 / 电气 / 经管 / 法学等，北京/上海/深圳/武汉/成都等10城）',
    category: '央国企',
    batch: '正式批',
    deadline: '',
    deadlineNote: '2027届校招于2026-09-04正式启动，招满即止（以官网为准）',
    source: '中国电子招聘 career.cec.com.cn / 国聘网',
    publishedAt: '2026-09-04',
    url: 'https://career.cec.com.cn',
    target: '2027届'
  },
  {
    id: 'cmg-2027',
    org: '招商局集团',
    position: '2027届全球校园招聘（交通物流 / 金融 / 船舶 / 生产运营 / 工程技术 / AI / 建筑设计 / 法务等多方向）',
    category: '央国企',
    batch: '正式批',
    deadline: '',
    deadlineNote: '各板块单位2026年9月上旬起陆续发布岗位，招满即止（以官网为准）',
    source: '招商局集团招聘官网 / 国聘网',
    publishedAt: '2026-09-01',
    url: 'https://www.cmhk.com',
    target: '2027届'
  },
  {
    id: 'cssgc-2027',
    org: '中国兵器装备集团',
    position: '2027届校园招聘（军工研发 / 技术 / 制造方向，兵器工业+兵器装备联合秋招）',
    category: '央国企',
    batch: '正式批',
    deadline: '',
    deadlineNote: '2027届校招于2026年9月联合启动，全年37场招聘会陆续开展，招满即止（以官网为准）',
    source: '国务院国资委人事招聘专栏 / 国资小新 / 国聘网',
    publishedAt: '2026-09-01',
    url: 'https://www.iguopin.com',
    target: '2027届（理工科为主）'
  },
  {
    id: 'powerchina-2027',
    org: '中国电建',
    position: '2027届校园招聘（电气 / 能源动力 / 土木 / 新能源 / 机械 / 计算机 / 造价等，六险二金）',
    category: '央国企',
    batch: '正式批',
    deadline: '',
    deadlineNote: '下属各单位2026年9月1日起陆续启动网申，招满即止（以官网为准）',
    source: '中国电建招聘 powerchina.cn / 高校就业网',
    publishedAt: '2026-09-01',
    url: 'https://www.powerchina.cn',
    target: '2027届本科及以上'
  }
];

for (const rec of additions) {
  if (!byId(rec.id)) data.records.push(rec);
}

fs.writeFileSync(path, JSON.stringify(data, null, 2) + '\n', 'utf8');
console.log('records:', data.records.length, 'updatedAt:', data.meta.updatedAt);
console.log('cnpc.deadline=', cnpc.deadline, '| guoxin.deadline=', guoxin.deadline);
