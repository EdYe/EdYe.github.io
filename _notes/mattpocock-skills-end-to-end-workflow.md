---
title: 'Matt Pocock 的 AI 代理開發工作流'
date: 2026-07-18
image: /images/AI筆記/mattpocock-skills-end-to-end-workflow.jpg
category: AI筆記
tags: [Skills Repo, Grill with Docs, 智慧區門檻, 雙軸審查, Spec與Tickets]
description: 'Matt Pocock 的 skills repo 以 Claude Code 為核心，透過 Grill→Spec→Tickets→Implement 流程解決上下文有限與品質難控管的痛點。'
quote: '💡對齊先於實作，壓縮先於擴張——AI 開發的效率不在於跑得多快，而在於每一步都把上下文花在刀口上。'
action: '🎯依 G-S-T-I 法則：Grill 訪談需求、Spec 壓縮規格、Tickets 拆分工單、Implement 觸發雙軸 Code Review。'
source_has_timestamps: true
---
## [核心摘要]

Matt Pocock 的 skills repo 是一套以 Claude Code 等 AI 代理為核心的開發工作流框架，擁有超過 17 萬 GitHub stars 與 750 萬次下載量。其核心價值在於解決 AI 輔助開發中「上下文視窗有限、規劃與實作混雜、品質難以控管」三大痛點，透過 **Grill-with-docs → Spec → Tickets → Implement（含 Code Review）** 的結構化流程，將模糊想法逐步壓縮為可執行、可審查的程式碼變更，並透過 sub-agent 機制確保程式碼審查品質 。 [scribd](https://www.scribd.com/document/869199074/Links)

***

## [詳細重點整理]

### 1. 安裝 Skills Repo [00:54]

使用 `npx skills@latest add mattpocock/skills` 安裝，需預先具備 Node.js 環境。安裝過程中可選擇 38 個 skills，分為官方認可的 `mattpocockskills` 與實驗性 skills 兩組。安裝器支援多種代理（Claude Code、Cursor、Codex 等），安裝範圍可選專案級或全域級。團隊協作建議使用專案級確保技能一致性；個人開發者可選全域級 。 [scribd](https://www.scribd.com/document/869199074/Links)

**關鍵概念：安裝範圍選擇（Installation Scope）**

### 2. Skills 的上下文效率設計 [02:30]

所有 skills 採用 user-invoked 設計，描述精簡。即使安裝全部 skills，僅佔用約 660 tokens 的上下文負載，與其他動輒大量滲透 context 的 skills 庫形成鮮明對比 。 [scribd](https://www.scribd.com/document/869199074/Links)

**關鍵概念：上下文極簡化（Context Minimalism）**

### 3. 執行 Setup 與配置 [04:34]

執行 `setup-mattpocock-skills` 進行初始化，包含三項配置：
- **Issue Tracker**：支援 GitHub、Jira、Linear、本地 markdown 等，代理會根據指示自動配置
- **Triage Labels**：用於標記與分類 ticket，可接受預設值
- **Domain Docs**：生成 `context.md` 與 ADR（Architecture Decision Records），分為 single-context 與 multi-context 兩種模式，99% 的專案適用 single-context [scribd](https://www.scribd.com/document/869199074/Links)

**關鍵概念：狀態化配置（Stateful Configuration）**

### 4. Ask Matt 技能：互動式導引 [06:52]

`ask-matt` 技能內建 skills repo 的完整知識，可作為入門指南使用。它會根據當前專案狀態建議主要流程，並強調應在「一個不中斷的 context window」中走完主流程，凸顯對 token 使用效率的意識 。 [scribd](https://www.scribd.com/document/869199074/Links)

**關鍵概念：元技能導引（Meta-Skill Guidance）**

### 5. Grill with Docs：需求訪談 [08:31]

`grill-with-docs` 是流程起點，透過結構化提問將模糊想法轉化為清晰計畫。它會自動探索程式碼庫，提出追問（通常 20 題左右），直到雙方達成 shared understanding 後輸出具體執行計畫。此步驟的核心價值在於：將「我想改 X」轉化為「可辯護的計畫」。 [scribd](https://www.scribd.com/document/869199074/Links)

**關鍵概念：漸進式需求淬鍊（Progressive Requirement Refinement）**

### 6. 智慧區與上下文管理 [11:30]

Matt 將 LLM 的「智慧區」定義為約 140k tokens 以內。超過此門檻會出現 attention degradation，導致幻覺與品質下降。這是決定是否將工作拆分為多 session 的關鍵判斷依據 。 [scribd](https://www.scribd.com/document/869199074/Links)

**關鍵概念：智慧區門檻（Smart Zone Threshold）**

### 7. Spec 與 Tickets：跨 session 壓縮 [10:08]

當工作需跨越多個 context window 時，使用 `to-spec` 將訪談討論壓縮為規格文件（含問題陳述、解決方案、使用者故事、實作決策、測試決策），再透過 `to-tickets` 將規格拆分為單一 context window 大小的工單。每張 ticket 對應一個獨立的 agent session 。 [scribd](https://www.scribd.com/document/869199074/Links)

**關鍵概念：上下文蒸餾（Context Distillation）**

### 8. Implement 與 Code Review [13:51]

`implement` 技能執行實作，並在過程中自動運行型別檢查、建置、驗證。Code Review 採用雙軸審查機制：
- **對比 Spec**：逐條核對驗收標準是否達成
- **對比 Standards**：檢查是否符合程式碼規範（若專案無規範文件，則套用 Martin Fowler 的經典 code smell 檢查）

審查由 sub-agent 執行，避免主代理「自我審查盲區」——代理往往難以批判自己剛寫的程式碼 。 [scribd](https://www.scribd.com/document/869199074/Links)

**關鍵概念：雙軸審查與子代理隔離（Dual-Axis Review with Sub-Agent Isolation）**

***

## [技術/數據對比]

| 維度 | 單 Session 流程 | 多 Session 流程 |
|---|---|---|
| 適用場景 | 工作量 < 140k tokens | 工作量超出智慧區 |
| 流程步驟 | Grill → Implement | Grill → Spec → Tickets → Implement |
| 上下文管理 | 單一不中斷 window | 每 ticket 清空重啟 |
| 審查方式 | Implement 內建 Code Review | 逐 ticket 實作 + 最終 Spec 比對 |

| Skills 特性 | Matt Pocock Skills | 一般 Skills 庫 |
|---|---|---|
| 調用方式 | User-invoked（手動觸發） | 自動滲透 context |
| Token 佔用 | ~660 tokens | 通常更高 |
| 審查機制 | 雙軸 sub-agent 審查 | 無或主代理自審 |

***

## [結論與行動建議]

### 啟發金句

> 「對齊先於實作，壓縮先於擴張——AI 開發的效率不在於跑得多快，而在於每一步都把上下文花在刀口上。」

### 具體行動建議：G-S-T-I 法則

- **G**rill：用 grill-with-docs 訪談淬鍊需求
- **S**pec：壓縮討論為規格文件（多 session 時使用）
- **T**ickets：拆分為智慧區大小的工單
- **I**mplement：實作並觸發雙軸 Code Review

### 生活實踐建議

在日常工作流程中，可將 G-S-T-I 法則應用於任何需要 AI 代理協作的複雜任務：先以「訪談」釐清需求邊界（Grill），再將共識文件化為可追溯的規格（Spec），拆解為可獨立完成的任務單元（Tickets），最後在執行時導入獨立的審查機制（Implement + Review）。即使不使用 Matt 的 skills 庫，這套「對齊 → 規格化 → 拆解 → 審查」的思維框架同樣適用於任何 AI 輔助開發場景 。 [scribd](https://www.scribd.com/document/869199074/Links)

***

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/M6mYodf0dJM?si=7Bq8WylmXFPB2cJd
- Skills Repo：https://aihero.dev/s/4arzG4
- 訂閱更新：https://aihero.dev/s/4arzG4/subscribe
- Discord 社群：https://aihero.dev/s/EfDm33
