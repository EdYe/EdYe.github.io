---
title: 'Claude Code Workflow：以程式碼取代 LLM 擔任 Orchestrator'
date: 2026-05-28
image: /images/AI筆記/claude-code-workflow-orchestration.jpeg
category: AI筆記
tags: [多智能體編排, Workflow工具, Token預算, 確定性編排, Claude Code]
description: 'Anthropic 悄悄在 Claude Code 中新增了 Workflow 工具，實現「確定性多智能體編排」。過去的 Sub-Agent 架構讓主 Orchestrator 的 Context Window 因反覆傳遞中間結果而膨脹'
quote: '讓程式碼來編排，而不是讓模型來記憶。'
action: '設定 CLAUDE_WORKFLOWS=true 並翻查舊 Session，找出適合轉換為 Workflow 的重複性任務'
source_has_timestamps: true
---
# Anthropic Just Dropped the Feature Everyone Needed

**頻道：** Ray Amjad｜**發布日期：** 2026年5月22日｜**片長：** 16分16秒

***

## [核心摘要]

Anthropic 悄悄在 Claude Code 中新增了 **Workflow 工具**，實現「確定性多智能體編排」。過去的 Sub-Agent 架構讓主 Orchestrator 的 Context Window 因反覆傳遞中間結果而膨脹，導致效能下降且 Token 浪費嚴重。新的 Workflow 機制以 **JavaScript 程式碼取代 LLM 擔任 Orchestrator**，讓 Sub-Agent 之間的結果可以直接傳遞，徹底解決 Token 稅與「越跑越笨」的問題。

***

## [詳細重點整理]

**1. 舊架構的三大痛點 [01:21]**

舊的 Sub-Agent 工作流讓主 Session 充當 Orchestrator，每個 Sub-Agent 的結果都會回流到主 Context Window 再傳給下一個 Agent。

- **Token 稅**：中間結果在主 Session 與 Sub-Agent 之間反覆來回，浪費大量 Token
- **能見度差**：執行過程只是一道難以追蹤的滾動文字牆
- **Orchestrator 退化**：Context Window 越塞越滿，模型開始「遺忘」，遇到條件判斷時尤其容易出錯

> **關鍵概念：上下文污染（Context Contamination）**——Orchestrator 因承載過多中間狀態而喪失判斷精確度。

***

**2. Workflow 工具的核心機制 [03:18]**

Claude Code 新增 `/workflows` 指令，對應專案 `.claude/workflows/` 資料夾中的 `.js` 檔案。

- Workflow 結構由 **meta（名稱/描述）、phases（階段）、schemas（回傳格式）、arguments（輸入參數）** 四個區塊組成
- 以 JavaScript 程式碼擔任 Orchestrator，Sub-Agent 的結果直接透過程式碼傳遞，**永遠不進入主 Context Window**
- 可混合使用：`agent`（單一 Sub-Agent）、`parallel`（批次並行）、`pipeline`（流水線，完成即觸發下一階段）

> **關鍵概念：確定性編排（Deterministic Orchestration）**——以程式碼邏輯取代 LLM 推理，確保分支、迴圈、條件判斷的可靠性。

***

**3. Workflow 實際操作示範 [07:14]**

三個真實案例展示了 Workflow 的應用場景：

| 案例 | 說明 | 技術亮點 |
|------|------|----------|
| **Triage Sentry** | 拉取未解決問題 → 篩選影響 >20 名用戶的 Bug → 自動修復並驗證 | Schema 回傳結構化結果，JavaScript 過濾邏輯 |
| **Dead Code Sweep** | 迴圈掃描並移除無用程式碼，最多執行 8 輪 | `while` 迴圈 + 提前終止條件 |
| **Personalized Outreach** | 載入 CSV 名單 → 並行研究每位潛在客戶 → 撰寫個人化郵件 | Pipeline 讓研究完成即立刻進入撰寫階段，不等全部完成 |

***

**4. Workflow 工具箱總覽 [14:24]**

- **agent**：每次生成一個全新的 Sub-Agent
- **parallel**：批次並行執行多個 Agent，等全部完成後繼續
- **pipeline**：流水線，完成一項即推進下一階段（避免等待）
- **schema**：強制結構化回傳格式，便於後續程式碼引用
- **phase log**：即時顯示各 Agent 執行狀態
- **arguments**：可從外部傳入參數，增加靈活性
- **budgets**：設定 Token 上限，防止工作流失控（例：Token 剩餘 >50,000 才繼續）

> **關鍵概念：Token Budget 護欄**——以程式碼層面的預算控制取代模型層面的自我節制。

***

**5. 何時該用 Workflow？ [15:17]**

- ✅ **需要重複執行**的流程（每天都會跑）
- ✅ **需要 Fan-Out**：根據條件/迴圈動態產生多個 Agent
- ✅ **任務夠長、可能中途失敗**：Workflow 支援自動重試（每個 Sub-Agent 最多重試 3 次）
- ❌ **一次性任務**：直接在對話中操作即可，不必額外建立 Workflow

***

## [結論與行動建議]

**啟發金句：**
> **「讓程式碼來編排，而不是讓模型來記憶。」**

**核心法則——P-S-B 法則：**
- **P（Pipeline/Parallel）**：選對並行策略，最大化吞吐量
- **S（Schema）**：用結構化回傳取代自由文字，確保 Agent 間的資料可靠傳遞
- **B（Budget）**：設定 Token 預算護欄，防止工作流失控

**生活實踐建議：**
1. **立即啟用**：設定環境變數 `CLAUDE_WORKFLOWS=true`，執行 `claude` 後確認 `/workflows` 指令出現
2. **翻查舊 Session**：請 Claude Code 分析你過去的工作記錄，找出適合轉換為 Workflow 的重複性任務（如每日 Code Review、Issue 修復流程）
3. **下載 Workflow Creator Skill**：從 [作者 GitHub](https://github.com/ray-amjad/claude-code-workflow-creator) 取得，讓 Claude Code 自動生成 Workflow 檔案

***

## [參考連結]

- 📺 原始影片：https://youtu.be/c0gVowvMR-g
- 🛠️ Workflow Creator：https://github.com/ray-amjad/claude-code-workflow-creator
