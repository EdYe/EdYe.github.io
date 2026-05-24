---
title: '大家都在用 Claude Code 建 Agent，卻沒有人在跑 Evals'
date: 2026-05-24
image: /images/AI筆記/everyone-building-claude-code-no-evals.jpeg
category: AI筆記
tags: [Evals評估, Instrumentation, Agent, Product Taste, 自我改善循環]
description: '在 AI Agent 開發爆炸性成長的當下，絕大多數團隊只顧著用 Claude Code 快速搭建 Agent，卻完全忽略了 Evals（評估機制）的建立。'
quote: '程式碼已經很便宜了，能讓你脫穎而出的，是你對該建什麼的判斷力。'
action: '先 Trace 讓每個 Agent 步驟可見，再用 Evals 量化品質，最後建立自動改善循環（T-E-L 法則）。'
source_has_timestamps: true
---
# 🎙️ 核心摘要
在 AI Agent 開發爆炸性成長的當下，絕大多數團隊只顧著用 Claude Code 快速搭建 Agent，卻完全忽略了 **Evals（評估機制）** 的建立。Arize AI 的 CPO Aparna Dhinakaran 透過一場 Live Demo，完整示範了「**建置 Agent → Instrumentation → Tracing → Evals → 自我改善循環**」的端到端流程，解決了 AI PM 最核心的痛點：如何知道你的 Agent 到底做得好不好？ [youtube](https://www.youtube.com/watch?v=pF4VZRU0qZA)

***
# 詳細重點整理
## 1. PM 的核心優勢：Product Taste [04:35]
程式碼成本趨近於零的時代，**Product Taste（產品品味）** 才是真正的競爭 Alpha。最優秀的 PM 能聚合來自 GitHub、Slack、Discord、Gong 通話記錄、Posthog/Amplitude 等各種數據源的用戶反饋，這種跨源整合的洞察力是 AI 無法直接替代的。

> **關鍵概念：Context Graph（上下文圖譜）** — 將 CRM、GitHub、Gong、Analytics、Slack 整合為統一的 Agent 上下文層，是企業級 AI Agent 突破孤島的關鍵。

***
## 2. 建置 PM Taste Agent [09:28]
在 Claude Code 終端機中，給予一個結構化 Prompt 即可快速建立 PM Agent：

- **資料來源**：Pull GitHub Discussions、GitHub Issues、Releases
- **評分維度**：Bug vs Feature、Reactions 數量、留言數、時間近效性
- **輸出格式**：Markdown 報告，包含 Top Pain Points、Feature Requests、Themes，按 P0–P3 優先級排列
- **自動化**：搭配 Claude Loop Skill 設定成 Cron Job，每小時自動更新報告

> **關鍵概念：Priority Scoring（優先級評分）** — Agent 主動對每個 Issue 賦予重要性分數，取代 PM 人工篩選。

***
## 3. One-Command Instrumentation [19:00]
過去需要工程師協助的 Tracing 設置，現在只需一行指令 `npx skills add` 加入 Arize Phoenix Instrumentation Skill：

- Claude Code 自動掃描 Codebase，識別所有 LLM Calls 與 Tool Calls
- 自動接入 Tracing Layer，數據即時串流至 Arize 觀測平台
- **Trace** = Agent 完整步驟回放；**Span** = 單一離散步驟（Eval 的最小執行單位）

> **關鍵概念：Span-Level Evaluation** — Eval 應在 Span 層級執行，而非整體 Trace，「這個評分步驟的優先級判斷正確嗎？」比「整個執行結果好嗎？」更有診斷價值。

***
## 4. Vibe Evals vs. 精確 Evals [33:58]
Claude Code 可自動讀取 Traces 並建議 Evals 草稿（Vibe Eval），常見建議包含：

| Eval 類型 | 評估內容 |
|-----------|----------|
| Report Groundedness | 報告引用的 Issue 是否有真實數據支撐 |
| Priority Alignment | P0/P1 是否符合實際最高分 Issue |
| Report Actionability | 建議是否具體可執行 |

**但 Vibe Eval 只是 v0 草稿**，不知道你的 Bug-First 政策、歷史排序邏輯或「Critical」的定義，必須以人工 Judgment 持續校準。

> **關鍵概念：Axial Coding（軸心編碼）** — 從生產 Traces 中歸納錯誤類型，將 50 個 Error Spans 分類為 10 類失敗模式，作為 Eval 設計依據。

***
## 5. 自我改善閉環 [48:50]
最頂尖團隊已在運行的自動改善流程：

1. 抓取所有 Eval 觸發失敗的 Spans
2. 依失敗類別分組
3. 提出具體 Prompt 修正方案
4. **人工審核並批准**（這一步不可跳過）
5. 部署新版本 Agent

> **關鍵概念：Human-in-the-Loop Approval（人工核准節點）** — 自動化改善循環必須保留人類在 Approval 環節的判斷，防止 Eval 誤校準導致惡性循環。

***
## 6. Evals 也會過時 [隱含全程]
你的優先級會改變，Bug 政策會改變，產品本身也在改變。**上季度校準的 Eval 這季度就會開始誤判**，定期對齊人工反饋是常態維護，不是失敗的標誌。

***
# 技術/數據對比
| 概念 | 舊做法 | 新做法（本影片） |
|------|--------|----------------|
| Tracing 設置 | 需工程師配合 | `npx skills add` 一行指令 |
| Eval 設計起點 | 從零手寫規則 | Claude 從 Traces 自動建議 v0 |
| PM 日報 | 人工整理 GitHub | PM Agent 每小時自動產出 |
| 錯誤診斷 | 看整體輸出結果 | Span 層級精確定位 |

***
# 結論與行動建議
**🔥 啟發金句**
> **「程式碼已經很便宜了，能讓你脫穎而出的，是你對該建什麼的判斷力。」**

**📐 具體行動法則：T-E-L 法則**
> **Trace（追蹤）→ Eval（評估）→ Loop（循環改善）**
先讓 Agent 的每個步驟可見，再量化品質，最後自動驅動改善。

**💼 生活實踐建議（針對 AI PM）：**
- **本週末兩小時行動**：建立一個 Claude Code PM Agent，接入你的 GitHub Repo，一行指令完成 Instrumentation，看著第一條 Trace 進入 Arize Phoenix
- **企業 PM**：先從內部工具（而非面向用戶的產品）開始，建立一個幫你省 4 小時/週的 Agent，自然就會想要追蹤它
- **Eval 心態轉換**：Eval 回傳錯誤是好事，代表有改善空間，用 Span 層級的失敗案例作為下一輪 Prompt 優化的素材

***
# 參考連結
- 📺 原始影片：https://youtu.be/DL-pUGcfrf4?si=-4QyrdpDOCXO0dv0 [youtube](https://www.youtube.com/watch?v=pF4VZRU0qZA)
- 📝 完整文章：https://www.news.aakashg.com/p/how-to-run-evals-in-claude-code-with
- 📜 逐字稿：https://www.aakashg.com/how-to-build-a-self-improving-pm-agent-in-claude-code/
- 🔧 Arize Phoenix（開源）：https://arize.com
