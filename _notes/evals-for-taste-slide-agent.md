---
title: 'Eval 飛輪：為 AI Agent 打造可量化的品質迭代系統'
date: 2026-05-26
image: /images/影片筆記/evals-for-taste-slide-agent.jpeg
category: 影片筆記
tags: [Evals, Grader, QA Loop, 評估飛輪, 迭代優化]
description: '本影片以Slide Generation Agent為實戰案例，示範如何為 AI Agent 設計、校正、迭代 Eval 體系。核心痛點是多數開發者缺乏客觀衡量指標，導致 Agent 調優全憑「感覺」。'
quote: 'Evals 不是你做一次就忘記的東西——它們是活的制品，必須隨系統演化。'
action: '先定義「成功」長什麼樣，用 Code Grader 管確定性邊界、Model Grader 管品質語意，並給 Judge 設具體錨點防止分數漂移。'
source_has_timestamps: true
---
## [核心摘要]

本影片以**Slide Generation Agent**為實戰案例，系統性示範如何為 AI Agent 設計、校正、迭代 Eval（評估）體系。核心痛點是：多數開發者缺乏客觀衡量指標，導致 Agent 調優全憑「感覺」、無法量化進步或退化。影片提出以**Rubric 驅動的 Eval 飛輪**取代主觀判斷，搭配 Code Grader + Model Grader + QA Loop 實現可重複、可行動的品質迭代。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

***

## [詳細重點整理]

### 1. 什麼是 Evals？ [00:19]

Eval 是針對特定 AI 系統的**系統性測試集**，由「任務情境」與「評分邏輯（Grader）」組成，讓「感覺好一點」轉化為可行動的數字信號。沒有 Evals，你只能在生產環境被動等 bug；有了 Evals，你可以主動定義「成功」並驗證每次迭代是否真的提升。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

**關鍵概念：** **Eval 即成功定義的形式化**（Formalizing What Success Looks Like）

***

### 2. 業界 Benchmark vs. 自建 Evals [03:43]

SWE-Bench、ARC-AGI 等通用基準雖具參考性，但**不針對你的 use case**。任何人在打造 Agentic System 時，都應自建對應的 Eval，才能真正衡量目標場景的品質。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

**關鍵概念：** **領域特定 Eval（Domain-Specific Evaluation）**

***

### 3. 三種 Grader 類型 [09:23]

| Grader 類型 | 特性 | 適用場景 | 缺點 |
|---|---|---|---|
| **Code Grader** | 確定性、快速、便宜 | Emoji 數量、Slide 張數、字數 | 脆性高、缺乏語意 |
| **Model Grader** | 彈性、可評語意品質 | 排版美觀度、顏色對比、文字一致性 | 不確定性、費用高、需校正 |
| **Human Grader** | 最高品質、最具洞察 | A/B 測試、Spot Check | 極慢、極貴 |

**關鍵概念：** **Multi-Judge Consensus（多評審共識機制）**——用多個 LLM 獨立評分取多數決，引入確定性緩衝 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

***

### 4. 實戰迭代：Slide Agent 的 Eval 飛輪 [15:30]

初版 Agent（僅給基礎 Prompt）產出品質低落：Emoji 過多、字體太小、版面雜亂。 根據 Eval 分數定向更新 System Prompt（加入排版規範、禁用 Emoji、設定字級），第二版視覺品質顯著提升。三版加入「每張必含圖表」需求，四版引入 **QA Loop**（自我審查代理）後，所有 Judge Grader 分數從 2.8～3.8 提升至 4.2～4.4。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

**關鍵概念：** **Eval-Driven Iteration Loop（Eval 驅動迭代飛輪）**

***

### 5. QA Loop 設計哲學 [29:05]

QA Agent 被刻意指示「**假設問題存在，去找出來**」，而非「確認是否有問題」。這種對抗性設計（Adversarial QA）讓 Agent 主動獵錯，而非被動確認。指令包含：渲染成圖片→自我視覺檢查→修正→重渲染→至少完成一輪修正確認才可停止。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

**關鍵概念：** **對抗性 QA Loop（Adversarial QA Loop）**

***

### 6. 更聰明的 Model vs. 精調 Prompt [33:05]

將 Sonnet 換成 **Opus 4.7** 後，僅用最初的簡單 Prompt，輸出品質便大幅超越多輪調優的 Sonnet 版本——Emoji 為零、版面更整潔，Judge 分數達 4.4～5.0。 但這也暴露另一問題：Model Grader 未設錨點（Anchor），導致分數虛高（無圖表的版本仍獲 Image Judge 滿分 5），凸顯 **Eval 本身也需要持續校正**。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

**關鍵概念：** **Eval 飽和（Eval Saturation）**與**評分錨點缺失（Missing Score Anchor）**

***

## [技術/數據對比]

| Agent 版本 | Text Judge | Image Judge | Layout Judge | Color Judge |
|---|---|---|---|---|
| 初版（基礎 Prompt） | ~2.8 | N/A | ~3.2 | ~3.5 |
| 加入排版規範 | ~3.5 | ~3.8 | ~3.6 | ~3.8 |
| 加入圖表要求 | ~3.8 | ~3.8 | ~3.9 | ~4.0 |
| 加入 QA Loop | **4.4** | **4.2** | **4.2** | **4.4** |
| Opus 4.7（簡單 Prompt）| **4.4** | **5.0*** | **4.2** | **4.8** |

*\*無圖表但 Judge 給滿分，顯示 Grader 校正問題* [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

***

## [結論與行動建議]

**啟發金句：**
> **「Evals 不是你做一次就忘記的東西——它們是活的制品，必須隨系統演化。」** [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

**具體行動建議（E-G-A 法則）：**
- **E**valuate：先定義「成功」長什麼樣，才開始建 Agent
- **G**rade：Code Grader 管確定性邊界，Model Grader 管品質語意
- **A**nchor：給 Judge Grader 設具體錨點（0分範例、5分範例），防止分數漂移

**生活實踐建議：**
在你的 AI 輔助工作流中（如文件生成、報告整理、程式碼審查），在上線前先定義 3 個「必過的最低品質門檻」作為你的輕量 Eval，形成個人的 Eval-Driven 工作習慣，不讓主觀感覺成為唯一品質標準。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

***

## [參考連結]

- 原始影片：https://youtu.be/v9FTCvkV_a0?si=u0zS-8OGbS-UIsvD
