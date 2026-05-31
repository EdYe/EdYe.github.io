---
title: '廉價軟體讓 PM 的工作更難了：軟體豐盛時代的治理挑戰'
date: 2026-05-31
image: /images/AI筆記/cheap-software-pm-job-harder.jpg
category: AI筆記
tags: [產品判斷力, 軟體豐盛, 殭屍產品, 生產等級梯, 治理]
description: 'AI 壓低了軟體建造成本，讓「原型」無處不在，但這反而讓 Product Manager 的真正瓶頸從「能不能建」轉移到「該不該依賴」。PM 的新核心職能是對「軟體豐盛時代」進行分類與治理——哪些留下、哪些晉升至生產、哪些應該主動淘汰'
quote: 'We can build everything. What should we build?——這才是 AI 時代 PM 的真正問題。'
action: '每季進行原型公域普查，在 Sprint Planning 中加入降級議程，培養能看見真正產品的技術判斷力'
source_has_timestamps: true
---
## [核心摘要]

AI 壓低了軟體建造成本，讓「原型」無處不在，但這反而讓 **Product Manager 的真正瓶頸從「能不能建」轉移到「該不該依賴」**。影片提出，PM 的新核心職能是對「軟體豐盛時代」進行分類與治理——哪些留下、哪些晉升至生產、哪些應該主動淘汰——而非只是加速原型開發。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

***

## [詳細重點整理]

**1. 原型能力只是基本門票 [00:00]**

AI 讓 PM 能用 Lovable、Claude Code、Codex 快速原型化，這已是業界共識。然而這只是「入場券」，並非 PM 的核心競爭力所在。真正的挑戰在於：AI 把瓶頸從「生產」移到了「判斷」。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

> **關鍵概念：軟體生產瓶頸位移（Bottleneck Shift）**

***

**2. Microsoft 百萬資產的現實警鐘 [01:14]**

Microsoft 內部 Power Platform 已建立超過 **100 萬個資產**，包含 18,000+ 個 Agent 環境、170,000 個 Power Apps、50,000 個自動化流程、1,200 個聊天機器人。這意味著「artifact 先到、需求後到」——PM 收到的不再是請求，而是一個已在運行的工具。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

> **關鍵概念：軟體豐盛（Software Abundance）**

***

**3. 非技術型 PM 的生存空間正在消失 [02:30]**

AI 產品本質上是技術系統，其行為高度由技術細節決定：模型行為、Agent 迴圈、資料存取邊界、RAG 檢索、Latency、Cost、權限與失敗模式。一個無法對這些因素進行推理的 PM，實際上「看不見真正的產品」。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

> **關鍵概念：技術產品判斷力（Technical Product Judgment）**

***

**4. 舊 PM 過濾器的崩潰 [03:45]**

傳統 PM 流程（PRD、Roadmap Review、Launch Checklist）的設計前提是「工程時間昂貴」，PM 是稀缺資源的守門人。但當任何人都可以在正式流程介入前就產出「半真實產品（Zombie Products）」，過濾器的邏輯便失效了。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

> **關鍵概念：殭屍產品（Zombie Products）**

***

**5. 廣泛建造 × 治理風險 [05:20]**

鼓勵全員建造能揭示隱藏需求，但沒有治理的廣泛建造會產生「秘密外洩」風險。GitGuardian 2026 報告指出，2025 年公開 GitHub 上暴露的 AI 服務金鑰達 **120 萬個**，年增 81%，預計 2026 年還將再成長 80–100%。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

> **關鍵概念：秘密蔓延（Secret Sprawl）**

***

**6. 市場判斷力是新的稀缺資源 [06:40]**

當第一版本的成本已趨近於零，PM 的核心問題變成：哪個客戶問題真正值得解決？哪個內部原型揭示了真實需求，哪個只是某個團隊的局部便利？競品功能是雜訊還是訊號？這不是產品管理，而是**產品判斷**。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

> **關鍵概念：產品判斷力（Product Judgment）**

***

**7. 新工作的具體樣貌 [07:44]**

PM 需要主動進入「**原型公域（Prototype Commons）**」——那個員工在正式流程之外自行建造工具的非正式空間。正確姿態是「開放式發現（Open Discovery）」：歡迎展示你做了什麼、解決什麼問題、碰了哪些資料。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

> **關鍵概念：原型公域（Prototype Commons）**

***

**8. 生產等級梯 [09:30]**

影片提出一個四層分類框架：

| 層級 | 說明 | 治理要求 |
|------|------|----------|
| **個人工具** | 單人使用，允許粗糙 | 避免敏感資料即可 |
| **團隊 Beta** | 小組使用 | 需有 Owner、備用 Owner、系統說明、失敗計畫 |
| **內部支援產品** | 公司依賴的內部軟體 | 需產品 Owner、存取管理、監控、文件、審計流程 |
| **外部產品/功能** | 客戶可見 | 上述全部 + AI 特定的 Evals 與治理 |

> **關鍵概念：生產等級梯（Production Class Ladder）**

***

**9. 降級與升級同樣重要 [11:00]**

只能升級的梯子最終會變成「雜物抽屜」——所有東西都累積到某個支援層級，形成新型技術債。PM 必須主動做**降級決策**，對不再有價值的工具明確宣告其終止，否則公司將以比命名速度更快的速度支付死軟體的維運成本。 [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

> **關鍵概念：軟體降級治理（Demotion Governance）**

***

## [結論與行動建議]

**啟發金句：**
> **「We can build everything. What should we build?」——這才是 AI 時代 PM 的真正問題。** [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)

***

**具體行動法則：4-Class Decision Rule（四類分類決策法則）**

每次面對一個原型或工具，PM 立刻問自己四個問題：
1. **這是什麼類別？**（個人工具 / 團隊 Beta / 內部支援產品 / 客戶承諾）
2. **它應該存在嗎？**
3. **它是為誰服務的？**
4. **我們願意依賴它到什麼程度？**

***

**生活實踐建議：**
- **每季進行「原型公域普查」**：主動盤點各部門正在使用的 AI 工具與自動化流程，用生產等級梯分類，識別哪些需要升級治理，哪些應該主動退役。
- **在下一個 Sprint Planning 中加入「降級議程」**：不只討論新功能，也討論哪些舊工具、舊 Agent 應正式廢止，避免支援成本無聲累積。
- **重建 PM 技術閱讀清單**：納入 AI Evals、Agent 架構、資料存取邊界、Cost Modeling 等主題，培養能「看見真正產品」的技術判斷力。

***

## [參考連結]

- 原始影片：https://youtu.be/b6J387xJvHg?si=r_xxwvMetxGMUzQw [youtube](https://www.youtube.com/watch?v=d95J8yzvjbQ)
- 完整文章與 Prompts：https://natesnewsletter.substack.com/p/product-management-cheap-software-governance
