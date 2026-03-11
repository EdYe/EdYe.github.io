---
title: 'Claude Code /btw 側邊頻道與回溯指令'
date: 2026-03-12
image: /images/影片筆記/claude-code-btw-sidebar-rewind.jpg
category: 影片筆記
tags: [Claude Code, 側邊頻道, 對話污染, 回溯, 工作流]
description: '這部影片介紹了 Claude Code 的全新指令 `/btw`，讓使用者在不中斷 AI 編碼任務且不污染對話上下文的情況下，即時進行詢問與溝通，極大化開發效率。'
quote: '不要讓無關的解釋污染了 AI 的上下文視窗，因為那對 AI 完成目標毫無幫助，只有你需要那些答案。'
action: '善用 /btw 分離詢問與編碼任務，走偏時用 /re 回溯而非爭論。'
source_has_timestamps: true
---
### 核心摘要

這部影片介紹了 Claude Code 的全新指令 `/btw`，讓使用者在不中斷 AI 編碼任務且不污染對話上下文的情況下，即時進行詢問與溝通，極大化開發效率。

---

### 詳細重點整理

#### 1. 解決「對話污染」與中斷問題 [[00:50](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=50)]

* **痛點：** 過去在 Claude 編寫代碼時，若中斷它（按 Escape 或 Ctrl+C）提問，會導致對話歷史充斥著無關的問答（Q&A），降低 AI 後續輸出的品質。
* **類比：** 這就像在人類進入「深度工作」狀態時拍肩膀打斷他，會破壞專注力並增加恢復成本 [[01:19](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=79)]。

#### 2. 全新 `/btw` 指令：內建的側邊頻道 [[02:18](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=138)]

* **功能：** 允許在 AI 執行任務期間輸入 `/btw` 並提問（例如：詢問為何使用特定函式庫）。
* **優勢：**
* **並行處理：** AI 會在彈出視窗回答你的問題，而背景的編碼任務**持續進行**，不被中斷 [[02:53](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=173)]。
* **零污染：** 這些問答內容不會被存入主對話歷史，保持上下文乾淨 [[03:19](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=199)]。
* **低成本：** 利用主會話的 Prompt 快取，詢問成本極低 [[03:36](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=216)]。


* **限制：** 僅限單次對話（無法追問）且無法使用工具（如讀取檔案或繪圖）[[03:42](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=222)]。

#### 3. 進階工具：Fork Session 與 Rewind [[04:04](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=244)]

* **Fork Session (`claude -c fork-session`)：** 當需要深度探討、讀取檔案或生成圖表（如 Mermaid 流程圖）時使用。它會複製當前會話到新視窗，兩者互不干擾 [[05:14](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=314)]。
* **Rewind 指令 (`/re`)：** 若透過 `/btw` 發現 AI 理解有誤，不要試圖爭論，直接使用 `/re` 回溯到錯誤發生前的時間點，並補強指令後重試 [[06:41](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=401)]。

#### 4. 最佳實踐建議工作流 [[04:54](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=294)]

* **快速提問：** 使用 `/btw`。
* **深度研究/不同方案嘗試：** 使用 `fork-session` 或 `/fork`。
* **修正觀念錯誤：** 使用 `/re` (Rewind)。

---

### 結論與行動建議

* **金句：** 「不要讓無關的解釋污染了 AI 的上下文視窗，因為那對 AI 完成目標毫無幫助，只有你需要那些答案。」 [[06:03](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=363)]
* **具體建議：**
* 開發者應習慣將「編碼任務」與「知識詢問」分開處理。
* 善用 `/btw` 來保持開發節奏。
* 如果 AI 走偏了，**「回溯 (Rewind) 比修正 (Correct) 更有效」**，因為這能徹底清除錯誤的上下文 [[06:48](http://www.youtube.com/watch?v=DqjBbAr3oTo&t=408)]。



---
