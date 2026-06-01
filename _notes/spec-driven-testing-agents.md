---
title: 'Spec-Driven Testing：讓 AI Agent 既聰明又安全的驗證框架'
date: 2026-06-01
image: /images/AI筆記/spec-driven-testing-agents.jpg
category: AI筆記
tags: [規格驅動驗證, AI Agent, 安全測試, 健壯性, 實作無關性]
description: 'AI Agent 越聰明不代表越安全——大型模型因理解能力更強，反而更容易被詩歌包裝的惡意指令所劫持。本影片提出「規格驅動驗證（Spec-Driven Validation）」框架，要求開發者在測試 AI Agent 時，超越傳統資料集評估，從規則、本體論、角色權限到健壯性需求'
quote: '你追求的不是最聰明的 Agent，而是足夠聰明、且不會造成任意傷害的 Agent。'
action: '建立獨立的 agent-spec.yaml，將業務規則、術語表、角色權限分開記錄，並納入 Git 版本控管。'
source_has_timestamps: true
---
# 🎯 Spec-Driven Testing for Agents With A Brain the Size of A Planet
**講者：Steven Willmott｜SafeIntelligence CEO｜AI Engineer Conference, 2026-05-31**

***

## [核心摘要]

AI Agent 越聰明不代表越安全——大型模型因理解能力更強，反而更容易被詩歌包裝的惡意指令所劫持。本影片提出「**規格驅動驗證（Spec-Driven Validation）**」框架，要求開發者在測試 AI Agent 時，超越傳統資料集評估，從規則、本體論、角色權限到健壯性需求，全面定義 Agent 的行為邊界，從而兼顧能力與安全。

***

## [詳細重點整理]

### 1. 更大不等於更安全 [00:07]

大型模型具備更強的語言理解能力，這反而讓它成為更容易被攻擊的目標。 用詩歌包裝惡意指令時，小型模型看不懂詩，大型模型卻能解讀並執行其中的惡意命令。

**關鍵概念：攻擊面悖論（Attack Surface Paradox）** — 能力越廣的 Agent，可被利用的表面積越大，安全測試的難度也成比例提升。

***

### 2. 資料集評估的根本局限 [01:44]

傳統 ML 評估依賴資料集 + F1/Accuracy，但這只能告訴你模型在已知樣本上的表現，無法保證「某條規則永遠不被違反」。 例如客服 Agent「永不給超過 10% 折扣」這類硬性規則，光靠測試集無法窮舉驗證。

**關鍵概念：規則不可窮舉性（Rule Non-exhaustibility）** — 真實部署場景中的業務規則需要獨立於資料集的形式化驗證機制。

***

### 3. Spec-Driven Validation 的五大組成要素 [05:01]

一份完整的 Agent Spec 需包含以下層次 ：

- **Ground Truth 資料集**：已知的良好輸入輸出範例
- **業務規則（Rules）**：例如「退貨需在 30 天內提出」等硬性限制
- **本體論與詞彙表（Ontologies）**：如特定航空公司只飛特定航線，內部術語不得混用（gross profit ≠ gross sales）
- **角色與權限（Rights & Roles）**：登入 vs 未登入、不同權限層級的行為差異
- **健壯性需求（Robustness Requirements）**：拼字錯誤、換句話說，能容忍多少語言變體？

**關鍵概念：健壯性包絡（Robustness Envelope）** — 類比視覺模型在霧天、夕陽下的偵測能力，語言模型需定義語言噪聲下的可接受範圍。

***

### 4. Spec 的雙重應用：安全測試 × 迭代優化 [08:48]

Spec 不只是測試規格，更是安全滲透測試的攻擊地圖 ：
- Agent 被允許討論的領域 = 最脆弱的攻擊入口
- Agent 在基礎設施中擁有操作權限的任務 = 最高風險區域

同時，Spec 可驅動自動化的「偽 RL 循環」：執行 Agent → 收集失敗案例 → 填補健壯性缺口 → 反覆迭代。

**關鍵概念：規格驅動安全迴路（Spec-Driven Security Loop）**

***

### 5. 實作建議：Spec 獨立於實作之外 [11:12]

Agent Spec 必須與底層模型或框架解耦 。無論你現在用 LangSmith、Vertex AI Agents 或其他平台，當你替換模型或基礎設施時，整套整合測試、單元測試、滲透測試都應能原封不動地繼續執行。

**關鍵概念：實作無關性（Implementation Independence）** — 類比 OpenAPI Spec（講者本人參與撰寫）對 REST API 的標準化，未來 Agent Spec 也應成為可版本管理的開放標準。

***

## [結論與行動建議]

**啟發金句：**
> **「你追求的不是最聰明的 Agent，而是足夠聰明、且不會造成任意傷害的 Agent。」** 

**核心法則：R-R-O-R-R 五層規格法則**
> **Rules（規則）→ Roles（角色）→ Ontology（本體）→ Robustness（健壯性）→ Repeatability（可重複驗證）**

**生活實踐建議：**
1. **立即行動**：在你的 AI 應用專案中，建立一份獨立的 `agent-spec.yaml`，將業務規則、術語表、角色權限分開記錄，並納入 Git 版本控管。
2. **安全思維轉換**：當你的 Agent 被設計用來回答某類問題時，那個領域恰好也是你最需要針對性做滲透測試的地方。
3. **健壯性壓力測試**：定期對你的 Agent 進行「噪聲測試」—故意在 Prompt 中加入拼字錯誤、同義改寫，觀察回應是否一致。

***

## [參考連結]

- 🎥 原始影片：[https://youtu.be/UQKg0td-Bf4](https://youtu.be/UQKg0td-Bf4) 
- 🔗 講者 LinkedIn：[https://uk.linkedin.com/in/stevenwillmott](https://uk.linkedin.com/in/stevenwillmott) 
- 🏢 SafeIntelligence：[https://x.com/njyx](https://x.com/njyx)
