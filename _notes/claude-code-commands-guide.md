---
title: 'Claude Code 指令全解析與應用'
date: 2026-03-19
image: /images/影片筆記/claude-code-commands-guide.jpg
category: 影片筆記
tags: [Claude Code, AI工具, 命令行開發, MCP, 生產力]
description: '這部影片是 Claude Code 的全指令百科全書，教你如何透過命令行工具極大化 AI 輔助編程的生產力。'
quote: 'Claude Code 指令非常強大，能幫你從最初的系統設定一路管到整個 Agent 團隊。'
action: '安裝後第一步務必執行 /init 並認真填寫 claude.md，讓 AI 輸出更符合需求。'
source_has_timestamps: true
---

這部影片由 AI 自動化專家 Duncan Rogoff 製作，詳盡地介紹了 **Claude Code**（Anthropic 推出的命令行 AI 工具）中幾乎所有的指令，並依據實用程度將其分為 10 個等級，旨在幫助開發者從初學者晉升為高效率的 Power User。

### 核心摘要
這部影片是 Claude Code 的全指令百科全書，教你如何透過命令行工具極大化 AI 輔助編程的生產力。

---

### 詳細重點整理

#### 1. 入門必備：環境設定與診斷 (Tier 1)
這是每位使用者初次執行時最關鍵的步驟，確保系統運行無誤。
* **`/login`**：驗證你的 Anthropic 帳號以開始使用。[[01:00](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=60)]
* **`/doctor`**：自動診斷安裝環境，找出任何潛在的損壞或配置問題。[[01:11](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=71)]
* **`/init` (初始化)**：**最重要指令**。建立 `claude.md` 檔案，讓 Claude 擁有專案的持久背景記憶（例如：慣用語言、資料夾規範、命名偏好等）。[[01:17](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=77)]
* **`/config` 或 `/settings`**：設定佈景主題（深/淺色）、預設 AI 模型及輸出偏好。[[01:46](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=106)]

#### 2. 工作流管理：模型切換與上下文優化 (Tier 2-3)
學會管理對話的「記憶」與「成本」，是成為高手的分水嶺。
* **`/model`**：可在對話中途隨時切換模型。建議：簡單任務用 Haiku（便宜快速）、一般開發用 Sonnet（平衡點）、複雜邏輯用 Opus。[[02:36](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=156)]
* **`/compact`**：壓縮對話歷史以節省上下文空間（Context Window），而非直接清空記憶。[[03:30](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=210)]
* **`/plan`**：進入「規劃模式」，讓 Claude 在動手寫代碼前先思考並與你討論方案，避免浪費 Token。[[03:56](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=236)]
* **`/fork`**：分支當前對話，嘗試不同的解決路徑而不互相干擾。[[04:36](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=276)]
* **`/btw`**：在 Claude 工作時插嘴問一個無關的小問題，不影響主對話流程。[[06:04](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=364)]

#### 3. 進階開發與安全自動化 (Tier 4-6)
利用插件與外部工具擴展 Claude 的能力邊界。
* **MCP (Model Context Protocol)**：連接第三方工具（如 Notion, Slack, Google Drive），讓 Claude 存取外部數據。[[06:41](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=401)]
* **`/security-review`**：掃描代碼中的漏洞或外洩的密碼，建議在 Merge 程式碼前必跑一次。[[05:13](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=313)]
* **`/loop`**：設定間隔時間重複執行指令（如每 5 分鐘檢查一次部署進度或測試結果）。[[07:23](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=443)]
* **`/simplify`**：啟動三個平行 Agent 來優化代碼質量、速度或記憶體佔用。[[05:33](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=333)]

#### 4. 個人化與環境整合 (Tier 7-9)
優化你的開發環境感受與跨裝置體驗。
* **`/theme` 與 `/color`**：自定義終端機的配色與提示列顏色。[[10:29](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=629)]
* **`/desktop`**：將目前的終端機會話轉移到 Claude Desktop 桌面應用程式繼續進行。[[09:57](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=597)]
* **`/stats` 與 `/insights`**：視覺化你的使用模式、Token 消耗量與摩擦點分析。[[11:01](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=661)]
* **`/stickers`**：一個有趣的彩蛋指令，可以用來訂購 Claude Code 的實體貼紙。[[13:24](http://www.youtube.com/watch?v=6TNZKtlF2p4&t=804)]

---

### 結論與行動建議

* **金句啟發**：「Claude Code 指令非常強大，能幫你從最初的系統設定一路管到整個 Agent 團隊。」
* **具體建議 (Step-by-Step)**：
    1.  安裝後第一步務必執行 `/init` 並認真填寫 `claude.md`，這會讓 AI 輸出的代碼風格更符合你的需求。
    2.  養成開發前先 `/plan`、開發後先 `/security-review` 與 `/simplify` 的習慣，能有效減少 Debug 時間。
    3.  若專案變大導致 AI 變笨，優先使用 `/compact` 而非 `/clear`。
