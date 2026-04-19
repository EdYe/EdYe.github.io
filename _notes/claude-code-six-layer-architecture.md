---
title: 'Claude Code AI 代理架構深度解析'
date: 2026-04-20
image: /images/AI筆記/claude-code-six-layer-architecture.jpeg
category: AI筆記
tags: [核心迴圈, 系統提示詞, 子代理, 上下文視窗, 代理架構]
description: '這段影片詳細解析了 Claude Code 背後的 AI 代理 (AI Agents) 核心架構。影片透過結構化的簡報來解說，以下為您萃取並整理影片中呈現的主要'
source_has_timestamps: true
---

這段影片詳細解析了 Claude Code 背後的 AI 代理 (AI Agents) 核心架構。影片透過結構化的簡報來解說，以下為您萃取並整理影片中呈現的主要投影簡報內容與核心概念：

### Act I: The Loop (核心迴圈) [[00:36](http://www.youtube.com/watch?v=ofLvTNZEHVk&t=36)]
* **Chatbot vs. Agent**：Chatbot 只是單純的「輸入訊息 -> 輸出回應」，而 Agent 會在一個核心的 While 迴圈中不斷運作：**模型 (Model) -> 執行工具 (Execute) -> 回饋結果 (Result)**。
* **迴圈三階段**：
  1. **Gather Context (收集上下文)**：讀取檔案、搜尋程式碼、理解問題的實際狀況。
  2. **Take Action (採取行動)**：編輯程式碼、實際做出修改。
  3. **Verify (驗證)**：執行測試程式、檢查輸出。若驗證失敗，則自動跳回第一階段。
* **終止信號 (Termination Signal)**：當模型回傳的結果包含「0 個工具呼叫 (Zero tool calls)」時，代表任務完成，迴圈才會停止。

### 每次行動的 10 步驟管線 (The 10-Step Pipeline) [[02:26](http://www.youtube.com/watch?v=ofLvTNZEHVk&t=146)]
每次代理進行一輪迴圈，其實包含了 10 個精細的步驟。其中只有 1 個步驟是真正的「執行」，其餘都是為了安全與控制：
* **Assembly (組裝)**：1. 組裝上下文 -> 2. 呼叫 API -> 3. 處理 Token 串流 -> 4. 萃取工具呼叫。
* **Safety (安全)**：5. 權限檢查 -> 6. 觸發使用工具前的 Hooks。
* **Execution (執行)**：7. **工具正式執行**。
* **Capture & Control (捕捉與控制)**：8. 捕捉結果 -> 9. 觸發使用工具後的 Hooks -> 10. 決定是否繼續迴圈。

### Act II: The Mind (代理的心智) [[03:03](http://www.youtube.com/watch?v=ofLvTNZEHVk&t=183)]
* **Extended Thinking (擴展思考)**：預設啟用，底層使用 ReAct 框架（Thought -> Action -> Observation 的不斷循環）。
* **Thinking Budget (思考預算)**：預設上限為 32,000 Tokens。思考越深，在軟體工程基準測試（如 SWE-bench）的表現越好，但也意味著消耗更多 Tokens 與成本。

### 隱藏的系統提示詞 (The System Prompt) [[03:52](http://www.youtube.com/watch?v=ofLvTNZEHVk&t=232)]
系統提示詞不是短短一段話，而是高達數千 Tokens，由 **8 個不同的層級 (8 Layers of DNA)** 組裝而成：
1. **Core Identity**：核心身份設定（約 270 tokens）。
2. **Behavioral Rules**：行為準則（例如：絕對不要 force push）。
3. **Tool Definitions**：工具的 JSON Schema 定義。
4. **Claude.md**：注入團隊或專案的專屬規範。
5. **Auto-memory**：自動記憶機制。
6. **Skills**：各種技能描述。
7. **MCP Tools**：Model Context Protocol 工具。
8. **Runtime Context**：動態執行時的上下文。

### The Guardrails (安全護欄與權限閘門) [[06:39](http://www.youtube.com/watch?v=ofLvTNZEHVk&t=399)]
* **Deny-First Architecture (拒絕優先架構)**：每一個工具呼叫都必須通過 6 道閘門，包含：自訂 Hooks、拒絕規則、允許規則、詢問規則、權限模式與程式化回呼 (Callback)。
* **作業系統沙盒 (OS Sandboxing)**：在最底層，Mac OS 使用 Seatbelt，Linux 使用 Bubblewrap，對檔案系統和網路進行隔離，此舉在不犧牲安全性的情況下，減少了 84% 的擾人權限提示。

### The Context Window (上下文視窗與 Token 經濟學) [[09:23](http://www.youtube.com/watch?v=ofLvTNZEHVk&t=563)]
* **二次方成本稅 (The Quadratic Tax)**：代理的整個工作記憶上限為 200,000 Tokens。由於 API 是無狀態的，每一次迴圈都會重新發送完整的對話紀錄（系統提示 + 歷史紀錄 + 工具結果），導致成本隨對話輪數呈二次方 (O(N²)) 增長。
* **緩解策略**：系統依賴 Prompt Caching (可節省 90% 提示詞成本)，並在 Context 滿載時進行自動壓縮 (Auto-compaction)，或將繁重工作委派出去。

### 解決方案：Subagents (子代理委派) [[11:40](http://www.youtube.com/watch?v=ofLvTNZEHVk&t=700)]
當主代理的 Context 快滿時，它可以平行生成多個「子代理 (Subagents)」：
* 每個子代理擁有自己乾淨的 Context Window，可以專注於特定工作（例如：一個專門搜尋基礎設施，另一個專門讀取 API）。
* 為了安全並行，子代理會在獨立的 Git Worktree 中運行以避免衝突。
* 主代理最終只會接收到摘要結果，保持主對話視窗的整潔。

### Act IV: The Architecture (整體架構) [[13:54](http://www.youtube.com/watch?v=ofLvTNZEHVk&t=834)]
整套系統並非採用複雜的群集 (Swarm) 或編排框架，而是由 **6 個層次 (6 Layers)** 堆疊起來的單一架構：
1. **Messages API** (處理底層呼叫、Streaming 與思考)
2. **Context Management** (管理記憶、歷史與自動壓縮)
3. **Tool System** (內建工具、MCP 與子代理)
4. **Agentic Loop** (收集 -> 行動 -> 驗證的迴圈)
5. **Permission Layer** (允許/拒絕的權限控制)
6. **User Interface** (使用者操作介面)

這個架構最核心的設計理念是**單一迴圈 (One While Loop)** 的極致簡潔：當控制流程就是「模型思考」本身時，未來模型每一次的升級，都會自動且免費地讓這個 AI 代理變得更加聰明。
