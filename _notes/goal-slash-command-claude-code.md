---
title: 'Claude Code /goal 功能：設定目標讓 AI Agent 自主運行數小時'
date: 2026-05-14
image: /images/AI筆記/goal-slash-command-claude-code.jpeg
category: AI筆記
tags: [/goal功能, Definition of Done, Token效率, Claude Code, AI Agent]
description: '`/goal` 功能徹底改變 AI Agent 的操作模式——過去開發者需要逐 prompt 引導 Agent，現在只需設定一個「完成條件（Definition of Done）」，Agent 就能自主運行數小時甚至數天，直到達成目標為止。'
quote: '不要設定任務，要設定目標；Agent 的工作不是執行指令，而是達成條件。'
action: '每次啟動 /goal 時，撰寫精確的 Definition of Done + Acceptance Criteria，這是決定 Agent 能否一次到位的核心變數。'
source_has_timestamps: true
---
# 🤖 AI Agent 的未來已來臨：Claude Code 與 Codex 的 /goal 功能深解

## [核心摘要]

**`/goal` 功能**徹底改變 AI Agent 的操作模式——過去開發者需要逐 prompt 引導 Agent，現在只需設定一個「完成條件（Definition of Done）」，Agent 就能自主運行數小時甚至數天，直到達成目標為止。這解決了長時間任務需要人工監督的核心痛點，讓真正的「無人值守自動化」成為可能。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

***

## [詳細重點整理]

### 1. /goal 功能是什麼？[00:00]

**`/goal`（目標驅動迴圈）** 是 Claude Code 與 OpenAI Codex 同步推出的新功能。使用者輸入 `/goal` 後設定完成條件，Agent 會持續工作直到該條件被滿足。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

- 此功能最初由 **Codex 在兩週前率先推出**，隨後 Anthropic 跟進實作
- 技術機制：每完成一個 turn，Claude Code 會調用輕量級的 **Haiku 模型**來評估「Definition of Done」是否達成；若未達成，則繼續下一輪迴圈
- 社群已有使用者分享跑了 **45 小時、甚至 5 天連續 session** 的真實案例
- 核心概念：**RALPH Loop**（Repeat And Loop until Passed a Human check）——此功能本質上是將 RALPH Loop 直接內建進 coding harness 中

***

### 2. Level 1：簡單範例示範 [01:54]

以「建立 Chrome 擴充功能，實現 Slack 式 emoji 快捷鍵」為例，展示 /goal 的基本用法。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

- 輸入 `/goal` + 任務描述 + **明確的 Definition of Done**（例：Chrome 擴充功能無 manifest 錯誤且快捷鍵正常運作）
- 對於簡單任務，/goal 的主要價值在於**自我驗證**：Agent 完成後會自動核查輸出是否符合條件
- 關鍵概念：**Definition of Done（DoD）** — 越具體的完成條件，越能有效引導 Agent 自我修正

***

### 3. Level 2：批次創作應用（Token 效率最大化）[04:04]

在 **每週 token 配額即將重置前**，善用剩餘 token 批次創建內容，是 /goal 的高價值應用場景。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

- 實際案例：Claude Code 讀取四支 YouTube 影片逐字稿，套用自訂 newsletter skill，**一次性生成四篇 Substack 電子報草稿**（耗時約 8 分鐘）
- 可輕鬆擴展至 30～40 篇，讓 Agent 不間斷工作直到 token 耗盡
- 工具推薦：搭配 **`plan-for-goal` skill**，自動產生含有 Stack、Scope、DoD、Acceptance Criteria 的標準化 markdown 計畫書
- 關鍵概念：**Token 效率最大化** — 利用 /goal 將閒置 token 轉化為可用的內容資產

***

### 4. Level 3：Codex vs. Claude Code 深度對比 [06:47]

以「建造一個 Game of Thrones 主題、AI 公司皮膚的 Settlers of Catan 遊戲（32-bit 像素風）」作為壓力測試，同步比較兩個平台的輸出。 [youtube](https://www.youtube.com/?app=desktop&hl=zh-tw)

| 比較維度 | Claude Code (Sonnet 4.7) | Codex (GPT-5.5) |
|---|---|---|
| **完成時間** | ✅ 13 分 5 秒 | ❌ 33 分鐘 |
| **視覺品質** | 基本文字符號，視覺較弱 | ✅ GPT Image 2 自動生成美術資源 |
| **遊戲功能性** | ✅ 核心玩法完整可運行 | 功能邏輯略遜，部分 UX 不完整 |
| **圖像生成** | ❌ 需外接 OpenAI / Imagen API | ✅ 原生整合 GPT Image 2 |
| **速度優勢** | 快 2.5 倍 | 慢但美觀 |

> **結論**：若注重速度與邏輯，Claude Code 勝出；若需視覺豐富的遊戲或媒體產品，Codex 因原生整合圖像生成更有優勢。

***

## [結論與行動建議]

**啟發金句：**
> **「不要設定任務，要設定目標；Agent 的工作不是執行指令，而是達成條件。」**

**具體行動建議（DoD 法則）：**
每次啟動 /goal 時，務必花時間撰寫精確的 **Definition of Done + Acceptance Criteria**，這是決定 Agent 能否一次到位的核心變數。垃圾進，垃圾出——條件越模糊，迴圈越失控。

**生活實踐建議：**
- **週五下班前**：檢查剩餘 token 配額，將下週需要批次處理的內容（報告、社群貼文、電子報）透過 /goal 一次性生成
- **開發新功能前**：先用 `plan-for-goal` skill 生成標準計畫書，讓 AI 有明確的驗收標準
- **跨平台策略**：文字邏輯密集任務用 Claude Code（速度快）；需要視覺資產的創意項目用 Codex（有圖像生成）

***

## [參考連結]

- 📺 原始影片：https://youtu.be/aEDq1bBynOg?si=SUrtLWjRs8QR4PG1
- 🆓 plan-for-goal skill 免費下載：https://www.skool.com/robonuggets-free（搜尋 n55）
- 🤖 RUBRIC AI Agent 指揮中心：https://www.getrubric.app/
