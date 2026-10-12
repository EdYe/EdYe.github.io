---
title: '打造第一座軟體工廠前必看'
date: 2026-10-12
image: /images/影片筆記/build-your-first-software-factory.jpg
category: 影片筆記
tags: [軟體工廠, 牙膏管擠壓效應, 六角形架構, Agent艦隊, 證據驅動自主]
description: '軟體工廠（Software Factory）是「從 issue 到合併上線」的可重複自動化流程：由 chief-of-staff agent 接收需求、派生 a'
quote: '💡你的注意力是那條牙膏管——不要再站在中段寫 code，站到兩端去：前面把決策拉出來，後面把驗證做出來。'
action: '🎯T-E-L 法則：先備齊型別約束、證據產線與 lint 強制架構，再憑證據（而非感覺）逐級調升 agent 工廠的自主層級。'
source_has_timestamps: true
source_raw: Watch this before you build your first software factory
---
## [核心摘要]

軟體工廠（Software Factory）是「從 issue 到合併上線」的可重複自動化流程：由 chief-of-staff agent 接收需求、派生 agent 艦隊寫碼、CI 驗證、agent 自動 review 到部署。核心痛點在於——工程師的價值已被「擠壓」出 coding 中段，必須移往前端規格與後端驗證。對 solo 工程師而言，搭建一座工廠只需數天、甚至數小時。

## [詳細重點整理]

### 1. 什麼是軟體工廠 

軟體工廠的定義（引用 Addy Osmani）：圍繞軟體工作的**可重複流程**。以 OpenAI 內部工廠為例，輸入是 issue tracker 或 production incident，接著自動觸發一連串流程：程式碼由 agent 撰寫、CI 自動觸發、review 由 agent 自動執行、自動部署、PR 被一路「保姆式照顧」到 rollout 完成。整個迴圈從 feature request 到可交付軟體無需人工介入。

核心主張：**這些基礎元件（primitives）都已經存在**，人們正在找出讓它運作的方法——這不是火箭科學。Solo 工程師或小團隊可以在幾天內（甚至亂做的話幾小時內）部署自己的軟體工廠。示範案例是一個給狗用的訓練排程 App（TypeScript + Express + React），刻意用「看似簡單」的 App 證明：**這套方法可以擴展到重型企業後端與安全關鍵系統**。

### 2. Demo：工廠啟動與新 Issue

實際架構：以 **Herder**（agent-aware multiplexer）做展示、以 **Pi**（開放、極度可駭、免費）作為 coding harness、GitHub Issues 作為工廠輸入介面。他強調 8~16 個平行終端 session 的「矩陣體驗」不是軟體工廠的最終形態——最終形態會是互動式聊天，多人可協同。

agent 拓撲：一名 **chief of staff（first mate / foreman）** 負責對外溝通（GitHub issues 與 repo），並在需要時派生整個 agent 艦隊。展示時刻意建立一個「欠規格」的 issue（「CSV export」），考驗 agent 是否會先發現規格不清。

關鍵概念：**Agent 艦隊**——由一個協調 agent 按工作量動態派生多個專責 agent。

### 3. AI 能力階梯修正版

一年前的 coding maturity ladder 已不夠有野心：底層的「mid-loop generation（辛辣的自動補全）」可以直接跳過，現在可以直接進入 **in-the-loop agentic coding**（與單一 agent 結對互動）。但起步仍必須經歷 in-the-loop 階段——你需要親身觀察 harness 與模型「在你的特定環境中哪裡失敗」，才能改善 agent 的環境。

階梯上層是 on-the-loop（4~6 個並行 session 熱切換——好玩一陣子後會燒盡或無聊），以及最高層的 multi-agent coding：**工廠層級**。此時你只對一到兩個 agent 說話，而你的工作方式已「蒸餾」進 skills、自訂 agent 指令與 lint 規則中（引述 poteto 的觀點）。停在 in-the-loop 就是在限制自己的產能。

### 4. 牙膏比喻 

軟體工程師的工作像被擠壓的牙膏管：**coding 中段已被完全擠出經濟誘因**——agent 做得又快又便宜，人類寫碼已無經濟意義。工程師的注意力必須移往牙膏管的兩端：

- **前端（coding 之前）**：產品定義、grill-me session、寫 spec、提前拉出重要決策（以前可以邊寫碼邊想清楚要問產品什麼，現在不行）
- **後端（coding 之後）**：嚴重投入**驗證與確認**——skills、guardrails、CI pipeline、讓系統自我驗證、讓 agent 互相驗證工作

關鍵概念：**牙膏管擠壓效應**——「go agentic or get out」已是不可選擇的現實。

### 5. 工廠前置條件 

自主要求的**信任不該建立在感覺上，而該建立在證據上**：如果 99~100% 的 PR 都穩定通過測試套件並產出一致高品質產出，你才調高自主層級。這是「證據問題」，不是「信任問題」。前置條件包括：

- **環境可虛擬化**：大部分企業軟體連單一開發機或單一 Docker 容器都跑不起來——這是「接縫」問題，不是 legacy 語言問題。能跑在 Docker image / cloud VM / microVM 是必要條件，因此 solo 開發者與小產品公司有巨大優勢
- **型別系統**：型別**約束 agent 的解空間**、提前攔截蠢錯。無型別語言必須「執行程式碼」才能獲得第一輪回饋；有型別只需編譯即可。建議：用 TypeScript（但別因此把百萬行 Java/.NET 重寫，有型別系統就好）
- **上下文**：架構圖、codebase 分析等 agent 需要的一切資訊

### 6. 測試自動化長篇論述

兩個極端都錯：mock 一切依賴的微觀 unit test「從來不是好主意」；把所有測試寫成 E2E 又會讓 CI 淪為 25 分鐘的瓶頸——自找的。正解基於**六角形架構**：

- **內核（inside）**：無依賴的業務邏輯核心，用高層級測試覆蓋（以使用者能懂的 scenario 表達）。所有依賴以 DDD 式 repository 抽象換成記憶體內的 **fakes**（不是 SQLite in-memory DB，而是與生產資料庫同抽象的查找表類別）——agent 現在非常擅長寫 fakes
- **外環（outside）**：少數 integration test 起真實 PostgreSQL（跑 migration、測讀寫更新），加上極少量跑在 Docker 的 E2E 測試

實測數據：4,000 個此類測試**以毫秒級執行**，整套 CI 最多 5 分鐘。「CI 是瓶頸」對後端工程而言是技術能力問題。

### 7. 前置條件續：Lint 與模組化 

自訂 lint 規則可強制**垂直切片架構**：例如「dog 模組的程式碼不得 reference training 模組的程式碼」。agent 擅長模組化但**愛抄捷徑**——當 lint 失敗的回饋出現，agent 會自行迭代修正並遵守你的設計意圖，無需你在場。觀察 agent 執行軌跡（trajectories）可看到它們違規後自我修正的過程。

### 8. Demo 續：Grilling 流程

工廠收到欠規格的 issue 後，feature owner（每個 issue 一名）派生 worker agent 執行 **grilling**（Matt Pocock 的 skill）：檢視 spec 與 codebase，把歧義以「開放問題」回貼到 GitHub，等待人類回答。沒有問題就直接開工。講者回答問題後按「looks good」，agent 接續工作。

模型策略：feature owner 用 Opus 級智慧模型（需要大量判斷與仲裁）；worker 用 **DeepSeek Flash** 等便宜模型。要嘛用昂貴的頂級模型免操心，要嘛把你的最佳實踐蒸餾進 skills——**後者可讓你用便宜模型而不損品質**。[[youtube](https://www.youtube.com/watch?v=iPq_aCk3EsE)]

### 9. 沙箱化 [31:40]

實際寫碼的 worker 跑在自訂 Docker 容器內（image 在 GitHub repo 可得）。沙箱三條路：

- Docker（最簡單，但 Windows 上檔案系統很慢，且可能不該是最終形態）
- Sourcegraph AMP 的 **Orbs**（VM 級原始元件）
- **T3 Code**：可註冊自有裝置（閒置筆電、遊戲桌機），從手機或工作機遠端派工給 agent

沒預算的話就 YOLO 不沙箱，但機器上有敏感資料的 solo 開發者不該裸奔。

### 10. 有憑證的 Agent

PR 不是以本人名義提交，而是以專屬 bot 帳號「Clank」提交。agent 拿自己的 GitHub 憑證操作：可限制其權限、避免洩漏私人資訊、避免讀到不該讀的 codebase。GitHub 免費允許額外 bot 帳號——在多數服務還難以發放短期 API key 的今天，這是最務實的解法。

### 11. 互動式 App 版本與 PR 證據

在建立信任的階段，每個 PR 自動起一台 VM 跑該版本 App，可直接點進去互動操作新功能（如 CSV 匯出按鈕），合併前實際驗證。這需要 work trees、分離容器、多機平行——目前較貴，但「幾個月或幾年後我們都會走到這裡」。

`/c4-diff`、`/show-me`：不看 AI 生成的每一行程式碼，改看**高層次視覺化證據**——Dex Horthy 的 `/show-me` skill 畫 ASCII sequence diagram，講者偏好 **UML 差異圖**、截圖（前端變更）、互動解說影片。挑你自己有感的組合即可。

### 12. Agentic Review [38:56]

feature owner 在 coding agent 提出 PR 後派生 **reviewer agent**：一個簡單 skill file，專門檢查 unit test 與 lint 規則**無法強制**的事——細微的架構違反、測試本身的問題。reviewer 標記問題，worker 接著修正，形成 agent 間的對抗式審查迴圈。

### 13. 靜態分析、成本與 Dark Factories 

（此段逐字稿未收錄，依章節標題與前文脈絡整理）續談靜態程式分析工具作為證據鏈的一環、工廠的 Token/模型成本控管（可觀測面板追蹤每個 issue 的花費與執行狀態），以及「**dark factory**」（全黑、無人工廻圈）是否該追求的討論——講者對此持保留態度，強調自主性應以證據為本逐級調升。

### 14. PR 文化與「AI 工廠精神病」

逐個看 PR 是**暫時性**階段：在證據與信心建立後應逐步放手。「AI factory psychosis」警告：過度盯梢與脅迫式管理自家 agent 工廠本身會成為新的精神負擔——別讓自己變成工廠的奴隸。

### 15. 總結 [52:50]

Primitives 已經就位：GitHub Issues + 免費 harness + Docker + lint + 測試，就能在幾天內搭出屬於 solo 開發者的軟體工廠。你該做的是把工作方式蒸餾進系統，讓證據（而非感覺）決定你何時放手。

## [結論與行動建議]

**啟發金句**：「你的注意力是那條牙膏管——不要再站在中段寫 code，站到兩端去：前面把決策拉出來，後面把驗證做出來。」

**具體行動法則——T-E-L 法則（Type–Evidence–Lint）**：想讓 agent 工廠自主運轉，先備齊三樣：型別約束解空間、證據產線（六角形測試 + PR 內視覺化 + 互動版本）、lint 強制架構。三者到位，你才調升自主層級——**信任要憑證據升級，不憑感覺**。

**生活實踐建議**：與其在 Claude Code 裡盯著一個 agent 跑完才下指令，不如把你的 MCP 工具、Gitea Actions、webhook 串成「issue 進、PR 出」的小型流水線：先用一個明顯欠規格的 issue 測試 grilling 行為，再把你的 review 偏好寫成 reviewer agent 的 skill file，最後讓所有 agent 用獨立 bot 帳號提交。你會發現自己從「操作者」變成「規格與驗證的設計者」。

## [參考連結]

- [原始影片：Watch this before you build your first software factory](https://www.youtube.com/watch?v=iPq_aCk3EsE)（Jo Van Eyck，2026-10-05，54:32）