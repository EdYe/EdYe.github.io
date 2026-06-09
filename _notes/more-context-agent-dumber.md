---
title: '為何更多 Context 反而讓 Agent 變笨'
date: 2026-06-09
image: /images/影片筆記/more-context-agent-dumber.jpeg
category: 影片筆記
tags: [上下文膨脹, U曲線效應, Context優化, 80/20混合模型, 裁判節點]
description: '這場演講揭示了一個反直覺的核心洞察：給 Agent 更多 Context 並不會讓它更聰明。Nupur Sharma（Qodo）從 DevSecOps 背景出發，提出「U 曲線效應」解釋 LLM 為何遺忘中間資訊'
quote: '💡 把整個代碼庫丟給 Agent，它會記住開頭和結尾，然後悄悄地遺忘中間的一切。'
action: '🎯 依 I-S-J 法則設計 Pipeline：迭代式檢索、80/20 推理拆分、加入裁判節點整合多 Agent 結果。'
source_has_timestamps: true
---
## [核心摘要]

這場演講揭示了一個反直覺的核心洞察：**給 Agent 更多 Context 並不會讓它更聰明**。Nupur Sharma（Qodo）從 DevSecOps 背景出發，提出「U 曲線效應」解釋 LLM 為何遺忘中間資訊，並系統性地介紹三種 Context 優化策略，以及解決 Agent 陷入「無限決策迴圈」的 80/20 混合模型架構。

***

## [詳細重點整理]

### 1. Agent 演進的困境 [00:48]

Agent 從靜態 4K prompt → 可使用工具的 Agentic Workflow → 多 Agent 協作，每一階段雖試圖解決問題，卻也帶來新的失控點：工具不知何時停止、多 Agent 之間理解衝突。核心問題從未解決：**Context 增加 ≠ 智能提升**。

**關鍵概念：上下文膨脹悖論（Context Inflation Paradox）**

***

### 2. U 曲線效應：中間記憶流失 [02:52]

LLM 在處理長 Context 時，呈現「頭尾記得、中間遺忘」的 **U 曲線（U-Curve）** 現象。Agent 只會關注初始目標與最後輸入，中間插入的 Jira 資訊、MCP 工具呼叫結果會被模型主動「淨化」以維持自身連貫性。Qodo 透過 Benchmark 實測驗證了此現象。

**關鍵概念：U 曲線記憶遺失（U-Curve Attention Degradation）**

***

### 3. 四種 Context 優化策略與成本對比 [04:26]

| 策略 | 原理 | 開發投入 | 適用場景 |
|---|---|---|---|
| **Context Engine（情境引擎）** | 建立搜尋排名邏輯，作為「過濾門衛」 | 中等，但規模化困難 | 大型產品公司 |
| **Hierarchical Summarization（階層式摘要）** | 為每個檔案/資料夾產生摘要索引 | 高（每次變更需 LLM 處理）| 有穩定代碼庫的團隊 |
| **Knowledge Graph（知識圖譜）** | 建立邏輯依賴關係的圖資料庫 | 最高，初期設定複雜 | 多 Repo 複雜依賴 |
| **Iterative Retrieval（迭代式檢索）** | 像「圖書館索引卡」按需深入查詢 | 低，結果品質佳 | 個人或小型團隊自建 Agent |



***

### 4. Self-Correction 自我修正機制 [07:50]

在 Agent 執行鏈中加入 **Critic Node（評審節點）**，負責比對 Agent 的輸出與原始目標是否一致。若 Context 已流失，評審節點強制 Agent 重跑。代價是增加延遲，但幾乎不需要開發者額外投入初始資料建置。

**關鍵概念：自我校正迴路（Self-Correction Loop）**

***

### 5. 編排悖論與 80/20 混合模型 [08:31]

能力越強的 LLM（如 Claude Opus）越容易陷入「研究方法」而非「解決問題」的無限迴圈——**Orchestration Paradox（編排悖論）**。解法是 **80/20 混合架構**：

- **80%：高推理模型**（開放式探索、工具選擇、問題發現）
- **20%：輕量確定性模型**（摘要輸出、驗證結果、最終判斷）
- 搭配 **計數器或超時機制**（如最多 5 次迭代、或 5 分鐘逾時）強制跳出迴圈

**關鍵概念：80/20 混合推理架構（Hybrid Reasoning Split）**

***

### 6. Qodo 代碼審查架構實作 [14:44]

Qodo 將上述理論落地為可運行的 **混合 Agent 架構**：

- **Context Collector**：收集 PR 資訊、工具輸出、Context Engine 資料
- **專業子 Agent**：安全 Agent、代碼差異 Agent、Jira Agent 等各司其職
- **Judge Agent（裁判節點）**：整合所有子 Agent 輸出，並對照 PR 歷史紀錄進行加權
- **自適應學習**：開發者接受建議 → 權重提升；拒絕建議 → 權重降低，形成持續進化的 Feedback Loop

**關鍵概念：加權式裁判節點（Weighted Judge Agent）**

***

## [結論與行動建議]

**啟發金句：**
> 「把整個代碼庫丟給 Agent，它會記住開頭和結尾，然後悄悄地遺忘中間的一切。」

**具體行動建議（I-S-J 法則）：**
- **I（Iterative Retrieval）**：優先採用迭代式檢索，低成本、高效益
- **S（Split 80/20）**：高推理模型負責探索，輕量模型負責決策輸出
- **J（Judge Agent）**：加入裁判節點整合多 Agent 結果，避免答案相互矛盾

**生活實踐建議：**
作為 AI 應用架構師，下次設計 Agent Pipeline 時，**不要試圖用一個萬能 Agent 完成所有任務**。拆分成「專業子 Agent + 裁判節點」，並為每個子 Agent 設定精準的 Context 邊界，就像為不同專業的工程師分配各自負責的 Code Review 範疇——讓每個人做自己最擅長的事。

***

## [參考連結]

- 原始影片：https://youtu.be/EcqMYoIV57A?si=0Db2tghSRoiK8Ui7 
- 講者 LinkedIn：https://www.linkedin.com/in/nupursh/
