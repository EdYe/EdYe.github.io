---
title: '讓你立刻獲得 Offer 的 AI PM 技能'
date: 2026-05-27
image: /images/AI筆記/ai-pm-skill-job-offers.jpeg
category: AI筆記
tags: [產品品味, Build-Trace-Eval-Loop, PM Agent, Evals, Context Graph]
description: '在 AI 代理（Agent）時代，程式碼已是廉價商品，PM 的真正競爭優勢在於「產品品味（Product Taste）」——即判斷什麼值得建造的直覺。本集完整示範從零到一：用 Claude Code 建造 PM Agent → 用 Arize 做 Tracing 可觀測性 → 用 Evals 量化品質'
quote: '使用觀測性工具、查看 Traces 和 Evals 的 PM，可能已經是業界前 1% 了。'
action: '這個週末花 2 小時：選一個產品、開啟 Claude Code 建立 PM Agent、接上 Arize Phoenix 做 Tracing、讓 Claude 建議 v0 Eval 並校準，設定自動 Loop。'
source_has_timestamps: true
---
# 🎯 讓你立刻獲得 Offer 的 AI PM 技能

**主講：** Aparna Dhinakaran（Arize AI 共同創辦人 & CPO，融資 $1.31 億） [youtube](https://www.youtube.com/watch?v=i7930fj3T54)
**主持：** Aakash Gupta｜時長：1 小時 19 分 [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

***

## [核心摘要]

在 AI 代理（Agent）時代，**程式碼已是廉價商品**，PM 的真正競爭優勢在於「**產品品味（Product Taste）**」——即判斷什麼值得建造的直覺。本集完整示範從零到一：用 Claude Code 建造 PM Agent → 用 Arize 做 Tracing 可觀測性 → 用 Evals 量化品質 → 自動化自我改善迴圈，解決 AI 代理「黑盒子、無法除錯、無法持續進步」的核心痛點。 [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

***

## [詳細重點整理]

### 1. PM 最大誤區：急著 Build，跳過 Eval [00:00]

多數團隊一開始就直接動手建造，卻沒有建立評估基準。正確順序是：**先 Build → 再 Trace → 再 Eval → 再 Loop**，而非跳過中間步驟。 [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

**關鍵概念：Build-Trace-Eval-Loop 框架**

***

### 2. 產品品味才是真正的護城河 [04:35]

> "Code is cheap now. The ones that stand out are those with an opinion and taste about what to build."

當每個工程師都能用 AI 快速產出程式碼，**PM 的稀缺資源變成了判斷力**。最優秀的 PM 懂得從 GitHub Issues、Gong 通話記錄、Slack、Twitter、PostHog 等多元來源聚合用戶反饋，建立「**Context Graph（脈絡圖）**」。 [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

**關鍵概念：Context Graph（企業級 Agent 的核心解鎖）**

***

### 3. 用 Claude Code 實際建造 PM Agent [09:28]

具體步驟如下： [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

- 在終端機開啟 Claude Code，建立新目錄
- 輸入 Starter Prompt：抓取 GitHub Discussions、Issues、Releases
- 設定評分維度：Bug vs Feature、反應數、留言數、時效性
- 指定輸出格式：P0–P3 優先順序的 Markdown PM 報告
- 加入 `loop` 指令，用 Claude 自動建立 **Cron Job**，每小時或每日定期執行

**關鍵概念：PM Taste Agent（產品品味代理）**

***

### 4. 一行指令完成 Tracing 可觀測性 [19:00]

以往 Tracing 需要工程師介入，現在只需執行：

```
npx skills add
```

Arize Phoenix 的 Instrumentation Skill 會自動掃描程式碼庫，識別所有 LLM Call 和 Tool Call，並自動接上 Tracing 層，**無需工程師支援**。Trace 資料即時串流進 Arize 儀表板。 [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

**關鍵概念：Span（評估的最小單位）** ——一個 Span = 一次離散的 Agent 步驟，Evals 在 Span 層級執行，而非 Trace 層級

***

### 5. 讓 Claude 自己建議 Evals [28:00]

在取得 Traces 後，可直接問 Claude Code：「幫我建議一個好的 Eval」。系統透過 Evaluator Skill 分析 Traces，自動提出三類 Eval： [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

| Eval 類型 | 評估目標 |
|---|---|
| **Report Groundedness** | PM 報告的引用是否有數據依據 |
| **Priority Alignment** | P0–P3 優先排序是否符合預期 |
| **Report Actionability** | 報告行動建議是否可執行 |

但重點是：**PM 需要更細粒度的 Eval**——針對每一個 Issue 個別評估優先分數是否準確，而非只看最終報告。

**關鍵概念：Vibe Evals（LLM 建議的 Eval 草稿，非最終裁決）**

***

### 6. Vibe Evals vs. Axial Coding [33:58]

LLM 自動建議的 Eval 只是 **v0 草稿**，它不知道你的 Bug-First 政策、你的薪資邏輯、你對「Critical」的定義。需以人類判斷校準後才能使用。 [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

**核心提醒**：當 Eval 觸發錯誤時，有兩種可能——
1. **Agent 輸出有問題**
2. **Eval 本身未校準**

兩種情況都很正常，都是進步機會。

***

### 7. 自我改善迴圈自動化 [48:50]

最頂尖的 AI 團隊已在運行以下自動迴圈： [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

1. 抓取所有 Eval 觸發失敗的 Spans
2. 按失敗類別分群
3. 提出具體 Prompt 修正方案
4. 人類審查並核准
5. 部署新版本

**關鍵概念：自我改善迴圈（Self-Improvement Loop）**——定期執行，人類只在核准步驟介入

***

### 8. Context Graph 是企業的終極解鎖 [01:06:00]

企業資料分散於各個孤島（CRM、Gong、Analytics、GitHub、Slack）。突破重圍的團隊正在建立**統一的 Context Layer**，讓一個 Agent 同時存取所有資料來源。 [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

**關鍵概念：Context Graph（企業 Agent 可觀測性的瓶頸解法）**

***

## [技術/數據對比]

| 維度 | 傳統 PM 工作流 | AI PM + Eval 工作流 |
|---|---|---|
| Tracing 設定 | 需工程師介入，耗時數天 | 一行 CLI 指令，分鐘內完成 |
| Feedback 來源 | 人工查閱 GitHub/Slack | Agent 自動聚合多源 |
| Issue 優先排序 | 人工判斷，每周一次 | 自動評分，每小時更新 |
| 品質評估 | 無系統化評估 | Span 層級 Eval 自動化 |
| 改善週期 | 依賴 Sprint 週期 | 觸發即改善，自動 Loop |

***

## [結論與行動建議]

**啟發金句：**
> 「使用觀測性工具、查看 Traces 和 Evals 的 PM，可能已經是業界前 1% 了。」 [youtube](https://www.youtube.com/watch?v=i7930fj3T54)

**具體行動法則：B-T-E-L（Build → Trace → Eval → Loop）**

**生活實踐建議：**

**這個週末的 2 小時行動計畫（Aparna 親自建議）：** [youtube](https://www.youtube.com/watch?v=i7930fj3T54)
1. 選一個你最熟悉的產品或自己手邊的內部工具
2. 開啟 Claude Code，輸入 Prompt 建立一個 PM Agent（從 GitHub Issues 開始）
3. 執行 `npx skills add`，接上 Arize Phoenix（免費開源）做 Tracing
4. 讓 Claude 建議 v0 Eval，再用你自己的判斷校準一次
5. 設定 Loop，讓它每天自動運行——這就是「自我改善的 PM 系統」

***

## [參考連結]

- 📺 原始影片：https://youtu.be/DL-pUGcfrf4?si=oX4u9B_z8mpxUdvM [youtube](https://www.youtube.com/watch?v=i7930fj3T54)
- 📝 完整文字稿：https://www.aakashg.com/how-to-build-a-self-improving-pm-agent-in-claude-code/
- 🔧 Arize Phoenix（開源）：https://arize.com
- 👤 Aparna LinkedIn：https://www.linkedin.com/in/aparnadhinakaran
