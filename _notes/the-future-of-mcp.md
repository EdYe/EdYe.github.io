---
title: 'MCP 未來藍圖：打造全方位連通的 AI 代理'
date: 2026-04-20
image: /images/AI筆記/the-future-of-mcp.jpeg
category: AI筆記
tags: [MCP協議, 連通性, 漸進式發現, 語義對齊, 代理人]
description: '這段影片由 Anthropic 的 David Soria Parra 深入探討了模型上下文協議（MCP）的未來發展。核心價值在於將 AI 從單純的對話模型轉化'
quote: '2026 年是關於連通性的一年，最優秀的代理人將靈活運用每一種可用工具，而非僅侷限於單一方法。'
action: '學習 Skills、MCP 與 CLI 三種技術，以「是否方便代理人理解」為首要 MCP 伺服器設計原則'
source_has_timestamps: true
---

## 核心摘要
這段影片由 Anthropic 的 David Soria Parra 深入探討了模型上下文協議（MCP）的未來發展。核心價值在於將 AI 從單純的對話模型轉化為具有強大「連通性」的代理人（Agents），透過 MCP 協議，讓 AI 代理能無縫串接各類應用程式與企業數據，實現真正的生產力自動化與更豐富的互動體驗。

---

## 詳細重點整理

### 1. MCP 的核心優勢與演進 [[00:50](http://www.youtube.com/watch?v=v3Fr2JR47KA&t=50)]
* MCP 讓伺服器能同時傳遞應用程式介面與工具，讓人類與模型能同步協作。
* **關鍵概念**：**語義對齊**。客戶端與伺服器端必須能理解彼此的對話內容，而不僅僅是資料傳輸。

### 2. 2026 年的代理人藍圖：全方位連通性 [[03:53](http://www.youtube.com/watch?v=v3Fr2JR47KA&t=233)]
* AI 代理將從實驗室的展示品轉向實際的生產環境，特別是針對財務分析、市場行銷等知識型工作者。
* **關鍵概念**：**連通性技術棧**。2026 年的代理人將結合 Skills、MCP 與 CLI/電腦使用（Computer Use）三種技術來完成複雜任務。

### 3. 優化代理人效能的兩大模式 [[08:11](http://www.youtube.com/watch?v=v3Fr2JR47KA&t=491)]
* **漸進式發現 (Progressive Discovery)**：避免將所有工具一次塞入上下文，而是讓模型在需要時才「尋找」並載入工具。
* **程式化工具調用 (Programmatic Tool Calling)**：讓模型撰寫指令碼一次執行多個任務，而非一步步對話，減少延遲與 Token 消耗。
* **關鍵概念**：**上下文減重**。透過動態加載工具，可大幅減少 50% 以上的上下文佔用 [[09:22](http://www.youtube.com/watch?v=v3Fr2JR47KA&t=562)]。

### 4. 針對代理人重新設計 API [[12:05](http://www.youtube.com/watch?v=v3Fr2JR47KA&t=725)]
* 停止直接將 REST API 轉換為 MCP，應根據代理人的「思維方式」來設計介面。
* **關鍵概念**：**伺服器端編排**。在伺服器端提供執行環境，讓模型能進行更強大的邏輯組合。

### 5. MCP 協議的未來路線圖 [[13:43](http://www.youtube.com/watch?v=v3Fr2JR47KA&t=823)]
* 預計 2026 年 6 月推出無狀態傳輸協議，簡化雲端部署。
* 推送「自動發現」功能，讓代理人能直接從網站 URL 找到對應的 MCP 伺服器。
* **關鍵概念**：**生態系標準化**。透過開源社群力量，建立跨平台的 AI 溝通標準。

---

## 結論與行動建議

* **啟發金句**：**「2026 年是關於連通性的一年，最優秀的代理人將靈活運用每一種可用工具，而非僅侷限於單一方法。」**
* **具體行動建議：3-2-1 整合法則**
    * **3 種技術儲備**：了解並學習 Skills、MCP 與 CLI 三者的應用場景。
    * **2 個優化方向**：檢查你的 AI 應用是否實現了「漸進式發現」與「程式化調用」來節省成本。
    * **1 個設計原則**：開發 MCP 伺服器時，請以「這是否方便代理人理解」為首要準則。
* **生活實踐建議**：
    * **工具觀察**：觀察日常工作中哪些 SAS 軟體（如 Notion, Slack）已有 MCP 整合，嘗試配置並體驗 AI 代理如何簡化你的工作流。
    * **建立錨點**：關注 Anthropic 的 MCP 官方 Discord 或 GitHub，追蹤 6 月即將發布的 SDK V2 更新，確保開發環境處於最新標準。

影片連結：[https://www.youtube.com/watch?v=v3Fr2JR47KA](https://www.youtube.com/watch?v=v3Fr2JR47KA)
