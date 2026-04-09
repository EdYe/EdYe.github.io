---
title: 'Claude Code 連鎖技能：context fork 打造全自動化工作流'
date: 2026-04-10
image: /images/影片筆記/claude-code-chaining-skills-explained.jpeg
category: 影片筆記
tags: [連鎖技能, Context Fork, 自動化工作流, 第二大腦, 上下文管理]
description: '本影片揭示了 Claude Code 一項顛覆性的功能：連鎖技能（Chaining Skills）。透過一行關鍵代碼 context fork，使用者可以將多個獨立的 AI 技能串聯成一個自動化的工作流。'
quote: '在一個你可以構建任何事物的世界裡，最重要的不再是「如何做」，而是「什麼值得做」以及如何構建系統去實現它。'
action: '觀察每週最重複的資訊處理流程，將其模組化為連鎖技能，用 context fork 銜接各步驟。'
source_has_timestamps: true
---

## 核心摘要
本影片揭示了 Claude Code 一項顛覆性的功能：**連鎖技能（Chaining Skills）**。透過一行關鍵代碼 `context fork`，使用者可以將多個獨立的 AI 技能串聯成一個自動化的工作流。這不僅提升了工作效率，更讓 AI 能在複雜任務中保持深度的上下文理解，實現從市場調查到內容生成的全自動化產出。

---

## 詳細重點整理

### 1. 連鎖技能的核心價值 [[00:36](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=36)]
* **定義**：將多個獨立的技能（Skill）串聯，只需輸入一個指令，即可按順序執行一系列任務並獲得最終整合輸出。
* **優勢**：相比單一大型指令，連鎖技能在每個步驟中擁有更集中的上下文（Context），能產生更高質量的結果。
* **關鍵概念**：**偽 Agent 軍團**——利用多個專業技能協作，模擬複雜的 AI 代理工作流，但保留人的介入彈性。

### 2. 關鍵語法：Context Fork [[05:12](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=312)]
* **代碼功能**：在技能文件中加入 `context fork`，會為該技能開啟獨立的上下文視窗。
* **運行邏輯**：它讓每個步驟在專屬環境中運行，處理完畢後將精華結果回傳至主視窗，避免長對話導致的資訊混亂。
* **工具權限**：可精確指定每個技能允許使用的工具（如 Web Search、File Read），確保執行效率。

### 3. 實戰案例一：行銷發布漏斗 [[00:46](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=46)]
* **流程拆解**：
    1. **市場掃描 [[01:25](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=85)]**：自動搜尋當前市場定價與競爭對手。
    2. **銷售頁面生成 [[02:13](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=133)]**：根據調研結果撰寫登陸頁文案。
    3. **郵件序列與社群公告 [[02:24](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=144)]**：生成推廣信件與 LinkedIn/X 貼文。
    4. **PDF 整合報告 [[02:41](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=161)]**：將所有資訊彙整成一份結構化的執行簡報。

### 4. 實戰案例二：第二大腦（Obsidian）檢索 [[07:21](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=441)]
* **應用場景**：連結個人的知識庫，進行深度專題研究。
* **執行步驟**：
    1. **Brain Search [[08:11](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=491)]**：在龐大的筆記庫中搜尋相關主題。
    2. **Insight Extraction [[08:23](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=503)]**：提取關鍵洞察與任務。
    3. **Synthesis [[08:35](http://www.youtube.com/watch?v=KsYCtXeAGBg&t=515)]**：將碎片化資訊轉化為結構化的研究綜述。

---

## 結論與行動建議

* **啟發金句**：**「在一個你可以構建任何事物的世界裡，最重要的不再是『如何做』，而是『什麼值得做』以及如何構建系統去實現它。」**
* **具體行動建議：3-S 技能構建法則**
    1. **Single (單一化)**：先寫出能完美執行單一任務（如搜尋、撰寫、排版）的獨立技能檔案（Markdown）。
    2. **Sequence (序列化)**：建立一個「策劃者技能」（Orchestrator），使用單引號 `'/command'` 列出執行順序。
    3. **Splice (銜接)**：加入 `context fork` 語句，並在結尾指定最終需要回傳的檔案格式（如 `.md` 或 `.pdf`）。

* **生活實踐建議**：
    * **建立自動化清單**：觀察自己每週重複性最高的「資訊處理流程」（例如：讀新聞 -> 寫摘要 -> 發推特），將其模組化為連鎖技能。
    * **工具整合**：嘗試將 Claude Code 連結至本地 Markdown 知識庫（如 Obsidian），讓 AI 成為能隨時調用你過去思考的「第二大腦」。

影片連結：[https://www.youtube.com/watch?v=KsYCtXeAGBg](https://www.youtube.com/watch?v=KsYCtXeAGBg)
