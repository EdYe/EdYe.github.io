---
title: 'Ship Real Agents：AI Agent 的完整 Eval Pipeline 建構指南'
date: 2026-05-15
image: /images/AI筆記/ship-real-agents-evals.jpeg
category: AI筆記
tags: [Agent評估, Vibes Problem, LLM評審, 追蹤, 迴歸測試]
description: '大多數 AI Agent 上線前的測試方式是「跑幾個 Query 看起來對就好」——稱之為 Vibes Problem。這種方式無法捕捉迴歸錯誤、無法整合進 CI/CD 流程。'
quote: '選對 Eval 比調整 Eval 更重要；同一個 Agent，Correctness Eval 0分，Faithfulness Eval 13分滿分。'
action: '先建立 Trace，分類失敗根因，用實驗框架量化每次 Prompt 改動效果，而非靠直覺判斷'
source_has_timestamps: true
---
以下是本影片的完整結構化筆記：

***

# Ship Real Agents: Hands-On Evals for Agentic Applications

**講者：Laurie Voss（Arize AI 開發者體驗主管）｜AI Engineer Conference，2026年5月14日**

***

## [核心摘要]

大多數 AI Agent 上線前的測試方式是「跑幾個 Query 看起來對就好」——Laurie 稱之為 **Vibes Problem（直覺測試問題）**。這種方式無法捕捉迴歸錯誤、無法整合進 CI/CD 流程，也無法告訴你修改一個 Prompt 是否同時破壞了其他三件事。本工作坊從零建構一個完整的 Eval Pipeline，對象是一個金融分析 Agent，涵蓋 Tracing（追蹤）、失敗根因分類、Code Eval、LLM-as-a-Judge 評估，到最終能夠「量化証明」Prompt 改善效果的實驗框架。 [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

***

## [詳細重點整理]

### 1. 為什麼需要 Eval？[00:07]

**Vibes Problem（直覺測試問題）** 是 AI Agent 開發的核心痛點： [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

- 手動跑幾個 Query 看輸出「感覺對」，但無法覆蓋邊界案例與惡意輸入
- 最常見的失敗原因：使用者用了 Agent 預期詞彙以外的表達方式
- 傳統單元測試失效，因為同一個 Prompt 每次輸出都不同，但「多個不同輸出可能都是正確的」
- 人工審查無法擴展，且無法整合進 CI 流程
- 沒有 Eval，就無法：安全改系統 Prompt、安全換模型版本、在出錯前捕捉迴歸

**關鍵概念：Vibes Problem（直覺測試問題）**

***

### 2. Trace 與 Span 的基礎架構 [00:06]

**Traces（追蹤記錄）** 是 Eval 的原始資料基礎，如同伺服器日誌之於後端： [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

- 每一個 Agent 呼叫、工具呼叫、LLM 調用，輸入與輸出都會被記錄為 Trace
- Trace 的組成單元是 **Span**，每個 Span 代表一個執行步驟（LLM 呼叫、工具呼叫皆為 Span）
- Span 記錄：輸入、輸出、時間、Token 數等元資料
- 底層基礎：**OpenTelemetry（OTel）**，加上 LLM 專屬的 **OpenInference** 擴充層（含 Prompt text、Token count、Tool invocation 等）

**關鍵概念：OpenInference（LLM 可觀測性標準）**

***

### 3. 三種 Eval 類型與使用時機 [00:10]

| 類型 | 特性 | 適用情境 | 限制 |
|------|------|----------|------|
| **Code Eval** | 確定性、毫秒級、幾乎零成本 | 格式驗證、長度限制、禁用詞、必填欄位 | 輸出複雜時脆弱 |
| **LLM-as-a-Judge** | 語意理解、彈性高 | 正確性、忠實度、語調 | 昂貴、本身非確定性 |
| **Human Eval** | 最高標準 | 建立 Golden Dataset | 無法擴展至 CI 規模 |

 [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

三者為**互補關係**，成熟的 Eval Suite 必須同時運用三種。Human Eval 的主要用途是建立「已知正確答案」的 **Golden Dataset** 供 LLM Judge 對標。

**關鍵概念：Golden Dataset（黃金標準資料集）**

***

### 4. Agent 的特殊挑戰：串聯失敗 [00:15]

**Cascading Failure（串聯失敗）** 是 Agent 評估最難的核心問題： [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

- 單一工具呼叫就需測試三層：選了正確工具？傳了正確參數？正確理解輸出？
- 多層失敗範例：Agent 誤將「Tesla」理解為「Nikola Tesla（發明家）」→ 輸出一份 18 世紀人物的投資分析
- 反向風險：Eval 若過度規定執行路徑，反而會在 Agent 找到更聰明解法時報錯
- 多 Agent 系統額外需測試：路由 LLM 是否選對子 Agent、資訊是否正確傳遞、是否正確停止

**關鍵概念：Cascading Failure（串聯失敗效應）**

***

### 5. Capability Eval vs. Regression Eval [00:18]

**Capability Eval（能力評估）** 是 Agent 持續進化的核心機制： [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

- Capability Eval：給 Agent 一個「它目前不擅長的能力」作為爬山目標，反覆迭代直到通過率達 100%
- 達到 100% 後，該 Eval 升級為 **Regression Eval（迴歸評估）**，確保已有能力不退化
- 整個 Eval Suite 的生命週期：不斷將 Capability Eval 轉化為 Regression Eval，再建立新 Capability Eval

***

### 6. 實作：Phoenix 可觀測性平台 [00:22]

**Arize Phoenix** 是開源 AI 可觀測性平台，核心功能： [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

- 兩行程式碼啟動：`import phoenix` + `register(auto_instrument=True)` 即可自動擷取所有日誌
- 支援主流框架：Claude Agent SDK、OpenAI Agent SDK、CrewAI、LangChain、LlamaIndex 等
- 實際展示：金融分析 Agent 對 Tesla 執行 4 次 Web 搜尋，所有 Span 清晰呈現在 UI 中

**關鍵概念：Auto-Instrumentation（自動儀器化）**

***

## [技術/數據對比]

### Correctness Eval vs. Faithfulness Eval 的致命差異

| Eval 類型 | 得分（13 題中）| 原因 |
|-----------|--------------|------|
| **Correctness Eval（正確性）** | 0 / 13 | 模型不知道「現在是什麼年份」，無法驗證前瞻性財務數據 |
| **Faithfulness Eval（忠實度）** | 13 / 13 | 模型確實依據其搜尋到的來源資料撰寫報告 |

 [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

**結論：選對 Eval 比調整 Eval 更重要。** 同一個 Agent，用不同的評估框架，會得到天差地別的結論。

***

### LLM Eval 解釋範例

一個要求「東京平價旅遊建議」的 Query，Agent 給出了旅遊建議但**沒有標示花費金額**。LLM Judge 能精準識別出這個細微的失敗：給了推薦但沒有回應「平價」的核心需求。 這類解釋可以在跑完 1000 條 Trace 後，再用第三個 LLM 自動分類失敗模式，找出系統性問題。 [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

***

### 完整 Eval Pipeline 架構

| 階段 | 工具/方法 |
|------|-----------|
| **Instrumentation** | Phoenix register + auto_instrument |
| **Data Collection** | Traces + Spans（OpenInference 標準）|
| **Trace Analysis** | 手動讀取 → 分類失敗根因 |
| **Eval 撰寫** | Code Eval → 內建 LLM Eval → 自訂 Rubric |
| **Meta Evaluation** | 測試你的 Judge 是否在正確地評判 |
| **Experiments** | 量化證明 Prompt 改善效果 |
| **Iteration** | 修改 Prompt → 重跑 Eval → 循環 |

 [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)

***

## [結論與行動建議]

**啟發金句：**
> **「選對 Eval 比調整 Eval 更重要；同一個 Agent，Correctness Eval 0分，Faithfulness Eval 13分滿分。」**

**具體行動建議：T-R-E 法則**
- **T（Trace First）**：先讓系統吐出 Trace，在寫任何 Eval 之前先讀懂你的資料
- **R（Root Cause）**：分類失敗根因，區分「一次性怪異輸出」vs「系統性 Prompt 問題」
- **E（Experiment）**：用實驗框架量化每次改動效果，而非靠直覺判斷

**生活實踐建議：**
- 下次修改 AI Agent 的 System Prompt 時，不要只跑 3 條測試就上線：先用 Phoenix（免費雲端版）建立 Trace，挑出 10-20 個失敗案例，寫一個 Faithfulness Eval 作為基線，再修改 Prompt，用 Experiment 功能對比改前改後的分數。 [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)
- 換模型版本（如 Claude Sonnet 4.5 → 4.6）前，必須先有 Regression Eval Suite，否則等於重新從零測試。

***

## [參考連結]

- 原始影片：https://youtu.be/Xfl50508LZM?si=pmM5ftBKIGoF4lLw [youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)
- 講者 Twitter：https://x.com/seldo
- Arize Phoenix（開源）：https://phoenix.arize.com
- 講者 GitHub：https://github.com/seldo
