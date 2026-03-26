---
title: 'AI 代理程式的長時程任務設計藍圖'
date: 2026-03-26
image: /images/AI筆記/ai-agent-long-running-blueprint.jpg
category: AI筆記
tags: [長時程任務, Harness架構, 對抗性評估, 脈絡焦慮, 多代理系統]
description: 'Anthropic 如何透過開發「Harness」設計，讓 AI 代理程式能長時間自主執行複雜任務，解決 AI 常見的「脈絡焦慮」與「自我評價過高」等問題'
quote: 'Harness 中的每一個組件，本質上都代表了我們對模型目前無法獨立完成該任務的一種假設。'
action: '拆解長時程任務並建立規劃與 QA 的多代理架構，給予評估者具體的評分量表'
source_has_timestamps: true
---

這部影片標題為 **「Anthropic Just Dropped the New Blueprint for Long-Running AI Agents」**，由 *The AI Automators* 頻道製作。影片深入解析了 Anthropic 官方發布的關於「長時程 AI 代理程式 (Long-running AI Agents)」的設計藍圖與技術實踐。

以下是為您整理的結構化筆記：

---

### 核心摘要
這部影片探討了 Anthropic 如何透過開發「Harness（裝具/框架層）」設計，讓 AI 代理程式能長時間（數小時甚至數天）自主執行複雜任務（如編寫完整遊戲或音樂工作站），解決 AI 常見的「脈絡焦慮」與「自我評價過高」等問題。

---

### 詳細重點整理

#### 1. 什麼是 AI Harness (代理程式裝具)？ [[01:02](http://www.youtube.com/watch?v=9d5bzxVsocw&t=62)]
* **定義：** Harness 是封裝 AI 模型的一層軟體結構，包含提示詞 (Prompts)、工具 (Tools)、反饋迴路 (Feedback loops) 與約束條件 (Constraints)。
* **比喻：** 模型像是「引擎」，而 Harness 則是「整台汽車」或「馬匹的韁繩」，負責控制動力並導向正確目標。
* **重要性：** 對於複雜任務，Harness 的設計與模型本身的性能同樣重要。

#### 2. AI 代理程式的兩大失敗模式 [[03:50](http://www.youtube.com/watch?v=9d5bzxVsocw&t=230)]
* **脈絡焦慮 (Context Anxiety) [[04:02](http://www.youtube.com/watch?v=9d5bzxVsocw&t=242)]：** 當 context window 即將填滿時，模型會開始表現失常，例如急著結束對話、草率完成步驟或謊稱任務已完成。
* **自我評價平庸 (Poor Self-evaluation) [[06:03](http://www.youtube.com/watch?v=9d5bzxVsocw&t=363)]：** 如果讓 AI 評價自己的工作，它通常會給予正面評價（即使成果很普通），且難以處理主觀的品質判斷（如設計的美感）。

#### 3. 解決方案：對抗性評估 (Adversarial Evaluation) [[07:21](http://www.youtube.com/watch?v=9d5bzxVsocw&t=441)]
* **生成器與評估器：** 引入一個專門的「評估器代理 (Evaluator Agent)」，其任務是抱持懷疑態度去審查「生成器代理」的成果。
* **將主觀品質量化 [[09:12](http://www.youtube.com/watch?v=9d5bzxVsocw&t=552)]：** 不要問「這美嗎？」，而是定義具體的設計原則（如：原創性、技術執行力、功能性），讓評估能更客觀。
* **工具授權：** 讓評估器擁有 Playwright 等工具，能實際操作生成的網頁、截圖並像真實用戶一樣進行測試 [[09:54](http://www.youtube.com/watch?v=9d5bzxVsocw&t=594)]。

#### 4. 實戰演練：從復古遊戲到音樂工作站 (DAW) [[11:32](http://www.youtube.com/watch?v=9d5bzxVsocw&t=692)]
* **2D 復古遊戲 [[11:32](http://www.youtube.com/watch?v=9d5bzxVsocw&t=692)]：** 透過「規劃者 (Planner) + 生成者 + 評估者」的框架，AI 在 6 小時內完成了一個具備關卡編輯器且可實際玩的遊戲；相比之下，單一 AI 運作的版本則無法運行。
* **瀏覽器數位音樂工作站 (DAW) [[14:15](http://www.youtube.com/watch?v=9d5bzxVsocw&t=855)]：** 使用最新的 **Opus 4.6** 模型，其具備 100 萬 token 的脈絡長度與強大的「脈絡壓縮 (Context Compaction)」能力，耗時約 4 小時、成本 125 美金，完成了具備基礎功能的 DAW。

---

### 結論與行動建議

* **Harness 會隨著模型進步而演進 [[15:23](http://www.youtube.com/watch?v=9d5bzxVsocw&t=923)]：** 許多現在設計的複雜 Harness 功能（如 Context Reset）是為了補足模型的缺陷。隨著模型性能提升（如 Opus 4.6 解決了脈絡焦慮），某些複雜的框架設計可能會變得不再必要。
* **金句/啟發：** 「Harness 中的每一個組件，本質上都代表了我們對模型目前無法獨立完成該任務的一種假設。」
* **具體建議：**
    1.  若要讓 AI 執行長時程任務，務必拆解任務並建立**規劃 (Planner)** 與 **QA (Evaluator)** 的多代理架構。
    2.  利用 **LLM as a judge** 的概念，但要給予評估者具體的評分量表 (Grading Rubrics)，而非模糊的指令。
