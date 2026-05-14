---
title: 'AI Agent 可觀測性：縮短偵測到診斷的落差'
date: 2026-05-15
image: /images/AI筆記/agent-observability-mind-the-gap.jpeg
category: AI筆記
tags: [可觀測性, Agent評估, OpenTelemetry, 追蹤診斷, 紅隊測試]
description: 'AI Agent 在生產環境中具有不確定性，隨著模型更換、Prompt 調整、邊緣案例累積，Agent 的實際行為與預期需求之間的「落差」會悄然擴大。'
quote: '可觀測性的真正價值，不是讓你知道出了什麼錯，而是讓你縮短從偵測到診斷的時間。'
action: '從建置第一天就接入追蹤與評估，善用 Observe Skill 自動生成測試資料並回滾最佳 Prompt'
source_has_timestamps: true
---
# Mind the Gap (In your Agent Observability)
**Amy Boyd & Nitya Narasimhan, Microsoft | AI Engineer 大會 — 2026年5月14日**

***

## [核心摘要]

AI Agent 在生產環境中具有**不確定性（Non-determinism）**，隨著模型更換、Prompt 調整、邊緣案例累積，Agent 的實際行為與預期需求之間的「落差（Gap）」會悄然擴大。本影片展示 Microsoft Foundry 的完整可觀測性（Observability）技術棧，涵蓋追蹤、評估、紅隊測試，並示範如何透過一個 Coding Agent Skill，從零自動生成評估資料集、優化 Prompt 並回滾至最佳版本，解決「不知道自己不知道什麼問題」的核心痛點。

***

## [詳細重點整理]

### 1. 為什麼要「Mind the Gap」[00:14]

「Mind the Gap」不只是倫敦地鐵的警示語，更是 Agent 可觀測性的精準比喻：
- **月台（Platform）= 需求**，**列車（Train）= Agent**——兩者之間存在不確定的落差
- Agent 上線後，模型更新、客戶行為改變、環境演化都會讓這個落差悄悄擴大
- **可觀測性三大支柱**：評估（Evaluate）→ 監控（Monitor）→ 優化（Optimize）

**關鍵概念：** **Agent 可觀測性生命週期（Agent Observability Lifecycle）**

***

### 2. Microsoft Foundry 可觀測性技術棧 [00:53]

Microsoft Foundry 是端對端的雲端 Agent 平台（`ai.azure.com`），可觀測性橫跨三個階段：

| 階段 | 技術手段 | 重點說明 |
|------|---------|---------|
| 建置期 | OpenTelemetry 追蹤（Tracing） | 記錄每個工具呼叫、訊息流程，支援跨平台 Agent 匯入 |
| 生產期 | 評估器（Evaluators）+ 監控 | 品質、安全、Agent 特定指標（意圖解析、任務遵從度） |
| 艦隊管理期 | 紅隊測試（Red Teaming）+ 集中控制平面 | 第二個 AI 對你的 Agent 發動對抗性攻擊，找出漏洞 |

**關鍵概念：** **OpenTelemetry 標準化追蹤（OTel-based Tracing）**

***

### 3. Agent 評估的三層架構 [01:37]

以天氣查詢 Agent 為例，說明評估不是一次性的，而是貫穿整個工作流程：

1. **意圖解析（Intent Resolution）**：使用者問「倫敦今天天氣」，Agent 是否正確理解意圖並決定呼叫工具？
2. **工具呼叫評估（Tool Call Evaluation）**：呼叫的工具是否符合預期？（不確定性意味著用百分比衡量）
3. **任務遵從度（Task Adherence）**：最終回應是否完成了使用者的整體任務目標？

> ⚠️ **任務遵從度是最需要持續調整的指標**——Demo 中 Agent 直接回「請給我更多資訊」而非回答問題，任務遵從度評分明顯偏低。

**關鍵概念：** **任務遵從度評估（Task Adherence Evaluation）**

***

### 4. 「零資料起點」：Observe Skill 示範 [01:00]

這是本影片最核心的技術展示——當你剛加入一家公司，老闆要你建立 Travel Agent，但**沒有任何歷史資料、沒有評估基準**，怎麼辦？

- **Path 1（SDK 路徑）**：適合新手，逐步手動建置 Agent → 追蹤 → 評估
- **Path 2（Observe Skill 路徑）**：只需建立一個空白 Agent Endpoint，然後對 Coding Agent 下一個 Prompt，它會：
  - 自動生成評估資料集
  - 執行批量評估
  - 優化 Prompt
  - 比較不同版本
  - 自動回滾到最佳版本
- Skill 的關鍵價值在於**展示推理過程**，讓你看見「你不知道自己不知道的失敗點」

**關鍵概念：** **零基評估自動化（Zero-Shot Evaluation Automation）**

***

### 5. 追蹤與診斷的閉環加速 [02:06]

可觀測性的真正價值不是「知道出錯了」，而是**縮短從偵測到診斷的時間**：

- **追蹤連結評估（Trace-Linked Evaluations）**：每條 Trace 都連結對應的評估分數，讓你精確定位問題發生在哪個步驟
- 實際案例：更換模型後，工具呼叫效率下降 → 評估指標報警 → 回到 Trace 比較新舊版本 → 發現某個工具沒被呼叫 → 立即修復
- 安全防護（Safeguarding）與品質評估的差異：品質評估是「建築師驗收」，紅隊測試是「找駭客試著攻破你的房子」

**關鍵概念：** **追蹤連結評估（Trace-Linked Evaluation）**

***

## [技術/數據對比]

| 對比項目 | 品質評估（Quality Eval） | 紅隊測試（Red Teaming） |
|---------|------------------------|----------------------|
| 假設前提 | 用戶正常使用 | 有惡意用戶主動攻擊 |
| 類比 | 建築師驗收（Building Inspector） | 請駭客試著破門（Pen Tester） |
| 執行方式 | 自動化評估器、定期排程 | 第二個 AI 發動對抗性 Prompt |
| 開源支援 | 內建評估器 + 自訂評估器 | PyRIT 開源儲存庫 + 平台一鍵版 |



***

## [結論與行動建議]

**啟發金句：**
> 「可觀測性的真正價值，不是讓你知道出了什麼錯，而是讓你縮短從偵測到診斷的時間。」

**具體行動建議（E-M-O 法則）：**
- **E（Evaluate Early）**：從建置第一天就接入 App Insights，啟用追蹤與評估指標，別等到上線才想到
- **M（Monitor Continuously）**：設定排程評估與持續評估（CI/CD 觸發），讓品質退化在被用戶發現前就報警
- **O（Optimize Automatically）**：善用 Observe Skill，對 Coding Agent 下 Prompt，讓它替你生成測試資料、優化並回滾 Prompt

**生活實踐建議：**
如果你正在開發 AI Agent 產品，立即到 `ai.azure.com` 建立 Foundry 專案，Fork 官方 Workshop 的 GitHub Repo（勾選「包含所有分支」），用 Codespaces 在瀏覽器中免安裝啟動開發環境，2 天的雲端費用約 10 美元。加入 Microsoft Foundry Discord 的 AI Engineer 頻道，可獲得免費資源協助。

***

## [參考連結]

- 📺 原始影片：https://youtu.be/iOXM3zE-2dk?si=99IAjkRGusmIRJSb
- 🐦 Amy Boyd (Twitter)：https://x.com/AmyKateNicho
- 🐦 Nitya Narasimhan (Twitter)：https://x.com/NityaNarasimhan
- 💼 LinkedIn — Amy：https://www.linkedin.com/in/amykatenicho/
- 💼 LinkedIn — Nitya：https://www.linkedin.com/in/nityan/
