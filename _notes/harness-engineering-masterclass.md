---
title: 'Harness工程：AI Agent失敗診斷法則'
date: 2026-07-07
image: /images/AI筆記/harness-engineering-masterclass.jpeg
category: AI筆記
tags: [Harness工程, 代理迴圈, 上下文管理, 工具介面, 驗證與可觀測性]
description: '影片核心貢獻是將「AI Agent為何失敗」的模糊問題，拆解成可診斷的具體層級，解決了業界普遍「出錯就怪模型不夠聰明」的認知盲點。'
quote: '當 Agent 失敗時，不要只問模型夠不夠聰明，要問是哪一層 Harness 撐不住了。'
action: '套用十二層診斷法則，每次 Agent 出錯時依序排查指令、上下文傳遞、上下文管理、工具介面、執行環境、持久狀態、編排、子代理、技能層、驗證與可觀測性等層級的瓶頸所在。'
source_has_timestamps: true
---

## [核心摘要]

本影片系統性地拆解了 AI Agent 的「**Harness Engineering（支架工程）**」——即圍繞模型所建構的完整系統層。模型本身只是推理引擎，真正讓 Claude Code、Codex 等工具展現「魔法」的，是九大基元（Primitive）：指令、上下文交付、上下文管理、工具介面、執行環境、持久狀態、編排、子代理、技能層，以及驗證與可觀測性。核心貢獻在於提供一套可診斷的框架：當 Agent 失敗時，不應只問「模型是否夠好」，而應逐層排查「哪個 Harness 層失效」，藉此將偶發的聰明行為轉化為可依賴的系統工程 。 [scribd](https://www.scribd.com/document/869199074/Links)

***

## [詳細重點整理]

### 1. Harness 工程的定義與模型邊界 [00:00]

模型本身只是接收 Prompt、輸出文字的推理引擎，其能力邊界在於只能看到 Prompt 內容與訓練資料。若當前專案、Repository 或事件不在輸入範圍內，模型只能猜測，這就是**幻覺（Hallucination）**的根源。因此，第一個問題不是「模型是否聰明」，而是「我們到底給了它什麼素材」。

關鍵概念：**模型邊界（Model Boundary）**

### 2. Agent 定義與 Agentic Loop [02:39]

OpenAI Agent SDK 將 Agent 定義為「配置了指令與工具、且置於可操作環境中的 LLM」。其核心運作機制是**代理迴圈（Agentic Loop）**：推理（Reason）→ 行動（Act）→ 觀察（Observe）→ 重複。講者強調需區分三層：模型（推理引擎）、Runtime（執行迴圈）、Harness（圍繞 Runtime 的系統）。Agent 失敗時常被歸咎於模型，但往往是 Harness 層未能支撐模型所致。

關鍵概念：**代理迴圈（Agentic Loop）**

### 3. 指令層 [03:45]

指令（Instruction）是第一個 Harness 基元，定義模型身份、工作類型、語氣、約束條件、編碼風格與審查規則。`agents.md`、`CLAUDE.md`、System Prompt、Cursor Rules 等皆屬此層。其價值在於將重複性指引移入環境，免去每次手動貼上。但指令是被動的——能說「遵循專案規範」，卻無法自行發現規範內容，除非相關檔案已被提供。

關鍵概念：**被動指令（Passive Instruction）**

### 4. 上下文交付 [06:15]

上下文交付（Context Delivery）機制讓模型取得所需素材，例如透過 `@` 符號引用檔案。提供原始碼、失敗測試、堆疊追蹤後，模型從給出通用修復進化為精準修復。但單純傾倒大量資料並非上下文工程——模型有有限的**上下文視窗（Context Window）**，且注意力並非免費。錯誤的上下文比缺失上下文更危險，因為它製造「合理的分心」。

關鍵概念：**上下文視窗（Context Window）**

### 5. 上下文管理 [08:14]

上下文管理（Context Management）解決「誰來決定此刻哪些上下文重要」的問題。Harness 透過 RAG 檢索、重排序（Re-ranking）、定期摘要、壓縮（Compaction）等技術，在接近視窗上限時觸發管理機制。核心目標是**保護模型的注意力**——保留重要片段、摘要冗餘部分、在正確時機檢索正確檔案，避免將半個視窗浪費在雜訊上。

關鍵概念：**注意力保護（Attention Protection）**

### 6. 工具介面 [10:46]

工具介面（Tool Interface）讓模型從「說話者」變為「行動者」。工具具備名稱、描述、輸入與輸出 Schema，模型決定呼叫哪個工具及傳入哪些參數。**MCP（Model Context Protocol）** 正是此層的標準化抽象，讓服務提供者暴露工具給模型。OpenAI Function Calling、Anthropic Tool Use、bash/grep 等皆屬此基元。但模型選對工具不等於執行安全——工具可能失敗、回傳髒資料、網頁可能含 Prompt Injection。

關鍵概念：**結構化行動（Structured Action）**

### 7. 執行環境 [12:19]

執行環境（Execution Environment）是工具呼叫成為「有界現實」的場所，涵蓋檔案系統範圍、網路策略、憑證、沙箱、容器、瀏覽器 Session 等。Daytona、E2B、Docker Dev Sandbox 等公司專注於此層。這裡是信任落實之處——不是告訴模型「別碰密鑰」，而是從環境層面讓它根本無法存取。每個任務在獨立沙箱中執行，不是部署細節，而是 Harness 基元。

關鍵概念：**有界執行（Bounded Execution）**

### 8. 持久狀態 [14:16]

持久狀態（Durable State）是跨回合存活的工作台，包括計畫檔案、檢查點、任務狀態、Session 摘要、執行日誌、Diff、記憶儲存等。上下文管理決定「此刻帶入模型什麼」，持久狀態則「在 Prompt 之外保存事實、產物與進度」。對 Coding Agent 而言是分支與測試日誌；對研究 Agent 而言是來源地圖與引用表。關鍵不在儲存格式，而在進度可被模型當前注意力之外檢查。

關鍵概念：**可檢查進度（Inspectable Progress）**

### 9. 編排 [16:19]

編排（Orchestration）決定工作如何流動：生命週期掛鉤（Lifecycle Hooks）、心跳、重試、審批閘道、人類交接、步驟排序、任務清單與模型路由。這層讓 Agent 工作從「聊天」變成「Runtime」。LangGraph 的 Hooks 是典型範例——真實系統需要攔截行為的切入點。模型並非靠意志力完成所有流程，而是 Harness 承載工作流並執行繁雜工作。

關鍵概念：**工作流承載（Workflow Carrying）**

### 10. 子代理 [18:13]

子代理（Sub-agents）讓 Harness 將工作拆分為有界迴圈。主代理派發任務後保留整合責任。OpenAI Agent SDK 提供兩種模式：Agents as Tools（管理器保持控制，呼叫專家）與 Handoff（主動對話轉移至專家）。子代理不是「更多模型」，而是具備更窄任務、更窄上下文、更窄工具的專家。透過縮小推理面積提升品質。但委派帶來一致性問題——若每個子代理自創流程，將產生平行不一致。

關鍵概念：**有界委派（Bounded Delegation）**

### 11. 技能層 [20:20]

技能層（Skill Layer）為可重複使用的程序，解決委派一致性問題。技能編碼了工作流程：何時使用、需要什麼輸入、遵循哪些步驟、優先使用哪些工具。Slash Commands、Playbooks、Runbooks、Recipes、Workflows 皆屬此層。技能讓 Harness 不必依賴每個 Agent 從零重新發現流程，將重複性專業知識從「記住要做某事」的指令，轉化為可調用的命名能力。

關鍵概念：**可重複程序（Reusable Procedure）**

### 12. 驗證與可觀測性 [22:20]

驗證（Verification）要求「收據」：測試、建置、型別檢查、Lint、瀏覽器截圖、視覺檢查、Evals。Agent 說「我完成了」，Harness 則問「證明給我看」。**「看起來不錯」不是驗證策略**。可觀測性（Observability）則記錄完整執行鏈：Traces、工具呼叫時間線、日誌、成本、延遲、Prompt 版本、工具版本、審批事件。Bug 往往不在最終訊息中，而在三步之前的工具呼叫——搜尋了錯誤符號、信任了錯誤頁面、跳過了失敗測試。可觀測性將「Agent 搞砸了」轉為可除錯系統。

關鍵概念：**收據式驗證（Receipt-based Verification）**

### 13. Harness 工程的演化 [25:14]

失敗應轉化為基礎設施改進：重複的上下文缺失→新增檢索規則；糟糕的工具結果→更嚴格的 Schema；危險指令→權限閘道；邊界案例→測試；重複修正→記憶；重複工作流→技能。這是 Agent 版本的**事後檢討迴圈（Postmortem Loop）**——不是解釋事件，而是改變系統使同類失敗更難再現。目標不是產生一次完美執行，而是讓下次執行從更好的起點出發。Harness 會因此**複利增長（Compound）**。

關鍵概念：**失敗即基礎設施（Failure as Infrastructure）**

***

## [技術對比]

| Harness 基元 | 核心職責 | 常見實作形式 | 失效時的症狀 |
|---|---|---|---|
| 指令 | 塑造模型行為 | `agents.md`、`CLAUDE.md`、Cursor Rules | 行為偏離規範、風格不一致 |
| 上下文交付 | 提供模型所需素材 | `@file` 引用、檔案注入 | 泛化修復、缺乏精準度 |
| 上下文管理 | 保護模型注意力 | RAG、Re-ranking、Compaction | 回應變慢、注意力被雜訊淹沒 |
| 工具介面 | 讓模型能行動 | MCP、Function Calling、bash/grep | 只說不做、無法執行操作 |
| 執行環境 | 有界執行與信任控制 | 沙箱、容器、Dev Container | 安全風險、存取失控 |
| 持久狀態 | 跨回合保存進度 | Plan 檔案、檢查點、記憶體 | 崩潰後重頭來過、進度遺失 |
| 編排 | 管理工作流生命週期 | Lifecycle Hooks、重試、審批閘道 | 流程卡死、缺乏恢復機制 |
| 子代理 | 拆分工作為有界迴圈 | Agents as Tools、Handoff | 串行過慢、上下文擁擠 |
| 技能層 | 可重複使用程序 | Slash Commands、Playbooks | 平行不一致、流程無標準 |
| 驗證與可觀測性 | 證明工作成功與除錯 | 測試、Traces、工具呼叫日誌 | 無法除錯、無法改進 |

***

## [結論與行動建議]

### 啟發金句

> 「Harness Engineering 是我們從聰明 Agent 邁向可依賴系統的方式。模型仍然重要，但可靠性是建立在模型周圍的系統之中。」

### 具體行動建議：W-H-I-C-H 法則

當 Agent 失敗時，依序排查六個維度：

- **W**hat instruction（指令是否缺失？）
- **H**ow was context（上下文是否錯誤或過載？）
- **I**solation environment（執行環境是否正確？）
- **C**oordination（編排與狀態是否到位？）
- **H**andoff（是否該委派子代理或載入技能？）
- 最後追問：**有沒有 Verification 與 Trace 讓我們看進去？**

### 生活實踐建議

在日常 AI 應用開發中，將這九大基元轉化為團隊的 **Agent 故障排查清單**。每次 Agent 出錯時，不要急著換模型或調 Prompt，而是打開可觀測性面板，沿 Trace 往回走三步，找出「哪一層 Harness 跑出了路」。長期而言，建立**事後檢討迴圈**：每週回顧重複性失敗，將其轉化為新的檢索規則、Schema 約束、權限閘道或技能，讓系統每週都比上週更穩健，實現真正的複利增長。

=========
將內容以色鉛筆手繪塗鴉風格繪製成圖卡
