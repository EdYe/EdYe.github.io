---
title: 'Agentic Search：Context Engineering 的核心解法'
date: 2026-05-09
image: /images/影片筆記/agentic-search-context-engineering.jpeg
category: 影片筆記
tags: [Context Engineering, Agentic Search, RAG, 工具設計, 語意搜尋]
description: 'Context Engineering 的核心挑戰不是模型本身，而是「如何把正確的資訊放入 LLM 的 Context Window」。Leonie 提出大膽論點：Context Engineering 有 80% 都是 Agentic Search 問題。'
quote: '好的搜尋極其困難，這正是為什麼我們需要多種搜尋技術——沒有銀彈，只有適合當下的組合。'
action: '為已知高頻查詢打造專用低門檻工具，記錄 Agent 每次工具呼叫行為，並以三段式結構撰寫 Tool Description。'
source_has_timestamps: true
---
# Agentic Search for Context Engineering
**講者：** Leonie Monigatti（Elastic）｜**來源：** AI Engineer Conference, 2026/05/08

***
## [核心摘要]
**Context Engineering（情境工程）** 的核心挑戰不是模型本身，而是「如何把正確的資訊放入 LLM 的 Context Window」。Leonie 提出大膽論點：**Context Engineering 有 80% 都是 Agentic Search 問題**。影片系統性地拆解了不同搜尋工具（語意搜尋、通用查詢工具、Shell Tool、Agent Skill）的適用場景與失效邊界，並提供在實際生產環境中組合這些工具的實戰架構。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***
## [詳細重點整理]
### 1. Context Engineering 的本質定義 [00:15]
**Context Engineering** 是指從所有可能的 Context Sources（本地檔案、資料庫、網路、長期記憶）中，決定「哪些內容」要進入 LLM Context Window 的技術藝術。大多數人只關注「箭頭終點」（放什麼資料），卻忽略了「箭頭本身」（搜尋工具如何決策）。

**關鍵概念：** Context Source Native Search Tools（各情境源的原生搜尋介面）

***
### 2. 從傳統 RAG 演進到 Agentic Search [02:23]
傳統 RAG 採用固定 Pipeline：使用者輸入 → 向量搜尋 → 餵入 LLM，存在兩大致命缺陷：
- 不管是否需要外部資訊都會觸發搜尋（浪費 Token，甚至干擾 LLM）
- 無法執行**多跳式搜尋（Multi-hop Retrieval）**，複雜問題無法迭代查詢

**Agentic Search** 以 Search Tool 取代固定 Pipeline，讓 Agent 自行決定「是否搜尋、如何改寫 Query、是否再次搜尋」。

**關鍵概念：** Multi-hop Retrieval（多跳式檢索）

***
### 3. Agentic Search 三大常見失效模式 [09:36]
Agent 不呼叫任何工具（誤以為自身知識足夠）、呼叫錯誤工具（例如應查 DB 卻跑去 Web Search）、生成錯誤的查詢參數（Query Parameter 格式有誤）。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

**解法優先順序：**
1. 撰寫高品質的 **Tool Description**（加入觸發條件、禁用條件、工具間關係）
2. 在 System Prompt 中強化對特定工具的呼叫指示
3. 降低 Tool Parameter 的複雜度

**關鍵概念：** Tool Description Engineering（工具描述工程）

***
### 4. 語意搜尋工具的邊界與失效 [17:52]
用 LangChain + Elasticsearch 實作語意搜尋工具（Top-K=3），對模糊主題查詢效果良好，但對**精確關鍵詞**（如 GDPA 縮寫）或**需要過濾條件**的查詢會完全失效，返回毫不相干的結果。

**關鍵概念：** Semantic Search Brittleness（語意搜尋的脆弱性）

***
### 5. 通用查詢工具（Execute Query Tool）與 Agent Skill [27:55]
改以讓 Agent 直接生成 ESQL 查詢語句（類似 SQL），使工具具備**高天花板（High Ceiling）**能力，可支援篩選、聚合運算。關鍵配套機制：

| 機制 | 作用 |
|------|------|
| **Error Handling（回傳錯誤給 Agent）** | 讓 Agent 自我修正 SQL 語法錯誤 |
| **Agent Skill（漸進式知識揭露）** | 在需要時將查詢語法文件載入 Context Window |
| **System Prompt 強化** | 要求先載入 Skill 再呼叫查詢工具 |

**關鍵概念：** Progressive Disclosure（漸進式知識揭露）

***
### 6. Shell Tool：全能但高風險 [34:42]
Shell Tool（Bash/Exec）讓 Agent 直接在終端機執行命令（ls、grep），可存取本地檔案系統、資料庫 CLI、curl 網路請求，極度靈活。**⚠️ 安全警告：** 未加防護措施的 Shell Tool 可能導致 Agent 刪除檔案，必須在沙箱環境中使用。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

Agent 面對語意搜尋時，會自動串接 grep + 同義詞（regulate、compliance、GDPR、governance）模擬語意理解，出乎意料地有效——但效率低落且不可靠。

**關鍵概念：** Synonym Chaining（同義詞串接模擬語意搜尋）

***
### 7. 語意化 grep 替代方案（Jina Grep） [41:51]
將 Jina CLI（`jina-grep`）告知 Agent 後，Agent 可直接呼叫語意版 grep，首次查詢即精準命中，無需多次迭代。同時建議：
- 精確關鍵詞 → 用傳統 `grep`
- 語意模糊查詢 → 用 `jina-grep`

**關鍵概念：** Semantic Grep（語意化 grep，基於 Multi-Vector Embeddings）

***
### 8. 工具選型實戰建議：Low Floor × High Ceiling [43:35]
搜尋工具不存在「銀彈」，應組合使用：

| 工具類型 | 優勢 | 場景 |
|---------|------|------|
| **專用搜尋工具**（低門檻） | 參數簡單、錯誤率低 | 已知高頻查詢行為 |
| **通用查詢工具**（高天花板） | 可應對複雜/意外問題 | 長尾需求、聚合計算 |
| **Shell Tool** | 極度靈活 | 探索性任務、多元資料源 |

**建議策略：** 若不了解 Agent 查詢行為 → 先部署通用工具 → **記錄 Agent 行為日誌** → 發現高頻模式後建立專用工具。更強大的 LLM 可顯著降低通用工具的參數錯誤率。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

**關鍵概念：** Low Floor × High Ceiling（低門檻 × 高天花板的工具設計哲學）

***
## [結論與行動建議]
**啟發金句：**
> 「好的搜尋極其困難，這正是為什麼我們需要多種搜尋技術——沒有銀彈，只有適合當下的組合。」

**具體行動建議（S-L-T 法則）：**
- **S（Specialize）** — 為已知的高頻查詢打造專用低門檻工具
- **L（Log）** — 記錄 Agent 的每一次工具呼叫行為，找出瓶頸
- **T（Tool Description）** — Tool Description 的品質決定 90% 的工具呼叫準確率

**生活實踐建議：**
作為 AI Application 架構師，設計 Agent 時可立即套用此框架：
1. 新專案初期 → 先用 Shell Tool 或通用 DB Query Tool 快速驗證
2. 上線前 → 分析 log，找出 Top 3 高頻查詢類型，打造專用語意搜尋工具
3. Tool Description 撰寫 → 加入「何時用」「何時不用」「與其他工具的呼叫順序」三段式結構

***
## [參考連結]
- 原始影片：https://youtu.be/ynJyIKwjonM?si=6NuQc75_80WwrRC2 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)
- 講者 Twitter：https://x.com/helloiamleonie
- 講者 LinkedIn：https://www.linkedin.com/in/804250ab/
