---
title: '非技術型 PM 的 Claude Code 完整建構指南'
date: 2026-05-19
image: /images/AI筆記/claude-code-setup-for-nontechnical-pms.jpeg
category: AI筆記
tags: [Claude Code, 產品經理, 多Agent架構, Builder PM, Lovable]
description: '本集揭示了一個非技術型 PM 被困於 Jira/PowerPoint 官僚角色的根本痛點，並提出一套可操作的 4 階層 Builder PM 框架——從 Lovable 到 Claude Code、再到 Cursor + Vercel'
quote: '你的工作不是管理 backlog，而是推動改變整個 Squad 看待自己角色的方式。'
action: '用 Lovable 建一個給自己用的個人工具，再把 Claude Code Desktop App 的 GitHub Connector 連接到那個 Repo'
source_has_timestamps: true
---
# 非技術型 PM 的 Claude Code 完整建構指南

**[核心摘要]**

本集揭示了一個非技術型 PM 被困於 Jira/PowerPoint 官僚角色的根本痛點，並提出一套可操作的**4 階層 Builder PM 框架**——從 Lovable 到 Claude Code、再到 Cursor + Vercel，最終進化為多 Agent 自動化架構。核心貢獻在於揭露一個「無人記錄的 Lovable + Claude Code 橋接工法」，讓非技術 PM 能在不懂部署的情況下獨立出貨產品。

***

## 詳細重點整理

### 1. 非技術 PM 的核心困境 [02:27]

多數非技術 PM 本質上是**美化的交付經理（Glorified Delivery Manager）**，卡在 Jira、Linear 和 PowerPoint 之間，完全依賴工程師出貨。AI 原生組織已改變這個現實——Shopify CEO 的 GitHub 貢獻紀錄全是綠色，小型超強團隊人人都在推送 feature 到 Production。

**關鍵概念：Product Owner 文化陷阱**

***

### 2. 第一層：從 Lovable 開始 [05:28]

從個人專案開始（家族度假屋預約系統、個人工具等），不從公司專案切入，降低犯錯風險。Lovable 的核心優勢是**把資料庫、驗證、部署等基礎建設全部打包**，讓非技術者不需要知道這些概念也能上手。

**關鍵概念：低風險沙盒學習（Zero-Risk Sandbox）**

***

### 3. 第二層：Lovable + Claude Code 橋接 [08:04 / 12:14]

這是影片最具突破性的實作演示。操作流程如下：
- 在 **Lovable** 上 bootstrap 初始產品，連接 GitHub Repo
- 將 **Claude Code Desktop App** 的 GitHub Connector 連到同一個 Repo
- 在 Claude Code 中開發功能，merge 到 GitHub
- **Lovable 自動同步更新**，作為視覺化 QA 環境
- 最終點擊 Lovable 的 **Publish 按鈕**發佈上線

這個工法讓非技術 PM 享有 Claude Code 的深度能力，同時以 Lovable 作為視覺測試與部署基礎設施，**無需理解分支管理或 CI/CD 流程**。

**關鍵概念：Lovable-as-Infrastructure（基礎設施借用法）**

***

### 4. 第三層：Cursor + Vercel 進入真實 Production [28:37 / 33:22]

當你開始需要**同時開發多個功能（多分支並行）**時，Lovable 的基礎設施角色就要交棒給 Vercel。Vercel 提供真實的 Preview URL，每個分支獨立預覽，適合更嚴謹的 QA 流程。

André 使用 **Cursor 作為 IDE**（搭配 Claude Code extension），而非直接用 Claude Code Desktop App，原因是可以直接查看與瀏覽程式碼檔案。重點是：**Cursor 免費版有 debugging agent**，當 Claude Code 卡住時，貼上錯誤訊息讓 Cursor Agent 解決，而不是從頭開始。

**關鍵概念：多分支並行開發（Parallel Branch Development）**

| 工具 | 角色 | 適用階段 |
|------|------|---------|
| Lovable | 視覺原型 + 基礎建設 | Level 1–2 |
| Claude Code | 核心開發引擎 | Level 2–4 |
| Cursor | IDE（含免費除錯 Agent）| Level 3–4 |
| Vercel | Production 部署 + 分支預覽 | Level 3–4 |

***

### 5. 第四層：CLAUDE.md + 多 Agent 架構 [41:17 / 42:50]

**CLAUDE.md** 是每次 Claude Code Session 啟動時自動載入的記憶檔案，是**整個 AI 團隊的文化設定檔**。第一條規則必須是：「對每個任務，先呼叫 PM Agent」。當你發現同一個問題修了兩次，就更新 CLAUDE.md，讓下一個 Session 繼承這個修正。

**PM Orchestrator Agent 架構如下：**
- **PM Agent**：唯一職責是決定把任務派給哪個 Agent，本身不寫程式碼
- **Researcher Agent**：負責調查與資料蒐集
- **Designer Agent**：提出設計方案
- **Architect Agent**：負責技術架構規劃
- **Implementer Agent**：實際撰寫程式碼

**關鍵概念：PM 即 Orchestrator（PM 作為工作流指揮者）**

> ⚠️ 陷阱警告：不要去 LinkedIn 複製知名 PM 的技能清單。應觀察你**真實團隊的工作方式**，把每個實際角色寫成一個 Agent。

***

### 6. AI 原生團隊的時間分配 [53:26]

AI 原生團隊將 **50% 的時間**花在改善 Agents 本身，而不是修改功能輸出。當某個功能出錯，**不要修補輸出，要找出是哪個 Agent 失敗，修正其指令，重新跑流程**——下一個 Session 繼承這個修復。

**關鍵概念：Fix the Agent, Not the Feature（修 Agent，不修 Feature）**

***

## 結論與行動建議

**啟發金句：**
> **「你的工作不是管理 backlog，而是推動改變整個 Squad 看待自己角色的方式。」**

**具體行動建議：F-G-D 法則（Fork → Git → Demo）**
1. **Fork**：請工程師把你加為低風險 Repo 的 Collaborator
2. **Git**：從 backlog 最老的一張票開始，開一個 branch 動手做
3. **Demo**：週五前推一個 branch，向團隊展示

**生活實踐建議：**
- **今天**：用 Lovable 建一個給自己用的個人工具（待辦清單、家族行事曆、習慣追蹤）
- **本週**：把 Claude Code Desktop App 的 GitHub Connector 連接到那個 Repo
- **本月**：觀察你的真實團隊工作方式，把 3 個核心角色寫成 CLAUDE.md 的 Agent Skill

***

## 參考連結

- 原始影片：[https://youtu.be/bYiXxeinhbg](https://youtu.be/bYiXxeinhbg) 
- 完整文字整理：https://www.news.aakashg.com/p/claude-code-non-technical-pms 
- André Albuquerque 的 Builders Camp：https://builderscamp.com
