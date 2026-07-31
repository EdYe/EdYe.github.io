---
title: 'Wayfinder：消除規劃戰爭迷霧'
date: 2026-07-31
image: /images/影片筆記/wayfinder-fog-frontier-destination.jpg
category: 影片筆記
tags: [Wayfinder, 戰爭迷霧, 票券系統, Issue Tracker, 命名目的地]
description: 'Wayfinder 是 Matt Pocock 開發的 AI 規劃技能（skill），核心解決了「大型工作無法在單一 agent session 內完成」的痛點。'
quote: '💡Planning is no longer the AI bottleneck — the bottleneck is knowing when to start charting instead of charging.'
action: '🎯將大型 AI 系統遷移拆解為 research／prototype／grilling 票券，用 GitHub issue 的 blocking 關係管理依賴，確保每個決策都有可追溯的一手來源。'
source_has_timestamps: true
---
# [核心摘要]

Wayfinder 是 Matt Pocock 開發的 AI 規劃技能（skill），核心解決了「大型工作無法在單一 agent session 內完成」的痛點。它將模糊的構想映射為 issue tracker 上的共享地圖（map），透過 **決策票券（decision tickets）** 逐一消除 **戰爭迷霧（fog of war）**，直到通往目的地的路徑清晰可見。不同於傳統單 session 規劃工具，Wayfinder 能跨越多個 agent session 編排研究、原型、討論與任務，並在 GitHub、Linear、Jira 等任意 issue tracker 中追蹤所有決策與阻塞關係 。 [github](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)

***

# [詳細重點整理]

## 1. 現有規劃工具的侷限性 [00:00]

既有規劃工具（包含作者自建的 `grill-with-docs` 技能）過度綁定於單一 session，導致使用者被迫將大型工作手動拆成小塊以適應 AI 的 context window 上限。問題在於，拆解過程中常在規劃階段就遇到無法回答的問題或迷失在迷霧中，同時還要不斷管理 token 消耗。**技能倉庫（Skills repo）** 已上線一段時間且廣受歡迎，甚至有人基於 Wayfinder 方法論自建了 harness 工具 。 [youtube](https://www.youtube.com/watch?v=F3lL98Pj90o)

**關鍵概念：Session 瓶頸** — 單一 agent session 的 context window 限制導致規劃野心被壓縮。

## 2. 大型工作的規劃本質與 Wayfinder 地圖機制 [02:10]

大型工作的本質是：你有起點和模糊的目的地，但中間步驟被「迷霧」籠罩。第一步是透過 **grilling session**（AI 訪談你）釐清基本方向。對於小工作這已足夠，但大量工作仍需要後續的 prototype session、額外 grilling 或 research session。每個 session 的產出都是地圖上的一張票券（ticket），每張票券需要獨立的 agent session 來處理 。 [youtube](https://www.youtube.com/watch?v=F3lL98Pj90o)

Wayfinder 在地圖上呈現兩個區域：
- **Frontier（前線）**：目前已知、可以立即決策的票券
- **Fog of war（戰爭迷霧）**：尚未能決策的事項，因為研究不足、缺乏原型或討論不夠 [github](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)

**關鍵概念：戰爭迷霧（Fog of War）** — 刻意不描繪看不見的路徑，隨著前線推進逐步消除迷霧並生成新票券 。 [github](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)

## 3. 透過 Issue Tracker 追蹤決策 [04:30]

Wayfinder 將地圖與所有票券存儲在 issue tracker 中。地圖是一個標記為 `wayfinder:map` 的主 issue，其下掛載子 issue 作為決策票券。每張票券的決議結果會寫回父地圖的 "Decisions so far" 區段，作為一行摘要加連結。地圖是 **索引而非存儲** — 決策只存在於其票券中，地圖僅提供 gist 與連結 。 [github](https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md)

技能本身是 **issue tracker 無關（tracker-agnostic）** 的，透過 `/setup-matt-pocock-skills` 配置即可支援 GitHub、Linear、Jira 等任意平台 。 [github](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md)

**關鍵概念：索引而非存儲（Index, not Store）** — 地圖僅索引決策，不重複存儲，避免資訊冗餘與不一致。

## 4. 啟動與遍歷地圖 [05:39]

啟動新 Wayfinder session 的第一步是 **命名目的地（destination）**。以作者實際案例為例，他想在 CVM 圖表視窗中加入 command palette（含 icon picker、搜尋其他圖表、複製元素等功能），目的地是一份可建構的 spec。

運作流程：
1. 呼叫 Wayfinder 技能並描述需求
2. 技能探索 repo 後觸發 grilling，詢問「完成是什麼樣子」
3. 自動建立初始地圖與第一批票券（案例中立即生成 7 張，但僅 3 張可立即執行）
4. 每張可執行票券在獨立 session 中處理 — 呼叫 `wayfinder <ticket-name>` 即可 [youtube](https://www.youtube.com/watch?v=F3lL98Pj90o)

**關鍵概念：命名目的地（Naming the Destination）** — 目的地決定 scope，是地圖編製的第一個動作 。 [github](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)

## 5. 票券類型與阻塞關係 [07:40]

Wayfinder 定義四種票券類型，分為需要人類介入（HITL）與 agent 自主完成（AFK）兩類 ： [github](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)

| 類型 | HITL/AFK | 用途 |
|------|----------|------|
| Research | AFK | agent 透過 `/research` 子代理查閱文檔、API 或知識庫，回報事實 |
| Prototype | HITL | 透過 `/prototype` 製作低成本原型，提升討論保真度 |
| Grilling | HITL | 透過 `/grilling` 與 `/domain-modeling` 逐一討論實作細節 |
| Task | HITL 或 AFK | 需在真實世界完成的前置工作（註冊服務、搬移資料等） |

票券之間存在 **阻塞關係（blocking relationships）** — 某些決策必須在其他決策完成後才能進行。阻塞使用 issue tracker 原生的 dependency 機制，使其在 tracker UI 中視覺化呈現。票券被 **認領（claim）** 後會 assign 給開發者，避免併發 session 衝突 。 [github](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md)

**關鍵概念：阻塞關係（Blocking Dependencies）** — 透過原生 issue tracker 依賴機制視覺化呈現前線，人類無需開啟地圖即可判斷可執行的票券。

## 6. 從地圖生成 Spec 與實作票券 [09:44]

地圖完成後，透過 `/to-spec` 技能將地圖轉化為 spec 文件。作者案例中，生成的 spec 初稿甚至超過 GitHub 字元上限，足見其密度。Wayfinder 建立的 spec 最大優勢在於 **每個決策都連結回原始票券（primary source）** — agent 在實作時若對任何細節有疑問，可直接查閱原始討論 。 [youtube](https://www.youtube.com/watch?v=F3lL98Pj90o)

Wayfinder 在工作流中的定位：
```
Wayfinder（地圖規劃）→ /to-spec（規格）→ /to-tickets（實作票券）→ 實作 → code review
```

這取代了原本 `grill-with-docs → to-spec → to-tickets` 的流程，在規劃階段投入更多時間以產出更高品質的 spec 。 [linkedin](https://www.linkedin.com/posts/karlweinmeister_matt-pocock-just-shipped-skills-11-and-activity-7482587310241394688-O7r7)

**關鍵概念：可追溯性（Traceability）** — spec 中每個決策連結回原始票券，克服了傳統 spec 僅為會議摘要、缺乏一手資料的弱點。

## 7. 何時使用 Wayfinder 與 FAQ [11:38]

使用判斷準則：若工作可在單一 session 內完成且規劃，就直接在單一 session 處理，無需 Wayfinder。Wayfinder 專為 **戰爭迷霧** 場景設計 — 你不知道路怎麼走，需要邊走邊釐清 。 [youtube](https://www.youtube.com/watch?v=F3lL98Pj90o)

作者也將 Wayfinder 應用於非編碼場景，如規劃花園辦公室建置（委託 site survey、研究廠商、聯繫供應商等）。

針對「這是不是 spec-driven development（SDD）？」的質疑，作者的觀點是：spec 僅是多 session 工作的 **目的地文件**，實作完成後即關閉 issue 並刪除 spec，**不持久化**。不同於傳統 SDD 持續維護與修改 spec 。 [youtube](https://www.youtube.com/watch?v=F3lL98Pj90o)

**關鍵概念：非持久化規格（Non-persistent Spec）** — spec 僅作為多 session 工作的導航終點，實作完成後即丟棄，不持續維護。

***

# [技術/數據對比]

| 維度 | 傳統單 Session 規劃 | Wayfinder 多 Session 規劃 |
|------|---------------------|---------------------------|
| Session 限制 | 綁定單一 session，受 context window 上限約束 | 跨越多個 session，每張票券一個 session |
| 決策追蹤 | 依賴 spec 作為唯一真相來源（僅為會議摘要） | 每個決策連結回原始票券（primary source） |
| 迷霧處理 | 無法系統性處理未知區域 | 戰爭迷霧機制，隨前線推進逐步消除 |
| 阻塞管理 | 手動追蹤依賴 | 原生 issue tracker dependency 視覺化 |
| 原型整合 | 需額外手動安排 | 內建 prototype 票券類型，防止 waterfall |
| 並行能力 | 無 | 透過 claim 機制支援併發 session |
| Spec 持久性 | 持續維護修改 | 非持久化，實作後即關閉刪除 |
| 適用場景 | 路徑清晰的小型工作 | 路徑模糊的大型跨 session 工作 |

 [linkedin](https://www.linkedin.com/posts/karlweinmeister_matt-pocock-just-shipped-skills-11-and-activity-7482587310241394688-O7r7)

***

# [結論與行動建議]

> **「Planning is no longer the AI bottleneck — the bottleneck is knowing when to start charting instead of charging.」**

**F-F-D 法則（Fog-Frontier-Destination）：**
- **Fog**：承認迷霧存在，不強行規劃看不見的路徑
- **Frontier**：每次只推進前線一張票券，解鎖新視野
- **Destination**：先命名目的地固定 scope，再逐層消除迷霧

**生活實踐建議：**
對於 AI agent 系統架構師而言，Wayfinder 的思維可直接應用於企業級 MCP 伺服器部署或多 agent 編排專案。將大型 AI 系統遷移（如知識圖譜整合、IdP 對接）拆解為 research 票券（調查 Neo4j/Graphiti API 限制）、prototype 票券（驗證 context graph 建模方案）、grilling 票券（與 stakeholders 確認資料治理邊界），透過 GitHub issue 的 blocking 關係自動管理依賴順序，確保每個決策都有可追溯的一手來源 。 [docs.plannotator](https://docs.plannotator.ai/frameworks/matt-pocock-skills)

***

# [參考連結]

- 原始 YouTube 影片：https://www.youtube.com/watch?v=F3lL98Pj90o
- Skills Repo（GitHub）：https://github.com/mattpocock/skills
- Wayfinder SKILL.md：https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md
- Wayfinder Issue Tracker 設定文件：https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md
- Skills v1.1 Release Notes：https://github.com/mattpocock/skills/releases
- AI Hero Skills 課程：https://aihero.dev/s/wEMEBn
- 安裝指令：`npx skills@latest add mattpocock/skills`
