---
title: 'Harness Engineering：如何打造軟體工廠'
date: 2026-10-07
image: /images/影片筆記/harness-engineering-software-factory.jpg
category: 影片筆記
tags: [軟體工廠, 工具鏈工程, 三層迴圈, 控制平面, 改進迴圈]
description: '本場演講（AI Engineer World''s Fair 2026）提出 Harness Engineering（工具鏈工程，近期亦被稱為 Loop Engi'
quote: '💡「工廠生產產品，工程師建造工廠。真正的報酬不是更快出貨，而是更高的品質。」'
action: '🎯A-A-M-M 法則：先建立自主性、再建立自動化，追蹤人工接管次數下降與機器發起 PR 上升，全程保持品質。'
source_has_timestamps: true
---
# Harness Engineering: How to Build a Software Factory 

---

## [核心摘要]

本場演講（AI Engineer World's Fair 2026）提出 **Harness Engineering（工具鏈工程，近期亦被稱為 Loop Engineering / 迴圈工程）** 作為從「使用編碼代理」邁向「軟體工廠（Software Factory）」的核心紀律。工廠定義為：使用者拿到的一切產出皆由 Agent 生成，工程師的工作轉為建造並優化「工廠」本身。演講解構了三大支柱指標（自主性、自動化、品質）、三層迴圈架構（inner / outer / meta loop），以及實作順序：控制平面 → Agent 就緒基礎設施 → 改進迴圈，並以 Tessl 產品示範落地路徑 。

---

## [詳細重點整理]

### 1. 適合對象與前提條件 [00:43]

此為進階主題：前提是你的團隊已在多工同時使用編碼代理，且 Agent 在簡單至中等複雜度任務上「經常做對事」。若仍處於 Agent 頻繁出錯的階段，先別急於工廠化。所有方法論皆 stack 中立，Tessl 只是使其變容易，不綁定特定工具 。

**關鍵概念：Agent 成熟度門檻（Agent Maturity Gate）**

### 2. 什麼是軟體工廠 [02:03]

軟體工廠沒有嚴格定義，但核心是：**終端產品完全由 Agent 生成，工程團隊專注於建造工廠**——提升其自主性、自動化程度與產出品質。每位工程師實質上轉型為「內部工具建造者」。

**關鍵概念：角色反轉（Engineers as Tool Builders）**

### 3. 三大支柱指標：自主性、自動化、品質 [02:58]

- **自主性**：到達正確答案需要多少人為干預（修正次數、方向調整）
- **自動化**：你對結果的信任度——不需人工審查就能接受解決方案的程度
- **品質**：實際交付使用者的產品好壞（使用者分析、測試覆蓋率等）

自主性 ≠ 自動化：Agent 可能經常一次做對（高自主性），但你仍逐行人工審查（低自動化）。路徑為：先提升自主性 → 再提升自動化 → 品質全程保持恆定 。

**關鍵概念：信任缺口**

### 4. 真正的回報是品質，而非速度 [04:33]

多數人把工廠視為「出貨更快」的手段（容忍一些 slop 換取更多功能上線），但講者認為這只是過渡現象。長期而言，軟體工廠讓 backlog 概念消失，釋放產能投入測試品質與架構重構，**最終回報是更高的程式碼品質**。附帶效益：非技術角色更容易貢獻想法，形成更具包容性的開發文化 。

**關鍵概念：Backlog 消融**

### 5. Harness Engineering 是什麼 [06:13]

工廠生產產品，而 Harness Engineering 建造的正是「自動化並改進工廠品質的迴圈」。這是抵達軟體工廠的核心實踐。此術語演進極快——近幾週已有人改稱 loop engineering 。

**關鍵概念：Harness Engineering（工具鏈工程）**

### 6. 三層迴圈：Inner、Outer、Meta Loop [06:43]

- **Inner Loop（內迴圈）**：Agent 在 PR 提交前的迭代——快速、便宜、高頻執行。改善它直接提升自主性，讓 Agent 自我修正而無需人類介入
- **Outer Loop（外迴圈）**：PR 提交後執行的昂貴、窮舉性檢查（如 agentic QA、mutation testing 驗證測試套件）。成本高但取代人工審查時間，值得
- **Meta Loop（元迴圈）**：位於開發流程之外，觀察 Agent 日誌、PR、issue tracker、使用者回饋，找出漏到使用者的錯誤或人工攔截過的錯誤，回饋至 inner/outer loop 防止重犯。**驅動 AI 原生程度（AI-native percentage）提升的關鍵投資就在 meta loop**

**關鍵概念：迴圈分層**

### 7. 為什麼 Harness Engineering 很難 [09:08]

三大困難皆根源於人類心理：

1. **知識迭代過快**：新紀律每週變化，讀論文、追部落格的最佳實踐兩週後就過時，甚至變成反模式。團隊等於被迫成為 AI 研究員
2. **本質上是計畫外工作**：改善 Agent 的投入與出貨功能直接競爭。不做就困在局部最佳化，做了就趕不上 deadline——永恆的取捨難題
3. **訊號不可讀**：關鍵資料藏於本地 Agent 日誌、某人的機器、某人的腦中。必須先將工作流搬到「一切皆被保存且可取得」的表面

**關鍵概念：訊號可讀性**

### 8. 三層實作架構 [11:13]

依 Tessl 建議的順序建造 ：

### 9. Layer 1：控制平面（Control Plane）[11:33]

將工作流搬到可讀的表面上：所有工作始於 issue tracker 的 issue → 送至 sandbox 中執行的 headless agent → Agent 提出 PR → 工程師在 PR 留言互動。三個標準組件：issue 追蹤與任務啟動、程式碼審查（GitHub PR review 最簡單）、標準化分發工作流的機制（skills registry 或共享 repo）。

### 10. Layer 2：讓基礎設施 Agent-Ready [12:47]

「比你想像的更糟」——如同把大量本地配置的專案交給別人 setup 的噩夢：CLI 存取、API 權限、讓 Agent 點擊走過產品、治理與合規、production log 存取、程式碼執行環境。每家公司的清單不同且無法事先規劃，就是花一兩週逐一打通 。

**關鍵概念：Agent-Ready Stack**

### 11. Layer 3：改進迴圈（Improvement Loops）[14:22]

**這是你最終投入最多時間的地方**，包含 meta loop 的組件：

- **Repo 維護**：每日 / 每週掃描 codebase 找問題
- **Playbooks**：常見開發實務手冊（如如何為 CLI 加功能）
- **重複任務識別與自動化**：愈快愈簡單，否則沒人會做
- **輸出品質持續監看**：發現 Agent 犯錯 → 更新對應 skill/playbook → 防止重犯

### 12. Tessl 如何協助：模組化與小步迭代 [15:32]

Tessl 的定位：將抵達前沿變成「多次小提升」而非一次吞下整隻麋鹿。四個賣點：替你追蹤快速變化的最佳實踐（解決知識落差）、模組化開放（不假設單一公司全都能做到 best-in-class）、預裝自動化迴圈（安裝後只需回應建議的變更）、漸進式（六個月後回頭看已完成 40%，從未延誤出貨）。產品面包括：具版本控制與治理（安全審查、品質審查、發佈權限）的 **Skills Registry**、issue tracker 連接器（目前 Linear → GitHub）、agentic code review 工具套件 。

### 13. Tessl Agent 與 Tessl Launch [17:37]

- **Tessl Agent**：挖掘 PR / issue 找出重複任務（如每週人工獵捕 flaky test），轉為 skill 並放上 GitHub Action 自動化——直接解決「沒時間做自動化」的問題。另提供一鍵安裝的維護任務（架構品質、程式碼重複、測試套件健壯度、安全漏洞的每週掃描）
- **Tessl Launch**：將任何 skill 轉為自動化工作流。可指定任何編碼代理執行（Codex、Claude Code、Gemini 皆可），在具適當權限的 sandbox 中長時間執行，持有 GitHub token 可提出 PR 並回應留言

## [結論與行動建議]

### 啟發金句

> **「工廠生產產品，工程師建造工廠。真正的報酬不是更快出貨，而是更高的品質。」**

### 具體行動建議：A-A-M-M 法則

追蹤四個指標逐步前進：**Autonomy**（先建立）→ **Automation**（再建立）→ **Manual takeovers 下降**（人工接管次數）→ **Machine-initiated PRs 上升**（無人發起的 PR 增加），全程品質保持恆定、最終向上拉升。這就是衡量自己離軟體工廠多遠的儀表板 。

### 生活實踐建議

- **從一條工作流開始**：不要試圖一次吞下整隻麋鹿。挑一個每週重複的任務（如 flaky test 獵捕、codebase 週掃描），寫成 skill、放上自動化、驗證效果，再下一條
- **先把訊號搬上可讀表面**：把散落在本地終端、個人腦中的 Agent 互動，集中到 issue tracker → PR → 留言的軌跡上——沒有可讀資料，一切改進迴圈都是空談
- **為「計畫外工作」預留預算**：在衝刺規劃中明確分配時間給 harness engineering，否則它永遠被出貨壓力吞噬，團隊將困在 Agent 不再進步的局部最佳化

---

## [參考連結]

- [原始 YouTube 影片](https://youtu.be/X6l4lpA0_NY)
- Tessl: [https://tessl.io](https://tessl.io)
- AI Engineer: [https://ai.engineer](https://ai.engineer)