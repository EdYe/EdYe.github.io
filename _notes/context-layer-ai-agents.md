---
title: 'AI Agent失敗真相：上下文才是關鍵'
date: 2026-07-18
image: /images/影片筆記/context-layer-ai-agents.jpg
category: 影片筆記
tags: [上下文層, 公司大腦, 複利學習迴圈, 上下文即IP, Context Sprawl]
description: 'Atlan共同創辦人Prukalpa Sankar揭示AI Agent失敗真因：非模型不夠聰明，而是缺乏業務上下文，績效=智力×上下文。'
quote: '💡「當你與競爭對手擁有相同的模型與相同的智力時，差異化來自你的上下文——上下文就是你的 IP。」'
action: '🎯依M-I-C-E法則（挖掘Mine、整合Integrate、複利Compound、演化Evolve）打造企業Context Layer，並建立如Code Review般的Context Review流程。'
source_has_timestamps: true
---
# WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar

***

## [核心摘要]

本場演講由 Atlan 共同創辦人 Prukalpa Sankar 主講，揭示 AI Agent 在生產環境中失敗的根本原因：**不是模型不夠聰明，而是缺乏業務上下文（Context）**。她提出「績效 = 智力 × 上下文」的框架，說明模型智力在過去十年成長了 1000 倍，但企業上下文幾乎原地踏步。她進一步描繪「Context Layer」的架構藍圖——一個類似 GitHub 的上下文管理系統，具備版本控制、依賴管理、品質治理與複利學習迴圈，讓 Agent 能像人類團隊一樣共享知識、持續學習，最終將企業文化與規範編碼為真正的智慧資產（IP）。 [web.archive](https://web.archive.org/web/20190710043004/https:/www.youtube.com/watch?v=ransFQVzf6c)

***

## [詳細重點整理]

### 1. Context 的時代來臨 [00:12]

2026 年被稱為「Context 之年」。Atlan 共同創辦人提出，在網際網路時代 Bill Gates 說「內容為王」，而在 Agentic 時代「上下文為王」。每隔幾天就有新的 Context 相關概念出現——Context Graph、Context Layer 等。但真正的問題是：模型指數級變聰明的同時，實際有用性卻未同步提升。僅 1/5 的 AI 用例進入生產環境，56% 的 CEO 認為 AI 目前帶來零財務效益。

**關鍵概念：Context Moment（上下文時刻）**

***

### 2. 績效 = 智力 + 上下文 [01:51]

認知智力（IQ）僅能解釋 10% 的工作績效變異。現實世界中，最聰明的人未必是最佳隊友——最佳隊友是學習最快、最能接受回饋的人。同樣地，模型 Benchmark 衡量的是「智力」（認知馬力），但「上下文」（業務情境知識）才是決定實際表現的關鍵變數。

過去十年，智力成長了 1000 倍，過去半年又翻了 2 倍；然而上下文——企業的情境知識——幾乎沒有移動，仍卡在儀表板、Slack 訊息串、即將離職的分析師腦中。

**關鍵概念：Performance = Intelligence × Context（績效等式）**

***

### 3. 人類學習模型：Maya 的故事 [04:27]

以虛擬分析師 Maya 為例，當加盟店主問「為什麼本週得來速時間上升？」這看似簡單的問題，實際需要四層知識：

- **事實知識**：什麼是得來速時間？誰在問？本週的定義與截止時間？
- **專業知識**：Q3 是季節性季度，需檢查天氣因素；上季推出新產品，需確認是否為根因
- **規範知識**：提問者的角色定位，如何客製化回答

Maya 如何學會這些？不是靠入職訓練，而是透過**觀察最佳隊友、犯錯、接收主管回饋、處理邊界案例**。這是人類在職場中累積上下文的方式。

**關鍵概念：On-the-job Learning（在職學習迴圈）**

***

### 4. Agent 架構演化：從專用 Agent 到通用 Agent [07:20]

**Era 1 — 專用 Agent（18 個月前）**：Atlan 從客服團隊開始，做 Jobs-to-be-Done 分析，針對特定任務建構個別 Agent（如健康情報 Agent「Hermione」、財務風險 Agent「MoneyPenny」）。初期有效，但暴露出四大問題：

- **Context Engineering 瓶頸**：建 Agent 只要 5 分鐘，但讓它具備業務上下文卻耗時無比
- **孤島效應**：各 Agent 各自為政，行銷更新定位後，SDR Agent 仍用舊版話術
- **除錯困難**：出錯時無法追溯是模型、Agent 還是 Context 的問題
- **Context Sprawl（上下文蔓延）**：各 Agent 擁有獨立記憶系統，學習不一致，難以定義單一真相來源
- **技術綁定風險**：12 個月內從 Relevance → Google ADK → Glean → Claude Code → Codex，每次切換 Context 都被困在原系統中

**關鍵概念：Context Sprawl（上下文蔓延）**

***

### 5. 轉向通用 Agent 與共享上下文 [11:06]

回到人類世界的啟發：Maya 不是孤星，而是夢幻團隊的一員。夢幻團隊建立在**共享上下文**之上——共享語言、共享真相圖像、共享 Playbook、共享決策權限、複利學習迴圈、共享記憶。

新架構的核心概念：各領域專家負責建構各自的技能（Skills），全部匯入一個共同的「公司大腦」（Context Layer），再透過檢索機制與通用 Agent 互動。

**關鍵概念：Shared Context（共享上下文）**

***

### 6. 行銷團隊實戰案例 [12:43]

Atlan 行銷團隊實際建構了 Context Layer。左側連接所有系統（社群平台、廣告平台、分析平台），中間是 Context Layer，右側是多種 Agent（Claude Code、Co-work、自有 Slack Bot、Qualified、Artisan）。

Context Layer 包含：
- **Data Graph（資料圖譜）**：自動化廣告 Agent 每日需知道從哪張表拉資料
- **Skills Library（技能庫）**：最佳 SEO 專家建構 SEO 技能，最佳競爭情報專家建構競情技能
- **Semantics & Metrics（語義與指標）**：ARR 如何定義？什麼是合格 Lead？
- **Org Structure & Entities（組織結構與實體）**

6 個月內，團隊建立了約 **300 個 Skills 和 40 個 Agents**。

**關鍵概念：Company Brain（公司大腦）**

***

### 7. Context Layer 的三大核心挑戰 [14:36]

將上下文管理如程式碼般治理時，浮現三大問題：

- **依賴管理**：競爭情報技能 → 類別定位技能 → 銷售戰卡技能，上游技能變動會破壞下游，技能快速過時與漂移
- **品質歸屬**：誰最終負責技能品質？
- **安全與治理**：Secrets 硬編碼在 .env 檔中，公開 Skill Repo 被隨意下載

**關鍵概念：Context as Code（上下文即程式碼）**

***

### 8. 定義 Context Layer：Context 的 GitHub [15:31]

Context Layer 需解決的核心問題：

- **生命週期管理**：版本控制、協作、分支管理（Local Context vs Global Context）
- **技能 Profile**：技能是否能像程式碼一樣擁有 Profile 與自學迴圈
- **品質管理**：影響範圍分析、審批者/維護者/貢獻者角色定義
- **安全態勢管理**：內建安全與治理機制

**關鍵概念：GitHub for Context（上下文的 GitHub）**

***

### 9. 複利學習迴圈與 Traces [16:43]

每次 AI 互動都會產生更多上下文——這是金礦。關鍵在於部署專門的 Harness，從 Traces 中逆向萃取知識，回饋到維護者迴圈：「Approve, Reject, Approve, Reject, Improve」。這形成了**複利學習迴圈**，讓 Context Layer 隨時間持續增值。

**關鍵概念：Compounding Learning Loop（複利學習迴圈）**

***

### 10. 如何開始建構公司大腦 [17:18]

上下文隱藏在企業系統中。透過連接 Salesforce、HubSpot、Data Warehouse、Application Layer，逆向建構這些系統之間的關聯。目前上下文在每個資料傳遞環節都會流失，但若能逆向建構並部署 AI 於其上，就能精準地建立公司大腦的第一版。

**關鍵概念：Reverse Context Construction（逆向上下文建構）**

***

### 11. Context Layer 架構總覽 [18:07]

完整架構包含四大元件：

- **持續挖掘**：從業務系統持續萃取上下文
- **公司大腦**：統一儲存與管理知識、技能、語義、指標
- **Context 開發生命週期**：技能開發、版本管理、部署
- **多元檢索機制**：MCP、SQL、Vector Retrieval、Hybrid Assembly

同時從 Traces 回收，建立複利學習迴圈。

**關鍵概念：Context Layer Architecture（上下文層架構）**

***

### 12. 結論：Context is IP [19:31]

現今大多數人仍以硬編碼方式建構 Agent 的上下文。這在規模化時將變得不可持續且危險——如同業務和財務會給出不同的營收數字，我們正快速邁向自主系統也出現同樣分歧的時刻。

當你與競爭對手使用相同模型、相同智力時，差異化來自你的業務運作方式。Context 是將企業文化與規範編碼為智慧資產的方式。

**關鍵概念：Context as IP（上下文即智慧資產）**

***

## [技術/數據對比]

| 維度 | 智力（Intelligence） | 上下文（Context） |
|---|---|---|
| 過去十年成長幅度 | 1000 倍 | 幾乎零成長 |
| 過去半年成長 | 2 倍 | 微幅 |
| 衡量方式 | Benchmark 測試 | 無標準化衡量 |
| 儲存位置 | 模型權重 | 儀表板、Slack、人腦 |
| 對績效的解釋力 | 約 10%（IQ） | 主要決定因素 |

| Agent 架構階段 | 專用 Agent（Era 1） | 通用 Agent + Context Layer |
|---|---|---|
| 部署速度 | 快（5 分鐘） | 需建構基礎設施 |
| 上下文管理 | 各自獨立、孤島化 | 集中管理、共享 |
| 學習方式 | 各自學習、不一致 | 複利學習迴圈 |
| 技術綁定風險 | 高（Context 被困在各系統） | 低（開放標準 MCP/Iceberg） |
| 規模化能力 | 不可持續 | 可持續擴展 |

| Atlan 行銷團隊成果 | 數據 |
|---|---|
| 建構 Skills 數量 | 約 300 個 |
| 部署 Agents 數量 | 約 40 個 |
| 建構週期 | 6 個月 |

***

## [結論與行動建議]

> **啟發金句：「當你與競爭對手擁有相同的模型與相同的智力時，差異化來自你的上下文——上下文就是你的 IP。」**

**具體行動法則：M-I-C-E 法則（Mine-Integrate-Compound-Evolve）**

- **Mine（挖掘）**：從現有業務系統（Salesforce、HubSpot、Data Warehouse）逆向建構上下文圖譜
- **Integrate（整合）**：將上下文集中至統一的 Context Layer，建立版本控制與依賴管理
- **Compound（複利）**：部署 Trace 回收 Harness，讓每次互動都回饋為可審批的知識增量
- **Evolve（演化）**：透過複利學習迴圈持續迭代技能，避免上下文漂移與過時

**生活實踐建議**：在日常產品開發中，將「上下文工程」視為與「Prompt Engineering」同等重要的學科。下次設計 AI Agent 時，先問自己：「如果這個 Agent 是新員工，它需要知道哪些業務定義、診斷 Playbook 和組織規範？」將這些知識結構化為可版本控制、可測試、可移植的 Skill，而非硬編碼在 Prompt 中。建立一個「Context Review」流程，就像 Code Review 一樣，讓團隊共同維護公司大腦的品質。

***

## [參考連結]

- 原始 YouTube 影片：[https://youtu.be/8G_1-3IO4ZQ](https://youtu.be/8G_1-3IO4ZQ)
- 講者 Prukalpa Sankar Twitter：[https://x.com/prukalpa](https://x.com/prukalpa)
- Atlan 官網：[https://atlan.com](https://atlan.com)
