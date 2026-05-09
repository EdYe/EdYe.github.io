---
title: 'Playground in Production：用 Pydantic AI 在生產環境持續優化 Agent'
date: 2026-05-09
image: /images/AI筆記/playground-in-production.jpeg
category: AI筆記
tags: [生產可觀測性, GEPA, Managed Variables, 線上評估, Pydantic AI]
description: '部署 AI Agent 只是起點，真正的挑戰是在不重新部署的情況下持續優化生產環境中的 Agent 表現。Pydantic CEO Samuel Colvin 展示了「生產環境→評估→自動優化」閉環工作流'
quote: '部署 Agent 只是開始，生產環境中的每一次 Trace，都是讓 Agent 變得更聰明的原料。'
action: '將所有硬編碼的 Prompt 字串遷移至 Logfire Managed Variables，並從現有生產 Traces 中挑選 50-100 筆案例建立評估資料集。'
source_has_timestamps: false
---
## [核心摘要]

部署 AI Agent 只是起點，真正的挑戰是在**不重新部署**的情況下持續優化生產環境中的 Agent 表現。 Pydantic CEO Samuel Colvin 展示了一套完整的「生產環境 → 評估 → 自動優化」閉環工作流，核心工具為 **Pydantic AI**、**Logfire** 與 **GEPA（自動 Prompt 進化）**，解決了「上線後無法快速迭代 Prompt 與模型」的核心痛點。 [startuphub](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/samuel-colvin-on-optimizing-ai-agents-in-production)

***

## [詳細重點整理]

### 1. Playground in Prod — 生產即實驗場 [00:00]
傳統開發流程中，Prompt 調整必須走 CI/CD 才能上線，導致迭代速度極慢。 這個工作坊主張將生產環境本身視為「Playground」，透過 Logfire 內建的 LLM Playground 直接測試 Prompt，每次請求都自動被 trace，實現即時觀測與快速反饋。 [pydantic](https://pydantic.dev/articles/gateway-merging-into-logfire)

**關鍵概念：生產環境可觀測性（Production Observability）**

### 2. Managed Variables — 免重啟動態參數更新 [早段]
**Managed Variables** 是 Logfire 提供的機制，讓開發者可以在不重新部署、不中斷服務的情況下，動態更新 Prompt 內容、切換模型（如 GPT-4o → Claude 3.5）或調整其他 Agent 參數。 這讓 A/B 測試不同 Prompt 變體變得極為輕量，直接對真實流量生效。 [linkedin](https://www.linkedin.com/posts/pydantic_improving-your-agents-in-production-without-activity-7445820063577903104-CGP7)

**關鍵概念：零停機參數熱更新（Zero-Downtime Live Variable Updates）**

### 3. Evals on Real Datasets — 用生產數據跑評估 [中段]
Pydantic Evals 框架支援建立資料集、執行評估、追蹤模型表現，並可在 CLI 或 Logfire UI 可視化結果。 Online Evals 功能讓相同的 Evaluator 類別（如幻覺率、工具調用準確率、回應品質）同時適用於離線開發與線上生產流量的採樣評分。 [pydantic](https://pydantic.dev/articles/online-evals-pydantic-logfire)

**關鍵概念：線上評估（Online Evals）**

### 4. GEPA — 從生產 Trace 自動進化 Prompt [後段]
**GEPA（Generative Evolutionary Prompt Adaptation）** 是整套閉環的核心：它分析生產 Traces 與使用者回饋信號，自動生成更優化的 Prompt 候選版本，實現「Prompt 自我進化」。 搭配 Managed Variables，GEPA 輸出的最佳 Prompt 可直接熱更新至生產環境，無需工程師手動介入。 [x](https://x.com/pydantic/status/2040054364929155119)

**關鍵概念：生成式進化 Prompt 適應（GEPA）**

***

## [技術/數據對比]

| 功能維度 | 傳統做法 | Logfire + Pydantic AI |
|---|---|---|
| Prompt 更新 | 需改程式碼 → PR → CI/CD → 重新部署 | **Managed Variables** 熱更新，零停機  [linkedin](https://www.linkedin.com/posts/pydantic_improving-your-agents-in-production-without-activity-7445820063577903104-CGP7) |
| 評估時機 | 僅在上線前（離線 Evals） | 上線前 + 生產中**同步評估**（Online Evals） [pydantic](https://pydantic.dev/articles/online-evals-pydantic-logfire) |
| Prompt 優化 | 人工調整、靠直覺 | **GEPA** 從 Trace 自動演化最優 Prompt  [x](https://x.com/pydantic/status/2040054364929155119) |
| 可觀測性 | 各系統分散 | OpenTelemetry 統一追蹤 LLM 呼叫、延遲、成本  [mlops](https://www.mlops.wtf/p/ai-agents-in-production-part-4-evaluating) |

***

## [結論與行動建議]

**啟發金句：**
> **「部署 Agent 只是開始，生產環境中的每一次 Trace，都是讓 Agent 變得更聰明的原料。」** [pydantic](https://pydantic.dev/articles/online-evals-pydantic-logfire)

**具體行動建議 — M-E-G 法則：**
- **M（Managed Variables）**：先為所有 Prompt 與模型選擇建立 Managed Variables，確保可以隨時熱更新
- **E（Evals）**：定義核心評估指標（幻覺率、任務完成率），同時啟用 Online + Offline Evals [pydantic](https://pydantic.dev/articles/online-evals-pydantic-logfire)
- **G（GEPA）**：積累足夠的生產 Trace 後，啟動 GEPA 自動優化循環，從人工調 Prompt 過渡到自動演化 [linkedin](https://www.linkedin.com/posts/pydantic_improving-your-agents-in-production-without-activity-7445820063577903104-CGP7)

**生活實踐建議：**
若您目前正在生產環境中運行 Pydantic AI Agent，可立即執行三件事：
1. 將所有硬編碼的 Prompt 字串遷移至 Logfire **Managed Variables** [x](https://x.com/pydantic/status/2040054364929155119)
2. 從現有生產 Traces 中挑選 50-100 筆案例建立評估資料集 [pydantic](https://pydantic.dev/pydantic-ai)
3. 為最關鍵的 Agent 行為（如幻覺、工具誤用）附掛 Online Evaluator，實現自動監控 [pydantic](https://pydantic.dev/articles/online-evals-pydantic-logfire)

***

## [參考連結]

- 原始影片：https://youtu.be/A48uhxfxbsM?si=p3_g2yYuT4T_S-fR
- Pydantic Logfire 官網：https://pydantic.dev/logfire [pydantic](https://pydantic.dev/logfire)
- Online Evals 技術文章：https://pydantic.dev/articles/online-evals-pydantic-logfire [pydantic](https://pydantic.dev/articles/online-evals-pydantic-logfire)
- Speaker Samuel Colvin：https://x.com/samuelcolvin [pydantic](https://pydantic.dev/authors/samuel-colvin)
