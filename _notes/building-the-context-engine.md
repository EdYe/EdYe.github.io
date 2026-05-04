---
title: 'Context Engine：讓 AI 程式代理理解組織決策脈絡'
date: 2026-05-04
image: /images/影片筆記/building-the-context-engine.jpeg
category: 影片筆記
tags: [Context Engine, 組織脈絡, 知識圖譜, 衝突解析, 個人化檢索]
description: 'Context Engine（上下文引擎）是 AI 程式代理（Coding Agent）從「能產出程式碼」進化到「產出符合組織脈絡的正確程式碼」的關鍵缺口。'
quote: 'Access doesn't equal understanding — 存取資料不等於理解資料。'
action: '建立組織決策日誌（ADR），在 AI Agent 規劃階段附上歷史 PR 脈絡，手動扮演 Context Engine 角色感受差異。'
source_has_timestamps: true
---
## [核心摘要]
**Context Engine（上下文引擎）** 是 AI 程式代理（Coding Agent）從「能產出程式碼」進化到「產出符合組織脈絡的正確程式碼」的關鍵缺口。本演講由 Unblocked 產品負責人 Peter Werry 主講，揭示了 Naive RAG、MCP Server 堆疊、大型 Context Window 三大常見迷思，並提出以知識圖譜、個人化檢索、衝突解析為核心的 Context Engine 架構，解決 Agent 在執行任務時因缺乏「組織歷史決策脈絡」而陷入 Doom Loop 的根本問題。 [hackmd](https://hackmd.io/dDyP2WXdTjqtGMYevX0NdA)

***
## [詳細重點整理]
### 1. 問題背景：人類正在成為瓶頸 [00:00]
AI 代理從「自動補全」演進到「背景雲端 Agent 自主執行任務」，但隨著平行代理增多，工程師在多任務上下文切換時產生認知負荷。**組織脈絡（Organizational Context）** 的定義是：過去決策的「為什麼」——包括踩過的坑、遭拒的 PR、事故報告和 Slack 討論——這些正是讓有經驗的工程師比新人更有效率的核心資產。

> **關鍵概念：組織脈絡（Organizational Context）** — 不只是程式碼本身，而是驅動程式碼演進的所有決策歷程。

***
### 2. 三大迷思破解 [00:00 ~ 00:23]
| 迷思 | 為何不夠 |
|---|---|
| **Naive RAG over docs = Context Engine** | 會觸發「搜尋滿足效應」，找到第一個看似正確的答案就停止，錯過真正關鍵資訊（如過去 Slack 討論、事故報告） |
| **連接一堆 MCP Servers = 搞定** | Access ≠ Understanding；資料存取不等於理解資料間的關係與決策脈絡 |
| **更大的 Context Window = 解決問題** | 多數組織的脈絡資料量早已超過百萬 token；即使塞得進去，模型仍難以跨來源推理、辨別衝突與真偽 |

> **關鍵概念：Satisfaction of Search（搜尋滿足效應）** — 源自放射科醫學術語，Agent 找到第一個合理答案就停止搜尋，導致更重要的資訊被忽略。

***
### 3. Context Engine 的六大核心能力 [約 00:15 ~ 00:27]
- **統一系統上下文（Unified System Context）**：建立資料間的關係圖譜，不只是連結，而是理解「決策為何如此」
- **衝突解析（Conflict Resolution）**：初期以「最新 + 主分支優先」策略偏向，但仍需 LLM Judge 在執行時動態去衝突；無法解析時須主動告知使用者
- **個人化與定向檢索（Personalized Retrieval）**：依工程師的 PR 貢獻記錄，對其最常工作的 repo 做深度優先檢索，減少雜訊
- **資料治理與權限傳遞（Data Governance）**：私有 Slack 頻道資訊只提供給有存取權的使用者，合成知識需附帶 Group ID 標籤避免越權
- **Token 效率（Token Efficiency）**：有 Context Engine 的任務從 2.5 小時 / 2100 萬 tokens 縮短至 25 分鐘 / 1000 萬 tokens
- **歷史決策記憶（Organizational Memory）**：從歷史 PR review 評論中蒸餾出最佳實踐，儲存為組織記憶，供未來任務調用

> **關鍵概念：上下文蒸餾（Context Distillation）** — 從大量歷史資料（PR、Slack、Incident）中萃取組織最佳實踐，形成可被 Agent 調用的「組織記憶」。

***
### 4. 三大血淚教訓 [約 00:23 ~ 00:28]
1. **優化存取而非理解**：早期以為連接知識圖譜 + 工具就夠，事實是 Agent 無法自行推理資料間的深層關係
2. **隱藏衝突而非曝光**：用 naive 策略解析衝突後，未能曝光無法解決的部分；正確做法是主動讓人類介入修正並從反饋學習
3. **快取 Context Engine 的答案**：試圖重用答案以節省 token，但程式碼與組織知識持續變動，且錯誤答案會污染後續上下文，導致**回歸均值退化（Regression to the Mean）**

***
### 5. 最高價值應用場景 [約 00:25 ~ 00:28]
- **規劃階段（Planning）**：CP/ROI 最高，讓 Agent 在任務開始前取得完整組織脈絡
- **Code Review**：提供組織動機而非只看程式碼語法
- **Ticket 豐富化（Ticket Enrichment）**：自動補全新功能需求單的背景資訊
- **問題分類（Triage）**：即時拉出過去相關事故與討論
- **事故管理（Incident Management）**：整合 Sentry/Datadog 訊號與歷史 Slack 討論，自動關聯根因
- **工程支援頻道（Engineering Support）**：自動回答跨團隊技術問題，節省資深工程師時間

***
## [技術/數據對比]
| 指標 | 無 Context Engine | 有 Context Engine |
|---|---|---|
| 任務完成時間 | 2.5 小時 | **25 分鐘** |
| Token 消耗量 | 2,100 萬 tokens | **1,000 萬 tokens** |
| 正確性 | 錯過 legacy 相依性、重複已踩過的坑 | 正確處理向後相容、符合組織慣例 |

 [hackmd](https://hackmd.io/dDyP2WXdTjqtGMYevX0NdA)

***
## [結論與行動建議]
**啟發金句：**
> **「Access doesn't equal understanding — 存取資料不等於理解資料。」**

**核心法則：P-R-G 法則（Planning-Resolution-Governance）**
- **P**lanning 優先：Context Engine 在規劃階段投入產出比最高
- **R**esolve conflicts openly：衝突無法解析時，曝光給人類而非隱藏
- **G**overn permissions propagation：讓資料治理貫穿整個上下文合成流程

**生活實踐建議：**
1. **立即行動**：在下一個 AI Coding Agent 任務中，將規劃階段的 Prompt 明確附上「為何這樣設計」的歷史 PR/Ticket 連結，手動扮演 Context Engine 角色，感受差異
2. **中期建設**：建立組織的「決策日誌」Repo，記錄每個架構決策的 ADR（Architecture Decision Record），這是最低成本的 Context Engine 雛型
3. **長期投資**：評估 [Unblocked](https://www.unblocked.dev) 等工具，或自建以 Knowledge Graph + Personalized Vector Retrieval + Permission-Aware Synthesis 為核心的 Context Engine

***
## [參考連結]
- 原始 YouTube 影片：[https://youtu.be/5ID22ACI7IM](https://youtu.be/5ID22ACI7IM) [hackmd](https://hackmd.io/dDyP2WXdTjqtGMYevX0NdA)
- 主講人：Peter Werry，Unblocked 共同創辦人
- 活動：AI Engineer Conference，2026 年 5 月 3 日
