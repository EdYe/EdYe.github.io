---
title: '建立 Agentic OS 讓 AI 穩定產出的底層架構'
date: 2026-05-03
image: /images/影片筆記/creating-your-own-agentic-os.jpeg
category: 影片筆記
tags: [Agentic OS, 情境管理, 記憶系統, 技能系統, Claude Code]
description: 'AI 工具輸出品質差的根本原因不是提示詞寫得不好，而是缺乏一套 Agentic OS。透過靜態身份情境、記憶層、可重複技能'
quote: 'AI 輸出品質的差距，不在於誰的提示詞寫得更好，而在於誰在工具底層建了更聰明的結構。'
action: '先用 AI 訪問自己生成 user.md，加入 Session Hook 與語義記憶，封裝第一個重複流程為技能，串成排程工作流。'
source_has_timestamps: true
---
## [核心摘要]

AI 工具（如 Claude Code）輸出品質差的根本原因不是提示詞寫得不好，而是缺乏一套**Agentic OS（智能代理作業系統）**。這套系統透過「靜態身份情境 + 記憶層 + 可重複技能 + 自動化排程工作流 + 多客戶架構」，解決了 LLM 開箱即用時的情境失憶與通才缺陷，讓 AI 能 90% 時間穩定產出高品質結果。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

***

## [詳細重點整理]

### 1. 問題定義：為何輸出品質差 [00:00]
同樣的工具、同樣的模型，不同人卻有截然不同的成果。核心差距在於是否在工具「底層」建立了結構。**Agentic OS** 的本質，就是一套「聰明的情境管理系統」——透過資料夾、檔案與結構，在對的時間把對的資訊注入 AI。

> **關鍵概念：情境管理（Context Management）**

***

### 2. 靜態情境：告訴 AI 你是誰 [03:10]
每個 AI 工具都會先讀取一個身份檔案（Claude Code 是 `claude.md`、OpenClaude 是 `soul.md`），作為 system prompt 的基底。建議方式是讓 AI 訪問你 15 個問題，再生成 `user.md`（關於你）與 `personality.md`（關於代理人），而非從頭手寫。此外，「**共用品牌情境資料夾**」存放品牌聲音、ICP、定位等，所有技能都從同一資料夾取用，更新一次即全部同步，可提升輸出品質 3x–10x。

> **關鍵概念：靜態情境（Static Context）**

***

### 3. 記憶系統：六層框架 [06:56]
LLM 原生記憶的缺陷稱為**「情境腐化（Context Rot）」**——對話越長，前期資訊越容易被遺忘。六層記憶架構從低到高分別為：

| 層級 | 機制 | 適用場景 |
|------|------|----------|
| Level 1 | `claude.md` 靜態規則 | 基本設定 |
| Level 2 | **Session Start Hook**（強制注入） | 確保情境每次都被載入 |
| Level 3 | **語義搜尋**（mem search / claude mem） | 80/20 核心，大多數人的最佳選擇 |
| Level 4 | 逐字精確回溯（Me Palace） | 客戶工作、用詞精準要求 |
| Level 5 | 知識庫 | 特定需求 |
| Level 6 | 跨工具共用記憶 | 多裝置、多 LLM 環境 |

> **關鍵概念：情境腐化（Context Rot）**

***

### 4. 可重複技能（Skills）[11:10]
要讓 AI 從通才變成專才，必須將流程封裝成「技能（Skill）」。核心原則：
- 單一技能保持在 **200 行以內**，確保 Claude 穩定理解
- 採用「**漸進式揭露（Progressive Disclosure）**」——先載入名稱和描述，需要時再載入完整技能檔
- 技能永遠引用共用品牌情境資料夾，而非硬編碼
- 每次執行後收集反饋，寫入 `learnings.md`，下次運行時先讀取 → **自學迴圈**

> **關鍵概念：漸進式揭露（Progressive Disclosure）**

***

### 5. 技能系統與排程工作流 [14:06]
單一技能節省時間有限，真正的威力在於「**技能系統（Skill System）**」——將多個技能串成完整流水線，並設定排程自動執行。範例流程：

`主題研究技能 → 腳本撰寫技能 → 內容重新包裝技能 → 人工審核節點 → 自動發佈`

一個「技能協調器（Skill Orchestrator）」作為 meta-skill，負責串接整個鏈條，讓你離開電腦後系統仍可自主運作。

> **關鍵概念：技能系統（Skill System）**

***

### 6. 分層規劃框架 [16:14]
依複雜度選擇對應的規劃框架，建議建立 3–4 個層級：
- **Level 1**：Claude 內建 `Shift+Tab` 規劃模式（簡單任務）
- **Level 2**：PRD 框架（半天至多天的專案）
- **Level 3**：**GSD（Get Stuff Done）框架**——輕量 meta-prompting，將複雜任務拆解為「計劃 → 執行 → 驗證」三階段，專門對抗情境腐化

> **關鍵概念：GSD 框架（Get Stuff Done Framework）**

***

### 7. 多客戶架構 [18:43]
透過 Claude Code 的「父資料夾情境繼承」機制：
- **根目錄** `claude.md`：共用方法論、技能、腳本
- **各客戶資料夾**：獨立品牌情境、獨立記憶/學習檔案、可覆寫父層設定
- 多客戶之間互不污染，卻共享核心技能資源庫

> **關鍵概念：情境繼承（Context Inheritance）**

***

### 8. 輸出整合：統一落點 [20:44]
AI 預設會把輸出散落在各處。解法是建立固定的 `projects/` 資料夾結構，依「技能類型」或「簡報（Brief）」分類，每個客戶有獨立的 `projects` 子資料夾，確保輸出永遠在可預測的位置。

> **關鍵概念：輸出可預測性（Output Predictability）**

***

### 9. 隨時隨地存取 [22:19]
兩步驟讓系統「跟著你走」：
1. 將系統部署到 **VPS 或 Claude Cloud**，不綁定本機運行
2. 透過 **Anthropic Channels 功能**，用 Telegram 或 Discord 從手機直接下指令，系統仍可存取所有背景檔案

> **關鍵概念：遠端存取層（Access Layer）**

***

## [結論與行動建議]

**啟發金句：**
> **「AI 輸出品質的差距，不在於誰的提示詞寫得更好，而在於誰在工具底層建了更聰明的結構。」**

**具體行動建議（S-M-S-S 法則）：**
- **S**tatic Context — 先用 AI 訪問自己，生成 `user.md` 與品牌情境資料夾
- **M**emory — 加入 Session Start Hook + 語義搜尋（Level 2+3）
- **S**kills — 把你最常重複的一個流程封裝成第一個技能，保持 200 行以內
- **S**chedule — 把 2–3 個技能串成一條排程工作流，讓系統 24/7 自動運作

**生活實踐建議：**
作為 AI 應用架構師，可立即將此架構應用於客戶交付流程——用多客戶資料夾架構隔離每個專案的情境，搭配品牌聲音 `voice_profile.md`，讓 AI 在撰寫提案、技術文件或行銷內容時，自動套用正確的語調與專業詞彙，無需每次重新說明背景。 [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)

## [參考連結]

- 原始影片：https://youtu.be/w0S-khYCaB4?si=zo2CvAFPcvPOWNAw [youtube](https://www.youtube.com/?hl=zh-tw&app=desktop)
