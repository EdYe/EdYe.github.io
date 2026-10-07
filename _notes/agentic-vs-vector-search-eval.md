---
title: '代理搜尋 vs 向量搜尋：Eval 實測'
date: 2026-10-07
image: /images/影片筆記/agentic-vs-vector-search-eval.jpg
category: 影片筆記
tags: [評測飛輪, 代理搜尋, 向量搜尋, 孤兒追蹤, 評測四元件]
description: 'Braintrust 開發者倡導者 Jess Wang 在 AI Engineer World''s Fair 2026 的演講，核心貢獻是一次完整、可複製的端對'
quote: '💡向量搜尋給你「接近」正確程式碼的距離，代理搜尋才給你連接邏輯的結締組織。'
action: '🎯D-T-S-E 法則：依序建立資料集、任務、評分、實驗，固定 harness 只變一個變數，用工具旗標而非純 prompt 控制行為。'
source_has_timestamps: true
---
## [核心摘要]

Braintrust 開發者倡導者 Jess Wang 在 AI Engineer World's Fair 2026 的演講，核心貢獻是一次完整、可複製的端對端 Eval（評測）實作：在 Microsoft TypeScript Go 儲存庫上，以真實修復 PR 建立 bug 定位資料集，讓 Claude Code 分別使用 **Agentic Search** 與 **Vector Search** 找出程式缺陷，並用儲存庫自帶的測試套件評分。關鍵發現：兩者準確率相同，但 Vector Search 成本高出 4 倍——因為檢索回來的程式碼片段缺乏上下文，Agent 被迫不斷反覆搜尋，LLM 呼叫大量堆疊。

## [詳細重點整理]

### 1. 別再靠「感覺」上線功能 [00:42]

許多團隊的出貨決策基於「PM 試了幾個 prompt 覺得不錯」或「工程團隊說準備好了」——這是 shipping on vibes。正確的語言應該是：「我跑了 200 個測試案例，94% 通過，所以出貨」，甚至能說出細微權衡：「這個功能提升準確率 5%，但語氣分數下降 5%」。

Eval 能回答的問題包括：哪個 LLM 最適合需求（新模型不斷推出，決策需要數據）、跨語言與跨程式語言的表現差異（英文強但日文弱、Python 強但 TypeScript 弱）、成本效率、品牌一致性、如何偵測系統退化。

**關鍵概念：「Vibes-Based Shipping」**——沒有量化證據就部署 AI 功能，是最常見的反模式。

### 2. 諂媚事件：Eval 抓住品質退化 [02:22]

2025 年 4 月，OpenAI 的一次模型更新原本要讓模型更樂於助人，結果讓模型變得 **sycophantic（諂媚）**——過度附和使用者，反而降低真實性。AI 系統複雜且非確定性（non-deterministic），沒有 Eval 系統就無法及時發現這類無聲的品質劣化。

**關鍵概念：Sycophancy Regression（諂媚退化）**

### 3. Eval 的四大組成：資料集、任務、評分、實驗 [03:02]

- **資料集（Dataset）**：餵給 AI 系統的輸入，包含黃金標準案例、邊界案例與失敗模式
- **任務（Task）**：定義 AI 的行為，通常是 system prompt 加所選模型
- **評分系統（Scorer）**：判定輸出好壞，形式包含 deterministic scoring、LLM as a judge、human in review
- **實驗（Experiment）**：資料集 × 任務 × 評分系統的一組配置即一個實驗；調整任一要素就產生新實驗可比較改善或回歸

**關鍵概念：「Eval 四元件模型」**

### 4. 評測飛輪：可觀測性與 Eval 的閉環 [05:47]

用 Braintrust SDK 包裹應用程式碼，生產日誌流入平台後，抽樣 10–20 筆建立資料集 → 跑 Eval → 比較實驗 → 學到系統洞察 → 修改程式碼部署 → 新日誌再進來，循環重複。也可用自然語言查詢 traces（例如「摘要我的實驗」「標出問題」），有助於在多輪對話中捕捉人工難察覺的幻覺與漂移（drift）。

Eval 是團隊運動：AI 工程師（程式碼與資料入庫）、PM（定義成功假設、調 prompt）、領域專家（提供 ground truth 標註）、資料分析師（分析結果）各有角色。

**關鍵概念：「Eval Flywheel（評測飛輪）」**

### 5. 實驗設計：Agentic Search vs Vector Search [08:42]

起因於 CEO 轉發 Cursor 的推文——Cursor 聲稱用 semantic（agentic）search 大幅提升 coding agent 效能，引發社群熱議，因此決定實際驗證：

- **Vector Search** [09:32]：把程式碼轉成 embeddings（語意向量）存入 Qdrant/Pinecone 等向量資料庫，查詢時回傳語意最接近的程式碼區塊
- **Agentic Search** [10:42]：給 LLM grep、find、ls、cat 等 bash 工具，像人類一樣探索 codebase——查函數名、開檔、讀檔、沿函數呼叫追到另一個檔案

### 6. 資料集與任務實作 [11:22]

- 資料集：從 Microsoft TypeScript Go 開源儲存庫找出標題含 "fix" 的已合併 PR，checkout 到 parent commit（bug 尚未修復的狀態），用 Claude 從 buggy 與 fixed 的 diff 生成 bug 任務描述，約 20 筆
- 任務：Agentic search 直接用 Claude Code 預設行為；Vector search 為保持實驗一致性仍在 Claude Code harness 中執行，但用兩層手段阻止預設行為——prompt 明確指示不用 agentic search，加上 `--disallowedTools` 旗標禁用工具（因為「prompting is never enough」）

**關鍵概念：「Prompt 不夠，要用工具層硬限制」**

### 7. 修復孤兒 Trace [13:17]

Claude Code 以子程序執行時，traces 變成孤兒（orphaned）——上層只看得到「run Claude agent」，看不到內部任何 LLM 呼叫與終端命令。解法是把 parent span ID 作為環境變數傳入子程序，修復後可看到所有輪次、LLM 呼叫與每個 grep/bash/ls/find 命令。這種透明度是後續除錯的基礎。

**關鍵概念：「Trace Orphaning 與 Span 繼承」**

### 8. 評分與結果 [14:37]

評分採二元制：通過 Microsoft TypeScript Go 官方測試套件 = 100%，失敗 = 0%。

**結果：兩者準確率相同，Vector Search 成本約 4 倍。**

### 9. 為什麼 Vector Search 輸在成本 [15:22]

- Vector search 回傳的程式碼區塊常缺少 imports、工具呼叫與上層呼叫程式碼，上下文不足以解 bug。實測案例：vector agent 做了 26 次搜尋仍拼不出三個函數跨檔案的互動關係
- Agentic search 如人類般 grep 函數名 → 讀完整函數 → 看出邏輯缺陷 → 沿呼叫鏈追進另一個檔案
- 精闢總結：**Vector search 給了「接近正確程式碼的 proximity」，Agentic search 才有連接邏輯的「connective tissue（結締組織）」**
- 成本差距根源：vector search 不斷「搜尋→回傳區塊→再搜尋」，LLM 呼叫堆疊推高成本 [16:27]

### 10. 限制與最佳實踐 [16:47]

此 eval 有許多可改進處：每個任務應跑多次 trial（LLM 非確定性導致單次分數不可信）、vector search 實作偏弱、資料集僅 20 筆應擴及更多儲存庫。但演講目的是示範端對端建立 eval 的完整流程，而非完美實驗。

## [結論與行動建議]

**啟發金句**

> Vector search gives you proximity to the code; agentic search gives you the connective tissue.

（向量搜尋給你「接近」正確程式碼的距離，代理搜尋才給你連接邏輯的結締組織。）

**具體行動建議：D-T-S-E 法則**  
建立任何 AI 系統評測時，依序完成 **D**ataset（真實資料，含邊界案例）→ **T**ask（prompt + 模型）→ **S**corer（用既有測試套件當免費 ground truth）→ **E**xperiment（固定 harness、只變一個變數、用工具旗標而非純 prompt 控制行為）。

**生活實踐建議**

- 你的 AI 應用開發流程中：與其憑「試了幾個 prompt 感覺不錯」就上線，先從生產日誌抽 10–20 筆建立資料集，跑一輪 eval 再部署
- 做 RAG 系統時，不要預設向量檢索一定優於 grep 式工具探索——先量測成本與準確率，特別注意 chunk 缺乏上下文導致的「反覆搜尋成本爆炸」
- 寫子程序工作流（如 Claude Code 嵌入自動化管線）時，記得傳遞 parent span ID 環境變數，避免觀測資料孤兒化

## [參考連結]

[原始 YouTube 影片](https://youtu.be/T3SS931wU0I)

來源：（影片頁面與完整逐字稿）[[about](https://about.youtube/)]