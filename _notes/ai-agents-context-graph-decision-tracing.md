---
title: 'AI代理決策追蹤與上下文圖譜'
date: 2026-03-31
image: /images/影片筆記/ai-agents-context-graph-decision-tracing.jpeg
category: 影片筆記
tags: [上下文圖譜, 決策追蹤, 知識管理, 圖形資料庫, AI代理]
description: '探討如何利用圖形資料庫補足AI代理缺失的決策追蹤能力，將企業內破碎的數據轉化為結構化的決策路徑，提升AI的可解釋性與執行效率'
quote: '你無法管理你不理解的事物，而你無法理解你未曾記錄的事物。'
action: '為AI代理同時配置短期、長期與推理記憶層，使用POLE+O模型進行數據建模'
source_has_timestamps: true
---

## 核心摘要
本影片為首屆「上下文圖譜（Context Graph）」研發者會議，深入探討如何利用圖形資料庫（如 Neo4j）補足 AI 代理（Agents）缺失的「決策追蹤」能力。核心價值在於將企業內破碎的數據轉化為結構化的決策路徑，提升 AI 的可解釋性與執行效率，從而解決 AI 專案難以落地生產環境的痛點。

---

## 詳細重點整理

### 1. 上下文圖譜的核心定義與價值 [[03:00](http://www.youtube.com/watch?v=868UYyKwe-E&t=180)]
* **定義**：上下文圖譜不僅是知識圖譜，它包含了組織內做出決策所需的所有資訊（Why），包括政策、前例與邏輯。
* **解決痛點**：目前的系統（如 Salesforce, SAP）僅記錄「結果」，而缺失了「決策過程」。
* **關鍵概念**：**缺失的為什麼（The Missing Why）**。透過記錄決策追蹤（Decision Tracing），讓 AI 代理能根據過去的邏輯做出具備一致性的判斷。

### 2. 金融服務業的應用演示 [[04:35](http://www.youtube.com/watch?v=868UYyKwe-E&t=275)]
* **應用場景**：以信用卡額度審核為例。
* **技術路徑**：代理調用工具檢索圖譜中的客戶歷史、詐欺標記與信用政策 [[07:11](http://www.youtube.com/watch?v=868UYyKwe-E&t=431)]。
* **混合搜索**：結合向量搜索（語義相關）與圖形嵌入（結構相關，如 FastRP 算法）來尋找最相關的前例 [[08:58](http://www.youtube.com/watch?v=868UYyKwe-E&t=538)]。
* **關鍵概念**：**因果決策鏈（Causal Chains）**。將決策節點存回圖譜，成為未來的判斷基礎。

### 3. 三層記憶架構：Short, Long, and Reasoning [[11:58](http://www.youtube.com/watch?v=868UYyKwe-E&t=718)]
* **短期記憶**：對話工作狀態（Session State）。
* **長期記憶**：透過實體提取（Entity Extraction）將非結構化對話轉為圖譜中的事實節點 [[12:05](http://www.youtube.com/watch?v=868UYyKwe-E&t=725)]。
* **推理記憶**：記錄工具調用軌跡與決策步驟。
* **關鍵概念**：**推理追蹤（Reasoning Traces）**。這是目前大多數 AI 框架中缺失的部分，卻是建立上下文圖譜的關鍵。

### 4. 知識管理與本體論（Ontology）的重要性 [[29:00](http://www.youtube.com/watch?v=868UYyKwe-E&t=1740)]
* **觀點挑戰**：專家 Jessica Talisman 提出，這不只是工程問題，而是**知識管理問題**。
* **層級劃分**：分為策略（為什麼做）、戰術（瓶頸與優化）與執行（作業面）三層 [[32:24](http://www.youtube.com/watch?v=868UYyKwe-E&t=1944)]。
* **關鍵轉化**：默會知識（Tacit Knowledge）在被記錄後轉化為程序性知識（Procedural Knowledge） [[36:18](http://www.youtube.com/watch?v=868UYyKwe-E&t=2178)]。
* **關鍵概念**：**本體導向（Ontology-driven）**。在建立資料庫前，必須先定義何謂「決策」、實體與規則。

### 5. 自動化構建與驗證機制 [[01:14:19](http://www.youtube.com/watch?v=868UYyKwe-E&t=4459)]
* **自動化挑戰**：如何處理跨數據源的名稱衝突（如不同的營收定義）。
* **評估框架**：建立圖譜後，需透過大量測試（Evals）驗證其對代理執行效果的提升 [[01:20:42](http://www.youtube.com/watch?v=868UYyKwe-E&t=4842)]。
* **關鍵概念**：**確定性執行（Deterministic Execution）**。利用圖譜建立護欄（Guardrails），而非僅依賴提示詞（Prompt）祈禱 AI 不出錯。

---

## 結論與行動建議

* **啟發金句**：**「你無法管理你不理解的事物，而你無法理解你未曾記錄的事物。」** [[42:40](http://www.youtube.com/watch?v=868UYyKwe-E&t=2560)]
* **具體行動建議：3-5-4 決策落地法**
    1. **3 層記憶並行**：為你的 AI 代理同時配置短期（會話）、長期（事實）與推理（過程）記憶層。
    2. **5 類實體提取**：使用 POLE+O 模型（人、組織、位置、事件 + 對象）進行初步的數據建模。
    3. **4 個檢視步驟**：
        - 承認這是知識管理問題。
        - 建立知識獲取基礎設施（如瀏覽器外掛記錄專家操作）。
        - **先建模，再持久化**（先寫 Schema/Ontology，再進資料庫）。
        - 將「知識捕捉」設為開發的首要目標。
* **生活實踐建議**：
    * **觀察紀錄**：在日常工作中，嘗試將「我為何做這個決定」記錄下來，而非只記錄「我做了什麼」。
    * **工具建議**：開發者可嘗試 `neo4j-agent-memory` Python 套件，快速為現有代理添加圖形記憶層 [[10:45](http://www.youtube.com/watch?v=868UYyKwe-E&t=645)]。

[影片連結](http://www.youtube.com/watch?v=868UYyKwe-E)
