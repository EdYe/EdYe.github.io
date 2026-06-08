---
title: 'Harness Engineering：AI 競爭的新淘金熱'
date: 2026-06-08
image: /images/AI筆記/harness-engineering-gold-rush.jpg
category: AI筆記
tags: [Harness工程, 系統性糾錯, RHO, ContextRot, AgentAI]
description: 'Harness Engineering（套架工程）正取代 Prompt Engineering 成為 AI 競爭的核心優勢。同一個模型，搭配不同的 Harness 設計，效能差距可達 6 倍。'
quote: 'Prompt Engineering 是讓 AI 做對一次；Harness Engineering 是讓 AI 不再做錯。'
action: '部署 AI Agent 前先設計工具層、記憶層與驗證層（H-M-V 法則），而非只調整 Prompt。'
source_has_timestamps: true
---
## [核心摘要]

**Harness Engineering（套架工程）** 正取代 Prompt Engineering 成為 AI 競爭的核心優勢。同一個模型，搭配不同的 Harness 設計，效能差距可達 **6 倍**。真正的競爭力不在於誰用了更好的模型，而在於誰建立了更好的「圍繞模型的系統」——包含工具、記憶體、上下文管理、權限控管、驗證機制與回饋迴圈。 [youtu](http://youtu.be)

***

## [詳細重點整理]

### 1. 什麼是 Harness Engineering [00:02]

模型是「智能引擎」，而 Harness 是讓智能引擎穩定輸出可靠結果的「整體系統架構」。它包括：工具調用規則、記憶庫、上下文管理、技能路由、權限層、稽核日誌、回退路徑與回饋迴圈。HashiCorp 與 Terraform 共同創辦人 **Mitchell Hashimoto** 在 2026 年初將此概念推向主流，他的核心論點是：當 AI 出錯，正確做法不是重跑同一個 Prompt，而是**改變系統，讓同類錯誤不再發生**。 [youtu](http://youtu.be)

> **關鍵概念：系統性糾錯（Systemic Error Prevention）**

***

### 2. Prompt / Context / Harness 三者的差異 [02:37]

這三者相關但不同，必須清楚區分： [youtu](http://youtu.be)

| 維度 | 操作對象 | 本質 |
|---|---|---|
| **Prompt 工程** | 模型直接讀取的文字 | 單次互動優化 |
| **Context 工程** | 模型接收的資訊內容 | 資訊篩選與組合 |
| **Harness 工程** | 模型外圍的不可見結構 | 持續可靠性設計 |

MCP Server、工具庫、技能庫本身**不是** Harness，它們只是組件；Harness 是決定所有組件如何協同運作的**組裝系統**。 [youtu](http://youtu.be)

***

### 3. Stanford + 清華研究：效能差距最高 6 倍 [03:17]

Stanford 與星洲大學（Singua University）的聯合研究顯示，**相同模型**搭配不同 Harness 設計，效能差異最高達到 6 倍。這意味著：當前沿模型能力趨同時，真正的競爭優勢將移轉到「建立更好系統」的團隊身上。Goldman Sachs 的數據亦佐證此論點——AI 對 GDP 有 7% 的巨大潛力，但截至 2024 年 4 月，美國僅有 4% 企業真正採用生成式 AI，根本原因正是缺乏成熟的「系統層」將 AI 能力轉化為可重複的生產力。 [youtu](http://youtu.be)

> **關鍵概念：系統層差距（System Layer Gap）**

***

### 4. Agent AI 的三大核心瓶頸 [05:16]

UC Berkeley 論文指出：一旦 AI 從聊天機器人進化為 **Agent**（主動執行工具、操作文件、呼叫 API），模型本身不再是唯一瓶頸，**系統擴展（System Scaling）** 才是下一個關鍵。三大瓶頸如下： [youtu](http://youtu.be)

- **Context Rot（上下文腐爛）**：龐大的 context window 若充斥舊日誌與無效資訊，有效訊號會被噪音淹沒。Claude Code 採用五層壓縮系統（micro-compact、context collapse 等）對抗此問題，並對大型輸出僅提供 8KB 預覽
- **Stale but Confident（過時卻自信的記憶）**：Agent 可能套用昨天的記憶來操作今天已重構的程式碼。成熟 Harness 應將記憶視為「提示」而非「事實」，並在閒置時自動清理記憶
- **Skills Routing（技能路由失誤）**：擁有更多工具不代表更好，關鍵是 Agent 能否在正確時機選用正確工具，並驗證輸出結果

***

### 5. 微軟研究：AI 自我優化 Harness — RHO [09:45]

微軟亞洲研究院與香港城市大學提出 **Retrospective Harness Optimization（RHO，回顧式套架優化）**，讓 Agent 透過回顧自身過去的工作記錄來優化 Harness，無需人工標記的 ground truth。 [youtu](http://youtu.be)

流程如下：
1. 從歷史任務中篩選「高難度＋多樣性」的任務（使用 DPP 方法平衡兩者）
2. 對每個任務執行多次嘗試，檢測「自我驗證」與「自我一致性」兩個信號
3. 產生多個候選 Harness，與舊版比較，只保留效能確實提升的版本

**實測結果**：使用 GPT-4.5 搭配 RHO，SWE-bench Pro 分數從 0.59 提升至 **0.78**，coding、技術工作與知識任務均有進步。優化後的 Agent 更頻繁驗證工作成果、更謹慎使用工具，且在長任務中表現更穩定。 [youtu](http://youtu.be)

> **關鍵概念：回顧式套架優化（Retrospective Harness Optimization, RHO）**

***

## [技術/數據對比]

| 指標 | 數據 | 來源 |
|---|---|---|
| 相同模型不同 Harness 效能差距 | 最高 **6x** | Stanford × Singua 研究 |
| SWE-bench Pro（優化前） | 0.59 | Microsoft RHO 論文 |
| SWE-bench Pro（RHO 優化後） | **0.78** | Microsoft RHO 論文 |
| AI 潛在 GDP 提升 | **7%（$7T/10年）** | Goldman Sachs 2023 |
| 美國企業實際 AI 採用率 | **僅 4%**（2024年4月） | Goldman Sachs 2024 |
| OpenAI 5 個月 AI 生成程式碼 | **~100 萬行 / 1,500 PRs** | OpenAI Essay |

***

## [結論與行動建議]

**啟發金句：**
> **「Prompt Engineering 是讓 AI 做對一次；Harness Engineering 是讓 AI 不再做錯。」**

**具體行動建議 — H-M-V 法則：**
- **H（Harness 先行）**：在部署任何 AI Agent 前，先設計圍繞模型的工具層、記憶層與驗證層，而非只調整 Prompt
- **M（Memory 懷疑論）**：把 AI 記憶視為「待核實的假設」，建立定期清理與驗證記憶的機制
- **V（Verify 每一步）**：每個工具呼叫後都要有自動化驗證，確認輸出是否符合預期、行為是否安全

**生活實踐建議（針對 AI 應用架構師）：**
- 在設計 AI 產品時，評估維度從「選哪個模型」升級為「設計怎樣的 Harness」
- 參考 Claude Code 的五層 Context 壓縮機制，在自己的 Agent 系統中引入 Context 分級管理
- 將 RHO 的核心思想落地：為生產環境的 Agent 建立「失敗任務回顧」機制，讓系統從錯誤中自動生成改進建議而非只靠人工 debug

***

## [參考連結]

- 📺 原始影片：https://youtu.be/mGYr9VqQnEI [youtu](http://youtu.be)
- 📄 Microsoft RHO 論文：https://arxiv.org/abs/2606.05922
- 📄 UC Berkeley Agent Harness 論文：https://arxiv.org/abs/2605.13357
- 📄 Microsoft Work IQ API：https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/
