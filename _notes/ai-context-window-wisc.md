---
title: 'AI 上下文視窗的挑戰與 WISC 架構'
date: 2026-03-26
image: /images/AI筆記/ai-context-window-wisc.jpg
category: AI筆記
tags: [上下文視窗, WISC架構, AI幻覺, 子代理, 提示詞管理]
description: '更大的上下文視窗不等於更好的結果；透過「WISC 架構」精簡並結構化輸入，才能徹底解決 AI 幻覺與效率低下的問題'
quote: '你的 AI 編碼助手沒有壞，是你餵給它太多垃圾了。'
action: '建立專案規則文件，對話超過 40 則訊息時主動總結並開啟新 Session'
source_has_timestamps: true
---

這部影片由 **DIY Smart Code** 頻道製作，深入探討了為什麼單純增加 AI 的上下文視窗（Context Window）反而會降低其表現，並提出了一套名為 **WISC** 的架構，旨在透過精準的上下文管理來提升 AI 編碼助理（如 Claude, Cursor, Windsurf）的效率與準確性。

---

### 核心摘要
**更大的上下文視窗不等於更好的結果；透過「WISC 架構」精簡並結構化輸入，才能徹底解決 AI 幻覺與效率低下的問題。**

---

### 詳細重點整理

#### 1. 為什麼更大的上下文會讓 AI 變笨？ [[01:05](http://www.youtube.com/watch?v=gyo0eRgsUWk&t=65)]
* **注意力衰減：** 研究顯示，隨著對話增長，AI 的注意力品質會從第一條訊息的近乎完美，到第 40 條訊息時下降至約 **20%**。
* **大海撈針問題：** 更多的 Token 代表 AI 必須在更龐大的資料中搜尋資訊。當你把乾草堆（上下文）變大，找到那根針（關鍵資訊）的難度就會倍增。
* **上下文腐敗：** 長期對話會導致 AI 開始幻覺文件名稱、重複已完成的工作，甚至破壞原本已修復的程式碼。

#### 2. WISC 架構：四大核心策略 [[02:17](http://www.youtube.com/watch?v=gyo0eRgsUWk&t=137)]
此框架由 Cole Medine 經過 2000 小時的實戰開發總結而成，分為四個步驟：

* **W - Write (寫入外部記憶) [[03:35](http://www.youtube.com/watch?v=gyo0eRgsUWk&t=215)]：**
    * 不要指望 AI 有長期記憶，應將架構規範、命名慣例、測試模式等寫入外部文件（如 `.claude.md`）。
    * **具體作法：** 在開始複雜任務前，先寫好 Markdown 規格文件 (Spec)，而非直接在對話框溝通。
* **I - Isolate (隔離與委派) [[04:55](http://www.youtube.com/watch?v=gyo0eRgsUWk&t=295)]：**
    * 利用「子代理 (Sub-agents)」進行研究。讓子代理閱讀 50 個檔案並產出 2 段總結，主代理只需讀取這 2 段總結。
    * **數據支持：** 這種做法比單一代理處理全部上下文的效果提升了 **90.2%**。
* **S - Select (分層選擇載入) [[06:23](http://www.youtube.com/watch?v=gyo0eRgsUWk&t=383)]：**
    * 建立金字塔型載入系統：基層是全局規則，中層是按需載入（如編輯 React 時才載入 React 規則），頂層是單次對話的特定指令。
    * **優點：** 節省 Token 空間，且利用 Anthropic 的 Prompt Caching 可降低 90% 的成本。
* **C - Compress (壓縮與清理) [[08:14](http://www.youtube.com/watch?v=gyo0eRgsUWk&t=494)]：**
    * 當對話過長，AI 開始出現重複言論時，應立即觸發壓縮。
    * **技巧：** 在「垃圾資訊」堆積前就進行總結並重啟新工作階段。

#### 3. 實作建議與步驟 [[10:00](http://www.youtube.com/watch?v=gyo0eRgsUWk&t=600)]
1.  **建立持久化規則：** 將重複說過三次以上的要求寫進專案規則文件。
2.  **採用 Scout Pattern (偵查模式)：** 派遣子代理去探索程式碼庫，完成後銷毀其上下文，保持主視窗乾淨。
3.  **手術式修剪：** 定期要求 AI 丟棄不再需要的上下文（如已修復的錯誤記錄或舊檔案內容）。

---

### 結論與行動建議
* **啟發金句：** 「你的 AI 編碼助手沒有壞，是你餵給它太多垃圾了。」(Your AI coding agent is not broken, you are feeding it garbage.) [[00:15](http://www.youtube.com/watch?v=gyo0eRgsUWk&t=15)]
* **具體行動：**
    1.  停止在對話框中進行長篇大論的背景說明。
    2.  今天就開始建立專屬的專案規則文件。
    3.  若對話超過 40 則訊息，請主動總結並開啟新 Session。
