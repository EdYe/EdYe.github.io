---
title: '從零打造 AI Agent：15章建構全紀錄'
date: 2026-07-12
image: /images/AI筆記/building-ai-agent-from-scratch.jpg
category: AI筆記
tags: [Harness架構, 上下文管理, 工具呼叫, 沙箱安全, 子代理委派]
description: '這部影片以「Agent = Model + Harness + UI」為核心架構，從零開始用 Python 逐步建構一個真實可運作的 Coding Agent'
quote: '💡提示詞是意圖，不是圍欄。不要告訴模型別碰機密——根本不給它機密。'
action: '🎯套用 M-H-U 法則檢視 AI Agent 專案：Model 可抽換、Harness 承載工程邏輯、UI 只做事件消費者，並確認具備上下文壓縮、審批閘道、驗證機制、可觀測性四項生產就緒指標。'
source_has_timestamps: true
---

## [核心摘要]

這部影片以「Agent = Model + Harness + UI」為核心架構，從零開始用 Python 逐步建構一個真實可運作的 Coding Agent，共 15 個章節、約 2,500 行程式碼。每一章新增一個原語（primitive），從無狀態的 LLM 呼叫出發，依序加入歷史記憶、指令系統、上下文交付、工具呼叫、上下文壓縮、技能載入、沙箱安全、持久化記憶、任務規劃、子代理委派、自我驗證、可觀測性追蹤，最終完成終端 UI。整套程式碼以 Git Tag 形式釋出（ch0→ch14），可逐章切換、實機運行，完整揭示了 AI Agent 背後的工程本質：真正讓模型「感覺像代理」的，全都在 Harness 層 。 [scribd](https://www.scribd.com/document/869199074/Links)

## [詳細重點整理]

### 1. 全局框架與三層架構 [00:00]

影片開場即定義核心等式：**Agent = Model + Harness + UI**。Model 是一個無狀態推理引擎，僅靠一次 API 呼叫；UI 是人類觸達代理的介面；真正讓代理「有感」的中間層——Harness——承載了迴圈、上下文、工具、沙箱、記憶等全部工程邏輯。三個套件各自獨立，依賴方向單向流動：UI → Harness → Model 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Harness（駕馭層）**

### 2. Ch 0 · 環境設定 [02:25]

介紹三個套件結構（UI、Model、Harness）與 Git Tag 倉庫運作方式。每個章節對應一個 Git Tag（ch0→ch14），切換至任意 Tag 即可獲得該階段的完整可運行代理。運行方式包含 `uv run demo`（播放章節腳本演示）、`uv run agent`（進入互動 REPL）、`uv run tui`（第 14 章後可用完整終端 UI）。 [scribd](https://www.scribd.com/document/869199074/Links)

### 3. Ch 1 · 裸模型 — 無狀態、單一 API 呼叫、無記憶 [05:08]

LLM API 本質上是無狀態的，一次請求進、一個答案出，呼叫之間不攜帶任何資訊。我們感受到的所有「對話記憶」，都是 Harness 將歷史訊息回饋給模型的結果，而非模型本身記得。本章僅建立一個 Agent 類別，包含單一 `send` 方法，每次呼叫都是獨立的聊天，不帶任何訊息列表 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Stateless LLM（無狀態語言模型）**

### 4. Ch 2 · 歷史訊息 — 訊息列表讓它「記住」 [06:49]

修復上一章遺忘問題的方式極簡：給 Agent 一個 `self.messages` 列表，每次對話先 append 使用者訊息、發送整個列表、再 append 回覆。整個差異只有三行程式碼——列表初始化與兩次 append。這是全片最重要的概念：**模型無狀態，Harness 保存對話並在每次呼叫時重播**。後續所有原語（指令、工具、記憶）都掛在這一個列表上 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Message List Replay（訊息列表重播）**

### 5. Ch 3 · 指令系統 — 系統提示 + AGENTS.md + 工作區 [08:10]

模型雖然記住對話，但每輪仍像陌生人。系統提示詞解決此問題：Harness 在每輪對話前 prepend 一條系統訊息，設定一次即永久生效。真實專案通常有一整份規則檔案，Harness 會自動載入工作目錄下的 `AGENTS.md`（與 Codex、Claude Code 採用相同慣例），將內建提示詞與 AGENTS.md 合併為單一系統訊息。本章同時引入 **Workspace（工作區）** 概念——代理擁有一個專屬目錄，所有路徑受限於此 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**System Prompt Layer（系統提示詞層）**

### 6. Ch 4 · 上下文交付 — 透過 @-引用拉入檔案 [09:37]

代理目前只能看到我們手動傳入的文字。本章引入 `@` 符號標記檔案路徑，Harness 在呼叫模型前掃描所有 `@` 引用，從磁碟讀取檔案內容，注入到使用者問題之前。目前為原始讀取（完整檔案），後續章節才處理大檔案的截斷 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**@-Reference Injection（@ 引用注入）**

### 7. Ch 5 · 工具呼叫 — 函式 + Schema、迴圈、審批閘道 [11:16]

工具本質上是「一個函式加上一個 JSON Schema」。工具存放於 `tools.py` 的註冊表中，向模型提供規格描述，再依名稱分派呼叫。關鍵分工：**模型決定呼叫什麼，Harness 決定如何執行並實際運行**。迴圈邏輯為：發送帶工具規格的請求 → 若模型觸發工具則執行 → 回傳結果 → 再次發送。Harness 目前上限六步以防止無限循環。安全措施包括：檔案工具限於工作區、Bash 在沙箱中運行（Docker 或本地子進程）、危險操作需通過審批閘道（Approval Gate）。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Tool = Function + Schema（工具 = 函式 + 綱要）**

### 8. Ch 6 · 上下文管理 — 壓縮（保留頭尾） [14:12]

一旦加入工具，每次呼叫與結果都堆積在對話中，歷史迅速增長。但上下文窗口有限，放任增長會導致模型漂移、重複自身、失去主線。Harness 承擔管理窗口的新職責，四種策略為：Select（選擇）、Compress（壓縮）、Write（寫出）、Isolate（隔離）。本章實作 Compress：當歷史超過 Token 預算時，將中段摘要為單一筆記，保護開頭與結尾（因為模型最可靠地讀取首尾）。另有 `clamp` 方法限制單一項目最大字元數，防止大檔案或工具輸出淹沒窗口 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Head-Tail Compaction（頭尾保留壓縮）**

### 9. Ch 7 · 技能系統 — 漸進式揭露的作業記憶 [16:58]

代理仍每次重新推導相同流程，缺乏「我們如何在這個倉庫做事」的記憶。技能（Skill）提供作業記憶：一個 Skill 就是一個目錄，包含 `skill.md`（名稱、描述、指令）。核心技巧是**漸進式揭露（Progressive Disclosure）**：系統提示詞中僅載入技能的一行描述，完整內容留在磁碟上，直到模型判斷相關時才透過已有的 `read_file` 工具讀取。至此系統提示詞自動載入三項內容：內建提示詞、AGENTS.md、技能描述 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Progressive Disclosure（漸進式揭露）**

### 10. Ch 8 · 沙箱與安全 — 預設封閉，逐一加固 [19:32]

代理運行程式碼，但所有程式碼至今都在我們自己的機器上運行。模型樂於請求執行任何操作——**提示詞是意圖，不是圍欄**。邊界必須存在於 Harness 中。策略為「Start Closed」：網路關閉、檔案系統受限、憑證不提供，再依爆炸半徑逐步開放。沙箱層級從 OS 沙箱到容器、用戶空間核心、微型 VM。Bash 工具改為在沙箱內運行；`read_file` 被限制在工作區內，無法讀取 `/etc/passwd`。核心法則：**不要告訴模型別碰機密，而是根本不給它機密** 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Start Closed（預設封閉）**

### 11. Ch 9 · 持久化狀態與記憶 — JSONL 會話 + 情節搜尋 [22:11]

代理至今在單一進程中運行，終止即遺失整個對話。Harness 將會話以 JSONL 格式寫入磁碟（`memory.py`），每行一條訊息。代理獲得 session 概念：啟動時載入歷史、每輪結束後儲存。終止進程後重新啟動，可從上次中斷處繼續。另加入 `search_memory` 工具——跨已儲存會話的純關鍵字搜尋（無嵌入向量），類似 Hermes Agent 的做法，是 Select 策略應用於歷史 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Episodic Memory（情節記憶）**

### 12. Ch 10 · 任務規劃 — 編排器 / 控制平面 [24:09]

單一迴圈無法處理多步驟任務——無法掛鉤、閘道或觀察各步驟。新增 Orchestrator 模組：**模型以 JSON 規劃步驟，Harness 驅動執行**。每步通過審批檢查、執行、失敗重試。Agent 迴圈本身不變，`main` 僅閘道一個 `/plan` 指令，將任務交給編排器。Harness 擁有工作流的形狀，Agent 仍負責實際工作 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Orchestrator Control Plane（編排器控制平面）**

### 13. Ch 11 · 子代理 — 委派 + 並行扇出，上下文隔離 [25:22]

多步驟任務仍共用單一上下文窗口，大量工具呼叫與死胡同會污染上下文。子代理（Subagent）為自包含子任務建立全新代理：獨立上下文、獨立工具、運行至完成、僅回傳答案而非完整對話記錄。提供兩個工具：`delegate`（單一子任務）與 `fan_out`（並行批次）。**上下文隔離本身就是一個特性**——兩個子任務並行執行，互不看到對方的推理過程，答案按順序返回 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Context Isolation（上下文隔離）**

### 14. Ch 12 · 驗證機制 — 沒有真實通過的運行，不算「完成」 [26:23]

代理完成任務後只回報「done」——但這是一句話，不是事實。Harness 不自行執行測試，而是**監看模型用 Bash 工具自行執行的測試記錄**，直到看到真實的通過結果（exit code 0）才接受完成。測試指令從 `AGENTS.md` 的 `testing` 區段讀取（可為 `npm test`、`go test`、`uv run verify` 等，語言無關）。閘道僅在當輪寫入程式碼檔案時觸發（依副檔名判斷），單純問問題不觸發 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Verification Gate（驗證閘道）**

### 15. Ch 13 · 可觀測性 — 追蹤器、Span、Token 成本、OpenTelemetry [28:11]

多步驟運行中斷時，可見的失敗幾乎從不是問題起點——真正的 bug 通常在三個工具呼叫之前。加入 Tracer，記錄每一步：模型呼叫、工具呼叫（含參數與結果）、驗證與規劃步驟。包含持續時間、Token 數量、成本（透過 Model 套件中的定價表計算，本地模型計為免費）。架構為一個 emit 對多個 sync——核心觸發 span 一次，透過事件縫隙可被多個消費者讀取：UI 面板、JSONL 檔案、控制台印表機、或 OpenTelemetry 相容收集器（如 Jaeger）。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Distributed Tracing（分散式追蹤）**

### 16. Ch 14 · 真實 UI — 終端 TUI（雙窗格、即時追蹤） [30:37]

三層架構完成閉環。終端 UI 以 `uv run tui` 啟動，提供雙窗格：左側對話、右側即時追蹤流（同樣的 span 來自可觀測性章節，顯示 Token 與成本）。審批閘道升級為 Modal 對話框，顯示檔案編輯的真實 unified diff。關鍵：UI 不重新實作代理，而是在 worker thread 中運行同一個代理，渲染 Tracer 記錄的內容。UI 套件是唯一匯入 Textual 的套件——**好的 UI 是事件的消費者，而非擁有者** 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**UI as Event Consumer（UI 即事件消費者）**

### 17. 回顧 — 約 2,500 行，Harness 才是代理的本質 [32:19]

從空檔案到可運行代理，15 章每章一個原語。模型幾乎未變——權重完全不變——是 Harness 將模型轉化為代理。約 2,500 行 Python，運行在我們自己的機器上的模型。建議讀者切換至各章 Git Tag，觀察開源 Coding Agent 的架構模式，尋找這些原語在真實專案中的對應 。 [scribd](https://www.scribd.com/document/869199074/Links)

關鍵概念：**Harness is the Agent（駕馭層即代理本身）**

## [技術/數據對比]

| 章節 | 原語 | 解決的痛點 | 核心機制 |
|------|------|-----------|---------|
| Ch 1 | 裸模型 | 無法對話 | 單一 API 呼叫 |
| Ch 2 | 歷史訊息 | 模型遺忘 | 訊息列表 append + replay |
| Ch 3 | 指令系統 | 無持久人格 | 系統提示詞 + AGENTS.md |
| Ch 4 | 上下文交付 | 無法讀取檔案 | @-reference 注入 |
| Ch 5 | 工具呼叫 | 只能說不能做 | Function + Schema + 迴圈 + 審批閘道 |
| Ch 6 | 上下文管理 | 窗口溢出 | 頭尾保留壓縮（Compaction） |
| Ch 7 | 技能系統 | 無程序記憶 | 漸進式揭露（Progressive Disclosure） |
| Ch 8 | 沙箱安全 | 程式碼不安全 | Start Closed + Docker/subprocess 沙箱 |
| Ch 9 | 持久化記憶 | 進程終止即遺失 | JSONL 會話 + 關鍵字搜尋 |
| Ch 10 | 任務規劃 | 單迴圈無多步驟 | Orchestrator + JSON 步驟規劃 |
| Ch 11 | 子代理 | 上下文污染 | Context Isolation + 並行 fan-out |
| Ch 12 | 驗證 | 「done」非事實 | 監看測試記錄直到 exit 0 |
| Ch 13 | 可觀測性 | 除錯盲目 | Tracer + Span + OpenTelemetry |
| Ch 14 | 終端 UI | 無可視化介面 | 雙窗格 TUI + 即時追蹤流 |

## [結論與行動建議]

**啟發金句：**

> 「提示詞是意圖，不是圍欄。不要告訴模型別碰機密——根本不給它機密。」

**具體行動建議 — M-H-U 法則：**

- **M**odel — 將模型視為無狀態的推理引擎，放在獨立套件中，更換 Provider 只需替換一個檔案
- **H**arness — 所有讓代理「感覺像代理」的邏輯都存在這一層：歷史、指令、工具、壓縮、技能、沙箱、記憶、規劃、驗證、追蹤
- **U**I — UI 是事件的消費者而非擁有者，透過 Tracer 渲染，不重新實作代理邏輯

**生活實踐建議：**

在日常評估或建構 AI 應用時，不要只關注模型選擇（GPT、Gemma、Claude），而應優先設計 Harness 層的工程品質。具體做法：

- 用 `git checkout ch0` → `ch14` 逐章運行，親手體驗每個原語的增量價值
- 在你的團隊專案中引入 `AGENTS.md` 慣例，讓代理自動讀取專案規則與測試指令
- 對任何 Agent 系統，先確認它是否具備：上下文壓縮、審批閘道、驗證機制、可觀測性追蹤——這四項是生產就緒與玩具的界線
- 查看開源 Coding Agent（如 Codex、Claude Code）的原始碼，尋找影片中對應的架構模式

## [參考連結]

- YouTube 原始影片：https://youtu.be/oUBgqzcV1qw?si=BrsL8BJO4rJhGqSj
- GitHub 倉庫（Git Tags ch0→ch14）：https://github.com/thecarbonlayer/gemma
