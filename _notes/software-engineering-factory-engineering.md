---
title: '軟體工程正在變成工廠工程'
date: 2026-09-28
image: /images/影片筆記/software-engineering-factory-engineering.jpg
category: 影片筆記
tags: [軟體工廠, 規格驅動開發, 資料平面, 技能迴圈, 後設工程]
description: 'Warp 創辦人 Zach Lloyd（前 Google Docs 首席工程師）提出核心論點：軟體工程正在從「手寫程式碼」轉變為「工廠工程」（Factory E...'
quote: '💡你不只是在建產品，你是在建造那個建造產品的東西——所有人都會寫更少的程式碼，但會交付更多的產品。'
action: '🎯依「I-T-S-M 法則」打造軟體工廠：Inputs 定義工作入口、Triage 先建分診 Agent、Spec 走雙規格由人類審規格、Monitor + Measure 持續監控並衡量產出效率。'
source_has_timestamps: true
---
# Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp

[核心摘要]  
Warp 創辦人 Zach Lloyd（前 Google Docs 首席工程師）提出核心論點：軟體工程正在從「手寫程式碼」轉變為「工廠工程」（Factory Engineering）。每個具規模的專案都會擁有一座「軟體工廠」——由 Agent 自動執行分診、規格撰寫、實作、審查、驗證與監控，人類只在關鍵節點介入。工程師的角色從寫程式碼，變成設計與調校這座「生產產品的機器」。他本人六個月未寫一行程式碼，卻比以往更快地交付產品 。[[support.google](http://support.google)]

[詳細重點整理]

### 1. 講者背景與開發正從互動走向自動化 [00:00]

Zach Lloyd 擁有 20 年以上工程資歷，曾任 Google Doc Suite 工程負責人。Warp 起家於終端機，現為開源 Agentic 開發環境，擁有超過 60,000 GitHub stars、800,000 活躍開發者。他仍頻繁交付產品，但過去六個月未寫任何一行程式碼。  
開發演進三階段：聊天/自動補全（Copilot、Cursor）→ 互動式 Agent（Claude Code、Warp）→ 自動化。未來 6 至 12 個月將大幅轉向全流程自動化。現場調查顯示：所有人都在用 Agent、幾乎所有人同時操作多個 Agent，但少於半數在雲端執行、僅少數人已自動化完整軟體開發生命週期（SDLC）。  
關鍵概念：**互動式 Agent → 自動化（Interactive Agents → Automation）**

### 2. 軟體工廠的核心迴圈 [03:40]

軟體工廠本質上就是 SDLC 的大迴圈：想法進入 → Agent 分診 → 複雜任務寫 Spec → 人類審 Spec → Agent 實作 → 人機共同 Code Review → Agent 驗證 → 人類審產品 → 出貨 → 監控 → 回饋至頂端。藍色方塊代表人類介入點。工程師未來的工作就是建造與管理這些工廠。  
關鍵概念：**軟體工廠迴圈（Software Factory Loop）**

### 3. 開源動機：建造公開工廠 [04:50]

Warp 封閉開發五年後開源，主因是想建立 [build.warp.dev](http://build.warp.dev)——一個公開展示所有 issue 流動狀態、Agent 與貢獻者工作情況的網站，是一座「原型工廠」的規模化實踐，運作不完美但確實可行。  
關鍵概念：**公開工廠（Public Factory）**

### 4. 軟體變得便宜且易於複製 [05:35]

軟體建構成本大幅下降的直接推論是：軟體被複製變得極為容易。當建軟體免費時，純靠產品建立軟體事業非常困難——你需要產品之外的優勢：分銷渠道、生態系、品牌、數據護城河或資本。但新創公司缺乏這些優勢，突圍方法之一就是公開建設（Build in the Open）：建立生態系、提升品牌、創造社群，甚至「從被 Hacker News 仇恨到被容忍」。  
關鍵概念：**複製摩擦消失（Trivial to Clone）**

### 5. 用自動化馴服開源的傳統痛點 [07:35]

開源的傳統痛苦——大量雜訊 issue、草率 PR、Code Review 地獄、耗時的變更驗證——如今可被自動化管理。Warp 正是先圍繞開源專案建好整套軟體工廠自動化，才敢做出開源的決定。開源本身沒有特殊性，每個有規模的專案都能受益；他預測每家公司、每個開源專案核心都會有一座軟體工廠，就像 CI/CD 十年前變成理所當然一樣。  
關鍵概念：**自動化護城河（Automation Taming Open Source Pain）**

### 6. 有效軟體工廠的四大組成 [08:25]

1. 一組自動化；2. 提供上下文與技能（Context and Skills）的方式；3. 在正確時機引入人類（當流程卡住時）；4. 自我改進能力（Loops）。做對了，開源世界會變成「Agent 幫助貢獻者貢獻、幫助維護者維護」。  
關鍵概念：**人機介入時機（Human-in-the-Loop Timing）**

### 7. 工廠導覽：輸入、分診、規格、實作、審查、驗證、監控 [09:25]

工廠底層是一張步驟圖（Graph），幾乎每個產品都長得很像。各站點細節：

- **輸入（Inputs）\[09:25\]**：想法來自團隊與使用者，透過 Task Tracker、Slack、終端機/IDE、監控系統等通道進入工廠。
- **分診（Triage）\[10:25\]**：Agent 檢視進來的 issue——簡單且無歧義就直接實作（這是啟動工廠最快的方式）。
- **產品規格與技術規格（Product Spec / Tech Spec）\[10:50\]**：困難任務交給 Agent 產生雙規格——Product Spec 描述產品不變量（Invariants），Tech Spec 描述架構與程式碼形狀。
- **實作與審查（Implementation and Review）\[11:20\]**：實作是雲端執行的 Coding Agent 產出 diff；審查是最痛的一環——先讓 Agent 做 Code Review，再逐步演變成「何時引入人類」的風險管理練習。
- **驗證（Verification）\[11:55\]**：包含 Computer Use——讓電腦實際操作 Agent 產出的 UI 並錄製影片與截圖；CI/CD 照用。
- **監控（Monitoring）\[12:15\]**：Agent 在出貨後不停止——觀察是否當機、是否被使用，並回饋到工廠頂端形成閉環。  
關鍵概念：**規格驅動開發（Spec-Driven Development）**

### 8. Build or Buy？工廠的架構分層 [12:30]

每個人都會部署某種工廠，但「調校工廠」（這些技能是否適合我的領域）才是真正的工程挑戰。多數組織應專注於自己的核心產品而非自建基礎設施——簡單版容易建，可規模化版本極其複雜（Uber 已建立內部版本）。  
完整工廠架構分四層：輸入層 → 控制平面（Control Plane，決定工作如何分發）→ 執行層（Cloud Sandboxes、選擇 Harness 與模型）→ 資料平面（Data Plane，讓 Agent 記住做過什麼、學習、隨時間改進）。  
關鍵概念：**資料平面（Data Plane）**

### 9. 測量與改進：技能迴圈 [13:50]

工廠不只是產品，更是心態（Mindset）。必須衡量效率：出貨了多少軟體？花費多少人類時間與 Token 時間？並持續改進。  
**技能迴圈（Skill Loop）**：工廠 Agent 執行技能，觀察 Agent（Observer Agents）監看技能如何被應用、找出問題並改進技能。例：Code Review Agent 留下註解、資深工程師修正這些註解，觀察 Agent 分析這些修正並讓 Code Review Agent 下次表現更好。  
關鍵概念：**技能迴圈（Skill Loop）**

### 10. 工程師的新定位 [15:10]

心態轉變：「你不只是在建產品，你是在建造那個建造產品的東西。」這更接近製程工程或製造業。若你的樂趣在寫程式碼——所有人都會寫得更少；若你的樂趣在交付產品——這是最好的時代。所有人都會寫更少程式碼、交付更多產品。這是一種 **後設工程（Meta-Engineering）**：如何把你的 Agent 系統工程化到最擅長做工程。

### 11. 入門 Repo 與 Q&amp;A [16:35]

提供開源 GitHub Repo（使用 Warp Agent 平台，但不強制）讓任何人嘗試建立自己的工廠 Agent——從分診 Agent 到 Spec 撰寫 Agent 的實作起點。  
Q&amp;A 三問：

- **Build vs. Buy \[17:20\]**：人人都會部署工廠，但領域調校（Skills 是否適配）仍是核心工程挑戰。
- **給新鮮人的建議 \[18:15\]**：新世界最重要的技能是適應力、批判性思考、學習速度；理解底層系統與架構、能讀懂 Agent 寫的 Spec 仍有巨大價值。Warp 正在史上最大規模招募，尋找「適應力強、產品導向的思考者」。
- **品味與產品感 \[19:30\]**：工廠比喻的風險是聽起來機械化、去人性化，但唯一重要的是「你是否在建有用的東西」。一座產出沒人關心產品的工廠毫無意義——**人類品味、產品感、人類在無法自動化的觸點上的引導是絕對必要的**。

[結論與行動建議]

**啟發金句**：「你不只是在建產品，你是在建造那個建造產品的東西——所有人都會寫更少的程式碼，但會交付更多的產品。」

**具體行動建議——「I-T-S-M 法則」**：打造你的軟體工廠，依序完成四件事：

- **I**nputs：定義工作入口（Issue Tracker / Slack / IDE / 監控）
- **T**riage：先建一個「簡單任務直接實作」的分診 Agent——這是啟動成本最低的第一步
- **S**pec：困難任務走 Product Spec + Tech Spec 雙規格，人類審規格而非審程式碼
- **M**onitor + Measure：出貨後持續監控回饋頂端，並衡量「出貨量 ÷（人類時間 + Token 成本）」

**生活實踐建議**：對於正在探索 Gitea + MCP + Actions + LLM Gateway + Webhooks 工作流的自架開發者，這支影片給出的最直接啟發是——不要只把這些工具當作「輔助開發」，而是把它們串成一座完整的工廠：用 Webhook 收 issue 做輸入層、用 Agent 做 Triage、用 Spec-driven 開發取代直接下指令寫 Code、用 CI/CD + 截圖驗證做 Verification、用 MCP 資料平面讓 Agent 累積記憶。從最小可行版本開始（一個分診 Agent），而非一步到位。

[參考連結]

- 原始影片：[https://youtu.be/tUPPVhBBcoM](https://youtu.be/tUPPVhBBcoM)
- Warp：[https://www.warp.dev](https://www.warp.dev)
- Warp 公開工廠：[https://build.warp.dev](https://build.warp.dev)

