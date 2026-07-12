---
title: 'AI Agent 記憶架構四層解析'
date: 2026-07-12
image: /images/AI筆記/ai-agent-memory-masterclass.jpg
category: AI筆記
tags: [工作記憶, 情節記憶, 語意記憶, 程序記憶, Context Assembly]
description: 'AI Agent 的記憶架構並非模型本身的能力，而是模型周圍的系統工程。模型在 context window 關閉後權重不變，真正讓 Agent「記得」的是一套'
quote: '「持久存儲是檔案櫃，工作記憶是書桌。模型只在書桌上工作——一切都取決於什麼被從檔案櫃中取出、放在它面前。」'
action: '依 W-R-S-P 法則檢查四層記憶：工作記憶是否純淨、能否找到正確的過去 session、事實是否為當前有效、程序是否最新。'
source_has_timestamps: true
---

## [核心摘要]

AI Agent 的記憶架構並非模型本身的能力，而是模型周圍的系統工程。模型在 context window 關閉後權重不變，真正讓 Agent「記得」的是一套決定何時儲存、召回、更新與遺忘狀態的記憶架構。影片以 cricket 聯賽管理應用為貫穿範例，拆解 **工作記憶**、**情節記憶**、**語意記憶** 與 **程序記憶** 四層結構如何協同運作，並指出記憶管理的核心挑戰不在儲存，而在「context assembly」——如何把正確的狀態在正確的時間推進 context window 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

***

## [詳細重點整理]

### 1. 記憶架構的本質：模型不記得，系統才記得 [00:00]

模型在 context window 關閉後，權重不會改變，也不會「醒來」時帶著昨天的筆記。真正讓 Agent 具備記憶的，是圍繞模型的外部系統——**Harness（駕馭層）**。Harness 包含工具、context、沙箱等所有包裹原始模型的機制，記憶是其中一個基礎元件，決定哪些狀態能存活到下一個動作。

**關鍵概念：Harness Primitives（駕馭層原語）**

RAG 與記憶是鄰接問題：RAG 問的是「該檢索什麼外部知識」，記憶問的是「哪些狀態應該跨對話、跨 session、跨使用者存活」。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

### 2. 四種記憶類型總覽 [01:08]

Agent 記憶分為四層：

- **工作記憶（Working Memory）**——當前 context window 中可見的活躍狀態
- **情節記憶（Episodic Memory）**——帶有時間戳記的過去事件記錄
- **語意記憶（Semantic Memory）**——不需回溯來源的穩定知識與事實
- **程序記憶（Procedural Memory）**——可重複使用的操作流程與技能

**關鍵概念：Memory Taxonomy（記憶分類學）**

### 3. 工作記憶：即時且有限的預算 [03:41]

工作記憶是模型當前能看見的所有內容：當前對話、最新使用者訊息、先前的助手回覆，以及仍在 context window 內的指令和附件。在認知科學中，工作記憶是我們處理眼前任務時使用的有限心智工作區。

**關鍵概念：Context Budget（上下文預算）**

工作記憶有兩個失效模式：

- **它會結束**——session 關閉後，所有對話內容消失，沒有持久狀態
- **它會填滿**——每一個有用的東西（指令、歷史、檢索片段）都在競爭同一個 context 預算

更大的 context window 有幫助，但不能消除設計問題。把整個 repository 倒進 context，就像把整個檔案櫃倒在桌上找一張便利貼——相關內容被淹沒，注意力被稀釋 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

### 4. 情節記憶：帶有時間的過去事件 [07:51]

情節記憶是 Agent 對「發生過的事」的記錄：特定的 issue 調查、特定的除錯 session、特定的 PR 追蹤。核心屬性是它帶有 **when（時間）**。

在 cricket 範例中，情節記憶讓 Agent 搜尋過去 session 中關於 issue #9 的歷史，例如找到「先前檢查發現沒有實作批准」或「找到了 codeex implement 評論」。這不是檢索一個扁平事實，而是帶回一個有足夠上下文的過去事件。

情節記憶的儲存可以是 Markdown 檔案、SQLite 全文搜尋，或向量資料庫（當關鍵字搜尋太脆弱時）。甚至可以用 **Temporal Knowledge Graph（時序知識圖譜）** 追蹤每個事實何時為真 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Temporal Slicing（時序切片）**

### 5. 語意記憶：穩定知識的浮動層 [10:44]

語意記憶是 Agent 的常駐知識——不需重播學習來源就知道的事。例如：你知道團隊使用 PNP，不會每次都回溯那個 PR 決定的過程。

在 cricket 範例中，語意記憶包含：
- cricket 資料夾路徑位置
- Meteor app root 在 `meteor/league` 資料夾下
- 程式碼只在兩個特定資料夾中
- buddy beantown → GitHub ID 映射

語意記憶的風險是 **事實會過時**。如果 issue #9 之前是「open but not approved」，但後來評論區已出現 `codeex implement`，兩個事實都留在記憶中而沒有時間或衝突處理，Agent 可能檢索到錯誤的版本 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Stable Fact Decay（穩定事實衰變）**

### 6. 程序記憶：如何做事的層 [13:14]

程序記憶是 runbook、檢查清單、可重複使用的技能。用人類的比喻：知道腳踏車有兩個輪子是語意記憶，知道怎麼騎腳踏車是程序記憶。

在 cricket 範例中，程序記憶不是「如果 issue 9 是 open 就實作」，而是完整的步驟序列：fetch issue → inspect commands → confirm proposal exists → confirm `codeex implement` comment → read getting-started markdown → work only in specified folders → run focus tests → open draft PR → comment back。

程序記憶可以存在：
- **Tool 定義**——tool schema 強制 Agent 提供特定結構
- **Skill 檔案**——最常見的形式
- **Runbook**
- **編排程式碼**——workflow graph、agent loop、approval gate

「實作需要明確批准」是語意記憶；「批准後要遵循的步驟序列」是程序記憶。程序記憶也會過時——如果專案已從「直接實作」改為「提案優先」的審批機制，舊流程仍被自信地執行，記憶就讓系統變得更糟 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Procedural Staleness（程序過時化）**

### 7. 記憶整合：Context Assembly 的工程問題 [15:47]

四種記憶分開來看各自完整，真正的工程問題在於如何組裝它們。在真實 Agent 中，工作記憶仍由當前 context window 構成，但它的「填充方式」不同了。

在模型回應前，**Agent Runtime（代理執行環境）** 會從多處收集材料：當前使用者請求、可見對話、過去 session 檢索、專案設定、已載入的 issue workflow、approval gate、工具結果、開啟的檔案——全部組裝成工作 context。

**核心心智模型：** 持久存儲是檔案櫃，工作記憶是書桌。模型只在書桌上工作。一切都取決於什麼被從檔案櫃中取出、放在它面前 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Context Assembly（上下文組裝）**

### 8. 記憶架構實戰演示 [18:25]

以 cricket issue #9 的完整請求為例，展示四種記憶如何協同：

| 記憶類型 | 提供的內容 |
|---|---|
| 工作記憶 | 當前使用者請求（「pick up issue #9, old club bug, assigned to buddy beantown」） |
| 情節記憶 | 先前 issue #9 session 與 approval state 變化 |
| 語意記憶 | repo 路徑、assignee 映射、approval rule |
| 程序記憶 | 實作 workflow 步驟序列 |

架構地圖分為三層：
- **左側——持久存儲**：session history、fact stores、skills & runbooks、documents & files
- **中間——Context Builder**：決定本回合拉取什麼材料，排序、組裝 prompt
- **右側——模型**：接收組裝好的工作記憶，呼叫工具、觀察結果、回應

產品名稱對照：以 Hermes 為例，它暴露的 session search、memory files、skills 幾乎一一對應情節、語意和程序記憶 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

### 9. 記憶管理的挑戰：衝突與遺忘 [20:58]

最有趣的記憶失效是 **衝突**。舊事件記錄 issue #9 是「open and assigned but not approved」，而當前執行緒顯示 `codeex implement` 評論已存在。

弱記憶系統把它當成檢索問題——抓取相關內容塞進 prompt。強記憶系統把它當成 **狀態問題**：這在何時為真？當時什麼為真？現在什麼為真？哪個程序治理當前行動？「給它一個向量資料庫」無法解決——向量資料庫擅長拉回相關文字，但無法自行判斷 issue 已從不符合變成符合 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

遺忘是另一個核心問題。記住一切的系統最終會記得太多。每種記憶類型都有自己的遺忘需求：

| 記憶類型 | 遺忘需求 |
|---|---|
| 工作記憶 | 需要選擇（selection） |
| 情節記憶 | 需要壓縮（compression） |
| 語意記憶 | 需要衝突解決（conflict resolution） |
| 程序記憶 | 需要維護（maintenance） |

**關鍵概念：Hygiene over Loss（衛生而非流失）**——遺忘不是純粹的損失，而是清理不再有幫助的內容，讓有用的東西保持易於找到。

### 10. 有效記憶處理策略 [23:09]

四個實用策略：

- **Temporal Decay（時序衰減）**——較舊的記憶降低優先級，除非被釘選、最近使用或綁定到持久策略
- **Contradiction Handling（矛盾處理）**——新事實與舊事實衝突時，更新當前狀態並將舊事實保存為歷史
- **Compression（壓縮）**——詳細 session → 摘要 → 事實 → 程序（如果描述重複的工作方式）
- **Manual Curation（人工策展）**——專案規則、approval gate、repo onboarding、production-facing checks 需要有人負責

大 context window 的討論在此定位：大窗口提供更多工作記憶，但不會幫你找到正確的過去 session、不會告訴你哪個事實是當前的、不會整理 runbook。把百萬 token 窗口塞滿過時事實、舊日誌和過時程序，只是把混亂搬進更大的房間 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Memory Compression Pipeline（記憶壓縮管線）**

### 11. 評估 Agent 記憶架構的五個問題 [25:47]

建構或評估 Agent 時，問五個問題：

1. **當前工作記憶中有什麼？**——模型這一步實際看到了什麼？
2. **哪個過去 session 重要？**——Agent 能否找到那些過去的 session、工具呼叫和結果？
3. **哪些事實是當前的？**——使用者事實、專案事實、偏好和當前狀態如何儲存和更新？
4. **哪個 workflow 適用？**——workflow 是編碼為工具、技能還是編排程式碼？
5. **什麼應該被遺忘？**——舊狀態如何失去優先級？矛盾如何處理？誰擁有程序？

如果能回答這五個問題，你看的是一個架構；如果不行，你大概只有散落的狀態。散落的狀態在 Agent 記錯事情並繼續自信執行之前都能正常運作 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Scattered State（散落狀態）**

***

## [結論與行動建議]

> **啟發金句：** 「持久存儲是檔案櫃，工作記憶是書桌。模型只在書桌上工作——一切都取決於什麼被從檔案櫃中取出、放在它面前。」

**具體行動建議——W-R-S-P 法則：**

設計或評估任何 AI Agent 時，依序檢查四層記憶：

- **W**orking：當前 context window 裡有什麼？是否被不相關內容污染？
- **R**ecall（Episodic）：能否找到正確的過去 session？能否區分舊狀態與當前狀態？
- **S**table（Semantic）：哪些事實是當前有效的？矛盾如何處理？誰負責策展？
- **P**rocedure：工作流程是否最新？程序記憶是否存在 tool schema、skill 檔案或編排程式碼中？

**生活實踐建議：** 在日常使用 Cursor、Claude Code 等 coding agent 時，主動管理 `.context.md` 或 `AGENTS.md` 作為語意記憶層，定期清理過時的專案規則與偏好設定；對重複出現的工作流程，撰寫 skill 檔案或 runbook 編碼為程序記憶，而非每次在對話中重新口述步驟。當 Agent 行為「不聽話」時，第一時間檢查的不是模型本身，而是 context builder 拉取了什麼、拉取的順序是否正確。

***

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/PxuMqeIqCEo
