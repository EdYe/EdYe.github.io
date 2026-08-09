---
title: 'Agent Auth協議：用權限取代憑證'
date: 2026-08-09
image: /images/AI筆記/agent-auth-authority-over-credentials.jpg
category: AI筆記
tags: [身份冒充, 權限分離, D-A-I三層架構, 能力模型, 即時撤權]
description: 'Agent Auth 協議解決 AI Agent 時代最迫切的安全痛點：Agent 不應假扮使用者使用其憑證，而應擁有獨立身份與細粒度權限控制。'
quote: '💡「停止給 Agent 你的鑰匙，給它們一張有你簽名的通行證——上面寫清楚能去哪裡、能做什麼、何時失效。」'
action: '🎯依A-R-C法則：給Agent權限（Authority）不給憑證、確保每個Agent可獨立撤銷（Revocable）、用細粒度Capability取代粗粒度Scope（Capability-based）。'
source_has_timestamps: true
---
## [核心摘要]

Agent Auth 協議解決了 AI Agent 時代最迫切的安全痛點：當 Agent 代為存取 Gmail、行事曆等服務時，傳統做法是讓 Agent「假扮使用者」使用其憑證，等同把 CEO 密碼交給新員工。此協議提出三大核心能力——可發現性（Discovery）、授權（Authorization）、身份（Identity），讓 Agent 成為獨立的主體（Principal），擁有自己的私鑰與能力清單，實現細粒度權限控制、完整稽核日誌與即時撤銷，從根本上改變 Agent 的安全範式 。 [youtube](https://www.youtube.com/)

## [詳細重點整理]

### 1. Agent 安全盲區 [00:12]

AI 浪潮中人們過度興奮，卻鮮少思考安全性。當你對 Agent 說「讀取我的郵件」「發送 email」時，Agent 實際上以你的身份在操作——它假扮成你，而非以自身身份行事。這與網際網路早期如出一轍：先狂歡，後才意識資安問題 。 [youtube](https://www.youtube.com/)

關鍵概念：**身份冒充（Identity Impersonation）**

### 2. 「雇用你的 Agent」類比 [02:48]

雇用新員工時，你會給他們專屬的 email 與憑證，絕不會把 CEO 的密碼交出去。Agent 也應如此——給予「權限（Authority）」而非「憑證（Credentials）」。這是整個協議的核心理念 。 [youtube](https://www.youtube.com/)

關鍵概念：**權限分離（Authority Separation）**

### 3. 三大核心問題 [04:21]

Agent 生態面臨三個根本性問題：

- **可發現性（Discovery）**：Agent 如何自動知道它能做什麼？目前需手動連接 MCP 或貼上個人 Token，缺乏自動化的能力目錄。
- **授權（Authorization）**：如何對 Agent 進行細粒度的權限授予？目前一旦連接 Gmail 往往給予完整讀取權限，缺乏精確控制。
- **身份（Identity）**：如何追蹤哪個 Agent、在何時、代表哪個使用者做了什麼？沒有獨立身份就無法實現稽核與撤銷 。 [youtube](https://www.youtube.com/)

關鍵概念：**D-A-I 三層架構（Discovery-Authorization-Identity）**

### 4. Capabilities 取代 Scopes [09:12]

傳統 OAuth 使用 Scope（如 `read`、`write`），但 Scope 過於粗粒度，無法精確表達 Agent 能執行的具體操作。Capabilities 模型將意圖（Intent）映射到具體工具操作，例如「讀取上週郵件」映射到 `gmail.messages.list` 這個能力，而非模糊的 `read` Scope 。 [youtube](https://www.youtube.com/)

關鍵概念：**能力模型（Capability Model）**

### 5. Well-known Agent Configuration Endpoint [10:30]

借鑑 OIDC 的 `.well-known/openid-configuration` 模式，Agent Auth 提出一個公開端點，讓 Agent 自動發現服務的互動方式——包括加密方式、能力清單等。服務只需實作此端點，Agent 即可自動協商能力 。 [youtube](https://www.youtube.com/)

關鍵概念：**Well-known Discovery Endpoint**

### 6. OpenAPI 轉譯與 Directory [11:40]

在所有服務原生支援協議之前，Agent Auth 透過 OpenAPI Spec 將現有服務的端點自動轉譯為 Capabilities。Directory 扮演「電話簿」角色，Agent 在此查找可用服務與對應能力。例如 Notion 的 OpenAPI JSON 可被解析為 20+ 項細粒度能力 。 [youtube](https://www.youtube.com/)

關鍵概念：**能力轉譯層（Capability Translation Layer）**

### 7. Agent 身份與私鑰 [17:23]

每個 Agent 獲得專屬的私鑰，用於簽署 Token 並建立加密通訊。服務端不再只看到「某使用者互動」，而是能記錄「Cursor 的 Agent #abc123 代表使用者執行了此操作」。Agent 從隱藏在使用者背後，轉變為獨立的行為主體 。 [youtube](https://www.youtube.com/)

關鍵概念：**Agent 作為 Principal（Principal Actor）**

### 8. 三層架構、一個協議 [21:50]

| 層級 | 職責 | 技術實作 |
|------|------|----------|
| Server 端 | 驗證 Agent、核發 Grants、強制約束 | Agent Auth Plugin |
| SDK 端 | 為 Agent 生成金鑰、管理身份 | 搭載 MCP 整合 |
| Directory | 匹配意圖與能力 | 類似電話簿的服務目錄 |

Server 驗證 Agent 身份與使用者策略；SDK 建立金鑰並指派給 Agent；Directory 將使用者意圖映射到具體 Capabilities 。 [youtube](https://www.youtube.com/)

關鍵概念：**三層分離架構（Three-Layer Separation）**

### 9. Live Demo：Device Flow 授權 [23:07]

示範將 Agent Auth MCP 連接至 Claude，Agent 以 Device Flow（如同連接新設備）請求能力。Agent 名為 "Email Reader"，僅請求讀取郵件的能力。使用者可逐項批准、拒絕或設為「永久拒絕」。 [youtube](https://www.youtube.com/)

關鍵概念：**Device Authorization Grant**

### 10. 稽核日誌與即時追蹤 [26:17]

Demo 展示 Agent 執行後的完整稽核日誌：包含 Agent ID、所在 Host、關聯的 User ID，以及執行了哪些操作、取得哪些結果。所有日誌按 Provider 分割，可精確追蹤每個 Agent 的行為 。 [youtube](https://www.youtube.com/)

關鍵概念：**全生命週期可追蹤性（Full Lifecycle Traceability）**

### 11. 細粒度權限與動態授予 [27:56]

Agent 預設僅有讀取能力。當使用者要求「發送郵件」時，Agent 缺乏發送能力，因此觸發 CIBA（Client Initiated Backchannel Authentication）流程，向使用者請求額外授權。使用者批准後，發送郵件的能力被動態授予 。 [youtube](https://www.youtube.com/)

關鍵概念：**動態能力授予（Dynamic Capability Granting）**

### 12. 即時撤銷 [29:32]

示範撤銷 Agent 身份：撤銷後 Agent 無法再存取任何服務。Agent 嘗試讀取郵件時被拒絕，因為其 Token 已失效。Host 會自動建立新的 Agent 身份（因為 `list` 是預設安全能力），但敏感操作（如發送郵件）仍需重新授權 。 [youtube](https://www.youtube.com/)

關鍵概念：**即時撤權（Instant Revocation）**

### 13. 約束條件與策略控制 [31:48]

Capabilities 可嵌入多種約束條件：

- 最大執行時間限制
- 執行次數限制
- Host 層級策略（如 Claude 可執行所有操作）
- 使用者層級策略（如新加入的 Agent 僅有特定權限）

系統在安全與使用者體驗之間取得平衡——不會每次讀取都要求批准，但敏感操作必須確認 。 [youtube](https://www.youtube.com/)

關鍵概念：**策略層級控制（Policy-Level Control）**

### 14. 核心啟示 [37:08]

> 我們必須停止將憑證交給 Agent，改為授予權限。停止說「假扮我」，改為說「在這些限制內為我行事」。 [youtube](https://www.youtube.com/)

關鍵概念：**權限取代憑證（Authority over Credentials）**

## [結論與行動建議]

**啟發金句：**

> 「停止給 Agent 你的鑰匙，給它們一張有你簽名的通行證——上面寫清楚能去哪裡、能做什麼、何時失效。」

**具體行動法則 — A-R-C 法則：**

- **A**uthority（權限）：給 Agent 權限，不給憑證
- **R**evocable（可撤銷）：確保每個 Agent 都有獨立身份，可隨時撤銷
- **C**apability-based（能力導向）：用細粒度 Capability 取代粗粒度 Scope

**生活實踐建議：**

在日常開發 AI Agent 應用時，套用「雇用新員工」思維：你會給新員工一張專屬門禁卡並設定可進入的樓層，而非把大樓主管的萬能鑰匙交給他。同理，為每個 Agent 配置獨立身份、預設最小權限、設定敏感操作的二次確認流程。即使是個人專案，也應避免直接將 OAuth Token 注入 Agent，改用 Agent Auth 的 MCP SDK 管理身份與能力，建立從開發階段就內建安全意識的習慣。

## [參考連結]

- 原始影片：[https://youtu.be/JvKO40CFq-s](https://youtu.be/JvKO40CFq-s) [youtube](https://www.youtube.com/)
- Better Auth：[https://www.better-auth.com](https://www.better-auth.com)
- Agent Auth Protocol Discord：透過影片中 QR Code 取得
