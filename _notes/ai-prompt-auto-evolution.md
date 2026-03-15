---
title: 'AI 提示詞自動進化：用 Auto Research 讓技能持續優化'
date: 2026-03-15
image: /images/AI筆記/ai-prompt-auto-evolution.jpg
category: AI筆記
tags: [提示詞工程, 自動化研究, 評估標準, 測試迴圈, Claude Code]
description: '這部影片介紹如何建立「自動化研究」系統，透過量化的評估標準 (Evals) 與重複測試迴圈，讓 Claude Code 技能學會自我修正與持續進化，將輸出準確率提升至近乎完美。'
quote: '隨著 AI 模型在未來幾年變得越來越聰明，這套持續累積的研究數據將成為你最有價值的資產。'
action: '為 AI 技能定義 3-5 個「是非題」形式的評分標準，設定自動化迴圈讓技能持續進化至準確率 95% 以上'
source_has_timestamps: true
---
這部影片由 Nick Saraev 製作，深入探討了如何利用 OpenAI 前創始成員 Andrej Karpathy 提出的 **「自動化研究 (Auto Research)」** 概念，結合 **Claude Code** 技能，讓 AI 的提示詞（Prompt）與輸出品質能夠「自行進化」與無限優化。

以下是為您整理的結構化筆記：

---

### 💡 核心摘要

這部影片介紹如何建立一套「自動化研究」系統，透過設定量化的評估標準 (Evals) 與重複測試迴圈，讓 Claude Code 技能學會自我修正與持續進化，將輸出準確率從一般水準提升至近乎完美的表現。

---

### 📘 詳細重點整理

#### 1. 自動化研究 (Auto Research) 的核心概念 [[00:32](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=32)]

* **來源：** 概念源自 Andrej Karpathy 的 GitHub 專案，旨在透過多個代理人 (Agents) 自主優化流程。
* **機器學習邏輯：** 傳統上用於模型訓練（如 nanoGPT），但 Nick 將其應用於「提示詞工程 (Prompt Engineering)」，讓 AI 自動改善其指令集（Skill.md）。
* **顯著成效：** 講者曾將此方法應用於網站速度優化，讓載入時間從 1100ms 降至 67ms，提升了 81.3% [[02:41](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=161)]。

#### 2. 自我進化系統的三大關鍵要素 [[03:41](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=221)]

* **客觀指標 (Objective Metric)：** 不能僅憑「感覺」，必須有具體的數據。例如網站載入毫秒數、冷郵件的回覆率，或是本影片中的「測試通過率」。
* **自動化測量工具 (Measurement Tool)：** 必須無須人工介入即可運行。講者建議編寫「測試套件 (Test Suite)」，讓 AI 按照標準操作流程逐一評估。
* **可變動的對象 (Something to Change)：** 在優化技能時，這個對象就是 **Markdown 格式的指令檔 (Prompt Instructions)**。

#### 3. 建立評估基準 (Evals) 的實戰技巧 [[05:31](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=331)]

* **處理 AI 的隨機性：** 提示詞輸出具有不確定性（Noise），因此需要讓系統重複執行多次（如 10 次），並觀察其眾數或中位數。
* **二進制標準 (Binary Answers)：** 建議評估標準應為簡單的「是」或「否」，避免使用 1-7 分的量表，因為變數過多會導致結果難以收斂 [[14:21](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=861)]。
* **避免過度限制：** 標準若過於僵化（如限定字數），AI 可能會為了「過關」而投機取巧，導致表面達標但實際品質下降 [[15:02](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=902)]。

#### 4. 以「流程圖生成技能」為例的優化步驟 [[07:01](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=421)]

* **設定四項指標：**
1. 文字是否清晰且語法正確？
2. 是否符合粉彩配色 (Pastel colors)？
3. 結構是否為線型（由左至右或上至下）？
4. 是否沒有多餘的編號（1, 2, 3...）？


* **運行流程：** 系統每 2 分鐘生成 10 張圖，通過另一位 Agent (如 Claude Sonnet Vision) 評分 [[13:13](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=793)]，若分數提高則保留該提示詞，反之則繼續變異修正。

---

### 🛠️ 結論與行動建議

**具體建議 (Step-by-step)：**

1. **複製框架：** 獲取 Andrej Karpathy 的 `auto-research` GitHub 倉庫概念。
2. **定義 Evals：** 為你的 AI 技能寫下 3-5 個「是非題」形式的評分標準。
3. **執行迴圈：** 在 Claude Code 中設定自動化腳本，讓它不斷生成、評分、修正指令，直到得分穩定在 95% 以上。

**金句啟發：**

> 「隨著 AI 模型在未來幾年變得越來越聰明，這套持續累積的研究數據（Research Data）將成為你最有價值的資產。你可以將這些優化過的邏輯交給未來的 GPT-6 或 Opus 5.0 繼續進化。」[[03:23](http://www.youtube.com/watch?v=qKU-e0x2EmE&t=203)]

---
