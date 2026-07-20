---
title: '如何打造真正有效的AI評測系統'
date: 2026-07-20
image: /images/影片筆記/build-evals-that-actually-matter.jpg
category: 影片筆記
tags: [對抗式用戶模擬器, LLM Judge校準, 錯誤分析迴圈, 評測反模式, 統計嚴謹性]
description: 'Lyft 客服 AI Agent 每月處理數百萬通對話，解決約三分之一的客服問題。影片揭示其端到端評測管線的核心痛點：用前沿 LLM 模擬用戶過於「禮貌」，導致'
quote: '如果你的評測通過率高達 90%，那不是你的 Agent 太強，而是你的用戶模擬器太弱。'
action: '採用 Data First、Fine-tune、Calibrate 的 D-F-C 法則打造評測系統，並建立每週錯誤分析迴圈持續迭代。'
source_has_timestamps: true
---
# Build Evals That Actually Matter — Nick Ung, Lyft

***

## [核心摘要]

Lyft 客服 AI Agent 每月處理數百萬通對話，解決約三分之一的客服問題。影片揭示其端到端評測管線的核心痛點：**用前沿 LLM 模擬用戶過於「禮貌」，導致離線評測通過率虛高至 90%，上線後立刻暴露大量未預見的失敗模式**。解法是微調一個基於真實 Lyft 用戶逐字稿的**對抗式用戶模擬器**，搭配可校準的 LLM 評審機制、統計嚴謹性與持續錯誤分析迴圈，形成完整的「離線評測 → 線上評測 → 回饋改進」閉環 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

***

## [詳細重點整理]

### 1. 評測系統全貌：開發 → 離線評測 → 上線 → 線上評測 [00:00]

整個評測生命週期分為兩大階段。**開發階段**涵蓋上下文管理、RAG 管線、工具定義、Agent Graph 建構與系統提示詞撰寫。**生產階段**則包含線上追蹤、線上評審與人工介入的錯誤分析管線。Nick 強調，AI Agent 的評測思維與傳統機器學習模型一致——不應將線上真實用戶當作測試資料 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：Launch Gate（發布門檻）**——在離線評測達標前，不允許 Agent 進入生產環境 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 2. 評測失敗的三大常見原因 [05:39]

- **評分未被用於實際決策**：LLM Judge 分數若只是浮動數字、未與發布門檻掛鉤，等同沒有評測。
- **LLM Judge 過於通用且雜訊高**：早期 Judge 輸出的分數太模糊、不可操作，團隊不信任其洞察。
- **生產回歸缺乏明確負責人**：回歸發生時需有清晰機制捕捉問題並指派 Owner 採取行動。

**關鍵概念：Meaningful Gating（有意義的門控）**——評測分數必須直接影響發布決策 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 3. 離線評測系統架構 [07:23]

借鑑 Sierra AI 的 **Taobench** 論文，Lyft 建構離線模擬器：LangGraph Agent 與 User LLM 進行多輪對話，生成完整對話軌跡，再由離線評審（LLM Judge + 確定性程式斷言）打分。模擬器定義三個核心維度：用戶意圖、用戶資料/世界狀態（如司機年資、車型）、用戶行為人格 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

確定性評估以程式碼斷言形式存在，例如驗證 Agent 是否正確呼叫了「授予退款」工具，類似傳統單元測試 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 4. 合成資料的挑戰與解法 [11:08]

直接用 LLM 生成 50 條測試查詢是最常見的反模式。Lyft 的做法是：從真實生產資料取樣，補充至離線資料集；再透過**資料變異**覆蓋不同黃金路徑與邊界案例 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 5. 微調對抗式用戶模擬器 [13:16]

這是全片最核心的技術貢獻。Lyft 最初用前沿 LLM 扮演用戶，結果用戶表現「太有耐心、太有條理」，離線評測通過率高達 90%。真實生產中的用戶卻是急躁、憤怒、不願詳細解釋問題的。解法是用真實 Lyft 用戶逐字稿**微調專用 LLM**，使其產出更貼近真實用戶的表達風格。微調後評測分數顯著下降，但這正是期望的結果——更難的評測才能暴露真正的問題 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

同時定義多種**用戶人格**：繞過者（Bypasser，直接要求轉人工）、退款尋求者（Refund Seeker）、AI 懷疑論者（AI Skeptic）等，讓模擬更貼近真實分佈。此方法亦參考了 Microsoft 的 User Allen 論文 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：Adversarial User Simulator（對抗式用戶模擬器）**——微調後的 LLM 模擬器能角色扮演沮喪、困惑、對抗性用戶，分佈與生產環境一致 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 6. LLM-as-a-Judge 的問題與重構 [17:33]

Ashe 指出，通用預建評測指標（如 DeepEval 的 response_helpfulness、toxicity、conciseness）雖然能用，但**不可操作**——「response_helpfulness = 0.5」無法告訴團隊該修什麼。應與領域專家合作，將評測框架圍繞**任務成功/失敗的二元結果**設計，並對齊業務目標。例如「教育策略評分量表」：Agent 教育用戶次數過多或過早轉人工都判定為失敗 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：Actionable Metric（可操作指標）**——評測分數必須能直接指向具體的修復行動 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 7. 校準 LLM Judge：如同訓練分類器 [21:17]

將 LLM Judge 視為二元分類器。標註約 100 個 Pass/Fail 人工範例，切分為 Train/Dev/Validation 三組。Train 集提供 Few-shot 範例給 Judge Prompt；Dev 集迭代改進 Prompt；Validation 集確認未過擬合。最終計算 Precision 與 Recall，量化 Judge 的可靠性。資料切分比例與傳統 ML 不同，因為不訓練模型權重，僅用於 Prompt 迭代 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 8. 標準漂移與評審持續校驗 [23:32]

**關鍵概念：Criteria Drift（標準漂移）**——評測標準不應事先固定不變。透過觀察資料與標註輸出，團隊對「品質」的認知會持續演進。評測標準應與模型觀察**共同開發**，而非解耦。每次新增範例後重新校準 Judge 的 Precision/Recall，確保評審持續追蹤真實品質標準 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 9. 統計嚴謹性 [24:56]

評測分數應附帶**信賴區間**。例如兩個評審分別得 84% 和 88%，若僅基於 50 個樣本，4 個百分點的差距可能在統計上不顯著。應根據場景決定統計嚴謹度的投入：發布決策與高層報告需完整校準；日常迭代則可適度放寬。較大的增益與配對設計所需的樣本數遠少 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 10. 評測反模式清單 [26:54]

Ashe 列舉了非窮盡的**Eval Anti-Patterns**，核心教訓是：**忽略資料是最致命的反模式**。若不查看原始資料，就無法建立有意義的評測標準與標籤；沒有標籤就無法評估 Judge；不評估 Judge 就不知道 Agent 管線是否正常運作。這形成層層依賴的基礎鏈條 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 11. 錯誤分析迴圈 [27:50]

**關鍵概念：Error Analysis Loop（錯誤分析迴圈）**——持續運行而非一次性稽核。流程為：深入原始 Trace → 定位失敗模式 → 僅保留會改變決策的指標、移除雜訊 → 形成新假設重新評測 → 重複。建議以週或雙週為週期執行 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 12. 追蹤與標註佇列 [29:18]

使用 LangSmith、Langfuse 等工具記錄完整 Graph 執行軌跡：節點執行、LLM 上下文、工具呼叫、Token 用量、延遲等。搭配**標註佇列**介面，讓領域專家無需閱讀原始 JSON 即可標註與回饋，這些標註成為離線評測資料集與 Judge 校準的 Ground Truth 來源 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 13. 持續學習閉環 [30:48]

**關鍵概念：Continual Learning Loop（持續學習迴圈）**——分為三層：

- **Model Learning**：後訓練、更新模型權重、訓練自訂 LLM。
- **Context Learning**：改善 Agent 所見的資訊（文件、記憶、工具輸出）。
- **Harness Learning**：更新系統提示詞、工具 Schema、控制流路由、重試策略 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

### 14. 未來方向：系統化 Eval Harness 與後訓練 [32:31]

目前離線模擬器散落於各 Notebook 與分析 Repo，缺乏可重複性。Lyft 正在投入**系統化 Eval Harness**：以 YAML 配置驅動，工程師、分析師、資料科學家均可貢獻評測套件。定義 Task、Dataset、Persona、LLM Adapter、Evaluator 等高階原語，支援並行執行上萬條測試。可在本地開發、Pre-commit Hook、CI/CD 等多個環節重複運行 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

另一方向是**後訓練與強化學習**：利用多年累積的真實用戶訊號，微調執行不同客服任務的模型，並構建 Reward Modeling 問題以啟用 RL 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

***

## [技術/數據對比]

| 維度 | 前沿 LLM 模擬用戶 | 微調後對抗式用戶模擬器 |
|---|---|---|
| 用戶語氣 | 過於禮貌、有耐心、條理清晰 | 急躁、憤怒、表達簡短 |
| 離線評測通過率 | ~90%（虛高） | 顯著下降（貼近真實） |
| 失敗模式覆蓋 | 遺漏生產中大量邊界案例 | 發現合成資料集遺漏數月的回歸 |
| 來源 | 前沿實驗室通用模型 | 真實 Lyft 用戶逐字稿微調 |
| 參考論文 | — | Microsoft User Allen、Sierra AI Taobench |

| 維度 | 通用預建評測指標 | 可操作業務對齊指標 |
|---|---|---|
| 設計來源 | 預建框架（如 DeepEval） | 領域專家 + 資料科學家共同定義 |
| 輸出形式 | 連續分數（如 0.5） | 二元 Pass/Fail |
| 可操作性 | 低——「helpfulness=0.5」不知如何修 | 高——直接指向具體修復行動 |
| 校準方式 | 無標準化校準 | Train/Dev/Validation 切分 + Precision/Recall |
| 決策影響 | 不影響發布決策 | 直接作為 Launch Gate |

***

## [結論與行動建議]

> **啟發金句**
> 「如果你的評測通過率高達 90%，那不是你的 Agent 太強，而是你的用戶模擬器太弱。」

> **具體行動建議 —— D-F-C 法則**
> - **D**ata First：先從真實生產資料取樣，而非用 LLM 憑空生成測試集。
> - **F**ine-tune：微調用戶模擬器使其貼近真實用戶分佈，而非使用通用前沿 LLM。
> - **C**alibrate：將 LLM Judge 視為分類器，用 Precision/Recall 持續校準，並附帶信賴區間。

> **生活實踐建議**
> 在日常工作中的 AI 應用評測中，建立一個每週運行的「錯誤分析迴圈」：回顧本週的失敗案例 Trace → 分類失敗模式 → 只保留能改變決策的指標 → 將改進回饋到提示詞、上下文或工具 Schema。這個習慣能確保你的 AI 應用品質持續演進，而非停滯在「看起來很好」的假象中。

***

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/3z2uT5aDx_Y
- 講者 Nick Ung LinkedIn：https://www.linkedin.com/in/unglikteng
- Taobench 論文（Sierra AI）
- Microsoft User Allen 論文
