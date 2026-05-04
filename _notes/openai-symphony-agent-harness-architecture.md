---
title: 'OpenAI Symphony：AI Agent 的 Harness 工程架構全解析'
date: 2026-05-04
image: /images/AI筆記/openai-symphony-agent-harness-architecture.jpeg
category: AI筆記
tags: [Agent Harness, Symphony, Outer Harness, 感測器回饋, 平行Agent]
description: 'OpenAI 開源了 Symphony，一個專為擴展自動化程式開發 Agent 設計的編排規格。當 AI Coding Agent 的效率超越人類時，工程師的工作重心從寫程式轉移至為 Agent 打造可靠的 Harness 防護架構'
quote: '模型是 CPU，但 Harness 才是真正發生工程的地方。'
action: '在現有 AI 工作流中加入 Linter / Schema 驗證作為 Computational Sensor，將工程重點從 Prompt 優化轉移至 Harness 架構設計。'
source_has_timestamps: true
---
# OpenAI 發布 Symphony：Agent Harness 工程的核心架構解析

**影片來源：** The AI Automators｜2026年4月30日｜片長 10:48 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [核心摘要]

OpenAI 開源了 **Symphony**，一個專為擴展自動化程式開發 Agent 設計的編排規格（Orchestration Spec）。影片核心論點是：**當 AI Coding Agent 的效率超越人類時，人類成為最大瓶頸**，因此工程師的工作重心已從「寫程式」轉移至「為 Agent 打造可靠的 Harness（防護架構）」。這支影片解構了 Inner/Outer Harness、Guides/Sensors 等關鍵架構思維，並說明如何將這些概念應用於自行建構的 AI 應用系統中。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [詳細重點整理]

**1. OpenAI Symphony 是什麼 [00:47]**

Symphony 是一個 Agent 編排規格，以 Linear（議題追蹤工具）作為人機介面。每一張 Ticket 會觸發一個對應的 Coding Agent 在獨立工作區持續執行，直到任務完成。本質上這是一個**狀態機流程（State Machine Flow）**，讓非技術人員也能參與高層次的 AI 工作流程管理。OpenAI 內部測試結果顯示，某些團隊的 Pull Request 合併數量提升了 500%。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：狀態機流程（State Machine Flow）**

***

**2. 什麼是 Agent Harness [02:35]**

**Agent Harness** 是包裹在 AI 模型外層的整體基礎架構。AI 模型（LLM）如同電腦的 CPU，只負責推理與輸出文字；而記憶管理、Sub-Agent 控制、工具呼叫執行等所有延伸功能，全部由 Harness 的程式碼負責。Harness 的定義極廣，理解其層次結構是構建可靠系統的關鍵。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：AI 模型即 CPU（LLM as CPU）**

***

**3. Inner Harness vs. Outer Harness [04:20]**

- **Inner Harness**：內建於 Claude Code、Cursor、Codex 等工具中，開箱即支援 Sub-Agent 管理、沙盒程式執行、工具權限控管等功能。
- **Outer Harness**：建立在 Coding Agent 外層的真實程式碼，能以**決定性方式（Deterministically）** 控制 Agent 的生命週期，例如強制終止 Session、清除上下文、從磁碟讀取任務狀態再重新注入。
- 代表工具：Ralph Wiggum Loop、Archon、GasTown 皆屬於 Outer Harness 的實作範例。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：決定性外層控制（Deterministic Outer Harness）**

***

**4. Guides（引導器）vs. Sensors（感測器）[05:24]**

| 類型 | 功能 | 範例 |
|------|------|------|
| **Guides（引導器）** | 在 Agent 執行前改善首次嘗試品質 | `AGENTS.md` 文件、Playbook、程式範例、Skill 定義 |
| **Computational Sensors（運算感測器）** | 執行後的決定性回饋，不耗用 AI Token | Linter、型別檢查（Type Check）、Schema 驗證 |
| **Inferential Sensors（推論感測器）** | 以 AI 評估 AI 輸出品質的回饋機制 | LLM as a Judge（另一個模型審查生成結果） |

影片特別強調，**Computational Sensors 是目前 AI 建構者最嚴重低估和低用的工具**。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：感測器回饋迴路（Sensor Feedback Loop）**

***

**5. AI 應用中的 Harness 層次 [07:34]**

在自行開發的 AI 應用中，Harness 同樣可以分層套用。以「合約審查系統」為例：Outer Harness 疊加在 Agentic 系統核心功能之上，提供自動化的文件計算驗證（不耗 AI Token），以及 LLM as a Judge 的推論檢查。整個 Harness 光譜從「高度決定性（如特定工作流合約審查）」延伸至「高度機率性（如 Deep Research）」。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：決定性 vs. 機率性光譜（Deterministic-Probabilistic Spectrum）**

***

**6. 編排器層（Orchestrator Layer）與 Symphony [08:37]**

當 Outer Harness 持續疊加時，會形成更上層的**編排器與排程器層（Orchestrator & Scheduler Layer）**，這正是 Symphony 所定位的位置。平行 Agent 最大的兩個挑戰為：**(1) Agent 之間的衝突（Clashing）** 與 **(2) 人機介入點的設計（Human-in-the-Loop Design)**。Symphony 以 Linear 作為人機介面，解決了「何時該讓人類介入，而非微管理每個 Session」的核心問題。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：編排器層（Orchestrator Layer）**

***

## [技術/數據對比]

| 架構層 | 代表工具 | 控制方式 | 適用場景 |
|--------|----------|----------|----------|
| Inner Harness | Claude Code、Cursor、Codex | 內建功能（Sub-Agent、Tool、Hook） | 單一 Agent 工作 |
| Outer Harness | Archon、Ralph Loop、GasTown | 決定性程式碼控制 Agent 生命週期 | 單/多 Agent 自動化迴圈 |
| Orchestrator Layer | OpenAI Symphony | Ticket 驅動、狀態機流程、Linear 介面 | 大規模平行 Agent 編排 |

 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [結論與行動建議]

**🔥 啟發金句：**
> **「模型是 CPU，但 Harness 才是真正發生工程的地方。」**（The model is the CPU, but the harness is where the real engineering happens.） [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**⚡ 核心法則：G-S-O 三層法則**
- **G（Guides）**：先餵飽 Agent，讓它第一次就做對
- **S（Sensors）**：用計算驗證＋LLM 評審建立回饋迴路
- **O（Orchestrate）**：以編排器層管理平行 Agent 與人機介入點

**🛠 生活實踐建議：**
- **立即行動**：在現有 AI 工作流中加入 Linter / Schema 驗證作為 Computational Sensor，這是成本最低、效益最高的 Outer Harness 起點。
- **中期建構**：參考 Symphony 的 GitHub Spec，讓自己的 Coding Agent 幫你用偏好的語言生成一套 Orchestration 系統，再對接 Linear 或 GitHub Issues 作為人機介面。
- **長期思維**：不要再把 AI 工程的重點放在「如何 Prompt 更好」，而要轉移至「如何設計更可靠的 Harness 架構」。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [參考連結]

- 📺 原始影片：https://youtu.be/5p6h23Md4Zw
- 🔗 Symphony GitHub Repo：https://github.com/openai/symphony
- 📄 OpenAI Harness Engineering 文章：https://openai.com/index/harness-engineering/
- 📄 Brigetta Berkeler Harness Engineering 文章：https://martinfowler.com/articles/harness-engineering.html
