圖片不存在，設為 TODO。根據 CLAUDE.md 規範輸出完整 Jekyll .md 檔案：

```markdown
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

# ast-grep 解決 AI 程式代理的隱藏漏洞

## [核心摘要]

所有主流 AI 程式代理（Claude Code、Cursor、Copilot）都共用一個根本盲點：**依賴文字搜尋（text search）而非程式碼結構搜尋**。這導致代理誤判字串為真實程式碼呼叫，開啟不必要的檔案、消耗大量 token、並讓你多付費。**ast-grep** 透過 Tree-sitter AST 解析，讓代理真正「讀懂」程式碼結構，可將搜尋誤報率降低超過 50%，直接削減每位開發者每月約 $15 的無謂支出。 [youtube](https://www.youtube.com)

***

## [詳細重點整理]

**1. AI 代理的共同盲點 [00:00]**

所有 AI 程式代理的搜尋底層都是文字比對（text search），它只看字元，無法區分「真正的函式呼叫」與「在字串或註解裡出現的相同文字」。當你要求清理 debug logs 時，代理找到 164 個結果，其中有許多只是測試 fixture 裡的字串 `"console.log('hi')"`——它並非真實呼叫，但代理照樣打開整個檔案並向你收費。 [youtube](https://www.youtube.com)

> **關鍵概念：文字搜尋盲點（Text Search Blind Spot）**

***

**2. ast-grep 的運作原理 [00:59]**

ast-grep 的搜尋機制分三個步驟： [youtube](https://www.youtube.com)

- **Tree-sitter 解析**：將每一行程式碼轉換為 AST（抽象語法樹），每個節點都被標記為其實際身分（函式呼叫、字串、註解等）
- **節點模式比對**：以 Meta-Variable 撰寫搜尋模式，`$VAR` 匹配任意單一節點，`$$$BODY` 匹配任意節點列表；對樹節點匹配，不對文字匹配
- **Rust 多核心執行**：以 Rust 實作，利用所有 CPU 核心，全程式碼庫掃描速度極快

> **關鍵概念：AST（抽象語法樹, Abstract Syntax Tree）**

***

**3. 實測數據對比 [02:06]**

在真實的 Archon 程式庫上針對 5 種常見搜尋做比較，文字搜尋的誤報率如下： [youtube](https://www.youtube.com)

***

## [技術/數據對比]

| 搜尋目標 | 文字搜尋誤報率 | ast-grep 結果 |
|---|---|---|
| `console.log`（debug logs） | 多計 26% | 12 檔案（vs 22） |
| `setTimeout` | 多計 19% | 精準節點匹配 |
| Promise chains | 多計 30% | 精準節點匹配 |
| `useState` hooks | **多計 122%** | 62 次（vs 138 次） |
| 整體 refactor | 138 hits / 30 files | 62 hits / 26 files |

每個誤報 = 代理多開一個檔案 = 多消耗約 500 tokens = 多付費。 [youtube](https://www.youtube.com)

***

**4. 競品比較分析 [03:53]**

| 工具 | 定位 | 缺點 |
|---|---|---|
| **Semgrep** | 安全規則、資料流分析 | 重量級，日常 refactor 過殺 |
| **Comby** | 泛用語法感知搜尋 | 缺乏 AST 語言節點精度 |
| **GritQL** | 多範式 DSL | 學習曲線高 |
| **IntelliJ Structural Search** | IDE 結構搜尋 | 綁定 JetBrains 生態 |
| **ast-grep** | 輕量 CLI，20+ 語言 | 今日仍需明確呼叫工具名稱 |

 [youtube](https://www.youtube.com)

***

**5. 安裝只需 30 秒 [05:23]**

兩行指令即可讓 Claude Code 擁有結構搜尋能力： [youtube](https://www.youtube.com)

```bash
npm install -g @ast-grep/cli
npx skills @ast-grep/agent-skill
```

重啟 Claude Code 後，需**明確告訴代理「Use ast-grep to find」**，否則代理仍會退回文字搜尋。

> **關鍵概念：Agent Skill 注入（Agent Skill Injection）**

***

## [結論與行動建議]

**💡 啟發金句：**
> **「你的 AI 代理每次 refactor 都多付出 122% 的代價——這不是 AI 的問題，是搜尋工具的問題。」** [youtube](https://www.youtube.com)

**⚡ 具體行動建議（P-A-S 法則）：**
- **Parse**（解析）：讓工具先把程式碼轉成 AST，再開始搜尋
- **Act**（精準行動）：只對真實節點進行匹配，不對字元進行比對
- **Save**（省錢省 token）：用結構搜尋取代文字搜尋，每月每人省下 ~$15

**🛠️ 生活實踐建議：**

1. **立即行動**：若你的團隊使用 Claude Code，今天就跑上述兩行指令，30 秒安裝完成
2. **Prompt 習慣**：在指派 refactor 任務時，養成在提示中加入「Use ast-grep to find」的習慣
3. **成本意識**：下次審查 AI 代理的 token 使用報告時，特別關注搜尋類任務的誤報比例，這是最直接可優化的成本項目

***

## [參考連結]

- 📺 原始影片：https://youtu.be/ITfmH9FPlT0
- 🔧 ast-grep GitHub（Rust CLI，13.8k stars）：https://github.com/ast-grep/ast-grep
- 📖 ast-grep 官網 + 20 種語言列表：https://ast-grep.github.io/
- 🤖 Claude Code 官方 ast-grep skill：https://github.com/ast-grep/agent-skill
- 🔌 ast-grep MCP server（實驗版）：https://github.com/ast-grep/ast-grep-mcp
```

---

注意：`image` 欄位的圖片檔案目前不存在於 `images/AI筆記/` 目錄中，需要補上圖片後才能正常顯示。建議將圖片存為 `images/AI筆記/ast-grep-solves-the-problem-every-ai-coder-has.jpeg`，或改用 TODO 標記佔位。
