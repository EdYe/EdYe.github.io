---
title: 'Gemini Workspace Intelligence：脈絡感知的跨應用智能串流'
date: 2026-05-04
image: /images/AI筆記/gemini-workspace-intelligence.jpeg
category: AI筆記
tags: [Gemini, 脈絡感知, 多源合成, Drive Projects, 事件驅動自動化]
description: 'Google 正式推出 Workspace Intelligence，將 Gemini AI 深度整合進 Gmail、Drive、Docs、Sheets、Slides 和 Vids，讓 AI 不再需要使用者手動提供背景資訊，自動建立脈絡化的個人知識庫'
quote: '你不再需要給 Gemini 背景資訊——因為它早就知道了。'
action: '在 Drive 建立現有專案的 Project 空間，試問 Gemini「這個專案目前狀況如何？」，並設定每日 Email 摘要 Studio 自動化趁免費先跑起來。'
source_has_timestamps: true
---
# Gemini Workspace Intelligence 完整解析

**頻道：Paul J Lipsky｜片長：12:16｜發布：2026-05-03**

***

## [核心摘要]

Google 正式推出 **Workspace Intelligence**，將 Gemini AI 深度整合進 Gmail、Drive、Docs、Sheets、Slides 和 Vids，讓 AI 不再需要使用者手動提供背景資訊——它已透過你的工作檔案、Email 往來紀錄及合作對象，自動建立起一個**脈絡化的個人知識庫**，實現跨應用的智能串流作業。

***

## [詳細重點整理]

**1. Workspace Intelligence 核心概念 [00:00]**

不再是孤立的 AI 助手，而是橫跨整個 Google 工作環境的**脈絡感知引擎**。它能同時讀取 Drive 內的文件、Gmail 的往來信件，並在所有應用程式中提供一致且具備個人化背景的回應，無需重複上傳或解釋資料。

> **關鍵概念：上下文持久化（Persistent Context）**——AI 永遠知道你在做什麼、與誰合作、目前進度為何。

***

**2. 跨文件智能生成 Pitch Deck [01:04]**

在 Gemini 中直接指令，可同時引用試算表數據、品牌指南文件、以及商業夥伴 Email 中的創意，一次性產出完整投資簡報。接著直接匯出至 Google Slides 進行人工微調，或由 Gemini 自動替換圖片（AI 生成指定場景圖）。

> **關鍵概念：多源情境合成（Multi-Source Synthesis）**——單一指令可跨越文件、試算表、Email 三個資料源。

***

**3. Google Vids 簡報轉影片 [03:23]**

透過 `vids.new` 進入 Google Vids，可將 Slides 直接轉換為含 AI 旁白的影片，適合無法出席簡報的投資人或遠端受眾。這是目前 Google Workspace 中**最被低估的工具之一**。

> **關鍵概念：非同步簡報傳遞（Async Pitch Delivery）**

***

**4. 文件內 AI 自動生成發票 [05:01]**

在 Google Docs 中，Gemini 可串接 Gmail 信箱，讀取客戶往來信件中的付款條件，並同時比對已有的發票範本格式，自動產出格式一致、數字精準的正式發票，也可於手機端直接輸出 PDF。

> **關鍵概念：格式感知生成（Format-Aware Generation）**——輸出結果不僅正確，且自動對齊既有企業文件風格。

***

**5. Drive Projects：專案知識庫 [06:20]**

在 Google Drive 左側新增「Projects」功能，可將相關的文件、試算表、Email 集中為一個專案空間，讓 Gemini 僅在該範圍內進行推理與回答，類似 **NotebookLM** 的「來源限定問答」邏輯，但直接整合於 Drive 工作流程中。

> **關鍵概念：範疇限定推理（Scoped Reasoning）**

***

**6. AI Inbox：Gmail 智慧收件匣 [08:15]**

Gemini 自動分析收件匣，將每封 Email 分類為「待辦事項（To-Do）」或「需了解（Catch-Up）」，協助使用者每日開始工作前快速掌握行動優先順序，目前仍在 Beta 階段，尚未開放所有用戶。

> **關鍵概念：行動優先收件（Action-Priority Inbox）**

***

**7. Ask Gemini in Gmail + Studio 自動化 [09:20]**

Workspace 訂閱用戶專屬功能：在 Gmail 頂部的「Ask Gemini」可呼叫自定義 Gem（如談判品牌合作的專屬助手），並串接 Drive、Chat 或網頁資料。Studio 功能則可設定 Email 觸發的自動化任務（如每日摘要全部信件），但預計數個月後將開始收取額外點數費用。

> **關鍵概念：事件驅動自動化（Event-Driven Automation）**

***

**8. Sheets Canvas 視覺化儀表板 [10:30]**

在 Google Sheets 中點擊「Ask Gemini → Create Canvas」，可將試算表數據即時轉換為互動式視覺儀表板，呈現分類比重、預算健康度與總預測等圖表，可隨時切換回原始資料檢視。

> **關鍵概念：即時資料視覺化（On-Demand Data Canvas）**

***

## [技術／功能對比]

| 功能 | 適用對象 | 目前狀態 |
|---|---|---|
| Workspace Intelligence（基礎） | Ultra / Pro 用戶 | 陸續推出中 |
| AI Inbox | 所有用戶（Beta） | 測試中，未全開 |
| Ask Gemini in Gmail | Workspace 訂閱用戶 | 已上線 |
| Studio 自動化 | Workspace 訂閱用戶 | 即將收費 |
| Drive Projects | Ultra / Pro 用戶 | 陸續推出中 |
| Sheets Canvas | Workspace 訂閱用戶 | 已上線 |
| Google Vids 轉影片 | 所有用戶 | 已上線（vids.new） |



***

## [結論與行動建議]

**✦ 啟發金句：**
> **「你不再需要給 Gemini 背景資訊——因為它早就知道了。」**

**✦ 核心法則：D-P-A 法則（Data → Project → Action）**
- **D（Data）**：將所有工作文件、信件集中在 Google Drive / Gmail
- **P（Project）**：在 Drive 建立 Project 空間，圈定 Gemini 的推理範圍
- **A（Action）**：透過 Ask Gemini 或 Studio 自動化，將重複性任務交給 AI 執行

**✦ 實務應用建議：**
- **立即可做**：在 Drive 左側新增一個現有專案的 Project，將相關文件與 Email 拉入，試問 Gemini「這個專案目前狀況如何？」
- **本週嘗試**：開啟 Google Sheets 的 Canvas 功能，將你的現有報表轉為互動儀表板，直接用於客戶提案或週報呈現
- **訂閱用戶必做**：在 Gmail 設定一個「每日 Email 摘要」Studio 自動化，趁現在仍免費，先跑起來再說

***

## [參考連結]

- 📺 原始影片：https://youtu.be/E93UOV891bM?si=uT6iMcYawCrhqaze
