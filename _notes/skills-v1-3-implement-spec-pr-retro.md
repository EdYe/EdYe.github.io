---
title: 'Skills v1.3：implement-spec、pr 與 retro'
date: 2026-10-06
image: /images/影片筆記/skills-v1-3-implement-spec-pr-retro.jpg
category: 影片筆記
tags: [子代理編排, 任務圖, 合併風險, 詞彙表, 回顧]
description: '本片介紹 Matt Pocock 的 Skills repo v1.3，核心貢獻是三個新 skill：implement-spec 用子代理自動編排多張 ticket，實現「離開鍵盤（AFK）」式的大型'
quote: '💡不要求證據，agent 就會說「應該可以」——驗證才是信任 agent 的唯一途徑。'
action: '🎯R-R-R 法則：審 PR 先看 blast radius 與門的方向、空閒時抽樣跑 retro、ticket 編排從手動升級到確定性腳本。'
source_has_timestamps: true
---
# Skills v1.3 筆記：/implement-spec、/pr、/retro [youtube](https://www.youtube.com/watch?v=BsJGo1wFTvQ)

## [核心摘要]

本片介紹 Matt Pocock 的 Skills repo v1.3，核心貢獻是三個新 skill：**implement-spec** 用子代理自動編排多張 ticket，實現「離開鍵盤（AFK）」式的大型工作落地；**pr** 提供結構化 PR 模板（摘要、證據、合併風險），解決人類 code review 瓶頸；**retro** 回顧 coding agent 的歷史 session，挖掘 agent 自己不會報告的隱性低效率。痛點：手動跑 ticket 迴圈太累、PR 難審、agent 的錯誤無人察覺。 [youtube](https://www.youtube.com/watch?v=BsJGo1wFTvQ)

## [詳細重點整理]

### 1. v1.3 總覽與三個新技能 [00:00]
v1.3 帶來三個關鍵 skill：implement-spec、PR、retro。其中 retro 在社群上反應最熱烈，被形容為「game changer」。

### 2. implement-spec：用子代理編排大型工作 [00:25]
大規模工作的落地流程是「一個 spec + 多張 ticket」：spec 定義目的地，ticket 把目的地拆成可在單一 coding agent 中執行的 session。若一次塞進同一個 agent，會進入 **dumb zone**（笨蛋區），觸發 auto-compact，導致品質下降。

**關鍵概念：三種迴圈編排方式**
- **手動迴圈（Manual Loop）**：使用者自己當 for loop，逐張下指令、清 context，不可行。
- **確定性迴圈（Deterministic Loop）**：用腳本讀取 ticket 並自動執行，最可靠、最便宜，但建置複雜，對新手門檻過高。
- **子代理編排（Sub-agent Orchestration）**：由 agent 幫忙「當保母」，每張 ticket 由子代理實作。因為子代理現在可以再產生子代理，功能已與 orchestrator 同級。這是 implement-spec 的本質，定位為 AFK 工作流的入門方案。

implement-spec 的九步流程：讀取 spec 與 tickets → 用子代理探索程式碼 → 建立 integration branch → 用 implement 子代理以 **TDD + worktrees** 實作每張 ticket → 合併回 integration branch → 觸發更多 implement 子代理 → 全部完成後呼叫 code review → 清理 → 產出單一 PR。

**關鍵概念：Task Graph（任務圖）**——tickets 不是線性步驟清單，而是帶有阻斷關係（blocking relationships）的任務圖，因此永遠存在一個「可被領取的 frontier」，實作時能平行化就平行化。

### 3. PR skill：讓人類審查盡可能簡單 [04:54]
靈感來自 Dex Hies 的「Show Me」skill——用簡潔圖表與偽代碼協助使用者視覺化理解主題。PR 仍是工作進 main 的主要瓶頸，此 skill 提供 PR body 模板，包含三個區塊：

- **Summary（摘要）**：基於 Show Me 模板的視覺化說明。
- **Evidence（證據）**：改動前後的對比。要求 agent 提供證據，往往促使它多跑一次測試或多截一張圖——**關鍵概念：驗證思維（Verification）**。不要求硬證據時，agent 很容易只憑讀過程式碼就宣稱「應該可以」。
- **Merge Danger（合併風險）**：**關鍵概念：單向門 vs 雙向門（One-way door vs Two-way door）**——雙向門代表可輕易 revert；單向門代表會刪資料或回滾成本高。再搭配 **Blast Radius（爆炸半徑）**：小半徑 + 雙向門的 PR 幾乎不需細審。

此 skill 是最穩定被自動觸發的 skill 之一（在 Opus 5.5 上幾乎每次都會自動套用），下載後 PR body 品質會直接提升。

### 4. context.md 更名為 glossary.md [08:10]
Domain modeling skill 改為寫入 `glossary.md` 而非 `context.md`。原因：`context.md` 語意過於模糊，無法觸發 agent 在正確時機讀取，使用者也不好理解。內容也已精簡到只剩詞彙表（glossary），故名實相符。許多 skills 依賴看到 `glossary.md` 才會正確使用領域語言，需同步更新。

### 5. retro skill：挖掘 agent 不會自己報告的問題 [09:37]
**關鍵概念：回顧（Retrospective）**。retro 針對 coding agent 的 session（當前、前一個或數個）提出改善建議，因為 agent 「不像它應該的那樣會抱怨」，也不會主動修自己的錯，需要另一個 agent 回頭檢視。實測發現的問題包括：

- Agent 在使用者未選定修法前就執行了不可逆的公開動作（擅自跑 release，導致只有 1.3.1 而無 1.3.0 release）
- Repo 沒有 CI pipeline，pnpm check 腳本沒有東西在執行
- 長 session 中 compaction 前後發生 **context loss**（上下文流失），重複指令應搬進 skill
- 自製 CLI（course video manager）浪費 token、Wiki CLI 不在 path 上

**關鍵概念：Human-in-the-loop（人機協作）**——retro 設計上刻意不自動化修復。若全自動，agent 會陷入不斷找到誤報、不斷修復的迴圈，把 repo 和 agent 帶往不該去的地方。建議用法：有空時對近期 sessions 抽樣跑 retro，特別是感覺「agent 做了怪事」的 session。

retro 檢查的改善類別：程式碼庫可導航性、可加入的自動檢查、可讓自動審查者執行的編碼標準、全域 agents.md 的健康度、token 經濟、指令中的 noop、agent 的資訊存取完整性。

### 6. AI Coding Crash Course [14:06]
aihero.dev 的課程同日更新，新增聚焦 implement-spec 的單元。

## [結論與行動建議]

**啟發金句**：「不要求證據，agent 就會說『應該可以』——驗證才是信任 agent 的唯一途徑。」

**具體行動建議：R-R-R 法則（Review the PR, Run the retro, Refactor the loop）**——審 PR 時先看 blast radius 與門的方向；空閒時抽樣跑 retro 找隱性低效率；ticket 編排從手動逐步升級到確定性腳本。

**生活實踐建議**：
- 在自己的 Gitea + Actions 工作流中套用「雙向門 / 單向門」分類，決定哪些自動化步驟需要人工簽核（例如 publish release 就屬單向門）
- 寫自動化腳本（webhook、Action）時強制附上「before/after 證據」，例如截圖或測試輸出，而不是相信腳本「應該成功」
- 定期回顧自己與 Claude Code 的歷史 session，把重複出現的指令蒸餾成 skill 或 agents.md 條目，降低 token 消耗

## [參考連結]

- [原始影片：New Skills! v1.3 brings /pr, /implement-spec, and /retro](https://youtu.be/BsJGo1wFTvQ)
- [Skills v1.3 Changelog](https://www.aihero.dev/skills/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md)
- [AI Coding Crash Course](https://aihero.dev/s/xrT0hb)