---
title: 'Claude Code：Powerup與Insights'
date: 2026-04-05
image: /images/AI筆記/claude-code-powerup-insights.jpg
category: AI筆記
tags: [Claude Code, Powerup, Insights, 行為分析, 知識閉環]
description: '這段影片深入介紹了 Claude Code 的兩項被低估但極其強大的核心功能：/powerup 與 /insights。前者是針對新手的「80/20 法則」快速學習指南'
quote: '/powerup 帶你從 0 到 80 分，而 /insights 的持續回饋，則是讓你從 80 分跨越到 100 分的關鍵。'
action: '每週執行一次 /insights 閱讀報告，建立自定義 Skill 將建議寫入專案規則檔案。'
source_has_timestamps: true
---

## 核心摘要
這段影片深入介紹了 Claude Code 的兩項被低估但極其強大的核心功能：`/powerup` 與 `/insights`。前者是針對新手的「80/20 法則」快速學習指南，後者則是資深使用者的「私人教練」，能分析過去 30 天的行為數據並生成量身定制的成長報告，幫助使用者從熟練跨越到卓越。

---

## 詳細重點整理

### 1. `/powerup`：快速掌握 80% 的核心能力 [[01:03](http://www.youtube.com/watch?v=xssGpNx3its&t=63)]
* 這是為初學者設計的「學習同伴」，包含 10 個待解鎖的基礎模組。
* **重點內容**：
    * **@ 符號使用**：教導如何精準標記檔案，減少 Claude 盲目搜尋造成的 Context 消耗 [[01:26](http://www.youtube.com/watch?v=xssGpNx3its&t=86)]。
    * **模式切換與工具擴充**：引導使用者理解不同工作模式、自動化工作流及代理（Agent）運作邏輯 [[01:48](http://www.youtube.com/watch?v=xssGpNx3its&t=108)]。
* **關鍵概念**：**基礎結構化學習**。透過 ASCII 動圖教學，讓使用者在幾分鐘內掌握最關鍵的 20% 技巧，解決 80% 的日常需求。

### 2. `/insights`：數據驅動的行為分析報告 [[02:18](http://www.youtube.com/watch?v=xssGpNx3its&t=138)]
* 這是進階使用者的「私人教練」，會掃描過去 30 天的 JSONL 歷史對話，生成一份 HTML 格式的成績單。
* **重點內容**：
    * **正面反饋**：總結你做得好的部分，例如將 Claude 轉化為業務作業系統的程度 [[03:12](http://www.youtube.com/watch?v=xssGpNx3its&t=192)]。
    * **盲點偵測**：指出常見錯誤，如無效的診斷循環、過於模糊的提示詞（Prompting）或重複失敗的操作 [[04:48](http://www.youtube.com/watch?v=xssGpNx3its&t=288)]。
* **關鍵概念**：**自我迭代**。透過分析 Top Tools 使用率、常用程式語言與錯誤模式，找出影響效率的「摩擦點」。

### 3. 未來規劃與自動化優化建議 [[05:31](http://www.youtube.com/watch?v=xssGpNx3its&t=331)]
* `/insights` 報告中包含「On the Horizon」區塊，會根據你的使用習慣（如早晨工作流）生成專屬的 Meta Prompt。
* **實踐技巧**：
    * 直接輸入指令：「根據報告中的建議，將其存儲為 `.claud` 資料夾中的新規則」 [[06:42](http://www.youtube.com/watch?v=xssGpNx3its&t=402)]。
    * 結合 **Obsidian** 與 **Google Workspace CLI**，建立自動化技能（Custom Skill），定期將分析結果發送到信箱或存檔至知識庫 [[07:00](http://www.youtube.com/watch?v=xssGpNx3its&t=420)]。
* **關鍵概念**：**知識閉環**。將 AI 的反饋直接轉化為系統規則，實現軟體與人的協同進化。

---

## 結論與行動建議

* **啟發金句**：**「`/powerup` 帶你從 0 到 80 分，而 `/insights` 的持續回饋，則是讓你從 80 分跨越到 100 分的關鍵。」**
* **具體行動建議（80-100 進階法則）**：
    1. **更新版本**：確保 Claude Code 升級至 2.1.90 以上版本 [[00:46](http://www.youtube.com/watch?v=xssGpNx3its&t=46)]。
    2. **每週執行一次 `/insights`**：花 5 分鐘閱讀 HTML 報告中的「錯誤診斷」與「新功能嘗試」建議。
    3. **建立一個自定義 Skill**：串接 `/insights` 內容，將建議直接寫入專案規則檔案（System Rules），讓 AI 下次自動避開你的雷點。
* **生活實踐建議**：
    * **建立「AI 成長日記」**：在 Obsidian 或其他筆記工具中設立 `Claude Tips` 分頁，將每次 `/insights` 的精華手動或自動轉入，作為長期優化個人工作流的依據。

影片連結：[https://youtu.be/xssGpNx3its](https://youtu.be/xssGpNx3its)
