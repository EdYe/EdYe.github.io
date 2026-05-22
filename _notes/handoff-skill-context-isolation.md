---
title: '/handoff 技能：用任務切片解決上下文汙染問題'
date: 2026-05-22
image: /images/影片筆記/handoff-skill-context-isolation.jpeg
category: 影片筆記
tags: [上下文預算, Compact限制, 任務切片, Sub-Agent迴路, 工具中立]
description: '/handoff 技能解決了 AI 編程工作階段中的上下文汙染問題。當一個工作階段進行到一半，需要分支處理另一個任務時，既不想中斷現有進度、也不想用 compact 覆蓋狀態，/handoff 能將當前 session 的精要壓縮為一份 Markdown 文件，無縫傳遞給全新的獨立 Agent。'
quote: '把任務邊界管理清楚，就是讓 AI 保持聰明的最佳方法。'
action: '規劃新功能時，用 Grilling → handoff → Prototype session 的三段式流程，確保規劃與實作的 context 互不汙染。'
source_has_timestamps: true
---
## [核心摘要]

`/handoff` 技能解決了 AI 編程工作階段中的**上下文汙染問題**。當一個工作階段進行到一半，需要分支處理另一個任務時，既不想中斷現有進度、也不想用 compact 覆蓋狀態，`/handoff` 能將當前 session 的精要壓縮為一份 Markdown 文件，無縫傳遞給全新的獨立 Agent，實現多工作階段的並行與協作。 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

***

## [詳細重點整理]

### 1. 上下文窗口的「聰明區」與「愚蠢區」 [01:36]

雖然 Claude 等模型宣稱支援 100 萬 token 上下文，但實際上在 **~120K token** 後，Attention 機制開始分散，回應品質明顯下降，即進入「**愚蠢區（Dumb Zone）**」。有效工作範圍遠比標稱值小得多，因此需要主動管理 context budget。 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

> **關鍵概念：上下文預算管理（Context Budget Management）**

***

### 2. Compact 的用途與侷限 [01:36–04:49]

`/compact` 將長對話壓縮成摘要並繼續在**同一個 session** 中推進，適合長時間 debug 或持續迭代同一問題。但每次 compact 都會在 session 開頭累積「沉積層（sediment）」，而且無法將工作分支到一個獨立的新 session，這是它的根本侷限。 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

> **關鍵概念：沉積式壓縮（Sedimentary Compaction）**

***

### 3. /handoff 的核心設計理念 [04:49–06:14]

`/handoff` 的關鍵差異在於：它將 context 中**特定任務的切片**輸出為獨立的 `handoff.md`，存至 OS 暫存目錄（非 workspace），使當前 session 保持純粹，並讓新 Agent 從乾淨的起點接手。指令中明確要求：不重複已在其他 artifacts 中的內容（用指標代替）、隱去敏感資訊（API key / PII）、並包含「建議 Skills 清單」讓下一個 session 能立即進入狀態。 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

> **關鍵概念：任務切片轉移（Task Slice Handoff）**

***

### 4. 實戰模式一：Grilling 中途分支 [06:14–07:20]

在 Grilling（規劃詢問）session 進行中，若發現某個需求超出當前 scope，用 `/handoff <任務描述>` 即可：一方面讓目前的 Grilling session 「範疇收斂」更清晰，另一方面同步將該任務的必要背景輸出給另一個 Agent 執行。說明任務目的是寫出高品質 handoff document 的關鍵步驟。 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

> **關鍵概念：範疇隔離（Scope Isolation）**

***

### 5. 實戰模式二：原型驗證迴路 [07:20–09:23]

Grilling session → `/handoff` 給 Prototype session → Prototype session 完成後再 `/handoff` 回原始規劃 session，形成一個**DIY Sub-Agent 迴路**。這個模式讓你能用完整的 context window 進行單一任務（如 UI 原型、複雜邏輯），再將學習成果壓縮回主線，極大提升複雜功能的設計品質。 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

> **關鍵概念：DIY Sub-Agent 迴路（Sub-Agent Loop）**

***

### 6. 跨 Agent 工具中立性 [09:23–09:50]

因為 handoff 文件只是純 Markdown，可以跨越不同工具生態：從 Claude Code 傳給 Codex、Copilot CLI 或任意其他 coding agent。這個特性使得**對抗性評審（Adversarial Review）**——即讓兩個不同 AI 互相審查——變得非常容易實現。 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

> **關鍵概念：工具中立傳遞（Tool-Agnostic Handoff）**

***

## [技術設計細節對比]

| 功能 | `/compact` | `/handoff` |
|------|-----------|------------|
| 作用範圍 | 同一 session | 跨 session / 跨 Agent |
| 輸出形式 | 內部摘要 | 獨立 Markdown 文件 |
| 原 session 狀態 | 被覆蓋 | 完整保留 |
| 適用場景 | 長時間 debug、持續迭代 | 任務分支、原型驗證、跨工具協作 |
| 儲存位置 | session 內部 | OS 暫存目錄（可拋棄） |

 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

***

## [結論與行動建議]

**啟發金句：**
> 「把任務邊界管理清楚，就是讓 AI 保持聰明的最佳方法。」

**核心法則：S-H-R 法則（Scope → Handoff → Resume）**
1. **Scope（範疇收斂）**：發現 out-of-scope 任務時，立刻識別，不要把它塞進當前 session
2. **Handoff（切片轉移）**：用 `/handoff <任務目的>` 明確描述下一個 session 的焦點，輸出 Markdown
3. **Resume（無縫接續）**：新 session 載入 handoff.md，讓 Agent 從高品質起點重新出發

**生活實踐建議（適合 AI 應用架構師）：**
- 規劃新功能時，用 Grilling → handoff → Prototype session 的三段式流程，確保規劃與實作的 context 互不汙染
- 建立個人 Skills 庫（如 Matt 的 skills repo），將這些 handoff 模式封裝為可重用 prompt，降低每次操作的認知成本
- 對需要評審的重要設計決策，嘗試「跨 Agent 對抗性評審」：Claude 設計 → Codex 審查，提升架構品質 [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)

***

## [參考連結]

- 原始影片：https://youtu.be/dtAJ2dOd3ko?si=IlIq1UoZ-Fa9gF6z [youtube](https://www.youtube.com/watch?v=zr-WE_XAfdc)
- Matt Pocock 的 Skills Repo：https://aihero.dev/s/YL1zWx
- AI Coding For Real Engineers 課程（6/1 開始）：https://aihero.dev/s/z2UZDd
