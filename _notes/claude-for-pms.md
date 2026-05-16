---
title: 'Claude for PMs：打造自我進化的 PM 工作作業系統'
date: 2026-05-17
image: /images/AI筆記/claude-for-pms.jpeg
category: AI筆記
tags: [Claude Cowork, Skills系統, PM工作流程, 漸進式揭露, Super PM]
description: '歐洲第一 AIPM 意見領袖 Pawel Huryn 示範如何以 Claude 完整工具矩陣（Cowork、Code、Dispatch）打造自我進化的 PM 工作作業系統，解決 PM 只把 AI 當聊天工具的痛點，實現真正的工作流程代理。'
quote: '你不能只做一個訪問用戶、管理 Backlog 的 PM——這只是在用 Photoshop 裁圖而已。'
action: '把最常做的 PM 工作描述給 Claude 生成第一個 skill.md，本週連接 Gmail MCP，本月建立含 3 個 Sub-agent 角色的知識工作系統。'
source_has_timestamps: true
---
# 🎯 [核心摘要]

這部影片由歐洲第一 AIPM 意見領袖 Pawel Huryn（Product Compass 創辦人，10K GitHub Stars）現場示範如何以 Claude 的完整工具矩陣（Cowork、Code、Dispatch）打造一套**自我進化的 PM 工作作業系統**。它解決了 PM 最常見的痛點：把 AI 只當聊天工具使用，卻無法真正融入工作流程、協作程式碼庫或跨裝置執行任務。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

# [詳細重點整理]

## 1. Cowork 進階實戰示範 [00:54]

告別 Chat，直接在 Cowork 選取桌面資料夾，即可讓 Claude 讀取真實檔案（PDF 發票、圖片）、自動辨識重複檔、依月份建立子目錄並整理歸檔，同時支援 sub-agents 平行處理多任務（起草信件、轉換 PDF、查 CRM 同時進行）。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：真實工作流程代理（Real Agentic Workflow）** — Cowork 在虛擬機中執行腳本，而非模擬操作。

## 2. Anthropic 的驚人出貨速度 [03:08]

52 天內發布 74 項更新，公司從 10 億美元估值增長到 300 億，背後原因是**流程重新設計**（Process Redesign），而非單純把 AI 插入舊流程。現代公司的 PM、PMM、Designer、Engineer 角色正在融合，自動化已覆蓋原型設計、Release Notes、UI 設計。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：流程重設計（Process Redesign Around AI）** — 不是用 AI 替換步驟，而是以 AI 為核心重新設計整個流程。

## 3. 為何停止使用 Chat [06:07]

Chat 有三大限制：無法跨裝置繼續、無法存取本地程式碼庫、無法執行真實系統指令。一旦在對話中途需要切換工具，就必須重建上下文。建議從一開始就選擇 Cowork 或 Claude Code。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：上下文連續性（Context Continuity）** — 工具切換的隱性成本是重新建立整個工作脈絡。

## 4. Cowork vs Code vs Dispatch 比較 [09:56]

| 工具 | 核心能力 | 適用 PM 場景 |
|---|---|---|
| **Chat** | 問答、簡單腳本 | 快速語法確認 |
| **Cowork** | 真實檔案、MCP 連接器、Sub-agents | 每日知識工作、信件草稿、簡報製作 |
| **Claude Code** | 執行本機指令、Explorer 視圖、Hooks、自定義 Sub-agent 角色 | 協作程式碼庫、複雜系統（50+ 檔案）、hooks 自動化 |
| **Dispatch** | 手機遠端啟動 Cowork/Code 任務 | 外出時觸發多執行緒任務並行 |

 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

## 5. Skills 與 MCP 連接器 [18:44]

**Skills（技能檔案）** 是以 Markdown 撰寫的程序知識，保存在 `skill.md`。Agent 先讀取名稱與描述，只在任務匹配時才載入完整指令，稱為**漸進式揭露（Progressive Disclosure）**，讓數百個 Skills 並存卻不增加 Token 消耗。MCP 連接器（Gmail、Slack、Google Drive）則如同 Agent 的 USB 擴充埠。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：漸進式揭露（Progressive Disclosure）** — 上下文管理的核心機制，大幅降低 Token 成本。

## 6. PM Skills Marketplace [25:03]

Pawel 開源的 `phuryn/pm-skills`（現已達 10,000 GitHub Stars）包含多個 Plugin：Data Analytics、Execution、Go-to-Market、Market Research、Product Discovery。其中 `discover` 指令可一鍵完成：**客戶需求分析 → 機會地圖 → 創意發想 → 假設映射 → 實驗規劃** 的完整 Discovery 流程。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：PM 技能資產化（PM Skill Productization）** — 將個人工作方法論轉為可重用、可迭代的 Markdown 模組。

## 7. Strategy Canvas 現場示範 [29:06]

實際示範以 `product_strategy` slash command 為 Amazon 生成完整產品策略簡報，包含：市場區隔、North Star Metric、護欄指標（Guardrail Metrics）、成長策略與單位經濟，且自動匹配多樣化版面與圖示。Claude 在 PowerPoint 操作能力上已達 McKenzie 顧問水準。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：護欄指標（Guardrail Metrics）** — 當聚焦北極星指標時，用於監控其他關鍵健康指標不退化。

## 8. Skill 迭代循環 [35:14]

技能進化流程：**安裝基準技能 → 實際使用 → 給予具體反饋 → 要求 Claude 從頭重寫（Rewrite from First Principles）→ 重測 → 循環**。經過 5-6 輪迭代可消除約 99% 的錯誤，等同於 AI 系統的 Eval 循環。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：從第一原則重寫（Rewrite from First Principles）** — 非修補式更新，而是理解根本失敗原因後全面重構。

## 9. 為何 PM 必須學 Claude Code [40:46]

Cowork 缺少：Explorer 視圖（大型資料夾層級瀏覽）、自定義 Sub-agent 角色（如 Researcher、Tester、Release Notes Writer）、Hooks（觸發式自動化）。這些功能對於與工程師協作、管理 50+ 檔案系統或建構複雜 AI Pipeline 缺一不可。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：Sub-agent 角色化（Agentic Persona Architecture）** — 在 Claude Code 中預定義具特定專長的 Agent 角色，構建可擴展的自動化系統。

## 10. 建構第二大腦（Second Brain）[44:43]

`CLAUDE.md` 應只作為**路由器**，存放專案結構與指針，領域知識分散存放於獨立檔案，Agent 按需載入。避免把所有指令塞入單一大型 CLAUDE.md，否則每次對話都浪費大量 Token 處理不相關知識。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：路由式知識架構（Router-Based Knowledge Architecture）** — CLAUDE.md 是目錄索引，不是知識倉庫本身。

## 11. 自我進化知識庫 [56:00]

知識分三類管理：
- **Rules（規則）**：已驗證，每次任務預設套用
- **Hypotheses（假設）**：追蹤中，附帶佐證資料
- **Rejected Patterns（棄用模式）**：保留記錄，避免反覆測試已知失敗路徑

**三行自我進化 Prompt**：① 任務前回顧規則 ② 執行時套用確認規則 ③ 收到反饋後更新知識庫。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：自我進化知識庫（Self-Improving Knowledge Base）** — 系統每次執行後自動累積學習，形成正向飛輪。

## 12. Dispatch 與遠端工作 [1:10:00]

Dispatch 讓你從手機啟動多個獨立執行緒：生成資訊圖表、檢查郵件、分析競爭對手，各自平行執行。建議改用 **Vercel Agent Browser**（Headless 模式）替代 Chrome MCP，後者每 0.5 秒截圖一次，實測每小時燒掉 $100 Token 費用。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：非同步任務分派（Asynchronous Task Dispatching）** — 工作系統在你不在時持續運作。

## 13. PM 常見錯誤與未來 [1:21:07]

未來的 PM 是**Super PM / Super Individual Contributor**，需跨越：技術理解（Terminal、程式碼庫）、商業策略（Revenue Driver、P&L）、多領域設計。僅會訪談用戶與管理 Backlog 的 PM 角色將不再足夠。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：Super PM（超級個人貢獻者）** — 技能邊界擴展至工程、設計、商業策略的複合型角色。

***

# [結論與行動建議]

**啟發金句：**
> **「你不能只做一個訪問用戶、管理 Backlog 的 PM——這只是在用 Photoshop 裁圖而已。」**

**具體行動建議 — S-I-R 法則：**
- **S（Skill）**：從 `phuryn/pm-skills` 安裝基準技能，不必從零開始
- **I（Iterate）**：每次使用後給出具體反饋，要求 Claude 從第一原則重寫，迭代 5-6 次
- **R（Route）**：在 CLAUDE.md 中只存路由指針，知識分散獨立存放

**生活實踐建議：**
- **立即行動**：把你最常做的一項 PM 工作（如用戶訪談記錄整理、PRD 撰寫）描述給 Claude，讓它幫你生成第一個 `skill.md`
- **本週目標**：在 Cowork 中連接 Gmail MCP，讓 Claude 草擬回信，你只需審核與發送
- **本月目標**：安裝 Claude Code，建立包含 3 個 Sub-agent 角色（Researcher、Writer、Reviewer）的個人知識工作系統

***

# [參考連結]

- 🎬 原始影片：[https://youtu.be/bITUsUsrxjM](https://youtu.be/bITUsUsrxjM) [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
- 📝 完整文章：https://www.news.aakashg.com/p/ai-pms-guide-to-claude
- 🛠️ PM Skills Marketplace：https://github.com/phuryn/pm-skills
- 👤 Pawel Huryn LinkedIn：https://www.linkedin.com/in/pavelhuryn/
