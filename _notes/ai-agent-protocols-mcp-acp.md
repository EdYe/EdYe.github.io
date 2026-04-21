---
title: 'AI 代理協議：MCP 與 ACP 的互補關係解析'
date: 2026-04-22
image: /images/AI筆記/ai-agent-protocols-mcp-acp.jpeg
category: AI筆記
tags: [MCP, ACP, AI代理協議, 使用者體驗, AI原生桌面]
description: '本影片深入解析了 AI 開發中的兩大關鍵協議：MCP（模型上下文協議）與 ACP（代理客戶端協議），展示了如何將繁瑣的終端機指令轉化為直觀的圖形介面。'
quote: 'ACP 與 MCP 的結合，正在為未來代理化工作（Agentic Work）奠定穩固的基石。'
action: '到 ACP 代理註冊表探索目前已支援的代理工具，嘗試在終端機與 UI 工具中分別執行同一任務感受差異。'
source_has_timestamps: true
---

## 核心摘要
本影片深入解析了 AI 開發中的兩大關鍵協議：**MCP（模型上下文協議）**與 **ACP（代理客戶端協議）**。透過實戰演示將 ACP 整合進「Orchestrate」應用程式的過程，展示了如何將繁瑣的終端機指令轉化為直觀的圖形介面，讓非技術使用者也能駕馭強大的 AI 代理工具，進而開啟 AI 原生桌面應用的新時代。

---

## 詳細重點整理

### 1. 釐清核心概念：MCP vs. ACP [[01:07](http://www.youtube.com/watch?v=P8OL_0ag4pk&t=67)]
* **MCP (Model Context Protocol)**：充當代理（如 Claude Code）與工具（如 Notion, Slack）之間的橋樑，主要負責提供「上下文」資訊，讓 AI 了解並操作日常軟體。
* **ACP (Agent Client Protocol)**：定義應用程式（客戶端）如何與運行在終端機的代理溝通。它解決了終端機介面難以使用的痛點，將 AI 能力引導至前端 UI。
* **關鍵概念**：兩者並非競爭關係，而是**互補關係**；MCP 負責「能力連結」，ACP 負責「介面互動」。

### 2. 為什麼我們需要 ACP？ [[02:22](http://www.youtube.com/watch?v=P8OL_0ag4pk&t=142)]
* 目前大多數 AI 代理運行在終端機（Terminal），雖然強大但對一般使用者來說門檻高且體驗不佳。
* ACP 允許開發者建立客製化的串流介面，讓使用者在熟悉的視窗中管理多個代理，無需在多個終端機分頁間跳轉。
* **關鍵概念**：**UX（使用者體驗）的升級**是 AI 普及化的最後一哩路，ACP 讓 AI 從黑盒子轉向可視化。

### 3. 實戰整合流程：從計畫到除錯 [[10:45](http://www.youtube.com/watch?v=P8OL_0ag4pk&t=645)]
* **階段化計畫**：利用 AI 代理（如 Claude Code）生成詳細的整合步驟，包含類型定義、會話管理、前端渲染及事件處理。
* **動態除錯**：演示了即使是非技術人員，也能透過將報錯資訊回饋給 AI，引導其修正程式碼包名錯誤或參數失效等問題 [[19:51](http://www.youtube.com/watch?v=P8OL_0ag4pk&t=1191)]。
* **介面優化**：參考成熟產品（如 T3 Code）的 UI 配置，實踐懸浮式訊息輸入框、模型選擇器與分支管理功能 [[27:30](http://www.youtube.com/watch?v=P8OL_0ag4pk&t=1650)]。
* **關鍵概念**：**「引導式開發」**——使用者不再是單純寫程式，而是作為「產品經理」與 AI 協作。

### 4. 未來的機會：AI 原生桌面應用 [[33:44](http://www.youtube.com/watch?v=P8OL_0ag4pk&t=2024)]
* 隨著 ACP 的成熟，將會出現大量「AI First」的桌面軟體（例如：整合 AI 代理的 Photoshop 或畫布設計工具）。
* 傳統老牌軟體反應較慢，這為創業者提供了利用 ACP 重新定義工作流程的龐大市場機會。
* **關鍵概念**：**「去終端化」**將釋放 AI 的生產力，讓非開發者也能建立複雜的數位資產。

---

## 結論與行動建議

* **啟發金句**：**「ACP 與 MCP 的結合，正在為未來代理化工作（Agentic Work）奠定穩固的基石。」** [[05:20](http://www.youtube.com/watch?v=P8OL_0ag4pk&t=320)]
* **具體行動建議（3-2-1 法則）**：
    * **3 種探索**：到 ACP 代理註冊表（Registry）探索目前已支援的 3 個代理工具（如 Claude Code, Gemini CLI, Codeex）。
    * **2 個對比**：嘗試在「終端機」與「具備 UI 的工具」中分別執行同一個任務，感受 ACP 帶來的操作直覺性差異。
    * **1 個嘗試**：如果你有開發構想，嘗試使用現成的 SDK（如 agent-client-protocol SDK）建立一個簡單的對話封裝。
* **生活實踐建議**：
    * **建立「自動化觀測紀錄」**：紀錄你在日常工作中哪些流程仍在使用繁瑣的終端指令，評估是否能透過 ACP 協議將其轉化為更易用的圖形化小工具。

影片連結：[https://www.youtube.com/watch?v=P8OL_0ag4pk](https://www.youtube.com/watch?v=P8OL_0ag4pk)
