---
title: 'Comprehend First, Code Later：大型程式碼庫的 AI 理解優先策略'
date: 2026-05-28
image: /images/AI筆記/comprehend-first-code-later.jpeg
category: AI筆記
tags: [Agent Manager, 程式碼理解, catch me up, 心智模型對齊, 理解優先原則]
description: '在擁有 15 年歷史、每天合併 100 個 PR、10 萬個組織依賴的龐大程式碼庫中，AI 最大的價值不是生成程式碼，而是協助理解程式碼。'
quote: '在大型程式碼庫中，AI 最大的解鎖點不是生成，而是理解。在 prompt 之前，先對齊你的心智模型。'
action: '接手新專案時先建立「catch me up」prompt，讓 AI 整理架構與慣例，再進入計劃與實作階段。'
source_has_timestamps: true
---
# 🎯 Comprehend First, Code Later
**演講者：Priscila Andre de Oliveira（Sentry 資深軟體工程師）**
**發表於 AI Engineer 大會 · 2026年5月27日**

***
## [核心摘要]
在擁有 15 年歷史、每天合併 100 個 PR、10 萬個組織依賴的龐大程式碼庫中，AI 最大的價值不是生成程式碼，而是**協助理解程式碼**。演講者分析了自己 116 個 Claude sessions，發現 67% 是「理解」用途，僅 2% 是「生成程式碼」。她因此建立了一套名為 "catch me up" 的個人技能，將理解行為結構化，解決了「AI 誤解需求、產出 slop 代碼」的核心痛點。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***
## [詳細重點整理]
### 1. 自我介紹與工作背景 [00:07]
Priscila 是 Sentry 資深軟體工程師，同時是 Verdaccio（開源 NPM Registry）維護者、Vienna JS 社群共同創辦人。她自稱「agent manager」—— 自 2025 年 12 月起，她已不再親手寫程式碼，改為純 prompting 模式工作。

**關鍵概念：Agent Manager（代理程式管理者）** — 工程師角色從「寫程式」轉型為「管理與引導 AI agent」。

***
### 2. Sentry 的技術規模與挑戰 [01:66]
Sentry 成立於 2010 年，擁有超過 15 年程式碼歷史、400 名員工、每天合併約 100 個 PR，全球 10 萬個組織依賴此系統。程式碼庫是一個「移動目標」：元件持續汰換、lint 規則不斷更新、技術債務龐大。

**關鍵概念：Moving Target Codebase（移動目標程式碼庫）** — 指高速迭代的大型系統，靜態知識快速失效。

***
### 3. 分析 116 個 Claude Sessions 的關鍵發現 [09:34]
讓 Claude 分析自己的快取對話紀錄後，發現使用分布如下：

| 類別 | 佔比 |
|------|------|
| 🧠 Comprehension（理解） | **67%** |
| ⚙️ Modification（修改） | 中等 |
| 📋 Process（流程） | 中等 |
| 🔍 Review（審查） | 中等 |
| ✍️ Generation（生成程式碼） | **僅 2%** |
| 其他 | 少量 |

**關鍵概念：理解優先原則** — AI 最高頻的實際用途是「讀懂程式碼」，而非「生成程式碼」。

***
### 4. "Catch Me Up" 個人技能的設計 [10:41]
她建立了一個儲存在本機的 Markdown prompt 技能，名為 **catch me up**，涵蓋六種程式碼探索模式：

- **Architecture**（架構）：模組關係與系統組成
- **Convention**（慣例）：程式碼風格與命名規則
- **Feature Trace**（功能追蹤）：某功能的完整執行路徑
- **Syntax**（語法）：語言特性與寫法說明
- **Testing**（測試）：測試策略與覆蓋範圍
- **History**（歷史）：為何這樣設計、過去決策脈絡

**關鍵概念：結構化理解技能（Structured Comprehension Skill）** — 將重複性的「看懂舊程式碼」需求，封裝成可重用的 prompt 模板。

***
### 5. 理解 → 計劃 → 實作的完整迴圈 [14:49]
她補充了 Jack Naish 的三階段流程（Research → Planning → Implementation），強調中間必須加入一個被忽略的步驟：**你必須先理解 AI 的研究結果，才能讓它開始計劃**。若跳過此步，AI 的心智模型可能對齊錯誤，導致 slop（爛）程式碼產出。

**關鍵概念：心智模型對齊（Mental Model Alignment）** — 確保人與 AI 在計劃前對問題理解一致，是避免低品質輸出的關鍵防線。

***
## [結論與行動建議]
**💡 啟發金句：**
> **「在大型程式碼庫中，AI 最大的解鎖點不是生成，而是理解。在 prompt 之前，先對齊你的心智模型。」**

**🔑 具體行動法則：C-A-P 法則**
1. **Comprehend（理解）**：用 AI 先讀懂現有程式碼
2. **Align（對齊）**：確認 AI 理解方向正確，再進入下一步
3. **Prompt（行動）**：帶著清晰模型，讓 AI 計劃與實作

**🏠 生活實踐建議：**
- **接手新專案時**：不要急著叫 AI 寫 code，先建立一個「catch me up」prompt，讓 AI 整理架構、慣例、歷史決策，用表格或圖解視覺化呈現
- **Code Review 時**：用理解模式先補充背景知識，再進行審查，避免因脈絡不足而產出表面意見
- **追查 Bug/回歸問題時**：用 AI 做 git blame 分析，取代等待跨時區同事回覆的漫長等待

***
## [參考連結]
- 📺 原始影片：https://youtu.be/li0SaBt9RDM?si=d-r4UWgPCIvG6_zy 
- 👤 演講者 LinkedIn：https://at.linkedin.com/in/priscila-andre-de-oliveira-ab34bb24b
