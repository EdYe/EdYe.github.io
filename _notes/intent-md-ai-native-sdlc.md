---
title: 'Claude Code 的 INTENT.MD：AI 原生 SDLC 工件鏈'
date: 2026-09-02
image: /images/AI筆記/intent-md-ai-native-sdlc.jpg
category: AI筆記
tags: [AI原生SDLC, intent.md, 工件鏈, 發佈閘門, 事件驅動維護]
description: 'Anthropic 發布《AI 原生 SDLC 指南》：代理壓縮建置成本（約 2 倍速）後，瓶頸已從程式碼移轉到交付流程本身。解法是以 intent.md 啟動「意圖→規格→計畫」工件鏈，靠 Hook、Evals 與發佈閘門治理全流程。'
quote: '程式碼已不再是瓶頸——你的交付流程才是；AI 時代的競爭，是流程設計的競爭。'
action: '🎯依 I-S-P-G 法則：Intent 先讓代理訪談你、把腦中意圖寫成 intent.md 才動工；Spec 意圖簽核後用 Hook 自動派生規格；Plan 把計畫逼問到「可獨立交接」的自足狀態；Gate 每次推進都過決定性閘門（Lint、測試、Evals、發佈核准）。'
source_has_timestamps: true
source_raw: Claude Code 的全新 INTENT.MD 是什麼
---
**影片資訊**：Rob Shocks 頻道・2026-09-01・長度 16:21

## [核心摘要]

Anthropic 發布《AI 原生 SDLC 指南》：代理壓縮建置成本（約 2 倍速）後，瓶頸已從程式碼移轉到交付流程本身。解法是以 intent.md 啟動「意圖→規格→計畫」工件鏈，靠 Hook、Evals 與發佈閘門治理全流程，再以事件驅動實現代理自主維護，人類只留守關鍵審查點，解決 AI 產能爆發、流程卻跟不上的痛點。 [youtube](https://www.youtube.com/watch?v=LoMOPj-lO8U)

## [詳細重點整理]

### 1. AI 原生 SDLC 範式轉移 [00:00]

- 傳統 SDLC 為「規劃→設計→建置→測試→部署→維護」的循環，其中建置階段最耗時、最昂貴；代理（agent）出現後，這段被大幅壓縮，團隊速度提升約 2 倍。
- 核心命題翻轉：程式碼已不再是瓶頸，**你的軟體交付流程才是**——下一步是把代理擴散到其餘所有階段，持續壓縮每個環節的人力時間。

關鍵概念：**瓶頸移轉（Bottleneck Shift）**

### 2. Intent.md 發現階段 [01:08]

- 傳統規劃靠需求會議、PRD、工作坊與利害關係人訪談；新流程改為讓代理反覆「訪談」你，直到完全理解功能或臭蟲，把你的領域經驗與脈絡傾倒進對話，再沉澱為 intent.md——一份**人類可讀、機器可執行**的檔案。
- 實作慣例：在專案中建立 `intent/` 資料夾存放 intent.md；可用的訪談工具包括 Switch Dimension Discovery、Matt Pocock 的 Realm、Cursor 的需求探索。
- **意圖發起者（Originator）**不必是專家：客戶報臭蟲、PM 提功能、開發者記錄流程改善都能發起，事後與代理一起覆核修正。
- 產品負責人以 backlog 形式審視這些意圖檔（可為排序的 Markdown、Notion 或 Linear），甚至可讓代理自動分診（front-end、任務大小、功能類型、優先級）。

關鍵概念：**工件鏈（Artifact Chain）**——intent → spec → plan 逐級派生

### 3. 規格自動生成與治理 [04:37]

- intent.md 一經提交或簽核，透過 Hook 或流程自動生成 spec.md；官方範本提示詞為「讀取 intent.md，產出需求與設計規格，套用可用 skills 與品牌規範，完整寫入 spec.md」。
- 可用 Cursor／Claude Code／Codex 原生 plan mode，或自建客製 skill；沒有一體適用，但**工作流必須標準化且不要頻繁變動**，讓團隊、代理與 skills 都對齊同一套流程。
- 治理手段：以 agents.md、skills、政策與風格指南約束每個工件的生成，確保組織最佳實踐被貫徹到整條工件鏈。
- （贊助段落 [06:02]：Neon 資料庫平台，主打 agent-first 的資料庫分支與 MCP／CLI／skills 整合。）

關鍵概念：**規格即派生（Spec-as-Derivative）**

### 4. 建置循環：Plan.md 的自足性與代理分工 [06:52]

- 工程師把 intent + spec 餵入 plan mode 產出 plan.md，並反覆質問計畫「哪些變更可能弄壞東西」，直到 plan.md **可獨立交接**——交給任何一位工程師（或另一個代理）都能不回看原始文件直接實作。
- 各階段由**獨立的代理與子代理**處理，彼此不共享對話記憶，全靠文件交接——這是為什麼每份工件都必須自足。
- 計畫解剖學：要改的檔案、工作順序（to-do）、風險、約束、以及證明（成功標準＋**決定性驗證**：Lint 與測試，非黑即白）。
- 治理與速度：版本化保存 intent／spec／plan 及其演進軌跡，才能追蹤領先與落後指標、驗證 **DORA 指標**與 AI 實際效益；透過鎖定權限（可用的工具、網路來源、套件白名單）換取 auto mode 的高速，並控制代理的**爆炸半徑**。
- 平行化：以 Git worktree 讓多代理同時開工；以 Hooks 做護欄——實作完成後自動回寫計畫、封鎖禁入資料夾、擋下未簽核的 NPM 套件。

關鍵概念：**自足交接（Self-Contained Handoff）**

### 5. 測試與 Evals：讓人類最後再碰 [10:42]

- 傳統測試卡在等 QA 排程；新流程要求代理在人類介入前完成盡可能多的測試：自行撰寫測試並確保通過、Lint、建置、端到端審查。
- 進階玩法：用 Playwright、TDD、Cursor Browser 讓代理實測軟體、截圖，甚至自行啟動 server 測試並附上螢幕錄影。
- **持續評估（Evals）**：收集約 20 個已解決的 issue 與預期結果，建立回歸集；每次更換模型、升級 skill 或重大流程變更時在 CI 中重跑，偵測 SDLC 是否退化。

關鍵概念：**回歸集（Regression Suite）**

### 6. 部署閘門與非同步代理審查 [12:22]

- 代理在自己的分支／worktree 完成變更後建立 Pull Request；另一個 Claude 實例**非同步**對照政策與安全協議審查，甚至由第二個 Claude Code 實例審查第一個的留言，各自掛載不同的 agents.md、skills、hooks 與 linting 政策。
- **發佈閘門**：可設定 Hook 阻擋部署，除非特定權限被授予、特定人員核准、或 release gate 條件達成。
- 最後再由安全／CI 預覽代理把關：決定性的 lint 與閘門檢查，加上 Cursor bug bot 或 Claude security review 掃描錯誤。

關鍵概念：**發佈閘門（Release Gate）**

### 7. 自主維護的未來 [13:46]

- 傳統維護是被動的：凌晨三點的告警、on-call、堆積到沒人理的 backlog 工單。
- AI 原生維護是**事件驅動**：資安事件、新工單、Slack 訊息或排程都能直接喚起 Claude，無需人類介入——它自行從日誌診斷、**替自己生成 intent.md**、提出修復建議，在你走到電腦前就已完成初步診斷。
- 觸發範例：監控指標偵測到頁面掛掉或 API rate limit 暴增，即自動啟動診斷代理。

關鍵概念：**事件驅動維護（Event-Driven Maintenance）**

### 8. 導入心法：沒有一體適用 [15:25]

- 全程宗旨：代理參與整條 SDLC 而非只有建置，壓縮每步的人力時間，但**人類仍留守關鍵審查點**；人機比例依任務危險度（criticality）調整。
- 已在用 Superpowers、BMAD 或自製工作流的團隊不必推倒重來；可行光譜從簡單迴圈、graph engineering、全自動迴圈、大型編排系統一路到文明工程（civilization engineering）。

關鍵概念：**人機比例調節（Human-in-the-Loop Calibration）**

## [技術/數據對比]

| 環節 | 傳統 SDLC | AI 原生 SDLC |
| --- | --- | --- |
| 瓶頸 | 建置階段最耗時昂貴 | 建置壓縮、速度約 2 倍，瓶頸移轉至流程 |
| 規劃 | 需求會議、PRD、工作坊 | 代理反覆訪談發起者，沉澱為 intent.md |
| 規格 | 人工撰寫、手動交接 | intent 簽核後由 Hook 自動生成 spec.md |
| 建置 | 單一工程師依規格實作 | 多代理＋子代理以 worktree 平行分工 |
| 測試 | 等 QA 排程，回饋圈數天 | 代理先寫測試、Lint、E2E、截圖與錄影 |
| 審查部署 | 同步人工 code review | 代理非同步審查＋安全掃描＋Hook 閘門 |
| 維護 | 被動回應告警（凌晨 on-call） | 事件觸發代理自主診斷並生成修復 intent |

## [結論與行動建議]

**啟發金句**：程式碼已不再是瓶頸——你的交付流程才是；AI 時代的競爭，是流程設計的競爭。

**具體行動建議**：「I-S-P-G 法則」
- **I**ntent：先讓代理訪談你，把腦中意圖寫成 intent.md 才動工
- **S**pec：意圖簽核後，用 Hook 自動派生規格
- **P**lan：把計畫逼問到「可獨立交接」的自足狀態
- **G**ate：每次推進都過決定性閘門（Lint、測試、Evals、發佈核准）

**生活實踐建議**（對接你目前的 Gitea + MCP + Actions + Webhook 技術棧）：
- 在既有專案根目錄建立 `intent/` 資料夾與 intent.md 模板，養成「先訪談、後動工」的肌肉記憶。
- 用 Gitea Webhook 觸發 Actions（或 Claude Code hooks），在 issue 貼上 accepted 標籤時自動生成 spec.md，把工件鏈接上你自己的 CI。
- 收集約 20 個已解決 issue 與預期結果建立 Evals 回歸集，每次換模型或升級 skill 就重跑一次，防止「升級反而退化」。
- 把「代理非同步審查 PR + 發佈閘門」的導入評估，包裝成你規劃中 AI 顧問／架構審查副業的第一個標準化服務項目。

## [參考連結]

- [原始 YouTube 影片](https://youtu.be/LoMOPj-lO8U) [youtube](https://www.youtube.com/watch?v=LoMOPj-lO8U)
- [Anthropic 官方指南：The AI-Native SDLC Playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)
- [Switch Dimension 課程（講者的 AI SDLC 教學）](https://dub.sh/aisdlc)
- [Molten OS（講者的產品開發 skills 開源庫）](https://github.com/switch-dimension/molten-os-core)