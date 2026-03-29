---
title: 'Claude Code打造AI行銷團隊教學'
date: 2026-03-29
image: /images/影片筆記/claude-code-ai-marketing-team.jpeg
category: 影片筆記
tags: [Claude Code, AI行銷團隊, Skills技能, MCP整合, Agent協作]
description: '透過Claude Code與VS Code環境，將Claude轉化為包含數據分析、內容創作、市場研究等多元角色的「AI行銷團隊」，實現全自動化工作流'
quote: '將任務轉化為技能，將技能整合為Agent。'
action: '整理出你最滿意的3份品牌範本作為AI的參考基準，先標準化再AI化'
source_has_timestamps: true
---

### 💡 核心摘要
本影片教學如何透過 **Claude Code** 與 **VS Code** 環境，將 Claude 轉化為包含數據分析、內容創作、市場研究等多元角色的「AI 行銷團隊」，實現從策略研究到素材產出的全自動化工作流。

---

### 📂 詳細重點整理

#### 1. 構建 AI 團隊的四個關鍵步驟 [[00:20](http://www.youtube.com/watch?v=yLXLHnD4fco&t=20)]
要打造高效的 AI 團隊，不能只是隨機下指令，需要結構化的設計：
* **定義功能：** 列出每週重複執行的行銷任務。
* **轉化技能 (Skills)：** 將每個任務轉化為一個專屬的「技能」工作流。
* **分配角色 (Agents)：** 將相似技能歸類到不同的 Agent 角色中（例如：寫手、設計師、分析師），避免單一 Agent 負擔過重導致品質下降。
* **整合協作：** 設定 `claude.md` 指令，讓 Claude 知道何時該調用哪個 Agent 或技能。

#### 2. 環境架設與基礎設定 [[01:10](http://www.youtube.com/watch?v=yLXLHnD4fco&t=70)]
* **工具準備：** 下載 **VS Code** 並安裝官方的 **Claude Code** 擴充功能，登入 Claude Pro 帳號。
* **目錄結構：** 建立「系統資料夾」（存放 SOP、品牌規範、模板）與「工作資料夾」（存放產出的廣告、頁面等）。
* **上下文注入：** 在 `context` 資料夾放入品牌音調、產品資訊，這會決定 AI 產出內容的準確度。
* **初始化：** 透過 `/init` 指令建立 `claude.md`，這是整個專案的靈魂，用於定義全域指令 [[02:54](http://www.youtube.com/watch?v=yLXLHnD4fco&t=174)]。

#### 3. 技能開發：參考基準法 (Reference-base Method) [[03:41](http://www.youtube.com/watch?v=yLXLHnD4fco&t=221)]
這是不寫程式也能提升品質的核心技巧：
* **範例引導：** 給予 Claude 既有的品牌簡報或文案範本，讓它分析風格模式。
* **技能擴展：** 基於分析結果，建立「品牌專屬簡報技能」，產出的投影片能達到 90% 的完成度 [[04:56](http://www.youtube.com/watch?v=yLXLHnD4fco&t=296)]。
* **外部工具整合 (MCP)：** 透過 MCP (Model Context Protocol) 連結外部工具（如圖像生成模型 Nano Banana），讓 AI 具備設計社群圖片的能力 [[06:25](http://www.youtube.com/watch?v=yLXLHnD4fco&t=385)]。

#### 4. 實戰 Agent 協作與遠端控制 [[08:23](http://www.youtube.com/watch?v=yLXLHnD4fco&t=503)]
* **建立專屬 Agent：** 透過 `/agents` 命令建立如 **Data Analyst** (分析數據、製作圖表 [[10:06](http://www.youtube.com/watch?v=yLXLHnD4fco&t=606)]) 或 **Content Creator** (撰寫部落格、設計贈品 [[10:55](http://www.youtube.com/watch?v=yLXLHnD4fco&t=655)])。
* **任務指派：** 只需輸入簡單需求，Claude 會根據路由規則自動分配工作。例如：10 分鐘內產出日本櫻花季的完整行銷方案（含研究、簡報、廣告圖、Landing Page）[[13:04](http://www.youtube.com/watch?v=yLXLHnD4fco&t=784)]。
* **遠端與協作：** * **Notion 整合：** 讓 AI 自動抓取 Notion 上的任務看板並執行 [[14:03](http://www.youtube.com/watch?v=yLXLHnD4fco&t=843)]。
    * **手機遠端控制：** 透過 `/remote-control` 生成連結，讓你在手機上也能指揮家中的電腦執行複雜任務 [[15:22](http://www.youtube.com/watch?v=yLXLHnD4fco&t=922)]。

---

### 🚀 結論與行動建議

* **核心金句：** 「將任務轉化為技能，將技能整合為 Agent。」
* **具體建議：**
    1.  **先標準化再 AI 化：** 整理出你最滿意的 3 份品牌範本作為 AI 的參考基準。
    2.  **善用 claude.md：** 持續更新這個文件，它是維持 AI 團隊一致性的關鍵。
    3.  **分工明確：** 寧可建立多個專注的小 Agent，也不要讓一個 Agent 做所有事。