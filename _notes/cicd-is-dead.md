---
title: 'CI/CD Is Dead — 代理時代的持續運算革命'
date: 2026-05-14
image: /images/AI筆記/cicd-is-dead.jpeg
category: AI筆記
tags: [持續運算, Agent Loop, 合併佇列, 多宇宙探索, CI轉型]
description: '傳統 CI/CD 是為「人類每週推送一兩個 diff」設計的序列化流程。當 AI Agent 以千倍規模持續產生 PR 時，runner 飽和、快取失效、merge queue 序列化瓶頸等問題使整個架構崩潰。'
quote: 'You, as a human, are the agent — and now the machines are replacing that role in the loop, but not the intent.'
action: '以 Intent → Validate-in-loop → Merge-by-intent 三步驟重構開發流程，讓 build/test 內嵌於 Agent harness，review 從看 diff 轉向確認意圖是否達成。'
source_has_timestamps: true
---
# CI/CD Is Dead — 代理時代的持續運算革命

**來源影片：** AI Engineer Conference — Madison Faulkner (NEA 合夥人) × Hugo Santos (Namespace CEO)
**時長：** 18分37秒 ｜ **發布日期：** 2026年5月13日

***

## [核心摘要]

傳統 CI/CD 是為「人類每週推送一兩個 diff」設計的序列化流程。當 AI Agent 以千倍規模持續產生 PR 時，runner 飽和、快取失效、merge queue 序列化瓶頸等問題使整個架構崩潰。本演講提出以**持續運算（Continuous Compute）**取代 CI/CD，將驗證內嵌至 Agent Loop，並以「意圖＋結果」取代 diff review，讓 merge queue 演化為支援多宇宙平行探索的高效能基礎設施。

***

## [詳細重點整理]

### 1. 傳統 CI/CD 為何在 Agent 規模下崩潰 [00:22]

- 人類開發者每週僅提交 1~2 個 PR，冷啟動 Docker build、本地快取暖機都被人類延遲所掩蓋
- Agent 規模下：N 個 repo × N 個 PR，大量短命 branch 同時競爭同一 codebase
- 合併衝突呈指數成長，merge queue 開始像**序列化資料庫鎖（Serialized DB Lock）**，time-to-commit 成為真正瓶頸
- GitHub 實際 commit 數量與程式碼增刪量在近幾個月出現驚人峰值（白線爆衝）

> **關鍵概念：序列化合併瓶頸（Merge Serialization Bottleneck）** — 大量 agent 並行工作時，git repository 作為單一 ledger 的序列化特性成為整個開發管線的最大限制。

***

### 2. 新架構：無 PR 的 Agent Loop [09:08]

取代傳統 PR 的新流程：

- **Intent & Plan（意圖與計畫）** — 以線性 ticket 或 Slack 訊息定義目標，取代 diff 作為工作單元
- **Agent Harness 內建驗證** — Agent checkout 已知 commit → 實作 → build/test（內部驗證）→ 回報人類 → 繼續
- **人類審查意圖結果，非程式碼** — "這是功能執行影片" / "這是安全 LLM 的評估結果"
- **Pre-merge Queue（預合併佇列）** — 已完成但待序列化的變更在此排隊，支援語義分組，讓人類可管理高流量

> **關鍵概念：Pre-merge Queue（預合併佇列）** — 介於 Agent Loop 完成與 git ledger 提交之間的緩衝層，提供可序列化保證同時解耦人類審查頻率。

***

### 3. 外部驗證的去人化：Agent 評審 Agent [11:36]

- 人類從 code reviewer 轉型為**意圖核准者（Intent Approver）**
- 外部驗證改由專業 LLM 擔任：安全聚焦 LLM、API 規範一致性 LLM 等
- 這些 LLM 以**有狀態環境（Stateful Environment）**運行 — 記憶體與狀態至關重要，從零啟動只會拖慢整個 loop
- 世界訊號（plan 變更、他人搶先合併）可動態修改 intent，觸發新一輪 loop

> **關鍵概念：有狀態內部迴圈（Stateful Inner Loop）** — Agent 需要持久化的運算環境（非無狀態的 ephemeral runner），才能在高頻迭代下維持效率。

***

### 4. 終極形態：多宇宙並行探索（Multiverse） [15:22]

- 未來數週至數月內，code 生成速度 + 驗證速度將快到讓「repo tip」成為移動靶
- Agent 將同時對**多個 commit** 進行同一計畫的探索，取最佳路徑合併
- 此模式下資源用量將爆炸性成長，效能與效率的 co-design（硬體+軟體協同設計）成為決定性因素
- Namespace 的解法核心：**增量運算（Incremental Compute）**，避免重複從零開始，讓 Agent 如同在自己的工作站上工作

> **關鍵概念：多宇宙提交探索（Multiverse Commit Exploration）** — Agent 在同一計畫下並行嘗試多個程式碼路徑，透過評估框架選擇最優解合併。

***

### 5. CI 並未消亡，而是形態轉變 [16:49]

| 傳統 CI 職責 | 新架構中的位置 |
|---|---|
| 程式碼是否可運作 | 內嵌至每次 Agent Loop 迭代 |
| 合規性/已知 checkout 保證 | 仍在，移入 harness invariant 層 |
| 跨變更協調 | 移入 Agent Loop 整體流程 |
| Governance 治理 | 提升至 harness，由流程規範強制執行 |

***

## [結論與行動建議]

**啟發金句：**
> **「You, as a human, are the agent — and now the machines are replacing that role in the loop, but not the intent.」**
> （你作為人類，本來就是那個 Agent；現在機器取代了你在迴圈中的執行角色，但意圖的制定者仍是你。）

**具體行動建議（I-V-M 法則）：Intent → Validate-in-loop → Merge-by-intent）**
1. **Intent 先行**：任何開發任務先寫下明確的 spec，而非直接開始寫 code
2. **Validate 內嵌**：在 Agent harness 設計中，build/test 必須在 loop 內完成，目標 < 2 分鐘
3. **Merge by Intent**：review 機制從「看 diff」轉向「確認意圖是否達成 + 結果證明」

**生活實踐建議：**
- **現在可做的事**：檢視你的 CI/CD pipeline，找出 build/test 中最耗時的步驟，投資讓它快 5 倍以上 — 這是進入 agentic 工作流的前提
- **PM 視角**：開始用 linear ticket 或結構化 spec 定義每個任務的「Intent + Success Criteria」，這就是未來給 agent 的輸入格式
- **架構師視角**：評估 Namespace 等新興 Continuous Compute 平台，傳統 GitHub Actions 的 ephemeral runner 模式在 agent 規模下將成本失控

***

## [參考連結]

- 🎥 原始影片：https://youtu.be/VktrqzQgytY?si=Qx2lXh7I7N8Pq6lG
- 🏢 Namespace：https://namespace.so
- 🐦 Madison Faulkner：https://x.com/madsfaulkner
- 💼 Hugo Santos LinkedIn：https://www.linkedin.com/in/hugomgsantos/
