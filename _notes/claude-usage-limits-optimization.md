---
title: 'Claude使用限制與優化技巧'
date: 2026-04-06
image: /images/AI筆記/claude-usage-limits-optimization.jpeg
category: AI筆記
tags: [Claude, Token管理, 上下文優化, 使用限制, 省量技巧]
description: '這段影片深入解析了 Claude 使用者近期頻繁遇到「使用限制」的原因，並揭示了 Anthropic 在尖峰時段調整 session 限制的內幕'
quote: 'AI 的承諾是不知疲倦，但我們的責任是給予它最清晰、最輕量的導航。'
action: '所有大型文件先轉換為 Markdown 再上傳，一個 Prompt 解決三個小問題，養成輸入 /context 監控 Token 的習慣。'
source_has_timestamps: true
---

## 核心摘要
這段影片深入解析了 Claude 使用者近期頻繁遇到「使用限制（Usage Limits）」的原因，並揭示了 Anthropic 在尖峰時段調整 session 限制的內幕。影片核心價值在於透過理解「Token（代幣）」與「Context（上下文）」的運作機制，提供 14 個實用的優化技巧，幫助使用者在不增加成本的情況下，極大化 AI 的工作效率與持久力。

---

## 詳細重點整理

### 1. 理解使用限制與 Token 機制 [[02:23](http://www.youtube.com/watch?v=vnocKrxasg4&t=143)]
* **Session 限制**：Claude 以 5 小時為一個 Session 單位，從發送第一則訊息起算。尖峰時段（如英國下午、美國上午）系統會更嚴格地限制工作量。
* **Token 的代價**：訊息、附件、歷史紀錄都會消耗 Token。使用 **Opus 4.6** 模型消耗速度是 **Sonnet** 的 5 倍。
* **關鍵概念**：**Token 是 AI 的貨幣**。了解預算分配（透過輸入 `/context` 指令查看實時消耗）是精準控制的第一步。

### 2. 聊天習慣與提示詞優化 [[11:05](http://www.youtube.com/watch?v=vnocKrxasg4&t=665)]
* **單一任務原則**：為每個新任務開啟新對話。長對話會累積大量歷史背景，導致每發送一個字都在燒掉巨量 Token [[11:40](http://www.youtube.com/watch?v=vnocKrxasg4&t=700)]。
* **批次處理請求**：不要一來一回發送瑣碎指令，應將多個要求（如：修正錯字+縮短引言+加上 CTA）整合在同一個提示詞中 [[13:04](http://www.youtube.com/watch?v=vnocKrxasg4&t=784)]。
* **關鍵概念**：**減少往返次數**。精確且具體的指令能顯著降低上下文的負擔。

### 3. 工作空間與文件管理技巧 [[15:19](http://www.youtube.com/watch?v=vnocKrxasg4&t=919)]
* **格式轉換**：避免直接丟入沉重的 PDF。建議先用其他工具將文件轉為 **Markdown** 或純文字格式，這是 AI 最愛且最節省空間的語言 [[16:22](http://www.youtube.com/watch?v=vnocKrxasg4&t=982)]。
* **善用 Claude Projects**：專案功能採用 RAG 技術，僅抓取相關內容進入上下文，比一般聊天室更節省資源 [[17:50](http://www.youtube.com/watch?v=vnocKrxasg4&t=1070)]。
* **精簡指令**：將自定義指令（Custom Instructions）保持在 500 字以內，減少每則訊息的固定載入開銷 [[19:42](http://www.youtube.com/watch?v=vnocKrxasg4&t=1182)]。
* **關鍵概念**：**結構化與輕量化**。保持工作區整潔，移除不相關的文件。

### 4. 進階省電與時間策略 [[23:33](http://www.youtube.com/watch?v=vnocKrxasg4&t=1413)]
* **Session 重置技巧**：利用 5 小時窗格的特性，在正式工作前幾小時先發送一個「丟棄式提示詞」啟動計時，可巧妙跨越兩個 Session 以獲得雙倍配額 [[23:33](http://www.youtube.com/watch?v=vnocKrxasg4&t=1413)]。
* **關閉多餘工具**：關閉「Extended Thinking（深度思考）」以及不常用的 MCP 連接器，避免背景程序偷偷吃掉 Token [[10:18](http://www.youtube.com/watch?v=vnocKrxasg4&t=618)]。
* **關鍵概念**：**避峰就谷**。將重度任務安排在非尖峰時段執行。

---

## 結論與行動建議

* **啟發金句**：**「AI 的承諾是不知疲倦，但我們的責任是給予它最清晰、最輕量的導航。」**
* **具體行動建議（3-M 優化法則）**：
    1.  **Markdown First**：所有大型文件先轉換格式再上傳。
    2.  **Multi-Task in One**：一個 Prompt 解決三個小問題，不重複發問。
    3.  **Monitor Context**：養成輸入 `/context` 的習慣，像看錢包餘額一樣監控 Token。
* **生活實踐建議**：
    * **建立時間錨點**：觀察自己所在時區的 Claude 尖峰時間，將「創意腦暴」等重度任務移至早晨非尖峰時段。
    * **工具清查日記**：每月檢查一次已連接的 MCP 或外掛，關閉重複功能的工具（例如：影片中提到的兩個 Chrome 控制插件）。

影片連結：[https://www.youtube.com/watch?v=vnocKrxasg4](https://www.youtube.com/watch?v=vnocKrxasg4)
