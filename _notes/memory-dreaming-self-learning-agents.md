---
title: 'Memory 與 Dreaming：Anthropic 讓 Agent 持續自我學習的新原語'
date: 2026-05-09
image: /images/影片筆記/memory-dreaming-self-learning-agents.jpeg
category: 影片筆記
tags: [Agent記憶, Dreaming, 記憶蒸餾, 連續自我學習, Anthropic]
description: '記憶體（Memory）與夢境（Dreaming）是 Anthropic 為 Claude Managed Agents 推出的兩項新原語，解決了 AI Agent 在長時間運行中「無法跨 session 持續學習」的核心痛點。'
quote: '奪走工作的不是 AI，而是那個讓 AI 每天都比昨天更聰明的人。'
action: '為 Agent 建立分層記憶庫（唯讀知識庫＋讀寫工作記憶），並在任務完成後定時觸發 Dreaming 自動優化記憶品質。'
source_has_timestamps: true
---
# 🧠 Memory and Dreaming for Self-Learning Agents

**影片來源：** Anthropic 工程師 Mahes（平台團隊 PM）於 2026 年 5 月 8 日發表的 24 分鐘技術演講。

***

## [核心摘要]

**記憶體（Memory）與夢境（Dreaming）** 是 Anthropic 為 Claude Managed Agents 推出的兩項新原語（Primitive），解決了 AI Agent 在長時間運行中「無法跨 session 持續學習」的核心痛點。Memory 讓 Agent 在任務執行中即時讀寫知識；Dreaming 則在 Agent 空閒時批次分析跨 session 的錯誤模式與學習成果，自動更新並優化記憶狀態，實現真正的「自我演化 Agent」。

***

## [詳細重點整理]

### 1. Agent 演化路線圖 [00:07]

Anthropic 的 Agent 能力原語演進順序如下：

- **MCP**（工具與外部資料存取）
- **Claude Code / Agent SDK**（強大的執行環境）
- **Skills**（2025年10月）：讓 Agent 學習新技能並分享給其他 Agent
- **Memory**（2026年初 Public Beta）：下一個核心原語

**關鍵概念：** **連續自我學習（Continuous Self-Learning）** — Agent 能根據自身執行經驗持續演化，而非每次 session 重新開始。

***

### 2. Memory 系統設計原則 [04:22]

Memory 在 Claude Managed Agents 中被建模為**檔案系統（File System）**，Agent 可使用熟悉的 bash 和 GP 工具自主管理與更新記憶。 三大設計要求：

- **最大化智能（Maximize Intelligence by Default）**：委託 Claude 自主決定記憶內容與結構
- **多 Agent 擴展性（Multi-Agent Scale）**：支援數百至數千個 Agent 並行共享記憶
- **企業級控制（Developer/Enterprise Control）**：版本歷史、歸屬元數據、獨立 API

**關鍵概念：** **樂觀並發（Optimistic Concurrency）** — 使用 Content Hash 確保多個 Agent 同時寫入記憶時不會互相覆蓋。

***

### 3. Memory 架構的三個層次 [09:39]

| 層次 | 說明 | 實例 |
|------|------|------|
| **儲存層（Storage Layer）** | 資料存放位置與元數據 | 版本歷史、歸屬紀錄、Content Hash |
| **結構與內容層（Structure/Content Layer）** | 記憶的格式與組織方式 | 檔案系統、Skills（程序性記憶）|
| **流程層（Process Layer）** | 何時更新、如何觸發 | Dreaming（批次異步學習）|



***

### 4. Dreaming — 全新研究預覽功能 [11:24]

**Dreaming** 是一個**帶外（Out-of-Band）批次異步流程**，在 Agent 完成任務後（或定期排程），掃描近期所有 session 的逐字稿，自動發現跨 Agent 的共同錯誤模式與成功策略，並產生優化後的記憶狀態差異（Diff）。

運作流程：
1. 定期或任務完成後觸發（支援 cron 排程或 API 呼叫）
2. 掃描近期多個 session 的 transcript
3. 發現共同模式、重複條目、過時記憶
4. 產生記憶 Diff（去重、驗證、補全、刪除過期資訊）
5. 可立即套用或透過 API 人工審核後再部署

**關鍵概念：** **記憶蒸餾（Memory Distillation）** — 類似 Test-Time Compute 的擴展思路，用額外計算換取更高品質、更精煉的知識索引，讓下游所有 Agent 共享這份計算成本。

***

### 5. 權限範圍與企業控制 [08:12]

Memory 支援多層次的**權限範圍（Permission Scopes）**：

- **唯讀（Read-Only）記憶庫**：例如全組織通用 SOP、SLO 規範（不允許 Agent 隨意修改）
- **讀寫（Read-Write）記憶庫**：Agent 工作記憶，隨任務進展即時更新
- **版本歷史（Version History）**：完整審計紀錄，包含「哪個 Agent、哪個 session、何時」做了哪些修改

***

## [技術/數據對比]

| 客戶 | 使用場景 | 效果 |
|------|---------|------|
| **Rockutin** | 內部知識 Agent | 首次執行錯誤率降低 **90%**，同時降低 token 耗用與延遲  |
| **Harvey**（法律科技） | 法律情境基準測試 | 任務完成率提升 **6 倍**  |

***

## [結論與行動建議]

**啟發金句：**
> **「奪走工作的不是 AI，而是那個讓 AI 每天都比昨天更聰明的人。」**
> — Memory + Dreaming 的本質：讓 Agent 的昨日經驗，成為今日的競爭優勢。

**具體行動建議（M-D-C 法則）：**
- **M（Memory）**：為你的 Agent 建立分層記憶庫（唯讀知識庫 + 讀寫工作記憶）
- **D（Dreaming）**：在任務完成後或每日定時觸發 Dreaming，讓系統自動優化記憶品質
- **C（Control）**：善用版本歷史與 Diff 審核，確保記憶更新的可追溯性與安全性

**生活實踐建議：**
若你正在開發 AI 應用或 Agent 系統，立即評估以下三個切入點：
1. 你的 Agent 是否每次 session 都在重複相同錯誤？→ 導入 **Memory API**
2. 你有多個 Agent 並行運作但彼此孤立學習？→ 啟用 **Dreaming** 做跨 Agent 知識整合
3. 你需要在企業部署並符合合規需求？→ 利用 **版本歷史 + 獨立 API** 做 PII 掃描與記憶審計

***

## [參考連結]

- 原始影片：[https://youtu.be/RtywqDFBYnQ?si=e8SlhSQO2q2EDaLg](https://youtu.be/RtywqDFBYnQ?si=e8SlhSQO2q2EDaLg) 
- Anthropic Managed Agents API — Memory & Dreaming 功能（2026 年 Public Beta）
