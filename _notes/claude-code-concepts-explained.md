---
title: 'Claude Code 27個核心概念全解析'
date: 2026-03-24
image: /images/影片筆記/claude-code-concepts-explained.jpg
category: 影片筆記
tags: [Claude Code, 脈絡管理, 子代理, 工作樹, MCP]
description: '將 Claude Code 從基礎安裝到進階自動化的 27 個核心概念，以淺顯易懂的語言拆解，幫助非技術背景的使用者也能高效操控這個強大的開發工具。'
quote: 'Chatbots 提供建議，Claude Code 採取行動。'
action: '從小處開始練習，善用 /re 指令復原，並開啟 LazyGit 追蹤 AI 對專案的改動。'
source_has_timestamps: true
---

這部影片 **《Every Claude Code Concept Explained for Normal People》** 是針對 Anthropic 推出的終端機 AI 工具 **Claude Code** 的全方位指南。

這部影片非常適合想利用 AI 進行開發，但又不具備深厚編程背景的人。以下為你整理的精華筆記：

---

### 核心摘要
這部影片將 **Claude Code** 從基礎安裝到進階自動化（如子代理與工作樹）的 **27 個核心概念**，以淺顯易懂的語言拆解，幫助非技術背景的使用者也能高效操控這個強大的開發工具。

---

### 詳細重點整理

#### 1. Claude Code 的本質與操作基礎
Claude Code 不只是聊天機器人，它是能直接在你的電腦上「執行動作」的代理人。
* **與一般 Chatbot 的區別：** ChatGPT 或網頁版 Claude 只能「說」，而 Claude Code 可以「做」（如建立檔案、安裝套件、架設資料庫）[[01:19](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=79)]。
* **終端機 (Terminal) 運作：** 它在黑底白字的指令介面運作，但你不需要背指令，直接用「白話英文」描述需求即可 [[01:53](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=113)]。
* **權限管理 (Permissions)：** 這是關鍵安全機制。你可以設定 `settings.json` 來「預先核准」安全動作（如讀取檔案、跑測試），並「攔截」高風險動作（如刪除檔案、API 調用）[[04:28](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=268)]。

#### 2. 記憶管理與脈絡維護 (Context Management)
AI 的「短期記憶」有限，學會管理脈絡能避免它產生幻覺或出錯。
* **脈絡視窗 (Context Window)：** 這是 Claude 的短期記憶。當對話太長會發生「脈絡腐爛 (Context Rot)」，導致表現下降 [[06:43](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=403)]。
* **壓縮指令 (`/compact`)：** 當記憶快滿時，可以使用此指令讓 Claude 總結重點並清空雜訊，保持思考清晰 [[11:05](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=665)]。
* **`claude.md` 專案手冊：** 在專案中建立此 Markdown 檔案，寫下你的偏好與規則（例如：必須使用 TypeScript），Claude 每次啟動都會先閱讀它 [[09:07](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=547)]。

#### 3. 進階協作：子代理與代理人團隊 (Agents & Teams)
當任務變得複雜時，Claude 會「分身」來提高效率。
* **子代理 (Sub-agents)：** 主代理會將任務委派給具有獨立記憶視窗的「專才」，避免主對話記憶過載，並提升準確度 [[18:21](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=1101)]。
* **代理人團隊 (Agent Teams)：** 這是更進階的功能，讓多個代理人（如 API 工程師與前端工程師）能直接溝通並共享任務清單，適合開發完整的軟體專案 [[19:54](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=1194)]。
* **工作樹 (Work Trees)：** 允許同時啟動多個 Claude 處理不同任務（如一個修 Bug、一個開發新功能），彼此互不干擾 [[25:20](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=1520)]。

#### 4. 自動化與擴充功能 (Skills & Hooks)
讓 Claude Code 變得更聰明且符合你的工作流。
* **技能 (Skills)：** 預寫的指令劇本，教導 Claude 如何執行特定專業任務（如撰寫文案、設計前端介面） [[16:02](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=962)]。
* **鉤子 (Hooks)：** 自動執行的腳本。例如：每當 Claude 儲存檔案，系統自動進行格式化，這不消耗任何 AI Token [[17:14](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=1034)]。
* **MCP 伺服器：** 透過「模型上下文協議 (MCP)」，讓 Claude Code 連結外部工具（如 Notion, Airtable, Asana），直接操作你的軟體堆疊 [[17:40](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=1060)]。

---

### 結論與行動建議

* **金句啟發：** 「Chatbots 提供建議，Claude Code 採取行動 (Chatbots give you advice, Claude Code takes actions)。」 [[01:36](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=96)]
* **具體建議：**
    1.  **從小處開始：** 不要一次給太大的指令，先從「建立一個簡單的登入頁面」開始練習。
    2.  **善用 `/re` 指令：** Claude 常會出錯，`/re`（重捲/復原）功能可以讓你回到程式碼出錯前的任何一個時間點 [[21:50](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=1310)]。
    3.  **付費模式選擇：** 影片建議對於中度使用者，選擇每月 $20 美金的 Pro 或更高階的 Max 方案比按量計費（API）更划算且省心 [[24:41](http://www.youtube.com/watch?v=ZlDnsf_DOzg&t=1481)]。
