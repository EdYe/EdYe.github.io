---
title: '資深工程師為何在 AI Agent 開發上屢屢碰壁：五個典範轉移'
date: 2026-05-31
image: /images/AI筆記/senior-engineers-struggle-ai-agents.jpg
category: AI筆記
tags: [語義狀態, 非確定性控制流, Evals, Agent工具設計, 錯誤容錯]
description: '資深工程師在建構 AI Agent 時面臨的最大挑戰，源自多年累積的隱性知識與直覺——這些是 Agent 完全看不到的。Google DeepMind 的 Philipp Schmid 提出五個典範轉移，說明 Agent 開發與傳統軟體開發的本質差異：從確定性控制流轉向非確定性目標導向設計。'
quote: 'Stop fighting the model. Trust it, verify it, but stop trying to force it into a step-by-step workflow.'
action: '將錯誤回傳模型而非重啟流程，在 CI/CD 中加入 LLM-as-a-Judge eval 步驟，以成功率取代 assert 判斷'
source_has_timestamps: true
---
## [核心摘要]

資深工程師在建構 AI Agent 時面臨的最大挑戰，源自**多年累積的隱性知識與直覺**——這些是 Agent 完全看不到的。Google DeepMind 的 Philipp Schmid 提出五個典範轉移，說明 Agent 開發與傳統軟體開發的本質差異：從確定性控制流轉向非確定性目標導向設計，解決工程師「過度干預」與「測試框架錯用」的核心痛點。

***

## [詳細重點整理]

### 1. 文字即狀態（Text is the New State）[00:07]

傳統軟體仰賴 Boolean flag、enum 等結構化資料來記錄狀態；Agent 時代，**語義上下文（Semantic Context）** 取代了這些硬性資料結構。 以溫度單位偏好為例，過去只能用 `is_celsius = true/false` 的旗標處理，現在 Agent 可以動態理解「我在歐洲用攝氏，但料理時想用華氏」這種細微的個人偏好。

> **關鍵概念：語義狀態（Semantic State）**

***

### 2. 交出控制權（Hand Over Control）[00:00]

傳統客服系統仰賴分類模型觸發預定工作流（deterministic workflow）；Agent 必須能動態回應意圖的轉變。 例如用戶說「取消訂閱」，傳統流程只能走預設的取消流程，但 Agent 可以理解背後的原因並即時提出替代方案，讓用戶改變心意。

> **關鍵概念：非確定性控制流（Non-Deterministic Control Flow）**

***

### 3. 錯誤即輸入（Errors Are Just Inputs）[05:04]

傳統軟體遇到錯誤通常重啟請求，代價低廉；但一個已運行 15 分鐘的 Agent，若遇錯就重來，將消耗大量算力並遺失所有上下文。 應仿照 Go 語言設計哲學，將錯誤視為與用戶輸入同等級的訊號，讓模型自行決定如何繼續前進。

> **關鍵概念：錯誤容錯設計（Error as Context）**

***

### 4. 評估取代單元測試（Evals Replace Unit Tests）[06:16]

傳統單元測試假設「輸入 A 永遠產出 C」，但 Agent 本質上是**非確定性的（Non-Deterministic）**，同樣的 prompt 不保證每次產出相同步驟或結果。 應改用 **Eval（成功率評估）**：測量 Agent 在多次執行中通過的比例，並以 LLM-as-a-Judge 或人類專家評估輸出品質。

> **關鍵概念：基於成功率的可靠性評估（Reliability-Based Evaluation）**

***

### 5. 建構即刪除（Build to Delete）[07:46]

`deleteItem` 這個 API endpoint 對熟悉代碼庫的工程師來說顯而易見，但 Agent 只能看到 function schema 和 doc string，完全沒有多年積累的隱性背景知識。 因此工具必須**自我說明（Self-Documenting）**，以語意介面設計。此外，隨著模型不斷進步，同樣的 Agent 會被多次重建——軟體是消耗品，要習慣「建了就準備刪」。

> **關鍵概念：Agent-Ready 語意介面（Self-Documenting Semantic Interface）**

***

## [結論與行動建議]

**啟發金句：**
> **"Stop fighting the model. Trust it, verify it, but stop trying to force it into a step-by-step workflow."** 

***

**具體行動建議 — T-E-R-E-D 法則：**

| 法則 | 核心行動 |
|------|----------|
| **T**ext as State | 以語義文字取代結構化狀態旗標 |
| **E**rror as Input | 將錯誤回傳模型，而非重啟流程 |
| **R**elinquish Control | 定義目標而非逐步指令 |
| **E**vals over Tests | 以成功率 % 取代 assert 判斷 |
| **D**esign to Delete | 撰寫 Agent-Ready 自我說明工具，預期重建 |

***

**生活實踐建議（針對 AI-Powered Application Architect）：**

- **工具設計審查**：下次設計 MCP tool 或 function calling schema 時，把你寫的 doc string 交給不熟悉系統的同事看，若他們不能理解，Agent 也不會理解。
- **導入 Eval Pipeline**：在你的 CI/CD 中加入 LLM-as-a-Judge 的 eval 步驟，設定每次 release 必須達到的 pass rate 門檻，而非只跑 deterministic unit tests。
- **錯誤處理重構**：審視現有 Agent flow，確認所有工具的錯誤回傳都進入 model context，而非直接 throw exception 中斷流程。

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/3_gYbhABcAE?si=edKABI81-3Gqtq8e
- 👤 講者 Philipp Schmid：[Twitter](https://x.com/_philschmid) ｜ [LinkedIn](https://www.linkedin.com/in/philipp-schmid-a6a2bb196/) ｜ [GitHub](https://github.com/philschmid)
