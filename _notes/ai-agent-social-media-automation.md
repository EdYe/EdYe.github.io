---
title: 'AI經紀人打造社群媒體自動化系統'
date: 2026-03-29
image: /images/影片筆記/ai-agent-social-media-automation.jpg
category: 影片筆記
tags: [Claude Code, 社群自動化, 短影音剪輯, Voice DNA, 內容排程]
description: '透過Claude Code建立具備17種專業技能的AI經紀人系統，能自動完成長影片轉短影音、LinkedIn專業貼文製作及長影片自動剪輯排程'
quote: '在這個AI快速進化的時代，開始實施AI代理人流程是你能做的最好的事情。'
action: '在系統中設定自己的語氣風格（Voice DNA），避免產出過於死板的「AI罐頭味」'
source_has_timestamps: true
---

這部影片詳細介紹了如何利用 **Claude Code** 結合一系列 AI 工具與 API，打造一套全自動化的社群媒體內容產製系統，從影片剪輯、圖文生成到自動排程發布，實現一人團隊的高效率轉型。

### **核心摘要**
**本影片展示了如何透過 Claude Code 建立一個具備 17 種專業技能的 AI 經紀人系統，能自動完成長影片轉短影音、LinkedIn 專業貼文製作及長影片自動剪輯排程等繁瑣任務。**

---

### **詳細重點整理**

#### **1. AI 社群媒體經紀人系統架構 [[04:16](http://www.youtube.com/watch?v=GSnKzuy-byk&t=256)]**
* **核心引擎：** 使用 Claude Code 作為開發與溝通介面，整合了 16-17 種專門針對內容創作開發的「技能 (Skills)」。
* **關鍵工具橋樑：**
    * **Cernio (原名 Late)：** 核心社交媒體 API，負責將內容發布至 YouTube、Instagram、TikTok、LinkedIn 等平台，並追蹤數據。
    * **Key.ai：** 提供視覺生成的 API，支持圖像 (如 Flux/Nano Banana) 與影片生成。
    * **Remotion & Clip Extractor：** 用於程式化影片剪輯與自動提取精華片段。

#### **2. 實戰專案一：長影片自動轉化短影音 [[17:35](http://www.youtube.com/watch?v=GSnKzuy-byk&t=1055)]**
* **執行流程：** AI 自動下載長篇 Podcast (如 Lex Fridman 的訪談)，提取逐字稿並挑選出 7 個最佳片段。
* **自動化編輯：** 系統會自動將影片裁切為 9:16 直式格式、追蹤人物臉部位置、加入字幕、轉場、插圖與背景音效 [[19:46](http://www.youtube.com/watch?v=GSnKzuy-byk&t=1186)]。
* **排程發布：** 自動將 7 支影片排程至一週七天，並同步推播至 YouTube Shorts、Instagram Reels 和 TikTok。

#### **3. 實戰專案二：LinkedIn 專業圖文內容製作 [[20:56](http://www.youtube.com/watch?v=GSnKzuy-byk&t=1256)]**
* **內容研究：** AI 深入分析特定技術文章 (例如 Nvidia 的 Nemo Guardrails)，並根據作者的「個人聲音 DNA (Voice DNA)」撰寫文案 [[22:31](http://www.youtube.com/watch?v=GSnKzuy-byk&t=1351)]。
* **視覺產出：** 同時生成一張資訊圖表 (Infographic) 以及一套 8 頁的投影片式卡片 (Document Carousel)。
* **草稿管理：** 生成的內容會直接以「草稿」形式上傳至 Cernio 儀表板，方便作者進行最後確認。

#### **4. 實戰專案三：全自動長影片生成 [[24:16](http://www.youtube.com/watch?v=GSnKzuy-byk&t=1456)]**
* **全方位產製：** 僅需一個指令，AI 便執行網路搜尋、撰寫 5 分鐘腳本、生成配音、製作視覺素材並用 ffmpeg 合成影片。
* **YouTube 優化：** 同時自動產出影片縮圖 (Thumbnail)、說明欄、標籤 (Tags) 以及影片時間軸戳記 [[25:41](http://www.youtube.com/watch?v=GSnKzuy-byk&t=1541)]。

---

### **結論與行動建議**
* **核心金句：** 「在這個 AI 快速進化的時代，開始實施 AI 代理人流程是你能做的最好的事情。」
* **具體建議：** 1.  **建立 Voice DNA：** 在系統中設定自己的語氣風格，避免產出過於死板的「AI 罐頭味」。
    2.  **善用指令技巧：** 建議在 session 開始時使用 `/continue` 加載上下文，結束時使用 `/done` 存檔 [[15:41](http://www.youtube.com/watch?v=GSnKzuy-byk&t=941)]。
    3.  **開源資源：** 作者已將此系統代碼上傳至 GitHub，建議創作者可以從中學習如何串接多個 API 實現工作流自動化。