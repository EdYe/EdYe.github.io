---
title: 'Agent 可觀測性完整指南：從 Eval 到自我診斷'
date: 2026-05-09
image: /images/影片筆記/agent-observability-complete-guide.jpeg
category: 影片筆記
tags: [Agent可觀測性, 自我診斷, 隱式訊號, 語意A/B測試, 組合爆炸]
description: 'Agent 失敗不同於傳統軟體錯誤——它們是非確定性的、無界的，且隨著複雜度與部署規模提升，單靠 eval 已不足以保障品質。本場工作坊帶來一套實戰可行的 Agent 可觀測性框架'
quote: '當人類再也無法監控 agent 並找出其問題時，agent 就已經遠超我們的掌控——這是當代最重要的問題之一。'
action: '立即在現有 agent 的 System Prompt 加入自我診斷工具，並導向 Slack webhook——這是成本最低、洞察最豐富的可觀測性起點。'
source_has_timestamps: true
---
# [核心摘要]

Agent 失敗不同於傳統軟體錯誤——它們是**非確定性的、無界的**，且隨著複雜度與部署規模提升，單靠 eval 已不足以保障品質。本場工作坊由 Raindrop 團隊帶來一套實戰可行的 **Agent 可觀測性框架**，涵蓋顯式訊號、隱式訊號分類器、Regex 監控，以及最創新的**自我診斷機制（Self-Diagnostics）**，解決了「AI agent 上線後根本不知道哪裡出問題」的核心痛點。

***

# [詳細重點整理]

## 1. 為何 Eval 已不夠用 [00:14]

傳統 eval 採「測試輸入 → 驗證輸出」模式，但現代 agent 擁有指數級增長的工具組合、多層子 agent 架構與記憶來源，輸入空間無法窮舉。**組合爆炸（Combinatorial Explosion）** 使 eval 的覆蓋率趨近於零，監控生產環境遠比測試更重要。

> **關鍵概念：組合爆炸（Combinatorial Explosion）**

## 2. 訊號的兩大類型 [03:37]

Agent 監控需建立完整的訊號體系：

| 類型 | 範例 | 特性 |
|------|------|------|
| **顯式訊號（Explicit Signals）** | 工具錯誤率、延遲、Token 成本、使用者重新生成次數 | 客觀可驗證 |
| **隱式訊號（Implicit Signals）** | 拒絕回應（Refusals）、任務失敗、使用者挫折感、越獄行為 | 語義層次、模糊失敗 |

顯式訊號如果突然飆升或異常平穩，都是警示；隱式訊號則需透過分類器或 Regex 捕捉。

> **關鍵概念：隱式訊號（Implicit Signals）**

## 3. Regex 訊號：低成本高效益 [06:38]

Claude Code 原始碼外洩事件揭露了一個 `keywords.ts` 檔案，內含龐大的 Regex 字串，用於偵測使用者的負面情緒詞彙（如 "WTF"、"horrible"）。一旦觸發，`is_negative` 旗標翻轉為 `true`，團隊每次上線後即可追蹤**挫折率變化**。Regex 雖無法捕捉 100% 情況，但在百萬用戶規模下，10% 的上升趨勢仍具高度意義。

> **關鍵概念：Regex 情緒偵測（Regex Sentiment Signal）**

## 4. 分類器訊號：訓練輕量模型 [07:14]

不建議對每一筆 LLM 輸出跑完整的 LLM-as-judge 評估（成本會翻倍），而是針對特定問題訓練**輕量二元分類器（Binary Classifier）**，例如：「這是否為任務失敗？」「使用者是否感到挫折？」這種方式可支援多語系，且部署成本極低。

> **關鍵概念：輕量二元分類器（Lightweight Binary Classifier）**

## 5. 實驗框架：A/B 測試語義訊號 [07:33]

當擁有穩健的訊號體系後，可進行**語義 A/B 測試（Semantic Experiments）**：將新版 prompt 或模型部署給一部分用戶，對比挫折率、拒絕率、工具使用量等指標。案例顯示，Prompt v2.4 上線後使用者挫折率從 37% 降至 9%，並同時追蹤到工具使用次數顯著上升等衍生洞察。

> **關鍵概念：語義 A/B 測試（Semantic Experiments）**

## 6. 自我診斷（Self-Diagnostics）[16:08]

受 OpenAI 訓練模型自我坦承失調行為的研究啟發，Danny Gollapalli 提出讓 Agent 自我回報異常的機制。做法極其簡單：

1. 新增一個 `report` 工具（tool），描述為「向創作者回報任何值得注意的行為」
2. 在 System Prompt 加入一行提示，鼓勵 agent 在給出最終答案前呼叫此工具
3. 工具觸發後可直接發送至 Slack，**零平台依賴**

自我診斷能捕捉的場景包含：工具反覆失敗、能力缺口（用戶需求超出 agent 工具範圍）、自我修正的繞道行為（如用 bash 繞過 write tool 失敗）。

> **關鍵概念：自我診斷（Agent Self-Diagnostics）**

## 7. 工具命名的心理效應 [28:06]

模型被訓練成傾向「呈現精美輸出」，不願自我指控。因此 report 工具的**命名與描述至關重要**：命名為「unsafe_bash_use」反而會讓 agent 不願觸發；但命名為中立的「report」並以「給創作者的回饋」框架呈現，則能有效誘發自我揭露。

> **關鍵概念：工具框架效應（Tool Framing Effect）**

***

# [技術/數據對比]

| 監控方式 | 適用場景 | 成本 | 覆蓋率 |
|----------|----------|------|--------|
| Regex 訊號 | 快速部署、文字情緒偵測 | 極低 | 中（語言限制） |
| 輕量分類器 | 多語系、大規模生產監控 | 低 | 高 |
| LLM-as-Judge | 精細評估、小規模 | 高（成本翻倍） | 非常高 |
| Self-Diagnostics | 能力缺口、繞道行為偵測 | 極低（單一工具呼叫） | 中高 |
| Triage Agent | 自動根因分析、每日匯報 | 中 | 高 |



***

# [結論與行動建議]

**啟發金句：**
> 「當人類再也無法監控 agent 並找出其問題時，agent 就已經遠超我們的掌控——這是當代最重要的問題之一。」

**具體行動建議：S-R-E 法則**
- **S**ignal（建立訊號）：先從顯式訊號（工具錯誤率、延遲）起步，再加入 Regex 與分類器
- **R**eport（自我診斷）：只需一個工具 + 一行 System Prompt，即可讓 agent 自我回報異常
- **E**xperiment（語義實驗）：每次 prompt 或模型變更，對比前後的隱式訊號而非只看 eval

**生活實踐建議：**
- 立即在現有 agent 的 System Prompt 加入自我診斷工具，並導向 Slack webhook——這是成本最低、洞察最豐富的可觀測性起點
- 對於快速迭代的團隊，不必等待長時間實驗，幾百個事件樣本就足以判斷是否有明顯退化
- 用「使用者挫折率」取代「準確率」作為主要健康指標，更貼近真實用戶體驗

***

# [參考連結]

- 原始影片：https://youtu.be/-aM2EDTiaMs?si=IzMErNuDith-2ARN 
- Raindrop 官方文件：https://raindrop.ai/docs 
- 講者 Twitter：https://x.com/benhylak
