---
title: 'Claude Code隱藏功能與優化'
date: 2026-04-03
image: /images/AI筆記/claude-code-hidden-features-optimization.jpeg
category: AI筆記
tags: [Claude Code, 記憶優化, 功能旗標, MCP, 多重Agent]
description: '本影片深度解析了 Claude Code 中鮮為人知的「隱藏功能」與進階設定，旨在解決開發者在使用 AI 代理時常遇到的上下文記憶衰退、介面閃爍及工作流受限等痛點'
quote: '讓 AI 在「做夢」中進化，將混亂的資訊碎片轉化為精準的智慧資產。'
action: '開啟 autodream 清理上下文，設定 CLAUDE_CODE_NO_FLICKER=1 穩定介面，根據任務類型切換輸出風格。'
source_has_timestamps: true
---

## 核心摘要

本影片深度解析了 Claude Code 中鮮為人知的「隱藏功能」與進階設定，旨在解決開發者在使用 AI 代理時常遇到的上下文記憶衰退、介面閃爍及工作流受限等痛點。透過啟發特定的功能旗標（Feature Flags），使用者能大幅提升 Claude Code 的執行效能與操作穩定性，將其轉化為更強大的自動化編程助手。

-----

## 詳細重點整理

### 1\. 記憶強化與「做夢」模式 [/dream] [[01:02](http://www.youtube.com/watch?v=AL_7VqZEqD4&t=62)]

  * **功能說明**：引入名為 `/dream`（或 `autodream`）的功能，模擬人類的 REM 睡眠。它能自動整合不同對話間的記憶，刪除陳舊無效的筆記，保留關鍵洞察。
  * **關鍵概念**：**記憶優化**。這解決了 AI 隨著對話變長而變得混亂的問題，讓記憶「越用越精準」而非越用越笨。

### 2\. 解決介面閃爍問題 [no flicker mode] [[03:11](http://www.youtube.com/watch?v=AL_7VqZEqD4&t=191)]

  * **功能說明**：透過在設定檔中將 `CLAUDE_CODE_NO_FLICKER` 設為 `1`，啟用實驗性的渲染器，解決終端機 UI 跳動與組件閃爍的問題。
  * **關鍵概念**：**穩定視埠渲染**。此模式還能開啟滑鼠點擊支援，讓終端機操作更接近現代編輯器，極大提升視覺舒適度。

### 3\. 多重 Agent 協作：Codeex 插件整合 [[04:34](http://www.youtube.com/watch?v=AL_7VqZEqD4&t=274)]

  * **功能說明**：整合 OpenAI 團隊釋出的 Codeex 插件，讓 Claude Code 內建「第二個大腦」。這不僅能提供不同的代碼審核視角，還能有效繞過 Anthropic 的速率限制（Rate Limits）。
  * **關鍵概念**：**雙重 Agent 校驗**。適合用於高風險的重構或遷移任務，確保代碼品質。

### 4\. MCP 電腦使用權限與遠端控制 [[05:40](http://www.youtube.com/watch?v=AL_7VqZEqD4&t=340)]

  * **功能說明**：透過 MCP（Model Context Protocol）讓 Claude 具備操作電腦 UI 的能力，可直接開啟 App、點擊界面進行除錯。同時支援 `/teleport`（跨設備接續會話）與 `/remote-control`（手機/平板控制本地會話）。
  * **關鍵概念**：**跨維度操作**。將 AI 的能力從純文字對話擴展到實際的作業系統操作。

### 5\. 動態角色切換：輸出風格設定 [/output-style] [[08:03](http://www.youtube.com/watch?v=AL_7VqZEqD4&t=483)]

  * **功能說明**：提供三種輸出模式：`Default`（高效工程）、`Explanatory`（教學詳解）、`Learning`（引導式編程）。
  * **關鍵概念**：**教學相長**。`Learning` 模式會引導使用者親手寫出關鍵部分，而非僅僅是接受 AI 生成的代碼差異（Diffs）。

-----

## 結論與行動建議

  * **啟發金句**：「讓 AI 在『做夢』中進化，將混亂的資訊碎片轉化為精準的智慧資產。」
  * **具體行動建議：3-S 優化法則**
    1.  **S**etup Dream：進入 Claude 實例輸入 `/memory` 並開啟 `autodream`，或手動下令「Consolidate my memory」來清理上下文。
    2.  **S**tabilize UI：在環境變數中加入 `CLAUDE_CODE_NO_FLICKER=1`，建立穩定的開發視窗。
    3.  **S**tyle Selection：根據任務類型切換風格，學習新項目用 `Learning` 模式，趕進度用 `Default` 模式。
  * **生活實踐建議**：
      * **建立環境檢查清單**：每次更新 Claude Code 後，檢查設定檔中的功能旗標是否失效。
      * **工具深度探索**：養成定期查看官方 GitHub 系統提示詞（System Prompts）的習慣，尋找像 `/dream` 這樣尚未正式文件化的指令，保持技術領先。

影片連結：[https://youtu.be/AL\_7VqZEqD4](https://www.google.com/search?q=https://youtu.be/AL_7VqZEqD4%3Fsi%3DReJ6r1B6ZKocYza3_)
