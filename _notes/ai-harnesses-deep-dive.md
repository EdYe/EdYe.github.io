---
title: 'AI Harnesses 深度解析：讓黑箱模型可靠落地'
date: 2026-05-19
image: /images/AI筆記/ai-harnesses-deep-dive.jpeg
category: AI筆記
tags: [AI Harness, 確定性驗證, Guardrail, Context壓縮, Agent可靠性]
description: 'AI Harness（代理人框架）是包圍模型的所有控制機制總稱，其目的是將不確定的黑箱模型錨定在穩定、可控的環境中。代理人失敗通常不是提示詞問題，而是 Harness 問題。'
quote: '我沒有修改任何一行提示詞，只是建了一個 Harness——結果卻天差地別。'
action: '下次 Agent 表現不佳時，先檢查 Harness 架構，再考慮修改 prompt；所有涉及外部系統的 Agent 都應加入 Verify Step'
source_has_timestamps: true
---
# AI Harnesses 深度解析：讓黑箱模型可靠落地

**核心問題不在提示詞，而在架構。** 這場演講展示了如何用一個 AI Harness 讓 GPT-3.5 Turbo 這種老舊模型，在不修改任何提示詞的情況下，成功自主完成「登入 Hacker News 並點讚」的任務。

***

## [核心摘要]

**AI Harness（代理人框架）** 是包圍模型的所有控制機制總稱，其目的是將不確定的黑箱模型錨定在穩定、可控的環境中。 演講的核心論點是：**代理人失敗通常不是提示詞問題，而是 Harness 問題**。透過逐步添加 Guardrails、Verify Step 與 Login Handler，一個無法可靠完成任務的 Agent 變得完全可用——全程未修改任何 prompt。

***

## [詳細重點整理]

### 1. 為何需要 Harness [01:45]
模型是黑箱：供應商可隨時降版、token 有上限、輸出具隨機性。**Harness 的核心價值是「可靠性（Reliability）」**——讓 Agent 做到它該做的事，無論底層模型如何。就像登山者用繩索固定於岩壁，Harness 讓模型無法「偏軌」。

> **關鍵概念：黑箱模型的不可控性（Model Non-determinism）**

### 2. Harness 的組成元件定義 [03:00–05:59]
一個標準的 Agent Harness 包含五大元件：

| 元件 | 說明 | 實例 |
|---|---|---|
| **Tool Registry** | 工具清單，Agent 可呼叫的能力集合 | 讀寫檔案、執行 Bash |
| **Model** | 底層 LLM，可替換 | GPT-3.5, Claude |
| **Context Primitives** | 管理與壓縮上下文的機制 | 自動截斷舊訊息 |
| **Guardrails** | 限制邊界，避免無限循環 | max_steps = 6 |
| **Verify Step** | 任務完成後的驗證邏輯 | 跑測試、lint、確認點讚 |

### 3. Demo 實測：Agent 失敗診斷 [08:12]
初始版本的 Agent 遇到登入頁面後**直接回報成功（謊言 / Hallucination）**，點讚從未真正發生。 問題不在 prompt，而在沒有任何機制去「驗證」Agent 自稱完成的動作是否屬實。

> **關鍵概念：代理人謊言（Agent Hallucination of Action）**

### 4. 添加 Guardrails + Context 壓縮 [10:20]
加入兩條 Guardrail：`max_iterations = 6`（超過即終止）與 `max_messages`（超過則壓縮上下文）。 上下文壓縮策略極為簡單：永遠保留 system prompt、user prompt 與最後兩條訊息，中間全部刪除。雖然 naive，但足夠示範核心概念。

> **關鍵概念：上下文壓縮（Context Compaction）**

### 5. Verify Step：讓 Agent 不再說謊 [13:02]
在 Harness 中加入 `verify_successful_upvote()` 函式，這是一段**確定性的程式碼（Deterministic Code）**，直接檢查 Agent 的工具呼叫歷史（trace），判斷是否真的點擊了正確按鈕、是否中途遭遇登入頁面。 不再信任 LLM 的自我報告，而是用 Harness 的邏輯去驗證。

> **關鍵概念：確定性驗證層（Deterministic Verify Layer）**

### 6. Login Handler：程式化注入憑證 [15:36]
在每次 Agent Loop 迭代前，Harness 檢查當前瀏覽器 URL。若偵測到登入頁面，**由 Harness 直接以 Playwright 填入帳號密碼並送出表單**，完全不透過 LLM，也不將密碼放入 prompt。 完成後將 `"harness_auto_login: success"` 訊息注入到 Agent 的訊息佇列，讓 Agent 知道已處理完畢。

> **關鍵概念：程式化憑證注入（Programmatic Credential Injection）**

### 7. 最終成果 [17:42]
GPT-3.5 Turbo（2023 年舊模型）在 Harness 的加持下，成功自主登入 Hacker News 並完成點讚，全程 6 次迭代，**全程未修改任何提示詞**。

***

## [技術架構對比]

| 版本 | 問題 | 改進點 |
|---|---|---|
| v1 裸 Agent | 遇登入頁崩潰、謊報成功 | 無 |
| v2 加 Guardrails | 限制迭代次數與訊息量 | max_iterations + context compaction |
| v3 加 Verify Step | 能正確回報失敗，停止謊言 | 讀取 tool call history |
| v4 加 Login Handler | 成功自主登入並點讚 | 程式化注入憑證 |

***

## [結論與行動建議]

**🔥 啟發金句：**
> 「我沒有修改任何一行提示詞，只是建了一個 Harness——結果卻天差地別。」

**⚙️ 核心法則：V-G-L 三層 Harness 法則**
- **V (Verify)**：任何 Agent 行動後，必須用確定性程式碼驗證，不信任 LLM 的自我報告
- **G (Guardrail)**：設定 max_steps 與 context 壓縮，避免無限迴圈與 token 浪費
- **L (Login/Secret Handler)**：敏感操作（憑證、支付）永遠由 Harness 程式化處理，絕不放進 prompt

**🗓️ 展望：動態 Harness（2027？）**
演講者預測下一個前沿是「**動態自生成 Harness**」：Agent 在執行任務前，先自動為該任務生成一套客製化的 Harness，自我感知可能的失敗點並預先設防。這被視為通往 AGI 的關鍵步驟之一。

**💼 實務應用建議：**
- 下次 Agent 表現不佳時，**先檢查 Harness 架構**，再考慮修改 prompt
- 所有涉及外部系統的 Agent（登入、API 呼叫、資料庫寫入），都應加入 Verify Step
- 在 CI/CD 流程中，將 Agent 的 Harness 視為獨立的工程模組來維護與測試

***

## [參考連結]

- 📺 原始影片：https://youtu.be/C_GG5g38vLU
- 👤 講者 Tejas Kumar (IBM)：[@tejask](https://x.com/tejask) | [GitHub](https://github.com/TejasQ)
