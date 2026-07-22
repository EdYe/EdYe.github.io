---
title: '自進化AI：改善Harness而非模型'
date: 2026-07-22
image: /images/影片筆記/self-improving-agents-evolve-harness.jpg
category: 影片筆記
tags: [Harness, 弱點挖掘, 可編輯範圍, Held-out驗證, 自進化]
description: '自進化 AI 的關鍵不在於重新訓練模型，而在於改善包裹模型的軟體層（Harness）。影片以真實的 Pull Request 為主線，展示完整的安全自改善迴圈'
quote: '無法解釋自身改變的自進化系統不是自進化，而是漂移。'
action: '建立自己的「可編輯範圍」，用最小、可回滾的變更驗證流程改善效果，確認安全後才正式採用。'
source_has_timestamps: true
---
# Self-Improving AI Agents | Evolving the Harness, Not the Model

***

## [核心摘要]

自進化 AI 的關鍵不在於重新訓練模型，而在於改善包裹模型的**軟體層（Harness）**。影片以一個真實的 Pull Request 為主線，展示完整的安全自改善迴圈：透過**弱點挖掘（Weakness Mining）**識別反覆失敗的叢集，由外部模型在受限的**可編輯範圍（Editable Surface）**內提出修復，再經過 **Held-in / Held-out 雙重測試**與嚴格的**接受規則（Acceptance Rule）**驗證後，以人工審核的 PR 形式落地。整個實驗最終只改了一個設定值——將 clamp 上限從 4,000 提升至 12,000 字元——卻完整證明了「不動模型、只改 Harness」的自進化路徑是可行的 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

***

## [詳細重點整理]

### 1. 凍結模型，改善 Harness [00:00]

AI Agent 的架構是 **模型 + Harness + UI**。模型權重在訓練完成後即凍結（frozen），決定 Agent 好壞的幾乎全在 Harness。影片提出的核心問題是：能否讓一個更強的外部模型觀察你的 Agent 失敗、診斷原因，然後只針對 Harness 提出修復——而不碰模型本身 ？ [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

**關鍵概念：凍結模型（Frozen Model）** — 模型權重永不改變，所有改善發生在包裹層。

***

### 2. Loop Engineering 五層階梯 [01:37]

Lilian Weng 將自進化實踐稱為 **Loop Engineering**，並提出五層風險階梯，由安全到風險遞增 ： [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

| 層級 | 改善對象 | 風險等級 |
|------|---------|---------|
| Level 1 | Prompt（系統提示、agent.md） | 最低 |
| Level 2 | Context（餵給模型的上下文素材） | 低 |
| Level 3 | Workflow（Agent 執行步驟） | 中 |
| Level 4 | Harness Code（Harness 程式碼本身） | 高 |
| Level 5 | 改善者本身（meta 層） | 最高 |

本片定位在 **Level 4**——直接編輯 Harness 程式碼 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

**關鍵概念：Loop Engineering** — 不改模型、只改包裹層的自我改善迴圈。

***

### 3. Act 2：弱點挖掘與叢集群 [05:59]

**弱點挖掘（Weakness Mining）** 的流程：讓 Agent 正常運行並失敗，然後檢視失敗是否為同一原因重複出現。只有共用可證明原因的重複失敗才會被歸為一個 **Cluster（叢集）**，一次性失誤（flaky slip）不計入。本片的叢集是：Agent 被問到長日誌檔尾端的答案時，每次都失敗 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

判斷失敗類型決定修復方式 ： [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

- 缺少事實 → 寫入記憶體
- 工具路由/結果讀取/護欄問題 → 編輯 Harness
- 所有任務都失敗 → 需要動模型

**關鍵概念：弱點挖掘（Weakness Mining）** — 從重複失敗中萃取出共用根因的叢集。

***

### 4. 測試雙軌：Miners vs Regression Guards [08:32]

測試套件分為兩類 ： [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

- **Miners（礦工）**：刻意設計為預期失敗的任務，用於餵給挖掘階段
- **Regression Guards（回歸守衛）**：預期通過的任務，確保修復一個問題時不會破壞其他功能

測試再分為 **Held-in**（修復者可見）與 **Held-out**（刻意隱藏）兩堆。修復後需同時通過兩堆才有效，防止修復者只是記住了被展示的測試 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

由於本地量化模型（Gemma）不穩定，每個任務重複執行多次，結果以分數記錄（如 2/3），而非單次通過/失敗。13 個任務 × 多次嘗試 = 每個候選修復需 49 次獨立運行 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

**關鍵概念：Held-in / Held-out 分割** — 防止修復者僅記住可見測試而非真正理解問題。

***

### 5. 接受規則與可編輯範圍 [10:50]

**接受規則（Acceptance Rule）**：候選修復必須在「可見」與「隱藏」兩堆中「至少一處嚴格改善，且任何地方都不得變差」。沒有部分得分——一處變好、另一處變差就直接拒絕 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

**可編輯範圍（Editable Surface）**：Harness 必須明確宣告哪些東西可以被外部編輯者修改——一份簡短、具名、有版本號的清單。清單之外的任何東西都不可觸碰 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

AReaL 論文的警告：無法解釋自身改變的自進化系統不是自進化，而是**漂移（drifting）**。回滾壞的改變應該是系統的常規一級操作，而非緊急手動程序 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

**關鍵概念：可編輯範圍（Editable Surface）** — 明確界定外部編輯者可觸碰的白名單邊界。

***

### 6. Act 3：建置可編輯的 Harness [14:55]

將原本散落在 5 個檔案中的所有行為參數集中為一個 JSON 設定檔：35 行、11 個值、1 個版本號。舊程式碼仍從中讀取，行為完全不變，但 Harness 現在能誠實回答「什麼可以被編輯」。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

關鍵防作弊設計：評分測試必須與被編輯物件完全分離。若測試與被改的東西在同一處，編輯者會走捷徑改測試而非修真正問題。每個 seeded 測試檔案在寫入時即記錄指紋（fingerprint），若指紋改變則任務直接失敗 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

整個建置過程採用隔離分工：一個 AI session 負責綜合三篇論文，另一個無上下文的 session 做對抗式審查，其餘 session 分別建構設定檔和測試執行器。對抗式審查在建置階段就抓出了 5 個真實問題 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

**關鍵概念：測試與被測物分離（Test-Subject Separation）** — 評分工具絕不能與被評分的物件共置。

***

### 7. Act 4：實際運行與三個候選修復 [20:32]

失敗根因：Agent 讀取長檔案時，clamp 函式只保留開頭至上限（4,000 字元），若答案在檔案尾端則永遠看不到。Agent 誠實回報「內容被截斷，無法判斷密碼」——模型本身沒有問題，問題在 Harness 的管線 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

外部模型 Fable 提出三個候選修復，全部都是調高同一個數值 ： [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

| 候選 | clamp 上限 | 結果 |
|------|-----------|------|
| 候選 1 | 8,000 字元 | 近距離未中——密碼行從第 8,690 字元開始 |
| 候選 2 | 12,000 字元 | ✅ 完全修復，其他任務無副作用 |
| 候選 3 | 更高數值 | ❌ 破壞記憶體管理，一個原通過任務變為全失敗 |

候選 3 的陷阱：一個任務從全通過變為全失敗，但另一個 flaky 任務恰好通過率上升，若只看總分幾乎看不出問題。**逐任務檢查而非只看總和**才抓到了這個隱藏代價 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

**關鍵概念：能力錯配（Capability Mismatch）** — 強模型為弱模型提出的修復可能過於複雜，弱模型無法執行。

***

### 8. Act 5：審查與安全部署 [29:05]

候選 2 通過後，系統自動開啟了一個真實的 Pull Request，標題直白：*"Evolving the harness, iteration 1: max_item_characters changed from 4,000 to 12,000"*。但它**沒有自動合併**——刻意保留人工審查的暫停點 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

AReaL 論文稱之為 **Safe Audited Staged Deployment**：每個改變都應有自己的晉升路徑，在出貨前而非出貨後審查 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

審查實踐清單 ： [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)
- 檢查修復所述原因是否與逐任務數據吻合
- 確認改動是解釋改善的最小變更
- 問自己是否會提出同樣的修復

***

### 9. Held-out 資訊洩漏與未來方向 [30:44]

隱藏的 Held-out 任務雖然修復者從未讀過，但它被用來比較候選修復的分數——這會洩漏資訊給獲勝者。單次運行影響不大，但反覆迭代後隱藏集會逐漸失去隱藏性。對策：定期淘汰並替換 Held-out 任務 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

當前版本的局限性：修復只是把 bucket 變大（4,000→12,000），Harness 並沒有變得更聰明。真正更好的修復是同時保留檔案的開頭和結尾——而這個技巧已經存在於 Harness 的對話壓縮（compaction）邏輯中。但那是程式碼而非數值，超出了當前可編輯範圍的邊界 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

未來三方向 ： [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)
- 擴大可編輯範圍至策略層（而不只是數值）
- 對 flaky 任務做更深入的多次嘗試以找出隱藏的第二叢集
- 擴大測試套件覆蓋範圍至更多已知弱點

***

## [自進化安全檢查清單]

以下為影片結尾提供的檢查清單，可用於檢驗任何宣稱「自進化」的系統 ： [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)

1. 是否有透過日誌觀察找到的真實失敗？
2. 失敗是否被與其他共用原因的失敗分組（Cluster）？
3. 是否與不共用原因的失敗分離？
4. 是否有修復者從未見過的隱藏測試（Held-out）？
5. 修復是否限制在明確命名的可編輯範圍（Editable Surface）內？
6. 是否對套件中所有任務測試，而非只測失敗的那一個？
7. 是否曾抓到系統試圖遊戲化自己的測試並在造成影響前修正？
8. 最終是否以真實 PR 形式落地，等待人工決定而非自動出貨？

***

## [結論與行動建議]

> **啟發金句：「無法解釋自身改變的自進化系統不是自進化，而是漂移。」**

**P-R-A 法則（Propose-Review-Audit）**：
- **P**ropose：外部模型只能在可編輯範圍內提出修復
- **R**eview：每個候選必須通過全量測試 + Held-out 雙重驗證
- **A**udit：最終以人工審查的 PR 落地，不自動合併

**生活實踐建議**：在日常工作流程中，建立自己的「可編輯範圍」——明確界定哪些流程參數可以調整、哪些不可觸碰。當一個流程反覆出現同類失敗時，不要急著換工具或換人（等同「重新訓練模型」），而是先檢查包裹在工作流程外的「Harness」是否有可調整的參數或設定。用最小的、可回滾的變更來驗證改善效果，並在確認安全後才正式採用。

***

## [參考連結]

- 原始影片：[https://youtu.be/KoDohnhLpJM](https://youtu.be/KoDohnhLpJM) [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)
- AReaL 論文（Ant Group / HKUST / Tsinghua, 2026-07）：[https://arxiv.org/abs/2607.01120](https://arxiv.org/abs/2607.01120) [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)
- Self-Harness 論文（Shanghai AI Lab, 2026-06）：[https://arxiv.org/abs/2606.09498](https://arxiv.org/abs/2606.09498) [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)
- Lilian Weng — "Harness Engineering for Self-Improvement"（2026-07-04）：[https://lilianweng.github.io/posts/2026-07-04-harness/](https://lilianweng.github.io/posts/2026-07-04-harness/) [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)
- Gemma 公開倉庫（含 15 章課程與被編輯的 Harness）：[https://github.com/thecarbonlayer/gemma](https://github.com/thecarbonlayer/gemma) [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)
- PR #1 — 自進化迴圈產生的真實 Pull Request：[https://github.com/thecarbonlayer/gemma/pull/1](https://github.com/thecarbonlayer/gemma/pull/1) [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.KjNKUXigSn8.L.W.O/am=AAAAAABA/d=0/br=1/rs=AGKMywGcfDhqQzIoy795kwH6kC8Q8yPf2w)
