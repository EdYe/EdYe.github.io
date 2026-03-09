---
title: 'Harness Engineering：2026年獨立開發者的關鍵技能'
date: 2026-03-09
image: /images/AI筆記/harness-engineering.png
category: AI筆記
tags: [Harness Engineering, AI Agent, 外部記憶, 框架工程, 極簡架構]
description: '在 2026 年，決定 AI Agent 表現的關鍵不再是底層模型的強弱，而是圍繞模型的「外部框架與基礎設施（Harness Engineering）」，越簡單的框架反而能帶來越高的執行成功率。'
quote: '2025 年是 AI Agent 之年，而 2026 年將是 Harness 框架之年。AI 模型本身，可能比你為它費心搭建的那一套複雜工具管線還要聰明。'
action: '拔掉多餘的 Agent 工具，讓 Agent 維護 Markdown 進度追蹤檔案，並學習 MCP 協定保持系統彈性。'
source_has_timestamps: true
source_raw: 'Harness Engineering'
---
### 📝 YouTube 影片重點筆記：Harness Engineering (2026 獨立開發者的關鍵技能)

🔗 **影片來源**：[https://youtu.be/DN2mhf0b02s](https://www.google.com/search?q=https://youtu.be/DN2mhf0b02s)

#### 🎯 一、 核心摘要

在 2026 年，決定 AI Agent（代理）表現的關鍵不再是底層模型（如 GPT 或 Claude）的強弱，而是圍繞模型的「外部框架與基礎設施（Harness Engineering）」，越簡單的框架反而能帶來越高的執行成功率。

#### 📊 二、 詳細重點整理

* **為何 AI Agent 常在真實任務中失敗？** [[01:39](http://www.youtube.com/watch?v=DN2mhf0b02s&t=99)]
* 近期的 Epics's agent 基準測試針對「真實專業工作」（如顧問、律師的日常任務）進行評估，發現即使是頂尖模型，完成率也僅約 24%。
* 研究指出，失敗原因通常不是模型「不夠聰明」或缺乏推理能力，而是**執行與協調（Execution and Orchestration）**出了問題。
* 當任務步驟過多時，Agent 容易迷失方向、陷入無效的錯誤迴圈，或是忘記最初的目標上下文。


* **什麼是「Harness Engineering (框架工程)」？** [[03:35](http://www.youtube.com/watch?v=DN2mhf0b02s&t=215)]
* 「Harness」指的是包覆在 AI 模型外圍的所有基礎設施，包含：模型能看到什麼、擁有什麼工具、出錯時如何恢復，以及如何在長時間任務中保持進度追蹤。
* 包括 OpenAI、Anthropic 和 Meta 等科技巨頭在歷經多次失敗後都得出相同結論：真正的工程價值與挑戰在於建立這個外部框架，而非模型本身。


* **少即是多：Vercel 與 Meta 的極簡實驗** [[04:35](http://www.youtube.com/watch?v=DN2mhf0b02s&t=275)]
* **Vercel 的驚人發現**：他們原本為 Text-to-SQL Agent 打造了各種專屬工具與除錯護欄，成功率約 80%。但當他們**移除 80% 的複雜工具**，只給予基本的 Bash 指令與標準檔案讀寫權限時，成功率竟提升至 100%，且速度快了 3.5 倍、消耗 Token 減少 40%。
* **過度工程的陷阱**：開發者常誤以為「增加更多工具、路由邏輯與護欄」能幫助模型，但這些複雜設定反而成了絆腳石。隨著模型越來越聰明，架構應該越趨簡單（幾乎不需要架構）。


* **善用「外部記憶」解決上下文衰退** [[06:38](http://www.youtube.com/watch?v=DN2mhf0b02s&t=398)]
* 即使現代模型支援龐大的上下文視窗（Context Window），當任務步驟過長時（例如 Meta 發現單一任務平均需調用 50 次工具），重要的初始指令容易被大量中間運算的雜訊給掩蓋。
* **解法**：不要把所有資訊硬塞進對話上下文中，而是**將「檔案系統（File System）」當作外部記憶**。讓 Agent 把關鍵資訊寫入實體檔案中，需要時再讀取（這也是 Claude Code 依賴 `.md` 檔案的原因）。



#### 💡 三、 結論與行動建議 (Step-by-step)

影片不僅提出了觀念上的翻轉，也給予了獨立開發者三個具體的實作建議：

1. **動手精簡你的 Agent 工具 (The Vercel Experiment)** [[09:50](http://www.youtube.com/watch?v=DN2mhf0b02s&t=590)]
* 如果你有自己建立的 Agent 環境，試著拔掉多餘的專屬工具或自訂管線。
* 只保留基本的終端機與檔案讀寫權限，讓模型自己找出解決方案。


2. **建立「進度追蹤檔案」** [[10:04](http://www.youtube.com/watch?v=DN2mhf0b02s&t=604)]
* 不要依賴模型的隱含記憶，請讓 Agent 維護一個 Markdown 格式的待辦清單（To-do list）。
* 設定規則：在每次行動前讀取該檔案，行動後更新進度，大幅減少模型在長任務中「當機或迷路」的機率。


3. **學習 MCP (Model Context Protocol) 與 Skills** [[10:37](http://www.youtube.com/watch?v=DN2mhf0b02s&t=637)]
* 透過標準化的協定讓模型與外部工具互動。
* 取代寫死（Hardcode）的整合程式碼，保持系統的彈性與乾淨。



💬 **啟發金句**：

> *"2025 was the year of agents... 2026 is the year of harnesses."*
> （2025 年是 AI Agent 之年，而 2026 年將是 Harness 框架之年。）
> *"The model is probably smarter than the tool pipeline you built around it."*
> （AI 模型本身，可能比你為它費心搭建的那一套複雜工具管線還要聰明。）

---
