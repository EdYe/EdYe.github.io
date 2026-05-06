---
title: 'Boris Cherny：程式碼撰寫已被 AI 徹底解決，接下來是民主化'
date: 2026-05-06
image: /images/AI筆記/coding-is-solved-boris-cherny-sequoia-2026.jpeg
category: AI筆記
tags: [Claude Code, Loop代理, 跨學科通才, 軟體民主化, 產品過剩]
description: 'Anthropic Claude Code 的創造者 Boris Cherny，在 Sequoia AI Ascent 2026 大會上宣告：程式碼撰寫已被 AI 徹底解決。他每天靠手機管理數百個 AI Agent、每日提'
quote: '最有能力寫出最好的會計軟體的人，是一位優秀的會計師，而不是工程師——因為領域知識才是難的部分，寫程式只是容易的部分。'
action: '立刻在工作流程中實驗一個「永久循環代理」，把每天手動重複的事交給 AI 自動循環執行，你的角色轉為需求定義與結果驗證。'
source_has_timestamps: true
---
# 「編程已被解決，接下來呢？」— Boris Cherny × Sequoia AI Ascent 2026
**[核心摘要]**

Anthropic Claude Code 的創造者 Boris Cherny，在 Sequoia AI Ascent 2026 大會上宣告：對他而言，**程式碼撰寫已被 AI 徹底解決**。他每天靠手機管理數百個 AI Agent、每日提交數十個 PR，並預言未來幾年軟體開發將像印刷術一樣民主化——領域專家（如會計師）將比工程師更能寫出好的行業軟體，AI 帶來的是「新文藝復興」而非程式員的末日。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

**[詳細重點整理]**

**1. Claude Code 的誕生起源 [02:39]**

Claude Code 是在 Anthropic 內部孵化器 Anthropic Labs 中「意外」誕生的，由 Boris 和少數幾位成員打造，同期產品還包括 MCP 與桌面應用程式。早期六個月幾乎毫無用武之地，真正的爆炸性成長始於 Opus 4 模型發佈之後，此後每一代模型發佈都帶來新的增長拐點。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：產品過剩（Product Overhang）** — 模型能力已超前於現有產品形態，存在尚未被釋放的巨大潛能缺口。

**2. 「編程已被解決」的定義 [05:07]**

Boris 在 2025 年 10–11 月起，就將 100% 的程式碼交給 AI 撰寫。他的標準是：對於他個人處理的代碼庫（TypeScript + React 技術棧），AI 已能完全勝任。但他也坦承，龐大且複雜的舊系統代碼庫，以及模型訓練覆蓋率低的語言，仍是當前的盲區。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：On Distribution** — 選用模型訓練資料中高頻出現的語言和框架，以最大化 AI 輸出品質。

**3. Boris 個人極端工作流程 [06:50]**

Boris 目前的工作方式幾乎完全依賴手機上的 Claude app，同時維持 5–10 個工作 session，每個 session 下有多個 Agent 並行。他大量使用 `/loop` 功能——本質是讓 Claude 用 cron 排程週期性任務，例如：

- 自動監控 PR 狀態、修復 CI 失敗、自動 Rebase
- 每 30 分鐘從 Twitter 抓取用戶反饋並進行分類
- 夜間啟動數千個 Agent 執行深度工作 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：Loop（循環代理）** — AI Agent 透過 cron 排程自我觸發、持續執行的工作模式，是未來人機協作的核心範式。

**4. 未來團隊型態與跨學科通才 [08:51]**

未來的頂尖人才不再是狹義工程師，而是**跨學科通才**（Cross-disciplinary Generalist）。Claude Code 團隊已是範本：產品經理、設計師、數據科學家、財務人員，全員都在寫程式碼。專業知識成為護城河，而「會寫程式」降格為基礎技能。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：跨學科通才（Cross-disciplinary Generalist）** — AI 加持下，個人得以橫跨工程、設計、產品、數據等多個專業領域同時作業。

**5. SaaS 末日？商業模式的重組 [10:26]**

Boris 引用 Hamilton Helmer《Seven Powers》理論分析：AI 時代**減弱**的護城河包括「轉換成本」與「流程壁壘」；**仍然有效**的是網絡效應、規模經濟、稀缺資源。他認為未來 10 年創業公司數量將增長 10 倍，因為從零開始的新創可以原生擁抱 AI，而大企業須耗費巨大資源進行組織轉型。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：Seven Powers（七種護城河）** — 商業策略框架，用於評估 AI 時代下各類競爭優勢的存廢。

**6. 印刷術類比：軟體開發的民主化 [23:35 前後 Q&A]**

Boris 以 1400 年代印刷術為類比：印刷術發明前，歐洲只有 10% 人口識字；之後 50 年出版量超過前千年總和，書籍成本下降百倍，數百年後識字率升至 70%。他預言**軟體開發的民主化將比識字更快發生**，且最終最會寫某領域軟體的人，是該領域的專家（如會計師），而非工程師。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：軟體民主化（Software Democratization）** — 編程技能將從專業壁壘演變為全民基礎能力，如同今日人人會使用 Office。

***

**[技術/數據對比]**

| 指標 | 過去（2024 以前） | 現在（2026） |
|------|-----------------|------------|
| 主流 AI 編程範式 | Typeahead（Tab 補全，逐行完成）| Agent Loop（全自動、多代理並行）|
| Boris 每日 PR 數 | 個位數（手動撰寫） | 數十至 150 個（AI 全代勞）|
| Claude Code 用戶量 | 緩慢成長（PMF 前） | 指數成長（自 Opus 4 起每版翻倍）|
| 模型 vs 產品貢獻比 | 50/50 | 模型比例持續提升 |
| Anthropic 全公司手寫程式碼比例 | 多數手寫 | **零手寫**，含所有 SQL |

***

**[結論與行動建議]**

**啟發金句：**

> **「最有能力寫出最好的會計軟體的人，是一位優秀的會計師，而不是工程師——因為領域知識才是難的部分，寫程式只是容易的部分。」**

**具體行動建議（Loop-First 法則）：**

立刻在你的工作流程中實驗一個「永久循環代理」——找一件你每天都要手動重複做的事（如整理回饋、監控數據、追蹤任務進度），讓 AI 接管並自動循環執行。

**生活實踐建議：**

- **PM / 產品人：** 不等工程師，直接用 Claude Code 建立 MVP 原型，然後交給 AI 迭代，你的角色是需求與驗證，而非實作。
- **所有知識工作者：** 把「我懂的領域知識」視為最大資產，主動學習如何將領域問題轉化成 AI 可執行的指令，而非學習程式語法本身。
- **組織管理者：** 現在就開始將全團隊轉變為「人人寫 code」的文化，從最願意嘗試的成員開始試點，並記錄組織工作流程的 AI 轉型過程。

***

**[參考連結]**

- 原始影片：https://youtu.be/SlGRN8jh2RI?si=KI_GYEeummNmNsO2 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
