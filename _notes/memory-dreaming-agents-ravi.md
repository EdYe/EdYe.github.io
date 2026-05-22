---
title: 'Memory 與 Dreaming：Anthropic Ravi 解說 Agent 自學習架構'
date: 2026-05-22
image: /images/影片筆記/memory-dreaming-agents-ravi.jpeg
category: 影片筆記
tags: [Agent記憶, Dreaming, 記憶全局優化, 企業級控制, 跨Session協調]
description: 'Anthropic 正式推出 Memory（記憶）與 Dreaming（夢境）兩大功能，為 Claude Managed Agents 建立自學習能力。Memory 讓 Agent 跨任務、跨 Session 保留學習成果；Dreaming 則是一個離線的非同步流程，自動分析多個 Agent 的歷史 Session，找出錯誤模式與低效行為，並全域優化記憶內容。'
quote: '共享且持續進化的記憶，為每個 Agent 墊高了起點；Dreaming 則讓這個起點繼續往上推。'
action: '為 Agent 建立分層記憶結構（組織級唯讀 + 任務級讀寫），並設定定期或 Session 結束觸發的 Dreaming 流程。'
source_has_timestamps: true
---
# 🧠 Memory and Dreaming for Self-Learning Agents

**主講人：Ravi（Anthropic Platform 團隊 API Knowledge Lead）**

***

## [核心摘要]

Anthropic 正式推出 **Memory**（記憶）與 **Dreaming**（夢境）兩大功能，為 Claude Managed Agents 建立自學習能力。Memory 讓 Agent 跨任務、跨 Session 保留學習成果；Dreaming 則是一個離線的非同步流程，自動分析多個 Agent 的歷史 Session，找出錯誤模式與低效行為，並全域優化記憶內容。兩者共同解決了「每次任務從零開始」的根本痛點，讓 Agent 群體像組織一樣持續進化。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

## [詳細重點整理]

### 1. Agent 能力進化時間軸 [00:69]

- 2024 年：發布 **MCP（Model Context Protocol）**，讓模型以規範化方式存取外部工具與資料
- 2025 年：發布 **Claude Code + Agent SDK**，大幅降低 Agent 建置門檻
- 2025 年底：發布 **Skills**，提供通用抽象讓模型擴充新能力
- 2026 年初：發布 **Cloud Managed Agents**，可靠地運行 Agent 的平台
- 現在（2026）：Memory + Dreaming 正式開放

**關鍵概念：任務時程加速定律**
Meter 研究指出，Agent 能完成的任務長度每 **7 個月翻倍**，但長時程的上下文管理仍是未解問題——記憶系統就是答案。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

### 2. Memory 的核心設計理念 [00:172]

Memory 的目標是讓 Agent 從一個任務到下一個任務持續進化，而不是每次重新出發。三大設計原則：

- **以檔案系統為模型**：讓 Claude 使用它已精通的 bash、grep 等工具來讀寫記憶，不另造輪子
- **多層級記憶範疇**：組織級唯讀記憶（SLO政策/Runbook）+ Agent 級讀寫記憶，形成層次結構
- **樂觀並行控制（Optimistic Concurrency Control）**：防止多個 Agent 同時寫入時互相覆蓋

**關鍵概念：記憶即檔案系統（Memory as File System）**
Opus 4.7 已是業界最強的「檔案系統記憶模型」，能自主判斷哪些資訊值得保存給未來的自己。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

### 3. 企業級控制能力 [00:512]

Memory 具備完整的生產環境支援能力：

- **版本控制與審計追蹤**：可 diff 不同版本，追蹤是哪個 Agent 寫入了哪筆記憶
- **獨立 API**：可從任意環境管理記憶，支援 CRUD、匯出、資料刪除（redaction）
- **唯讀/讀寫雙範疇**：組織級記憶為唯讀，任務級記憶可讀寫

**關鍵概念：記憶主權（Memory Sovereignty）**
企業可完全控制記憶的演進軌跡與存取權限，而非交由黑盒管理。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

### 4. 為何需要 Dreaming？[00:594]

當 Memory 單純由 Agent 在工作中「即時更新」時，出現了三大問題：

| 問題 | 描述 |
|------|------|
| **重複學習** | 各 Agent 在不同 Session 中各自從相同錯誤學起 |
| **記憶碎片化** | 多個 Agent 寫入導致記憶重複或結構混亂 |
| **局部最優** | 記憶被更新為對當下 Session 最有利，而非全局最優 |

**關鍵概念：記憶全局優化（Global Memory Optimization）**
Agent「邊做邊記」是局部最優，Dreaming 提供了一個從上帝視角重新整理的機制。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

### 5. Dreaming 的運作機制 [00:670]

Dreaming 是一個**完全解耦的背景流程**，具有以下特性：

- **觸發方式**：可排程（每小時/每晚）、事件驅動（Session 結束時）、或手動 ad hoc 觸發
- **分析對象**：跨 Session、跨 Agent 的歷史逐字稿（transcripts）
- **輸出**：一份「經過驗證、更有組織、更高品質」的記憶快照，Agent 可選擇是否採用
- **架構**：Dreaming 本身就是建立在 Cloud Managed Agents 上——用 Agent 來優化 Agent 的記憶

**關鍵概念：非同步反饋迴路（Async Feedback Loop）**
Dreaming 與 Agent 主要任務完全分離，既不增加延遲，也不讓 Agent 在「完成任務」vs「優化記憶」之間做取捨。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

### 6. 實際成效數據 [00:278]

| 客戶 | 使用場景 | 成果 |
|------|---------|------|
| **Racketing** | 生產環境 Agent 部署 | 首次錯誤率降低 **97%** |
| **Wise Docs** | 文件驗證流程 | 跨 Session 記憶減少常見問題 |
| **Harvey（法律 AI）** | 法律基準測試 | Dreaming 使完成率提升 **6 倍** |

 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

### 7. Demo 展示：SRE On-Call Agent 系統 [00:944]

以 SRE（Site Reliability Engineering）的 On-Call 場景為例：

- Agent 接收系統警報 → 自動分析與修復
- 共用唯讀記憶存有 SLO 政策、Runbook、On-Call 名單
- 當某 Agent 發現問題並開始修復，寫入記憶「修復中」狀態
- 後續 Agent 讀取記憶後，知道已有修復進行中，避免重複處理
- Dreaming 分析後發現：CPU 飆升 60 秒後觸發警報為跨 Session 重複模式，自動記錄 retry 行為優化建議

**關鍵概念：跨 Session 協調記憶（Cross-Session Coordination Memory）**
記憶讓 Agent 群體不再是「各自為政的孤島」，而是像有共同記憶的團隊。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

## [結論與行動建議]

### 🔥 啟發金句
> **「共享且持續進化的記憶，為每個 Agent 墊高了起點；Dreaming 則讓這個起點繼續往上推。」**

### 具體行動建議：**M-D-S 法則**
- **M（Memory）**：為你的 Agent 建立分層記憶結構（組織級唯讀 + 任務級讀寫）
- **D（Dreaming）**：設定定期或 Session 結束觸發的 Dreaming 流程，讓記憶全局優化
- **S（Scope）**：明確定義哪些記憶是跨 Agent 共享的，哪些是任務私有的

### 生活實踐建議
作為 **AI 應用架構師**，這個架構直接對應你在設計多 Agent 系統時的痛點：
1. **設計 Agent 的「組織記憶層」**：將公司的 SOP、常見問題、最佳實踐寫入唯讀 Memory Store，讓所有 Agent 共享
2. **引入 Dreaming 作為品質守門員**：在 Agent 系統上線後，設定每日 Dreaming，自動識別跨客戶、跨任務的錯誤模式
3. **利用版本控制做記憶審計**：在產品 Review 時，可以 diff 記憶版本來了解 Agent 「學到了什麼」

***

## [參考連結]

- 📺 原始影片：https://youtu.be/IGo225tfF2I?si=jmIWt-_YXUoKQ09V
- 主講人：Ravi，Anthropic Platform API Knowledge Team Lead [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)
