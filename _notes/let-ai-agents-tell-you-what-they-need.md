---
title: '讓 AI Agent 告訴你它需要什麼：需求驅動式情境方法論'
date: 2026-05-06
image: /images/AI筆記/let-ai-agents-tell-you-what-they-need.jpeg
category: AI筆記
tags: [機構知識, 需求驅動式情境, 部落知識, Context Gap Scanner, 知識版本控制]
description: '企業 AI 的最大瓶頸不在模型能力，而在機構知識（Institutional Knowledge）的缺失與混亂。IKEA 數位部門 Staff Engineer 提出「需求驅動式情境」方法論'
quote: '你不需要先整理知識庫，再讓 Agent 上工；你需要讓 Agent 上工，才能知道知識庫少了什麼。'
action: 'F-D-C 法則：Fail First 讓 Agent 面對真實任務先失敗、Discover Gaps 收集缺口清單、Curate & Commit 補充後 commit 到 GitHub，重複迭代。'
source_has_timestamps: true
---
## [核心摘要]

企業 AI 的最大瓶頸不在模型能力，而在**機構知識（Institutional Knowledge）**的缺失與混亂。IKEA 數位部門的 Staff Engineer Raj Navakoti 提出「**需求驅動式情境（Demand-Driven Context）**」方法論：不再由人工整理知識庫塞給 AI，而是讓 Agent 面對真實任務、在失敗中主動暴露知識缺口，由此漸進式地構建高品質、可信任的知識區塊（Context Blocks）。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [詳細重點整理]

### 1. 企業 AI 的真實困境 [02:47]

用電影《記憶拼圖（Memento）》類比：AI 推理能力極強，但沒有機構的「脈絡記憶」，每次都得從零開始。McKinsey 數據顯示，88% 的企業使用 AI，但只創造了 6% 的價值。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：機構知識鴻溝（Institutional Knowledge Gap）**

### 2. 知識的三色分類 [05:33]

企業 Jira 任務可分三類：

- 🟢 **綠色（通用知識）**：LLM 已知，可直接執行
- 🟠 **橙色（可教知識）**：需要提示 / 指引，可通過 Prompt 或技能擴充
- 🔴 **紅色（部落知識 Tribal Knowledge）**：只存在於員工腦中，從未被記錄，這是 AI 卡關的核心所在 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：部落知識（Tribal Knowledge）**

### 3. 現有 RAG/MCP 方案的盲點 [10:11]

企業建了 10–20 個 MCP Server，塞入 Confluence / SharePoint，但企業知識庫的現實是：20% 過時、20% 不可靠、10% 重複、**40% 從未被記錄**。塞入「爛知識」只換來不確定性輸出，準確率頂多 30%，工程師反而要幫 AI 填空，做更多人工作業。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：知識巨石（Knowledge Monolith）**

### 4. 需求驅動式情境的核心邏輯 [11:24]

類比新人入職：不是先讓他「讀完所有文件再上班」，而是直接給任務，在他提問的過程中自然暴露知識缺口，再補充並記錄下來。

這套方法的一個循環為：

1. 給 Agent 真實問題（故障 / 事件）
2. Agent 嘗試解決，失敗並產出「缺口清單」
3. 領域專家填補缺口
4. Agent 成功並**自動整理、記錄新知識**
5. 重複，信心分數逐步從 1.5 提升到 4.4 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：失敗驅動學習（Failure-Driven Discovery）**

### 5. 自動化規模化：Context Gap Scanner [26:27]

手動跑 15 次循環極痛苦，因此可以自動化：取出過去 20 個 Jira 事件 / 客服工單，批次對照知識庫進行探針測試（Probe），輸出：

- 哪些文件「乾淨、可信賴」
- 哪些「陳舊或不完整（Stale）」
- 哪些「完全未記錄（Missing）」
- 自動生成優先修復的看板（Kanban Board） [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：情境缺口掃描（Context Gap Scanning）**

### 6. 儲存策略：為何選 GitHub [33:01]

知識應以 Markdown 文件存放於 GitHub Repository，原因是多 Agent / 多團隊協作時，GitHub 的 PR、Review 流程天然具備**衝突解決機制**，且可隨時 Publish 到 Confluence / Slack。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：知識版本控制（Knowledge Version Control）**

### 7. Meta Model：知識地圖 [36:27]

讓 Agent 理解「業務流程 → 系統 → API → 技術術語」的層次關聯圖，避免它在一堆文件中盲目搜尋。Meta Model 本身即是知識庫的「導航地圖」，能讓 Agent 預判「修改這個系統會影響哪些業務流程」。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：領域 Meta Model（Domain Meta Model）**

***

## [技術/數據對比]

| 指標 | 傳統 Push 方式（RAG/MCP）| 需求驅動式 Pull 方式 |
|---|---|---|
| 知識準備方式 | 人工整理後塞入 | Agent 失敗時主動拉取 |
| 知識準確率 | ~30%（Raj 實測）| 隨循環迭代提升至 ~4.4/5 |
| 未記錄知識 | 無法發現（不知道自己不知道）| 每次循環自動浮現缺口 |
| 擴展方式 | 不斷堆 MCP Server | 自動化批次掃描 + Kanban 修補 |
| 儲存位置 | Confluence / SharePoint（雜亂）| GitHub Repo（版本控制） |

 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [結論與行動建議]

**啟發金句：** 「你不需要先整理知識庫，再讓 Agent 上工；你需要讓 Agent 上工，才能知道知識庫少了什麼。」 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**具體行動建議（F-D-C 法則）：**
- **F**ail First：給 Agent 一個真實任務讓它失敗
- **D**iscover Gaps：收集缺口清單
- **C**urate & Commit：補充後 Commit 到 GitHub，重複迭代 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**生活實踐建議：**
- 立刻取出一張最近的 Jira 事件或 Incident，用現有的 Claude / Copilot + 此 Prompt 框架，做一次「失敗測試」，觀察 Agent 提問了哪些你從未寫下的事情
- 若已有 MCP Server，不需重建，直接在現有架構上加一層「缺口偵測 + 知識整理 Agent」即可
- 以 GitHub Repo 為知識庫的單一真相來源（Single Source of Truth），搭配 Meta Model 描述你的服務架構關聯

***

## [參考連結]

- 原始影片：[https://youtu.be/_QAVExf_1uw](https://youtu.be/_QAVExf_1uw) [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
- 講者 LinkedIn：[https://www.linkedin.com/in/raj-navakoti-529880b1/](https://www.linkedin.com/in/raj-navakoti-529880b1/) [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
- 論文預印本（arXiv）：搜尋 "Demand-Driven Context" 可找到 2025 年 3 月的 preprint [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
