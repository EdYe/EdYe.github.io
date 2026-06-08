---
title: 'Claude Code Ultra Code 多代理人並行模式'
date: 2026-06-08
image: /images/AI筆記/claude-ultra-code-multi-agent.jpg
category: AI筆記
tags: [Ultra Code, 多代理人並行, 動態工作流程, 超高思考, Token成本]
description: 'Claude Code 推出全新設定 Ultra Code，將單一 Claude 實例轉化為最多 100 個並行代理人的協作團隊，透過超高思考加動態工作流程的組合，大幅提升複雜任務的執行效率與品質。'
quote: '你不是在執行 Claude，你是在執行一支 100 人的智慧團隊——但帳單也是 100 倍的。'
action: '只在任務真正複雜時啟用 Ultra Code，善用內建交叉驗證機制，並於每次執行後輸入 /usage 追蹤費用避免超支。'
source_has_timestamps: true
source_raw: 'Claude Just Dropped ULTRA CODE'
---
## [核心摘要]

Claude Code 推出全新設定 **Ultra Code**，將單一 Claude 實例轉化為最多 100 個並行代理人的協作團隊，透過「超高思考（xhigh thinking）+ 動態工作流程（dynamic workflows）」的組合，大幅提升複雜任務的執行效率與品質——代價是極高的 token 消耗成本。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [詳細重點整理]

### 1. Ultra Code 的本質 [00:00]

Ultra Code 並非一種「努力程度（effort level）」，而是兩項技術的捆綁包：**超高思考（xhigh thinking）** + **動態工作流程（dynamic workflows）**。它位於 Claude Code 的 `/effort` 選單中，緊鄰 Max 選項，但本質上是截然不同的機制——Max 代表最深度的單一思維鏈，Ultra Code 則代表多代理人並行協作。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：多代理人並行架構（Multi-Agent Parallelism）**

***

### 2. 兩大核心組件 [01:16]

Ultra Code 由兩個組件構成： [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

- **超高思考（xhigh thinking）**：思考深度僅次於 Max，每一個步驟都進行深度推理，但非絕對最高等級
- **動態工作流程（Dynamic Workflows）**：收到任務後，先制定完整計畫，再拆解成多個子任務，分配給不同代理人**同步執行**，最後由獨立代理人進行**交叉查核（fact-check）**後才輸出結果

> **關鍵概念：動態工作流程（Dynamic Workflows）**

***

### 3. Ultra Code vs. Max 對比 [02:21]

| 維度 | Max | Ultra Code |
|---|---|---|
| 思考深度 | 最高（Max） | 超高（xhigh） |
| 代理人數量 | 單一 | 最多 100 個並行 |
| 執行方式 | 序列式（one at a time） | 並行式（parallel） |
| 結果查核 | 無獨立查核 | 獨立代理人交叉驗證 |
| 適用情境 | 需要最深思維鏈的單一問題 | 複雜、多面向的大型任務 |
| 費用 | 高 | **極高（最貴）** |

 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

### 4. 開啟方式 [00:34]

在 Claude Code 中輸入 `/effort`，從選單選擇 **Ultra Code** 即可啟用。啟用後，**整個 session 期間**的所有任務都會自動套用多代理人模式，無需每次重新設定。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：Session 級別持久設定**

***

### 5. 實測演示 [02:57]

以「研究餐車創業完整指南」為案例：Ultra Code 自動將任務拆解為多個平行子任務（許可證申請、設備費用、供應商尋找、常見錯誤等），畫面底部的閃電符號數字即時跳升，代表代理人陸續啟動。最終輸出一份包含實際費用、所需許可證、採購來源的**完整啟動指南**，且已經過交叉驗證。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：任務分解與並行執行（Task Decomposition & Parallelization）**

***

### 6. 費用警示 [03:58]

Ultra Code 是 Claude Code **成本最高的執行模式**，官方文件亦明確標注。原因在於同時燃燒 100 個代理人 × 深度思考層級的 token，費用呈倍數放大。可透過輸入 `/usage` 查看本次執行的詳細費用明細。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

> **關鍵概念：Token 並行消耗（Parallel Token Burn）**

***

## [結論與行動建議]

**啟發金句：** 「你不是在執行 Claude，你是在執行一支 100 人的智慧團隊——但帳單也是 100 倍的。」

**具體行動建議（Ultra Code 3C 法則）：**
- **Complex（複雜）**：只在任務真正複雜、需多面向同步調查時才啟用
- **Check（查核）**：善用內建的交叉驗證機制，確保輸出品質
- **Cost（成本）**：每次執行後輸入 `/usage`，追蹤費用避免超支

**生活實踐建議：**
作為 AI 應用架構師，可將 Ultra Code 定位為「研究與規劃階段」的重型武器——例如競品分析、技術選型評估、新功能 PRD 起草等需要多角度同步調查的任務。日常的程式碼補全或單一問題解答，仍應使用 Max 或更低層級以控制成本。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

## [參考連結]

- 原始影片：https://youtu.be/IgIlIWqeT-I
- Dynamic Workflows 官方公告：https://claude.com/blog/introducing-dynamic-workflows-in-claude-code [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
- Claude Code 文件：https://code.claude.com [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
