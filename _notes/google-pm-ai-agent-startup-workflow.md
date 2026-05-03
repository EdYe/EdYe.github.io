---
title: 'Google PM 用 21 AI Agent 組建完整新創開發團隊'
date: 2026-05-03
image: /images/影片筆記/google-pm-ai-agent-startup-workflow.jpeg
category: 影片筆記
tags: [AI Agent, 系統分析師, 語音規格, 視覺接地, 機構知識]
description: 'Google PM Gabor Mayer 揭示了一套以 21個 Claude Code AI Agent 組建完整新創開發團隊的方法論，涵蓋系統分析師、設計師'
quote: 'Vibe Coding 只是難以維護的低品質程式碼的重新包裝。'
action: '先建立 Agent 鷹架與工具連接，用語音口述取代鍵盤輸入提升規格密度，每張前端 Ticket 必須附上視覺截圖。'
source_has_timestamps: true
---
以下是這部影片的結構化深度筆記：

***
# [核心摘要]
Google PM Gabor Mayer 揭示了一套以 **21個 Claude Code AI Agent** 組建完整新創開發團隊的方法論，涵蓋系統分析師、設計師、前端/後端工程師、法律顧問等角色。核心痛點在於：一次性大 Prompt 的 Vibe Coding 會導致上下文壓縮、規格細節靜默丟失，最終產出難以維護的低品質程式碼。透過分工細化的 Agent 團隊 + Confluence/Jira/Figma 工具鏈，可在數小時內將產品構想推進到 TestFlight。 [youtube](https://www.youtube.com)

***
# [詳細重點整理]
## 1. 21-Agent 新創作業系統架構 [00:00–04:57]
Gabor 建立了一個涵蓋完整公司職能的 Agent 團隊，每個 Agent 有獨立的 Markdown 定義文件，存入 Claude Code 的 project memory： [youtube](https://www.youtube.com)

- **System Analyst Agent**（系統分析師）：最核心的 Agent，逐一提問釐清需求、記錄決策至 Confluence、建立 Jira Ticket 的依賴關係圖
- **CTO Agent**：負責高層次技術架構決策
- **Design Agent**：執行 UI/UX 視覺設計方向
- **Spaghetti Agent（程式碼維護 Agent）**：檢查命名慣例、循環引用、注解品質，防止 Vibe Coding 變成難以維護的義大利麵程式碼
- **Product Council Agent**：審查資料儲存方式與資安設計
- **Test Architect Agent**：設計測試品質保障機制
- **UX Flow Architect**：設計可點擊原型流程

**關鍵概念：Agent 化分工（Agentified Division of Labor）** [youtube](https://www.youtube.com)

***
## 2. System Analyst Agent 的運作邏輯 [05:52–15:30]
不同於直接給 AI 一個巨型 Prompt，正確流程是要求 Agent 在撰寫任何文件或程式碼之前，**一次只問一個澄清問題**： [youtube](https://www.youtube.com)

> 「Please ask clarifying questions one at a time because I might get overwhelmed if you ask too many questions at once.」

Agent 整合 **Atlassian MCP**，直接將決策記錄寫入 Confluence、在 Jira 建立對應 Ticket，確保所有規格可被複製並形成可維護的文件基礎。

**關鍵概念：上下文鷹架（Context Scaffolding）** [youtube](https://www.youtube.com)

***
## 3. 語音口述取代鍵盤輸入 [35:29–47:30]
使用 **Super Whisper** 等語音轉文字工具，以語音口述方式輸入產品規格，可比鍵盤輸入多產出約 **5倍以上的規格細節**： [youtube](https://www.youtube.com)

> 「即使我說話不夠精確，AI 也會自行理解與詮釋——口述的資訊密度遠高於打字。」

示範中，Gabor 用一段長達數分鐘的語音口述，涵蓋了技術棧（Flutter + Firebase）、向量嵌入資料庫設計、Token 使用限制（24小時 20,000 字上限）、API Key 安全儲存策略等完整規格，這在純鍵盤輸入時極難實現。

**關鍵概念：語音驅動規格（Voice-Driven Specification）** [youtube](https://www.youtube.com)

***
## 4. Figma Make → Jira Ticket → Claude Code 完整工作流 [47:30–1:23:59]
完整的「從 0 到 TestFlight」工作流順序如下： [youtube](https://www.youtube.com)

1. **Claude App（語音）** → 系統分析師 Agent 逐問確認需求
2. **Confluence** → 存入產品規格文件
3. **Figma Make** → 依視覺方向生成 UI 設計稿
4. **Claude Code** → 讀取 Figma 截圖並依設計稿生成前端程式碼
5. **Jira** → 自動建立前端 Epics 與帶 Figma 連結的 Ticket
6. **模擬器驗證** → 推送至 **TestFlight**

> 重點提醒：每張前端開發 Ticket **必須附上 Figma 截圖**，否則 AI 會預設生成通用 AI 審美風格，無法呈現品牌設計。

**關鍵概念：視覺接地（Visual Grounding）** [youtube](https://www.youtube.com)

***
## 5. Sprint 組織與依賴關係管理 [1:23:59–1:53:56]
Atlassian MCP 目前不完整支援 Sprint 功能，Gabor 以 **Tag 標籤作為替代方案** 進行依賴映射。沒有依賴管理，Agent 可能在尚不存在的程式碼上堆疊功能，導致建構順序錯亂。 [youtube](https://www.youtube.com)

Agent 的每次迭代教訓與 API Workaround 都保存在 Agent 的 Markdown 文件中，使下一個專案從既有知識積累出發，而非從零開始。

**關鍵概念：機構知識沉澱（Institutional Knowledge Encoding）** [youtube](https://www.youtube.com)

***
# [技術/數據對比]
| 維度 | 一次性 Vibe Coding | Gabor 的 21-Agent 系統 |
|---|---|---|
| 規格產出方式 | 單一大 Prompt | 系統分析師逐問 + 語音口述 |
| 文件管理 | 無 | Confluence（MCP 自動寫入） |
| Ticket 管理 | 無 | Jira（自動建立 + 依賴映射）|
| 設計輸入 | 文字描述 | Figma 截圖附至每張 Ticket |
| 程式碼品質把關 | 無 | Spaghetti Agent 自動審查 |
| 知識積累 | 每次從零 | Agent MD 文件累積迭代學習 |
| 最終輸出 | 原型或錯誤百出的 App | TestFlight 可測試的正式 App | [youtube](https://www.youtube.com)

***
# [結論與行動建議]
**💡 啟發金句：**
> **「Vibe Coding 只是難以維護的低品質程式碼的重新包裝。」**（Vibe coding is just the rebranding of unmaintainable low-quality source code.） [youtube](https://www.youtube.com)

**具體行動建議：S-D-V 法則**
- **S（Scaffold First）**：先建立 Agent 鷹架與工具連接（Confluence + Jira），再開始構建
- **D（Dictate, Don't Type）**：用語音口述取代鍵盤輸入，提升規格密度 5 倍
- **V（Visualize Every Ticket）**：每張前端 Ticket 必須附上視覺截圖，確保設計意圖落地

**生活實踐建議：**
- 作為 AI-Powered 應用架構師，可直接採用此工作流替代傳統 PRD 撰寫流程——先在手機 Claude App 上用語音口述產品構想（遛狗時、通勤時皆可），讓系統分析師 Agent 自動整理成 Confluence 文件與 Jira Ticket，大幅壓縮從構想到開發啟動的時間 [youtube](https://www.youtube.com)

***
# [參考連結]
- 原始 YouTube 影片：[https://youtu.be/kQelqKkI-EQ](https://youtu.be/kQelqKkI-EQ) [youtube](https://www.youtube.com)
- 完整文字版：[https://www.news.aakashg.com/p/claude-code-dev-team](https://www.news.aakashg.com/p/claude-code-dev-team) [youtube](https://www.youtube.com)
- Gabor 的 Maven 課程（PM to AI Builder）：[https://maven.com/gabor/productbuilder](https://maven.com/gabor/productbuilder) [youtube](https://www.youtube.com)
