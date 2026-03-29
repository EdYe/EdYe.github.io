---
title: 'Stitch 2.0結合AI的網站設計自動化'
date: 2026-03-29
image: /images/影片筆記/ai-stitch-2-design-automation.jpg
category: 影片筆記
tags: [Stitch 2.0, 設計系統, Claude Code, React組件, Shadcn UI]
description: 'Google Stitch 2.0透過設計系統與Claude Code結合，解決AI生成網站外觀過於單調的問題，實現從設計到React組件的自動化工作流'
quote: '從頭開始設計並不總是好主意，模仿已證實有效的模式能幫助你更快做出真正好用的產品。'
action: '利用Enhanced Prompt功能讓AI代替你撰寫技術性的設計指令，並搭配Shadcn UI提升互動質感'
source_has_timestamps: true
---

**《4 Ways to Actually Use Stitch 2.0 in AI Coding》**
---

### 💡 核心摘要
這部影片詳細介紹了 Google **Stitch 2.0** 如何透過其強大的設計系統（Design System）與 **Claude Code** 或其他 AI 代理程式（Agents）結合，解決 AI 生成網站外觀過於單調、不一致的問題，並實現從設計到 React 組件的高效自動化工作流。

---

### 📝 詳細重點整理

#### 1. 核心機制：設計系統與 `design.md` 文件 [[00:45](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=45)]
* **跨平台移植性：** Stitch 使用 `design.md` 作為設計的「靈魂」，將顏色、主題、字體等視覺規範轉化為 AI 易於理解的語言，使設計能在不同 AI Agent 之間完美同步。
* **視覺化優勢：** 不同於單純的文字描述，Stitch 能將設計系統視覺化，讓開發者在實作前就能預覽色彩與字體配置 [[01:12](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=72)]。
* **自動生成與一致性：** 即使未明確要求，Stitch 也會自動建立設計系統，確保多次生成或多個頁面之間的風格保持高度一致 [[01:29](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=89)]。

#### 2. 風格參考與重塑功能 (Redesign Feature) [[04:09](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=249)]
* **非單純複製：** 新版 Stitch 不再只是依樣畫葫蘆，而是將上傳的截圖視為「風格指南」。
* **提取設計語言：** 它能分析參考網站的佈局模式、組件位置與設計語言，並將其應用到你自己的原創內容上 [[04:15](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=255)]。
* **多樣化輸入：** 除了全網頁截圖（推薦使用 GoFullPage 擴充功能），還可以透過輸入 URL 直接爬取風格，或上傳手繪草圖與線框圖（Wireframe）來對齊需求 [[05:15](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=315)]。

#### 3. 自動化開發工作流：Stitch 與 Claude Code 整合 [[06:44](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=404)]
* **增強提示詞 (Enhanced Prompt)：** 透過 Google 開發的 Skills，將模糊的指令轉化為 Stitch 優化的描述詞，因為 Stitch 更擅長處理「感性形容詞」而非精確描述 [[07:01](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=421)]。
* **自主構建循環 (Stitch Loop)：** 結合 Chrome DevTools，讓 AI Agent 能以自主模式反覆修正，直到完成整個網站的開發 [[07:20](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=440)]。
* **結構化實作：** 解決了 AI 產出冗長 HTML 的痛點，利用 `React component skill` 將設計自動拆解為模組化的 React 組件 [[08:04](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=484)]。

#### 4. 提升互動性：結合 UI 函式庫 (Shadcn UI) [[10:11](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=611)]
* **擺脫靜態頁面：** AI 直接生成的組件往往缺乏互動，透過 `shadcn UI skill`，可以引導 AI 將 Stitch 設計轉換為具有良好交互體驗的 Shadcn 組件。
* **豐富的套件整合：** 支援連接多個 Registry（如 Glassmorphism 或 Motion Primitives），讓生成的網站具備高級感與豐富的動畫效果 [[10:54](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=654)]。

---

### 🚀 結論與行動建議

**金句標註：**
> 「從頭開始設計並不總是好主意，模仿已證實有效的模式能幫助你更快做出真正好用的產品。」[[03:47](http://www.youtube.com/watch?v=b0lwCDNOFUY&t=227)]

**具體操作建議 (Step-by-Step)：**
1.  **準備階段：** 在你的 AI Agent 環境中安裝 Google 提供的 **Stitch MCP** 與相關技能（Skills）。
2.  **設計對齊：** 使用 `design.md` 模板或參考截圖定義網站風格，確保視覺風格與品牌一致。
3.  **優化指令：** 利用 `Enhanced Prompt` 功能，讓 AI 代替你撰寫技術性的設計指令。
4.  **模組化產出：** 執行 `React component skill` 將成果轉化為可維護的 React 程式碼，並搭配 **Shadcn UI** 提升互動質感。