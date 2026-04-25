---
title: 'Claude Code 六大記憶系統全比較：從 Markdown 到雲端大腦'
date: 2026-04-25
image: /images/影片筆記/claude-code-memory-systems-compared.jpeg
category: 影片筆記
tags: [記憶層級, 語義搜索, 記憶宮殿, 知識互聯, 雲端大腦]
description: '這部影片深度解析了 Claude Code 的六個記憶層級，從原生的 Markdown 文件到跨平台的雲端資料庫系統。核心價值在於解決 AI 的「內容腐蝕」（Context Rot）問題，教導如何精準提取跨專案的關鍵決策。'
quote: '記憶系統的價值不在於存儲了多少資訊，而在於 AI 能否在正確的時間，為你提取正確的脈絡。'
action: '先建立精簡的 claude.md，使用超過一週後設定 Hook 自動注入，跨月時安裝 mem-search 語義搜索。'
source_has_timestamps: true
---

## 核心摘要
這部影片深度解析了 Claude Code 的六個記憶層級，從原生的 Markdown 文件到跨平台的雲端資料庫系統。核心價值在於解決 AI 的「內容腐蝕」（Context Rot）問題，教導使用者如何透過結構化管理，讓 AI 在不超載上下文的情況下，精準提取跨專案、跨時間的關鍵決策與知識。

---

## 詳細重點整理

### 1. 層級一：原生 Markdown 記憶系統 [[01:37](http://www.youtube.com/watch?v=UHVFcUzAGlM&t=97)]
* **重點內容**：介紹 `claude.md` 與 `memory.mmd` 的基本用法。`claude.md` 應放置專案規則與風格，而 `memory.mmd` 則是 AI 自動記錄的索引。
* **關鍵概念**：**「避免過載」**。建議 `claude.md` 保持在 200 行以內，過多資訊應存於外部文件並透過索引引用，以防上下文遺忘。

### 2. 層級二：可靠性增強與自動注入 [[06:31](http://www.youtube.com/watch?v=UHVFcUzAGlM&t=391)]
* **重點內容**：透過設定「Session Start Hook」（會話啟動鉤子），在每次開啟終端機時自動將記憶索引注入。
* **關鍵概念**：**「層次化繼承」**。建立全域（Global）、網域（Domain）與專案（Project）三層記憶架構，讓 AI 了解不同層級的背景。

### 3. 層級三：語義搜索與規模化 [[16:56](http://www.youtube.com/watch?v=UHVFcUzAGlM&t=1016)]
* **重點內容**：當文件量變大，關鍵字搜索會失效。此層級引入 `mem-search` 插件，將記憶轉化為「向量（Vectors）」。
* **關鍵概念**：**「語義檢索（RAG）」**。系統會根據使用者的提問意圖，自動提取最相關的前三條記憶片段，解決長文本搜索難題。

### 4. 層級四：逐字稿級別的對話召回 [[24:12](http://www.youtube.com/watch?v=UHVFcUzAGlM&t=1452)]
* **重點內容**：介紹 `MemPalace` 框架，這是一個本地的 RAG 系統，強調「不壓縮、不摘要」，完整保存對話細節。
* **關鍵概念**：**「記憶宮殿架構」**。仿效人類記憶，將資訊存放於「側翼、房間、抽屜」，達成極速且精準的逐字檢索。

### 5. 層級五：互聯知識庫（第二大腦） [[29:08](http://www.youtube.com/watch?v=UHVFcUzAGlM&t=1748)]
* **重點內容**：引用 Andrej Karpathy 的 `LLM Wiki` 概念。區分「原始素材夾」與「AI 維護的 Wiki 夾」，建立深度研究的 Wikipedia。
* **關鍵概念**：**「知識互聯」**。適合需要長期連結不同學科、文章或影片資訊的深度研究者。

### 6. 層級六：跨工具的雲端大腦 [[35:13](http://www.youtube.com/watch?v=UHVFcUzAGlM&t=2113)]
* **重點內容**：介紹 `Open Brain` 或 `Mem0`。將記憶存放在雲端資料庫（如 Supabase），讓 ChatGPT、Claude 與 Cursor 共享同一個記憶。
* **關鍵概念**：**「平台中立性」**。讓記憶不再鎖定在特定設備或工具，達成真正具備連續性的 AI 協作。

---

## 結論與行動建議

* **啟發金句**：**「記憶系統的價值不在於存儲了多少資訊，而在於 AI 能否在正確的時間，為你提取正確的脈絡。」**
* **具體行動建議：1-2-3 實踐法則**
    * **Level 1**：花 10 分鐘建立精簡的 `claude.md`，定義核心風格。
    * **Level 2**：若使用超過一週，設定 Hook 自動注入記憶索引。
    * **Level 3**：當專案跨月且細節過多時，安裝 `mem-search` 進行語義檢索。
* **生活實踐建議**：
    * **建立錨點**：每週末執行一次「記憶整理（Reorganize Memory）」指令，讓 AI 刪除重複與過期的資訊。
    * **觀察日記**：記錄 AI 哪次回答「忘記了先前約定」，這就是你該升級記憶層級的訊號。

影片連結：[http://www.youtube.com/watch?v=UHVFcUzAGlM](http://www.youtube.com/watch?v=UHVFcUzAGlM)
