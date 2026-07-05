---
title: '雙Agent架構：用AI建造AI的自我修復法'
date: 2026-07-05
image: /images/AI筆記/agents-building-agents.jpg
category: AI筆記
tags: [AutoAgent, Golden Dataset, Harness Engineering, 自我修復評測, 失效叢集分析]
description: '本片核心揭示了「用 AI 建造 AI」的系統工程方法,解決了 AI Agent 開發中精準度低、難以迭代、且難以規模化維運的痛點。講者提出雙 Agent 架構——由 Coding Agent 擔任建造者'
quote: '💡AI is very powerful and very good at building any type of software... so we are using AI to build AI.'
action: '🎯依序建立 Golden Dataset、Eval Loop 與 Harness 三大基礎設施（G-E-H 法則），讓 Coding Agent 能安全自主迭代 Agent。'
source_has_timestamps: true
---
## 核心摘要

本片核心揭示了「**用 AI 建造 AI**」的系統工程方法,解決了 AI Agent 開發中精準度低、難以迭代、且難以規模化維運的痛點 。講者 Alfonso Graziano 提出雙 Agent 架構——由 Coding Agent(如 Claude Code)擔任建造者,自動修正目標 Agent 的程式碼、System Prompt 與工具邏輯,並透過自我修復評測(Self-Healing Evals)機制持續迭代收斂,讓 Agent 開發從「Prompt 調試」進化為可規模化的「系統工程」。 [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

## 詳細重點整理

1. AI Agent 的核心問題與架構 [00:00]
業界普遍追求 AI Agent 自動化,但其非決定性(Non-deterministic)本質帶來幻覺、延遲、成本等問題。講者將 Agent 拆解為「LLM(大腦)+ 工具 + 上下文 + Agentic Loop」的基本元件 。**核心概念:Agentic Loop 三元素模型**。 [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

2. Golden Dataset 與評測失效模式 [03:28]
Golden Dataset 是與領域專家共建的測試集,定義輸入與預期輸出(包含工具呼叫鏈),作為非決定性系統下的「測試套件」基準 。一個未配備工具的裸 Agent,初始通過率僅 18%,失效原因多來自缺少工具、System Prompt 不完整或上下文檢索能力不足。**核心概念:黃金資料集(Golden Dataset)即非決定性系統的回歸測試基準**。 [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

3. AutoAgent——自主優化迴圈 [08:23]
受 Andrej Karpathy 的 AutoResearch 啟發,講者打造 AutoAgent,讓 Coding Agent 自動執行評測、修改程式碼、嘗試新 Prompt 與新工具,並驗證成效 。在簡單案例中通過率從 18% 提升至 83%(約 10 次迭代),在已被人工優化過的正式環境 Agent 上仍額外提升 10% 準確率,證明機器能找到人類未發現的優化路徑。**核心概念:AutoAgent 自主優化迴圈**。 [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

4. AutoAgent 運作機制細節 [11:30]
流程為:建立優化任務(以 Markdown 定義目標、倉庫、指標)→ 產生基準報告 → 每輪迭代開新分支、提出假設、修改 Agent、跑評測 → 若改善則延續、若退化則回溯(Rollback)。人類角色聚焦於初始情境設計與「護欄」設定(例如禁止直接竄改評測標準作弊)。真實案例中,正式環境 Agent 的準確率從 67% 提升至 86%,主要透過修正 System Prompt、工具描述與邏輯。**核心概念:假設驅動的分支回溯機制(Hypothesis-Branch-Rollback)**。 [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

5. 真實使用數據的失效模式 [19:00]
第二類問題來自上線後的真實用戶數據,透過使用者回饋(讚/倒讚 + 留言)或領域專家標註追蹤紀錄(Trace)蒐集問題 。**核心概念:即時數據回饋迴圈(Live Data Feedback Loop)**。 [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

6. Trace 叢集分析與修復流程 [23:22]
收集大量帶回饋的 Trace(案例中達 114 筆)後,Coding Agent 對失效模式進行叢集分析與根因推論,產出包含正負回饋率、根因與修復建議的完整 Markdown 報告 。團隊再進行人工三角驗證(Triage)、與領域專家確認後決定修復、延後或捨棄,修復後的失效模式會回寫進 Golden Dataset 防止迴歸。**核心概念:失效叢集分析(Failure Cluster Analysis)**。 [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

7. Harness Engineering 基礎架構 [27:59]
講者總結 AutoAgent 與真實數據修復流程之所以可行,核心在於「Harness Engineering」——為 Coding Agent 打造可靠工作環境,包含規格驅動開發(Spec-Driven)、品質關卡(Linting、單元測試、評測、LLM Code Review)、上下文工程與可觀測性 。**核心概念:harness 工程(治理與護欄基礎設施)**。 [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

## 結論與行動建議

**啟發金句:** "AI is very powerful and very good at building any type of software... so we are using AI to build AI." [youtube](https://www.youtube.com/watch?v=0TpFf_TOuhU)

**具體行動建議——G-E-H 法則:** Golden Dataset(建立黃金測試集)→ Eval Loop(建立自我修復評測迴圈)→ Harness(打造規格、護欄與可觀測性基礎設施),三者缺一不可,才能讓 Coding Agent 安全自主迭代。

**生活實踐建議:** 對於 AI 應用架構師而言,可將此模式應用於日常 PM 工作流——先用真實使用者回饋建立「失效叢集」清單,再交由 Coding Agent 產出修復假設與報告,人類只負責驗證與拍板,大幅縮短迭代週期。

## 參考連結

https://youtu.be/aHhB3sjGjkI?si=G1JrA6MwXv-piyt5
