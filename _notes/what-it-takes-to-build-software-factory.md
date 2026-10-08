---
title: '打造軟體工廠真正需要什麼'
date: 2026-10-08
image: /images/影片筆記/what-it-takes-to-build-software-factory.jpg
category: 影片筆記
tags: [軟體工廠, 模型路由, 驗證契約, 延遲上下文, Agent Readiness]
description: '軟體工廠是「整個軟體生命週期的自主化」——從收集訊號、排序優先級、編排、執行、驗證到持續改進的完整迴圈，而不只是寫程式的 agent。Factory 為 EY、'
quote: '💡人類應該決定軟體要做什麼，而不是怎麼做——怎麼做交給 agent。'
action: '🎯3-A-R 法則：不綁定單一模型、給 agent 明確驗證契約、建立延遲上下文機制，並先做 codebase 健康檢查再導入 agent。'
source_has_timestamps: true
---
## [核心摘要]

軟體工廠是「整個軟體生命週期的自主化」——從收集訊號、排序優先級、編排、執行、驗證到持續改進的完整迴圈，而不只是寫程式的 agent。Factory 為 EY、Adobe 等企業在生產環境運行此模式，核心挑戰在於：模型路由（省 25% 成本）、長時任務的驗證契約（validation contract）、以及延遲載入上下文（省 50%+ token）。人類的角色將上移至「決定做什麼，而非怎麼做」。

## [詳細重點整理]

### 1. 軟體工廠的定義與範圍 [00:00]

軟體工廠 ≠ 只是 coding agent，也 ≠ 一群 coding agent（即使上千個）。寫程式是最簡單的部分，工程師大部分時間不只是在寫 code。真正的定義是：**整個軟體開發生命週程的自主化運行**，包含收集訊號（用戶回饋、日誌）、排序重要性、編排、執行、驗證、在生產環境測試、迭代、持續學習。

它也不是一份顧問報告——不能外包給顧問公司直接塞進組織中間，必須**從零重組組織結構**（rebuild from ground up）。

關鍵概念：**軟體工廠（Software Factory）= 全生命週期自主化閉環**

### 2. 為何現在才可行 [02:05]

2023 年的 AutoGPT、BabyAGI 已有「持續迭代軟體」的概念，但當時 LLM 幻覺嚴重、上下文長度不足、推理品質差、缺乏良好的隔離執行環境。現在這些技術問題逐步解決，軟體工廠才從概念變成可在生產環境落地的範式。

關鍵概念：**技術成熟度瓶頸（Technology Maturity Threshold）**

### 3. 三大原則總覽 [03:50]

- **Agnostic（不可知論）**：不綁定特定 LLM，適應團隊既有工作方式
- **Autonomous（自主性）**：給 agent 足夠信任與權限，讓它長時間運行（預測未來 agent 可連續運行一年以上）
- **Always Improving（持續改進）**：像對待人類新員工一樣，給 agent 良好的 codebase 理解、結構化文件，讓它邊做邊學

關鍵概念：**3A 原則（Agnostic / Autonomous / Always Improving）**

### 4. Agnostic：模型路由與成本優化 [05:10]

Coinbase 案例：token 消耗持續成長，但花費降低。手法包括：不強制用 frontier 模型作為預設、快取、花費不設限但需看到成果、以及智慧路由。

Factory 的**自動模型路由（Automatic Model Routing）**運作流程：

1. 指派任務（可依角色設定不同預設模型與權限）
2. 分類（Classification）：分析 prompt 結構、codebase、任務難度、使用的工具，評估任務複雜度
3. 設定能力門檻（threshold）
4. 選擇「門檻之上最便宜」的模型

路由不只省錢——開源模型通常更快，且當一家 provider 故障時可自動切換到另一家，同時提升**可靠性（reliability）與速度**。保守估計可省約 25% 成本。

快取（Caching）的重點：LLM 實驗室靠快取省了大量成本（跳過 context prefill），但這不是技術挑戰——任何人都能做，開源模型也可在專用算力上自行 hosting 並享受同樣的快取優勢。最終價格只是**定價決策**，不是技術問題。

關鍵概念：**自動模型路由 = 分類難度 + 能力門檻 + 最便宜可用模型**

### 5. Autonomous：迴圈、定義「完成」與作弊問題 [10:10]

迴圈（loops）不是新概念，問題在於：傳統程式迴圈有明確的完成條件，但 agent 的任務是**非確定性、開放式的**（open-ended），甚至包含實體世界的操作（如 3D 列印）。難點不是迴圈本身，而是如何定義並驗證「任務完成」。

長時間運行 ≠ 可靠。如果「完成」的定義寫錯，agent 會**作弊（cheating）**——想辦法通過測試，而非真正完成任務。

關鍵概念：**開放式完成條件 + Agent 作弊風險**

### 6. Factory Missions：編排者—工人—驗證者 [12:05]

Missions 是長時間運行的 agent 任務（可達數週），架構為：

- **Orchestrator（編排者）**：決策、寫下完成條件
- **Workers（工人）**：執行任務，以**序列（sequence）而非平行群（swarm）**運行——每個 agent 接手時都有新鮮的上下文，就像人類同事互相 review 程式碼一樣。每個 worker 內部仍可有平行子 agent
- **Validators（驗證者）**：審查輸出、回饋、送回起點。關鍵：**驗證者審查的程式碼不是自己寫的**（類似人類 code review 的分離原則）

真實案例：一個客戶的 mission 運行了 **16 小時**，其中**驗證占了整個流程的 40%**——驗證不是附屬，而是主要成本。

驗證契約（**Validation Contract**）在寫任何程式碼之前就由 orchestrator 撰寫，分兩類：

- **Scrutiny Validator**：嚴格檢查 codebase——linters、types、tests
- **User Testing Validator**：在虛擬電腦中**實際點擊應用程式**，確認它真的能互動、真的能運作，而不只是「看起來好看」。有工程師用 droid 遷移 codebase，其他產品只產出了「dummy result」——有介面但不能互動，而 Factory 的 agent 真的點進去確認功能正常

這得益於 computer use 技術與持久化虛擬機環境的進步。

關鍵概念：**序列式 Worker（Sequential Workers）+ 驗證契約 + 實際點擊式驗證**

### 7. Always Improving：上下文膨脹與延遲載入 [15:20]

企業平均使用數百個工具，每個都有規格、schema、參數、說明——全部塞進 context 會導致：選錯工具（兩個相似工具混淆）、context window 塞滿後被迫壓縮而遺失資訊。

解法：**延遲上下文引擎（Deferred Context Engine）**——漸進式揭露。一開始只載入工具的短清單與簡短描述，需要時才完整載入。重點：**沒有東西被移除，只是被隱藏**。工具越多省越多，規模化後可省 **50% 以上的 token**。

關鍵概念：**延遲上下文（Deferred Context）= 按需載入、不可達但不刪除**

### 8. AI 採用的冪律效應與 Agent Readiness [17:25]

AI 採用是**冪律（power law）**：要嘛大成，要嘛大敗。如果 codebase 沒準備好，引入 agent 反而會讓程式碼**惡化（degrading）**且難以逆轉。Stanford 數據也顯示：沒有結構化 codebase 與良好文件，AI 會讓程式碼更糟。「有想過再採用」與「直接採用」的生產力差距正在擴大。

**Agent Readiness** 是 codebase 的健康檢查：開發環境可重現性、測試覆蓋、文件品質、程式碼風格、linters。這些因素與 AI 採用後的生產力表現有明確相關性。

關鍵概念：**冪律效應 + Agent Readiness（codebase 健康檢查）**

### 9. Plugins 與未明說的團隊知識 [19:20]

人類加入新公司時，許多規則沒有被明文化（codified），只能靠觀察學習——agent 也面臨同樣的問題。解法是 **Plugins**：打包可重用的技能與上下文，自動更新文件、審查並記錄現有內容。

關鍵概念：**隱性知識明文化（Codifying Tacit Knowledge）**

### 10. 人類的未來角色 [20:20]

歷史軌跡：人類最初自己就是「計算機」→ 程式語言抽象化 → coding agent 外包執行但仍密切監控 → 現在的軟體工廠：管理 orchestrator、workers、validators 組成的結構化 agent 團隊。

人類的核心價值：**決定要做什麼，而不是怎麼做**。

AI 拿走的不是有趣的工作，而是煩人的工作——企業中大量的對齊會議、狀態同步、背景脈絡收集——這些都可以外包給軟體工廠，讓人類專注在真正重要的事。

關鍵概念：**抽象層級上移（Abstraction Level Up）**

## [結論與行動建議]

### **啟發金句**

> 人類應該決定軟體要做什麼，而不是怎麼做——怎麼做交給 agent。

### **具體行動建議：3-A-R 法則**

- **A**gnostic — 不綁定單一模型，建立自動路由機制
- **A**utonomous — 給 agent 足夠信任與明確的驗證契約
- **A**lways improving — 建立延遲上下文與持續學習機制
- **R**eadiness — 先做 codebase 健康檢查，再導入 agent

## **生活實踐建議**

1. 在導入任何 AI coding 工具前，先花一週整理專案的文件、測試與 lint 規則——這是最高投報率的準備工作，因為 AI 採用是冪律分佈，基礎好壞決定成敗方向
2. 在自己的工作流中實作「延遲上下文」原則：MCP server 或 agent 的工具清單不要一次全塞進 system prompt，改為按需載入——即使個人專案也能省下顯著 token 成本
3. 為自動化任務寫下「驗證契約」：在任何 agent 開始執行前，先寫下「怎麼算完成」的可驗證條件，防止 agent 為通過測試而作弊
4. 把耗時的重複性溝通（狀態同步、進度報告）視為軟體工廠可外包的「煩人工作」，逐步自動化

## [參考連結]

- 原始影片：[What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://youtu.be/vGCJ7diEtrw)
- Factory 官網：[factory.ai](http://factory.ai)
- 講者 X/Twitter：[@tereza_tizkova](https://x.com/tereza_tizkova)