---
title: 'Eval 成熟度模型：從直覺判斷到自動化 CI/CD 飛輪'
date: 2026-05-28
image: /images/AI筆記/maturity-phases-running-evals.jpeg
category: AI筆記
tags: [Eval評測, Agent品質, LLM as Judge, Eval飛輪, 工具調用]
description: '多數團隊將 Eval 當作單元測試來寫，試圖窮舉所有可能的失敗情況，但這是錯誤框架。正確做法是：鎖定已知失敗模式、精準覆蓋、快速交付'
quote: 'Eval 不是在跑測試，而是在重播生產。'
action: '先定義失敗模式（F），人工標注附理由（D），讓每個生產異常成為下一輪改善的燃料（F）'
source_has_timestamps: true
---
## [核心摘要]

多數團隊將 Eval 當作單元測試來寫，試圖窮舉所有可能的失敗情況，但這是錯誤框架。正確做法是：**鎖定已知失敗模式、精準覆蓋、快速交付**，並建立「生產追蹤 → 離線實驗 → 改善方向」的**飛輪循環**，讓 Eval 成為持續提升 Agent 品質的引擎，而非無止盡的測試負擔。

***

## [詳細重點整理]

### 1. Eval 的根本目的與核心原則 [00:14]

Eval 的存在完全服務於「**Agent 品質**」——確保 Agent 在真實使用者與真實使用情境下，能夠如預期運作。風險涵蓋三個層面：**品牌聲譽風險**（Agent 對客戶不友善）、**系統成本風險**（Agent 運行成本失控）、**合規與法律風險**（Agent 行為越界）。

**關鍵概念：失敗模式導向（Failure-Mode-Driven Evals）**

Eval 的設計邏輯與單元測試根本不同：
- ❌ 不要窮舉所有可能出錯的情況（無限，無法交付）
- ✅ 先由領域專家定義「**已知失敗模式**」，再針對這些模式建立 Eval
- Eval 結果不必是 100 分，方向性趨勢正確即可接受

***

### 2. 第一成熟度階段：Vibe Check + 文件化 [00:420]

初期從「**直覺判斷（Vibe Checking）**」出發並非錯誤，關鍵是要**同步文件化**。流程如下：
- 給 Agent 約 10 組範例輸入，觀察輸出
- 讓領域專家（Subject Matter Expert）標記 👍 / 👎
- **最重要：要求標記者寫下「為什麼」的理由（Justification）**，而非只給分

**關鍵概念：領域知識萃取（Domain Knowledge Extraction）**
這些文字化的理由是未來實現「LLM as Judge」自動化的知識來源，不能省略。

***

### 3. 第二成熟度階段：LLM as Judge 規模化 [00:588]

將人工標注的失敗理由，透過 Cursor / Cloud Code / Codex 等工具系統性整理出**失敗模式分類**，再建構 LLM 評審機制。

重要注意事項：
- **LLM Judge 本身也需要被 Eval**：「把法袍套在 LLM 身上，不代表它就是可信的法官」
- 也可用**確定性程式碼**判斷客觀失敗，例如：Tool Call 次數過多、Token 用量過高
- **資料集應納入生產環境的真實 Trace**，而非只用合成資料

**關鍵概念：Eval 飛輪（Eval Flywheel）**
生產 Trace → 人工或自動分析異常 → 帶回離線實驗環境 → 重跑 Eval → 指引改善方向 → 回到生產。

***

### 4. 第三成熟度階段：處理工具調用（Tool Calls）的複雜性 [00:774]

Agent 開始與外部系統互動時，Eval 難度大幅提升。工具調用分兩類：

| 工具類型 | 說明 | Eval 難度 |
|---|---|---|
| **Context Gathering Tools** | 唯讀，僅抓取資料注入 LLM | 相對可控 |
| **CRUD Tools** | 對外部系統進行增刪改查 | 高度複雜 ⚠️ |

CRUD 工具的兩大 Eval 難題：
1. 很難重現 Trace 當下外部系統的確切狀態
2. 無法在離線 Eval 時真正對生產系統執行操作

**解決方案（新興技術）：**
- **向量資料庫時間戳查詢（Timestamp Query）**：以 Trace 記錄時間點查詢向量庫，還原當下的資料狀態
- **系統狀態注入 Trace（State Injection）**：將外部系統當時的快照直接嵌入 Trace，讓 Agent Trace 本身承載完整上下文

***

### 5. 進階方向：Topic Modeling + 自動化 CI/CD Eval [01:007]

- **生產端 Topic Modeling**：自動化挖掘新興失敗模式，不依賴人工審視
- **Cloud Code + Eval CLI**：將 Eval 納入自動化 Pipeline，以 CI/CD 方式持續運行

**關鍵概念：Eval 即生產重播（Eval as Production Replay）**

***

## [技術/數據對比]

| 維度 | 單元測試（Unit Tests） | Agent Evals |
|---|---|---|
| **覆蓋策略** | 窮舉所有情況 | 鎖定已知失敗模式 |
| **結果要求** | 必須 100% 通過 | 方向性趨勢正確即可 |
| **評審方式** | 確定性（Deterministic） | 確定性 + LLM as Judge |
| **資料來源** | 合成/靜態測試資料 | 生產 Trace（動態） |
| **適用場景** | 功能正確性 | Agent 品質與行為對齊 |

***

## [結論與行動建議]

**啟發金句：**
> **「Eval 不是在跑測試，而是在重播生產。」**

**具體行動建議（F-D-F 法則）**：
- **F**ail Modes First：先定義失敗模式，再寫 Eval
- **D**ocument Justifications：人工標注必須附理由，不只給分
- **F**lywheel Always：每一個生產異常都是下一輪改善的燃料

**生活實踐建議（給 AI 應用架構師）：**
1. **本週開始**：為你手上的 Agent，與領域 PM 或 SME 合開一場 1 小時「失敗模式盤點會」，列出 5 個最怕發生的 Bad Case
2. **本月目標**：建立一個小型 Eval Dataset（20~50 筆生產 Trace），加入人工標注 + 理由欄位
3. **季度規劃**：若 Agent 已有 CRUD 工具調用，評估是否導入 Timestamp Query 機制，確保 Eval 重現性

***

## [參考連結]

- 📺 原始影片：[https://youtu.be/FB-MLPhL9Ms](https://youtu.be/FB-MLPhL9Ms) 
- 👤 講者 Phil Hetzel（Braintrust Solutions Engineering Lead）：[https://www.linkedin.com/in/philliphetzel/](https://www.linkedin.com/in/philliphetzel/) 
- 🏢 Braintrust（Agent 品質平台）：AI Engineer 2026 會議演講，發布於 2026/05/27
