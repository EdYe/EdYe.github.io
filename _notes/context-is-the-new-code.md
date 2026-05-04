---
title: 'Context 即程式碼：CDLC 讓 AI 上下文可版控與可測試'
date: 2026-05-04
image: /images/AI筆記/context-is-the-new-code.jpeg
category: AI筆記
tags: [Context工程, CDLC, 規格驅動, LLM評審, 飛輪效應]
description: 'AI 編碼代理（Coding Agent）的時代，驅動代理的 Context（提示、規則、記憶）正取代程式碼成為軟體交付的核心資產。然而 Context 目前仍被當作臨時拼湊物管理，缺乏版本控制與測試'
quote: 'LLM 只是引擎，Context 才是燃料；給錯燃料，再好的引擎也跑不動。'
action: '檢視 agent.md / claude.md，確認每條規則都有對應的 Eval 測試案例；將常用 Context 提交到 Repo 與團隊共享。'
source_has_timestamps: true
---
# 📋 Context Is the New Code — Patrick Debois, Tessl

## [核心摘要]

AI 編碼代理（Coding Agent）的時代，**驅動代理的 Context（提示、規則、記憶）正取代程式碼成為軟體交付的核心資產**。然而 Context 目前仍被當作臨時拼湊物管理，缺乏版本控制、測試與觀測。Patrick Debois（DevOps 之父）提出「**Context Development Lifecycle（CDLC）**」——涵蓋 Generate、Evaluate、Distribute、Observe 四大環節，讓 Context 成為可重複、可改善的工程實踐，並透過飛輪效應持續強化 AI 輸出品質。

***

## [詳細重點整理]

### 1. 為何 Context 是新程式碼 [00:48]

曾經需要大量撰寫的程式碼，現在只需告知 AI「請先判斷用戶的套件管理器，再依生態系執行步驟」即可解決。程式碼正被轉化為**可重用的 Skill（技能）與工作流（Workflow）**。如同 2009 年 DevOps 問「如果 Ops 像 Dev 一樣運作？」，現在的問題是：「如果 Context 就是 Code，我們該如何工程化管理它？」

**關鍵概念：Context-as-Code**（將 Context 視為正式工程產物管理）

***

### 2. Generate：生成 Context [03:50]

Context 的來源多元，包含：
- **手動提示（Prompting）**：最基礎的人工輸入
- **可重用指令檔**：如 `agent.md`（各代理工具趨向統一格式）
- **外部文件匯入**：注入最新 Library 文件，防止 LLM 幻覺版本錯誤
- **MCP 整合**：從 GitLab、GitHub、Slack、票務系統拉取即時 Context
- **Spec-Driven Development**：將規格書（Specification）交由 Agent 拆解為逐步計畫

**關鍵概念：Spec-Driven Context Generation**（規格驅動的 Context 生成）

***

### 3. Evaluate：測試 Context [06:26]

修改兩行 `agent.md` 後，你是否知道它的實際影響？Context 必須有測試機制：
- **Linting**：驗證 Context 格式是否符合規範（如描述長度、欄位完整性）
- **Grammarly 式語意驗證**：讓 LLM 判斷 Context 是否清晰易懂
- **LLM-as-Judge 單元測試**：給定 Context，產生程式碼，讓另一 LLM 判斷輸出是否符合規則（如 URL 前綴是否為 `/awesome`）
- **端對端沙箱測試**：Judge 擁有工具執行能力，實際 `curl` 驗證行為
- **CI/CD 整合 + 錯誤預算（Error Budget）**：因 LLM 非確定性，需多次執行（如 5 次）計算通過率，而非單次判斷

**關鍵概念：Context Evals with Error Budget**（帶有容錯預算的 Context 評估機制）

***

### 4. Distribute：分發 Context [13:59]

Context 也需要像程式碼一樣可被打包與分發：
- **Git Repo 共享**：最低摩擦的起點
- **Context 套件（Package）**：將跨專案、跨團隊可重用的 Context 打包
- **Registry 市集**：如 Tessl Registry，供搜尋與安裝技能包（但目前品質良莠不齊）
- **依賴地獄（Dependency Hell）**：Context 套件間的版本衝突問題已浮現
- **安全掃描**：Snyk 等工具開始掃描 Context 是否含憑證洩漏或 Prompt Injection
- **AI SBOM**：記錄 Context 用哪個模型產生，類比軟體物料清單（SBOM）

**關鍵概念：Context Package Registry + AI SBOM**

***

### 5. Observe：觀測 Context 效能 [17:49]

Context 在實際使用中的回饋是持續改善的關鍵：
- **Agent 日誌分析**：標準化格式（Agent 日誌標準正在建立）讓組織能發現「哪些 Context 經常缺失」並統一補足
- **PR 回饋即 Context 回饋**：PR 被指出問題，代表生成該 PR 的 Context 需要改善
- **生產環境監控**：代碼上線後失敗，系統自動標記「哪些改動導致錯誤」並產生測試案例
- **Context Filter（上下文過濾器）**：類似 Web Application Firewall，在 Context 載入前過濾 Prompt Injection 與危險模式

**關鍵概念：Context Flywheel**（觀測回饋 → 改善 Context → 更好輸出 → 更多觀測，形成飛輪）

***

## [技術/概念對比]

| 傳統軟體工程 | Context 工程（CDLC） |
|---|---|
| 撰寫程式碼 | 撰寫 Prompt / Skill / agent.md |
| 單元測試 / E2E 測試 | Context Evals（LLM-as-Judge）|
| CI/CD 管線 | 帶 Error Budget 的 Eval Pipeline |
| Library / Package | Context 套件 / Skills Package |
| Package Registry（npm/pip）| Context Registry（Tessl 等）|
| SBOM（軟體物料清單）| AI SBOM（Context 來源追蹤）|
| WAF（Web 應用防火牆）| Context Filter（Prompt Injection 防護）|
| 生產觀測（APM）| Agent 日誌分析 + 生產回饋循環 |



***

## [結論與行動建議]

**啟發金句：** 「LLM 只是引擎，Context 才是燃料；給錯燃料，再好的引擎也跑不動。」

**具體行動建議（G-E-D-O 法則）：**
> **Generate（生成）→ Evaluate（評估）→ Distribute（分發）→ Observe（觀測）**，循環優化，建立 Context 飛輪。

**生活實踐建議：**
1. **立即行動**：檢視你的 `agent.md` / `claude.md`，確認每條規則都有對應的 Eval 測試案例
2. **團隊協作**：將常用 Context 提交到 Repo，讓團隊成員共享，而非用 Slack 傳貼
3. **建立回饋習慣**：每次 PR 被指出問題時，問自己「我應該在哪個 Context 檔案裡加入這個規則？」
4. **語音編碼**：Patrick 親身推薦，語音輸入比打字更能產生詳細、高品質的 Context

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/bSG9wUYaHWU
- 👤 講者 LinkedIn：https://www.linkedin.com/in/patrickdebois/
- 🐦 講者 Twitter/X：https://x.com/patrickdebois
- 🛠️ 相關產品：Tessl（https://tessl.io）
