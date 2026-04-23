---
title: 'Claude Code 個人化記憶系統設計：六大建築基石'
date: 2026-04-23
image: /images/AI筆記/claude-code-memory-patterns.jpeg
category: AI筆記
tags: [記憶系統, 記憶分層, 衰減晉升, Hooks注入, Claude Code]
description: '這部影片打破了「尋找完美 AI 記憶框架」的迷思，強調記憶系統必須量身定做。透過 Claude Code 的代理人能力，可審計多種框架，結合身份識別、長期知識與動態衰減機制。'
quote: '記憶就像指紋，沒有兩個記憶系統應該長得一模一樣。'
action: '在 Claude Code 專案中建立 memory/ 資料夾，將身份與情境放入 identity.md 與 context.md，設定 sessionStart Hook 自動載入記憶。'
source_has_timestamps: true
---

你好！我是你的影片深度萃取器。這部影片是由 Mark Kashef 分享關於如何為 Claude Code 打造「個人化記憶系統」的深度教學。記憶不應是現成的套裝軟體，而應該像你的指紋一樣，完全契合你的工作流。

以下是為你提煉的精華內容：

## 核心摘要
這部影片打破了「尋找完美 AI 記憶框架」的迷思，強調**記憶系統必須量身定做**。透過 Claude Code 的代理人（Agentic）能力，我們可以審計多種既有框架（如向量資料庫與 Markdown），並結合身份識別、長期知識與動態衰減機制，打造一個能隨使用者一同進化的「數位記憶宮殿」，大幅提升 AI 的協作效率。

---

## 詳細重點整理

### 1. 記憶系統的定位與哲學 [[01:23](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=83)]
* 記憶系統不應試圖「取代」Claude Code 原生的記憶，而是要「補充」它。
* **關鍵概念**：**記憶是無限遊戲**。它不是完成後就結束的任務，而是一個需要持續維護、疊代與演進的動態過程 [[02:52](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=172)]。

### 2. 三步驟快速建構法 [[03:10](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=190)]
* **步驟一：克隆（Clone）**：將 GitHub 上優秀的記憶框架連結交給 Claude Code。
* **步驟二：審計（Audit）**：啟動子代理人（Sub-agents）深入分析不同框架的優劣（如向量資料庫 vs. Markdown）。
* **步驟三：提取（Extract）**：根據個人需求，讓 Claude 提取最適合你的設計模式並生成程式碼。
* **關鍵概念**：**按需定制**。與其強行採用 100% 的外部框架，不如只提取 10% 真正適合你的部分 [[01:48](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=108)]。

### 3. 記憶系統的六大建築基石 [[08:22](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=502)]
* **身份 (Identity)**：永久持續的資訊（如姓名、職業、核心價值觀）。
* **核心情境 (Critical Context)**：與當前角色或業務高度相關的重要背景。
* **工作記憶 (Working Memory)**：當下任務的零碎想法，通常是暫時性的。
* **長期與情事記憶 (Long-term & Episodic)**：儲存「為什麼」做某事以及重要的歷史成果。
* **衰減與晉升 (Decay & Promotion)**：不重要的資訊隨時間淡化，高頻使用的資訊晉升為核心記憶 [[09:34](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=574)]。
* **關鍵概念**：**記憶分層**。透過分層過濾，將原本需要 25,000 tokens 的查詢優化至 7,000 tokens [[10:11](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=611)]。

### 4. 進階記憶檢索邏輯 [[10:42](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=642)]
* **顯著性 (Salience)**：根據記憶被訪問的頻率來決定其重要性。
* **漸進式揭露 (Progressive Disclosure)**：優先加載身份與核心知識，僅在必要時檢索完整的歷史紀錄。
* **壓縮存續 (Compaction Survival)**：當工作階段過長需要壓縮時，確保核心記憶能被自動注入壓縮後的版本 [[11:30](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=690)]。

### 5. 實戰注入技術：Hooks 與 `claude.md` [[15:06](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=906)]
* **自動注入**：在 `claude.md` 中設定讓 Claude 在會話開始時「讀取」特定的身份檔案。
* **確定性執行 (Hooks)**：使用 Claude Code 的 Hooks 功能（如 `sessionStart`），強迫系統在啟動時載入記憶，避免 AI 遺忘 [[16:16](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=976)]。
* **關鍵概念**：**魔法指令**。使用「Read」等特定指令詞，能讓 Claude 更精準地調用工具來處理記憶檔案 [[17:29](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=1049)]。

---

## 結論與行動建議

* **啟發金句**：**「記憶就像指紋，沒有兩個記憶系統應該長得一模一樣。」** [[02:01](http://www.youtube.com/watch?v=OMkdlwZxSt8&t=121)]
* **具體行動建議：3-5-10 記憶設計法則**
    1. **3 分鐘身份定義**：寫下 3 個關於你「誰」且永不改變的標籤。
    2. **5 分鐘情境描述**：寫下 5 個你目前事業或生活中最重要的背景資訊。
    3. **10 分鐘工作流導入**：在 Claude Code 專案中建立一個 `memory/` 資料夾，並將上述內容放入 `identity.md` 與 `context.md`。
* **生活實踐建議**：
    * **建立記憶錨點**：在你的 `claude.md` 檔案中加入一個 Hook，設定每次開啟新會話時自動讀取你的身份檔案。
    * **定期「記憶修剪」**：每個月檢查一次你的記憶資料夾，手動刪除已過時的資訊（模擬衰減機制），保持系統的精確與輕量。

影片連結：[https://www.youtube.com/watch?v=OMkdlwZxSt8](https://www.youtube.com/watch?v=OMkdlwZxSt8)
