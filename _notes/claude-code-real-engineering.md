---
title: 'Claude Code 實戰：多階段計劃管理大型工程任務'
date: 2026-05-01
image: /images/影片筆記/claude-code-real-engineering.jpeg
category: 影片筆記
tags: [Claude Code, Plan Mode, 多階段計劃, GitHub Issue, 上下文管理]
description: '處理大型工程任務時，單一上下文視窗往往不夠用。本影片展示以多階段計劃驅動 Claude Code 的實戰工作流，讓 AI 輔助開發從混亂變成可重複、可追蹤的工程流程。'
quote: '重要的不是你在做什麼，而是你怎麼做它——大型任務的成敗，在第一行程式碼之前就已決定。'
action: '採用 P-C-E 法則：Plan（先進規劃模式）→ Commit（每階段結束即提交）→ Externalize（用 GitHub Issue 持久化計劃）'
source_has_timestamps: true
---
## 核心摘要

處理大型工程任務時，單一上下文視窗往往不夠用。本影片展示一套以 **多階段計劃（Multi-Phase Plan）** 驅動 Claude Code 的實戰工作流：先強制規劃、再分段執行、以 GitHub Issue 作為跨對話橋樑，配合極簡記憶規則，讓 AI 輔助開發從混亂變成可重複、可追蹤的工程流程。

---

## 詳細重點整理

### 1. 用語音輸入與 Plan Mode 啟動任務 [00:00]

用語音輸入工具將任務需求口述為初始 prompt，不需要精心撰寫。啟動 Claude Code 時，透過 Shift+Tab 切換到底部左側的 **Plan Mode**（規劃模式），強制 AI 在任何大型任務前先制定計劃，而非直接產出程式碼。

**關鍵概念**：**Plan Mode（規劃模式）** — 阻止 Claude Code 立即寫程式，改為先探索程式庫、提問、輸出計劃。

---

### 2. 探索子代理 + 澄清問題迴圈 [01:00]

Plan Mode 啟動後，Claude Code 自動派出 **探索子代理（Explore Sub-Agent）** 掃描現有程式庫結構，再以互動式多步驟表單的形式提出澄清問題（如：用 positional argument 還是 required option？匹配方式要嚴格還是彈性？）。使用者逐一回答，形成一個確認需求的迴圈，此時完全沒有寫任何程式碼。

**關鍵概念**：**澄清問題迴圈（Clarifying Questions Loop）** — 在執行前窮盡規格模糊點，將人類決策集中在前置階段。

---

### 3. 記憶檔案的「極簡規則」 [02:42]

User Memory 檔案只有 43 行，核心規則是：

> "In all interactions and commit messages, be extremely concise and sacrifice grammar for the sake of concision."

此規則讓計劃輸出緊湊易讀，也讓計劃末尾自動附帶一個「未解決問題清單」（Unresolved Questions），供使用者快速回覆補充資訊。

**關鍵概念**：**極簡記憶規則（Conciseness Memory Rule）** — 透過 User Memory 控制全域輸出風格，代替每次在 prompt 重複說明。

---

### 4. 拆分多階段計劃以管理上下文 [04:06]

當計劃規模超出單一對話視窗時，在計劃確認後明確指示 Claude：「make the plan multi-phase」，使其將實作步驟拆成多個可獨立執行的 Phase。執行前先用 `/context` 指令確認剩餘空間（此時 83.7% 空閒，僅用 33k tokens）。

**關鍵概念**：**多階段計劃（Multi-Phase Plan）** — 將大型功能水平切割為可逐段執行、可分配上下文的小任務。

---

### 5. 分段執行與 Accept Edits 模式 [05:00]

計劃確認後，切換至 **Accept Edits On** 模式並下達 "execute phase one"。每個 Phase 結束後：
- 用 VS Code git diff 檢視變更
- 對已完成的 Phase 做 commit 或 git stage，明確標記進度
- 用 `/context` 確認 token 用量（Phase 1 僅消耗 ~3k tokens）

**關鍵概念**：**階段邊界提交（Phase Boundary Commit）** — 每階段結束即 stage/commit，讓版本歷史與計劃階段一一對應。

---

### 6. 以 GitHub Issue 作為跨視窗計劃持久化 [07:56]

當需要清空上下文時，指示 Claude 將含進度的完整計劃（已完成 ✓ 標記）透過 `gh issue create` 存入 GitHub。清空後，只需輸入 "get GitHub issue #24 and enact phase 4" 即可在全新上下文中無縫接續，不損失任何計劃資訊。Issue 還有一個隱性好處：團隊成員可非同步留言、補充需求。

**關鍵概念**：**計劃外部化（Plan Externalization）** — 用 GitHub Issue 作為跨上下文視窗的持久化記憶，取代容易消失的對話記錄。

---

## 技術 / 數據對比

| 階段 | 消耗 Token | 上下文剩餘 |
|------|-----------|-----------|
| 規劃 + 探索完成後 | ~33k | 83.7% |
| Phase 1 執行 | ~3k 增量 | 健康 |
| Phase 2-3 執行 | 持續健康 | 健康 |
| 清空上下文後 | 16k（僅 memory + system） | 接近 100% |

---

## 結論與行動建議

**啟發金句**：「重要的不是你在做什麼，而是你怎麼做它——大型任務的成敗，在第一行程式碼之前就已決定。」

**具體行動建議**：**P-C-E 法則（Plan → Commit → Externalize）**
1. **Plan**：所有大型功能都先進 Plan Mode，強迫 AI 問清楚需求
2. **Commit**：每個 Phase 結束立即 stage/commit，邊界清晰
3. **Externalize**：上下文不夠時，把計劃存進 GitHub Issue，不怕重開視窗

**生活實踐建議**：
- 在 Claude Code User Memory 加入一行：「所有輸出、commit 訊息請極度簡潔，可犧牲語法換取精簡」，立即提升計劃可讀性
- 當一個功能感覺「有點複雜」時，主動輸入 "make the plan multi-phase"，不要等 context 爆了才後悔
- 用語音輸入工具起草初始 prompt，10 秒口述比 5 分鐘打字更快進入規劃迴圈

---

## 參考連結

- [How I use Claude Code for real engineering](https://youtu.be/kZ-zzHVUrO4?si=wsJHoeEbPPQebRHa)
