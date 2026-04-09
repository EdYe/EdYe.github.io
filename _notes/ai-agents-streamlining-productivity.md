---
title: 'AI 代理與技能漸進揭露：極大化生產力的思維變革'
date: 2026-04-10
image: /images/影片筆記/ai-agents-streamlining-productivity.jpeg
category: 影片筆記
tags: [上下文精簡, 漸進式揭露, 遞迴技能構建, AI代理, 生產力]
description: '這段影片深入探討了 AI 代理人（Agents）與 Claude 技能（Skills）的運作邏輯。講者 Ross Mike 指出，當前的 AI 模型已經足夠強大，關鍵在於如何透過「精簡上下文」與「逐步疊代技能」來極大化生產力。'
quote: '不要為了看起來酷而擴張，要為了生產力而擴張。'
action: '手動帶教 3 次建立技能，遇錯即更新技能文件，完美後固化為自動化流程。'
source_has_timestamps: true
---

## 核心摘要
這段影片深入探討了 AI 代理人（Agents）與 Claude 技能（Skills）的運作邏輯。講者 Ross Mike 指出，當前的 AI 模型（如 Claude 3.5 Opus、GPT-4）已經足夠強大，關鍵在於如何透過「精簡上下文」與「逐步疊代技能」來極大化生產力。這是一場從「追求酷炫工具」轉向「深耕個人工作流」的思維變革。

---

## 詳細重點整理
### 1. 拋棄冗長的 System Prompt 與 .md 文件 [[01:44](http://www.youtube.com/watch?v=S_oN3vlzpMw&t=104)]
* 許多人習慣在 `agent.md` 或 `claude.md` 中塞入大量背景資訊，但講者認為 95% 的人其實不需要。
* **關鍵概念**：**模型已經夠聰明了**。過多的通用指令（如告訴它使用 React）只會浪費 Token，讓 AI 變笨。除非是公司專有的私密資訊或極特殊的規範，否則應保持 Minimalist（極簡主義）。

### 2. 技能（Skills）的「漸進式揭露」優勢 [[03:25](http://www.youtube.com/watch?v=S_oN3vlzpMw&t=205)]
* 技能文件與普通文件的區別在於，它平時只會向 AI 提供「名稱」與「描述」。
* **關鍵概念**：**漸進式揭露（Progressive Disclosure）**。只有當 AI 判斷需要該技能時，才會讀取詳細內容。這能節省數千個 Token，並確保 AI 在 70% 以下的黃金上下文窗口內保持高效運作 [[31:11](http://www.youtube.com/watch?v=S_oN3vlzpMw&t=1871)]。

### 3. 不要「下載」技能，要「親手建立」 [[08:28](http://www.youtube.com/watch?v=S_oN3vlzpMw&t=508)]
* 下載別人的技能 marketplace 雖然快，但 AI 缺乏你具體工作流的脈絡。
* **關鍵概念**：**體驗式學習**。你應該像帶領新員工一樣，先手動帶領 AI 走一遍流程（Back and forth），確認它產出正確後，再要求它「根據剛才成功的紀錄生成技能文件」。

### 4. 遞迴式技能構建法（Recursive Skill Building） [[20:44](http://www.youtube.com/watch?v=S_oN3vlzpMw&t=1244)]
* 技能不是寫完就沒事了，而是需要根據錯誤不斷進化。
* **關鍵概念**：當 AI 失敗時（如 API 報錯），不要氣憤，而要詢問錯誤原因，解決後命令 AI：**「根據這次修復更新技能文件，確保未來不再犯」**。

---

## 結論與行動建議
* **啟發金句**：**「不要為了看起來酷而擴張，要為了生產力而擴張。」(Don't scale for what looks cool, scale for productivity.)** [[26:36](http://www.youtube.com/watch?v=S_oN3vlzpMw&t=1596)]

* **具體行動建議：3-5-1 疊代法則**
    1. **3 次手動帶教**：針對一個新任務（如分析贊助郵件），手動引導 AI 執行 3 次，糾正其細節。
    2. **5 個數據源整合**：嘗試建立一個能跨多個工具（如 Notion, Google Sheets, Twitter API）的複雜技能。
    3. **1 次自動化固化**：在任務執行完美後，下令：「請回顧上述對話，並為我寫一個 skill.md 檔案」。

* **生活實踐建議**：
    * **建立「錯誤感謝日誌」**：每當 AI 代理人出錯時，將其視為優化「技能文件」的絕佳機會，立即修補邏輯漏洞。
    * **上下文體檢**：定期檢查你的 AI 對話，如果 System Prompt 超過 1000 Tokens，強迫自己將其拆分為「技能」以釋放 AI 的思考空間。

Https://youtu.be/S_oN3vlzpMw?si=o41HHj9RHwjiY2K6
