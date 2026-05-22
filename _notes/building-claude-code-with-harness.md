---
title: 'Harness 工程：打造可部署的 Claude Code 代理系統'
date: 2026-05-22
image: /images/AI筆記/building-claude-code-with-harness.jpeg
category: AI筆記
tags: [Harness工程, 智能體循環, 工具調度, 上下文管理, 多智能體]
description: '這篇文章最重要的洞察是：真正讓 Claude Code 強大的，不是模型本身，而是包在模型外層的 Harness。它把 AI 代理拆成五個核心能力'
quote: '不是模型不夠強，而是大多數人沒有替模型造好 Harness。'
action: '用 L-T-C-P-A 法則落地：先做主循環、schema 化工具、分層上下文、配置化權限、最後引入多智能體'
source_has_timestamps: false
---
這篇文章的價值，不在於「怎麼寫提示詞」，而在於把 Claude Code 拆成一套可重建的工程系統：主循環、工具調度、上下文管理、權限治理與多智能體協作。原文由 Fareed Khan 於 2026/4/7 發表，並附有對應的 `claude-code-from-scratch` GitHub 倉庫可供實作參照。 [github](https://github.com/FareedKhan-dev/claude-code-from-scratch)

[核心摘要]

這篇文章最重要的洞察是：真正讓 Claude Code 強大的，不是模型本身，而是包在模型外層的 **Harness**。它把 AI 代理拆成五個核心能力：單執行緒推理循環、型別化工具系統、可壓縮的上下文層、規則式權限治理，以及可隔離的多智能體協作。這套設計解決了長任務易失焦、工具濫用、上下文爆炸與並行衝突等痛點，讓 coding agent 從 demo 升級成可部署系統。

[詳細重點整理]

註：原始來源是文章而非影片，沒有可驗證時間戳；以下改以**章節定位**標示，避免虛構時間。

1. Harness 工程的本質 [章節：文章開頭]  
Harness 不是模型訓練，而是模型外部的執行環境設計。核心原則有四個：模型只負責決策、工具是唯一外部介面、上下文必須被管理、權限應用聲明式規則。  
關鍵概念：**Harness Engineering**

2. 核心智能體循環 [章節：第一階段]  
整個系統從最小化的 while loop 開始：模型思考、要求工具、接收結果、再思考，直到任務終止。關鍵不是流程複雜，而是讓所有任務都共用同一個循環，任務差異只存在於模型決策，而不在控制程式裡。  
關鍵概念：**Perception-Action Loop**

3. 工具調度與 TodoWrite 規劃 [章節：第一階段中段]  
工具註冊表用名稱對應 handler，讓新能力能以「新增工具」而不是「改核心邏輯」的方式擴充；這是 MCP 與內建工具能共存的基礎。接著用 TodoWrite / TodoRead / TodoUpdate 建立執行前規劃，讓模型在多步任務中持續被自己的計畫約束，避免偏題。  
關鍵概念：**Typed Dispatch Registry**

4. 子智能體與上下文管理 [章節：第一、二階段交界]  
子智能體的重點不是更聰明，而是**隔離噪音**：探索大型 codebase 時，把大量 read / grep / glob 中間結果留在子上下文，父智能體只接收摘要。再往上則是按需技能載入、三層上下文壓縮與磁碟持久化記憶，讓長任務不被 token 視窗拖垮。  
關鍵概念：**Context Isolation**

5. 多智能體團隊與非同步執行 [章節：第三階段]  
系統進一步把慢操作丟到背景執行，讓主循環不被 I/O 阻塞；再用 JSONL 郵箱、FSM 協定與任務圖，讓多個專業智能體能持續溝通、領取任務並避免死鎖。這裡的工程價值在於：協作不是靠模型「懂配合」，而是靠明確狀態機與共享任務結構。  
關鍵概念：**FSM Team Protocol**

6. Worktree、權限與生產化能力 [章節：第三至六階段]  
Git worktree 解決並行寫檔衝突，每個智能體在自己的分支與目錄作業，完成後再做重疊檔案檢查。再加上 YAML 規則權限、事件匯流排、對話恢復、asyncio 並行工具、提示詞快取與官方 MCP 執行時，整套系統才真正從「能跑」變成「能上線」。  
關鍵概念：**Production Harness**

[技術/數據對比]

| 項目 | 文中設計 | 作用 |
|---|---|---|
| 主循環 | 單一 while loop | 把所有任務統一成同一種感知-行動-觀察模式 |
| 工具系統 | 名稱 + 描述 + input schema + dispatch | 限制模型表達空間，提升工具選擇穩定性 |
| 任務規劃 | TodoWrite / TodoUpdate | 讓多步任務先規劃、再執行、再驗證 |
| 上下文管理 | 技能注入 + 三層壓縮 + 持久記憶 | 控制長對話 token 壓力與失焦問題 |
| 多智能體 | 子智能體隔離 + 郵箱 + FSM + 任務圖 | 把大型任務拆解並安全協作 |
| 並行寫檔 | Git worktree | 避免多智能體同時修改同檔造成衝突 |
| 權限治理 | always_deny / always_allow / ask_user | 把安全策略前置成結構性能力 |
| 高效執行 | asyncio.gather + prompt cache + MCP | 提高工具吞吐量並擴充外部能力 |

文中幾個很值得記住的數字：上下文在約 92% 視窗使用率時觸發壓縮、提示詞快取示例中快取命中以約 10% 成本重用前綴、MCP 接入後工具數從 14 個內建擴到 28 個、Redis 郵箱示例延遲低於 10ms，而 JSONL 郵箱則受 500ms 輪詢限制。這些數字的共同含義是：真正可用的 agent，核心優化點是**上下文、延遲與控制面**，而不是再多加幾條 prompt。

[結論與行動建議]

啟發金句：  
**不是模型不夠強，而是大多數人沒有替模型造好 Harness。**

具體行動建議：  
用一個好記的 **L-T-C-P-A 法則** 來落地：  
- L = Loop，先做最小主循環  
- T = Tools，用 schema 化工具取代自然語言亂控  
- C = Context，把技能、摘要、記憶分層管理  
- P = Permissions，把安全規則寫進配置  
- A = Agents，最後才引入多智能體與非同步

生活實踐建議：  
- 做內部 AI 助手時，先別急著做 20 個 agent，先把「主循環 + 3 個工具 + todo 計畫」做好。  
- 做產品設計時，把「權限、恢復、可觀察性」當成一級需求，不要等到上線後補。  
- 做團隊導入時，優先建立 **技能系統** 與 **任務圖**，因為這兩者最直接決定 agent 是否能跨任務持續穩定工作。

[參考連結]

- 原文：[Building Claude Code with Harness Engineering](https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0)（Fareed Khan，2026/4/7） [links.thorstenfreitag](https://links.thorstenfreitag.com/?oeuUMw)
- 程式碼倉庫：[claude-code-from-scratch](https://github.com/FareedKhan-dev/claude-code-from-scratch) [github](https://github.com/FareedKhan-dev/claude-code-from-scratch)
