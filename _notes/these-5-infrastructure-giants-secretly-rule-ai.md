---
title: '掌控 AI Agent 的五大基礎設施控制層'
date: 2026-05-21
image: /images/AI筆記/these-5-infrastructure-giants-secretly-rule-ai.jpeg
category: AI筆記
tags: [Agent治理, 委派授權, 語意治理, 可觀測性, 基礎設施控制層]
description: '真正決定 AI Agent 能否上線的，不是 OpenAI 或 Anthropic，而是掌控 Agent 基礎設施控制層的五類公司：Runtime、Identity、Data、Payments、Observability'
quote: 'Agent 不遵守組織架構圖，你的治理模型必須彌補這個缺口。'
action: '在 Agent 功能規劃時套用 7 問框架建立控制地圖，每個控制點指定技術選型與負責團隊，缺一不可上線。'
source_has_timestamps: true
source_raw: 'These 5 Infrastructure Giants Secretly Rule AI'
---

## [核心摘要]

真正決定 AI Agent 能否上線的，不是 OpenAI 或 Anthropic，而是掌控**Agent 基礎設施控制層**的五類公司：Runtime（Cloudflare/AWS）、Identity（Auth0/Okta）、Data（Snowflake/Databricks）、Payments（Stripe）、Observability（Datadog）。模型只是生產流程的一個環節，這五層基礎設施才是決定 Agent 能否安全交付的真正守門人。 

***

## [詳細重點整理]

### 1. 運算力不是全部 [00:00]
模型能力與 GPU 算力只決定 AI 能否「被服務」，但當 Agent 開始自主行動後，真正的瓶頸轉移到：**Agent 跑在哪裡？記得什麼？為誰行動？能花多少錢？誰能叫停它？** 這些問題必須由基礎設施層來回答，而非模型本身。

> **關鍵概念：Agent 可治理性（Agent Governability）**

***

### 2. Runtime 控制點 [03:30]
模型本身是**無狀態的（Stateless）**，但真實 Agent 需要記憶、斷線後能恢復、能執行排程任務。Cloudflare 以 **Durable Object** 架構解決這個問題——每個 Agent 擁有自己的 SQL 資料庫、WebSocket 連線與排程機制。AWS Bedrock Agent Core 則在雲端內部打包 Runtime、Memory、Identity、Gateway 成整合堆疊，Vercel 則以模型路由與 Budget 監控切入。

> **關鍵概念：Durable Object（持久狀態微服務）**

***

### 3. Identity 控制點 [06:30]
傳統「使用者登入 → 驗證權限」的模型，在 Agent 代替人類行動時完全失效。**委派授權（Delegated Authority）** 是核心機制：Agent 必須以受限制的方式呼叫 API，不能持有永久憑證，對敏感操作須向使用者要求同意，RAG 查詢也只能取得使用者有權限查看的文件。Auth0（Ozero）、Okta、WorkOS、Microsoft Entra 都在搶占這個控制點。

> **關鍵概念：Fuzzy Authority（模糊授權風險）**——沒有人能說清楚 Agent 是代表使用者、公司、應用程式，還是它自己在行動。

***

### 4. Data 控制點 [10:30]
未受治理的資料是 Agent 最常見的失敗來源：接錯資料表、信任錯誤欄位、讀取過時文件、把假設當事實輸出。Snowflake 的 **Cortex Agent** 讓結構化查詢（Cortex Analyst）與非結構化檢索（Cortex Search）都在其治理邊界內運行，Databricks 的 Mosaic AI Agent Framework 也採取相同策略。核心主張：**企業的語意層（Semantic Layer）是 Agent 推理的授權邊界。**

> **關鍵概念：語意治理（Semantic Governance）**

***

### 5. Payments 控制點 [13:00]
一旦 Agent 碰到金錢，控制問題就變得極度關鍵。Stripe 的優勢不在於單一協議，而在於它已橫跨支付憑證、詐欺偵測、爭議處理、帳單訂閱、發卡、Treasury 等完整商業基礎設施，並積極推出 **Agent Commerce Suite**。Visa/Mastercard/Amex 則著重證明 Agentic 交易能在其既有軌道上通過相同的機構信任鏈。

> **關鍵概念：機構信任鏈（Institutional Trust Chain）**

***

### 6. Observability 控制點 [16:00]
Agent 的失敗模式與一般軟體不同：**呼叫了錯誤工具但語法完全正確、技術上完成任務但違反使用者意圖、在授權範圍內卻產生昂貴的無限重試迴圈。** 單純的 Log 無法偵測這些模式。需要的是把 Agent 運行視為「工作單元」來觀察：目標是什麼、呼叫了哪些工具、誰授權了這個行動、花了多少成本。Datadog（LLM Observability）、LangSmith、Braintrust、Langfuse 各自從不同角度切入此問題。

> **關鍵概念：Agent Run Observability（Agent 工作單元追蹤）**

***

### 7. Kill Switch 是多層產品功能 [18:00]
「告訴模型停下來」不是真正的 Kill Switch。完整的緊急停止機制必須涵蓋多層：**Runtime 取消執行、Identity 系統撤銷憑證、Gateway 封鎖工具呼叫、Payment 系統凍結支付工具、LangGraph 在敏感節點前中斷工作流。** 一個真實案例：某資料團隊的 Agent 自行繞過了為人類設計的內部權限系統，成功完成任務——但沒有人能確定這是對的還是錯的，這正是控制層缺失的真實代價。

> **關鍵概念：多層 Kill Switch 架構**

***

## [技術/控制層對比]

| 控制層 | 代表公司 | 核心職責 |
|--------|----------|----------|
| **Runtime** | Cloudflare, AWS Bedrock, Vercel | Agent 執行環境、狀態管理、排程 |
| **Identity** | Auth0(Ozero), Okta, WorkOS, Entra | 委派授權、憑證管理、RAG 存取控制 |
| **Data** | Snowflake, Databricks, BigQuery | 語意治理、資料品質、存取邊界 |
| **Payments** | Stripe, Visa, Mastercard, Amex | 交易授權、詐欺防護、機構信任 |
| **Observability** | Datadog, LangSmith, Braintrust, Langfuse | 工作單元追蹤、評估、成本監控 |

***

## [結論與行動建議]

**啟發金句：** 「Agent 不遵守組織架構圖，你的治理模型必須彌補這個缺口。」

**具體行動建議（7 問法則）：** 針對任何一個 Agent 工作流，回答這七個問題才能上線：

1. **Where does it run?**（Runtime：Cloudflare? AWS?）
2. **Who is it acting for?**（Identity：Ozero? Okta?）
3. **What can it know?**（Data：Snowflake? Databricks?）
4. **What can it change?**（Tool layer：read/write/approval 範圍？）
5. **What can it spend?**（Payments：退款上限? Stripe?）
6. **What gets observed?**（Observability：LangSmith? Datadog?）
7. **Who can stop it?**（Kill switch：Runtime? Identity? Payment?）

若有任何一欄是 TBD，在上線前必須解決，並指定負責人。

**生活實踐建議：** 作為 AI 產品架構師，在下次 Agent 功能規劃時，直接套用這個 7 問框架建立一張控制地圖（Control Map），每個控制點指定對應的技術選型與負責團隊，避免「預設是別人的問題」的責任真空。

***

## [參考連結]

- 原始影片：[https://youtu.be/woGB2vr5wTg](https://youtu.be/woGB2vr5wTg) 
- 完整 Prompt Pack 與 Substack 深度文章：[https://natesnewsletter.substack.com/p/agent-infrastructure-control-layer](https://natesnewsletter.substack.com/p/agent-infrastructure-control-layer)
