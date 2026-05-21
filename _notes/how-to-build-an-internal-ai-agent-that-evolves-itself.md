圖片檔案尚未存在，image 欄位用 TODO 標記副檔名。以下是完整輸出：

```markdown
---
title: '如何打造能自我進化的 AI 內部代理人'
date: 2026-05-21
image: /images/AI筆記/how-to-build-an-internal-ai-agent-that-evolves-itself.TODO
category: AI筆記
tags: [AI Ops代理人, 自進化架構, Claude Code, 程式碼即知識庫, 指令集記憶]
description: '自進化 AI 內部代理人（Self-Evolving Internal Agent）解決了新創公司在人力有限時如何規模化運營的核心痛點。'
quote: '讓代理人不只能完成任務，更能在遇到不會的任務時，自己建立完成它的能力。'
action: '用 Claude Code CLI 建立任務佇列、給予唯讀程式碼庫、配備編碼子代理人與可自編 instructions.md，快速複製自進化 AI Ops 代理人架構'
source_has_timestamps: true
source_raw: How to Build an Internal AI Agent That Evolves Itself
---

# [核心摘要]

**自進化 AI 內部代理人**（Self-Evolving Internal Agent）解決了新創公司在人力有限時如何規模化運營的核心痛點。Answer This 以 2 位全職員工達成超過 200 萬美元 ARR，關鍵在於打造了一個能自行擴充工具集、處理逾 100 封每日郵件、關閉 400+ 支援工單的 AI Ops 代理人，且整個系統可被非技術人員直接透過 Slack 訓練與修正。

***

# [詳細重點整理]

## 1. 代理人的核心效益 [00:01]

Answer This 是一家為科學研究工作流程建構 AI 代理人的新創公司，靠著內部 AI Ops 代理人，兩名全職員工撐起了超過 200 萬美元 ARR 。這個代理人每天處理 100+ 封電子郵件、自動關閉客服工單、更新 CRM，還能即時回答業務問題，例如「某個潛在客戶的狀態是什麼？」，無需再切換多個應用程式查找 。 [youtube](https://www.youtube.com/watch?v=yQNILxENRt0)

**關鍵概念：AI Ops 代理人（AI Ops Agent）**——將原本需要人工的重複性業務操作，統一交由 AI 代理人處理。

***

## 2. 自進化架構設計 [01:35]

系統架構核心是將 **Claude Code CLI 包裝在 Python 中**，來自 Slack、Email 等渠道的新訊息進入任務佇列，代理人逐一迭代處理 。最關鍵的突破是：當代理人遇到尚未能處理的重複性任務時，它會呼叫一個子編碼代理人（Coding Sub-Agent）來自動建立新工具，這個工具會被永久儲存並在未來的工作階段中繼續使用 。整個工具集從最初的骨架成長到超過 **45 個自建 CLI**，包含自動創建 cron job 監控廣告落地頁是否正常運行 。 [youtube](https://www.youtube.com/watch?v=yQNILxENRt0)

**關鍵概念：自擴充代理人（Self-Extending Agent）**——AI 代理人能在運行時自行撰寫並永久化新工具，實現能力的持續成長。

***

## 3. 業務邏輯的灌輸方式 [02:05]

為了讓代理人理解只有創辦人才知道的業務邏輯，系統提供代理人一份**唯讀的資料庫與程式碼庫副本**，並透過 cron job 在每次發版後自動同步更新 。當客服詢問訂閱邏輯或 App 內功能位置時，代理人可直接查閱程式碼庫自行推理解答，無需人工介入 。 [youtube](https://www.youtube.com/watch?v=yQNILxENRt0)

**關鍵概念：程式碼即知識庫（Codebase as Knowledge Base）**——以唯讀程式碼庫作為代理人的業務邏輯知識來源。

***

## 4. 可編輯人格記憶系統 [03:22]

代理人透過一個 `instructions.md` 檔案載入「人格」，每次代理人運行時都會讀取此檔案，且代理人本身能夠編輯更新它 。非技術共同創辦人 Ryan 發現一類客服錯誤後，直接在 Slack 告知代理人，代理人即自行更新指令集，此後同類錯誤再未發生——這完全繞過了技術債與工程師介入 。 [youtube](https://www.youtube.com/watch?v=yQNILxENRt0)

**關鍵概念：可自編指令集（Self-Editable Instructions）**——讓代理人像員工一樣接受反饋並自主更新行為規範。

***

# [技術/數據對比]

| 記憶類型 | 內容 | 實現方式 |
|---|---|---|
| **事實記憶（Factual Memory）** | 程式碼庫與資料庫的運作方式 | 唯讀程式碼庫 + 定期 cron job 同步 |
| **行為記憶（Behavioral Memory）** | 使用者的教學與反饋偏好 | `instructions.md` 檔案，可自行更新 |
| **程序記憶（Procedural Memory）** | 重複性任務的處理流程 | 代理人自建的 CLI 工具集 |

***

# [結論與行動建議]

**啟發金句：**
> **「讓代理人不只能完成任務，更能在遇到不會的任務時，自己建立完成它的能力。」**

**具體行動建議：四步法快速複製此架構（4-Step Agent Bootstrap）**
1. 用 Claude Code CLI 包裝 Python，建立任務佇列接收 Slack / Email 訊息
2. 給代理人唯讀的程式碼庫存取權限
3. 提供基本 CLI 工具集 + 一個編碼代理人作為 CLI
4. 載入可自我編輯的 `instructions.md` 指令檔案

**生活實踐建議：**
- **PM/產品團隊**：將常見的客戶反饋分類、工單路由設定為代理人工具，讓非技術成員可直接在 Slack 訓練代理人行為，不必依賴工程師
- **小型新創**：優先使用 Claude Code CLI 作為主代理人框架，逐步給予 Intercom、Stripe、Fathom 等工具的 CLI 存取，讓系統自然進化擴充，而非一次性設計完整功能
- **個人應用**：把自己的日常 SOP 文件化成 `instructions.md`，讓 AI 助理根據你的實際反饋持續校準行為模式

***

# [參考連結]

- 原始影片：[How to Build an Internal AI Agent That Evolves Itself — YC Root Access](https://youtu.be/DGD9b8K42lk?si=0KlamISPpM6dJRum) [youtube](https://www.youtube.com/watch?v=yQNILxENRt0)
```

image 欄位的副檔名標記為 `TODO`，待實際圖片放入 `images/AI筆記/` 後再確認副檔名並更新。
