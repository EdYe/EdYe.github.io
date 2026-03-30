---
title: 'AI研究工作流：三大工具整合'
date: 2026-03-30
image: /images/影片筆記/ai-research-workflow-claude-notebooklm-obsidian.jpeg
category: 影片筆記
tags: [Claude Code, NotebookLM, Obsidian, 技能創建, 自動化研究]
description: '本影片展示了如何將 Claude Code、NotebookLM 與 Obsidian 三大工具結合，構建一套「上帝模式」的自動化研究工作流'
quote: '真正強大的不是工具本身，而是你如何將它們串聯成一套能自我優化的閉環系統。'
action: '安裝Claude Code、NotebookLM-PI與Obsidian，建立第一個資料抓取技能'
source_has_timestamps: true
---

## 核心摘要
本影片展示了如何將 **Claude Code**、**NotebookLM** 與 **Obsidian** 三大工具結合，構建一套「上帝模式」的自動化研究工作流。透過 Claude Code 的技能創建功能，使用者能將複雜的 YouTube 搜索、深度資料分析與結構化筆記記錄整合為單一指令，大幅提升知識內化與內容產出的效率。

---

## 詳細重點整理
### 1. 超強工作流的宏觀架構 [[01:34](http://www.youtube.com/watch?v=kU3qYQ7ACMA&t=94)]
* **流程拆解**：利用 Claude Code 作為中樞，先透過 YouTube 搜索獲取資料，再交由 NotebookLM 進行免費的大規模分析（不耗費 Claude Token），最後將結果自動存入 Obsidian 庫中。
* **關鍵概念**：**「研究怪獸」模式**——將瑣碎的工具調用轉化為一個封閉且自動化的生產力環節。

### 2. 核心組件：NotebookLM 與 API 整合 [[06:33](http://www.youtube.com/watch?v=kU3qYQ7ACMA&t=393)]
* **技術突破**：雖然 NotebookLM 官方尚未開放公共 API，但影片介紹了使用開源專案 `NotebookLM-PI` 來實現 CLI 操作。
* **功能擴展**：透過 Claude Code 呼叫 NotebookLM，可以生成 Podcast 腳本、心智圖、投影片或資訊圖表等多元產出。
* **關鍵概念**：**「算力轉移」**——將繁重的分析任務外包給 Google 的 NotebookLM，節省 Claude 的使用成本。

### 3. 技能創建器 (Skill Creator) 的妙用 [[05:26](http://www.youtube.com/watch?v=kU3qYQ7ACMA&t=326)]
* **工作流自動化**：介紹如何使用 `/plugin` 安裝技能創建器，並透過自然語言描述（如：搜尋 YouTube 並回傳結構化結果）來定義新技能 [[05:55](http://www.youtube.com/watch?v=kU3qYQ7ACMA&t=355)]。
* **超級技能 (Super Skill)**：將多個子技能（搜尋 + 分析 + 儲存）封裝成一個單一指令（例如 `YouTube Pipeline`），達成一鍵完成整套研究流程 [[09:04](http://www.youtube.com/watch?v=kU3qYQ7ACMA&t=544)]。
* **關鍵概念**：**「工具自進化」**——讓 AI 自己撰寫並優化其執行工具。

### 4. Obsidian：數位大腦與長期進化 [[12:07](http://www.youtube.com/watch?v=kU3qYQ7ACMA&t=727)]
* **知識固化**：所有的分析結果以 Markdown 格式儲存於 Obsidian  vault 中，方便人類閱讀與視覺化（Graph View）。
* **Claude.md 的核心地位**：利用 `claude.md` 檔案記錄使用者的工作習慣與偏好，讓 AI 隨著時間推移越來越了解你的需求。
* **關鍵概念**：**「共生進化環節」**——檔案越多，AI 對你工作風格的理解就越深，實現長期且持續的效能提升。

---

## 結論與行動建議
* **啟發金句**：**「真正強大的不是工具本身，而是你如何將它們串聯成一套能自我優化的閉環系統。」**
* **具體行動建議（3-1-1 法則）**：
    1. **3 個安裝**：安裝 Claude Code、NotebookLM-PI 與 Obsidian。
    2. **1 個技能**：使用 Skill Creator 建立第一個「資料抓取」技能。
    3. **1 個檔案**：在 Obsidian 中建立 `claude.md`，並告訴 Claude：「請根據我們今天的對話更新我的工作風格與偏好」。
* **生活實踐建議**：
    * **建立錨點**：每次完成一項專題研究後，強制要求 Claude 更新 Obsidian 中的索引檔案。
    * **觀察紀錄**：每週檢查一次 Obsidian 的關聯圖（Graph View），觀察不同研究主題之間是否產生了意想不到的連結，作為靈感來源。

影片連結：[https://www.youtube.com/watch?v=kU3qYQ7ACMA](https://www.youtube.com/watch?v=kU3qYQ7ACMA)
