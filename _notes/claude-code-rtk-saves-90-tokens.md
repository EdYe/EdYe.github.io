---
title: 'Claude Code + RTK：節省 90% Token 消耗'
date: 2026-05-27
image: /images/影片筆記/claude-code-rtk-saves-90-tokens.jpeg
category: 影片筆記
tags: [Context Window, Token壓縮, RTK, Shell指令, 輸出蒸餾]
description: 'RTK（Runtime Token Kit）是一個免費開源的 CLI 工具，專門解決 Claude Code 使用 shell 指令時的 Context Window 爆炸問題。它攔截終端機指令的原始輸出，壓縮後才送入 Claude 的上下文記憶體，在典型的 30 分鐘工作 Session 中可將 Token 消耗從 11.8 萬降至約 2.39 萬'
quote: '節省 Token 不靠省著用，靠在資訊進入 Context 之前就把它壓縮。'
action: '5 分鐘安裝 RTK，執行 cargo install rtk 與 rtk init -g 全域初始化，自動壓縮所有 shell 指令輸出'
source_has_timestamps: true
---
# [核心摘要]

**RTK（Runtime Token Kit）** 是一個免費開源的 CLI 工具，專門解決 Claude Code 使用 shell 指令時的 **Context Window 爆炸問題**。它攔截終端機指令的原始輸出，壓縮後才送入 Claude 的上下文記憶體，在典型的 30 分鐘工作 Session 中可將 Token 消耗從 11.8 萬降至約 2.39 萬，節省 80% 費用，且安裝後完全靜默執行、零維護。 [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)

***

# [詳細重點整理]

## 1. 為什麼 Token 被燒光？[00:00]

Claude Code 每執行一條終端機指令（如 `git status`、`npm install`、`git diff`），就會把指令的**完整原始輸出**塞入 Context Window。例如 `npm install` 可能產生 47 行輸出，全數計為 Token，長期累積下來一個工作 Session 即可燒掉 118,000 tokens。 [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)

**關鍵概念：Context Window 消耗複利效應** — 每條指令的輸出都疊加在同一個 Context 內，不會自動清除，形成累積性的 Token 膨脹。

## 2. RTK 如何攔截壓縮？[00:19]

RTK 插入在「Claude Code 發出指令 → 原始輸出回傳」這條鏈路的中間層。它讀取原始輸出後，萃取出「已安裝套件、警告、錯誤」等關鍵摘要，再以**數行結構化摘要**取代數十行原始文字傳給 Claude。Claude 依然獲得足夠的語意資訊繼續協作，但 Token 消耗僅為原始量的一小部分。 [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)

**關鍵概念：輸出蒸餾（Output Distillation）** — 保留語意但剔除冗餘格式字符，是 RAG 與 Prompt 壓縮領域的核心技術原理。

## 3. 安裝流程（一次性設定）[01:42]

1. 前往 `rustup.rs` 安裝 Rust 套件管理器 `cargo`
2. 執行 `cargo install rtk`
3. 執行 `rtk init -g`（全域初始化，自動覆蓋 CLI 及 VS Code Extension）
4. 重啟 Claude Code / VS Code
5. 隨時執行 `rtk gain` 查看累積節省量 [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)

## 4. 實測結果 [02:52]

連續執行 `git status`、`git log --oneline -20`、`git diff`、`ls` 等指令後，`rtk gain` 顯示：**10 條指令節省了 76% Token（6,800 tokens）**，主要節省來源為 `git diff`。 [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)

**關鍵概念：Shell-Heavy vs File-Heavy Session** — RTK 只攔截 shell 指令輸出；若大部分操作是 Claude Code 用內建工具**直接讀取檔案**，則 RTK 無法介入。

***

# [技術/數據對比]

| 指令 | 原始 Token（×10次） | RTK 後 Token | 節省率 |
|---|---|---|---|
| `git status` | 3,000 | 600 | 80% |
| `npm install` | ~高 | 壓縮摘要 | 70–92% |
| `git diff` | 最高 | 大幅壓縮 | ~92% |
| **整體 Session** | **118,000** | **23,900** | **~80%** |

 [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)

***

# [結論與行動建議]

**啟發金句：** 節省 Token 不靠省著用，靠在資訊進入 Context 之前就把它壓縮。

**具體行動建議（I-C-G 法則）：**
- **I**nstall：5 分鐘一次性安裝，`cargo install rtk`
- **C**onfigure：`rtk init -g` 全域設定，覆蓋所有工具
- **G**ain：定期 `rtk gain` 追蹤累積節省量，強化節省意識

**生活實踐建議：** 若你是日常重度使用 Claude Code 進行系統架構設計或 API 串接的開發者，shell 指令佔比高，RTK 帶來的節省將非常顯著。即使 Session 以檔案操作為主，也建議安裝——因為只要有 shell 指令，它就自動生效，最差情況也只是「幫你少省一點」。 [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)

***

# [參考連結]

- 📺 原始影片：https://youtu.be/CncyYt9ozAQ?si=OwfCmBBvhcbqruIL [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)
- 🔧 RTK GitHub：https://github.com/rtk-ai/rtk [youtube](https://www.youtube.com/watch?v=m3i2mk5hs8U)
