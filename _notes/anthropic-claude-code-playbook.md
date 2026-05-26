---
title: 'Anthropic 發布 Claude Code 大型程式碼庫部署手冊'
date: 2026-05-17
image: /images/AI筆記/anthropic-claude-code-playbook.jpeg
category: AI筆記
tags: [Claude Code, Harness架構, CLAUDE.md, MCP, 大型程式碼庫]
description: 'Anthropic 發布 Claude Code 大型程式碼庫部署手冊，核心論點是模型外的生態系（Harness）比模型本身更決定實際表現。手冊提出 7 個組件與 3 大模式，建立順序：CLAUDE.md 優先，MCP 最後。'
quote: 'Harness 比 Model 更決定結果——生態系的天花板，才是 AI 能力的天花板。'
action: '立刻從根目錄建立一頁 CLAUDE.md 全局規範，並指定 DRI 負責維護，每季審查配置是否需更新。'
source_has_timestamps: true
---
## [核心摘要]

Anthropic 發布了 **Claude Code 大型程式碼庫部署手冊（Playbook）**，核心論點是：**模型外的生態系（Harness）比模型本身更決定 Claude Code 的實際表現**。手冊提出 7 個組件（5 個擴展點 + 2 個能力）與 3 大模式，並明確建立順序：**CLAUDE.md 優先，MCP 最後**，解決了大型企業在千萬行程式碼庫中部署 AI 編程工具的落地痛點。

***

## [詳細重點整理]

### 1. Harness 優先論 [0:00]

**核心概念：Harness-over-Model 論點**

模型周圍的生態系——即 Harness——才是決定 Claude Code 規模化效能的關鍵，而非模型本身。Anthropic 的 Applied AI 團隊（Griffith、Lee、Concannon 等人）明確指出此論點，適用範圍涵蓋數百萬行的 Monorepo、數十年的 Legacy 系統，以及 C、C++、C#、Java、PHP 等語言。

***

### 2. Agentic Search vs. RAG [1:29]

**核心概念：Agentic Search（主動搜尋）**

傳統 AI 編程工具依賴 RAG 嵌入索引，在活躍的大型程式碼庫中會出現「索引過時」問題——指向已更名的函式或已刪除的模組。Claude Code 改採 **Agentic Search**：無嵌入管線、無中央索引，每個實例直接從當前程式碼庫讀取，如同工程師手動翻閱一樣。

***

### 3. 7 組件 Harness 架構 [2:14]

**核心概念：分層式 Harness 架構**

7 個組件依建立順序如下：

| 層級 | 組件 | 功能說明 |
|------|------|----------|
| 1 | **CLAUDE.md** | 每次 session 自動載入的情境檔案 |
| 2 | **Hooks** | 可在 session 結束後自動提案 CLAUDE.md 更新 |
| 3 | **Skills** | 按需載入的專業知識（如安全審查技能） |
| 4 | **Plugins** | 將 Skills、Hooks、MCP 打包成可安裝模組分發 |
| 5 | **LSP 整合** | 以符號（Symbol）精確搜尋，取代字串 Grep |
| 6 | **MCP Servers** | 最後建立，開放結構化搜尋工具給 Claude 呼叫 |
| 7 | **Subagents** | 獨立執行任務後只回傳最終結果給主 Agent |



***

### 4. Pattern 1 — 讓程式碼庫可導航 [4:32]

**核心概念：Navigability（可導航性）**

Anthropic 提出 6 個子模式讓大型程式碼庫對 Claude 更友善：
- **精簡分層的 CLAUDE.md**：根目錄放全局規範，子目錄放局部慣例
- **在子目錄初始化**，而非只在 Repo 根目錄
- **限定測試/lint 指令範圍**在子目錄，避免跑全局浪費 context
- 使用 `.gitignore` + `permissions.deny`（存於 `.claude/settings.json`）統一噪音過濾
- 建立**程式碼庫地圖**（Markdown 索引檔，列出頂層目錄一行說明）
- 啟用 **LSP**，讓 Claude 以符號搜尋取代字串 Grep

***

### 5. Pattern 2 — 持續維護 CLAUDE.md [5:51]

**核心概念：配置衰退（Configuration Decay）**

為舊模型版本撰寫的指令可能對新模型產生反效果。Anthropic 建議每 **3 到 6 個月**進行一次配置審查，尤其在重大模型版本發布後效能出現停滯時。具體案例：一個攔截 Perforce 的 P4 edit Hook，在 Claude Code 原生支援 Perforce 後即變成多餘且有害的配置。

***

### 6. Pattern 3 — 建立所有權機制 [6:25]

**核心概念：Agent Manager（代理管理人）**

技術配置之外，**組織所有權**才是推動大規模採用的關鍵。Anthropic 提出三個層級：
- **DRI（Directly Responsible Individual）**：最低可行所有者，負責設定、權限與 CLAUDE.md 慣例
- **Agent Manager**：新興職位，兼具 PM 與工程師能力，專責管理 Claude Code 生態系
- **跨職能工作小組**：工程、資安、治理代表共同定義需求並制定推廣路線圖

***

## [結論與行動建議]

**🔥 啟發金句：**
> **「Harness 比 Model 更決定結果——生態系的天花板，才是 AI 能力的天花板。」**

**具體行動建議：CLAUDE-First 法則**
> **C**LAUDE.md → **H**ooks → **S**kills → **P**lugins → **L**SP → **M**CP（依此順序，禁止跳層）

**生活實踐建議：**
- 🛠️ **今日行動**：若你的專案尚未建立 CLAUDE.md，立刻從根目錄的一頁全局規範開始，記錄專案架構、命名慣例與禁止行為
- 👥 **組織行動**：在 AI 工具推廣前，先指定一位 DRI，避免「人人都在用，但沒人維護」的配置荒廢
- 🔄 **季度行動**：每季進行一次 CLAUDE.md 審查，尤其在新模型版本發布後的一個月內

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/IYBP_JT9aUo?si=QFPGKyrajo33ubWP 
- 📝 Anthropic 原文：https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
- 📚 Claude Code 文件：https://code.claude.com/docs/en/overview

***

# Claude Code 如何在大型程式碼庫中運作：最佳實踐與入門指南

> *最成功的 Claude Code 部署案例，在配置、工具及組織架構上都展現出一套可辨識的共通模式。本文是 **Claude Code at scale（Claude Code 規模化）** 系列文章的一部分，該系列涵蓋工程組織在企業級規模下使用 Claude Code 的最佳實踐。*

- **分類**：企業 AI（Enterprise AI）
- **產品**：Claude Code
- **日期**：2026 年 5 月 14 日
- **閱讀時間**：5 分鐘

---

Claude Code 已在以下各種生產環境中運行：數百萬行程式碼的單一儲存庫（monorepo）、數十年歷史的老舊系統、跨越數十個儲存庫的分散式架構，以及擁有數千名開發者的組織。這些環境帶來的挑戰是較小、較簡單的程式碼庫所沒有的：例如每個子目錄都有不同的建置指令，或是分散在沒有共用根目錄的多個資料夾中的老舊程式碼。

本文涵蓋我們觀察到的、能促成 Claude Code 大規模成功採用的模式。我們所謂的「大型程式碼庫」涵蓋廣泛的部署情境：數百萬行程式碼的 monorepo、數十年累積的老舊系統、分散於不同儲存庫的數十個微服務，或上述情況的任意組合。這也包括許多團隊通常不會聯想到 AI 編碼工具的語言所運行的程式碼庫，例如 C、C++、C#、Java、PHP。（在這些情境中，Claude Code 的表現往往比多數團隊預期得更好，尤其是近期模型發布之後。）雖然每個大型程式碼庫的部署都會受到其特定版本控制、團隊結構以及累積慣例的影響，但本文所介紹的模式具有通用性，是考慮採用 Claude Code 的團隊很好的起點。

## Claude Code 如何在大型程式碼庫中導航

Claude Code 導航程式碼庫的方式與軟體工程師相同：它走訪檔案系統、讀取檔案、使用 grep 來精確找到所需內容，並追蹤程式碼庫中的引用關係。它在開發者的本機運行，不需要建立、維護或上傳程式碼庫索引到伺服器。

過去的 AI 編碼工具依賴基於 RAG 的檢索方式，即將整個程式碼庫嵌入（embedding），並在查詢時取出相關片段。在大規模情境下，這類系統可能會失效，因為嵌入流程無法跟上活躍工程團隊的開發速度。等到開發者查詢索引時，索引反映的可能是幾天、幾週甚至幾小時前的程式碼狀態。檢索結果可能回傳兩週前已被團隊重新命名的函式，或是上個衝刺週期已刪除的模組，且毫無提示資料已過時。

代理式搜尋（Agentic search）則能避免這些失效模式。它不需要維護嵌入流程或集中式索引，即使有數千名工程師持續提交新程式碼也不受影響。每個開發者的執行個體都是從即時的程式碼庫運作。

但這種方式有一個取捨：它在 Claude 擁有足夠的起始上下文、知道該往哪裡看時表現最佳。這意味著 Claude 的導航品質取決於程式碼庫的設置是否完善，包括透過 CLAUDE.md 檔案與 skills 來層層堆疊上下文。如果你要求它在十億行的程式碼庫中找出某個模糊模式的所有實例，那麼在工作開始之前，你就會先撞上上下文視窗的上限。在程式碼庫設置上投入的團隊，會看到更好的成果。

## 工作框架（harness）與模型同樣重要

關於 Claude Code 最常見的誤解之一，就是認為它的能力完全取決於所使用的模型。團隊往往專注於模型的基準測試（benchmark）以及它在測試任務上的表現。但實際上，圍繞模型建構的生態系——即「工作框架（harness）」——對 Claude Code 表現的影響，比模型本身還要大。

工作框架由五個擴展點構成——CLAUDE.md 檔案、hooks、skills、plugins 以及 MCP 伺服器——每一個都有不同的功能。團隊建構它們的順序很重要，因為每一層都建立在前一層之上。另外兩項能力——LSP 整合與 subagents——則完整了整個設置。以下說明這些元件與能力各自的作用：

[**CLAUDE.md**](https://code.claude.com/docs/en/memory) **檔案是第一步**。這些是 Claude 在每次 session 開始時會自動讀取的上下文檔案：根目錄檔案提供全局視角，子目錄檔案提供區域慣例。它們提供 Claude 完成任務所需的程式碼庫知識。由於它們會在每個 session 中載入（無論任務為何），因此應聚焦於廣泛適用的內容，才不會拖累效能。

[**Hooks**](https://code.claude.com/docs/en/hooks-guide) **讓設置具備自我改進的能力**。多數團隊將 hooks 視為防止 Claude 做錯事的腳本，但更有價值的用途是持續改進。一個 stop hook 可以在 session 結束時回顧過程，並在上下文還新鮮時提出對 CLAUDE.md 的更新建議。一個 start hook 可以動態載入團隊專屬的上下文，讓每位開發者在無需手動配置的情況下，都能取得適合自己模組的設置。對於 linting 與格式化等自動化檢查，hooks 能以確定性的方式執行規則，比依賴 Claude 記住指令更能產出一致的結果。

[**Skills**](https://code.claude.com/docs/en/skills) **讓正確的專業知識隨選即用，又不會讓每個 session 都變得臃腫**。在擁有數十種任務類型的大型程式碼庫中，並非所有專業知識都需要存在於每個 session。Skills 透過[漸進式揭露（progressive disclosure）](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)解決這個問題，將那些原本會搶佔上下文空間的專業工作流程與領域知識卸載出來，只在任務需要時才載入。例如，安全性審查的 skill 會在 Claude 評估程式碼漏洞時載入，而文件處理的 skill 則會在程式碼變更需要更新文件時載入。

Skills 也可以限定在特定路徑下，這樣它們只會在程式碼庫的相關部分啟用。例如，擁有支付服務的團隊可以將其部署 skill 綁定到該目錄，這樣當有人在 monorepo 其他地方工作時，它就不會自動載入。

[**Plugins**](https://code.claude.com/docs/en/plugins) **負責分發有效的做法**。大型程式碼庫的一個挑戰是：*好的* 設置可能僅限於小圈子內流傳。Plugin 能將 skills、hooks 與 MCP 配置打包成一個可安裝的單一套件，這樣當新工程師在報到第一天安裝該 plugin 時，他們就能立即擁有與既有使用者相同的上下文與能力。Plugin 的更新可以透過[受管理的市集（managed marketplaces）](https://support.claude.com/en/articles/13837433-manage-claude-cowork-plugins-for-your-organization)在整個組織中分發。

舉例來說，我們合作的一家大型零售組織建立了一個 skill，將 Claude 連結到他們的內部分析平台，讓業務分析師能夠在不離開工作流程的情況下取得績效資料。他們在全面推廣到業務部門之前，先以 plugin 的形式發布該 skill。

**語言伺服器協定（LSP）整合，讓 Claude 擁有與開發者在 IDE 中相同的導航能力。** 大多數大型程式碼庫的 IDE 都已運行 LSP，支援「跳至定義（go to definition）」與「找出所有引用（find all references）」等功能。將此能力提供給 Claude，能讓它擁有符號（symbol）層級的精確度：可以追蹤函式呼叫至其定義、跨檔案追蹤引用，並區分不同語言中同名的函式。沒有 LSP 時，Claude 只能依文字進行模式比對，可能會找到錯誤的符號。我們合作過的一家企業軟體公司，在 Claude Code 推行前就在全組織範圍內部署了 LSP 整合，正是為了讓大規模的 C 與 C++ 導航能夠可靠運作。對於多語言的程式碼庫而言，這是價值最高的投資之一。

**MCP 伺服器擴展一切。** MCP 伺服器是 Claude 連接到內部工具、資料來源與 API 的方式，這些都是它原本無法觸及的。最先進的團隊建立了 MCP 伺服器，將結構化搜尋暴露為 Claude 可直接呼叫的工具。其他則將 Claude 連接到內部文件、票務系統或分析平台。

[**Subagents**](https://code.claude.com/docs/en/sub-agents) **將探索與編輯分離。** Subagent 是一個獨立的 Claude 執行個體，擁有自己的上下文視窗，它接受一個任務、完成工作，並只將最終結果回傳給父代理。一旦工作框架就緒，有些團隊會啟動一個唯讀的 subagent 來繪製子系統的地圖，並將結果寫入檔案，然後讓主代理在掌握完整全貌後進行編輯。

<img src="https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a04aaf1c37c6196e5ee19bb_fig1-the-claude-code-harness-v1%402x.png" width=800/>

**Claude Code 擴展層概覽。**

下表彙整了每個元件的功能、載入時機，以及我們最常見到的混淆之處：

| 元件 | 它是什麼 | 何時載入 | 最適合用於 | 常見混淆 |
| --- | --- | --- | --- | --- |
| CLAUDE.md | Claude 自動讀取的上下文檔案 | 每個 session | 專案特定慣例、程式碼庫知識 | 用它來放置應屬於 skill 的可重用專業知識 |
| Hooks | 在關鍵時刻執行的腳本 | 由事件觸發 | 自動化一致行為、捕捉 session 學習成果 | 用提示（prompt）做應該自動執行的事 |
| Skills | 針對特定任務類型打包的指令 | 隨選載入（相關時） | 跨 session 與專案可重用的專業知識 | 把所有東西塞進 CLAUDE.md |
| Plugins | 打包的 skills、hooks、MCP 配置 | 設定後始終可用 | 在整個組織中分發有效的設置 | 任由好的設置僅限小圈子流傳 |
| 語言伺服器協定（LSP）* | 透過語言專屬伺服器提供即時程式碼智能 | 設定後始終可用 | 在型別語言中進行符號級導航與自動錯誤偵測 | 假設它是自動運作 |
| MCP 伺服器 | 連接外部工具與資料 | 設定後始終可用 | 讓 Claude 存取其原本無法觸及的內部工具 | 在基礎尚未穩固前就建立 MCP 連接 |
| Subagents* | 用於特定任務的獨立 Claude 執行個體 | 被呼叫時 | 將探索與編輯分離、平行處理 | 在同一個 session 中同時進行探索與編輯 |
| *LSP 透過 plugin 層存取。Subagents 是一種委派能力，而非一個可配置的擴展點。 |

## 來自成功部署的三種配置模式

如何為大型程式碼庫配置 Claude Code，很大程度上取決於該程式碼庫的結構。儘管如此，我們在觀察的部署案例中始終看到三種模式。

### 讓程式碼庫在大規模下仍易於導航

Claude 在大型程式碼庫中提供協助的能力，受限於它能否找到正確的上下文。每個 session 載入太多上下文會降低效能，而載入太少則讓 Claude 盲目摸索。最有效的部署案例會在前期投入心力，讓程式碼庫對 Claude 來說易於理解。我們持續觀察到以下幾種模式：

- **保持 CLAUDE.md 檔案精簡且分層。** Claude 會在程式碼庫中移動時以累加方式載入這些檔案：根目錄檔案提供全局視角，子目錄檔案提供區域慣例。根目錄檔案應只包含指引性內容與關鍵注意事項；其他內容都會變成雜訊。
- **在子目錄而非儲存庫根目錄初始化。** Claude 在工作範圍被限定在任務真正相關的程式碼庫部分時效果最好。在 monorepo 中，這可能違反直覺，因為工具通常假設從根目錄存取，但 Claude 會自動沿目錄樹向上走訪，並沿途載入它找到的每個 CLAUDE.md 檔案，因此根層級的上下文永遠不會遺失。
- **依子目錄限定測試與 lint 指令範圍。** 當 Claude 只變更一個服務時卻執行完整測試套件，會造成逾時並把上下文浪費在無關的輸出上。子目錄層級的 CLAUDE.md 檔案應指定適用於該部分程式碼庫的指令。這種做法在服務導向的程式碼庫中效果很好，因為每個目錄都有自己的測試與建置指令。在具有深層跨目錄相依關係的編譯語言 monorepo 中，依子目錄限定範圍較難實現，可能需要專案特定的建置配置。
- **使用 `.ignore` 檔案排除生成檔案、建置產物與第三方程式碼。** 在 `.claude/settings.json` 中提交 `permissions.deny` 規則，意味著這些排除設定會被版本控制，因此團隊中的每個開發者都能獲得相同的雜訊抑制效果，而不需要自行配置。在某些程式碼庫中，生成檔案本身就是開發工作的對象。從事程式碼生成器開發的開發者可以在自己的本機設定中覆蓋專案層級的排除規則，而不影響團隊其他成員。
- **當目錄結構無法承擔此任務時，建構程式碼庫地圖。** 對於程式碼未以慣常目錄結構整合的組織，可在儲存庫根目錄放置一個輕量級的 markdown 檔案，列出每個頂層資料夾並附上一行描述，這就為 Claude 提供了一個可在開啟檔案前快速瀏覽的「目錄」。對於擁有數百個頂層資料夾的程式碼庫，最佳做法是分層方式：根目錄檔案只描述最高層級結構，而子目錄的 CLAUDE.md 檔案提供下一層的細節，並在 Claude 走訪目錄樹時隨選載入。對於較簡單的情境，使用 `@-mention` 方式指明 Claude 應參考的特定檔案或目錄也能達到同樣效果。
- **執行 LSP 伺服器，讓 Claude 以符號而非字串進行搜尋。** 在大型程式碼庫中對常見函式名稱執行 grep 會回傳數千個匹配項，而 Claude 會耗費上下文開啟檔案以判斷哪個才是關鍵。LSP 只會回傳指向同一符號的引用，因此過濾工作在 Claude 讀取任何內容之前就已完成。設定這個功能需要為你的語言安裝[程式碼智能 plugin](https://code.claude.com/docs/en/discover-plugins#code-intelligence)以及對應的語言伺服器二進位檔；Claude Code 文件涵蓋了可用的 plugin 與疑難排解。

**一個注意事項**：即使是分層的 CLAUDE.md 做法也有失效的邊緣情境，例如擁有數十萬個資料夾與數百萬個檔案的程式碼庫，或運行在非 git 版本控制上的老舊系統。我們將在本系列的後續文章中探討這些挑戰。

### 隨著模型智能演進，主動維護 CLAUDE.md 檔案

隨著模型演進，為當前模型撰寫的指令可能會對未來模型造成反效果。曾經引導 Claude 處理它原本不擅長的模式的 CLAUDE.md 檔案，在下一個模型推出時，可能變得多餘甚至有所限制。例如，一條告訴 Claude 將每次重構拆分為單一檔案變更的 CLAUDE.md 規則，對較早的模型可能有助於保持正軌，但會阻礙更新的模型進行它能勝任的協調式跨檔案編輯。

為彌補特定模型限制而建立的 skills 與 hooks——無論是模型推理本身的限制，或是 Claude Code 工具本身的限制——一旦這些限制消失，就會變成額外負擔。例如，一個攔截檔案寫入、以強制執行 Perforce 程式碼庫 `p4 edit` 的 hook，在 Claude Code 加入原生 Perforce 模式後就變得多餘。

團隊應預期每三到六個月進行一次有意義的配置審查，但在每次重大模型發布後，若感覺效能似乎到達瓶頸，也值得進行一次審查。

### 為 Claude Code 的管理與採用指派負責人

僅靠技術配置並不能推動採用。做得正確的組織也會在組織層面投入心力。

擴散最快的推行案例，會在廣泛開放存取之前投入專門的基礎設施建設。一個小團隊（有時甚至只是一個人）會把工具串接好，讓 Claude 在開發者第一次接觸時就能融入他們的工作流程。在某家公司，幾位工程師打造了一系列在第一天就可使用的 plugins 與 MCPs。在另一家公司，一整個專責管理 AI 編碼工具的團隊在推行開始前就把基礎設施準備就緒。這兩個案例中，開發者的初次體驗都是高效而非令人挫折的，採用因此得以擴散。

<img src="https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a04e25f1984beb50dc5525b_fig2-phases-of-claude-code-rollout-v1%402x.png" width=800/>

如今負責這項工作的團隊通常隸屬於「開發者體驗（developer experience）」或「開發者生產力（developer productivity）」部門，這通常是負責新工程師入職培訓與開發者工具建置的職能單位。在多個組織中，正在出現一個新興角色：代理管理員（agent manager），這是一個結合產品經理（PM）與工程師的混合職能，專門負責管理 Claude Code 生態系。對於沒有專屬團隊的組織，最小可行版本是設置一位 DRI（直接負責人）：由一個人擁有對 Claude Code 配置的所有權，並擁有對設定、權限政策、plugin 市集與 CLAUDE.md 慣例做決策的權限，以及維持其與時俱進的責任。

由下而上的採用方式能激發熱情，但若沒有人來統整有效做法，就容易碎片化。你需要有一個人或一個團隊來組裝並推廣正確的 Claude Code 慣例（例如標準化的 CLAUDE.md 階層或精選的 skills 與 plugins 集合）。沒有這項工作，知識會停留在小圈子內，採用也會陷入停滯。

在大型組織中，特別是受監管產業，治理問題會很早出現，例如：誰來控制哪些 skills 與 plugins 可用？如何避免數千名工程師各自獨立重新打造同樣的東西？如何確保 AI 生成的程式碼經過與人類撰寫程式碼相同的審查流程？為了及早處理這些問題，我們建議從一組已核准的 skills、必要的程式碼審查流程，以及有限的初期存取權開始，並隨著信心增加逐步擴展。

我們觀察到，最順利的部署案例出現在早期就建立跨職能工作小組的組織，這類小組會把工程、資訊安全與治理代表聚集起來，共同定義需求並建立推行路線圖。

## 將這些模式應用到你的組織

Claude Code 是圍繞傳統軟體工程環境設計的，其中工程師是程式碼庫的主要貢獻者，儲存庫使用 Git，且程式碼遵循標準目錄結構。大多數大型程式碼庫都符合這個模式，但非傳統設置——例如含有大量二進位資產的遊戲引擎、使用非常規版本控制的環境，或非工程師也參與貢獻的程式碼庫——需要額外的配置工作。我們的指引假設的是慣例設置，本文所描述的模式已在我們眾多客戶中發揮作用。剩餘的複雜性則需要依你的程式碼庫、工具與組織具體狀況進行判斷。這也是 Anthropic 應用 AI 團隊（Applied AI team）直接與工程團隊合作的價值所在：將這些模式轉譯為你組織的具體需求。

<img src="https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a04e2860abbe67418ca0f8b_fig3-getting-started-checklist-v2%402x.png" width=800/>

*開始使用 [Claude Code for Enterprise（企業版 Claude Code）](https://claude.com/product/claude-code/enterprise)。*

---

***誌謝：*** *特別感謝 Anthropic 應用 AI 團隊的 Alon Krifcher、Charmaine Lee、Chris Concannon、Harsh Patel、Henrique Savelli、Jason Schwartz、Jonah Dueck 與 Kirby Kohlmorgen，分享他們在大規模部署 Claude Code 的經驗；以及 Zoox 的 Amit Navindgi 對本文提供回饋。*