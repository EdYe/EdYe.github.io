---
title: 'AI Agent 維護比打造更重要：H-P-E 法則'
date: 2026-06-23
image: /images/AI筆記/ai-agent-maintenance-hpe-framework.jpg
category: AI筆記
tags: [工具精簡, 模型漂移, 數據腐爛, Harness, AI Agent維護]
description: '「打造更多 AI Agent」不是 2026 年的真正挑戰——維護 Agent 周圍的系統（Harness）才是。Vercel 透過刪除 80% 的工具讓'
quote: 'Agent 不需要大聲地失敗，也能開始悄悄地傷害你的業務。它只要繼續工作就夠了。'
action: '定期執行 5 項 Harness 健康檢查：查來源、測權限、確認任務、要求溯源、評估價值'
source_has_timestamps: true
---
好的！這是一支由 Nate B Jones 發布於 2026 年 6 月 17 日的 AI 策略深度影片，主題核心是「AI Agent 的維護藝術」。以下是結構化筆記：

***

# 🎯 [核心摘要]

「打造更多 AI Agent」不是 2026 年的真正挑戰——**維護 Agent 周圍的系統（Harness）** 才是。Vercel 透過刪除 80% 的工具讓 Agent 變得更好，揭示了一個反直覺的事實：Agent 的退化不只因為外部世界改變，更因為底層模型自己「進步了」。

***

# [詳細重點整理]

## 1. Vercel 的反直覺教訓 [00:00]

Vercel 研究了頂尖銷售人員的真實工作流程，據此建立了一個能過濾 inbound 訊息、資格認定潛在客戶、起草回覆並分流問題的 Agent。 關鍵發現不是 Agent 建立後的功能，而是後來的維護行動：**團隊持續刪除工具，Agent 反而變得更準確、更可信**。「新手直覺是加法；維護直覺是問什麼應該被刪掉。」

**關鍵概念：工具精簡（Tool Pruning）**——移除冗餘工具以維持 Agent 的高信任度。

## 2. 模型進步本身也會「破壞」Agent [04:34]

底層模型並不穩定：它持續在推理能力、指令理解與跨步驟執行上進步。 這造成了一個新型維護問題——**為舊模型設計的 Harness，會讓更強的新模型受到不必要的限制，或相反地給予過寬的權限而釀成風險**。過去幾個月（2025 年 11 月至 2026 年 3 月）已有大量真實案例。

**關鍵概念：模型漂移（Model Drift）**——模型進步導致原有約束設計失效。

## 3. 系統數據也在腐爛 [04:34 continued]

Agent 會繼承所有周邊系統的「老舊垃圾」：過時的 Wiki、已改變定義的 CRM 欄位、失效的 SOP、變成垃圾桶的 Slack 頻道。 這對人類來說只是煩人，對 Agent 來說卻極度危險——**Agent 不會坐著等待，它會主動從過時的資料裡產出非常有說服力的錯誤結論**。

**關鍵概念：數據腐爛（Data Staleness）**——Agent 的輸出品質直接等於它所讀取的資料新鮮度。

## 4. Harness 是什麼？ [10:18]

**Harness（工作台）** 是讓模型能在真實工作中發揮作用的整套設置，包含：Agent 讀取的來源、它能記住什麼、能觸碰哪些工具、可以更改什麼、需要帶回什麼證明、以及什麼時候必須停下來讓人類決定。 OpenAI 的 Codex 和 Anthropic 的 Claude Code 被認為是目前全球打造最好 Harness 的兩個團隊。

**關鍵概念：Harness（能力脈絡框架）**——Agent 的工作台，決定 AI 能力如何轉化為真實產出。

## 5. 你的 Harness 是什麼？ [13:30]

對個人而言，Harness 可能是：提示詞、記憶配置、來源資料夾、審核習慣、瀏覽器存取規則、驗證迴圈。 對產品負責人來說是 Agent 讀取的規劃資料來源；對工程師是 repo、test、terminal、permissions 和 logs。**關鍵問題不是「我能建立 Agent 嗎？」而是「我能在漫長航程中維護這艘帆船嗎？」**

***

# [技術/數據對比]

| 維度 | 舊思維（加法） | 新思維（維護） |
|---|---|---|
| Agent 改善方法 | 加更多工具、記憶、整合 | 刪除不必要工具、精簡 Harness |
| 系統破壞原因 | 模型變差或外部故障 | 模型進步 + 環境數據腐爛 |
| 建立時機 | 一次性建置完成 | 持續迭代重建 |
| 主要風險 | 明顯的系統錯誤 | 安靜地基於舊有「真相」持續運作 |
| 代表平台 | 任何 no-code 快速搭建工具 | Codex、Claude Code（持續維護 Harness）|

***

# [結論與行動建議]

**啟發金句：**「Agent 不需要大聲地失敗，也能開始悄悄地傷害你的業務。它只要繼續工作就夠了。」

**核心法則：H-P-E 法則**
- **H（Harness）**：定義你的 Agent 工作台——來源、工具、權限、審核機制
- **P（Prune）**：定期修剪——刪除過時工具、更新數據來源、測試 Harness 是否仍符合現在的模型能力
- **E（Evolve）**：主動進化——每當模型更新或業務改變，重新審視整個系統

**具體行動建議（5 項 Harness 健康檢查）：**
1. **查來源（What's it eating?）**：Agent 讀取的文件是否仍是當前事實？
2. **測權限（Test its reach）**：現有的工具存取權，是否對當前模型能力仍然合適？
3. **確認任務（Check its job）**：Agent 的角色是否悄悄改變了？不要讓任務無聲地漂移。
4. **要求溯源（Check the proof）**：輸出必須附帶可追溯的連結與來源，不接受「模型說了算」。
5. **評估價值（Check its value）**：Agent 的輸出真的改變了工作嗎？還是在製造更多待處理的工作堆？

***

# [參考連結]

- 原始影片：[https://youtu.be/BOXK2XFLA-E](https://youtu.be/BOXK2XFLA-E) 
- 完整文章（Agent Maintenance Guide）：[https://natesnewsletter.substack.com/p/ai-agent-maintenance](https://natesnewsletter.substack.com/p/ai-agent-maintenance) 
- 推薦書目：*The Maintenance of Everything* by Stewart Brand（Stripe Press 出版）
