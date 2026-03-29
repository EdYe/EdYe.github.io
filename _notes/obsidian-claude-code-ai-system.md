---
title: 'Obsidian結合Claude Code打造AI系統'
date: 2026-03-29
image: /images/影片筆記/obsidian-claude-code-ai-system.jpeg
category: 影片筆記
tags: [Obsidian, Claude Code, AI作業系統, 知識管理, 自動化路由]
description: '將Claude Code嵌入Obsidian筆記軟體，克服AI缺乏長期記憶的缺點，建構出能自動處理任務、管理知識且具備「大腦」功能的個人AI作業系統'
quote: 'Claude Code很出色，但如果沒有家，它就像是一個患有失憶症的天才。'
action: '從建立一個簡單的Obsidian Vault並連結終端機開始，嘗試用/init讓AI認識你的工作流程'
source_has_timestamps: true
---

這是一份關於如何將 **Claude Code** 與 **Obsidian** 結合，打造一個強大 AI 作業系統的深度筆記整理。

---

### **核心摘要**
本影片教學如何透過將 Anthropic 的 **Claude Code (終端機介面 AI)** 嵌入 **Obsidian** 筆記軟體，克服 AI 缺乏長期記憶的缺點，並解決數位筆記難以整理的痛點，建構出一個能自動處理任務、管理知識且具備「大腦」功能的個人 AI 作業系統。

---

### **詳細重點整理**

#### **1. 為什麼要結合 Claude Code 與 Obsidian？**
* **解決 Claude Code 的健忘症：** AI 雖然強大，但每次開啟新對話都會遺失先前的專案背景與決策。Obsidian 提供了一個穩定的「本地數據庫」，讓 AI 擁有持續性的記憶 [[00:43](http://www.youtube.com/watch?v=eIXheJcxDIg&t=43)]。
* **賦予 Obsidian 一位「管理員」：** 傳統筆記軟體常讓人花過多時間在手動分類與搜尋。透過 Claude Code，你可以直接用對話方式讓 AI 幫你歸檔、路由與組織文件 [[02:11](http://www.youtube.com/watch?v=eIXheJcxDIg&t=131)]。
* **本地化與靈活性：** 所有的數據都存在你的電腦（Markdown 格式），即便未來更換 AI 模型，這套系統與資料依然屬於你 [[13:28](http://www.youtube.com/watch?v=eIXheJcxDIg&t=808)]。

#### **2. 系統搭建步驟 (Step-by-Step)**
1.  **安裝 Obsidian：** 至官網下載並建立一個新的儲存庫 (Vault) [[02:25](http://www.youtube.com/watch?v=eIXheJcxDIg&t=145)]。
2.  **安裝必要插件：**
    * **Terminal：** 在 Obsidian 內開啟終端機介面 [[03:22](http://www.youtube.com/watch?v=eIXheJcxDIg&t=202)]。
    * **Templater：** 用於自動化模板 [[03:33](http://www.youtube.com/watch?v=eIXheJcxDIg&t=213)]。
    * **Web Viewer：** 讓你在筆記軟體內直接瀏覽網頁 [[03:39](http://www.youtube.com/watch?v=eIXheJcxDIg&t=219)]。
3.  **外觀與環境設定：** 推薦安裝 **PLN 主題** 獲得彩色側邊欄，並安裝 Claude Code 於電腦中（需透過 Anthropic 官方文檔指引完成登入）[[04:14](http://www.youtube.com/watch?v=eIXheJcxDIg&t=254)]。
4.  **啟動與初始化：** 在 Obsidian 的終端機輸入 `claude` 啟動，接著使用 `/init` 指令建立 `claude.md`，讓 AI 掃描並熟悉你的筆記庫結構 [[05:06](http://www.youtube.com/watch?v=eIXheJcxDIg&t=306)]。

#### **3. 腦部架構設計：人機協作模型**
* **人類 hemisphere (左腦)：** 存放個人想法、日記、原始任務。設定為 AI 可讀取但除非獲得指令否則不可寫入，以保留人類的原始聲音 [[08:06](http://www.youtube.com/watch?v=eIXheJcxDIg&t=486)]。
* **機器 hemisphere (右腦)：** 存放 AI 產出的研究成果、標準作業程序 (SOP)、程式碼與自動化工作流 [[08:23](http://www.youtube.com/watch?v=eIXheJcxDIg&t=503)]。
* **自動化路由：** 透過自定義指令（如 `/new`），AI 會根據你碎碎念的內容（例如：今天喝了四杯咖啡、要做某個專案），自動將資訊分發到正確的資料夾或日誌中 [[10:14](http://www.youtube.com/watch?v=eIXheJcxDIg&t=614)]。

#### **4. 高效率工作流實例**
* **每日開局 (`/today`)：** AI 會掃描你的信箱、行事曆與昨日筆記，自動產出今日的待辦清單，並提醒你最該優先處理的任務 (Eat the Frog) [[11:14](http://www.youtube.com/watch?v=eIXheJcxDIg&t=674)]。
* **開發與自動化：** 影片展示了如何在同一個視窗內完成冷啟動開發 (Cold Email Pipeline)，從抓取資料到驗證、執行，完全不需切換視窗 [[12:17](http://www.youtube.com/watch?v=eIXheJcxDIg&t=737)]。
* **內容研究 (`/comments`)：** 自定義指令讓 AI 直接讀取 YouTube 留言並分析趨勢，自動產生下一部影片的靈感 [[13:03](http://www.youtube.com/watch?v=eIXheJcxDIg&t=783)]。

---

### **結論與行動建議**
* **金句啟發：** 「Claude Code 很出色，但如果沒有家，它就像是一個患有失憶症的天才。」
* **核心建議：** 數位生產力的終點不在於使用更多工具，而在於「減少切換」。將 AI 放入你的筆記軟體，讓它從一個「外部顧問」變成你的「內部圖書館管理員」。
* **下一步行動：** 建議從建立一個簡單的 Obsidian Vault 並連結終端機開始，嘗試用 `/init` 讓 AI 認識你的工作流程。