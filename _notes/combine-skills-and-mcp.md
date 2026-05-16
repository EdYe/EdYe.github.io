---
title: '結合 Skills 與 MCP 填補 Agent 上下文缺口'
date: 2026-05-17
image: /images/AI筆記/combine-skills-and-mcp.jpeg
category: AI筆記
tags: [MCP, Skills系統, Context Gap, 安全防護, Eval驅動開發]
description: 'MCP 給了 Agent 操作能力，但不給它「如何正確使用」的知識。Supabase 用真實的 Postgres 安全漏洞案例驗證：純 MCP 的 Agent 會繞過 Row Level Security 暴露資料，而加上 Skill 的 Agent 則能正確處理。'
quote: 'The bottom line is not the context — it's the guidance.（瓶頸不是上下文的量，而是有沒有正確的指引。）'
action: '為核心產品撰寫一份 skill.md，將不可遺漏的安全規則直接內嵌，並指向最新設計文件連結，明確規範 Agent 操作順序。'
source_has_timestamps: true
---
# Combine Skills and MCP to Close the Context Gap

**核心痛點：** Agent 光有 MCP（工具整合）還不夠——沒有產品專屬的 Skill 指引，它會悄悄犯下你永遠不知道的安全漏洞。

***

## [核心摘要]

MCP 給了 Agent 操作能力，但不給它「如何正確使用」的知識。Supabase 的 Pedro Rodrigues 用一個真實的 Postgres 安全漏洞案例驗證：**純 MCP 的 Agent 會繞過 Row Level Security（RLS）暴露資料**，而加上 Skill 的 Agent 則能正確處理。 核心結論是：現在 Agent 的瓶頸不是「上下文量」，而是「有沒有正確的任務指引（Guidance）」。

***

## [詳細重點整理]

### 1. 為什麼 MCP 單獨不夠用 [00:14]

Agent 在訓練資料中可能完全不知道某個產品的特定安全規則，例如 Postgres 中建立 View 時若未加 `security_invoker = true`，會自動繞過底層資料表的 RLS，讓不該看到的資料外洩。 實驗結果顯示，**只用 MCP 的 Agent 成功繞過 RLS、送出不安全查詢**，而加上 Skill 的 Agent 正確設置了 flag。

> **關鍵概念：** **Context Gap（上下文缺口）**——Agent 掌握工具，卻缺乏產品環境的正確知識，導致靜默式失敗。

***

### 2. 什麼是 Skill？ [02:55]

**Skill** 是包含指令、腳本與資源的資料夾，Agent 可動態發現並載入。 結構包含：

- **Front Matter**：name + description，Agent 據此判斷何時載入該 Skill
- **skill.md**：主指令檔，Agent 執行任務時的核心參考
- **Reference Files**（可選）：輔助文件，但 Agent 非常懶得主動讀取

> **關鍵概念：** **Progressive Discovery（漸進式發現）**——Agent 依需求動態載入 Skill，而非一次全部載入。

***

### 3. 撰寫 Skill 的三大原則 [05:54]

**原則一：不重複資訊（Don't Duplicate）** 
Skill 不應複製文件內容，而是要**指向**最新文件的所在位置。強迫 Agent 去讀官方文件，而非依賴可能過時的訓練資料。Supabase 甚至實驗透過 SSH 暴露文件，讓 Agent 像操作檔案系統一樣查詢文件。

**原則二：能被跳過的必然被跳過（If Skippable, Will Be Skipped）** 
實驗發現，Agent 載入一個 Reference File 後，幾乎不可能再主動載入第二個。因此，**絕對不能遺漏的安全規則、核心知識，必須直接放進 skill.md 本體**，而非放在 Reference File 裡。Supabase 最初把安全 Checklist 放在 Reference File，結果 Agent 常常漏掉。

> **關鍵概念：** **Mandatory Context（強制上下文）**——關鍵資訊必須內嵌於主檔，避免被 Agent 的懶惰行為略過。

**原則三：有主見（Be Opinionated）** 
你最了解自己的產品，不要怕告訴 Agent「最佳工作流程」。以 Supabase 為例，推薦的 Schema 管理流程為：
1. 先在開發/暫存環境自由執行 DDL 操作
2. 執行 Supabase Advisor 檢查安全與效能問題
3. **最後才**建立 Migration File（而非每改一次 Schema 就建一個）

***

### 4. Eval 驗證結果 [10:55]

Supabase 設計了 6 種情境，針對三種測試條件（無 MCP / 只有 MCP / MCP + Skill），跨 4 個模型（Claude Opus 4.6、Sonnet 4.6、GPT-5.4、GPT-5.4 mini）進行評測。

| 測試條件 | 表現 |
|---|---|
| 無 MCP、無 Skill（基準線） | 最差 |
| 只有 MCP | 中等，有安全盲點 |
| **MCP + Skill** | **所有模型均最高分** |

結果一致：**Skill + MCP 在所有模型上全面勝出**，且此方法與 Agent 無關（agnostic），Claude、GPT 皆適用。

> **關鍵概念：** **Eval-Driven Skill Development（評測驅動的 Skill 開發）**——把 Markdown 文件當成程式碼一樣跑 CI 測試，用 Braintrust 評分 Agent 行為。

***

## [結論與行動建議]

**啟發金句：**
> **"The bottom line is not the context — it's the guidance."**（瓶頸不是上下文的量，而是有沒有正確的指引。）

**具體行動建議：S-O-S 法則**
- **S**ingle Source of Truth：指向文件，不複製文件
- **O**pinionated：提供有主見的最佳工作流程
- **S**tart Minimal：從最小可行 Skill 開始，持續迭代版本

**生活實踐建議：**
身為 AI 應用架構師，可立即為你的核心產品或平台（如內部資料庫、API 設計規範）撰寫一份 `skill.md`，重點放在：① 不可遺漏的安全規則直接內嵌、② 指向最新設計文件的連結、③ 明確規範 Agent 的操作順序工作流。這樣每次讓 Agent 介入你的系統時，都能大幅降低靜默錯誤的風險。

***

## [參考連結]

- 原始影片：https://youtu.be/JT3OzDKrucU?si=gOc5JyP0AoAs0CHJ
- 講者 Pedro Rodrigues（Supabase AI Tooling Engineer）：https://x.com/rodriguespn23
