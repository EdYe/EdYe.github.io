---
title: '終結Token浪費：三層架構解方'
date: 2026-07-31
image: /images/AI筆記/never-hit-token-limit-again.jpg
category: AI筆記
tags: [重複輸入, 手動習慣, TokenSaver技能, Ringer多代理框架, 三層架構]
description: 'AI Token 消耗的真正元兇不是輸入文字，而是重複輸入——模型每回合重傳整段歷史。單日追蹤到 37.7 億 Token，96% 屬重複輸入，全片提出三層架構因應。'
quote: '💡「你打字的訊息，只是整個呼叫中最微不足道的一部分。整理你的桌面，是你永遠擁有的工作。」'
action: '🎯先落實 Level 1 九項手動習慣（尤其任務切換時開新對話），再安裝 Token Saver 技能自動化，視需求評估 Ringer 中介層攔截請求。'
source_has_timestamps: true
---
# [核心摘要]

AI Token 消耗的真正元兇不是你輸入的文字，而是**重複輸入（Reused Input）**——模型在每次對話回合中重新傳送整段歷史對話。在一天內，追蹤器記錄到 37.7 億個 Token 流經 Codex 工作區，其中高達 96%（35.9 億）屬於重複輸入 。影片提出一套三層架構：Level 1 為九項手動習慣、Level 2 為 Token Saver 自動化技能、Level 3 為 Ringer 多代理攔截框架，目標是將 Token 使用效率提升 10 倍 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

***

# [詳細重點整理]

## 核心問題：重複輸入的複利效應 [00:00]

LLM 的運作機制決定了每次「按下 Enter」時，整段對話歷史會被重新打包從頭傳送。第一則訊息成本等於你輸入的內容；第二則等於你輸入的加上第一次的回答與原始輸入；到第十則時，新輸入的文字已成為微不足道的捨入誤差 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**重複輸入（Reused Input）**——模型已見過、卻在每次請求中被迫重新處理的內容。這不是 AI 實驗室會自動修復的問題，因為實驗室有誘因讓你消耗更多 Token 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

「桌面隱喻」貫穿全片：AI 就像你的工作桌，模型能力越強、工具越多，桌面堆積越快，你越早撞牆。整理桌面是使用者自己的責任 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

## Level 1：九項手動習慣 [04:40]

### 規則 1：編輯錯誤，而非爭辯 [04:40]

發現自己輸入有誤時，不要在下一則訊息中說「那是錯的」——直接使用編輯按鈕修正原始請求並重新發送。避免將錯誤的請求、錯誤的回答、以及修正指令全部堆疊進對話歷史 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**原地修正（Edit-in-Place）**。

### 規則 2：合併相關問題並指定輸出格式 [05:15]

同一文件集的多個問題應一次性提交，並明確指定期望的輸出形式（一頁摘要、150 字、純 bullet、標題）。減少 AI 在消歧義上浪費的 Token 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

### 規則 3：任務變更時開新對話 [05:58]

長對話在聚焦同一問題時有效率，但跨任務時會攜帶大量重複 Token。從零開始的新任務不會完全歸零（系統指令仍會載入），但能阻止舊對話的累積。這是在實測中帶來最大可量化改變的規則 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**任務隔離（Task Isolation）**。

### 規則 4：只攜帶結果，不攜帶過程 [07:13]

多階段工作流程中（如研究 → 寫作），每個階段結束後只將最終產物（如研究報告）帶入下一步。不要將初稿、三輪批評、被拒絕的來源和模型推理全部堆疊進下一個階段 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

### 規則 5：只要求你需要的答案 [08:06]

輸出 Token 會被重複計費——產生時付一次，之後每一回合作為輸入再付一次。要求精簡的輸出（段落、JSON、五個 bullet）不僅節省輸出 Token，更節省後續每一回合的輸入 Token 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**輸出複利（Output Compounding）**。

### 規則 6：自己搜尋檔案 [09:03]

模型具備檔案搜尋能力是便利功能，但也是巨大的 Token 消耗器。自行搜尋檔案、找出相關段落，只將必要的 snippet 提供給模型，而非讓模型讀取整份檔案 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

### 規則 7：發送最輕量的來源格式 [09:30]

如果文字內容是重點而排版不是，就將 PDF 轉為 Markdown 或純文字後再貼入。不要因為「模型能處理」就丟入 PDF 和 18 張截圖——能處理不代表不會燒光你的 Token 配額 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

### 規則 8：整理來源，保持桌面乾淨 [~10:00]

花時間整理來源檔案，不要偷懶丟入原始格式。將來源整理好是減少 Token 消耗的基本功 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

### 規則 9：將答案存入可檢索的資料庫 [10:13]

使用 OpenBrain 或自建資料庫，將反覆查詢的資訊儲存在可快速檢索的地方。模型能直接從資料庫取出答案，而不需重新挖掘來源、重新計算。這大幅提升 Token 效率 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**檢索優先於重算（Retrieve Over Recompute）**。

## Level 2：Token Saver 技能 [11:13]

一條指令即可安裝到 Codex 與 Claude Code 的自動化技能，在使用者維持正常工作流程的同時執行以下操作 ： [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

- 開啟大型來源前先搜尋
- 發送選定段落而非整份檔案
- 盡可能以程式碼執行精確工作
- 儲存已接受的版本，並從該結果加上你的修改建構下一個請求
- 將答案控制在指定長度
- 阻止無意義的重試循環

關鍵概念：**自動化桌面清理（Automated Desk Cleaning）**。

## Level 3：Ringer 多代理框架 [16:23]

Level 1 和 Level 2 共享同一個天花板：技能無法縮小它所在的那次呼叫。當模型讀取技能時，請求的初始封包（對話歷史、常駐指令、工具定義）已在信封中發送完畢 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

Ringer 在本地端運行，位於 AI 介面與模型供應商之間。在請求送達模型供應商之前，它可以 ： [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

- 直接回傳答案，完全跳過模型呼叫
- 以固定本地配方執行，無需模型呼叫
- 只選取有用段落送出
- 在硬性限制下轉發小型請求
- 完全停止請求

### 規則 10：只載入任務可用的工具 [12:24]

每個連接的工具都攜帶描述（功能、使用時機、參數），這些描述在模型做任何事之前就是輸入。典型配置（GitHub + Slack + Sentry + Grafana）在 Claude 執行任何動作前就消耗約 55,000 個 Token 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**工具定義耗損（Tool Definition Overhead）**。

### 規則 11：善用壓縮與上下文編輯 [13:13]

OpenAI 支援長時任務的壓縮（Compaction），攜帶狀態前進但需要更少 Token。Anthropic 支援上下文編輯（Context Editing），清除舊的工具結果和思考區塊。需注意：清除舊內容後，模型依賴初始提示的近似版本繼續工作 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**上下文壓縮（Context Compaction）**。

### 規則 12：選擇夠用的最低模型 [~14:30]

使用能完成任務的最「笨」模型。Token Saver 技能會分析問題並給出模型選擇的初步建議。越熟悉 AI 工作的人，越能判斷這條「最笨模型」的界線在哪裡 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**最小可行模型（Minimum Viable Model）**。

### 規則 13：善用提示快取 [15:35]

Prompt Caching 對重複性 API 工作極為重要，可快取部分提示內容，避免重複傳送整段訊息。但這是 API 層級功能，一般知識工作者不需使用——若你不知道什麼是 API 和 Prompt Caching，就不需要它 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**提示快取（Prompt Caching）**。

### 規則 14：強制硬性限制 [17:55]

透過 Ringer 等中介層可以強制執行封包大小限制——限制送出的封包大小、回傳的封包大小、或對每次呼叫設定硬性上限，確保永遠不會送出 1,000 萬 Token 的請求 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

### 規則 15：檢索已接受的答案 [~18:30]

Ringer 可以查詢 OpenBrain 或資料庫，若已有被接受的答案，直接回傳「我們上週已討論過此問題，回應如下」，完全節省 100% 的模型呼叫 。 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

關鍵概念：**本地優先回應（Local-First Response）**。

***

# [技術/數據對比]

### 單日 Token 消耗實測數據

| 指標 | 數值 |
|------|------|
| 單日 Token 總量 | 37.7 億  [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |
| 重複輸入 Token | 35.9 億  [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |
| 重複輸入佔比 | 96%  [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |
| 單日 Codex 執行緒數 | 143  [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |

### 三層優化架構比較

| 層級 | 機制 | 自動化程度 | 適用對象 | 核心限制 |
|------|------|-----------|---------|---------|
| Level 1 | 九項手動習慣 | 完全手動 | 所有使用者 | 依賴個人紀律  [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |
| Level 2 | Token Saver Skill | 半自動（在現有對話內運作） | Codex / Claude Code 使用者 | 無法縮小當前呼叫的已發送封包  [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |
| Level 3 | Ringer 多代理框架 | 全自動（攔截請求前處理） | 進階使用者 / API 工作者 | 需自行部署中介層  [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |

### 工具定義 Token 耗損

| 工具組合 | Token 消耗（模型執行前） |
|----------|----------------------|
| GitHub + Slack + Sentry + Grafana | ~55,000  [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM) |

***

# [結論與行動建議]

> 「你打字的訊息，只是整個呼叫中最微不足道的一部分。整理你的桌面，是你永遠擁有的工作。」 [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)

**E-D-C 法則（Edit–Delink–Carry）**：
- **E**dit：原地修正錯誤，不疊加爭辯
- **D**elink：任務切換時斷開舊對話
- **C**arry：只攜帶階段產物前進，不攜帶過程

**生活實踐建議**：
在日常 Codex / Claude Code 工作流程中，先實施 Level 1 的九項習慣（尤其是規則 3——任務切換時開新對話，這是實測中效果最大的改變）。接著安裝 Token Saver 技能自動化大部分手動工作。若你的工作涉及大量 API 重複呼叫與多工具整合，進一步評估 Ringer 中介層來在請求發出前攔截並精簡 Token。定期審計自身的 Token 消耗分佈，找出重複輸入的熱點並針對性優化。

***

# [參考連結]

- 原始 YouTube 影片：https://youtu.be/Y8vAQ1FgNbM [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)
- 完整文章與 Token Saver 技能：https://natesnewsletter.substack.com/p/reduce-ai-token-usage [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)
- Nate B Jones Newsletter：https://natesnewsletter.substack.com/ [youtube](https://www.youtube.com/watch?v=Y8vAQ1FgNbM)
