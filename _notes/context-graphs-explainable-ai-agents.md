---
title: 'Context Graphs for Explainable, Decision-Aware AI Agents'
date: 2026-05-29
image: /images/AI筆記/context-graphs-explainable-ai-agents.jpeg
category: AI筆記
tags: [Context Graph, 推理記憶, 決策先例, 參考類別驗證, AI Agent]
description: '現有的 AI Agent 擅長語言與推理，卻缺乏「為什麼要做某件事」的決策依據。此演講提出 Context Graph（情境圖）作為解法——不只儲存知識，更將組織政策、規則、歷史決策整合進圖資料庫'
quote: '每一個決策都是先例，未來的 Agent 繼承它。'
action: '設計 AI Agent 工作流時，加入決策節點子流程，明確要求 Agent 列出行動的可逆性與出錯代價，並為每個 Agent 設定授權邊界與 Escalation 機制'
source_has_timestamps: true
---
# 🧠 Context Graphs for Explainable, Decision-Aware AI Agents

**來源：** AI Engineer World's Fair — Neo4j 講座（Andreas Kollegger & Abhik / Zaid Zaim） [youtube](https://www.youtube.com/?hl=zh-tw)
**影片連結：** https://youtu.be/abvQEhvRI_c
**時長：** 16 分 38 秒 | 發布日期：2026年5月28日

***

## [核心摘要]

現有的 AI Agent 擅長語言與推理，卻缺乏「**為什麼要做某件事**」的決策依據。此演講提出 **Context Graph（情境圖）** 作為解法——不只儲存知識，更將組織政策、規則、歷史決策整合進圖資料庫，讓 Agent 在每一個決策點都能追溯因果、評估風險、知道自己是否有授權行動，最終將每筆決策寫回圖中成為「**先例**」，供未來的 Agent 學習繼承。 [youtube](https://www.youtube.com/?hl=zh-tw)

***

## [詳細重點整理]

### 1. 為何需要 Context Graph？ [00:38]

AI Agent 目前缺少的不是語言能力，而是 **知識脈絡中的「為什麼」**。Context Engineering 的下一步是將**政策（Policies）與規則（Rules）**也植入 Agent 的決策依據，而非僅提供工具與資料。**關鍵概念：Context Engineering → Context Graph 的躍升** [youtube](https://www.youtube.com/?hl=zh-tw)

### 2. 三種記憶架構 [01:36]

記憶系統分三層，缺一不可：

- **短期記憶（Short-term Memory）：** 對話歷史、當前狀態
- **長期記憶（Long-term Memory）：** 組織、人物、物件等廣義知識
- **推理記憶（Reasoning Memory）：** 政策與規則驅動的決策邏輯

**關鍵概念：推理記憶（Reasoning Memory）** [youtube](https://www.youtube.com/?hl=zh-tw)

### 3. 五階段決策框架 [06:10]

Abhik 提出可直接實作於 LangGraph / ADK 的決策工作流：

1. **問題框架化（Frame）：** 明確目標、因果脈絡與環境範圍
2. **全域規則查詢（Global Context）：** 引入硬性規則（Hard Rules）、軟性規則（Soft Rules）與歷史先例
3. **風險價值分析（Risk-Value Analysis）：** 評估決策可逆性、出錯代價、要最大化的價值
4. **行動或升級（Act or Escalate）：** 若無授權或確定性不足，立即交由更高層級 Agent 或人類決策者
5. **寫回推理鏈（Record Reasoning）：** 將完整推理過程、行動與結果存入圖，成為未來決策先例

**關鍵概念：決策先例回寫（Precedent Writing）** [youtube](https://www.youtube.com/?hl=zh-tw)

### 4. 參考類別驗證（Reference Class Validation）[11:43]

> **「99% 時候開藥 X 是對的，但對 1% 的患者可能致命。統計規律無法幫你確定你在哪個群體。」**

在採取行動之前，Agent 必須先判斷「目前情境屬於哪個參考類別」，而非依賴統計多數。這是風險評估中最關鍵的一步，也是 AI Agent 最容易忽視的隱性知識。**關鍵概念：Reference Class Validation（參考類別驗證）** [youtube](https://www.youtube.com/?hl=zh-tw)

### 5. Agentic 圖應用架構 [05:56]

基礎架構為：使用者查詢 → Agent → 知識來源（Graph DB）→ Text-to-Cypher 工具 → 圖遍歷 → 可靠回應。**Neo4j 的 Graph Academy** 提供免費線上課程，支援這套架構的學習與實作。**關鍵概念：Text-to-Cypher（文字轉圖查詢語言）** [youtube](https://www.youtube.com/?hl=zh-tw)

***

## [結論與行動建議]

**啟發金句：**
> **「每一個決策都是先例，未來的 Agent 繼承它。」**（Every decision becomes precedent. Future agents inherit it.） [youtube](https://www.youtube.com/?hl=zh-tw)

**具體行動建議 — F-R-A-R 法則：**

| 步驟 | 英文 | 意義 |
|------|------|------|
| **F**rame | 框架化 | 定義目標、因果與環境 |
| **R**ules | 規則查詢 | 引入全域政策與歷史先例 |
| **A**nalyze | 分析 | 執行風險價值評估與參考類別驗證 |
| **R**ecord | 回寫 | 將推理鏈與決策結果存回圖 |

**生活實踐建議：**
- **在設計 AI Agent 工作流時**，加入一個「決策節點」子流程，明確要求 Agent 列出行動的可逆性與出錯代價，再決定是否執行
- **建立組織的「決策圖」**：將企業 SOP、例外處理規則以 Neo4j 圖資料庫形式儲存，讓 Agent 查詢時有依據
- **Escalation 機制不可省**：為每個 Agent 設定「授權邊界」，超過邊界必須轉交人類或高權限 Agent，這是可靠 Agentic 系統的安全底線 [youtube](https://www.youtube.com/?hl=zh-tw)

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/abvQEhvRI_c
- 📚 Neo4j Graph Academy（免費課程）：https://graphacademy.neo4j.com
- 🐦 講者 Andreas Kollegger：https://x.com/akollegger
