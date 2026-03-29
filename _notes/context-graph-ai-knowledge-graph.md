---
title: 'Context Graph：AI的脈絡圖譜'
date: 2026-03-29
image: /images/影片筆記/context-graph-ai-knowledge-graph.jpg
category: 影片筆記
tags: [Context Graph, 知識圖譜, RDF, 語義消歧, 本體論]
description: 'Context Graph是專為AI優化的知識圖譜結構，透過結構化的語義關聯，解決大型語言模型在處理大規模數據時的歧義性與脈絡流失問題'
quote: 'Context Graph本質上是為AI優化的圖譜，它不只是餵給LLM的資料，而是一種讓機器理解世界脈絡的基礎設施。'
action: '在處理複雜文件時，應結合圖譜技術解決代名詞與脈絡遺失問題，並善用現有行業標準的本體論'
source_has_timestamps: true
---

這部影片由 TrustGraph 的共同創辦人 Daniel Davis 主講，深入探討了 **Context Graph（上下文圖譜）** 的定義、歷史背景及其在 AI 時代的重要性，強調這並非全新發明，而是知識圖譜（Knowledge Graph）技術的進化應用。

### 核心摘要
**Context Graph 是專為 AI 優化的知識圖譜結構，透過結構化的語義關聯（如 RDF 或屬性圖），解決大型語言模型（LLM）在處理大規模數據時的歧義性與脈絡流失問題。**

---

### 詳細重點整理

#### 1. 知識圖譜並非新技術，而已具規模化應用 [[01:09](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=69)]
* **長期存在的應用：** 知識圖譜技術早已在信用卡詐欺檢測（毫秒級查詢）、石油與天然氣工業、醫療研究等領域大規模運行多年。
* **搜尋引擎基礎：** 如 Google 搜尋背後使用的 `schema.org` 本質上就是一種本體論（Ontology），用來結構化網頁資訊。
* **圖譜結構：** 核心在於「主體-謂詞-客體」（Subject-Predicate-Object）的三元組結構，這是資訊交換的理想方式。

#### 2. 屬性圖 (Property Graphs) vs. RDF 生態系統 [[04:57](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=297)]
* **屬性圖 (以 Neo4j 為代表)：** 側重於為特定用途結構化數據。允許在主體或客體上附加屬性（如：年齡、最後訪問時間），適合處理大規模元數據。 [[05:34](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=334)]
* **RDF 生態系統：** 較為複雜且語法敏感（如 Turtle, JSON-LD），旨在移除原位脈絡的同時保留其含義。
* **消除歧義的重要性：** 影片舉例「Fred 是隻貓」與「Fred 有四條腿」，若無圖譜連結，機器可能誤認 Fred 是一張桌子。 [[10:46](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=646)]

#### 3. 解決 AI 的「脈絡流失」與「歧義性」 [[12:13](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=733)]
* **從 POC 到生產的瓶頸：** 許多 AI 演示在小數據集表現良好，但在企業級大規模數據上失效，主因是單純的「文本塊（Text Chunking）」會遺失代名詞（他、她、它）所指代的對象。 [[13:21](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=801)]
* **Context Graph 的介入：** 透過圖譜連接，AI 能知道某段文字屬於哪一章、哪一頁、指代哪個角色，從而檢索出包含完整脈絡的子圖（Subgraph）。 [[15:41](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=941)]
* **否定「絕對真理」：** 提出觀察結果受環境影響（如：天空在地球是藍的，在火星則不然）。Context Graph 能記錄這些觀察的靜態性與時效性（Freshness）。 [[18:07](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=1087)]

#### 4. 圖譜分析與 LLM 的結構化呈現 [[24:42](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=1482)]
* **成熟的算法：** 利用已存在數十年的算法進行「社群偵測」、「路徑尋找」與「異常檢測」（Anomaly Detection），這在資安與防詐騙中至關重要。
* **LLM 更擅長機器可讀格式：** 實驗發現，將檢索到的子圖以結構化格式（如 Triples）提供給 LLM，效果優於純文字或簡單的列表。 [[29:41](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=1781)]
* **結構即資訊：** 就像程式碼（Coding）具有強大模式，結構本身就向 LLM 傳達了額外的邏輯資訊。 [[31:08](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=1868)]

#### 5. 本體論 (Ontologies) 不需要重新發明輪子 [[32:38](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=1958)]
* **現成的標準：** 世界上已有成千上萬個成熟的本體論（如醫療、金融 FIBO、甚至 BBC 的食譜標準）。
* **無需從零開始：** 開發 Context Graph 時應善用現有標準，僅需針對 AI 優化進行微調，而非盲目自創。 [[35:01](http://www.youtube.com/watch?v=gZjlt5WcWB4&t=2101)]

---

### 結論與行動建議
* **核心啟發：** 「Context Graph 本質上是為 AI 優化的圖譜（AI Optimized Graph）。」它不只是餵給 LLM 的資料，而是一種讓機器理解世界脈絡的基礎設施。
* **具體建議：**
    * **不要只依賴向量嵌入（Vector Embeddings）：** 在處理複雜文件或大規模數據時，應結合圖譜技術解決代名詞與脈絡遺失問題。
    * **善用現有本體論：** 在建立系統前，先搜尋該領域是否已有行業標準的本體論可供使用，避免重複造輪子。
    * **關注結構化輸出：** 嘗試以更結構化的方式（如三元組）與 LLM 互動，這能顯著提升模型的理解準確率。