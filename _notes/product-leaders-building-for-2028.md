---
title: '為 2028 超前部署：Eval 就是新 PRD'
date: 2026-07-27
image: /images/影片筆記/product-leaders-building-for-2028.jpg
category: 影片筆記
tags: [可解釋性特徵, 前沿產品與前沿模型共生, 湧現能力跳躍, Eval驅動開發, 人類判斷壟斷]
description: '本集訪談邀請 Dianne Penn（Anthropic AI 研究與 Labs 團隊產品負責人），深入解析 Anthropic 從 2023 年僅五名工程師的弱勢團隊，躍升為史上'
quote: '💡你需要前沿產品才能擁有前沿模型——兩者共生，缺一不可。'
action: '🎯將產品開發核心從寫 PRD 轉向建 Eval 集：每個模型迭代先建 eval、再測試、最後產品化。'
source_has_timestamps: true
---
## [核心摘要]

本集訪談邀請 **Dianne Penn**（Anthropic AI 研究與 Labs 團隊產品負責人），深入解析 Anthropic 從 2023 年僅五名工程師的弱勢團隊，躍升為史上成長最快公司的關鍵歷程。核心貢獻在於揭示 **「Eval 驅動開發循環」**（Eval-Driven Development Loop）如何取代傳統 PRD，讓產品在模型尚未就緒時就能前置部署、快速驗證，解決了 AI 產品開發中「模型能力不確定、產品迭代難以規劃」的核心痛點 。 [youtube](https://www.youtube.com/)

***

## [詳細重點整理]

### 1. 早期 Anthropic 的文化基石 [02:31]

2023 年加入時，整個產品團隊僅五名工程師，API 業務甚至只有一名工程師負責。公司當時的核心優勢不在技術規模，而在「使命、文化、價值觀」的深度踐行。一個代表性事件是 **Golden Gate Claude**：2024 年初基於可解釋性研究，團隊發現模型內部層存在表達特定主題的「特徵」，其中一項是金門大橋。調高該特徵後，Claude 會在每個回覆中執著於金門大橋。整個體驗在 24 小時內由工程、產品、設計、研究團隊協作上線，雖然最終僅觸及約 2,000 名用戶，但讓團隊意識到「能以不同於競爭對手的方式，將研究成果轉化為用戶體驗」，成為 Anthropic 找到自我認同的隱藏轉折點 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：可解釋性特徵**

### 2. Opus 3 — 首個前沿模型的里程碑 [08:55]

訓練 Opus 3 時公司不到 200 人。核心問題是「為什麼有人應該選擇 Claude？」。2023 年，沒有人會將 Anthropic、Claude 與程式碼放在同一句話中。當時 GPT-4 雖用於程式碼，但僅是多種用途之一。Dianne 觀察到人們開始用模型撰寫長篇程式碼（而非僅自動補全），判斷這是機會點，於是投入訓練 Opus 3 使其更擅長程式碼。從訓練角度來看是相對較小的調整，卻在早期為用戶帶來了當時被認為不可能的差異化價值 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：長篇程式碼生成**

### 3. Opus 4.5 — 模型與產品共生的奇蹟 [13:50]

Opus 4.5（恰好也是一年後的寒假期間發布）之所以具備魔力，在於不再「只有模型」，還有了「載體」——一個優秀的產品體驗 Claude Code。團隊有一句核心信條：「**需要前沿產品才能擁有前沿模型，才能讓人們感受到前沿模型的魔力。**」Opus 4.5 如果沒有 Claude Code 這樣的產品，不會有那個爆發時刻；Claude Code 沒有 Opus 4.5，也不會有那種加速的採用。兩者缺一不可 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：前沿產品與前沿模型共生**

### 4. 指數曲線中的適應力 [13:50]

模型正處於指數曲線的「內部」，意味著每一次改善都是巨大的跳躍。Dianne 強調三個核心能力：**適應力**（面對新資訊時能否調整決策，而非堅守原計畫）、**第一性原理思考**（推演「下一步是什麼」）、以及**組織內部信任**。Scaling Laws 論文中最有趣的不只是平滑的 loss 下降曲線，而是**湧現能力** 的不連續跳躍——模型從「無法計算 1+1」到「能可靠計算 1+1」的瞬間發生，而這些跳躍可能在你不自覺時就已完成 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：湧現能力跳躍**

### 5. Token Maxing — 體驗未來的捷徑 [20:02]

YC 總裁 Garry Tan 提出一個觀點：如果你現在願意每年花 10 萬美元在 token 上，你就是在過 2028 年的生活——屆時 token 成本大幅降低，人人皆可如此工作。Dianne 從產品視角補充：token 花費是輸入，真正的輸出是**實驗**。她觀察到 Anthropic 內部最具創造力的思考者和原型構建者，確實會花大量時間與每個新版研究模型互動。內部有一個 Slack 頻道，幾乎全公司都在公開測試早期版本 Claude，嘗試不同用途，在約 10 次請求內就會有「魔法」或新用例湧現。實驗不是個人運動，而是**社群發現** 的過程 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：社群發現式實驗**

### 6. Anthropic Labs 的孵化模式 [23:30]

Labs 的核心論題是：識別並追蹤那些不在核心路線圖中的**不連續大型押注**，判斷是否有「實質」，以及其 10 倍、100 倍、1,000 倍的潛力。Claude Code、Skills、Claude Design、MCP 皆出自 Labs。2025 年的方法論是：對主題或領域持有強烈觀點，但對具體原型保持每週更新式的靈活。有時一個論題「現在還不行」，就會在 1 到 2 個模型世代後重新檢視。關鍵在於團隊規模小——有時一個想法就是從一名工程師開始。過大的團隊反而會因協調成本拖慢零到一的進程 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：不連續大型押注**

### 7. 研究員的角色與成功特質 [27:30]

研究員不僅是日常的「假設→資料→演算法→測試→迭代」循環，更承載對未來的願景（如公司創立時就已在討論如何讓 Claude 使用電腦）。PM 團隊的角色是將模糊的用戶反饋轉化為研究員可執行的語言——例如「Claude 幻覺」需被拆解為：應該呼叫工具卻未呼叫（工具使用失敗）、查看了正確文件但提取了錯誤事實（知識/搜索綜合失敗）、或對齊問題。最成功的研究員具備三大特質：**第一性原理思考能力**、對研究領域的熱情與大膽描繪、以及**貼近細節**（親自查看訓練過程的 eval 結果和底層資料）。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：第一性原理思考**

### 8. Evals Are the New PRDs [44:16]

團隊有一句核心口號：**「Evals 就是新的 PRD。」** 傳統產品需求文件（PRD）在 AI 產品開發中被評估集取代——因為模型能力不確定，唯有透過系統化的 eval 測試才能定義「成功」長什麼樣。Dianne 頻繁問團隊的一個問題是：「假設 Claude 8 來了，用戶行為會怎麼改變？這對你今天怎麼建構產品意味著什麼？」——以此確保產品設計的**向前相容性** 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：Eval 驅動開發**

### 9. Claude 的「憲法」與拒絕文化 [01:03:50]

Claude 願意推回（push back）是其成功的關鍵特質之一。Claude 不會盲目服從用戶指令，而是基於其內化的憲法原則判斷請求是否合理，這讓它在需要深度推理和品質把關的場景中表現更可靠 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：憲法式對齊**

### 10. 人類判斷的不可替代性 [01:11:40]

在 AI 寫作與驗證方面，Dianne 強調**避免過度依賴 AI**。她分享自己的使用方式：用 Claude 輔助思考和起草，但最終判斷必須由人類承擔。她用 Claude 8 的思想實驗來引導團隊思考——即使模型能力飛速進步，人類在以下領域仍持續有價值：定義「什麼值得做」的品味與方向判斷、跨領域的脈絡綜合、以及道德與社會影響的最終問責 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

**關鍵概念：人類判斷壟斷**

***

## [技術/數據對比]

| 維度 | 傳統產品開發 | Anthropic 的 Eval 驅動開發 |
|------|------------|------------------------|
| 需求定義 | PRD（產品需求文件） | Eval 集（評估測試集） |
| 模型能力 | 確定，可精確規劃 | 不確定，需系統化測試發掘 |
| 反饋處理 | 用戶反饋直接進入迭代 | 拆解為工具/知識/對齊三層可執行分類 |
| 產品策略 | 基於當前模型能力規劃 | 基於「Claude 8 來了會怎樣」向前相容設計 |
| 實驗模式 | 個人探索 | 全公司公開 Slack 頻道社群發現 |
| Labs 賭注 | 大團隊追蹤大方向 | 小團隊（甚至單人）追蹤不連續押注 |

***

## [結論與行動建議]

> **「你需要前沿產品才能擁有前沿模型——兩者共生，缺一不可。」**

**具體行動法則：E-D-D 法則（Eval-Driven Development）**

將產品開發的核心從「寫 PRD」轉移到「建 Eval 集」——用系統化評估定義成功標準，取代靜態需求文件。在每個模型迭代中，先建 eval、再測試、最後產品化。

**生活實踐建議**

作為 AI 應用架構師與產品經理，建議每週撥出固定時間進行「社群發現式實驗」：與團隊在共享頻道中公開測試最新模型版本，每人嘗試 10 次不同 prompt，從中提煉新用例與產品機會。同時，在每次產品規劃會議中加入一個固定議程：「如果下一個模型世代能力翻倍，這個設計還成立嗎？」——以此確保你的產品路線圖始終向前相容 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

***

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/tivaWTTVRhY
- Lenny's Newsletter 完整逐字稿：https://www.lennysnewsletter.com/p/anthropics-first-technical-pm-on
- Dianne Penn LinkedIn：https://www.linkedin.com/in/dianne-na-penn
- Tokenmaxxing (YC)：https://www.ycombinator.com/library/Pa-tokenmaxxing-how-top-builders-use-ai-to-do-the-work-of-400-engineers
- Anthropic Labs 介紹：https://www.anthropic.com/news/introducing-anthropic-labs
- Golden Gate Claude：https://www.anthropic.com/news/golden-gate-claude
