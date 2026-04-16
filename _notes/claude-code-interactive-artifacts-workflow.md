---
title: 'Claude Code 互動式 Artifacts 工作流三層進階應用'
date: 2026-04-17
image: /images/AI筆記/claude-code-interactive-artifacts-workflow.jpeg
category: AI筆記
tags: [Claude Code, Artifacts, Bun 熱重載, MCP 伺服器, Agentic 工作流]
description: '深入解析 Anthropic 工程師愛用的 Claude Code 工作流，從靜態 Artifacts、Bun 熱重載到 Channels 數據儀表板三層進階應用。'
quote: '最好的工具是你能在使用它的同時，也正在構建它。'
action: '3-L 遞進法則：先用 Artifact 跑多種風格、再架 Bun 熱重載、最後以 MCP + Channels 建互動儀表板。'
source_has_timestamps: true
---

## 核心摘要
這段影片深入解析了 Anthropic 工程師也愛用的 Claude Code 工作流，核心圍繞著「互動式 Artifacts (Artifacts)」的進階運用。透過將 Claude 從簡單的對話框轉化為可互動的儀表板與設計工具，大幅提升了開發、設計與數據分析的效率，縮短了從「概念構思」到「具體執行」的距離。

---

## 詳細重點整理

### 1. 第一層：靜態 Artifacts (Static Artifacts) [[00:15](http://www.youtube.com/watch?v=ASAaKhK1B5w&t=15)]
* **重點內容說明**：利用 Claude 生成單一 HTML 檔案來進行快速原型開發或設計發想。這對於「我看到才知道我要什麼」的視覺化需求非常有效。
* **應用場景**：設計 UI 變體（如製作 10 種不同的設置頁面樣式）、模擬 LinkedIn 貼文預覽。
* **關鍵概念**：**快速視覺化探索**。將複雜組件抽離，在獨立環境中快速迭代，選定後再放回主程式碼。

### 2. 第二層：互動式 Artifacts 與 Bun 伺服器 [[03:43](http://www.youtube.com/watch?v=ASAaKhK1B5w&t=223)]
* **重點內容說明**：透過 Bun 建立輕量化本地伺服器，實現 HTML Artifact 的「熱重載 (Hot Reload)」。
* **功能升級**：在 HTML 中加入「評論」功能，用戶點擊畫面即可留下回饋，並透過導出的 JSON 回傳給 Claude 進行修正。
* **學習輔助**：製作互動式教學工具（如解釋資料庫安全性 RLS 或 PG Bouncer 原理），透過點擊動畫加深理解。
* **關鍵概念**：**反饋閉環 (Feedback Loop)**。讓 AI 生成的東西不再是靜態文件，而是可以互動並修正的活工具。

### 3. 第三層：Claude Code Channels 進階數據工作流 [[06:28](http://www.youtube.com/watch?v=ASAaKhK1B5w&t=388)]
* **重點內容說明**：這也是 Anthropic 工程師使用的核心技巧，利用 `Channels` 功能讓本地 Artifact 直接與 Claude Code 後端通訊。
* **自動化整合**：連接 MCP 伺服器（如 Stripe 或 PostHog），讓 Claude 直接抓取真實數據並渲染成動態儀表板。
* **實例應用**：建立一個可以監控用戶行為的自定義後台，直接在儀表板上點擊「修正 UI」或「調整數據顯示」，Claude 會在後台自動執行指令並更新畫面。
* **關鍵概念**：**無縫 Agentic 工作流**。將 UI 當作與 AI 溝通的介面，實現「在工具中修改工具」。

---

## 結論與行動建議

* **啟發金句**：**「最好的工具是你能在使用它的同時，也正在構建它。」** (It becomes much easier to switch between actually using the tool and building the tool.)

* **具體行動建議：3-L 遞進法則**
    1. **Level 1 (初階)**：下次寫程式或設計時，要求 Claude 先產出一個 `index.html` 的 Artifact 進行 5-10 種風格測試，而非直接改主代碼。
    2. **Level 2 (中階)**：安裝 **Bun** 環境，嘗試讓 Claude 生成一個帶有「熱重載」功能的本地預覽頁面。
    3. **Level 3 (高階)**：學習使用 **MCP 伺服器** (Model Context Protocol) 連結外部數據（如 GitHub 或數據庫），並嘗試使用 `channels` 功能建立互動式管理介面。

* **生活實踐建議**：
    * **建立「視覺化」錨點**：不再滿足於純文字溝通，當遇到複雜邏輯或設計抉擇時，強制自己啟動「Artifact 模式」，要求 Claude 用圖表或 UI 呈現。
    * **觀察日記**：紀錄使用互動式 Artifact 後，從「提出回饋」到「看到成品修正」的時間縮短了多少，體會 AI 作為「即時執行者」的力量。

---
**相關影片連結**：[Watch on YouTube](http://www.youtube.com/watch?v=ASAaKhK1B5w)
