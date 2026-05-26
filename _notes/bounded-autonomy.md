---
title: 'Bounded Autonomy：AI Agent 設計的有界自主性框架'
date: 2026-05-26
image: /images/AI筆記/bounded-autonomy.jpeg
category: AI筆記
tags: [有界自主性, 複雜度陷阱, Agent設計, 極簡化, 爆炸半徑]
description: 'AI Agent 開發的最大陷阱不是技術能力不足，而是過度複雜化。Oliver 每天為 200 多個品牌生成約 4,000 個創意素材，其核心經驗是：模型天生傾向冗長，開發者也是。'
quote: '永遠不要自動化一件你自己都不會做的工作。'
action: '用 M-E-B 法則設計 Agent：從最少 context 開始，定義明確升級觸發條件，依爆炸半徑劃定自主邊界。'
source_has_timestamps: true
---
# 📝 Bounded Autonomy：在自由意志與決定論之間

**影片：** Angus J. McLean（Oliver AI Director）@ AI Engineer Conference，2026年4月

***

## [核心摘要]

AI Agent 開發的最大陷阱不是技術能力不足，而是**過度複雜化**。Oliver 每天為 200 多個品牌生成約 4,000 個創意素材，其核心經驗是：模型天生傾向冗長，開發者也是。解法不是加更多工具或上下文，而是**極簡化**——用最少的 context 完成任務，永遠不要自動化一件你自己都不會做的工作。 [youtube](https://www.youtube.com/watch?v=yzIE0uZFao8)

***

## [詳細重點整理]

### 1. 複雜度陷阱 [00:00 起]

Angus 花了大量時間打造一個複雜 Agent 來生成他的履歷，最終發現四個字母就打敗它：**HTML**。他估計簡化帶來的效能提升高達 **100 倍**。 這說明了工程師常見的反模式：用 AI 解決其實根本不需要 AI 的問題。 [youtube](https://www.youtube.com/watch?v=yzIE0uZFao8)

**關鍵概念：** **複雜度通膨（Complexity Inflation）**——開發者與模型雙方都有過度設計的本能傾向。

### 2. Oliver 的大規模 Agent 實踐 [約 02:00]

Oliver 作為廣告創意公司的 AI 總監，每天透過 Agent 為全球 200+ 品牌生產約 4,000 個創意素材，而品牌主通常毫不知情這些素材出自 AI。 這代表 AI Agent 在創意產業的**工業化落地**已是現在進行式，而非未來願景。 [ie.oliver](https://ie.oliver.agency/generative-ai/)

**關鍵概念：** **AI Inside™**——將 AI 嵌入品牌行銷引擎的全流程，而非作為獨立工具使用。 [ie.oliver](https://ie.oliver.agency/generative-ai/)

### 3. 三大核心反直覺原則 [約 05:00]

這是 Angus 從實戰中提煉出的設計哲學： [youtube](https://www.youtube.com/watch?v=yzIE0uZFao8)

- **用精選文件取代網路存取**：不給 Agent 開放式的 internet access，改用策劃好的文件庫，降低幻覺與不可預測性
- **問「最少需要多少 context？」**：反向思考，從削減上下文開始，而非堆疊
- **不要自動化你自己都不會的工作**：沒有人類能力基線，就無法設計正確的 Agent 邊界

**關鍵概念：** **最小有效 Context（Minimal Effective Context）**——以夠用為原則，避免資訊噪音。

### 4. Bounded Autonomy（有界自主性）的本質 [約 10:00]

**Bounded Autonomy** 是本次演講的核心框架：給予 Agent 在明確邊界內自主行動的能力，觸及邊界時強制升級至人類判斷。 實作上包含三個要素： [tianpan](https://tianpan.co/forum/t/bounded-autonomy-the-pattern-thats-actually-working-for-ai-agent-deployment-in-2026/1258)

- **Clear Limits**：明確定義 Agent 能做與不能做的事
- **Mandatory Escalation**：不確定時必須請求人類介入
- **Audit Trails**：每個決策都記錄推理過程以利學習 [tianpan](https://tianpan.co/forum/t/bounded-autonomy-the-pattern-thats-actually-working-for-ai-agent-deployment-in-2026/1258)

**關鍵概念：** **爆炸半徑（Blast Radius）**——邊界設定應基於操作失敗的影響範圍，而非任務複雜度。 [tianpan](https://tianpan.co/forum/t/bounded-autonomy-the-pattern-thats-actually-working-for-ai-agent-deployment-in-2026/1258)

***

## [技術/數據對比]

| 維度 | 複雜 Agent 路線 | 極簡化路線（Angus 方法）|
|---|---|---|
| CV 生成案例 | 複雜 Agent 流程 | HTML（效率提升 100x） [youtube](https://www.youtube.com/watch?v=yzIE0uZFao8) |
| 上下文策略 | 開放 internet + 大量 context | 精選文件 + 最小 context [youtube](https://www.youtube.com/watch?v=yzIE0uZFao8) |
| 自主程度 | 全自主（高風險）| Bounded Autonomy（有邊界） [tianpan](https://tianpan.co/forum/t/bounded-autonomy-the-pattern-thats-actually-working-for-ai-agent-deployment-in-2026/1258) |
| 適合任務 | 複雜低影響操作 | 高影響操作需人類把關 [tianpan](https://tianpan.co/forum/t/bounded-autonomy-the-pattern-thats-actually-working-for-ai-agent-deployment-in-2026/1258) |
| 失敗模式 | 幻覺、不可預測 | 升級至人工，可稽核 [tianpan](https://tianpan.co/forum/t/bounded-autonomy-the-pattern-thats-actually-working-for-ai-agent-deployment-in-2026/1258) |

***

## [結論與行動建議]

**啟發金句：**
> **「永遠不要自動化一件你自己都不會做的工作。」**
> — 沒有人類基線能力，就無法設計出有效的 Agent 邊界。

**具體行動建議：** **M-E-B 法則**
- **M（Minimal）**：從最少 context 開始設計，逐步加入
- **E（Escalate）**：定義明確的升級觸發條件
- **B（Bounded）**：依據「爆炸半徑」劃定 Agent 自主邊界

**生活實踐建議：**

1. **下次開發 Agent 前**，先手動完成一次完整流程，確認你真的理解每個步驟
2. **建立精選文件庫**取代讓 Agent 自由搜尋，可大幅提升輸出穩定性
3. **用「這個操作失敗的代價是什麼？」**作為每個自動化決策的第一道過濾器
4. 作為 AI 應用架構師，可將 Bounded Autonomy 框架直接套用到客戶的 Agent 設計審查流程中

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/t4359sKBu4w?si=1kqzCL0xiF_k2ep4
- 🔗 講者 LinkedIn：https://uk.linkedin.com/in/angusjmclean
- 🏢 Oliver Agency AI：https://ie.oliver.agency/generative-ai/
