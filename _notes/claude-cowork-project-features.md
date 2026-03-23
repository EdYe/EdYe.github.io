---
title: 'Claude Co-work專案功能：記憶與自動化實戰'
date: 2026-03-23
image: /images/影片筆記/claude-cowork-project-features.jpg
category: 影片筆記
tags: [Claude Co-work, 專案管理, 記憶機制, 自動化任務, AI協作]
description: '這部影片介紹了 Claude Co-work 的最新「專案」功能，強調其透過獨立工作區、自定義指令與內建記憶機制，能有效整合並自動化執行複雜的長期專案任務'
quote: '專案功能不僅是為了開始一項新工作，更是為了管理一段長達數月的持續性協作。'
action: '為每個主要客戶或長期目標建立獨立 Project，並初始化記憶文件與排程任務'
source_has_timestamps: true
---
這是一份關於 **Claude Co-work Projects** 功能的深度解析與實作筆記。這項新功能正徹底改變 AI 輔助工作的流程，特別是在處理長期專案與複雜客戶需求時。

---

### 📌 核心摘要
這部影片介紹了 **Claude Co-work** 的最新「專案 (Projects)」功能，強調其透過**獨立工作區、自定義指令與內建記憶機制**，能有效整合、管理並自動化執行複雜的長期專案任務。

---

### 📂 詳細重點整理

#### 1. 專案功能的基礎與優勢
* **集中化管理：** 專案允許使用者將相關的對話、檔案與任務歸納在同一個專用工作區，避免不同任務間的資訊混雜 [[01:24](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=84)]。
* **雙重記憶機制：**
    * **軟記憶 (Soft Memory)：** 系統每 24 小時自動掃描專案內的所有對話，提取重要資訊並建立背景上下文 [[03:43](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=223)]。
    * **硬記憶 (Hard Memory)：** 透過自定義的 `learnings.md` 或 `memory.md` 檔案，手動或指令化地紀錄客戶偏好、技術憑證與關鍵決定 [[02:32](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=152)]。

#### 2. 三種建立專案的方法 [[04:29](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=269)]
* **從頭開始 (From Scratch)：** 適合全新的客戶或任務，可立即設定專屬指令與上傳初始文件。
* **從 Claude Chat 匯入：** 若先前已在標準版 Claude 使用過 Project 功能，可直接同步至 Co-work 環境中 [[04:34](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=274)]。
* **轉換現有資料夾：** 將過往在 Co-work 中已有的對話資料夾直接升級為專案模式 [[05:32](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=332)]。

#### 3. 實戰應用：自動化任務管理 [[06:06](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=366)]
* **合約/提案解析：** 影片示範上傳一份客戶提案後，指令 Claude 讀取時間軸並自動在 Co-work 中建立對應的**排程任務 (Scheduled Tasks)** [[09:22](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=562)]。
* **環境一致性：** 專案層級的指令 (Project Instructions) 會與全域指令結合，確保 AI 在該專案下始終保持特定的語氣、目標與專業知識架構 [[07:25](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=445)]。

#### 4. 高效率筆記技巧：跨對話銜接 [[13:10](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=790)]
* **結算指令：** 當單一對話過長導致 Token 消耗過快時，建議使用特定指令讓 AI 總結當前進度、更新記憶檔案，並**生成一段供下一次對話使用的「接續提示詞 (Prompt)」** [[13:28](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=808)]。
* **自動化更新：** 可設定排程任務，讓 AI 在每場對話結束後自動將新學到的知識同步至 `learnings.md` 檔案中 [[12:33](http://www.youtube.com/watch?v=X1Z_qANEIyo&t=753)]。

---

### 💡 結論與行動建議

**金句：** 「專案功能不僅是為了開始一項新工作，更是為了管理一段長達數月的持續性協作。」

**具體行動建議 (Step-by-step)：**
1.  **建立專案：** 為每個主要客戶或長期目標建立獨立 Project。
2.  **上傳上下文：** 包含提案、官網 URL、過往會議記錄與技術文件。
3.  **初始化記憶文件：** 指令 AI 建立 `memory.md`，並要求其在每次對話結束前主動更新此檔案。
4.  **善用排程：** 將文件中的 Deadline 轉化為系統內的 Scheduled Tasks，讓 AI 主動追蹤進度。
