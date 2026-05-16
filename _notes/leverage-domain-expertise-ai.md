---
title: '垂直 AI 的制勝關鍵：如何讓領域專業知識驅動產品'
date: 2026-05-17
image: /images/AI筆記/leverage-domain-expertise-ai.jpeg
category: AI筆記
tags: [垂直AI, 領域專家, Oracle評估者架構, AI組織設計, 品質評估]
description: '根據 Gartner 數據，約 50% 的生成式 AI 專案遭到放棄。核心原因是缺乏對所自動化工作流程的深層理解。Chris Lovejoy 提出 Oracle-Evaluator-Architect 三層架構，作為企業將領域專家整合進 AI 組織的核心框架。'
quote: '贏得垂直 AI，根本上是一個組織問題，而不是模型問題。'
action: '問自己三個問題：AI 輸出品質誰真正負責？這個人有沒有真正的決策權？品質衡量是靠人工品味還是可量測指標？'
source_has_timestamps: true
---
# 如何善用領域專業知識打造更好的 AI 產品

**核心論點：垂直 AI 的競爭本質是「組織問題」，而非「模型問題」。** 贏家不在於擁有最強的 LLM，而在於能否建立一個「領域原生 AI 組織」，將領域專業知識系統性地嵌入產品。

***

## [核心摘要]

根據 Gartner 的數據，去年約 50% 的生成式 AI 專案遭到放棄 。Chris Lovejoy（前醫師、Anterior 早期員工）認為，這是因為大多數企業在建置 AI 產品時，缺乏對所自動化工作流程的深層理解 。他提出「Oracle → Evaluator → Architect」三層架構，作為企業將領域專家整合進組織的核心框架。

***

## [詳細重點整理]

### 1. 為何需要領域專家？[00:04:49]

前端模型已足夠好，真正的缺口是**組織如何將專家判斷力運作化** 。評估 AI 輸出品質本身就需要「品味」（taste），而這種品味必須來自領域經驗，無論是正式（醫師、律師）或非正式（深度業務使用者）皆然 。

**關鍵概念：領域原生 AI 組織（Domain-Native AI Organization）**

### 2. 三大角色框架 [00:02:52]

| 角色 | 核心任務 | 適用情境 |
|---|---|---|
| **Oracle（神諭者）** | 直接看輸出 → 調整 Prompt → 改善產品（全閉環自負責） | 無法客觀量化品質、規模尚小、品味主導 |
| **Evaluator（評估者）** | 定義品質指標 → 建立量測系統 → 協作工程師改進 | 可量化輸出品質、人工迭代速度足夠 |
| **Architect（架構師）** | 設計能自動從使用行為學習並持續改進的系統 | 需求變異大、人工迭代太慢、需動態自適應 |



**關鍵概念：Oracle–Evaluator–Architect 框架**

### 3. 三個實際案例 [00:10:51]

- **Granola（AI 會議記錄）**：第一員工 Joe 是記者出身，親自讀論文、訪談數千名用戶後寫 Prompt，持續擔任 Oracle 角色。因為「沒有完美的會議記錄」，需要人的品味主導 。
- **Tandem（醫療 AI 書記）**：初期由 McKinsey 背景醫師 Roy 擔任 Oracle，規模擴大後演化為**分散式 Oracle**，由不同專科、不同國家的醫師各自負責子集的 Prompt 調整 。
- **Anterior（醫療保險事前授權）**：Chris 本人先扮演 Oracle，後建立臨床審查 Dashboard 轉型為 Evaluator，最終設計自動改進系統成為 Architect，完整走過三個階段 。

**關鍵概念：分散式 Oracle（Decentralized Oracle）**

### 4. 三種角色所需技能 [00:17:03]

- **Oracle**：直接相關的領域經驗（非泛泛的「我是醫師」）、Prompt 工程能力、對細節的高度執著、客戶溝通力 
- **Evaluator**：資料科學直覺、定義指標能力、統計技能、業界人脈（建立審查團隊用）、產品管理經驗 
- **Architect**：以上所有 + LLM 產品開發實戰經驗 + 工程能力 

**關鍵概念：T型領域專家（Domain Breadth Hiring）**

### 5. 如何真正發揮領域專家價值 [00:19:25]

三個核心原則：

- **指定首席領域專家（Principal Domain Expert）**：避免「人人都負責 = 無人負責」的委員會陷阱，給予明確的 AI 品質最終決策權
- **給予真正的擁有權（Ownership）**：讓他在決策桌上，而非只是顧問角色。失去擁有權的專家會在 12–18 個月後離職，組織也失去寶貴的隱性知識
- **招募有廣度的人（Hire for Breadth）**：領域專業是底線，但要盡量兼備資料科學、工程、PM 等鄰近技能，才能隨組織成長從 Oracle 演化到 Architect

***

## [結論與行動建議]

**啟發金句：**
> 「贏得垂直 AI，根本上是一個組織問題，而不是模型問題。」 

**具體行動建議 — O-E-A 演進法則：**
1. 早期招募有廣度技能的首席領域專家，從 **Oracle** 起步
2. 當規模讓一人閉環難以為繼時，轉型為 **Evaluator**，建立可量測系統
3. 當人工迭代速度已成瓶頸，設計能自動學習的 **Architect** 架構

**生活實踐建議：**
若你正在開發 AI 產品，現在就問自己三個問題：「我的 AI 輸出品質，誰真正負責？」「這個人有沒有真正的決策權？」「我的品質衡量機制是靠人工品味，還是可量測的指標？」— 答案將決定你該組建哪種類型的組織。

***

## [參考連結]

- 原始影片：[https://youtu.be/kfSDc2eVLo4](https://youtu.be/kfSDc2eVLo4)
- 講者 Twitter：[@ChrisLovejoy\_](https://x.com/ChrisLovejoy_)
- 講者 LinkedIn：[Dr. Christopher Lovejoy](https://www.linkedin.com/in/dr-christopher-lovejoy/)
