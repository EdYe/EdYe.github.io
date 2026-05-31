---
title: 'Agent 需要決策軌跡，不只是文件：Context Graph 的三層記憶架構'
date: 2026-05-31
image: /images/AI筆記/agents-decision-traces-context-graph.jpg
category: AI筆記
tags: [決策軌跡, Context Graph, 圖結構嵌入, 實體萃取, 混合搜尋]
description: '標準 RAG 只給 Agent 一個知識庫，讓它「回答問題」。Context Graph（上下文圖譜）則在此基礎上加入過去的決策軌跡（decision traces）、因果鏈與推理記憶，讓 Agent 從「回答問題」進化為「做出有根據的決策」——直接給出「應接受還是拒絕，以及原因」。'
quote: '知識庫讓 Agent 知道風險在哪，上下文圖譜讓 Agent 知道該怎麼決定。'
action: '從 uvx create-context-graph 切入實作，選擇最接近業務的內建 domain，快速驗證 Context Graph 在審核流程中的落地效益'
source_has_timestamps: true
---
# Why Your Agents Need Decision Traces, Not Just Documents — Zach Blumenfeld, Neo4j

**AI Engineer 大會 | 2026年5月29日 | 時長 20:12**

***

## [核心摘要]

標準 RAG 只給 Agent 一個知識庫，讓它「回答問題」。**Context Graph（上下文圖譜）** 則在此基礎上加入過去的決策軌跡（decision traces）、因果鏈與推理記憶，讓 Agent 從「回答問題」進化為「做出有根據的決策」——直接給出「應接受還是拒絕，以及原因」。這解決了 AI Agent 在高風險場景（如金融審核）中缺乏歷史判斷依據的核心痛點。

***

## [詳細重點整理]

### 1. 知識庫 vs. 上下文圖譜 [00:14]

傳統 RAG 知識庫告訴 Agent「風險因素是什麼」，而 **Context Graph** 告訴它「面對這個案例，過去是如何判決的、為什麼」。以金融分析師 Agent 為例：知識庫給出客戶資料與政策，Context Graph 額外疊加過去相似案例的決策軌跡，讓 Agent 直接給出「拒絕/接受 + 理由」的可執行答案。

**關鍵概念：決策軌跡（Decision Traces）**

### 2. Context Graph 的三層記憶架構 [00:47]

`neo4j-agent-memory` 套件實現了三層完整記憶：

- **短期記憶（Short-term Memory）**：對話歷史與當前 session 上下文
- **長期記憶（Long-term Memory）**：從對話中萃取、隨時間累積的實體（人、事、物）
- **推理記憶（Reasoning）**：儲存在 Context Graph 中的決策軌跡與因果鏈

### 3. 混合搜尋：語意 + 結構雙軌並行 [07:00]

系統同時執行兩種搜尋：

- **向量語意搜尋**：找出語意相似的過往案例（如「詐欺拒絕」）
- **Graph Embedding 結構搜尋**：將整個決策軌跡圖結構嵌入向量，讓「結構相似的決策」也能被發現——這是純文件向量搜尋無法做到的

**關鍵概念：Graph Embedding（圖結構嵌入）**

### 4. 實體萃取 Pipeline [14:07]

從非結構化文字建立知識圖譜的流程分三階段，由粗到精逐步精煉：

- **spaCy** → 快速命名實體識別（NER）
- **GLiNER** → 更進階的 zero-shot 實體識別
- **LLM fallback** → 處理前兩層無法解析的複雜情況
- 最後執行獨立的**去重複（deduplication）、合併與豐富化**策略

### 5. 一鍵啟動：`uvx create-context-graph` [08:30]

只需一行終端機指令即可搭建完整 full-stack 應用，類似 `create-react-app` 的概念：

```bash
uvx create-context-graph --name <app_name> --domain <domain> --framework pydantic-ai --demo-data
```

- 內建 **22 個領域**（金融服務、醫療等），也可自訂 domain 自動生成本體（ontology）
- 支援 **Pydantic AI、LangGraph、Crew、Google ADK、OpenAI、Strands** 等主流框架
- 可從 **GitHub、Notion、Jira、Slack** 匯入真實資料
- 自動生成 **MCP server**，支援多輪對話

***

## [結論與行動建議]

**啟發金句：**
> **「知識庫讓 Agent 知道風險在哪，上下文圖譜讓 Agent 知道該怎麼決定。」**

**具體行動建議（3-T 法則）：Trace → Track → Transfer）**
1. **Trace（追蹤）**：在 Agent 每次做決策時，主動記錄決策軌跡與推理過程至 Context Graph
2. **Track（累積）**：讓實體與決策隨時間累積成長期記憶，形成組織決策知識庫
3. **Transfer（遷移）**：用 Graph Embedding 將結構性知識遷移到新情境，讓 Agent 複用過去的判斷智慧

**生活實踐建議：**
作為 AI 應用架構師，可立即從 `uvx create-context-graph` 切入實作，選擇與自身業務最接近的內建 domain（如 FinServ），快速驗證 Context Graph 在審核流程、客戶決策或產品推薦中的落地效益，而不必從零建構圖譜 schema。

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/B9h9ovW5H9U?si=GEjiT5ROMMHNGuqi
- 👤 講者 LinkedIn：https://www.linkedin.com/in/zachblumenfeld/
- 📦 GitHub：`neo4j/neo4j-agent-memory`（影片中提及）
