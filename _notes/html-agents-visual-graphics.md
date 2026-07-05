---
title: 'HTML是Agent做視覺任務的正解'
date: 2026-07-05
image: /images/影片筆記/html-agents-visual-graphics.jpg
category: 影片筆記
tags: [語言原生性, HTML版面能力, 座標式工具錯配, 資料驅動生成, Nori實戰案例]
description: '這部影片揭示一個關鍵洞察：AI Coding Agent 並非真的不擅長處理視覺與空間任務，問題出在工具本身用人類的操作邏輯（拖曳、座標、像素）強加給 Agent'
quote: '💡不要用使用者的角度思考，要用模型的角度思考（Stop thinking like a user. Think like the model.）'
action: '🎯善用H-T-M法則，讓Agent優先以HTML/CSS作為中介格式產出視覺成品，再轉換成最終呈現格式'
source_has_timestamps: true
---
## 核心摘要

這部影片揭示了一個關鍵洞察：AI Coding Agent 並非真的不擅長處理視覺與空間任務，問題出在工具本身用人類的操作邏輯（拖曳、座標、像素）強加給 Agent。講者 Amol Kapoor 主張應該讓 Agent 用它最熟悉的「語言」——HTML——來建構投影片、文件甚至影片，因為 HTML 的標籤本身就帶有語意結構（標題、圖表、網格），讓模型能以「結構化思考」取代「座標運算」，從而徹底解決 Agent 在製作視覺成品時常見的版面錯位、文字重疊等問題。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

## 詳細重點整理

1. 座標式工具是錯配的根源 [00:44]
PowerPoint、Figma、Canva 這類工具的底層資料結構，是為了人類手眼協調（點擊、拖曳、對齊網格）而設計，當交給 Agent 操作時，輸出常常版面錯亂、文字看不清。**人機介面錯配**正是 AI 在視覺任務上「看起來很爛」的真正原因，而非模型本身缺乏空間推理能力。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

2. SVG 鵜鶘測試暴露的盲點 [02:00]
開發者 Simon Willison 設計的經典測試——要求模型畫出「騎自行車的鵜鶘」並限制只能用 SVG，結果模型的輸出普遍很糟，常被當作 AI 缺乏幾何理解的證據。但講者指出，這個測試的問題在於 SVG 本身就是一堆數字座標，連人類自己手寫 SVG 都畫不出鵜鶘，這不是公平的能力測試。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

3. 媒介決定思考方式 [02:45]
真正的關鍵概念是**「語言原生性」（native medium）**：模型訓練時看過數十億筆 HTML 範例，天生理解標籤背後的語意（標題就是標題、網格就是網格），而 SVG 純粹是數字陣列，沒有語意可循。把畫布操作丟給 Agent，就像要求人類手寫 SVG 一樣不合理。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

4. HTML 讓模型「免費」獲得版面能力 [03:39]
因為瀏覽器負責把 HTML/CSS 渲染成像素，模型只需要輸出結構化標記，不必自己計算任何座標，圖表、字型、動態效果全部可以透過既有的網頁技術達成。這正是講者主張「HTML is all you need」的技術核心。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

5. 投影片本質與編輯格式可分離 [04:34]
講者點出一個常被忽略的事實：「投影片」與「PowerPoint」並非同義詞，PowerPoint 只是其中一種編輯／呈現模式，觀眾根本不關心你用什麼工具產出最終畫面。這意味著可以自由選擇 Agent 已經擅長的編輯格式（HTML），最後再轉成 PDF 或其他輸出格式即可。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

6. Nori 的實戰案例：看板、銷售、文件、影片全用 HTML [05:16]
Nori 公司用這套 HTML 方法製作董事會報告、銷售簡報、品牌文件，甚至連這支介紹影片本身的視覺效果都是純 HTML/CSS（「divs all the way down」）所構成。這證明此方法已超越概念驗證，進入日常生產流程。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

7. 資料驅動的端到端產出 [06:08]
講者強調漂亮的版面本身沒有價值，關鍵是要讓模型存取通話逐字稿、Email 等真實資料，才能端到端自動生成完整內容，他甚至曾在通勤地鐵上用手機完成整份董事會報告。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

## 結論與行動建議

啟發金句：「不要用使用者的角度思考，要用模型的角度思考」（Stop thinking like a user. Think like the model.）。 [youtube](https://www.youtube.com/watch?v=ikb6kqhsDw4)

具體行動建議：可採用**「H-T-M 法則」（HTML for Thinking, Theming, and Media）**——凡是要 Agent 產出視覺成品，優先以 HTML/CSS 作為中介格式，再轉換成最終呈現格式（PDF、影片等）。

生活實踐建議：身為產品架構師，下次需要 Agent 產出簡報、報告或視覺化儀表板時，可以直接要求 LLM 輸出 HTML/CSS 而非要求它操作 Figma MCP 或截圖比對迴圈，能大幅減少版面錯位與返工時間，並更貼合既有品牌風格的客製化需求。

## 參考連結

https://youtu.be/JRTAtZ5iBkU
