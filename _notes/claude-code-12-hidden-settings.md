---
title: 'Claude Code 12項隱藏設定技巧'
date: 2026-07-10
image: /images/AI筆記/claude-code-12-hidden-settings.jpg
category: AI筆記
tags: [權限白名單, Deny Rules, Plan-Execute模型分層, Effort Level, Context衰退]
description: 'Claude Code 提供數百項設定，但僅需 12 項一行設定即可徹底改變日常工作流。涵蓋通知提醒、權限管理、模型成本優化、資料隱私控制、上下文品質維護等面向'
quote: '瓶頸不再是模型本身，而是你能否縮短「你要求的」與「真正需要發生的」之間的差距。'
action: '依 S.P.E.E.D. 法則設定 settings.json：啟用通知、建立權限白名單與Deny Rules、模型分層與Effort調校、隱私與Auto-compact優化、給目標不給步驟。'
source_has_timestamps: true
---
# [核心摘要]

Claude Code 提供數百項設定，但僅需 12 項一行設定即可徹底改變日常工作流。涵蓋通知提醒、權限管理、模型成本優化、資料隱私控制、上下文品質維護等面向，解決開發者最常見的痛點：等待權限確認的時間浪費、API 額度快速耗盡、上下文衰退導致品質下降，以及歷史記錄無故消失。所有設定均集中在 `~/.claude/settings.json` 單一檔案中完成，無需撰寫任何程式碼 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

***

# [詳細重點整理]

### 1. 啟用通知音效 [00:15]

輸入 `/config` 開啟設定介面，找到 `local notifications` 選項，透過空白鍵切換通知方式（terminal bell、ghosty 等），讓 Claude Code 完成任務或需要權限確認時即時通知桌面。同場加映 Dave Schumacher 開發的 **Claude Sounds** 庫，可作為 notification hook 替代方案，提供趣味語音提醒。

**關鍵概念：非同步通知機制（Asynchronous Notification）**

***

### 2. 遠端控制推播通知 [01:53]

在 `settings.json` 加入 `"agent_push_notify_enabled": true`。搭配 Claude Code 內建的 remote control 功能，在手機遠端操作時，當 Claude 需要權限確認或等待輸入，會自動推播通知到手機，讓你在離開螢幕時不錯過任何互動節點。

**關鍵概念：推播式權限確認（Push-based Permission Approval）**

***

### 3. 自動生成權限白名單 [02:35]

輸入 `/fewer-permission-prompt`，Claude Code 會掃描最近 50 個 transcript，提取常見的唯讀 bash 和 MCP tool call 頻率，自動生成優先排序的 allow list 寫入 `settings.json`。這不是無腦全自動批准，而是基於你過去的批准行為建立精準白名單，在不犧牲安全性的前提下大幅減少權限提示。

**關鍵概念：行為驅動權限白名單（Behavior-driven Allow List）**

***

### 4. 設定 Deny Rules 保護敏感操作 [03:47]

Deny rules 的檢查順序為：deny → ask → allow，deny 永遠優先生效，且任何層級的 allow 都無法覆蓋。建議至少設定兩條：
- 禁止讀取 `.env` 檔案（防止 API keys 進入 context）
- 禁止 `git push *`（保留發佈權力在人類手中）

**關鍵概念：權限優先級覆蓋（Permission Precedence Override）**

***

### 5. 模型成本優化：Plan-Execute 分離 [04:35]

輸入 `/model` 選擇預設方案「Opus Plan」或 Fable 5 Plan。運作邏輯：規劃階段使用 Opus/Fable 進行深度推理，執行階段自動切換至 Sonnet 處理。核心原則——**大模型用於錯誤成本高的場景（規劃、審查、難題），小模型用於高頻操作（檔案讀取、文件處理、實作執行）**。此設定可作為所有新 session 的預設值。

**關鍵概念：Plan-Execute 模型分層（Model Tier Separation）**

***

### 6. Effort Level 調校 [06:09]

`/effort` 指令提供 low → max ultra code 的選擇，預設為 automatic。獨立測試（20 輪/每個等級）顯示：max 以下品質幾乎無差異，正確率完全不變。多出的 token 購買的是「再驗證」和「但書」，而非更好的答案。建議：
- 例行工作：使用預設 effort
- 真正困難的問題：使用 high
- max：幾乎永不碰觸，尤其搭配 Fable 時成本極高

**關鍵概念：思考預算邊際遞減（Diminishing Thinking Budget Returns）**

***

### 7. 關閉遙測與非必要 LLM 呼叫 [07:40]

在 `settings.json` 的 ENV 區段加入四行設定：

| 設定 key | 效果 |
|---|---|
| `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY` | 停止「Claude 表現如何？」問卷打斷工作流 |
| `CLAUDE_CODE_DISABLE_TELEMETRY` | 退出分析與使用追蹤 |
| `CLAUDE_CODE_DISABLE_ERROR_REPORTING` | 阻止自動錯誤報告發送至 Sentry |
| `CLAUDE_CODE_DISABLE_NON_ESSENTIAL_MODEL_CALLS` | 減少閒聊、小知識等非必要 LLM 呼叫 |

額外步驟：至 Claude.ai → Settings → Privacy → 關閉「Help improve AI models」，防止對話與 coding session 被用於模型訓練。

**關鍵概念：資料隱私最小化（Data Privacy Minimization）**

***

### 8. 延長歷史記錄保留期 [08:42]

Claude Code 預設僅保留 30 天對話歷史，超過即刪除。在 `settings.json` 加入 `"cleanupPeriodDays": 365`（或更大數值）延長保留。切勿設為 0，會立即清除所有記錄。

**關鍵概念：歷史保留窗口（History Retention Window）**

***

### 9. 提前觸發 Auto-Compact [09:28]

預設在 context window 95% 滿時才壓縮，但品質在 70-80% 就開始衰退（context rot）。在 ENV 區段加入 `CLAUDE_AUTO_COMPACT_PERCENTAGE_OVERRIDE`，設為 `75`，讓 session 在 context rot 發生之前自動壓縮。

辨識技巧：ENV 區段的 key 為全大寫，頂層設定的 key 為小駝峰。

**關鍵概念：上下文衰退閾值（Context Rot Threshold）**

***

### 10. 設定 Status Line 即時監控 [10:25]

輸入 `/status line`，加上指令描述：`show model name and context percentage with a progress bar`。Claude Code 會自動設定底部狀態列，顯示模型名稱、context 百分比與進度條，讓你即時掌握 context 使用量，在 auto-compact 觸發前手動儲存摘要筆記。

**關鍵概念：上下文可視化監控（Context Visibility Monitoring）**

***

### 11. 快速暫存 Prompt [11:11]

輸入 prompt 到一半時按下 `Ctrl+S`，將當前 prompt 暫存剪下。在下個 prompt 視窗按 `Cmd+V` 即可貼回。等同於剪貼簿式的 prompt 暫存機制。

同場加印：在 `settings.json` 加入 `"spinnerTipsEnabled": false`，移除 spinner 下方的小提示文字，保持專注。

**關鍵概念：Prompt 暫存快取（Prompt Stash Cache）**

***

### 12. 移除 AI 共同作者標記 [12:20]

Claude Code 預設在每次 commit 加入 `co-authored-by: AI` 等標記。在 `settings.json` 的 attribution 區段，將 commit 和 PR 的值留空，即可停止自動歸因。Claude Code 據稱佔了近幾個月 GitHub 全部 commit 的 4%，但你可以選擇不公開標記。

**關鍵概念：提交歸因控制（Commit Attribution Control）**

***

### 13. （彩蛋）Loop Engineering：2026 新範式 [~13:30]

2026 年 prompt engineering 的方向已反轉。過去追求又長又詳細的 prompt，逐一指定每個步驟。Anthropic 最新模型指引建議相反：**當模型有足夠資訊時，讓它自行行動**。

Tarik（Claude Code 團隊）發布的 field guide 在 3 天內獲得 200 萬次觀看，核心論點：最佳結果來自縮短「你要求的事」與「實際需要發生的事」之間的差距。給予目標、上下文、完成定義（done criteria），但不給步驟。

真正與 Fable 5 搭配的高手在做的是：在實作前、中、後執行特定的 loops。

**關鍵概念：迴圈工程（Loop Engineering）**

***

# [技術/數據對比]

### Effort Level 測試結果（20 輪/等級，相同問題）

| Effort 等級 | 輸出品質 | 正確率 | Token 消耗 | 實際建議 |
|---|---|---|---|---|
| Low | 基線 | 基準 | 最低 | 快速草稿 |
| Default | 與 Max 幾乎相同 | 不變 | 中等 | ✅ 例行工作首選 |
| High | 略高 | 不變 | 高 | ✅ 困難問題使用 |
| Max/Ultra | 幾乎無提升 | 不變 | 極高 | ❅ 幾乎不需要 |

### Plan-Execute 模型分層策略

| 階段 | 推薦模型 | 原因 |
|---|---|---|
| Plan / Review | Opus 或 Fable 5 | 錯誤成本高，需要深度推理 |
| Build / Execute | Sonnet | 高頻操作，速度與成本兼顧 |

### Deny Rules 檢查優先級

| 優先級 | 規則類型 | 說明 |
|---|---|---|
| 1（最高） | Deny | 永遠阻擋，不可被任何 allow 覆蓋 |
| 2 | Ask | 需要人工確認 |
| 3（最低） | Allow | 自動批准 |

***

# [結論與行動建議]

> **「瓶頸不再是模型本身，而是你能否縮短『你要求的』與『真正需要發生的』之間的差距。」**

**具體行動法則 — S.P.E.E.D. 法則：**
- **S**ound — 啟用通知，不再浪費等待時間
- **P**ermission — 建立白名單 + Deny Rules，權限分層
- **E**conomy — 模型分層 + Effort 調校，成本減半零品損
- **E**nvironment — 隱私設定 + 歷史延長 + Auto-compact 提前
- **D**elegation — 給目標不給步驟，讓模型自行決策

**生活實踐建議：** 將 Plan-Execute 分層思維套用至日常工作——用「深度思考模式」處理策略規劃與架構決策，用「快速執行模式」處理重複性高的實作任務。如同 Claude Code 的模型分層，人的精力也應依任務複雜度進行分配，避免在例行工作上耗費過多決策能量 。 [youtube](https://www.youtube.com/watch?v=Gz7S1v1k664)

***

# [參考連結]

- 原始 YouTube 影片：https://youtu.be/M2p7OvKLAWw
