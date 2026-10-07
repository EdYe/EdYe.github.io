---
title: 'Build the Right Thing：產品工程（上）'
date: 2026-10-07
image: /images/影片筆記/build-right-thing-product-engineering-part-1.jpg
category: 影片筆記
tags: [產品工程, 下游性原則, 使用者脈絡, 媽媽測試, 當責判斷]
description: 'AI 正快速吃掉「實作」工作，唯一不會被自動化的是「知道該建造什麼」。這場工作坊以現場排隊入場的真實痛點為教材，示範工程師如何用 The Mom Test 驗證'
quote: '💡把錯的東西建造得再完美，仍然是錯的東西——速度沒有判斷力，只是更快地建造出錯的東西。'
action: '🎯1 + 4 法則：動手前先用 1 個問題定義痛點，再用事件、替代方案、代價、後果 4 個證據問題驗證，答不出具體內容就先別寫程式。'
source_has_timestamps: true
---
# 📝 Build the Right Thing: Product Engineering (Part 1) — Kent C. Dodds

## [核心摘要]

AI 正快速吃掉「實作」工作，唯一不會被自動化的是「知道該建造什麼」。這場工作坊以現場排隊入場的真實痛點為教材，示範工程師如何用 **The Mom Test** 驗證問題、用 Jobs-to-be-done 與 Kano Model 做產品判斷，把「把事情做對」的能力升級為「做對的事情」的產品工程判斷力。[[youtube](https://www.youtube.com/watch?v=_fHTqOs5wQA)][[finance.biggo](https://finance.biggo.com/podcast/2b5eaeb54f514000)]

## [詳細重點整理]

### 1. 簡報開始前的瓶頸 [00:12]

工作坊開場前，場館外大排長龍的入場隊伍本身，成了整場工作站的活教材：一款名為「**Just Get In the Workshop**」的 App 構想就此誕生——讓與會者不用錯過演講的前 20 分鐘。Kent C. Dodds 用這個當下的挫折感，練習判斷「一個問題是否值得用軟體解決」。[[youtube](https://www.youtube.com/watch?v=_fHTqOs5wQA)][[daily](https://daily.dev/posts/build-the-right-thing-product-engineering-part-1-kent-c-dodds-epicproduct-engineer-ct77am9yb)]

**關鍵概念：產品工程（Product Engineering）** —— 當 AI 讓程式碼產出愈來愈便宜，工程師的稀缺價值從「實作速度」移轉到「知道該建造什麼」的判斷力。[[kentcdodds](https://kentcdodds.com/better)]

### 2. 完成的實作仍是失敗的工作 [13:59]

「把東西建造對」（building the thing right）是「建造對的東西」（building the right thing）的**下游**。解決方案再完美，若是解決了一個不存在的問題，沒有人會使用它——兩者都重要，但只要在「對的東西」上失敗，整體就是失敗。做對的事優先，再把事做對。[[kentcdodds](https://kentcdodds.com/chats/07/02/the-right-thing-before-the-thing-right-product-engineering-with-wayne-allan)][[gitnation](https://gitnation.com/contents/becoming-product-engineers)]

**關鍵概念：下游性原則（Downstream Principle）**

### 3. 客戶脈絡改變工程決策 [21:18]

工程師必須縮短自己心中的心智模型與使用者實際模型之間的落差：理解使用者真正的問題、對問題（而非自己的解決方案）投入感情，並且在動鍵盤前先驗證問題是否真實存在——「挖掘真實的使用者痛點，而不是 solution-shaped 的故事」。[[gitnation](https://gitnation.com/contents/build-the-right-thing-product-engineering-for-software-developers-3752)]

**關鍵概念：使用者脈絡（Customer Context）**

### 4. 建造工作環境，並看超越你的 ticket [28:17]

工程師的工作不是關 ticket 而已。當 coding agent 承擔更多實作時，工程師要負責的是代理賴以運作的**系統環境**：API、資料實體、UI 元件等工作件（primitives）。壞的 primitives 會強迫產出壞的結果，無論 prompt 多好——「AI 不會修好你的架構，它只會繞過它」。[[linkedin](https://www.linkedin.com/posts/kentcdodds_your-coding-agent-needs-better-primitives-activity-7483181239764668417-vEmh)][[coderabbit](https://www.coderabbit.ai/blog/the-last-software-engineer-knows-what-to-build)]

**關鍵概念：工作件思維（Primitives）**

### 5. Just Get In the Workshop：建造之前先改變問題 [36:55]

工作站命名了三大框架：早期驗證用 **The Mom Test**、拆解需求用 **Jobs Theory**（jobs-to-be-done）、排優先序用 **Kano Model**。本段深入展開第一項。[[ai](https://ai.engineer/talks/_fHTqOs5wQA-build-right-thing-product-engineering-part-1)]

The Mom Test 的核心是**改變訪談的對象**：請人評估你的點子，只會得到禮貌性的安慰；請對方描述一次具體經歷，工程師才有行為可以解讀。投影片將「你會用這個嗎？」「問題是什麼？」對比為四種蒐集證據的提問：

- **事件（Episode）**：告訴我上次發生這件事是什麼時候？誰在其中？為什麼煩到讓你記得？
- **替代方案（Workaround）**：你當時怎麼繞過去的？這揭露新解決方案必須融入或取代的既有流程
- **代價（Cost）**：那個替代方案花了你多少錢、時間或力氣？問題發生頻率多高？
- **後果（Consequence）**：沒有更好的解決方案，你正在失去什麼？

以工作坊排隊為例：問題從「排隊好煩，做個自動入場 App」被重新框定為「付費學員錯過演講前 20 分鐘的損失值不值得改變」，接著追問學員做了什麼、延遲影響多大、發生頻率是否足以正當化改變。這些答案會反過來約束解決方案的設計。[[ai](https://ai.engineer/talks/_fHTqOs5wQA-build-right-thing-product-engineering-part-1)]

**關鍵概念：媽媽測試（The Mom Test）** —— 媽媽永遠會說你的點子很棒，因為她愛你；所以永遠問過去行為，絕不問對方對你方案的評價。[[kentcdodds](https://kentcdodds.com/chats/07/02/the-right-thing-before-the-thing-right-product-engineering-with-wayne-allan)][[ai](https://ai.engineer/talks/_fHTqOs5wQA-build-right-thing-product-engineering-part-1)]

### 6. 在為所有人工程之前先驗證需求 [45:58]

**問題驗證**與**解決方案驗證**回答不同的問題：Mom Test 建立的是「問題是否值得投入」；原型（prototype）則讓使用者揭示「這個特定方案能否帶他們到達目的地」。早期採用者即使面對大量缺陷仍保持興奮，代表核心利益是真的；使用者遇到幾次困難就棄用，也是解決方案價值的證據。[[ai](https://ai.engineer/talks/_fHTqOs5wQA-build-right-thing-product-engineering-part-1)]

### 7. 原型接觸使用者後持續學習 [49:05]

上線不是終點。建立 ship 後的回饋迴圈（feedback loops），區分「可量測的改善」與「真正的改善」，持續驗證自己建造的東西是否仍值得存在。[[gitnation](https://gitnation.com/contents/build-the-right-thing-product-engineering-for-software-developers-3752)]

**關鍵概念：回饋迴圈（Feedback Loop）**

### 8. 角色改變，技術當責仍在 [51:35]

即使 AI 代理承擔愈多實作與審查，「當責判斷」（accountable judgment）必須留在人的迴圈裡：代理能告訴你某個改變**能不能**做（could）；產品工程師決定它**該不該**存在（should），並為這個答案及其後果負責。[[coderabbit](https://www.coderabbit.ai/blog/the-last-software-engineer-knows-what-to-build)]

**關鍵概念：當責判斷（Accountable Judgment）**

## [結論與行動建議]

**啟發金句**：把錯的東西建造得再完美，仍然是錯的東西——速度沒有判斷力，只是更快地建造出錯的東西。

**具體行動建議**：**「1 + 4 法則」** —— 動手之前，先用 1 個問題定義痛點，再用 4 個證據問題（事件、替代方案、代價、後果）驗證它。任何一題答不出具體內容，就先別寫程式。[[ai](https://ai.engineer/talks/_fHTqOs5wQA-build-right-thing-product-engineering-part-1)]

**生活實踐建議**：

- 對 AI 開發工作流：讓 agent 寫程式前，先列出這個功能解決的使用者問題與其發生頻率；把「問題驗證」變成 prompting 的第一個 step，而不是直接下實作指令
- 對 YouTube 內容創作：驗證影片題材時不要問朋友「這主題好不好」，改問「你上次為了找這類資訊做了什麼、卡在哪裡」
- 對購物與專案決策：買設備或啟動 side project 前，先回想自己上次的 workaround 花了多少時間成本，頻率是否高到值得投入

## [參考連結]

- 原始影片：[Build the Right Thing: Product Engineering (Part 1) — Kent C. Dodds](https://www.youtube.com/watch?v=_fHTqOs5wQA)（AI Engineer 頻道，2026-10-05，全長 55:19）[[youtube](https://www.youtube.com/watch?v=_fHTqOs5wQA)]
- 延伸：[Part 2](https://www.youtube.com/watch?v=s0hFne6EeOI) 深入 Jobs-to-be-done 與 Kano Model，含完整時間戳章節[[youtube](https://www.youtube.com/watch?v=s0hFne6EeOI)]
- 官方課程：[Epic Product Engineer](https://www.epicproduct.engineer/)[[epicproduct](https://www.epicproduct.engineer/)]