---
title: 'Skill Issue：用 AI 讓 Agent 真正善用 Supabase 的閉環框架'
date: 2026-05-06
image: /images/AI筆記/skill-issue-ai-agents-supabase.jpeg
category: AI筆記
tags: [Agent Skills, Eval驅動開發, RLS安全漏洞, Supabase, Braintrust]
description: 'AI Engineer 大會工作坊揭示撰寫 Agent Skills 的核心挑戰——不是「會寫」，而是「寫得有效」。展示 Agent 在無 Skills 引導時如何產生 RLS 繞過漏洞，並提出閉環開發框架。'
quote: 'Write a Skill, run Evals, inspect results, iterate — stop guessing, start measuring.'
action: 'S-E-I 法則：Security First（建立 View 一律加 SECURITY INVOKER）→ Eval-Driven（用 Braintrust 跑評估）→ Iterate（description 以 use 開頭反覆測試）。'
source_has_timestamps: true
---
# Skill Issue: 如何用 AI 讓 Agent 真正善用 Supabase

**[核心摘要]**

本場 AI Engineer 大會工作坊（2026/05/04）由 Supabase AI 工具工程師 Pedro Rodrigues 主講，揭示撰寫 **Agent Skills** 的核心挑戰——不是「會寫」，而是「寫得有效」。透過實際 Supabase 工作流示範，以「Performance Review App」為例，展示 Agent 在沒有 Skills 引導時如何產生 **RLS（Row Level Security）繞過漏洞**，並提出「撰寫 Skill → 執行 Eval → 分析結果 → 迭代」的閉環開發框架。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

**[詳細重點整理]**

**1. 什麼是 Agent Skills [00:03:09]**

Skills 是包含 `skill.md` 主檔案、reference 文件與腳本的資料夾結構，用於給 Agent 提供自定義工作流、說明文件與可執行腳本。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：漸進式揭露（Progressive Disclosure）**

- `skill.md` 的 front matter（`name` + `description`）優先載入 Context，Agent 按需再讀取完整內容
- 可類比為「一本書的目錄」——主檔是索引，reference 文件是各章節
- Skills 與 MCP 的差異：MCP 適合做「整合工具」（無需本地環境），Skills 則提供「上下文與工作流定義」，兩者應並用而非二擇其一 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

**2. 沒有 Skill 時的 Agent 失誤示範 [00:30:42]**

直接要求 Claude Code 建立 Supabase `department_stats` SQL View，Agent 成功建立並回報「一切正常」，但實際上：

- 所有使用者（包含基層員工）都能看到全公司薪資與績效資料
- 原因：**PostgreSQL 在建立 View 時預設使用建立者的權限（Security Definer），繞過 RLS 政策**
- Postgres 15+ 起需明確加上 `SECURITY INVOKER` flag，才能讓 View 繼承資料表的 RLS 政策 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：SECURITY INVOKER vs SECURITY DEFINER（RLS 繞過漏洞）**

***

**3. 撰寫有效 Skill 的實戰技巧 [01:10:00]**

Pedro 展示為 Supabase 安全性撰寫的 Skill，包含三個 PostgreSQL 安全核心要點：
- 公開 Schema 必須預設啟用 RLS
- 建立 View 時必須加上 `SECURITY INVOKER`
- 其他 RLS 稽核要點

**Description 撰寫技巧：以動詞 `use` 開頭**（如 `"Use this skill when working with Supabase security"`），實驗顯示能顯著提升 Claude 自動載入 Skill 的機率。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**三種觸發 Skill 的方式（可靠性由低到高）：**
- 依賴 Agent 自動判斷載入（需優化 description）
- Prompt 中加入 `use [skill名稱]` 關鍵字（≈100%）
- Claude Code 中使用 `/[skill名稱]` slash command（100%） [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

**4. 安裝 Skill 的工具鏈 [01:12:04]**

使用 Vercel 的 `npx skills` npm 套件進行安裝，支援：
- 從 GitHub repo 或本地路徑安裝
- 跨 Agent（Claude Code、Cursor 等）安裝
- 自動在 `.claude/skills/` 建立 symlink [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：Skill 分發標準化（Skills vs Plugins）**

***

**5. 以 Evals 自動化測試 Skill 效能 [01:23:45]**

採用 OpenAI 提出的 **Eval-Driven Development** 循環框架（源自其 blog post "Systematically Evaluate Agent Skills"）：

| 步驟 | 說明 |
|------|------|
| **定義 Metrics** | 明確「好」的行為是什麼（工具呼叫順序、推理路徑） |
| **撰寫 Skill** | 撰寫 `skill.md`、reference 文件、腳本 |
| **執行 Evals** | 使用 **Braintrust** 平台自動化運行評估場景 |
| **評分 & 迭代** | 分析 Agent 行為，調整 Skill 後重複循環 |

Braintrust 可視為 Agent 行為的「可觀測性工具」，提供完整的 Agent 行為追蹤紀錄。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

**關鍵概念：Eval-Driven Development（評估驅動開發）**

***

**[技術/數據對比]**

| | MCP Tools | Skills Scripts |
|---|---|---|
| **執行環境** | Server-side（不需本地環境）| 本地機器（需匹配 OS）|
| **適用場景** | 服務整合、API 呼叫 | 工作流定義、上下文注入 |
| **Context 佔用** | 全部工具說明預載 | 漸進式揭露，按需載入 |
| **推薦策略** | 整合外部服務時使用 | 補充說明與自定義工作流時使用 |

 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

**[結論與行動建議]**

**啟發金句：**
> **「Write a Skill, run Evals, inspect results, iterate — stop guessing, start measuring.」**

**具體行動建議：S-E-I 法則**
- **S（Security First）**：建立 Supabase View 一律加 `SECURITY INVOKER`，並預設啟用 RLS
- **E（Eval-Driven）**：每次修改 Skill 後，用 Braintrust 跑 Eval，用數據而非直覺決定優劣
- **I（Iterate on Description）**：Skill 的 description 以動詞 `use` 開頭，並針對「應載入/不應載入」場景反覆測試

**生活實踐建議：**
作為 AI 應用架構師，可立即將此框架應用於團隊內部工具：為公司既有的資料庫操作規範（如命名慣例、安全規則）撰寫 Skill，讓所有開發者的 Agent 共享相同的知識基準，等同於將「資深工程師的隱性知識」編碼化。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

**[參考連結]**

- 📺 原始影片：https://youtu.be/GmAQKINjv1E?si=YBBvNYoG1WLUnxoH [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
- 🛠️ Workshop GitHub Repo：`github.com/hudrippn/improve-skills-workshop-aie-europe`
- 👤 講者 Pedro Rodrigues：https://www.linkedin.com/in/pedro-neves-rodrigues/
