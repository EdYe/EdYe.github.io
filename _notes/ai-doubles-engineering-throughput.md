---
title: '用 AI 讓工程團隊產能翻倍：Intercom 實戰紀錄'
date: 2026-05-17
image: /images/AI筆記/ai-doubles-engineering-throughput.jpeg
category: AI筆記
tags: [Claude Code, Skills飛輪, 工程產能, 平台複利, 脈絡注入]
description: 'Intercom 在不到一年內，透過將 Claude Code 視為「需要入職訓練的新工程師」而非通用工具，實現了工程產能倍增（2x）。核心策略：選定單一平台、全面接入生產系統、建立可重用技能資產庫。'
quote: '工程師的工作是往上移動，讓 Agent 接管你今天在做的事，你去做 Agent 做不了的事。'
action: '把最常重複執行的一項任務封裝成 Claude Code Skill，並在職位描述加入 AI 使用要求，公開表揚每一個 AI 工具化貢獻。'
source_has_timestamps: true
---
# 🤖 用 AI 讓工程團隊產能翻倍 — Intercom 實戰紀錄

**主講人：** Brian Scanlan，Intercom 資深首席工程師
**來源：** AI Engineer 大會，2026 年 5 月 15 日

***

## [核心摘要]

Intercom 在不到一年內，透過將 Claude Code 視為「需要入職訓練的新工程師」而非通用工具，實現了工程產能倍增（2x）。他們的核心策略是：**選定單一平台、全面接入生產系統、建立可重用技能（Skills）資產庫**，並將工程師的工作從「執行任務」升級為「定義問題」。

***

## [詳細重點整理]

### 1. 為什麼選擇「All-in 單一平台」[00:07]

過去 Intercom 讓工程師自由選擇 Copilot、Cursor、Augment 等工具，結果效果分散、難以累積優勢。 他們將此比喻為「多雲策略」——**分散即意味著放棄平台複利效益**。最終決策：全公司統一使用 **Claude Code**，2024 年 12 月決策、2025 年 1 月開始推行。

**關鍵概念：平台複利（Platform Compounding）**

***

### 2. 像新人入職一樣「訓練」AI [00:39]

Claude Code 被接入 Intercom 所有生產系統，包含：Rails monolith、React 慣例、測試標準、安全規則。 目標是讓 Claude 達到「能處理 Intercom 任何技術任務的資深工程師水準」。同時將所有 Claude Code 插件統一推送至數百台工程師筆電，避免版本破碎化。

**關鍵概念：脈絡注入（Context Injection）**

***

### 3. 給問題，不給任務 [00:57]

核心原則：**Give agents problems, not tasks**（給 Agent 問題，而非步驟指令）。 Brian 分享一個真實案例：某次安全事件，Snowflake 元數據被意外上傳至 GitHub，他只是把問題描述給 Claude，Claude 自動找到對應的安全政策 Skill、下載文件、完成分析、提供下一步——**2 分鐘完成原本需要 20 分鐘的工作**。

**關鍵概念：問題導向代理（Problem-Oriented Agent）**

***

### 4. 技能（Skills）資產庫的建設邏輯 [01:03]

Skills 是 Intercom 的核心資產：小型、高品質、可測試、持久耐用的作業封裝單元。 他們使用歷史程式碼、事件記錄進行**回溯測試（backtesting）**，以確保 Skills 品質。所有 Claude 的會話逐字稿也被導入 S3，用於數據挖掘與 Skills 效果評估，形成持續改善的飛輪。

**關鍵概念：技能飛輪（Skills Flywheel）**

***

### 5. 組織變革的執行方式 [00:23]

Intercom 更新了所有職位描述：**「不採用 AI，就是未達預期」，二元標準，無灰色地帶**。 同時設立專職 2x 團隊（持續擴編），透過 Slack 自動化頻道公開表揚每一個貢獻 Skills 的行為。定期舉辦 Hackathon 和 AI 沉浸日帶動文化轉型。

**關鍵概念：執行動能管理（Change Momentum Management）**

***

## [技術/數據對比]

| 指標 | 成果 |
|---|---|
| PR 產出（Pull Request throughput）| **倍增（2x）**，達成時間不到 1 年  |
| 自動審核核准率 | **17.6%** 的 PR 由 Agent 自動審核通過  |
| 合規認證 | 通過 **SOC 2、ISO 27001、HIPAA**，無需人工介入審核流程  |
| 缺陷（Bug）處理速度 | 關閉速度創歷史新高，部分團隊實現「缺陷清零」  |
| 程式碼品質 | 與 **Stanford 研究團隊合作**驗證，品質指標持續上升  |
| CI 基礎設施 | 因 PR 量暴增導致 **CI 系統一度崩潰**，被迫緊急擴容  |

***

## [結論與行動建議]

**啟發金句：**
> **「工程師的工作是往上移動，讓 Agent 接管你今天在做的事，你去做 Agent 做不了的事。」** 

**核心法則：P-S-C 法則**
- **Platform（平台）**：選定一個，All-in，不分散
- **Skills（技能）**：將知識封裝成高品質、可重用的 Skill
- **Context（脈絡）**：把公司知識全部餵給 Agent，讓它真正「懂你的系統」

**生活實踐建議：**
- **下週就做**：把你最常重複執行的一項任務（如：跑測試、寫PR描述、查安全政策）封裝成一個 Claude Code Skill
- **思維轉換**：遇到問題時，第一直覺改為「把問題描述給 Agent」，觀察它能否自己找到解法
- **組織層面**：若你是 PM 或 Tech Lead，考慮在職位描述中加入 AI 使用要求，並公開表揚每一個 AI 工具化貢獻 

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/4_VQBbs2iQA?si=YU6EOkgycJ47djid
- 🐦 主講人 Twitter：https://x.com/brian_scanlan
- 💼 主講人 LinkedIn：https://www.linkedin.com/in/scanlanb/
