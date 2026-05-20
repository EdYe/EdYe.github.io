---
title: 'Don''t Build Slop：AI Agent 四級成熟度框架'
date: 2026-05-20
image: /images/AI筆記/dont-build-slop-ai-agent-maturity-framework.jpeg
category: AI筆記
tags: [成熟度框架, 五條鐵律, Kanban, 雲端部署, 系統提示精簡]
description: '這場演講的核心貢獻在於為 AI Agent 建構者提供一套反「質量低劣」（Slop）的方法論。Ara Khan 將 Agent 開發拆分為四個成熟度等級，並提出'
quote: 'Frontier 模型如此強大，你能做的最好的事就是讓開——每一條你加進去的指令，都在賭你沒有讓它變更糟。'
action: '系統提示往少寫，用 Kanban 管理 Agent 工作流，驗證後直上雲端'
source_has_timestamps: true
---

# Don't Build Slop：AI Agent 四級成熟度框架

**主講人：** Ara Khan（Cline）｜**來源：** AI Engineer Conference，2026年5月19日

***

## [核心摘要]

這場演講的核心貢獻在於為 AI Agent 建構者提供一套反「質量低劣」（Slop）的方法論。Ara Khan 將 Agent 開發拆分為四個成熟度等級，並提出五條鐵律，幫助開發者從快速驗證走到雲端生產規模。核心洞察是：**Frontier 模型越強，系統提示應越短**，過多指令反而導致「感官超載」，讓模型表現退化。

***

## [詳細重點整理]

### 1. 四級 Agent 成熟度框架 [00:34]

Ara 將 Agent 開發的旅程分為四個清晰階段 ：

| 等級 | 名稱 | 核心行動 | 適用場景 |
|------|------|----------|----------|
| Level 1 | **框架原型** | 使用 LangChain、LangGraph 等框架 | 30分鐘快速驗證 PMF |
| Level 2 | **自建 Agent** | 從零實作，遵守五條鐵律 | 需要客製化、準備上線 |
| Level 3 | **UX 工作流** | Kanban 看板管理多個並行 Agent | 推理綁定（Inference-bound）場景 |
| Level 4 | **雲端部署** | Agent 跑在雲端，規模化至百萬任務 | 企業級多人協作 |

**關鍵概念：推理綁定（Inference-Bound）**——指 Agent 執行需 8~10 分鐘，期間人閒置，驅動並行多 Agent 的需求。

***

### 2. Level 2：自建 Agent 的五條鐵律 [02:55]

**Rule 1：每個 Agent 都是狀態機 [02:74]**
所有 Agent 的本質都是一個帶有條件的遞迴 while loop，無論是 Cursor 還是 Codex 都一樣。能在腦中視覺化狀態機，建構 Agent 就能更清晰。

**Rule 2：每新增一個功能都在冒險讓 Agent 變差 [03:57]**
GPT-5.3 的系統提示僅為 GPT-5 的 1/3 大小。Frontier 模型越強，越需要「讓開讓它跑」——長提示造成感官超載，反而降低效能。**關鍵概念：提示精簡原則（Prompt Pruning）**。

**Rule 3：讓 Agent 成為偽強化學習管線的一部分 [04:40]**
提供完善的 CLI 介面與 CI/CD，讓其他編碼 Agent 能輕鬆建構、測試、迭代你的 Agent，形成「Agent 開發 Agent」的 meta 迴路。

**Rule 4：不要建構 Slop（垃圾代碼）[05:21]**
架構設計必須由人類審慎規劃，不能讓模型任意生成。即使不親手寫每一行，也必須花時間閱讀程式碼，確保架構的合理性。

**Rule 5：Frontier Labs 的 API 在試圖鎖定你 [05:82]**
新模型（如 Opus 4.6、Gemini 1.5 Pro）的推理軌跡（Reasoning Traces）需要以精確格式發送，否則效能靜默降級，開發者完全無從察覺。**關鍵概念：推理軌跡（Reasoning Traces）格式對齊**。

***

### 3. Level 3：Kanban 是最佳 UX 形態 [06:61]

Ara 在 2026 年 3 月 26 日公開預測 Kanban 是管理 Agent 的最佳介面，結果 Claude Code 在本場演講的前十小時發布了同樣的設計。Kanban 讓開發者轉型為「工程經理（Engineering Manager）」，把多個並行 Agent 當作 IC 工程師來調度——查看高層進度、設定依賴關係、掌控工作流。

***

### 4. Level 4：雲端 Agent 的規模化優勢 [08:37]

雲端 Agent 可以在手機發出一個指令後，獨立執行長達 50~60 分鐘的複合任務（包含 UI 點擊、設定變更、終端測試），完成後直接發 PR。核心優勢是每個 Agent 有隔離的獨立機器環境，且允許企業內上千人共享同一套標準化設定。

***

## [結論與行動建議]

**啟發金句：**
> **「Frontier 模型如此強大，你能做的最好的事就是讓開——每一條你加進去的指令，都在賭你沒有讓它變更糟。」**

**具體行動建議（S-K-C 法則）：**
- **S（Simple Prompt）**：系統提示永遠往少寫、往精簡
- **K（Kanban First）**：用 Kanban 看板管理你的 Agent 工作流
- **C（Cloud Scale）**：驗證後直上雲端，拒絕本地依賴的複雜性

**生活實踐建議：**
- **今天就做**：在你的 AI 編碼工作中，刪掉系統提示裡覺得「可能沒用但保險」的段落，觀察效果是否提升
- **下週嘗試**：用 Linear 或任何 Kanban 工具，同時管理 2~3 個並行 Coding Agent，體驗工程管理者的視角
- **中期目標**：為你的核心 Agent 建立完善的 CLI + CI/CD，讓它可以被其他 Agent 測試與迭代

***

## [參考連結]

- 🎥 原始影片：https://youtu.be/yUmS-F9IX90
- 🐦 主講人 Twitter：https://x.com/arafatkatze
- 💼 主講人 LinkedIn：https://www.linkedin.com/in/arafatkatze/
