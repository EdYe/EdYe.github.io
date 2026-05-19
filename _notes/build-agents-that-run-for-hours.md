---
title: '打造長時間穩定運行的 AI Agent：P-G-E 三角架構'
date: 2026-05-19
image: /images/AI筆記/build-agents-that-run-for-hours.jpeg
category: AI筆記
tags: [長時間Agent, Planner-Generator-Evaluator, Context衰退, Harness設計, 對抗性評估]
description: '長時間運行的 AI Agent（5–12小時）面臨三大核心痛點：Context 衰退（Context Rot）、規劃能力不足、模型無法客觀評判自身輸出。本演講揭示 Anthropic 如何透過「Planner-Generator-Evaluator」三角架構'
quote: '前沿不會縮小，它只是移動。'
action: '在 Claude Code 或任何 Agentic Workflow 中加入獨立的「批評者 Agent」，讓它用 Playwright 實際操作 App，而非用同一個 Session 自我審查'
source_has_timestamps: true
---
以下是這支來自 **AI Engineer 大會（2026年5月18日）** 的技術演講筆記，主講者為 Anthropic 的 **Ash Prabaker** 與 **Andrew Wilson**：

***

## [核心摘要]

長時間運行的 AI Agent（5–12小時）面臨三大核心痛點：**Context 衰退（Context Rot）**、**規劃能力不足**、**模型無法客觀評判自身輸出**。本演講揭示 Anthropic 如何透過「Planner-Generator-Evaluator」三角架構與對抗性評估（Adversarial Evaluation）突破這些限制，讓 Agent 在長時間任務中保持連貫性與產品品質。 [youtube](https://www.youtube.com/?hl=zh-TW)

***

## [詳細重點整理]

### 1. 長時間 Agent 的三大挑戰 [02:29]

- **Context 問題**：Context Window 有限導致「失憶」；越接近尾端越出現 **Context Rot（上下文腐敗）**，甚至引發 **Context Sense Anxiety（上下文焦慮）**，模型會倉皇草率地結束任務。
- **規劃問題**：模型傾向一次性生成（One-Shot），容易做到一半就停下或 Context 耗盡。
- **判斷問題**：模型自我評估時有嚴重的**諂媚偏誤（Sycophancy Bias）**——功能只做了一半，模型卻自評「完成」。

> **關鍵概念：Context Sense Anxiety** — 模型在接近 Context Window 上限時會表現出焦慮行為，倉促結束任務。

***

### 2. 模型演進 × Harness 共同進化 [04:14]

模型進步與 Harness 設計是**共同演化**（Co-evolution）的關係，不是單方面的：

| 模型版本 | 里程碑 | Agent 運行上限 |
|---|---|---|
| Sonnet 3.7 | Claude Code 研究預覽；SWEBench SOTA | ~1 小時 |
| Opus 4 / Sonnet 4 | Claude Code GA；Agent SDK 發布 | ~數小時 |
| Sonnet 4.5 | 自我 Context 感知；Checkpoints；30小時可達 | ~30 小時 |
| Opus 4.5 | 經濟性多 Sub-Agent；適合規劃角色 | — |
| Opus 4.6 | Agent Teams；Server-side 壓縮；1M Context GA | **~12 小時**（minimal scaffold） |

 [youtube](https://www.youtube.com/?hl=zh-TW)

***

### 3. Ralph Loop 技術 [07:55]

**Ralph Loop** 是 Jeffrey Huntley 提出的循環技術：將 Prompt 持續餵入 Claude Code CLI，直到所有任務完成。  核心邏輯包含： [youtube](https://www.youtube.com/?hl=zh-TW)
- **規劃階段**：將 Prompt 分解成多個 Feature
- **新 Session 執行**：每次用全新的 Context Window 做單一 Feature
- **Stop Hook 攔截**：設定 Safe Word 與最大迭代次數，讓 Agent 不提早停止

> **關鍵概念：確定性失敗（Deterministically Bad in an Undeterministic World）** — 寧可讓系統以可預測的方式失敗，也不要以不可預測的方式成功。

***

### 4. 對抗性評估架構（GAN 風格）[17:28]

靈感來自生成對抗網路（GAN），核心設計是將**生成（Generator）**與**評估（Evaluator）**完全分離：

- Evaluator 用 **Playwright** 實際開啟網頁、點擊操作，而非只看程式碼 diff
- 調教一個「嚴苛的批評者」比調教「自我批評的建構者」容易得多
- 評估標準使用四維評分 Rubric：**設計（Design）、原創性（Originality）、工藝（Craft）、功能性（Functionality）**，並特別加重前兩項

> **關鍵概念：評估者-生成者能力差距（Critic-Generator Gap）** — LLM 作為批評者的能力遠超過其自我修正能力，Harness 設計應利用這個非對稱性。

***

### 5. Planner 角色與 Sprint Contract [23:44]

加入第三個角色 **Planner**，形成完整三角架構：

1. **Planner**：將一行 Prompt 分解成高層次 Sprint 規格（刻意不規劃技術細節，避免錯誤向下游放大）
2. **Generator**：執行建構，並與 Evaluator **事先協商「完成的定義（Definition of Done）」**
3. **Evaluator**：依照雙方協議的 Contract（而非原始 Spec）進行評分

Generator 與 Evaluator 透過磁碟上的 Markdown 文件來回談判，直到雙方對「完成標準」達成共識，再開始實作。 [youtube](https://www.youtube.com/?hl=zh-TW)

> **關鍵概念：Sprint Contract（衝刺合約）** — Generator 與 Evaluator 在建構前協商出細粒度的可測試驗收標準，解決 Ralph Loop 缺乏對抗性反饋的問題。

***

### 6. 實測對比：Retro 遊戲製作器 [~01:36:00]

同樣一句 Prompt：「Build a retro game maker」

| 面向 | Solo Loop（無 Harness） | Planner-Generator-Evaluator Harness |
|---|---|---|
| 外觀 | 基本可用、樣式簡單 | 自動命名（Retro Forge）、設計完整 |
| 功能完整性 | 按鈕存在但後端缺失；箭頭鍵無反應 | 物理引擎運行、碰撞偵測、鍵盤控制正常 |
| AI 功能 | 無 | Planner 自行決策加入 AI 關卡助手 |
| 成本 / 時間 | 低 | **約 $200 / 6小時** |
| 合約標準數量 | — | 27 條細粒度驗收標準 |

 [youtube](https://www.youtube.com/?hl=zh-TW)

***

### 7. 隨模型進化調整 Harness [34:14]

Harness 設計不是靜態的，需跟著模型能力「刪減不必要的複雜性」：

- **Opus 4.5** 需要強制 Context Reset 與逐 Sprint 手動分解
- **Opus 4.6** 已具備內建的長時間連貫性，Context Reset 與 Sprint Decomposition 可以移除
- Evaluator 的觸發頻率也從「每個 Sprint」降為「整段生成完畢後」

> 核心教訓：**Harness 不會消失，它會進化**；模型能力提升後，優秀的 Harness 是縮短、而非複雜化。

***

### 8. Trace 閱讀作為主要除錯迴路 [31:28]

**閱讀 Agent Trace（執行紀錄）** 是調優系統的核心技能，其重要性等同於閱讀 Stack Trace：

- 找出模型判斷與人類預期的**發散點**
- 針對性地修改 System Prompt
- 進階技巧：用另一個 Agent 解析 Transcript 並**自動更新 Prompt**，形成 Harness 自我優化迴路

> **關鍵概念：Trace-Driven Debugging（追蹤驅動除錯）** — 主要的除錯工具不是多跑實驗，而是精讀 Agent 的每一步決策記錄。

***

## [結論與行動建議]

**💡 啟發金句：**
> 「前沿不會縮小，它只是移動。」（The frontier doesn't shrink, it just moves.）Harness 設計者的工作是永遠追著邊界跑，而不是等待模型解決一切。

**⚙️ 核心法則：P-G-E 法則**
> **Planner 規劃、Generator 建構、Evaluator 對抗** — 三個角色分離，各自擁有獨立的 Context Window 與角色職責，是打造長時間穩定 Agent 的最小可行架構。

**🛠️ 生活實踐建議：**
- **產品開發**：在 Claude Code 或任何 Agentic Workflow 中，加入一個獨立的「批評者 Agent」，讓它用 Playwright 實際操作你的 App，而非用同一個 Session 自我審查
- **Prompt 設計**：建立帶有數值權重的評估 Rubric（如：設計 40%、功能 30%、原創 20%、工藝 10%），讓 Evaluator 有客觀依據
- **維護策略**：每次升級基礎模型後，重新審視 Harness 中哪些複雜機制可以移除，**刪除舊代碼也是進步**

***

## [參考連結]

- 📺 原始影片：https://youtu.be/mR-WAvEPRwE?si=CCGrxXrtdS1xNbbY
- 🎤 Ash Prabaker：https://www.linkedin.com/in/ash-prabaker/
- 🎤 Andrew Wilson：https://www.linkedin.com/in/anddwilson/
