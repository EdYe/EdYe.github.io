---
title: '現代架構101：簡單即是最好的架構'
date: 2026-03-08
image: /images/影片筆記/modern-architecture-101.png
category: 影片筆記
tags: [架構師, API設計, CQRS, 快取, 訊息佇列]
description: '由 Jerry Nixon 在 NDC Copenhagen 2025 演講，逐步構建現代化軟體架構並解釋每個組件的存在理由，核心理念是「簡單即是最好的架構」。'
quote: '簡單即是最好的架構。'
action: '延遲決策，根據需求選擇合適的組件，不在專案初期堆疊所有技術。'
source_has_timestamps: true
source_raw: 現代架構101
---

這部影片是由 Jerry Nixon 在 NDC Copenhagen 2025 發表的演講，主題為**「現代架構 101：給新工程師與健忘專家的指南」 (Modern Architecture 101 for New Engineers & Forgetful Experts)**。

講者以深入淺出的方式，逐步構建一個現代化的軟體架構，並解釋了每個組件存在的理由。核心理念是**「簡單即是最好的架構」(Simplicity is the best architecture)**。

以下是影片的重點摘要：

### **1. 架構師的角色 [[09:04](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=544)]**

* 架構師是負責做出「最昂貴決定」的人，也就是那些日後最難以更改的決定。
* 架構師的主要工作往往是說「不」，或者是「晚點再做」，以防止解決方案變得過於複雜。
* 目標是成為「簡單性」的守護者。

### **2. 基礎架構演進：從客戶端到 API [[16:33](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=993)]**

* **資料庫分離**：應用程式（Client）不應直接連線資料庫，這樣會導致架構耦合且難以維護。
* **引入 API**：在 Client 和資料庫之間加入 API 層，可以解決資料庫驅動程式版本更新的問題，並隱藏資料庫細節。
* **API 管理 (APIM/Gateway) [[28:45](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=1725)]**：強烈建議在 Client 和 API 之間加入 APIM。雖然初期增加工作量，但對於未來的 API 版本控管 (Versioning)、負載平衡和安全性至關重要。

### **3. 效能與擴展性設計**

* **讀寫分離 (CQRS pattern) [[20:48](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=1248)]**：
* 將「寫入」和「讀取」的操作分開。
* **唯讀副本 (Read Replica)**：寫入主資料庫，資料會同步到唯讀副本。這樣讀取操作不會影響寫入效能。
* **最終一致性 (Eventual Consistency)**：接受資料同步會有微小的延遲，換取極大的效能提升。


* **快取 (Caching) [[32:05](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=1925)]**：
* **Level 1 Cache**：記憶體內快取，速度最快。
* **Level 2 Cache**：分散式快取 (如 Redis)。
* **觀念**：只要給資料 1 秒鐘的快取，就能大幅減少資料庫負載，提升 API 吞吐量。


* **靜態內容與 CDN [[44:01](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=2641)]**：靜態資源應透過 CDN (內容傳遞網路) 發送，讓資料更靠近使用者，提升載入速度。

### **4. 彈性與非同步處理**

* **服務匯流排 (Service Bus) [[25:38](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=1538)]**：用於微服務之間的溝通，解耦系統。就像郵差一樣傳遞訊息，並處理「死信 (Dead Letter)」。
* **重試策略 (Retry Policy) [[35:25](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=2125)]**：應對網路瞬斷等暫時性故障，自動重試請求。
* **佇列 (Queue) [[36:24](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=2184)]**：當請求量超過資料庫處理能力時，將請求放入佇列排隊。這能讓使用者先得到回應 (如「已接收」)，後端再慢慢處理，提升使用者體驗。
* **事件中樞 (Event Hub) [[39:44](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=2384)]**：用於大量資料的攝取 (Ingestion) 和事件回應，可觸發 Serverless Function 來處理業務邏輯。

### **5. 資料庫優化技術 [[45:53](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=2753)]**

講者介紹了幾種 SQL Server (及其他資料庫) 的進階功能：

* **Column Store (列存儲)**：將資料垂直存儲，對於聚合查詢 (Aggregates) 速度可快 100 倍，且壓縮率高。
* **No-Index Table (Heap)**：沒有主鍵索引的表，寫入速度極快，但沒有排序保證，使用需謹慎。
* **In-Memory Tables**：將資料表放在記憶體中，讀寫速度極快。
* **Graph Database**：處理複雜關係 (如物流路徑) 時比傳統關聯式查詢更高效。

### **6. 安全性與結論**

* **安全性 [[58:01](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=3481)]**：提到了使用 Microsoft Entra ID (前 Azure AD) 和 JWT token 進行身分驗證，建議在應用層重新生成包含細粒度權限的 token。
* **最終建議 [[01:00:55](http://www.youtube.com/watch?v=WRg13Ze_UpY&t=3655)]**：**延遲決策 (Defer decisions)**。不需在專案開始時決定所有細節，將決策推遲到最後一刻可以保持靈活性並減少錯誤決策的成本。

這場演講強調，現代架構不是堆疊所有技術，而是根據需求選擇合適的組件，並始終保持架構的簡單與可維護性。

相關影片連結：

* [Modern Architecture 101 for New Engineers & Forgetful Experts](https://www.youtube.com/watch?v=WRg13Ze_UpY)
