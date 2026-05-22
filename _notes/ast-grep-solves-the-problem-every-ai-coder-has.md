---
title: 'ast-grep 解決 AI 程式代理的隱藏漏洞'
date: 2026-05-21
image: /images/AI筆記/ast-grep-solves-the-problem-every-ai-coder-has.jpeg
category: AI筆記
tags: [AI代理, AST, 程式碼搜尋, ast-grep, Claude Code]
description: '所有主流 AI 程式代理（Claude Code、Cursor、Copilot）都共用一個根本盲點：依賴文字搜尋（text search）而非程式碼結構搜尋。這導致代理誤判字串為真實程式碼呼叫，開啟不必要的檔案、消耗大量 token、並讓你多付費。'
quote: '你的 AI 代理每次 refactor 都多付出 122% 的代價——這不是 AI 的問題，是搜尋工具的問題。'
action: '立即安裝 ast-grep 並在 refactor 提示中加入「Use ast-grep to find」，30 秒完成、每月省下 ~$15。'
source_has_timestamps: true
source_raw: ast-grep Solves the Problem Every AI Coder Has
---

# ast-grep 解決 AI 程式代理的盲點

## [核心摘要]

所有主流 AI 程式代理（Claude Code、Cursor、Copilot）都依賴**文字搜尋（text search）**而非程式碼結構搜尋，導致大量 token 浪費。**ast-grep** 透過解析 AST（抽象語法樹）讓代理真正「讀懂程式碼」，在真實測試中將搜尋過數達到 122% 的 grep 過計問題徹底消除，每位開發者每月可節省約 $15 的純粹浪費成本。

***

## [詳細重點整理]

### 1. AI 代理的核心盲點 [00:00]

所有 AI 程式代理的搜尋引擎底層都是 ripgrep（文字搜尋），它看見的是「字元串」而非「程式碼結構」。 當代理被要求清理 debug log 時，它會把測試夾具（test fixture）中的字串 `"console.log hi"` 當成真實的函式呼叫進行分析，並向你收費。

**關鍵概念：結構性盲點（Structural Blindness）**

### 2. ast-grep 的運作機制 [00:59]

ast-grep 以三個步驟運作：
- **Tree-sitter 解析**：將每一行程式碼轉換成節點樹（AST），每個節點被標記為函式、呼叫、字串、註解等具體類型
- **節點模式匹配**：使用 `$VAR`（單節點）和 `$$$BODY`（多節點列表）等**元變數（Meta-Variables）**，對樹狀結構進行匹配，而非對文字比對
- **Rust 多核心執行**：全程式庫掃描速度極快，可在代理迴圈中每隔幾秒執行一次

**關鍵概念：抽象語法樹（AST, Abstract Syntax Tree）**

### 3. 實測數據對比 [02:39]

在 Archon 真實重構場景下，5 種常見搜尋的過計率如下：

| 搜尋目標 | grep 過計率 | 實際情況 |
|---|---|---|
| Debug logs | +26% | 混入測試夾具字串 |
| setTimeout | +19% | 混入字串常數 |
| Promise chains | +30% | 混入字串字面值 |
| **useState hooks** | **+122%** | **138 hits vs 62，30 檔 vs 26 檔** |

**關鍵概念：Token 過計損耗（Token Over-Count）**

### 4. Token 經濟學計算 [03:20]

掃描 22 個檔案約消耗 11,000 tokens，一次重構約 $0.01。 若團隊每天執行 50 次重構、每月 30 天，每位開發者每月浪費 **$15**，全部源於錯誤的搜尋工具選擇。

**關鍵概念：代理執行成本（Agent Runtime Cost）**

### 5. 與競品工具的差異 [03:53]

| 工具 | 特性 | 缺點 |
|---|---|---|
| **Semgrep** | 支援資料流分析、安全規則 | CLI 速度慢，日常重構過重 |
| **Comby** | 語法感知但通用 | 缺乏 AST 節點精準度 |
| **GritQL** | 多範式 DSL | 學習曲線陡峭 |
| **IntelliJ 結構搜尋** | 功能強大 | 綁定 JetBrains 生態 |
| **ast-grep** | 輕量、20+ 語言、易於整合 | 需明確指示代理使用 |

**關鍵概念：輕量結構化搜尋（Lightweight Structural Search）**

### 6. 30 秒整合方式 [05:23]

兩個指令即可完成整合：

```bash
npm install -g @ast-grep/cli          # 安裝 CLI 工具
npx skills @ast-grep/agent-skill      # 安裝代理技能
```

重啟 Claude Code 後，必須**明確告訴代理「Use ast-grep to find...」**，否則代理仍會預設使用舊的文字搜尋。

***

## [結論與行動建議]

**啟發金句：** A regular search sees characters. ast-grep sees structure. 

**具體行動建議（S-A-T 法則）**：
- **S（Structure）**：用結構搜尋取代文字搜尋
- **A（Add skill）**：兩條指令整合 ast-grep 至代理
- **T（Tell explicitly）**：明確指示代理使用 ast-grep，不要假設它會自動選擇

**生活實踐建議：** 在進行大規模程式碼重構前，先用 ast-grep 做一次預掃描，比對 grep 和 ast-grep 的結果數量差異。若差距超過 20%，代表你的程式庫有大量誤判風險，立即切換搜尋工具可直接降低 AI 代理成本。

***

## [參考連結]

- 原始影片：[https://youtu.be/ITfmH9FPlT0](https://youtu.be/ITfmH9FPlT0) 
- ast-grep GitHub（Rust CLI，13.8k stars）：https://github.com/ast-grep/ast-grep 
- Claude Code 官方 ast-grep Skill：https://github.com/ast-grep/agent-skill 
- ast-grep MCP Server（實驗性）：https://github.com/ast-grep/ast-grep-mcp
