#!/usr/bin/env node
/**
 * 秋招看板生成脚本
 * 读取 recruit-data.json -> 生成 recruit-seed.js（供工作台加载）+ dashboard.html（独立可视化看板）
 * 用法：node generate.js
 * 定时任务每天 8:00 执行：先更新 recruit-data.json，再跑本脚本重新生成看板。
 */
const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const DATA_PATH = path.join(DIR, 'recruit-data.json');
const SEED_PATH = path.join(DIR, 'recruit-seed.js');
const DASH_PATH = path.join(DIR, 'dashboard.html');

function loadData() {
  const raw = fs.readFileSync(DATA_PATH, 'utf8');
  return JSON.parse(raw);
}

// 与工作台/看板共用的状态计算逻辑
function statusOf(rec, today) {
  const t = today || new Date();
  const base = new Date(t.getFullYear(), t.getMonth(), t.getDate());
  const dl = rec.deadline ? new Date(rec.deadline + 'T00:00:00') : null;
  if (dl) {
    const diff = Math.round((dl - base) / 86400000);
    if (diff < 0) return { key: 'closed', label: '已截止', diff };
    if (diff <= 14) return { key: 'urgent', label: '即将截止', diff };
    return { key: 'open', label: '报名中', diff };
  }
  return { key: 'open', label: '报名中(待公布)', diff: null };
}

function statsOf(data, today) {
  const recs = data.records || [];
  let total = recs.length, open = 0, urgent = 0, closed = 0;
  recs.forEach(r => {
    const s = statusOf(r, today);
    if (s.key === 'closed') closed++;
    else { open++; if (s.key === 'urgent') urgent++; }
  });
  return { total, open, urgent, closed };
}

function buildSeed(data) {
  const payload = {
    meta: data.meta,
    records: data.records,
    generatedAt: new Date().toISOString()
  };
  return 'window.__RECRUIT_DATA__ = ' + JSON.stringify(payload, null, 2) + ';\n';
}

function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function buildDashboard(data) {
  const today = new Date();
  const st = statsOf(data, today);
  const recs = (data.records || []).slice().sort((a, b) => {
    const da = a.deadline || '9999-12-31';
    const db = b.deadline || '9999-12-31';
    return da < db ? -1 : da > db ? 1 : 0;
  });

  const catCount = {};
  recs.forEach(r => { catCount[r.category] = (catCount[r.category] || 0) + 1; });

  const urgentList = recs
    .map(r => ({ r, s: statusOf(r, today) }))
    .filter(x => x.s.key === 'urgent')
    .map(x => `<li><b>${esc(x.r.org)}</b> · ${esc(x.r.position.split(' / ')[0])} — 还剩 <span class="coral">${x.s.diff} 天</span>（${esc(x.r.deadline)}）<a href="${esc(x.r.url)}" target="_blank" rel="noopener">公告↗</a></li>`)
    .join('') || '<li class="muted">未来 14 天内暂无明确截止的岗位（多为招满即止，请持续关注）。</li>';

  const closedList = recs
    .map(r => ({ r, s: statusOf(r, today) }))
    .filter(x => x.s.key === 'closed')
    .map(x => `<li><b>${esc(x.r.org)}</b> · ${esc(x.r.batch)}（截止 ${esc(x.r.deadline)}）<a href="${esc(x.r.url)}" target="_blank" rel="noopener">公告↗</a></li>`)
    .join('') || '<li class="muted">暂无已截止记录。</li>';

  const rows = recs.map(r => {
    const s = statusOf(r, today);
    const badge = r.category === '央国企' ? 'badge-soe' : 'badge-net';
    const stat = s.key === 'closed' ? 'st-closed' : s.key === 'urgent' ? 'st-urgent' : 'st-open';
    return `<tr>
      <td class="org">${esc(r.org)}</td>
      <td>${esc(r.position)}</td>
      <td><span class="badge ${badge}">${esc(r.category)}</span></td>
      <td>${esc(r.batch)}</td>
      <td class="${stat}">${r.deadline ? esc(r.deadline) : '<span class="muted">待公布</span>'}${r.deadlineNote ? `<br><span class="note">${esc(r.deadlineNote)}</span>` : ''}</td>
      <td class="${stat}">${esc(s.label)}</td>
      <td class="muted">${esc(r.source)}<br>${r.publishedAt ? '发布 ' + esc(r.publishedAt) : '发布待定'}</td>
      <td><a href="${esc(r.url)}" target="_blank" rel="noopener" class="coral">查看↗</a></td>
    </tr>`;
  }).join('');

  const catBars = Object.keys(catCount).map(c => {
    const n = catCount[c];
    const pct = Math.round(n / st.total * 100);
    const cls = c === '央国企' ? 'bar-soe' : 'bar-net';
    return `<div class="catrow"><span class="catname">${esc(c)}</span>
      <span class="catbar"><span class="${cls}" style="width:${pct}%"></span></span>
      <span class="catnum">${n}</span></div>`;
  }).join('');

  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>2027届秋招 · 可视化看板</title>
<style>
  :root{
    --cream:#FAF8F3; --cream2:#F3EEE5; --ink:#2E2A33; --muted:#8A8493;
    --purple:#E7DEF7; --purple-d:#B49BDb; --purple-deep:#6E52A6;
    --coral:#FF7A66; --coral-d:#E85C47; --line:#ECE5DA;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--cream);color:var(--ink);
    font-family:-apple-system,"PingFang SC","Microsoft YaHei",system-ui,sans-serif;line-height:1.6}
  .wrap{max-width:1080px;margin:0 auto;padding:32px 20px 60px}
  h1{font-family:"Songti SC","Noto Serif SC",Georgia,serif;font-size:34px;margin:0 0 4px}
  .sub{color:var(--muted);font-size:14px;margin-bottom:24px}
  .cards{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:28px}
  .card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 16px;
    box-shadow:0 4px 18px rgba(110,82,166,.06)}
  .card .n{font-size:32px;font-weight:800;font-family:"Songti SC",serif}
  .card .l{color:var(--muted);font-size:13px;margin-top:2px}
  .card.coral .n{color:var(--coral-d)} .card.soe .n{color:var(--purple-deep)}
  .card.purple{background:linear-gradient(135deg,#F3ECFB,#E7DEF7)} 
  .sec{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;margin-bottom:22px;
    box-shadow:0 4px 18px rgba(110,82,166,.05)}
  .sec h2{font-family:"Songti SC",serif;font-size:20px;margin:0 0 12px;display:flex;align-items:center;gap:8px}
  .sec h2::before{content:"";width:6px;height:18px;background:var(--coral);border-radius:3px;display:inline-block}
  ul.remind{margin:0;padding-left:0;list-style:none}
  ul.remind li{padding:8px 0;border-bottom:1px dashed var(--line);font-size:14px}
  ul.remind li:last-child{border-bottom:0}
  .coral{color:var(--coral-d);text-decoration:none;font-weight:600}
  .muted{color:var(--muted);font-size:12px}
  .note{color:var(--muted);font-size:11px}
  .catrow{display:flex;align-items:center;gap:10px;margin:6px 0}
  .catname{width:90px;font-size:13px}
  .catbar{flex:1;height:14px;background:var(--cream2);border-radius:8px;overflow:hidden}
  .catbar>span{display:block;height:100%;border-radius:8px}
  .bar-soe{background:var(--purple-deep)} .bar-net{background:var(--coral)}
  .catnum{width:30px;text-align:right;font-weight:700}
  table{width:100%;border-collapse:collapse;font-size:13px}
  th,td{text-align:left;padding:10px 8px;border-bottom:1px solid var(--line);vertical-align:top}
  th{color:var(--purple-deep);font-weight:700;background:var(--cream2)}
  td.org{font-weight:700;white-space:nowrap}
  .badge{display:inline-block;padding:2px 8px;border-radius:20px;font-size:11px;font-weight:700}
  .badge-soe{background:#EDE4FA;color:#6E52A6} .badge-net{background:#FFE6E0;color:#E85C47}
  .st-open{color:#3a9d6b} .st-urgent{color:var(--coral-d);font-weight:700} .st-closed{color:#9a93a3}
  .footer{color:var(--muted);font-size:12px;text-align:center;margin-top:30px}
  @media(max-width:720px){.cards{grid-template-columns:repeat(2,1fr)}
    table{font-size:12px}.catname{width:64px}}
</style>
</head>
<body>
<div class="wrap">
  <h1>2027 届秋招 · 可视化看板</h1>
  <div class="sub">数据更新：${esc(data.meta.updatedAt)} ｜ 范围：${esc(data.meta.scope)} ｜ 仅 2027 届 · 已排除社招</div>

  <div class="cards">
    <div class="card"><div class="n">${st.total}</div><div class="l">招聘总数</div></div>
    <div class="card soe"><div class="n">${st.open}</div><div class="l">报名中（未截止）</div></div>
    <div class="card coral"><div class="n">${st.urgent}</div><div class="l">14 天内截止</div></div>
    <div class="card purple"><div class="n">${st.closed}</div><div class="l">已截止</div></div>
  </div>

  <div class="sec">
    <h2>即将截止提醒</h2>
    <ul class="remind">${urgentList}</ul>
  </div>

  <div class="sec">
    <h2>已截止（需确认是否补录）</h2>
    <ul class="remind">${closedList}</ul>
  </div>

  <div class="sec">
    <h2>类别分布</h2>
    ${catBars}
  </div>

  <div class="sec">
    <h2>按截止时间排序的全部岗位</h2>
    <div style="overflow-x:auto">
    <table>
      <thead><tr><th>单位</th><th>岗位 / 项目</th><th>类别</th><th>批次</th><th>截止</th><th>状态</th><th>来源 / 发布</th><th>公告</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>
    </div>
  </div>

  <div class="footer">本看板由 generate.js 自动生成 · 数据文件 recruit-data.json 与脚本同目录 · 定时任务每日 8:00 刷新</div>
</div>
</body>
</html>`;
}

function main() {
  const data = loadData();
  fs.writeFileSync(SEED_PATH, buildSeed(data), 'utf8');
  fs.writeFileSync(DASH_PATH, buildDashboard(data), 'utf8');
  const st = statsOf(data, new Date());
  console.log('[OK] recruit-seed.js + dashboard.html 已生成');
  console.log(`[统计] 总数=${st.total} 报名中=${st.open} 14天内截止=${st.urgent} 已截止=${st.closed}`);
}

main();
