---
title: 'MCP 伺服器安全治理：三層架構的統一控制平面'
date: 2026-06-04
image: /images/AI筆記/mcp-unified-control-plane.jpg
category: AI筆記
tags: [MCP治理, 安全稽核, 沙箱隔離, 企業架構, Agent風險]
description: '隨著 AI Agent 大規模導入企業，MCP 伺服器的安全治理成為迫切痛點。解方是三層架構：MCP Gateway（管控層）+ 沙箱（OS 層隔離）+ 輕鬆部署，缺一不可。'
quote: '安全必須在 Agentic 表面之外強制執行，而不是依賴 Agent 本身的行為正確性。— Nanocloud 創辦人'
action: '建立 MCP Gateway 白名單、為每個 Agent Session 設沙箱隔離、選用能整合既有 Stack 的方案以降低落地阻力'
source_has_timestamps: true
---
## [核心摘要]

隨著 AI Agent 大規模導入企業，**MCP 伺服器的安全治理**成為迫切痛點。Docker PM Cecilia Liu 以兩個真實恐怖故事揭示：無論是未審核的 MCP 安裝還是過度自主的 Agent，後果都已在企業中真實發生。解方是三層架構：**MCP Gateway（管控層）+ 沙箱（OS 層隔離）+ 輕鬆部署**，缺一不可。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [詳細重點整理]

### 1. 恐怖故事一：未授權的 MCP 伺服器 [00:30]

一名實習生加入新公司後，自行上網搜尋 MCP Server 以提升生產力，找到看起來「很正規」的伺服器便直接安裝使用。整個過程無任何審核、無審計日誌。三週後，安全團隊發現程式碼庫與 API 金鑰外洩，但由於完全沒有紀錄，無從追查。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：無審計軌跡的供應鏈風險（Supply Chain Attack Without Audit Trail）**

### 2. 恐怖故事二：過度自主的 Agent [01:50]

一位資深開發者使用公司**已核准**的 GitHub MCP Server，要求 Agent「清理 repo」。因為開發者完全信任自主執行，Agent 依照許可工具清單，合併所有 open PR、刪除分支、關閉 issue，結果未推送的本地工作進度全數消失。**沒有任何惡意行為，卻造成無法挽回的損失。** [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：許可（Permitted）≠ 意圖（Intended）**

### 3. 企業必須回答的四個問題 [03:00]

當 AI 使用者已從「幾十人」擴展到「數百、數千人」的規模，問題不是「是否會發生」，而是「何時發生，以及你是否知道」。四個關鍵問題： [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

- **What is allowed**：哪些 MCP Server、哪些工具被允許使用？
- **Who is doing what**：誰、用什麼 Client、呼叫什麼工具、在何時？
- **What is flowing through**：是否有憑證或敏感資料外洩於模型上下文中？
- **What happened**：是否有完整的行為軌跡紀錄？

**關鍵概念：可觀測性缺口（Observability Gap）**

### 4. 三大防護要素：Control + Sandbox + Deploy [04:20]

三個必要元素缺一不可，構成完整的 MCP 治理架構： [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

- **MCP Gateway（管控層）**：坐落於 AI Agent 與 MCP Server 之間，所有流量強制流經此層，提供 Curated Catalog（精選目錄）、認證與 Secret 管理、細粒度存取政策、完整稽核日誌
- **Sandbox（沙箱層）**：在 OS 層而非應用層定義 Agent 能力上限；每個 Agent 擁有獨立容器，整體在 microVM 內執行，具備獨立核心與 Hypervisor 隔離；Nanocloud 創辦人金句印證：「安全必須在 Agentic 表面之外強制執行，不能依賴 Agent 本身的行為正確性」
- **輕鬆部署**：支援本地 / 遠端環境，相容既有 Identity Provider（Azure AD、Okta）、Secret Manager（AWS Secrets Manager）、可觀測性工具（Splunk、Datadog），支援單雲/多雲/地端/氣隙環境，一個 Helm 指令完成安裝

**關鍵概念：雙硬牆隔離（Two Hard Walls）**

### 5. 為何 Gateway 本身不夠？ [07:00]

Gateway 管控 Agent **被允許呼叫什麼**，但無法控制 Agent **實際會做什麼**。Agent 本質上是非確定性的（non-deterministic），因此治理必須延伸至應用層之下，即 OS 層的沙箱隔離。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：非確定性 Agent 風險（Non-Deterministic Agent Risk）**

***

## [技術/數據對比]

| 防護層級 | 管控範疇 | 解決的問題 |
|---|---|---|
| **MCP Gateway** | 應用層（哪些工具可用） | 未授權伺服器、憑證外洩、無稽核軌跡 |
| **Sandbox（microVM）** | OS 層（能做什麼最大值） | 過度自主刪除、跨 session 資料存取 |
| **部署適配** | 基礎設施層（與既有 Stack 整合） | 治理工具因導入困難而被放棄 |

***

## [結論與行動建議]

**💡 啟發金句：**
> **「安全必須在 Agentic 表面之外強制執行，而不是依賴 Agent 本身的行為正確性。」— Nanocloud 創辦人** [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**具體行動建議（C-S-D 法則）：**
- **C（Control）**：先建立 MCP Gateway，定義精選目錄，強制所有 Agent 流量流經管控層
- **S（Sandbox）**：在 OS 層為每個 Agent Session 建立獨立的 microVM 隔離環境
- **D（Deploy Easy）**：選用能整合既有 Identity、Secret、Observability Stack 的方案，降低落地阻力

**生活實踐建議（以 AI 應用架構師角度）：**

你在設計 AI-Powered 應用時，可立即採取以下行動： [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
1. **審核現有 MCP Server 清單**：盤點團隊目前使用的所有 MCP Server，建立白名單制度
2. **預設 Human-in-the-loop**：對於涉及寫入、刪除、推送的操作，設計明確的確認步驟，避免 fully autonomous 模式造成不可逆損失
3. **要求 Agent 沙箱化**：在架構設計時，要求每個 Agent Session 在隔離容器中執行，尤其是有存取本地檔案系統或 Git 操作的 Agent
4. **評估 Docker MCP Gateway**：參考開源 repo（[github.com/docker/mcp-gateway](https://github.com/docker/mcp-gateway)）進行 PoC，確認與現有 Azure AD / AWS 環境的整合性

***

## [參考連結]

- 🎬 原始影片：[https://youtu.be/2_2yQ_b9fgs](https://youtu.be/2_2yQ_b9fgs)
- 📦 Docker MCP Gateway 開源 Repo：[https://github.com/docker/mcp-gateway](https://github.com/docker/mcp-gateway)
- 📖 Docker MCP Gateway 文件：[https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/)
- 📝 MCP 恐怖故事系列部落格：[https://www.docker.com/blog/mcp-security-issues-threatening-ai-infrastructure/](https://www.docker.com/blog/mcp-security-issues-threatening-ai-infrastructure/)
