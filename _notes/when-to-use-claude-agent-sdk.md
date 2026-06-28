---
title: 'Claude Agent SDK：何時選 SDK 而非 CLI'
date: 2026-06-28
image: /images/AI筆記/when-to-use-claude-agent-sdk.jpg
category: AI筆記
tags: [Agent Harness, Claude Agent SDK, 多Agent並行, 產品化部署]
description: 'Claude Agent SDK 本質是將 Claude Code 的強大 Agent Harness 封裝成可程式化調用的 SDK，解決了「何時該用 SDK 而非直接用 CLI」的困惑。'
quote: 'LLM + Harness = Agent；而 Claude Agent SDK，就是讓你把自己做的產品，裝上 Claude Code 這顆最強大腦的那條線。'
action: '將研究驗證（CLI）→ 產品部署（SDK）作為標準流程，搭配 Gradio 快速原型化交付利害關係人展示'
source_has_timestamps: true
---
## [核心摘要]

**Claude Agent SDK** 本質是將 Claude Code 的強大 Agent Harness 封裝成可程式化調用的 SDK，解決了「何時該用 SDK 而非直接用 CLI」的困惑。核心差異在於：SDK 讓你能以 Python 程式碼**產品化**、**動態組態**、以及**並行協調多個 Agent**，而 CLI 則適合互動式使用。

***

## [詳細重點整理]

### 1. Agent Harness 是什麼？[00:00]

**Agent Harness（代理人框架）** 是 LLM 之外的所有元件總稱，包含工具（tools）、執行循環（loop）與目標管理（goal）。業界有一個公式：**LLM + Harness = AI Agent**。框架光譜從「輕量型框架」（如 OpenAI Agents SDK、Google ADK）到「全包型 Harness」（如 LangChain Deep Agents、Claude Agent SDK）皆有。

> **關鍵概念：Agent Harness** — 代理人框架，泛指工具調用、記憶管理、Context 壓縮等非 LLM 核心的基礎設施層。

***

### 2. Claude Agent SDK 的定位 [02:25]

Claude Agent SDK 本質上是**以程式碼驅動 Claude Code 引擎**的接口，核心函式只有一個：`query()`，迭代其回傳結果即可。與其他全包型框架的最大差異在於：它**僅支援 Anthropic 模型**，但內建了 Claude Code 擁有的所有能力（檔案讀寫、指令執行、網頁搜尋、程式碼編輯、Context 自動壓縮）。

> **關鍵概念：Programmatic Agent Harness** — 將互動式 CLI 工具轉為可程式化控制的 SDK 層，實現產品化部署。

***

### 3. 實作示範：四步驟建構語言家教 [03:43]

以西班牙語家教應用為例，四個遞進步驟展示 SDK 能力：

- **Step 1 [04:26]** 最簡 Agent Loop：系統 Prompt + `query()` 即可運作，且不需 API Key（登入 Claude AI 訂閱帳號即可）
- **Step 2 [05:16]** 賦予工具：指定 `data/` 資料夾，Agent 自動建立並管理學習者記憶檔案（詞彙、語法錯誤、學習歷程）
- **Step 3 [07:39]** 雙 Agent 並行：主 Agent（家教）+ 副 Agent（課程教練）同時運行，共用同一份資料夾，各自獨立決策
- **Step 4 [10:14]** 產品化：包裝成 Gradio 應用，左側對話、右側即時顯示等級進度與學習歷程，由背景 Agent 持續更新

> **關鍵概念：多 Agent 並行協調（Multi-Agent Parallelism）** — 不同於子 Agent 委派模式，此架構是透過程式碼主動排程多個獨立 Claude Code 進程，實現同步協作。

***

### 4. 核心問題解答：為何不直接用 CLI？[12:36]

SDK 相比 CLI 有三個核心優勢：

1. **產品化（Productionize）**：將在 Claude Code CLI 互動開發好的流程，直接轉化為可部署至 CI/CD pipeline 的程式
2. **打造自有產品**：想將 Claude Code 的 Harness 能力作為自家產品的 AI 引擎（如語言家教 App）
3. **動態程式組態**：當需要程式化建構複雜的 Prompt 參數（如語言種類、多 Agent 角色設定），CLI 難以維護，SDK 更靈活

***

## [技術/數據對比]

| 維度 | 輕量型框架（OpenAI SDK / Google ADK） | 全包型 Harness（Claude Agent SDK） |
|---|---|---|
| 內建工具 | ❌ 需自行實作 | ✅ 檔案讀寫、執行指令、網頁搜尋 |
| Context 壓縮 | ❌ | ✅ 自動管理 |
| 模型相容性 | ✅ 任意模型 | ⚠️ 僅限 Anthropic 模型 |
| 上手難度 | 低（彈性高） | 低（開箱即用） |
| 適合場景 | 自訂工具鏈、跨模型 | 產品化、多 Agent 協調 |



***

## [結論與行動建議]

**啟發金句：**
> **「LLM + Harness = Agent；而 Claude Agent SDK，就是讓你把自己做的產品，裝上 Claude Code 這顆最強大腦的那條線。」**

**具體行動建議（P-P-P 法則）**：
- **Productionize（產品化）**：已用 Claude Code 驗證的流程 → 用 SDK 封裝部署
- **Parallelize（並行化）**：用程式碼控制多個 Agent 同步運行，而非依賴 CLI 手動開多個終端
- **Personalize（個人化）**：動態傳入 Prompt 參數，打造有記憶、會成長的 AI 產品

**生活實踐建議：**
身為 AI 應用架構師，你可以用 Claude Agent SDK 取代手動維護的「多 Claude Code 終端工作流」，將**研究驗證（CLI）→ 產品部署（SDK）**作為標準流程，並搭配 Gradio 快速原型化交付給利害關係人展示。

***

## [參考連結]

- 原始影片：https://youtu.be/HIJVMVBM4KM
- 作者課程資源：https://edwarddonner.com/curriculum
- 影片示範 Repo：https://github.com/ed-donner/tutor
