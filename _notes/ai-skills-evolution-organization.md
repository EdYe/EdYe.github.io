---
title: 'AI技能演進：從提示詞到組織基礎設施'
date: 2026-03-31
image: /images/影片筆記/ai-skills-evolution-organization.jpeg
category: 影片筆記
tags: [AI技能, 提示詞工程, 組織知識, 自動化工作流, 技能複利]
description: '探討AI技能的演進，指出技能已從個人的提示詞配置轉變為組織與Agent可讀的基礎設施標準，實現更精準、可複用且具複利效應的自動化工作流'
quote: '提示詞會隨對話蒸發，但技能會隨時間複利。技能是人類專業知識的活紀錄。'
action: '選出3個重複性任務、建立skill.markdown文件、進行5次定量測試並疊代更新'
source_has_timestamps: true
---

## 核心摘要

本影片探討了 AI「技能」（Skills）的演進，指出技能已從個人的提示詞配置，轉變為組織與 Agent（代理）可讀的基礎設施標準。透過將專業知識封裝成 Markdown 格式的技能文件，使用者能擺脫重複複製貼上的「提示詞地獄」，實現更精準、可複用且具複利效應的自動化工作流。

-----

## 詳細重點整理

### 1\. 技能的四大演進趨勢 [[01:04](http://www.youtube.com/watch?v=0cVuMHaYEHE&t=64)]

  * **從個人配置到組織基礎設施**：技能現在是工作場所通用的資產，具備版本控制並可跨平台（Excel, PowerPoint, Claude）調用。
  * **調用者由人轉向 Agent**：Agent 單次運行可調用數百次技能，遠超人類效率，因此技能設計應以「Agent 優先」。
  * **跨平台開放標準**：OpenAI、Microsoft 與 Anthropic 已達成共識，技能成為 AI 運作的共同底層架構。
  * **從閉源走向社區共享**：技能像「棒球卡」一樣被交換與優化，透過社區集體發現最佳實踐。
  * **關鍵概念**：**技能複利（Skills Compound）**：提示詞會隨對話結束消失，但技能會隨時間優化並產生長期價值。

### 2\. 打造高效技能的關鍵要素與地雷 [[09:32](http://www.youtube.com/watch?v=0cVuMHaYEHE&t=572)]

  * **描述（Description）是成敗關鍵**：避免模糊描述（如「幫助分析」），應包含具體觸發詞與輸出類型，且**必須保持在單一行**，否則 AI 無法讀取 [[10:28](http://www.youtube.com/watch?v=0cVuMHaYEHE&t=628)]。
  * **方法論（Methodology）的五大支柱** [[10:49](http://www.youtube.com/watch?v=0cVuMHaYEHE&t=649)]：
    1.  **推理過程**：提供決策框架而非單純步驟。
    2.  **具體格式**：明確指定 Markdown、Excel 或 PDF 等。
    3.  **邊緣案例**：寫下所有人類視為常識但 AI 可能出錯的情況。
    4.  **範例參考**：提供樣板讓 AI 模式匹配。
    5.  **保持精簡**：核心文件建議在 100-150 行以內，避免膨脹上下文。
  * **關鍵概念**：**API 合約化**：將技能視為一種合約，明確定義 Agent 能得到什麼與不能得到什麼。

### 3\. 組織技能的三層體系 [[18:53](http://www.youtube.com/watch?v=0cVuMHaYEHE&t=1133)]

  * **第一層：標準技能**：品牌語氣、格式規範等全公司通用的準則。
  * **第二層：方法論技能**：資深員工的專業核心，能大幅縮短新進人員的學習曲線 [[19:29](http://www.youtube.com/watch?v=0cVuMHaYEHE&t=1169)]。
  * **第三層：個人工作流**：解決日常瑣事的私人技能，建議系統化存儲以防突發狀況。
  * **關鍵概念**：**隱性知識顯性化**：將專家腦中的「手感」轉化為 Agent 可執行的 Markdown 文件。

-----

## 結論與行動建議

  * **啟發金句**：**「提示詞會隨對話蒸發，但技能會隨時間複利。技能是人類專業知識的活紀錄。」** [[25:06](http://www.youtube.com/watch?v=0cVuMHaYEHE&t=1506)]

  * **具體行動建議（3-1-5 法則）**：

    1.  **選出 3 個重複性任務**：找出你每週至少做 2 次的工作（如會議摘要、數據清理）。
    2.  **建立 1 個 `skill.markdown` 文件**：將上述任務的推理邏輯、格式要求與範例寫入。
    3.  **進行 5 次定量測試**：針對不同輸入測試技能表現，並像軟體版號一樣進行疊代更新。

  * **生活實踐建議**：

      * **建立技能庫**：不要將技能散落在各處，使用 GitHub 或 Notion 建立自己的「技能倉庫」。
      * **Agent 測試思維**：在交給 Agent 執行前，先手動模擬 10 次，確保所有邊緣案例（Edge Cases）都已寫入技能文件中。
      * **觀看連結**：[Anthropic, OpenAI, and Microsoft Just Agreed on One File Format](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3D0cVuMHaYEHE)
