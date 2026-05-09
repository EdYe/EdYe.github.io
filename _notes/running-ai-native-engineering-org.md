---
title: '打造 AI-Native 工程組織：重寫舊流程的實戰指南'
date: 2026-05-09
image: /images/影片筆記/running-ai-native-engineering-org.jpeg
category: 影片筆記
tags: [AI原生組織, 瓶頸轉移, JIT規劃, 強制Dogfooding, 工程流程]
description: '當 AI Coding 工具從個人輔助升級為組織預設工作模式，原本為「昂貴的人工編碼」所設計的流程（Design Doc、Code Ownership、六個月 Roadmap）會悄悄失效。'
quote: 'What served you prior may not serve you any longer.——曾經有效的，不代表現在依然有效。'
action: '找出你團隊中「最吵鬧的一個工作流」，問自己「它現在仍然服務原本的目的嗎？」，若答案模糊，先把它砍掉，觀察三週。'
source_has_timestamps: true
---
# Running an AI-Native Engineering Org

**核心洞察：** 當 AI 程式碼生成能力讓工程頻寬不再是瓶頸，組織的流程、審查機制與團隊結構本身才是真正需要重構的物件。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [核心摘要]

本影片由 Anthropic Claude Code 工程總監 Fiona Fung 主講，揭示了一個關鍵痛點：**當 AI Coding 工具從個人輔助升級為組織預設工作模式**，原本為「昂貴的人工編碼」所設計的流程（Design Doc、Code Ownership、六個月 Roadmap）會悄悄失效。影片系統性地分享了 Claude Code 團隊如何識別瓶頸轉移，並重寫團隊規範，讓 AI-native 組織能持續高速且高品質地交付。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [詳細重點整理]

### 1. 瓶頸已轉移，舊流程悄悄失效 [00:02]

過去「工程頻寬昂貴」催生了瀑布式、敏捷式開發、預規劃、Code Ownership 等制度。現在**程式碼生成已非瓶頸**，新的瓶頸轉向了：驗證（Verification）、程式碼審查（Code Review）、跨部門協作（Security、Legal）、以及維護成本。

> **關鍵概念：** **瓶頸轉移（Bottleneck Shift）** — 流程應服務當下瓶頸，而非歷史遺留瓶頸。

***

### 2. 規劃節奏從「六個月 Roadmap」轉為 JIT 規劃 [08:44]

六個月 Roadmap 的前提是「程式碼昂貴，要算好再動手」。現在 Fiona 採用 **Just-In-Time（JIT）規劃**：不寫 Design Doc，改為直接 PR 或 Prototype。產品辯論不再靠白板，而是**直接用 Claude 生成三個實作版本來比較**，讓技術辯論從抽象討論進化為「以程式碼為證據的討論」。

> **關鍵概念：** **JIT 規劃（Just-In-Time Planning）** — 原型生成成本趨近於零，計劃的粒度與時效性應隨之提升。

***

### 3. Code Review：重新定義「何時需要人工審查」[13:55]

Claude 負責處理 Linting、Style、簡單 Bug Fix 與補測試。人工審查則保留在三個核心場景：
- **法律與安全敏感程式碼**（Risk Tolerance 高）
- **信任邊界（Trust Boundary）**相關邏輯
- **產品品味與設計感**（Product Sense）

> **關鍵概念：** **Trust but Verify（信任但驗證）** — AI 審查提升速度，人工審查保衛邊界。

***

### 4. Code Ownership 模糊化後的正確提問方式 [12:36]

「誰改了這段程式碼？」這個問題在 AI 協作下已失去意義，真正要追問的是：
- 誰是這個領域的**專家**？
- 誰可以**解答客戶問題**？
- **怎麼自動化**這個查詢本身？

> **關鍵概念：** **雙重點擊提問（Double-Click Ownership）** — 所有權問題的背後是情境問題，應直接問對問題，而非找責任人。

***

### 5. 團隊組成：招聘策略的兩個核心 Profile [15:45]

Fiona 重點強調兩種工程師 Profile：
- **具產品感的創意建造者（Creative Builders with Product Sense）**：好奇心強、能快速迭代解決使用者問題
- **深度系統專家（Deep Systems Expertise）**：分散式系統、基礎架構——這是 AI 無法輕易取代的硬核能力

**刻意降低重視的能力**：原始程式碼產出量（Raw Throughput），因為模型已大幅補足了這一塊。

> **關鍵概念：** **能力稀缺重組（Capability Re-scarcity）** — AI 讓部分能力變得充裕，組織應重新押注真正稀缺的人才維度。

***

### 6. 組織扁平化與 Dogfooding 文化 [18:00]

**所有管理者須先以 IC（Individual Contributor）身份上任**，親身使用 Claude Code，累積「街頭信譽（Street Cred）」，才能升為 Manager。這打破了傳統 10:1 IC:Manager 模型，保持組織高度扁平化與敏捷。

> **關鍵概念：** **強制性 Dogfooding（Mandatory Dogfooding）** — 技術領導者必須成為自家產品的深度使用者，才能做出正確的工程與產品決策。

***

### 7. 三大團隊強制規範（Must-Do Norms）[20:41]

Claude Code 團隊強制執行的核心規範：
1. **所有成員（含非工程職）**都使用 Claude Code
2. **Claudify Everything** — 任何可自動化的事情，優先考慮交給 Claude
3. **明確授權殺死舊流程（Explicit Permission to Kill Old Processes）** — 流程不會自動消亡，必須主動審查並廢除

***

### 8. 衡量成效的三個核心指標 [23:06]

| 指標 | 趨勢 | 說明 |
|------|------|------|
| **Onboarding Ramp-up Time** | ↓ 大幅縮短 | 工程師、PM、設計師上手速度 |
| **PR Cycle Time** | ↓ 縮短 | 若沒有縮短，代表 CI/CD 等下游管線成為新瓶頸 |
| **Claude-assisted Commit 比率** | ↑ 趨近 100% | Claude Code 團隊近四個月已無非 AI 協助提交 |

***

## [結論與行動建議]

**啟發金句：**
> **「What served you prior may not serve you any longer.」——曾經有效的，不代表現在依然有效。**

**具體行動法則：** **B-K-C 法則**
- **B（Bottleneck）**：先找到當前真正的瓶頸在哪裡
- **K（Kill）**：明確授權團隊殺死已無效的舊流程
- **C（Claudify）**：把釋放出來的人力集中到 AI 無法取代的高價值工作

**生活實踐建議：**
找出你團隊中「最吵鬧（最耗能）的一個工作流」——可能是週會、狀態報告、Design Doc、Code Review SLA——問自己一個問題：**「它現在仍然服務原本的目的嗎？」** 如果答案模糊，先把它砍掉，觀察三週，看看缺少它之後真正損失了什麼。

***

## [參考連結]

原始影片：[https://youtu.be/igO8iyca2_g](https://youtu.be/igO8iyca2_g) [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
