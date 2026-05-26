---
title: 'MCP 閘道器模式：企業悄悄採用的 AI 採購架構'
date: 2026-05-26
image: /images/AI筆記/mcp-gateway-pattern-enterprise.jpeg
category: AI筆記
tags: [MCP閘道器, 企業採購, 意圖分類, 安全策略, 遞迴編排]
description: '大型企業正悄悄採用 MCP 閘道器模式取代繁瑣的 ERP 採購操作介面，透過統一的 ChatGPT App 與 MCP 協調器自動判別採購意圖並路由到正確後端，解決系統邊界導致的 AI 體驗斷鏈問題。'
quote: '真正的 AI 轉型，不是讓員工學會新系統，而是讓系統學會消失在員工的視線之外。'
action: '從公司內部最沒人想學的系統下手，用 MCP 協調器包裝成自然語言介面，快速展示 AI 實際價值。'
source_has_timestamps: true
---
# The MCP Gateway Pattern Big Enterprises Are Quietly Adopting

[核心摘要]

大型企業（如 PwC 客戶）正悄悄採用一種新架構：以 **MCP 閘道器模式（MCP Gateway Pattern）** 取代繁瑣的 ERP 與採購系統操作介面。核心痛點是——技術採購人員（研究、機器人、營運部門）不願深入學習複雜的後端系統。透過一個統一的 ChatGPT App + MCP 協調器，系統自動判別採購意圖並路由到正確後端，解決了系統邊界導致的 AI 體驗斷鏈問題。

***

## [詳細重點整理]

### 1. 企業採購的真實痛點 [01:22]

技術採購人員——無論是 AI 研究員、機器人工程師還是營運人員——都不願意學習 ERP 和採購系統的複雜操作介面。 他們的目標只是「買到 GPU 或機器手臂」，而不是學習系統流程。這個脫節每年造成大量企業效率損耗。

**關鍵概念：系統邊界斷鏈（System Boundary Breakdown）**

***

### 2. 核心架構：GPT App + MCP 協調器 [02:43]

整體架構由三層構成：
- **前端**：一個 ChatGPT App，作為統一對話介面
- **中間層**：MCP 協調器（MCP Orchestrator），負責意圖分類與路由
- **後端**：多個 ERP / 採購系統（直接採購系統、間接採購系統）

**關鍵概念：MCP 協調器（MCP Orchestrator）** — 隱藏後端所有複雜性的核心引擎

***

### 3. 直接 vs. 間接採購路由 [04:46]

MCP 協調器使用 **Anthropic Agent Skills 標準**（以 Markdown 格式定義技能名稱與描述）自動分類採購請求：
- **直接採購**：GPU、機器手臂等核心生產物料 → 路由至直接採購 MCP Server，進行供應商驗證與優化建議
- **間接採購**：辦公椅、文具等非核心物品 → 路由至間接採購系統

**關鍵概念：意圖分類（Intent Classification）**

***

### 4. UI Resources 與 React Widget 動態渲染 [06:03]

MCP 協調器不只回傳資料，還會告訴前端 GPT App **要載入哪個 React UI 視圖**，並搭配從後端取得的結構化資料動態渲染。 這讓使用者看到的不只是文字回應，而是完整的操作確認介面。

**關鍵概念：UI Resources（UI 資源指令）**

***

### 5. OAuth vs. API Key：安全異質後端的挑戰 [06:54]

現實中後端系統的安全標準不一：有的支援 OAuth 完整身份流，有的只有 API Key。 MCP 閘道器（MCP Gateway）在此發揮關鍵作用——在前端統一加上安全策略，同時提供細粒度工具授權（Fine-Grained Tool Authorization），特別適用於高度受監管行業（如電力能源公司）。

**關鍵概念：MCP 閘道器安全層（MCP Gateway Security）**

***

### 6. MCP 呼叫 Agent 再呼叫 MCP 的遞迴編排模式 [08:15]

這個架構揭示了一個新的企業 AI 編排模式：

> **ChatGPT App → MCP 協調器 → Agent Skills → 子 Agent → 子 MCP Server**

這種遞迴結構讓單一 MCP 端點能夠協調跨多個後端的複雜工作流，而不暴露任何內部複雜性給最終使用者。

**關鍵概念：MCP-in-MCP 遞迴編排（Recursive MCP Orchestration）**

***

## [結論與行動建議]

**啟發金句：**
> 「真正的 AI 轉型，不是讓員工學會新系統，而是讓系統學會消失在員工的視線之外。」

**具體行動建議——GPO 法則（Gateway-Proxy-Orchestrate）：**
1. **Gateway（閘道）**：用 MCP Gateway 統一管理後端安全策略，不論 OAuth 或 API Key
2. **Proxy（代理）**：以 MCP 協調器作為唯一對外介面，隱藏所有後端路由邏輯
3. **Orchestrate（編排）**：用 Anthropic Agent Skills 標準定義可組合的技能單元，實現 MCP 遞迴調用

**生活實踐建議：**
- 若你正在設計 AI 應用，可先從公司內部「最沒人想學的系統」（ERP、報銷、審批）下手，用 MCP 協調器包裝成自然語言介面，快速展示 AI 實際價值。
- 參考 Anthropic 官方 [Agent Skills 文件](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) 與 [MCP 規格](https://modelcontextprotocol.io) 作為實作起點。

***

## [參考連結]

- 原始影片：https://youtu.be/aC6xuKBVHD4
- Jake Wilson LinkedIn：https://www.linkedin.com/in/jacobwilsonpwc
- Anthropic Agent Skills 文件：https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- MCP 官方規格：https://modelcontextprotocol.io
