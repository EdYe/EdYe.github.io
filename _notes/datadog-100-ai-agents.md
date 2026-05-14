---
title: 'Datadog 部署百個 AI Agent 的實戰架構設計原則'
date: 2026-05-14
image: /images/AI筆記/datadog-100-ai-agents.jpeg
category: AI筆記
tags: [AI Agent, 評估體系, 模型無關性, DevSecOps, 持久執行]
description: 'Datadog 工程/AI 總監 Diamond Bishop 基於部署超過 100 個 AI Agent 的實戰經驗，揭示 AI Agent 從「能跑」到「能在生產環境自主運行」的關鍵落差。核心貢獻在於提出一套具備可複製性的 Agent 架構設計原則——涵蓋介面設計'
quote: '「Intelligence 不再是瓶頸，你的架構才是。」'
action: '沒有評估體系不上線任何 Agent，將所有介面設計為 Agent 可用的第一類介面，並用記憶系統解耦業務知識與底層模型'
source_has_timestamps: true
---
影片成功擷取！以下是這場來自 **Agentic AI Foundation** 大會（2026年5月11日）的精華筆記。

***

# [核心摘要]

Datadog 工程/AI 總監 Diamond Bishop 基於部署超過 100 個 AI Agent 的實戰經驗，揭示 AI Agent 從「能跑」到「能在生產環境自主運行」的關鍵落差。核心貢獻在於提出一套具備可複製性的 Agent 架構設計原則——涵蓋介面設計、持久性執行、評估體系與模型無關性——幫助工程團隊為「下一個一千個 Agent」做好準備。 [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

***

# [詳細重點整理]

## 1. Datadog 三大生產 Agent [00:30]

Datadog 目前已有三個正式上線的 AI Agent，各自針對 DevSecOps 中最耗人力的任務： [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

- **Bits AI SRE**：自主調查警報，目標是讓工程師不再凌晨兩點被叫醒
- **Bits AI Dev**：分析服務錯誤與延遲問題，自動生成程式碼修復建議
- **Security Analyst**：自動執行安全調查清單，取代大量人工重複性操作

> **關鍵概念：DevSecOps 自動化**——將開發、維運、安全三大領域的重複性任務委派給 Agent。

***

## 2. Code Agent-First：新版 Bezos API Mandate [04:20]

**Agent 是你的第一類用戶（First-Class User）**，這是此次最重要的設計思想。所有介面、文件、API 設計都必須預設 Agent 可以使用，而非僅為人類設計。 具體做法包括： [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

- 建立 **`llms.txt`** 與 **`.md` 格式文件**，讓 LLM 能讀懂你的文件
- 部署 **MCP Server**，提供 Agent 直接存取產品的入口
- 推動 UX 設計師將 Agent 納入使用者情境設計中

> **關鍵概念：Agent-Native 公司**——如果你沒有這麼做，「你會被開除並被一個 Agent 取代」。

***

## 3. 主動式 vs 反應式 Agent [06:30]

真正「贏」的 Agent 不是聊天框，而是能在背景持續運行數小時的事件驅動型 Agent。 實作要點： [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

- **Event-Driven**：由事件觸發，而非等待用戶輸入
- **Temporal 框架**：確保長時間執行的 Agent 在重啟、故障、換模型後仍能持續
- **Container / Sandbox 隔離**：不應在本機執行，需有適當儲存與檔案系統

> **關鍵概念：Durable Long-Running Agent（持久長跑 Agent）**

***

## 4. Eval, Eval, Eval：評估是護城河 [07:30]

「如果你要上線一個 Agent，但不知道怎麼做評估，請不要上線它。」這是全場最強警告。 評估體系須包含： [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

| 評估類型 | 說明 |
|---|---|
| **Offline Eval** | 上線前的靜態測試與基準驗證 |
| **Online Eval** | 生產環境中的持續監控 |
| **Living Eval System** | 隨時間演進、能自我更新的評估系統 |

進階做法：將 Eval 工具透過 MCP Server 暴露給 Agent 本身，讓 Agent 自動執行改善循環（Self-Improvement Loop）。 [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

> **關鍵概念：Eval 自動化迴圈**

***

## 5. Agent 層級的 Bitter Lesson [08:40]

Rich Sutton 的 **Bitter Lesson** 原本是給 ML 研究者的教訓，Bishop 將其延伸至 Agent 工程層： [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

- **保持 Agent Harness 極度簡單**，設計之初就預設要重寫
- **模型無關（Model-Agnostic）**：今天最強的模型明天可能不是（Claude → Codex → 下一個）
- **框架無關（Framework-Agnostic）**：不要將業務邏輯綁死在特定框架上
- 用 **Memory System** 保存 Agent 跨模型的學習成果，實現「知識可攜帶」

> **關鍵概念：Agent-Level Bitter Lesson（簡單性原則）**

***

## 6. Multiplayer 的新定義 [09:55]

「Multiplayer 不再是 Figma 那種人對人協作了。」 現在有三種協作維度，每種都需要不同的溝通機制： [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

- **Human ↔ Human**（傳統協作）
- **Human ↔ Agent**（混合協作）
- **Agent ↔ Agent**（自主協作）

> **關鍵概念：Multi-Modal Collaboration Architecture**

***

# [結論與行動建議]

**啟發金句：**
> **「Intelligence 不再是瓶頸，你的架構才是。」** [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)

**具體行動建議（E-P-M 法則）：**
- **E（Eval First）**：沒有評估體系，不上線任何 Agent
- **P（Proactive Design）**：將所有介面設計為 Agent 可用的第一類介面
- **M（Model-Agnostic Memory）**：用記憶系統解耦業務知識與底層模型

**生活實踐建議：** [youtube](https://www.youtube.com/watch?v=F0T92oxulVE)
- 現在就檢視你的產品或服務文件，加入 `llms.txt` 與 `.md` 格式版本
- 若你的團隊有 UX 設計師，下次設計評審時加入一個問題：「這個介面，Agent 可以操作嗎？」
- 不要把所有 Prompt 和邏輯綁死在一個框架（如 LangChain）上，保持可替換性

***

# [參考連結]

- 🎬 原始影片：https://youtu.be/C3y3M_03Vco?si=aO2TyKDx83fbx4g4
- 🐕 Datadog AI Agents：https://www.datadoghq.com/product/ai-agents
- ⏱ Temporal（持久執行框架）：https://temporal.io
- 📄 llms.txt 規範：https://llmstxt.org
- 🤖 Speaker 新專案：https://dispatchagents.ai
