---
title: 'Anthropic 發布 Claude Code 大型程式碼庫部署手冊'
date: 2026-05-17
image: /images/AI筆記/anthropic-claude-code-playbook.jpeg
category: AI筆記
tags: [Claude Code, Harness架構, CLAUDE.md, MCP, 大型程式碼庫]
description: 'Anthropic 發布 Claude Code 大型程式碼庫部署手冊，核心論點是模型外的生態系（Harness）比模型本身更決定實際表現。手冊提出 7 個組件與 3 大模式，建立順序：CLAUDE.md 優先，MCP 最後。'
quote: 'Harness 比 Model 更決定結果——生態系的天花板，才是 AI 能力的天花板。'
action: '立刻從根目錄建立一頁 CLAUDE.md 全局規範，並指定 DRI 負責維護，每季審查配置是否需更新。'
source_has_timestamps: true
---
## [核心摘要]

Anthropic 發布了 **Claude Code 大型程式碼庫部署手冊（Playbook）**，核心論點是：**模型外的生態系（Harness）比模型本身更決定 Claude Code 的實際表現**。手冊提出 7 個組件（5 個擴展點 + 2 個能力）與 3 大模式，並明確建立順序：**CLAUDE.md 優先，MCP 最後**，解決了大型企業在千萬行程式碼庫中部署 AI 編程工具的落地痛點。

***

## [詳細重點整理]

### 1. Harness 優先論 [0:00]

**核心概念：Harness-over-Model 論點**

模型周圍的生態系——即 Harness——才是決定 Claude Code 規模化效能的關鍵，而非模型本身。Anthropic 的 Applied AI 團隊（Griffith、Lee、Concannon 等人）明確指出此論點，適用範圍涵蓋數百萬行的 Monorepo、數十年的 Legacy 系統，以及 C、C++、C#、Java、PHP 等語言。

***

### 2. Agentic Search vs. RAG [1:29]

**核心概念：Agentic Search（主動搜尋）**

傳統 AI 編程工具依賴 RAG 嵌入索引，在活躍的大型程式碼庫中會出現「索引過時」問題——指向已更名的函式或已刪除的模組。Claude Code 改採 **Agentic Search**：無嵌入管線、無中央索引，每個實例直接從當前程式碼庫讀取，如同工程師手動翻閱一樣。

***

### 3. 7 組件 Harness 架構 [2:14]

**核心概念：分層式 Harness 架構**

7 個組件依建立順序如下：

| 層級 | 組件 | 功能說明 |
|------|------|----------|
| 1 | **CLAUDE.md** | 每次 session 自動載入的情境檔案 |
| 2 | **Hooks** | 可在 session 結束後自動提案 CLAUDE.md 更新 |
| 3 | **Skills** | 按需載入的專業知識（如安全審查技能） |
| 4 | **Plugins** | 將 Skills、Hooks、MCP 打包成可安裝模組分發 |
| 5 | **LSP 整合** | 以符號（Symbol）精確搜尋，取代字串 Grep |
| 6 | **MCP Servers** | 最後建立，開放結構化搜尋工具給 Claude 呼叫 |
| 7 | **Subagents** | 獨立執行任務後只回傳最終結果給主 Agent |



***

### 4. Pattern 1 — 讓程式碼庫可導航 [4:32]

**核心概念：Navigability（可導航性）**

Anthropic 提出 6 個子模式讓大型程式碼庫對 Claude 更友善：
- **精簡分層的 CLAUDE.md**：根目錄放全局規範，子目錄放局部慣例
- **在子目錄初始化**，而非只在 Repo 根目錄
- **限定測試/lint 指令範圍**在子目錄，避免跑全局浪費 context
- 使用 `.gitignore` + `permissions.deny`（存於 `.claude/settings.json`）統一噪音過濾
- 建立**程式碼庫地圖**（Markdown 索引檔，列出頂層目錄一行說明）
- 啟用 **LSP**，讓 Claude 以符號搜尋取代字串 Grep

***

### 5. Pattern 2 — 持續維護 CLAUDE.md [5:51]

**核心概念：配置衰退（Configuration Decay）**

為舊模型版本撰寫的指令可能對新模型產生反效果。Anthropic 建議每 **3 到 6 個月**進行一次配置審查，尤其在重大模型版本發布後效能出現停滯時。具體案例：一個攔截 Perforce 的 P4 edit Hook，在 Claude Code 原生支援 Perforce 後即變成多餘且有害的配置。

***

### 6. Pattern 3 — 建立所有權機制 [6:25]

**核心概念：Agent Manager（代理管理人）**

技術配置之外，**組織所有權**才是推動大規模採用的關鍵。Anthropic 提出三個層級：
- **DRI（Directly Responsible Individual）**：最低可行所有者，負責設定、權限與 CLAUDE.md 慣例
- **Agent Manager**：新興職位，兼具 PM 與工程師能力，專責管理 Claude Code 生態系
- **跨職能工作小組**：工程、資安、治理代表共同定義需求並制定推廣路線圖

***

## [結論與行動建議]

**🔥 啟發金句：**
> **「Harness 比 Model 更決定結果——生態系的天花板，才是 AI 能力的天花板。」**

**具體行動建議：CLAUDE-First 法則**
> **C**LAUDE.md → **H**ooks → **S**kills → **P**lugins → **L**SP → **M**CP（依此順序，禁止跳層）

**生活實踐建議：**
- 🛠️ **今日行動**：若你的專案尚未建立 CLAUDE.md，立刻從根目錄的一頁全局規範開始，記錄專案架構、命名慣例與禁止行為
- 👥 **組織行動**：在 AI 工具推廣前，先指定一位 DRI，避免「人人都在用，但沒人維護」的配置荒廢
- 🔄 **季度行動**：每季進行一次 CLAUDE.md 審查，尤其在新模型版本發布後的一個月內

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/IYBP_JT9aUo?si=QFPGKyrajo33ubWP 
- 📝 Anthropic 原文：https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
- 📚 Claude Code 文件：https://code.claude.com/docs/en/overview
