---
title: 'AI Agent 記憶四大類型：CoALA框架'
date: 2026-07-03
image: /images/影片筆記/ai-agent-memory-coala-framework.jpg
category: 影片筆記
tags: [工作記憶, 語意記憶, 程序記憶, 情節記憶, CoALA框架]
description: '影片指出一個生產級 AI Agent 的關鍵設計痛點：多數開發者只關注上下文窗口（working memory），卻忽略了知識、技能與經驗三種持久記憶。'
quote: '記憶正是區分聊天機器人與智能代理的關鍵——聊天機器人只給出回應，而 Agent 能給出被持久知識與累積經驗塑造過的回應。'
action: '設計 Agent 前依序盤點 Working、Semantic、Procedural、Episodic 四層記憶需求（W-S-P-E法則），而非盲目全部啟用。'
source_has_timestamps: true
---
# AI Agent 記憶四大類型：CoALA 框架完整解析

IBM Technology 頻道由 Martin Keen 講解 AI Agent 的四種核心記憶類型，這套框架直接解決了「聊天機器人 vs 真正智能代理」的本質差異問題——沒有持久記憶的系統只是在對話，而非真正在學習與行動。 [scribd](https://www.scribd.com/document/869199074/Links)

## 核心摘要

影片指出一個生產級 AI Agent 的關鍵設計痛點：多數開發者只關注上下文窗口（working memory），卻忽略了知識、技能與經驗三種持久記憶。這套源自普林斯頓研究團隊的 **CoALA**（Cognitive Architectures for Language Agents）框架，將人類記憶類比對映到 Agent 架構，區分出 working、semantic、procedural、episodic 四種記憶，並說明並非每個 Agent 都需要全部四種。 [scribd](https://www.scribd.com/document/869199074/Links)

## 詳細重點整理

**1. Working Memory（工作記憶）[00:00:07]**

這是 Agent 的上下文窗口，包含當前對話、系統指令與已載入的檔案資料，等同於程式中的 RAM——速度快但易失且有容量上限。即使目前最大上下文窗口可達百萬 token 級別，塞入過多資訊仍會導致模型「迷失在中間」而效能下降，這是每個聊天機器人本身就具備的記憶類型。關鍵概念：**上下文窗口即揮發性緩存**。 [scribd](https://www.scribd.com/document/869199074/Links)

**2. Semantic Memory（語意記憶）[00:03:25]**

儲存事實、規則、慣例與文件，學術上常用向量資料庫或知識圖譜實現，但實務上多數生產系統其實只用簡單的 Markdown 檔案，例如 Claude Code 專案根目錄的 CLAUDE.md，內含專案架構、程式慣例與禁忌事項，並在每次 session 開始時載入上下文。沒有語意記憶，Agent 就會不斷重複犯同樣的錯誤，因為缺乏可持續參考的知識庫。關鍵概念：**持久知識庫**。 [scribd](https://www.scribd.com/document/869199074/Links)

**3. Procedural Memory（程序記憶）[00:04:47]**

這是 Agent「知道如何做事」的能力，透過開放標準 Agent Skills 與 skill.md 檔案格式實現，每個技能是一個包含說明與步驟指引的資料夾。其核心機制是**漸進式揭露**（progressive disclosure）：Agent 平時只看到每個技能的輕量索引（名稱+描述，約百 token），符合任務需求時才載入完整指令，需要時才拉入其他檔案或模板，避免一次性塞爆工作記憶。關鍵概念：**漸進式揭露**。 [scribd](https://www.scribd.com/document/869199074/Links)

**4. Episodic Memory（情節記憶）[00:06:40]**

這是 Agent 對過去互動、決策與所學經驗的記錄，最原始的作法是儲存每次對話全文再做搜尋，但這種方式效用有限。真正實用的生產系統會做**蒸餾壓縮**：Agent 跨會話累積筆記，自行判斷哪些資訊未來值得保留，例如「上次除錯 auth 模組時，問題出在 middleware 層」這種精煉經驗，遠比完整 45 分鐘除錯記錄有用。這也是記憶中最難處理的一類，因為要決定何時該遺忘過時資訊本身就是工程難題。關鍵概念：**經驗蒸餾**。 [scribd](https://www.scribd.com/document/869199074/Links)

## 技術/數據對比

| Agent 類型 | 所需記憶類型 | 範例 |
|---|---|---|
| 簡單反射型 Agent | 僅 Working Memory | 溫控器、基本路由機器人 [scribd](https://www.scribd.com/document/869199074/Links) |
| 窄範圍任務型 Agent | Working + Procedural | 密碼重置客服 Agent [scribd](https://www.scribd.com/document/869199074/Links) |
| 完整編碼型 Agent | 全部四種 | 需要專案知識(semantic)、技能系統(procedural)、跨會話學習(episodic) [scribd](https://www.scribd.com/document/869199074/Links) |

## 結論與行動建議

**啟發金句**：「記憶正是區分聊天機器人與智能代理的關鍵——聊天機器人只給出回應，而 Agent 能給出被持久知識與累積經驗塑造過的回應。」 [scribd](https://www.scribd.com/document/869199074/Links)

**具體行動建議**——**W-S-P-E 法則**：設計 Agent 前先盤點需求，依序檢視 Working（上下文夠用嗎）、Semantic（有沒有專案知識庫）、Procedural（是否需要可複用技能）、Episodic（是否需要跨會話學習），再決定該架構要啟用哪幾層記憶，而非盲目全上。 [scribd](https://www.scribd.com/document/869199074/Links)

**生活實踐建議**：對應到日常工作，可以把 Semantic Memory 的做法應用在個人知識管理上——用簡單 Markdown 檔案記錄專案規則與慣例，而非依賴複雜工具；同時學習 Episodic Memory 的「蒸餾」精神，寫工作筆記時只記錄「下次遇到同樣問題該怎麼處理」的精華結論，而非流水帳式記錄整個過程。 [scribd](https://www.scribd.com/document/869199074/Links)

## 參考連結

https://youtu.be/BacJ6sEhqMo?si=HYjYpySoKOq8PDAR
