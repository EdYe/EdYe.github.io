---
title: 'Agent 別再手握萬能鑰匙：用 Token Exchange 收斂權限'
date: 2026-07-31
image: /images/AI筆記/agent-overprivilege-token-exchange.jpg
category: AI筆記
tags: [過度授權, 萬能憑證, 同意疲勞, Token Exchange, 策略前置評估]
description: 'AI Agent 被賦予單一萬能 API Key 後，能在無人監管下執行高風險操作（如刪除生產資料庫），造成真實事故。'
quote: '💡最好的安全不是阻止一張已經存在的憑證被濫用，而是讓它根本不存在。'
action: '🎯依 S-T-P 法則：Scope 限定工具呼叫權限、Token 鑄造短期臨時權杖、Policy 在憑證生成前先做策略評估。'
source_has_timestamps: true
---
# 📝 筆記：It's 10pm. Do You Know Where Your Agents Are?

***

## [核心摘要]

AI Agent 被賦予單一萬能 API Key 後，能在無人監管下執行高風險操作（如刪除生產資料庫），造成真實事故。Kim Maida 提出解法並非新技術，而是將 OAuth 2.0 的 Token Exchange（RFC 8693）規範整合至 Agent 執行路徑中：每一次工具呼叫都動態鑄造一個僅限該動作的短期權杖，經策略評估後才生成，確保高風險憑證根本不存在，同時讓 Human-in-the-Loop 擁有真正的策略性牙齒，適用於 CLI、MCP Server 及任何 OAuth Provider。

***

## [詳細重點整理]

### 1. Agent 越權問題的現實危害 [00:00]

從 1960 至 1980 年代的公共服務宣導「晚上 10 點了，你知道你的孩子在哪嗎？」出發，類比現今 AI Agent 被賦予過多責任卻缺乏監管的現狀。Agent 經常拿著一組 API Key 就自由運作，而這在出事前看似無害。

**關鍵概念**：**過度授權（Overprivilege）**

***

### 2. Demo：夜班事件處理 Agent [01:48]

展示一個事件管理 Agent 在夜間值班，半睡半醒的人類使用者監督下處理多張工單：

- 備用電源故障 → 判斷為硬體問題，升級給早班團隊
- TLS 憑證即將過期 → 使用同一組 API Key 呼叫雲端服務續約憑證
- 帳單資料庫損壞 → 讀取文件指示「刪除資料庫並自動還原備份」，Agent 直接 **Drop Production Postgres Database**，且無法確認備份是否成功執行，僅標記升級處理
- 重啟生產伺服器 → 使用同一組萬能 API Key 將 Prod 服務下線
- 網站三分之一使用者故障 → 自行決定擴容，產生額外雲端費用

**關鍵概念**：**萬能憑證（Kitchen Sink Credential）**—一組 Key 能做所有事，無論你是否同意

***

### 3. 為何 Agent 危險地過度授權 [04:52]

Agent 持有萬能 API Key，能自由執行它自行決定的操作，即使有人監督也難以中途阻止。Agent 的設計本質是「想幫忙」，會使用手上所有權限來完成任務。問題隨著越來越多 Agent 在無人監督下運行而加劇。

單靠 Human-in-the-Loop 無法解決，因為人類會疲勞、會有同意疲勞（Consent Fatigue），過去數十年的存取管理經驗已證明僅靠人工判斷不夠。

**關鍵概念**：**同意疲勞（Consent Fatigue）**

***

### 4. Agentic 執行路徑分析 [05:56]

完整執行路徑如下：

```
使用者 → Runtime（CLI/SDK/App）→ LLM → 提出工具呼叫
→ MCP Client 分派 → MCP Server 執行 → 呼叫資源 API
→ 回應返回 → 模型迴圈直到完成 → 回傳結果給使用者
```

Runtime 可能是 Claude Code 等 CLI、AI SDK 等 SDK、或 Cursor / Codeex 等應用。在這條路徑中有數個位置可以引入真正的存取控制，且不限於 OAuth。

**關鍵概念**：**Agentic 執行路徑（Agentic Execution Path）**

***

### 5. 解法：OAuth Token Exchange [07:27]

**RFC 8693** 是 OAuth 2.0 的擴展規範，用於 Token Exchange。解決三大核心問題：

- 憑證未被歸屬到使用者或 Agent 身份
- Agent 對 API Key 內所有權限擁有無限制存取
- 無法僅靠 Human-in-the-Loop 把關

透過**安全權杖服務（Security Token Service, STS）**作為授權伺服器，驗證身份並發行權杖。IdP（Google、Okta、Auth0 等）提供授權伺服器功能。

**關鍵概念**：**RFC 8693 Token Exchange**

***

### 6. 委派：收窄使用者權限 [08:32]

使用者登入後，授權伺服器提示使用者同意**僅委派其權限的子集**給 Agent。這是第一層權限收窄—只委派部分使用者權限。發行的權杖同時識別使用者身份及其存取層級，已比 API Key 方案更安全，因為知道「誰」在操作以及「能做什麼」。

**關鍵概念**：**權限委派收窄（Delegation Narrowing）**

***

### 7. 每次工具呼叫鑄造臨時權杖 [09:23]

OAuth Client（可能是 MCP Client 與第三方 MCP Server 間的閘道、自建 Agent 應用、或 CLI 封裝器）接收 prompt 與 Subject Token，Agent 迴圈運行時：

1. 模型提出工具呼叫
2. Runtime 使用 OAuth App Client Credentials 向 STS 認證
3. 同時發送包含使用者身份的 Subject Token
4. 建立 Token Exchange 請求，**僅要求該次工具呼叫所需的 MCP Server 權限**

此時擁有三項關鍵資訊：**Agent 身份**、**委派使用者身份**、**使用者存取層級**。

透過**治理策略（Governance Policy）**評估請求的存取、請求者、資源、委派鏈。若符合策略，STS 發行存取權杖，具備：

- **Audience 限制**：僅目標 MCP Server 可使用
- **短期有效**：通常數分鐘內過期
- **臨時性（Ephemeral）**：永不儲存，呼叫完成即銷毀

**關鍵概念**：**任務範圍短期臨時權杖（Task-Scoped Short-Lived Ephemeral Token）**

***

### 8. Demo 重現：導入 Token Exchange 後 [11:44]

同樣的 Agent 與工單，但加入了 Token Exchange：

- **硬體故障**：Audit Log 現在顯示完整資訊—Agent 代表誰操作、呼叫哪個 MCP Server、接觸哪些下游資源
- **憑證續約**：僅請求「續約憑證」的特定 Scope，而非萬能 API Key
- **帳單資料庫**：文件指示 Drop Database，但**策略在憑證鑄造前即評估**，發現限制 Agent 不得刪除資料庫 → **憑證根本不存在，無從洩漏、重放或竊取**
- **重啟 Prod**：Agent 請求使用者核准，使用者點擊 Approve，但策略要求使用者須具備特定 Role → 使用者無該 Role → 即使已核准仍被阻止
- **擴容**：使用者確實擁有權限 → 策略核准通過 → Agent 執行

**關鍵概念**：**策略前置評估（Pre-Mint Policy Evaluation）**

***

### 9. 跨平台相容性 [15:52]

基於開放標準的 Token Exchange 方案適用範圍廣泛：

- 現成 Agent 與自建 Agent
- CLI（如 Claude Code）
- 第三方與專有 MCP Server、MCP 閘道
- Agent 對 Agent 通訊
- 任何 OAuth Identity Provider
- OpenClaw 及未來新技術

***

### 10. Q&A 重點 [17:34]

- **安全屏障放置位置**：STS 位於 Runtime 與 MCP Server 之間。使用者 OAuth Token 包含使用者接受委派時的所有授權，但 Agent 不應在每次呼叫中使用所有授權，STS 確保只在請求符合範圍時才發放下游權杖。
- **企業採用阻力**：RFC 8693 並非新規範，已存在多年，不需引入全新協議。新出現的規範可與 Token Exchange 結合使用。
- **Scope 定義粒度建議**：從資源伺服器既有的 Scope 開始作為基線（因為使用者的下游 OAuth Token 已包含資源 Scope），再依需求疊加自訂 MCP Server 的治理 Scope，或直接透傳。

***

## [技術/數據對比]

| 維度 | 傳統 API Key 方案 | Token Exchange 方案 |
|---|---|---|
| **身份識別** | 無法辨識使用者或 Agent | 同時識別 Agent + 委派使用者 + 存取層級 |
| **權限範圍** | 萬能憑證，可執行所有操作 | 每次呼叫僅限該動作的特定 Scope |
| **權杖生命週期** | 長期有效，持續儲存 | 數分鐘過期，臨時性，永不儲存 |
| **策略攔截時機** | 憑證已發放後才檢查 | **憑證鑄造前即評估**，不合規則憑證不存在 |
| **Human-in-the-Loop** | 僅靠人類判斷，易疲勞誤判 | 人類核准仍受策略 Role 約束 |
| **Audit 可見性** | 僅見 API Key 呼叫端點 | 完整記錄誰、代表誰、呼叫什麼、接觸哪些資源 |
| **高風險操作防護** | 憑證存在後才阻止，有洩漏風險 | 憑證根本不存在，無從洩漏、重放或竊取 |
| **跨平台支援** | 依賴特定 API Key 機制 | CLI、MCP Server、MCP 閘道、任何 OAuth Provider |

***

## [結論與行動建議]

> **啟發金句：**
> 「最好的安全不是阻止一張已經存在的憑證被濫用，而是讓它根本不存在。」

> **具體行動建議 — S-T-P 法則：**
> - **S**cope：每次工具呼叫僅請求該動作所需的特定權限範圍
> - **T**oken：鑄造短期、臨時、永不儲存的存取權杖
> - **P**olicy：在憑證生成前即進行策略評估，讓人類核准也有真正的牙齒

> **生活實踐建議：**
> 在設計任何 AI Agent 系統時，將「最小權限原則」從概念層落實到執行層。不要給 Agent 一把萬能鑰匙後才試圖用流程攔截它；而是在它每次開門前，先確認這扇門它該不該開、你有沒有權限授權它開。即使你身為架構師或 PM 已經批准了某項操作，系統仍應有獨立的策略層把關——這不僅適用於 Agent，也是你組織內部權限治理的最佳實踐。

***

## [參考連結]

- 原始 YouTube 影片：[https://youtu.be/I3znWC3MEXM](https://youtu.be/I3znWC3MEXM)
- Kim Maida Twitter：https://x.com/kimmaida
- Kim Maida LinkedIn：https://linkedin.com/in/kimmaida
- Kim Maida 個人網站：https://maida.kim
- RFC 8693（Token Exchange）：https://datatracker.ietf.org/doc/html/rfc8693
