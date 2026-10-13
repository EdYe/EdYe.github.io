---
title: 'Code Review 之死：人工審查成為新瓶頸'
date: 2026-10-13
image: /images/影片筆記/death-of-the-code-review.jpg
category: 影片筆記
tags: [人工審查瓶頸, 審查效率斷崖, 多重審查共識, 迴圈上的人類, 審查系統化]
description: 'AI agent 讓開發者產出 741% 更多的程式碼，但實際出貨的軟體只增加 30%——瓶頸已從「寫程式」轉移到「人工 code review」。本場演講以 '
quote: '💡未來幾年的贏家不是產出最多程式碼的團隊，而是能用證據說明為什麼信任自己出貨東西的團隊。'
action: '🎯R-H-E 法則：停止逐個審 PR，把人類判斷投入 Review Harness，將「好」的定義、公司脈絡與領域知識編碼為規則與評測，再放量給 agent。'
source_has_timestamps: true
source_raw: the death of the code review
---
## [核心摘要]

AI agent 讓開發者產出 741% 更多的程式碼，但實際出貨的軟體只增加 30%——瓶頸已從「寫程式」轉移到「人工 code review」。本場演講以 Cisco、METR、Cognition、OpenAI、Bun 等大量實證數據證明：「審得更用力」與「完全不審」都不可行，code review 正被重建為一套由人類設計規則、機器執行的工程系統（review harness），人類角色從引擎升級為飛行員。

## [詳細重點整理]

### 1. 新瓶頸：人工審查 [00:00]

Agent 產生程式碼的速度暴增，但人類審查速度完全不變。三位經濟學家追蹤 100,000 名 GitHub 開發者並比對 telemetry：啟用自主 agent 的開發者寫了 741% 更多的程式碼，出貨軟體卻只多 30%。研究直指 review 是瓶頸——通往 production 的路徑仍經過人類。產生程式碼突然變得極便宜，但「判斷能否信任它」仍然極其昂貴，尤其涉及高爆炸半徑（blast radius）的敏感程式碼。

關鍵概念：**人工審查瓶頸（Human Review Bottleneck）**

### 2. 生成不再是瓶頸，但「審更用力」行不通 [02:37]

Stripe 在 Anthropic 的 Fable 發表材料中報告一天內遷移 5,000 萬行 Ruby codebase（原估需團隊兩個月）；Bun 用六天把百萬行 Zig 遷移到 Rust。然而 Cisco 兩十年前的研究（10 個月、2,500 次審查、320 萬行程式碼）顯示：**reviewer 單次閱讀超過 400 行後找缺陷的效率崩潰，每小時超過 450 行則完全失效**。以此計算，一個 agent 的 10,000 行 PR 需要三到四個工作天的人工審查——而一個開發者可同時跑十幾個 agent。專職審查者不但會迅速倦怠，數據也證明此路不通。

關鍵概念：**審查效率斷崖（Review Effectiveness Cliff，400 行門檻）**

### 3. 不讀程式碼？迴圈設計與 OpenAI 零人工產品 [04:52]

Peter Steinberger（OpenClaw 作者）主張「不該再 prompt agent，該設計 prompt agent 的迴圈」；Andrej Karpathy 也提倡把自己移出迴圈。OpenAI 今年二月發表內部實驗：從空 repo 開始、全程 agent 撰寫，五個月後達百萬行程式碼、1,500 個 merged PR，僅用三名工程師，連審查 agent 的 scaffolding 都由 agent 撰寫，且「人類可以審 PR 但不必要」，審查幾乎全部 agent 對 agent。但 OpenAI 未揭露產品內容、也未開源做法——暗示此策略仍有破洞。核心賭注是：**迴圈設計能否取代人工檢查，取決於迴圈能看到什麼**。

關鍵概念：**迴圈設計替代檢查（Loop Design Substitutes for Inspection）**

### 4. 測試通過 ≠ 可合併：METR 與 FrontierCode [06:42]

METR（三月）聘請四位 SWE-bench 對應的開源專案現役維護者，審視已通過 SWE-bench Verified 的 PR——**只有約一半真正夠格被 merge**。失敗點不是正確性，而是程式碼品質與悄悄破壞其他程式碼的變更（測試套件之外的事物）。Cognition（Devon 作者群）六月推出 FrontierCode：20+ 位維護者從自家 repo 打造 150 項任務（每項 40+ 小時專家工作），評分行為正確性、回歸、安全性、範圍、紀律、測試品質與可維護性——把人類審查 rubric 機器化。

關鍵概念：**Mergeability 評測（人類審查準則的機器可檢查化）**

### 5. Mergeability 基準將成為下一個訓練訊號 [09:11]

Sarah Guo 指出：編譯器是免費驗證器、測試套件是免費驗證器——**任何可便宜驗證的東西都能被訓練到擊敗它**，這正是模型生成程式碼快速變強的原因。因此 mergeability 基準一旦出現，不只會是量測工具，會立刻成為 frontier model 的訓練訊號；「誰寫下今天的審查標準，就是在寫明年的預設模型行為」。前例：2024 年 OpenAI 的 CriticGPT 訓練來抓模型寫的程式碼的 bug，人機協作優於任一方，且該訓練訊號立刻讓模型變好。

關鍵概念：**免費驗證器定理（Free Verifier Principle）**

### 6. 今日的自動化審查：GitHub Copilot 與 Cursor [11:06]

GitHub Copilot 的 reviewer 已完成 6,000 萬次審查，佔全 GitHub 所有 code review 的五分之一以上——機器審查已是世界最大 code host 的主流預設。Cursor 公開了 reviewer 架構：第一版對每個 diff 跑 **8 次審查 pass 並洗牌順序**，因為審查順序會改變結果——目的是過濾誤報（自動審查者亂標就會被忽略）。北大團隊獨立驗證同一手法：多次審查、保留共識項，可提升審查品質達 44%。Cursor 重建版讓模型對 diff 推理、呼叫工具、決定往哪深挖，最有趣的細節是：**必須明確告訴模型「預設不信任程式碼、假設一定有問題」**——好的審查本質就是預設懷疑。

關鍵概念：**多重審查共識（Multi-pass Consensus Filtering）**

### 7. 審查與修復融合 + 廠商生態 [13:16]

Cursor 的 reviewer 現在會從自己的發現生成 fix agent——不只標記 bug，還寫出補丁交回 diff 給你核准，下一步計畫是讓 reviewer 實際執行程式碼以證明自己的 bug 報告為真。CodeRabbit 是最大專職 reviewer（已審 1,300 萬+ PR）；Greptile 為整個 repo 建圖，讓 reviewer 看到變更如何影響遠端程式碼；Graphite 用開發者接受/拒絕自家建議來建立評測集。**所有廠商的成功指標都相同：人類是否接受我的答案**。Cursor 稱之 resolution rate，已從 52% 推升到 70%+——這些公司每天大規模用人類接受度訓練審查 harness。

關鍵概念：**接受度指標（Acceptance Metric / Resolution Rate）**

### 8. 能否完全跳過人類？Carlini 編譯器與 Bun 移植 [15:00]

Anthropic 的 Nicholas Carlini 用 16 個 agent 從零以 Rust 打造 C 編譯器，能編譯 Linux kernel，約 2,000 個 session 無人在迴圈內（in the loop）——但**人類一直在迴圈上（on the loop）**：測試 harness、回饋系統全是人類寫的。Carlini 自己警告：看著測試通過就以為完工，但極少如此。Bun 把百萬行 Zig 移植到 Rust，六天完成、測試套件通過 99.8%，沒有人類讀過那個 diff；但檢視後發現 **13,044 個 unsafe block，同等規模的人寫 Rust codebase 約只有 74 個——高出三個數量級**。Unsafe block 是作者「斷言」而非「證明」記憶體安全之處；測試套件能驗證公開介面的行為，卻驗證不了 13,000 個測試套件從未設計去檢查的斷言。

關鍵概念：**迴圈上的人類（Human on the Loop）**

### 9. OpenAI 如何把審查重建為系統 + Dex Horthy 的反悔 [17:30]

OpenAI 沒有刪除審查，而是搬移它：Codex 審自己的變更，再叫更多 agent 審那些審查，循環到每個 agent reviewer 都滿意為止；每個變更點都讓 Codex 可開機執行，能實際跑一份 Codex 看 UI、確認 bug 被修；並把整個 logging stack 曝露給 agent。失敗時的修法「幾乎從來不是更努力試」（與 Cisco 研究呼應）。他們一度每個週五得人工清理 AI slop，後來訓練專責 agent 處理——**審查沒有消失，而是被重建為一個由人類打造的系統**。Dex Horthy 花六個月叫大家不要讀程式碼，今年三月在台上收回：「我錯了，請讀程式碼。我們試了六個月不讀，下場不好，被迫大規模拆掉重寫系統的某些部分。」

關鍵概念：**審查系統化（Review Rebuilt as a System）**

### 10. 測試看不見的脈絡與人類檢查點的存活 [19:30]

測試通過從不告訴你：這個 module 存在是因為有三個外部使用者；有個沒人承認寫的 cron job 依賴它存在。**測試套件之外永遠有脈絡**。人類檢查點持續存活於可預測之處：正確性無法便宜驗證之處、爆炸半徑大的地方、資安環境（提議移除人工審查會被立刻否決）、以及需要有人署名負責的地方。人類角色不是消失，而是**向上移動好幾層**：從逐行檢查程式碼，變成設計並調校那些檢查程式碼的系統、定義什麼是「好」。

關鍵概念：**人類角色上移（Humans Moving Up the Stack）**

### 11. 誰來審查審查者？Prompt Injection 與 Production [20:40]

Anthropic 自家的自動安全審查器在 README 中明載：**未針對 prompt injection 攻擊強化，僅應用於審查受信任的 PR**——審查器會被它正在審查的東西說服放行。今年三月的研究證實：包著無辜 commit message 的漏洞程式碼，88% 的機率騙過自主審查 agent，送給人類 reviewer 卻只有 35% 通過。移除人類不只失去一個 reviewer，而是失去「難以被愚弄的東西」——自動審查會栽在「自信框架的壞程式碼」上，而那正是 agent 最擅長產出的東西。加上 benchmark scaffold 被抓到洩漏答案，連如何為這些評審者評分都沒有共識，因此**Production 成為最後一位屹立不搖的審查者**：一旦 premerge 全是機器，觀察程式碼在真實世界實際做什麼的軌跡（trajectory）就變得不可或缺。

關鍵概念：**Prompt Injection 攻擊面與 Production 即審查者**

### 12. 今天就能做的事：打造審查 Harness [23:29]

結論：code review 沒死，但被重建為工程系統；人類從驅動審查的引擎變成飛行員。具體行動：**停止逐個審查 PR**——那是 2026 年錯誤的抽象層級。把寶貴時間投入建立可靠的 review harness：將你對「好」的定義、公司脈絡、領域知識編碼成規則與評測，再放量給 agent 使用。把心力集中在審查者、規則與評測的上層，就能突破「只快三分之一」的封頂。**未來幾年的贏家不是產出最多程式碼的團隊，而是能用證據說明「為什麼信任自己出貨的東西」的團隊。**

關鍵概念：**審查 Harness（Review Harness）**

## [結論與行動建議]

**啟發金句**：「未來幾年的贏家不是產出最多程式碼的團隊，而是能用證據說明為什麼信任自己出貨東西的團隊。」

**具體行動建議（R-H-E 法則）**：停止逐個審 PR（Stop Reviewing），把人類判斷投入**R**eview **H**arness——**E**ncode（編碼你的「好」的定義、公司脈絡與領域知識為規則/評測），再放量給 agent。心力的正確抽象層級是：審查者 → 規則 → 評測，而非逐行 diff。

**生活實踐建議**：作為 AI 應用架構師，可將此原則直接套用到你的 Gitea + MCP + Actions 工作流：在 webhook/Actions pipeline 中加入多重審查 pass（借用 Cursor 的 8-pass 洗牌共識法過濾誤報）、為自動審查 agent 加入「預設不信任、假設有問題」的系統提示、並因應 prompt injection 風險（88% 騙過率）把人工檢查點保留在資安敏感與高爆炸半徑的變更上；同時為 production 軌跡建置觀測（如 Arize 這類 observability 工具），讓「實際跑了什麼」成為最後的審查者。

[參考連結]

原始 YouTube 網址：[https://youtu.be/*mi3alkqy4s*](https://youtu.be/mi3alkqy4s)