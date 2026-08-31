# 秋招信息工作台 · Autumn Campus-Recruit Workbench

一个**单文件、双击即用**的 2027 届秋季校园招聘信息管理工具。纯前端（HTML + 原生 JS + localStorage），无需后端、无需联网即可使用；配套 Node 脚本可定时刷新招聘情报并生成可视化看板。

> 面向人群：2027 届毕业生（毕业时间约 2026.9–2027.8）。默认数据仅收录**校园招聘**，严格排除社会招聘。

---

## ✨ 功能

- **信息池看板**：分类筛选（央国企 / 互联网大厂），一键录入到岗位管理。
- **岗位管理**：未投递 → 已投递 → 笔试中 → 面试中 → offer → 已拒绝，全链路追踪；支持手动补充。
- **可视化看板**（`dashboard.html`）：统计卡片（总数 / 报名中 / 14 天内截止 / 已截止）、即将截止提醒区、按截止时间排序列表、类别分布。
- **简历定制**：按方向管理多版简历，粘贴岗位 JD 自动生成修改要点。
- **面试进度**：统一记录每场面试的问题与复盘。
- **面试准备**：模拟电话面试排练指令、12 道高频题、优势 / 劣势分析、准备清单。
- **数据持久化**：全部个人数据存于浏览器 `localStorage`；招聘情报存于 `recruit-data.json` + `recruit-seed.js`。

## 🚀 快速开始

1. 直接双击 `秋招工作台.html` 即可使用（推荐 Chrome / Edge）。
2. 招聘情报来自 `recruit-data.json`；点工作台内「信息池看板 → 刷新数据」可重新加载。
3. 想看独立看板：双击 `dashboard.html`，或在工作台左侧「独立看板」打开。

## 🔄 数据更新（可选）

仓库自带一份真实 2027 届校招数据。**每日自动刷新**由本地定时任务（见下文）或你自己的 CI 完成：

```bash
node generate.js      # 读取 recruit-data.json → 生成 recruit-seed.js 与 dashboard.html
```

`generate.js` 输出：
- `recruit-seed.js`：工作台加载的信息池数据（classic script，支持 `file://` 直接打开）。
- `dashboard.html`：独立可视化看板。

### 定时任务示例（Windows 任务计划 / macOS launchd / cron）

每天 08:00 联网搜集 → 更新 `recruit-data.json` → 运行 `generate.js` → 推送日报。
（本项目作者用 WorkBuddy 自动化实现；你也可用任意调度器调用上面的 `node generate.js`。）

## 📁 目录结构

```
秋招工作台/
├── 秋招工作台.html      # 主工作台（单文件，双击打开）
├── dashboard.html       # 独立可视化看板（由 generate.js 生成）
├── recruit-data.json    # 招聘情报数据源（2027 届校招）
├── recruit-seed.js      # 工作台加载的信息池（由 generate.js 生成）
├── generate.js          # Node 生成脚本
└── README.md
```

## 🔒 隐私说明

本仓库已**脱敏**：`DEFAULT_PROFILE` 中的电话 / 邮箱 / 微信 / 作品集均为占位符（`（你的xxx）`），能力与经历保留。你本地使用时在「面试准备」模块填入自己的真实信息即可，数据只存在你自己的浏览器里。

## 📄 License

MIT —— 随意 fork、改、分发，注明出处即可。
