---
title: 'Claude Code結合Firecrawl突破爬蟲瓶頸'
date: 2026-03-31
image: /images/影片筆記/claude-code-firecrawl-scraping.jpeg
category: 影片筆記
tags: [Claude Code, Firecrawl, 網頁爬蟲, 資料擷取, 自動化]
description: '深入探討如何透過結合Claude Code與Firecrawl，徹底解決AI在網頁爬蟲時遇到的瓶頸，顯著提升資料獲取的成功率與處理速度'
quote: '工欲善其事，必先利其器；當原生AI觸及天花板時，整合正確的外部工具能讓你的生產力實現量級躍遷。'
action: '註冊Firecrawl獲取API Key、整合Skill到Claude Code、練習定義Schema以獲取精簡資料'
source_has_timestamps: true
---

## 核心摘要
本影片深入探討如何透過結合 **Claude Code** 與 **Firecrawl**，徹底解決 AI 在網頁爬蟲時遇到的瓶頸。Claude Code 原生的網頁抓取能力（Web Fetch）在面對動態 JavaScript 渲染或防爬蟲機制（Anti-bot）時常顯得力不從心，而 Firecrawl 的介入能將網頁資訊轉化為高效的 Markdown 格式，顯著提升資料獲取的成功率與處理速度，是進行大規模市場調研與競爭分析的利器。

---

## 詳細重點整理
### 1. Claude Code 的先天限制與解決方案 [[00:00](http://www.youtube.com/watch?v=phuyYL0L7AA&t=0)]
* Claude Code 在處理重度依賴 JavaScript 的網站或具有防爬蟲保護的頁面時，經常回傳空結果或效率低下。
* **關鍵概念**：**Firecrawl 整合**。它能將複雜的 HTML 簡化為大語言模型（LLM）易於理解的 Schema 與 Markdown，減少 Token 消耗並繞過偵測。

### 2. Firecrawl 的核心能力與動作指令 [[01:08](http://www.youtube.com/watch?v=phuyYL0L7AA&t=68)]
* 影片介紹了 Firecrawl 提供的八種主要動作，其中最重要的包括：
    * **Scrape (抓取)**：給予 URL 直接獲取單頁內容 [[03:19](http://www.youtube.com/watch?v=phuyYL0L7AA&t=199)]。
    * **Crawl (爬取)**：從一個起點自動遍歷整個網站 [[03:32](http://www.youtube.com/watch?v=phuyYL0L7AA&t=212)]。
    * **Search (搜索)**：在不知道確切網址的情況下，先搜尋再抓取 [[03:39](http://www.youtube.com/watch?v=phuyYL0L7AA&t=219)]。
    * **Agent (智能代理)**：最強大的功能，自動判斷需要採取的動作組合，但消耗額度較高 [[04:02](http://www.youtube.com/watch?v=phuyYL0L7AA&t=242)]。
* **關鍵概念**：**Browser Interact**。這是最新功能，能模擬人類點擊、捲動等行為，如同 Playwright 的自動化操作 [[04:33](http://www.youtube.com/watch?v=phuyYL0L7AA&t=273)]。

### 3. 實戰效能對比測試 [[05:45](http://www.youtube.com/watch?v=phuyYL0L7AA&t=345)]
* **測試一 (動態網站)**：針對 Similar Web 進行測試，Claude 原生抓取在 5 分鐘後掛掉，而 Firecrawl 僅花 **42 秒** 就完整提取了所有流量指標 [[07:01](http://www.youtube.com/watch?v=phuyYL0L7AA&t=421)]。
* **測試二 (防爬蟲機制)**：針對 Yellow Pages 測試，Claude 原生被 403 錯誤攔截，Firecrawl 則在 **53 秒** 內成功抓取 16 筆商業資訊 [[08:09](http://www.youtube.com/watch?v=phuyYL0L7AA&t=489)]。
* **關鍵概念**：**效能差距**。在大規模任務中，Firecrawl 能節省約 80% 以上的時間與成本。

### 4. 開源與雲端版本的抉擇 [[09:34](http://www.youtube.com/watch?v=phuyYL0L7AA&t=574)]
* Firecrawl 是開源產品，可以透過 Docker 自行架設，但會失去其專有的「Anti-bot 引擎」與「Agent」等進階功能。
* **關鍵概念**：**專有技術價值**。若需處理高度商業化的防爬蟲網站，建議使用其雲端服務。

---

## 結論與行動建議
* **啟發金句**：'工欲善其事，必先利其器；當原生 AI 觸及天花板時，整合正確的外部工具能讓你的生產力實現量級躍遷。'
* **具體行動建議（3-S 安裝法則）**：
    1. **Setup Account**：前往 Firecrawl 官網註冊並獲取 API Key。
    2. **Skill Install**：在 Claude Code 終端機輸入指令，將 Firecrawl Skill 與 CLI 整合。
    3. **Schema Define**：練習在抓取前定義具體 Schema（如：價格、評分、名稱），以獲取最精簡的資料結果。
* **生活實踐建議**：
    * **建立自動化監測錨點**：利用 `crawl` 功能，每週定期對競爭對手或感興趣的電商頁面進行一次自動化數據追蹤。
    * **觀察紀錄**：記錄在使用原生抓取失敗的案例，對比使用 Firecrawl 後的成功率，建立屬於自己的「高難度網站抓取清單」。

影片連結：[https://www.youtube.com/watch?v=phuyYL0L7AA](https://www.youtube.com/watch?v=phuyYL0L7AA)
