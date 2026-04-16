---
title: 'Graphify：將資料夾轉為 AI 知識圖譜的開源工具'
date: 2026-04-17
image: /images/AI筆記/graphify-knowledge-graph-intro.jpeg
category: AI筆記
tags: [Graphify, 知識圖譜, Treesitter, 本地優先, 多模態]
description: '介紹開源工具 Graphify，能將資料夾轉化為可查詢知識圖譜，透過三階段管線減少 71 倍 Token 使用量並保護本地隱私。'
quote: 'Graphify 將混亂的資料夾轉化為連貫的智慧圖譜，讓 AI 不再只是讀取程式碼，而是真正理解系統的脈絡。'
action: '1-3-7 守則：pip install graphify、三階段全掃描、找出 7 個上帝節點重構。'
source_has_timestamps: true
---

## 核心摘要
這段影片介紹了開源工具 **Graphify**，這是一款能將任何包含程式碼、文件、圖像及影音的資料夾，轉化為「可查詢知識圖譜」的 AI 工具。它透過大幅減少 71 倍的 Token 使用量，並結合本地端隱私處理，讓開發者能以極高效率與低成本，讓 AI 深度理解複雜專案的架構與關聯。

---

## 詳細重點整理
### 1. Graphify 的核心功能與多模態處理 [[00:26](http://www.youtube.com/watch?v=eYHpKFfhK2A&t=26)]
* Graphify 不僅是程式碼索引器，它支援多達 22 種程式語言，並能處理 PDF、Markdown、圖像甚至透過 Whisper 本地轉錄影音文件。
* **關鍵概念**：**多模態知識連接**。它能顯示函數調用、文件與實作的關係，以及跨檔案的架構邊界。

### 2. 三階段處理管線 (Three-Pass Pipeline) [[02:29](http://www.youtube.com/watch?v=eYHpKFfhK2A&t=149)]
* **第一階段：確定性提取** [[02:37](http://www.youtube.com/watch?v=eYHpKFfhK2A&t=157)]：使用 Treesitter 解析程式碼，提取函數與類別。此過程完全在本地端完成，不涉及 LLM，保證隱私且準確。
* **第二階段：影音轉錄** [[02:57](http://www.youtube.com/watch?v=eYHpKFfhK2A&t=177)]：利用本地端的 Faster Whisper 轉錄影音，並結合專案詞彙庫以確保專業術語的準確性。
* **第三階段：語義提取** [[03:16](http://www.youtube.com/watch?v=eYHpKFfhK2A&t=196)]：利用 LLM 提取文件與圖像中的語義關係，捕捉 AOT 解析無法發現的設計決策。
* **關鍵概念**：**本地優先與分層理解**。將結構、時間與語義訊息層層堆疊，構建完整的知識圖譜。

### 3. 三大輸出產物與架構洞察 [[03:48](http://www.youtube.com/watch?v=eYHpKFfhK2A&t=228)]
* **可視化圖譜 (graph.html)**：使用 Vis.js 渲染，可縮放、過濾並觀察社群集群。
* **圖譜報告 (graph.report)**：識別具有過多連接的「上帝節點」(God Nodes)，並給出架構建議，如同資深工程師的程式碼審查。
* **資料持久化 (graph.json)**：儲存所有節點與邊，支持各種查詢。
* **關鍵概念**：**結構化洞察**。幫助用戶快速識別複雜系統中的潛在問題。

### 4. 安裝、配置與隱私保護 [[04:52](http://www.youtube.com/watch?v=eYHpKFfhK2A&t=292)]
* 安裝簡易，僅需 `pip install graphify`。支援 Cursor、GitHub Copilot、Claude Code 等 11 種 AI 助手。
* 具備「增量處理」與「監視模式」(Watch Mode)，僅分析變動的文件。
* **關鍵概念**：**隱私保障模型**。核心程式碼保持本地處理，僅非敏感的文件語義提取才調用 API。

---

## 結論與行動建議
* **啟發金句**：「Graphify 將混亂的資料夾轉化為連貫的智慧圖譜，讓 AI 不再只是讀取程式碼，而是真正理解系統的脈絡。」
* **具體行動建議（1-3-7 快速上手守則）**：
    * **1 次安裝**：執行 `pip install graphify` 並完成助手配置。
    * **3 階段分析**：對現有的複雜專案進行一次全掃描，生成知識圖譜。
    * **7 倍效能**：利用生成的 `graph.report` 找出專案中最混亂的 7 個「上帝節點」並嘗試重構。
* **生活實踐建議**：
    * **建立技術錨點**：在進入新專案（Onboarding）時，優先使用 Graphify 生成報告，縮短摸索期。
    * **觀察日記**：定期使用 `watch` 模式監控圖譜變化，觀察隨著開發進行，系統耦合度是否過高。
    * **工具搭配**：將 Graphify 與 Cursor 配合使用，利用其減少 Token 的特性，實現更精準、更低成本的 AI 對話。

影片連結：[https://www.youtube.com/watch?v=eYHpKFfhK2A](https://www.youtube.com/watch?v=eYHpKFfhK2A)
