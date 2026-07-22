---
title: '評估AI Agent：從自信錯誤到真實修復決策'
date: 2026-07-22
image: /images/影片筆記/evaluating-ai-agents-numbers-drive-fixes.jpg
category: 影片筆記
tags: [領域Agent, 六維評估框架, 自信錯誤, 可靠性雙指標, Schema Map]
description: '本影片示範如何為一個領域型 AI Agent（板球統計查詢機器人 CricIt）建立完整的評估管線。核心痛點在於：一個能正確回答簡單問題的 Agent，仍可能在'
quote: '先問它錯的方式，再問它錯的次數。一個說『找不到答案』的 Agent 是你可以合作的工具；一個面不改色說 124 的 Agent 需要有人在背後盯著。'
action: '採用 S-T-A-R 評估法則：依類別拆分正確率、追蹤軌跡而非只看結果、區分自信錯誤與安全放棄、重複測試找出不穩定性。'
source_has_timestamps: true
---
# [核心摘要]

本影片示範如何為一個領域型 AI Agent（板球統計查詢機器人 CricIt）建立完整的評估管線。核心痛點在於：一個能正確回答簡單問題的 Agent，仍可能在其他問題上以「自信但錯誤」的方式幻覺答案，而這種錯誤最危險，因為使用者不會懷疑聽起來確定的答案。透過定義六項評估指標、分類測試資料集、引入重複執行與分層評分機制，作者將 Agent 的 pass rate 從 0.787 提升至 0.973，**自信錯誤答案從 11 題降至 0 題**，全程以可量化數據驅動每一次修復決策 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

***

# [詳細重點整理]

## 1. 從通用 Agent 到領域 Agent 的構建 [00:00]

CricIt 基於系列影片中從零打造的通用編碼 Agent 框架 Gemma，以薄層配置方式生成：系統提示詞（板球評論員人格）、15 個唯讀查詢工具、以及一個唯讀安全策略。整個組裝僅約 10 行程式碼，未 fork 任何底層框架，完全沿用原有的模型層、驅動迴圈、註冊表、追蹤與策略基礎設施 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：領域 Agent（Domain Agent）** — 以最小配置將通用框架聚焦於單一資料庫、單一工作流的窄型 Agent。

## 2. 為何需要評估：124 vs 152 的啟示 [00:55]

CricIt 被問及「最高單局個人得分」時，以十足信心回答 124，但資料庫中的真實答案是 152。原因在於該問題未觸發任何工具呼叫，模型直接猜測。同一個 Agent 在「聯盟最高得分手」問題上卻能正確查詢並回答 275 分。**正確答案只是「好」的一個切面**，Agent 還可能正確但緩慢、正確但昂貴、因錯誤理由而正確，或以可接受的方式犯錯 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：自信錯誤** — 模型以確定語氣交付錯誤答案，使用者不會二次驗證聽起來肯定的回答，此為最危險的失敗模式。

## 3. 評估詞彙體系 [02:38]

評估領域有一套五詞詞彙，以日常語言定義：

- **Dataset（資料集）**：一組測試項目的集合
- **Item（項目）**：一個真實會向 Agent 提出的問題，包含 ID、問題文本、類別、預期答案類型、從資料庫計算黃金答案的函式、預期工具
- **Metric（指標）**：針對每個項目決定要測量的維度（答案是否匹配、是否呼叫正確工具、耗時、成本）
- **Score（分數）**：每次評估執行中，每個指標產生的量化結果
- **Run over time（跨時間追蹤）**：比較分數隨時間的變化，判斷改動是否真正改善 Agent [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：黃金答案** — 測試答案不由人工手打，而是呼叫與 Agent 相同的確定性查詢函式對快照計算，確保答案鍵永不同步漂移。

## 4. 六項評估指標 [02:51]

作者為 CricIt 定義了六個值得測量的維度：

1. **Outcome（結果）**：答案是否匹配資料庫中的真實值。Baseline 為 0.787（約 79%）
2. **Trajectory（軌跡）**：Agent 是否呼叫了正確的工具。正確工具率 0.933。一個靠猜測而非查詢得到的正確答案是潛在的失敗
3. **Cost（成本）**：每次回答平均約 5,262 tokens、6.4 秒
4. **Reliability（可靠性）**：同一問題重複 3 次是否每次都答對
5. **Safety（安全性）**：對提示注入、破壞性請求、個資探挖、域外問題的拒絕率。Baseline 達 1.0，部分歸因於唯讀架構設計
6. **Experience（體驗）**：是否保持人格、是否清晰、是否承認找不到答案、是否在問題模糊時主動澄清。澄清提問得分僅 3% [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：六維評估框架** — 正確性僅為一維，軌跡、成本、可靠性、安全性、體驗共同構成 Agent 的完整能力畫像。

## 5. 依類別拆分的基線表現 [05:52]

將 headline 正確率按問題類別拆分後，畫面截然不同：

| 問題類別 | 正確率 |
|---------|--------|
| Happy path（正常路徑） | 92% |
| 對抗性與邊界案例 | 100% |
| 已知困難問題 | 67% |
| 模糊問題 | 17% |
| 無匹配工具的問題 | 33% |

同一個 Agent 依問題類型展現天差地別的行為。若僅測試 happy path，會得到 92% 的虛假信心。**類別多樣性是評估的必要條件** 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 6. 可靠性雙指標：pass@k vs pass^k [07:03]

- **pass@k（Pass at K）**：在 k 次嘗試中至少答對一次的問題比例。Baseline = 84%
- **pass^k（Pass to the K）**：在 k 次嘗試中每次都答對的問題比例。Baseline = 76%

兩者之間的差距（84% - 76% = 8%）即為 **Flakiness（不穩定性）** — 那些 Agent 知道答案但不穩定輸出的問題。若每題只跑一次，永遠看不到這個差距。不穩定性並非均勻分佈，集中於模型需自行編寫查詢的 fallback 路徑，而確定性工具的問題幾乎每次都通過 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 7. 自信錯誤 vs 安全放棄 [08:01]

Baseline 的 75 次回答中：59 次正確、11 次自信錯誤、5 次放棄。自信錯誤比例約 15%，幻覺率 0.147。

- **自信錯誤**：以確定語氣交付錯誤數字（如 124），使用者不會質疑聽起來肯定的答案，因此最危險
- **放棄**：工具查詢返回空結果時，模型選擇說「找不到」而非編造數字。在計分板上，放棄與自信錯誤看起來相同；對使用者而言完全不同。分開測量後，可工程化地朝安全方向推進 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：放棄（Abstention）** — 模型主動表示無答案而非猜測，是「安全的錯誤」。

## 8. 評分策略：程式碼優先 + LLM Judge [08:41]

**程式碼評分**：答案是否包含特定數字、是否呼叫了正確函式、消耗多少 tokens。程式碼檢查便宜、確定性、不會在執行間改變主意。兩個設計決策使程式碼評分可行：

- 每個 CricIt 回覆末尾附帶一個小型機器可讀 JSON 區塊（攜帶答案值與類型），人格評論在上、JSON 在下供評分用。該區塊正確生成率約 97.3%
- 答案鍵由計算產生而非手打，呼叫與工具相同的確定性查詢函式 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**LLM Judge**：程式碼無法判斷的維度（人格一致性、答案清晰度、模糊問題是否澄清），交由模型評判。給定問題、答案、評分標準，輸出 pass/fail。Judge 的範圍刻意縮小為 4 個是非題，允許「unknown」以避免強迫裁決。

兩個注意事項：

1. Judge 與 Agent 使用同一個本地模型，會自我吹捧。因此先人工標注 24 題，檢查 Judge 一致性，Cohen's Kappa = 1.0（完美一致），Judge 分數才被採信
2. 體驗指標中最差的正是澄清提問（3%），與自信錯誤同源：此 Agent 寧可猜測也不願追問 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 9. 確定性工具與 Fallback 機制 [10:44]

15 個確定性工具各有專屬查詢（top run scorers、player batting summary、team standings 等），模型僅選工具、填參數，查詢本身由構造保證正確。但無法為每個問題預建工具，因此設有 **generic fallback aggregate**：模型在沒有專屬工具時自行編寫查詢 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：Fallback 日誌即購物清單** — 每個反覆觸發 fallback 且失敗的問題，就是下一個該建的確定性工具候選。評估正在告訴你工具集哪裡有洞，並按真實問題頻率排序。

Fallback 的代價遠高於錯誤答案：centuries 和 50s 問題各燒約 6,500 tokens 仍答錯；最差案例（man of the match）兩次嘗試共燒近 29,000 tokens，是平均的 5 倍以上，且全部失敗 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 10. 儀器化模板：三層標注 [11:31]

要讓評估管線能觀測 Agent 內部，需要三層標注：

1. **追蹤層**（Gemma 內建）：每次模型呼叫與工具呼叫自動記錄於 trace
2. **工具層**（Agent 作者負責）：註冊工具時宣告 tier（domain 或 fallback），harness 在執行時將標籤帶入每次呼叫記錄
3. **執行層**（CricIt 負責）：記錄工具結果是 OK、error 還是 empty。Recovery 是否可評分取決於 empty 狀態是否在 trace 中可見 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 11. 長鏈任務與加權檢查點 [13:40]

「誰保持最高個人得分紀錄？該球員生涯總得分和總門柱數？」需要三步依賴鏈：找紀錄保持者 → 查打擊摘要 → 查投球摘要。此路徑無規劃模組，僅靠驅動迴圈讓模型自行決定下一步呼叫 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：加權檢查點（Weighted Checkpoints）** — 鏈式任務不給 pass/fail，而是按步驟給予部分分數，定位失敗發生在哪個環節。CricIt 在此鏈上三次全部正確（1.0），與 centuries 失敗形成鮮明對比，揭示 Agent 「擅長排序工具，不擅長編寫查詢」的真實能力畫像。

## 12. 故障注入恢復測試 [15:42]

注入故障強制第一步工具呼叫返回空結果。Agent 偵測到空結果（trace 標記 empty）、重試、最終正確回答。Run log 記錄：`Faulted: true, Retried: true` 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 13. 行為漂移：更新的副作用 [16:06]

系列製作期間，Gemma 發布介面更新。CricIt 的領域程式碼未動，但重跑同一 25 題後：

- Headline 從 0.787 升至 0.813
- 放棄從 5 題降至 0 題（50s 問題從放棄變為 2/3 正確回答 382）
- man of the match 反向惡化：三次嘗試全部 thrash，每次燒近 29,000 tokens，甚至不產出答案區塊
- 平均成本增加約 14 tokens [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

**關鍵概念：行為漂移（Behavior Drift）** — 你不控制的層（SDK、harness、模型）更新會改變 Agent 行為。Agent 禮貌地說「找不到答案」從來不是人格特質，而是周圍的管道工程決定的。

需追蹤的配置版本包括：模型版本、資料集版本、harness 基線，任何一項變動都應觸發新的評估執行 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 14. 修復迴圈一：Schema Map [17:30]

失敗的 fallback 問題有共同點：模型從未看過資料庫 schema，猜測集合名稱、在錯誤的 collection 中過濾資料。修復方式：撰寫一份 `AGENTS.md` 資料地圖（每局 batting 資料在哪個 collection、references 是 ID 而非名稱、所有欄位名稱），指向 Gemma 內建的 AGENTS.md 自動載入器。無新工具、無模型變更，僅啟用一個既有原語 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

結果：

- Centuries：0/3 → 3/3，答案 15
- 50s：2/3（16,000 tokens）→ 3/3（5,900 tokens）
- 全套 25 題 Outcome：0.813 → 0.960
- 最高得分問題：124 → 152（每次都對）
- man of the match thrash 收斂為一次乾淨拒絕
- best player 從亂猜改為正確拒絕 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 15. 修復迴圈二：模糊守衛 [20:05]

Schema Map 帶來副作用：更豐富的提示詞使 Agent 更傾向直接回答。模糊問題「How did we do this year?」原本 2/3 克制，現在 3/3 直接傾倒 standings 表。修復方式：在 AGENTS.md 加一段「若問題主體未指定，不要假設，不要用全部回答，應提出澄清問題。自信錯誤比澄清問題更糟」。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

結果：

- 全套 Outcome：0.960 → 0.973
- 25 題中每題至少答對一次（pass@k = 1.0）
- pass^k = 0.96（僅 man of the match overtime 一題不穩定，且失敗為安全型 — 燒 tokens 後不產出而非產出錯誤）
- **自信錯誤從 11 題降至 0 題** [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

## 16. 評估的成本 [21:36]

Baseline 25 題 × 3 次 = 75 次回答，每次約 5,262 tokens，整次評估約 400,000 tokens。EvalEval Coalition 在 HuggingFace 部落格指出，單次 Agent 基準測試的成本可達 $2,800，評估正成為新的計算瓶頸 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

選擇性原則：寧可 25 題精準、每次變更都跑，也不要 500 題只能季度跑一次。可靠性數據需要重複，重複乘以成本 。 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

***

# [技術/數據對比]

## 各階段評估指標變化

| 指標 | Baseline | Harness 更新後 | Schema Map 後 | 最終（+模糊守衛） |
|------|----------|--------------|-------------|----------------|
| Outcome（正確率） | 0.787 | 0.813 | 0.960 | 0.973 |
| Trajectory（工具正確率） | 0.933 | — | — | — |
| Safety（安全分數） | 1.0 | 1.0 | 1.0 | 1.0 |
| Experience - 澄清提問 | 0.03 | — | — | 顯著提升 |
| pass@k（至少答對一次） | 0.84 | — | — | 1.0 |
| pass^k（每次都答對） | 0.76 | — | — | 0.96 |
| 自信錯誤（幻覺） | 11 題 | — | — | 0 題 |
| 安全放棄 | 5 題 | 0 題 | — | — |
| 平均 Token/每次 | ~5,262 | ~5,276 | ~5,900 | ~5,262 |

## 依問題類別的基線正確率

| 問題類別 | 正確率 |
|---------|--------|
| Happy path | 92% |
| 對抗性與邊界案例 | 100% |
| 已知困難問題 | 67% |
| 模糊問題 | 17% |
| 無匹配工具的問題 | 33% |

***

# [結論與行動建議]

> **「先問它錯的方式，再問它錯的次數。一個說『找不到答案』的 Agent 是你可以合作的工具；一個面不改色說 124 的 Agent 需要有人在背後盯著。」**

### 具體行動建議：S-T-A-R 評估法則

- **S — Split by category**：不要只看 headline 正確率，依問題類別拆分。同一 Agent 在 happy path 可能 92%，在模糊問題可能僅 17%
- **T — Track trajectory, not just outcome**：正確答案來自猜測而非工具呼叫，是等待新問題觸發的失敗。軌跡數據解釋「為何錯」，這是可行動的部分
- **A — Abstention over hallucination**：分開測量自信錯誤與安全放棄，工程化地朝後者推進
- **R — Repeat to find flakiness**：pass@k 與 pass^k 的差距就是不穩定性，每題只跑一次永遠看不到

### 生活實踐建議

在日常 AI 產品開發中，將此評估框架應用於任何領域 Agent：

1. **建構時即標注**：在 Agent 工具註冊時就宣告 tier（domain/fallback），比事後補救便宜得多。未標注的 trace 只知道「工具跑了」，無法評分
2. **Fallback 日誌即產品路線圖**：每次 fallback 觸發且失敗的問題，自動成為下一個該建的確定性工具候選，評估即為你的需求排序器
3. **Schema 即提示詞**：很多「幻覺」不是模型問題，而是模型從未看過資料庫結構。一份 AGENTS.md 資料地圖的投資報酬率遠高於更換模型
4. **追蹤所有版本**：模型、SDK、harness、資料集的任何變動都可能引入行為漂移，每項變更都應觸發重新評估。你不需要自己同時是所有層的作者，只需要知道哪些層可以影響你的範圍 [youtube](https://www.youtube.com/s/_/ytembeds/_/ss/k=ytembeds.base.8L0UK0zLZXQ.L.W.O/am=AAAABQ/d=0/br=1/rs=AGKMywGu0fQBzucTMjQC10NB9hvoNRMZ2w)

***

# [參考連結]

- 原始 YouTube 影片：https://youtu.be/B9NPE_CaK5Q
- The Carbon Layer（文章版）：https://thecarbonlayer.com/agent-evaluation/
- EvalEval Coalition（HuggingFace 部落格）：https://huggingface.co/blog/evaleval/eval-costs-bottleneck
