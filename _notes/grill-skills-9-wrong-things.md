---
title: '9 件工程師在 /grill-* 技能中常犯的錯誤'
date: 2026-05-26
image: /images/影片筆記/grill-skills-9-wrong-things.jpeg
category: 影片筆記
tags: [可Grill性, 上下文智慧區, 主動規劃平衡, 上下文保值, 參數化知識]
description: '/grill-me 與 /grill-with-docs 技能是 AI Agent 規劃模式的替代工具，核心概念是透過持續問答建立對任務的「共識理解」。然而多數工程師誤用'
quote: 'Grilling is a conversation, not an interview. It''s your job to figure out where you''re going.'
action: '規劃階段用大模型 Grill、控制 Scope 在 120K tokens 內、同一 Session 產出 PRD 並平行開兩個 Session 倍增效率'
source_has_timestamps: true
---
# 9 Things People Get Wrong With /grill-\* Skills

**Matt Pocock｜2026年5月25日｜片長 13:28**

***

## [核心摘要]

`/grill-me` 與 `/grill-with-docs` 技能是 AI Agent 規劃模式（Plan Mode）的替代工具，核心概念是透過持續問答建立對任務的「共識理解」。然而多數工程師誤用了它——他們要麼被動接受 AI 狂問 200 題、要麼試圖在規劃階段解決本不該在此解決的問題。這支影片透過 9 個失敗模式，揭示**如何精準控制 Grilling Session 的品質、範疇與效率**，讓規劃真正轉化為可執行的工程決策。

***

## [詳細重點整理]

### 1. 混淆高低保真度問題 [00:00–03:44]

問題分為兩類 ：
- **低保真度問題（Low-Fidelity）**：可直接在問答中回答，例如「這個路由的 URL 應該是什麼？」——可被「Grillable」
- **高保真度問題（High-Fidelity）**：需要實際看到原型才能回答，例如「這個 UI 填表流程應該是單頁還是多頁？」——屬於「Ungrillable」

遇到 Ungrillable 問題時，正確做法是透過 `/handoff` 技能轉入**原型開發子 Session**，完成後再 handoff 回原始 Grilling Session 繼續進行。

> **關鍵概念：可 Grill 性（Grillability）**——區分問題是否能在對話中被解決的判斷力。

***

### 2. 範疇設定過大 [03:44–05:41]

若 Grill 的範疇太大，會同時觸發兩個問題 ：
- 高保真度問題會隱藏在龐大範疇中，讓整個 Session 難以推進
- 上下文視窗會進入**「笨蛋區（Dumb Zone）」**——Matt 估計多數最先進模型在約 **120K tokens** 後開始品質劣化

正確做法是事先請 Agent 將大範疇**拆解成多個小範疇**，分別 Grill。

> **關鍵概念：上下文智慧區（Smart Zone）**——保持在 120K tokens 以內以維持模型高品質推理。

***

### 3. 態度過於被動或過於強硬 [05:41–06:54]

Grilling Session 是**對話，不是單向問答**。兩種失敗極端 ：
- **過度被動**：讓 AI 狂問 540 題、範疇爆炸、問了一堆無意義問題
- **過度強硬**：堅持不斷在低保真度問題上鑽牛角尖，遲遲不進入實作階段

工程師需主動掌舵——引導對話方向、設定邊界、判斷何時應停止 Grilling、直接寫 Code。

> **關鍵概念：主動規劃平衡（Active Planning Balance）**——在規劃的深度與進入實作的時機之間取得平衡。

***

### 4. 不珍視 Grilling Session 的產出 [06:54–08:40]

整個 Grilling Session 積累的上下文（設計決策、問答記錄）**是極高價值的資產**。常見的荒謬錯誤 ：
- 在結束 Session 後清空上下文，另起新視窗才跑 `/to-prd` 指令
- 直接丟棄 10 萬 tokens 的珍貴設計決策

正確做法：若 Session 還有足夠 Budget，就**直接在同一視窗進入實作**；若需要 handoff，則在同一 Session 內先產出 PRD（使用 `/to-prd` 技能）再移交。

> **關鍵概念：上下文保值（Context Preservation）**——將規劃 Session 的決策結果轉化為可攜帶的工程交付物。

***

### 5. 使用能力太弱的模型來 Grill [08:40–10:24]

Grilling 高度依賴模型的**參數化知識（Parametric Knowledge）**——即訓練時學到的系統設計直覺，而非從對話中注入的上下文 。模型需要能夠：
- 辨識工程師尚未考慮到的潛在問題
- 提出非顯而易見的設計建議

相反地，**實作階段（Implementation）可以使用較弱的模型**，因為此時大部分資訊已以上下文形式提供（詳細計畫、程式碼片段）。

> **關鍵概念：參數化知識優先（Parametric Knowledge First）**——Grilling 的品質取決於模型本身的推理深度，而非僅靠 Prompt。

***

### 6. 不執行平行 Grilling Sessions [10:24–11:26]

同時開啟 **2 個 Grilling Sessions 平行進行**，可直接翻倍規劃產能 。操作方式：
- 對第一個 Session 回答問題後，趁它處理時切換到第二個 Session
- 兩個 Session 交替作答，形成高效的非同步流程
- Matt 自身極限為 2 個，若有長時間執行的研究任務則可嘗試 3 個

> **關鍵概念：非同步規劃並行（Async Planning Parallelism）**——把 AI 等待時間轉化為另一個規劃任務的推進動力。

***

## [結論與行動建議]

**啟發金句：**
> **「Grilling is a conversation, not an interview. It's your job to figure out where you're going.」**

**核心法則：G-S-P 三軸法則**
- **G（Grillability）**：先判斷問題是否可 Grill，Ungrillable 問題立即 Handoff 去原型
- **S（Smart Zone）**：控制 Scope，讓整個 Session 保持在 120K tokens 智慧區內
- **P（Preserve & Parallelize）**：珍視每一次 Session 的產出，同時平行跑兩個 Session 倍增效率

**生活實踐建議（AI 應用開發場景）：**

作為 AI 應用架構師，可將這套方法直接應用於產品規劃工作流 ：
1. **需求拆解時**：用 `/grill-with-docs` 對每個功能模組分別進行小範疇 Grilling，避免一次性規劃整個產品
2. **PRD 撰寫前**：在同一 Session 內完成規劃後直接產出 `/to-prd`，不要另起 Session 浪費決策上下文
3. **模型選擇策略**：規劃階段用 Claude Opus / GPT-4o 等大模型；實作階段可降級至 Claude Sonnet / GPT-4o-mini 節省成本
4. **每日工作節奏**：開啟兩個規劃 Session 並行，一個處理前端 UX 流程，另一個處理後端 API 設計

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/UzMNBN6xLLA
- 🛠️ /grill-with-docs 技能：https://aihero.dev/s/kI3sig
- 📄 /handoff 技能：https://aihero.dev/s/hnJZQI
- 🎓 AI Coding Cohort：https://aihero.dev/s/kBCOel
