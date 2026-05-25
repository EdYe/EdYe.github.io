---
title: 'WebMCP 與 MCP Apps：讓 Web 成為 Agent 的無限畫布'
date: 2026-05-25
image: /images/AI筆記/introducing-webmcp-agents-in-the-browser.jpeg
category: AI筆記
tags: [MCP Apps, WebMCP, Agent介面, MCP Transport, 瀏覽器原生API]
description: '聊天介面（Chat UI）並非 AI Agent 的終態。本演講以打造漫畫閱讀器的實戰案例，揭示了兩項革命性技術：MCP Apps 與 WebMCP，解決了「Agent 只能輸出文字牆」的核心痛點，讓 Web 平台成為真正的無限畫布。'
quote: 'CSS and JavaScript aren''t just the language of the web — they''re the language of interactive experiences on agents.'
action: '評估現有 Web Dashboard，以 T-A-W 三層法則（Tool→App→WebMCP）逐步讓產品 Agent Ready'
source_has_timestamps: true
---
## [核心摘要]

**聊天介面（Chat UI）並非 AI Agent 的終態**。本演講以打造漫畫閱讀器的實戰案例，揭示了兩項革命性技術：**MCP Apps**（將 HTML/CSS/JS 打包成單一檔案嵌入 Agent 介面）與 **WebMCP**（讓現有網頁直接成為 Agent 工具伺服器），解決了「Agent 只能輸出文字牆」的核心痛點，讓 Web 平台成為真正的無限畫布。

***

## [詳細重點整理]

### 1. 講者背景與核心命題 [00:07]

Rachel Lee Nabors，曾任職 Mozilla、W3C、Microsoft Edge PM，React 官方文件作者。她的核心論點是：**Chat 之於 Agent，就像終端機（CLI）之於桌面軟體**——是過渡期，不是終點。現在的「Starfish Design」（純聊天框落地頁）要求使用者自行摸索，體驗如同 1980 年代的文字冒險遊戲。

**關鍵概念：Starfish Design** — 以 Chat Box 為中心、讓使用者承擔所有探索負擔的 UI 反模式。

***

### 2. MCP Transport：STDIO vs HTTP [00:06]

| | **STDIO（Studio）** | **HTTP** |
|---|---|---|
| 運行方式 | 本地 process，由 client 啟動 | Web service，監聽 HTTP endpoint |
| 設定方式 | JSON config + 命令列參數 | 只需輸入 URL |
| 適用場景 | 開發者本地工具 | Serverless、Vercel/Cloudflare Edge |
| 使用者體驗 | 門檻高 | 友善 |

**關鍵概念：MCP Transport** — Agent 與 MCP Server 之間的通訊協定層。

***

### 3. MCP 工具設計：結構化資料回傳 [00:08]

MCP Tools 回傳的是結構化 JSON，工具清單設計應對映網站的原生導航邏輯（list comics、list storylines、search by character 等）。特別之處在於 `get_transcript` 工具回傳 **Markdown**，而非 JSON，可直接注入 context。MCP Resources 理論上是做 context pre-priming 的最佳載體，但目前幾乎無 Client 端實作，是當前生態系的重大缺口。

**關鍵概念：MCP Resources** — 設計來在 Agent 切換任務模式時預先載入相關文件/資源的機制，目前嚴重缺乏實作支援。

***

### 4. MCP Apps：在 Agent 內嵌入互動介面 [00:13]

MCP Tool 的回傳值可以是一個完整的互動式 App，做法是在工具定義中加入 `meta` 屬性指向一個 URL，該 URL 回傳單一 HTML 檔案（內嵌所有 CSS/JS）。Agent 介面將其渲染於 **iframe** 中，結果是 Agent 內出現了一個像素級還原的漫畫閱讀器，支援前後翻頁、逐字稿模式切換，體驗與原網站無異。

**關鍵概念：MCP App** — 將 HTML+CSS+JS 打包成單一檔案，由 Agent 介面在 iframe 中渲染的富媒體互動元件。

***

### 5. MCP Apps 的限制與最佳實踐 [00:16]

- **沙盒隔離**：運行於 iframe 中，無 `localStorage`，無跨 iframe 狀態共享
- **外部資源須宣告**：字型、圖片等需配置 **CSP（Content Security Policy）**，否則一片空白
- **網路請求需代理**：App 本身無直接網路存取，需透過 `callServerTool` 向 MCP Server 請求
- **工具可見性控制**：導航類工具應設 `visibility: app`，避免 LLM 誤用為文字工具
- **建議以設計系統為基礎**：字型、CSS 從同一 Server 共享，透過 CORS policy 管理

**關鍵概念：Content Security Policy (CSP)** — 控制 MCP App iframe 可載入哪些外部資源的安全策略。

***

### 6. WebMCP：讓網頁成為 Agent 的工具伺服器 [00:17]

現有瀏覽器 Agent 靠截圖或 DOM traversal 來操作網頁，既耗 token 又不準確。**WebMCP** 讓網頁直接暴露可呼叫的函式給 Agent，有兩種模式：

- **Declarative（宣告式）**：在現有 `<form>` 上加 `tool-name` 和 `tool-description` 屬性，即可將表單暴露為 Agent 工具，適合表單密集型網站
- **Imperative（命令式）**：使用 `navigator.modelContext.registerTools()` 以程式方式註冊工具並掛載 callback，適合 API 呼叫、資料轉換等複雜工作流

**關鍵概念：WebMCP** — 讓任意 HTML 頁面成為迷你 MCP 工具伺服器的瀏覽器原生 API，WebMCP 之於 MCP，如同 JavaScript 之於 Java（名稱相似，架構獨立）。

***

### 7. WebMCP Demo：瀏覽器原生 API 的無限可能 [00:20]

透過 **MCP-B 擴充套件**（調試工具）示範：Agent 在網頁上呼叫 `next_page` 工具直接觸發頁面導航，完全不需點擊。此外，Web Speech API、Canvas、Audio、WASM、CSS Animation 等**瀏覽器原生 API** 皆可在 MCP App 及 WebMCP 環境中零依賴使用，是被嚴重低估的 Agent UI 構建資源。

**關鍵概念：Zero-dependency Browser APIs** — Web Speech、Canvas 等無需引入第三方 library 即可在 Agent 環境中使用的瀏覽器內建能力。

***

## [結論與行動建議]

**啟發金句：**
> **「CSS and JavaScript aren't just the language of the web — they're the language of interactive experiences on agents.」**
> CSS 和 JavaScript 不只是 Web 的語言，它們是 Agent 互動體驗的語言。

**具體行動建議：三層 Agent UI 升級法則 — T-A-W**
- **T（Tool）**：將現有 API 包裝為 MCP Tool，回傳結構化 JSON
- **A（App）**：為核心工具加上 MCP App，嵌入完整互動介面
- **W（WebMCP）**：在現有網站加入 WebMCP 屬性，讓瀏覽器 Agent 直接呼叫頁面函式

**生活實踐建議：**
1. **產品開發者**：評估現有的 Web Dashboard，哪些表單可以直接加上 `tool-name`/`tool-description` 屬性，讓 AI 助理直接操作，無需重寫後端
2. **AI 應用架構師**：在設計 MCP Server 時同步規劃 MCP App 的設計系統，讓 Agent 的視覺回饋與品牌一致
3. **內容創作者**：參考 WebMCP 的 Declarative 模式，以最低成本讓既有網站「Agent Ready」

***

## [參考連結]

- 🎬 原始影片：[https://youtu.be/LMbeDEQO6QM](https://youtu.be/LMbeDEQO6QM) [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)
- 👤 講者 X (Twitter)：https://x.com/nearestnabors
- 👤 講者 GitHub：https://github.com/rachelnabors
- 📰 講者 Newsletter「The Agentic Web」：可循 LinkedIn 聯繫追蹤
