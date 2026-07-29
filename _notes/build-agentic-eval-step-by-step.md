---
title: '從零打造 Agentic Eval 實戰教學'
date: 2026-07-29
image: /images/影片筆記/build-agentic-eval-step-by-step.jpg
category: 影片筆記
tags: [Agentic Eval, 領域專業知識, 地板天花板測試, Goldilocks原則, 多次採樣]
description: '本影片由 Aakash Gupta 主持，邀請前 Meta Llama 模型 PM、現為 Gamow Labs 創辦人的 Daniel McKinnon，'
quote: '💡Eval 不是用來證明模型很強，而是用來找到模型在哪裡會失敗。知道天花板在哪裡，才是評估的意義。'
action: '🎯下次寫 AI 功能規格時先建立 Eval 而非 PRD，依 F-C-S-M 法則設計地板案例、天花板案例、多次採樣與中間題庫'
source_has_timestamps: true
---

## [核心摘要]

本影片由 Aakash Gupta 主持，邀請前 Meta Llama 模型 PM、現為 Gamow Labs 創辦人的 Daniel McKinnon，**從零開始實機示範如何建構一個 Agentic Eval（代理式評估）**。核心論點是：在 GenAI 時代，Eval 已取代 PRD 成為溝通產品規格的最佳方式，因為 AI 產品行為太多元，無法用文字完整描述，只能用「範例」來定義。而建構好 Eval 的關鍵不在工具，而在**領域專業知識（Subject Matter Expertise）**——Daniel 以臨床基因體學為例，示範從囊狀纖維化（簡單）到先天性心臟病雙基因遺傳（困難）的完整 Eval 建構流程 。 [youtube](https://www.youtube.com/)

***

## [詳細重點整理]

### 1. Eval 取代 PRD 的邏輯 [00:00]

傳統 PRD 大量篇幅描述產品在特定情境下如何運作，但 GenAI 產品需要「做所有事」，無法逐一描述。**Eval 本質上就是模型的問答題（trivia question）**——包含一個 prompt、一個正確或合理正確的答案、以及一套評分方式。它告訴工程團隊「成功長什麼樣子」，是 GenAI 時代最清晰的溝通工具。若模型在 offline eval 上表現不佳，就需更換模型、調整 harness 或改變產品方向，而非盲目上線 。 [youtube](https://www.youtube.com/)

> **關鍵概念：Eval 即規格（Eval as Spec）**——範例取代描述，成為產品定義的載體。

***

### 2. Offline Eval vs Online Eval [02:41]

**Offline eval** 是在開發階段預先準備的一組「問答題集」（約 100 題），作為真實流量的代理指標。例如食譜網站的 offline eval 就是 100 個不同口味冰淇淋的 prompt，搭配答案與評分方式。**Online eval** 則是上線後真實用戶的滿意度。兩者的假設是：offline 表現好 → online 用戶滿意。這不總成立，但仍是目前最佳預測方式。有時 offline eval 能在第一週就告訴你「以現有模型技術，這件事做不到」，避免浪費資源上線 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

> **關鍵概念：離線-上線預測鏈（Offline-to-Online Prediction Chain）**

***

### 3. 舊基準已飽和，任務範式轉移 [12:35]

兩年前 OpenAI 用 MMLU、HellaSwag、ARC、HumanEval 等 Q&A 基準衡量模型進步。如今前沿模型在這些基準上幾乎 100% 滿分，**這些 benchmark 已飽和且失去鑑別力**。Anthropic 在 Opus 4.8 上改用完全不同的基準：agentic coding、agentic terminal coding、multidisciplinary reasoning、agentic computer use、agentic financial analysis。核心範式從「問答」轉向「**任務**」——模型不再是收到 prompt 回傳答案，而是接收一個需要多步驟（推理、工具呼叫、搜尋）的複雜任務 。 [youtube](https://www.youtube.com/)

> **關鍵概念：任務思維（Task Thinking）取代 QA 思維**——Eval 從單輪問答進化為多步驟代理任務評估。

***

### 4. Eval 的機械化建構流程 [07:03]

儘管任務更複雜，建構 Eval 的框架大致不變：

- **定義問題**：用一句話描述功能要做什麼
- **收集代表性 prompt**：約 100 個，遵循 Goldilocks 原則——不能太簡單（100% 正確率，無優化空間）也不能太難（0% 正確率，不知是否可行），目標 **25%–50% 成功率**
- **設計評分**：可自動評分、用另一個 LLM 當裁判、或人工評審
- **持續迭代**：隨著模型進步，成功率會從 25%→50%→100%，此時需丟棄舊 eval、建構更難的新版

> **關鍵概念：Goldilocks 原則**——Eval 難度必須「恰到好處」，留有優化空間。

***

### 5. 臨床基因體學 Eval 實機演示 [15:32]

Daniel 選擇了一個他深度關心的領域：**新生兒加護病房（NICU）中的全基因體定序診斷**。問題是：全基因體定序已是診斷金標準，但解讀結果極度耗時，限制了這項救命技術的可及性。目標是將人類專業知識「蒸餾」進模型，擴大技術覆蓋面。

流程背景：定序儀產出原始 reads → 處理找出與參考基因體的差異 → 判斷這些變異是否有臨床意義。一位患者的基因體約有 **10 億筆 reads、每筆 150 鹼基對**，存在一個巨大的文字檔中 。 [youtube](https://www.youtube.com/)

> **關鍵概念：知識蒸餾（Knowledge Distillation）**——將領域專家的判讀能力注入模型。

***

### 6. 囊狀纖維化 Eval——尋找模型地板 [17:59]

Daniel 先從最簡單的案例開始，確保模型「能做」。他選擇**囊狀纖維化（Cystic Fibrosis）**，一種遺傳原因已充分理解的疾病，標誌性基因是 **CFTR**，標誌性變異是 **delta F508**（第 508 位的苯丙胺酸缺失）。

操作步驟：

- 用 Codex 在一個 VCF（變異檔）中手動插入這個變異，製造一個「合成患者」
- VCF 本質上是一個純文字檔，記錄染色體、位置、參考鹼基與變異鹼基
- 同一 prompt 同時丟給多個模型測試：GPT 3.5 (Codex spark low)、Haiku、GPT 5.5 (extra high)
- 結果：**所有模型都成功找到 CFTR 變異**，確認此任務對當前模型「不過難」 [youtube](https://www.youtube.com/)

> **關鍵概念：地板測試（Floor Test）**——先用最簡單的真實案例確認模型能力下限。

***

### 7. 先天性心臟病 Eval——尋找模型天花板 [33:07]

確認簡單案例可行後，必須測試困難案例以**建立模型能力上限**。Daniel 引用一篇研究論文：**先天性心臟病的雙基因遺傳架構（Digenic Architecture）**。

- **單基因、單變異**疾病（如囊狀纖維化）在某些情況下已是「已解決問題」
- **雙基因（Digenic）**疾病涉及兩個基因的交互作用，是極新的研究領域
- 即使論文已發表，理論上 agent 應能搜尋網路找到所有文獻並深度理解，但實際上這對模型構成真正的挑戰
- 目的是**找到模型的天花板**：知道哪些案例模型會失敗，才是 Eval 存在的意義 [youtube](https://www.youtube.com/)

> **關鍵概念：天花板探測（Ceiling Probing）**——刻意尋找模型失敗的案例，界定能力邊界。

***

### 8. 為何需要多次取樣 [40:39]

模型具有**非確定性（Non-determinism）**：同樣的 prompt 每次跑結果可能不同。單次成功或失敗不能代表真實能力分佈。必須對同一任務**多次執行（多次採樣）**，才能理解模型在該任務上的真實表現分佈，而非一次幸運或不幸運的結果 。 [youtube](https://www.youtube.com/)

> **關鍵概念：多次採樣（Multi-sampling）**——以分佈而非單點衡量模型能力。

***

### 9. 領域專業知識決定一切 [47:04]

Daniel 的基因學 Eval 之所以有效，是因為**他懂基因學**，而非因為用了什麼模板或工具。**不存在像 PRD 模板那樣的 Eval 模板**。這也是為什麼 Anthropic 和 OpenAI 正在招募投資銀行家、會計師、律師等垂直領域專家——你必須先深度理解問題，才能建構有意義的 Eval 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

> **關鍵概念：領域專業驅動（SME-Driven Eval Design）**——Eval 的品質上限由領域知識決定，而非工具或框架。

***

### 10. Meta vs Google 的產品文化 [50:01]

Daniel 在 Meta（Llama）和 Google（Gemini）都工作過：

- **Google**：更偏工程導向（engineering-led）
- **Meta**：更偏產品導向（product-led），文化更激進（aggressive）
- 他經歷了 Llama 3 的高峰到 Llama 4 的低谷 [youtube](https://www.youtube.com/)

***

### 11. 創辦 Gamow Labs [52:59]

Daniel 創辦了 **Gamow Labs**，專注於解決臨床基因體學的可及性問題，將基因診斷專業知識蒸餾進模型，擴大這項救命技術的覆蓋範圍 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

***

## [技術/數據對比]

| 維度 | 舊範式（Q&A Eval） | 新範式（Agentic Eval） |
|---|---|---|
| **核心任務** | 單輪問答（prompt → answer） | 多步驟任務（task → reasoning → tools → output） |
| **代表性基準** | MMLU, HellaSwag, ARC, HumanEval | Agentic coding, terminal coding, agentic reasoning, computer use, financial analysis |
| **飽和狀態** | 前沿模型已接近 100% | 仍有大量優化空間 |
| **時間跨度** | 單次回應 | 長時間序列，多步驟 |
| **評分難度** | 較易（有明確對錯） | 較難（多步驟中部分正確可能導致錯誤結果） |
| **溝通載體** | PRD（文字描述） | Eval（範例驅動） |

| 測試案例 | 疾病 | 基因架構 | 難度 | 模型表現 |
|---|---|---|---|---|
| 囊狀纖維化 | 單基因、單變異（CFTR delta F508） | 已充分理解 | 簡單（地板測試） | 多個模型均成功 |
| 先天性心臟病 | 雙基因（Digenic） | 新興研究領域 | 困難（天花板測試） | 暴露模型能力邊界 |

***

## [結論與行動建議]

> **啟發金句：**
> 「Eval 不是用來證明模型很強，而是用來找到模型在哪裡會失敗。知道天花板在哪裡，才是評估的意義。」

**具體行動法則——F-C-S-M 法則：**

- **F（Floor）**：先找一個最簡單的真實案例，確認模型「能做到」
- **C（Ceiling）**：再找一個你預期模型會失敗的案例，確認「天花板在哪」
- **S（Sample）**：對每個案例多次採樣，理解真實分佈而非單一結果
- **M（Middle）**：在 floor 與 ceiling 之間填入約 100 個案例，目標 25%–50% 成功率，留出優化空間

**生活實踐建議：**

身為 AI 應用架構師與產品經理，下次要為 AI 功能寫規格時，**不要先寫 PRD，先寫 Eval**。具體做法：選定一個你深度理解的領域，用一句話定義問題，在 ChatGPT 或 Claude 中建立 Project，上傳相關文件，用 AI 幫你生成約 100 個測試案例（用 AI 測 AI），設定 Goldilocks 難度，設計評分機制（LLM judge + 人工校準），最後將 Eval 交付工程團隊作為優化目標。若你的功能在 offline eval 上只有 50%，先判斷哪些子任務能達到 80%，**用 guardrails 限制產品只回答高信心度的問題**——這就是 PM 在 AI 時代的核心價值判斷 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

***

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/ztN6bE_FuQQ
- 完整圖文版：https://www.news.aakashg.com/p/how-to-build-your-first-eval
