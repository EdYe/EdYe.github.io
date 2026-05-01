---
title: 'Agent vs Workflow：架構定義與選擇準則'
date: 2026-05-01
image: /images/影片筆記/agents-vs-workflows.jpeg
category: 影片筆記
tags: [Agent, Workflow, 工具呼叫迴圈, 平行化, 架構設計]
description: '多數開發者（包括 OpenAI）混用「Agent」與「Workflow」兩個概念。Anthropic 給出明確區分：Agent 是 LLM 自行決定何時停止的迴圈；Workflow 是預先定義程式碼路徑的有向流程。'
quote: 'An agent is a loop where the LLM decides when to stop — everything else is a workflow.'
action: '設計 AI 系統前先問：通往解答的路徑是否已知？已知→Workflow 並積極優化；未知→Agent 並加 max_steps 保護。'
source_has_timestamps: true
---
## 核心摘要

多數開發者（包括 OpenAI）混用「Agent」與「Workflow」兩個概念。Anthropic 在 *Building Effective Agents* 一文中給出明確區分：Agent 是一個由 **LLM 自行決定何時停止**的迴圈；Workflow 是事先寫死程式碼路徑的有向流程。這個區分不只是語意問題，而是決定系統架構、可優化性與可靠性的關鍵設計判斷。

---

## 詳細重點整理

### 1. OpenAI Agent Kit 的命名誤用 [00:00]

內容：OpenAI 發布 Agent Kit，宣稱讓開發者「可視化設計 Agent 工作流」。但其展示的範例實為：確定性步驟 → 越獄防護過濾器 → 路由 LLM 呼叫 → 三個分支路徑。這是一個預先定義好所有程式碼路徑的有向圖，並非 Agent。

**關鍵概念**：**命名膨脹（Agent Inflation）** — 行銷導向的術語濫用掩蓋了架構本質

### 2. Anthropic 的權威定義：Agent = 迴圈 [01:05]

內容：Anthropic 在 2024 年 12 月發布的 *Building Effective Agents* 正式確立定義。Agent 的本質是 **多次 LLM 呼叫組成的迴圈**，每次呼叫都能透過工具取得新資訊；何時停止由 LLM 自行發出 stop token 決定。Workflow 則是有向流程，所有程式碼路徑皆預先已知。

**關鍵概念**：**Anthropic Building Effective Agents**

### 3. Agent 的工具呼叫機制 [01:55]

內容：Agent 的迴圈依賴工具呼叫（Tool Calling）運作：LLM 發出「執行這段程式碼並回傳結果」的指令 → 系統執行工具 → 將結果送回 LLM → 下一輪決策。以 `write_file` 工具為例：使用者請求 → 助理回傳工具呼叫 → 本機執行 → 結果回傳 → LLM 繼續或停止。這個迴圈驅動 Claude Code、Cursor 等 Coding Agent。

**關鍵概念**：**Tool Calling Loop（工具呼叫迴圈）**

### 4. Workflow 的可優化性優勢 [03:00]

內容：Workflow 因路徑已知，可進行多種優化：**平行化**（同時發出多個 LLM 呼叫）、分段摘要（將長文切分後各自摘要再合摘要）等。路徑已知 = 可事先排程 = 可壓縮延遲。若只能在荒島帶走一個，作者會選 Workflow。

**關鍵概念**：**平行化 Workflow（Parallelizable Workflow）**

### 5. 選擇準則：路徑是否已知 [04:10]

內容：Agent 適用於「路徑不清楚」或「需要泛化至各種任務」的場景，例如 Coding Agent 面對未知程式碼庫與未知 Bug。Workflow 適用於「同樣的事要執行上千次」的場景，可充分優化。Agent = 爵士即興演奏；Workflow = 古典樂的精心排練。

**關鍵概念**：**泛化 vs 優化的取捨**

### 6. Agent–Workflow 連續光譜 [05:30]

內容：現實系統通常落在光譜中間，而非純粹一端。常見混合模式：(1) Agent + max_steps 限制（防止無限迴圈，ADK 內建此參數）；(2) Agent 內部呼叫 Workflow 工具（兼顧泛化與優化）；(3) Workflow 內含評估迴圈（反覆精煉文字）。判斷方向：**LLM 是否有能力提前中斷迴圈** → 是則偏 Agent。

**關鍵概念**：**max_steps、Agent-within-Workflow、Loop-within-Workflow**

---

## 技術 / 數據對比

| 維度 | Agent | Workflow |
|------|-------|----------|
| 停止控制者 | LLM 自行決定 | 預先寫定的程式碼 |
| 路徑是否已知 | 未知，動態決定 | 已知，固定程式碼路徑 |
| 優化空間 | 有限（交給 LLM） | 高（可平行化、排程） |
| 適用場景 | 未知任務、需泛化 | 重複任務、需穩定 |
| 典型範例 | Claude Code、Cursor | 文件摘要流水線、評估系統 |
| 比喻 | 爵士即興 | 古典樂演奏 |

---

## 結論與行動建議

**啟發金句**：「An agent is a loop where the LLM decides when to stop — everything else is a workflow.」

**具體行動建議**：設計 AI 系統前先問一個問題：「通往解答的路徑，是我事先知道的嗎？」已知 → 用 Workflow 並積極優化；未知 → 才考慮 Agent，並記得加 max_steps 保護。

**生活實踐建議**：
1. 下次看到任何工具把「可視化流程圖」稱為 Agent，直接問：「LLM 可以自行決定何時停嗎？」沒有的話，那就是 Workflow。
2. 若你正在建構 Coding Agent，優先考慮讓 Agent 呼叫 Workflow 工具（而非全部交給 Agent 即興發揮），可大幅提升效能與可控性。
3. 在團隊溝通中，用 Anthropic 定義統一術語：Agent = 迴圈 + LLM 控制停止；Workflow = 有向圖 + 程式碼控制。

---

## 參考連結

- [Most devs don't understand what agents are](https://youtu.be/AtYtuVTZCQU?si=wlO6v--q-8deY5bX)
- [Building Effective Agents - Anthropic](https://www.anthropic.com/research/building-effective-agents)
