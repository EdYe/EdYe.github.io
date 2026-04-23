---
title: 'AI 捕捉決策脈絡：Decision Record 五大支柱'
date: 2026-04-23
image: /images/AI筆記/ai-capture-decision-record.jpeg
category: AI筆記
tags: [決策脈絡, Decision Record, AI輔助, 脈絡守護, 知識管理]
description: '本文探討在軟體開發與團隊協作中，決策脈絡（Context）消失所帶來的隱性成本。透過 Decision Record (DR) 機制並利用 AI 從對話記錄中提煉決策理由，讓 AI 成為脈絡守護者。'
quote: '程式碼會留下，但脈絡會蒸發；我們捕捉決策，是為了給未來的自己留下一道光。'
action: '複製決策對話貼入 AI Prompt 生成 DR 草案，重點校對「Why」欄位並補上「重新檢視條件」，建立 decisions/ 資料夾歸檔。'
source_has_timestamps: false
---

你好！我是你的影片深度萃取器。這篇文章深刻地揭示了團隊協作中常見的「記憶腐蝕」問題：我們往往記得了「做了什麼」，卻忘了「為什麼這樣做」。

透過 **Decision Record (決策記錄)**，我們能將 AI 從「代筆者」轉化為「脈絡守護者」。以下為你整理的精華內容：

## 核心摘要
本文探討了在軟體開發與團隊協作中，決策脈絡（Context）消失所帶來的巨大隱造成本。作者提出透過 **Decision Record (DR)** 機制，並利用 AI 快速從對話記錄中提煉決策理由與限制。核心價值在於：**不再讓 AI 替我們做決定，而是讓 AI 幫我們捕捉決定背後的「為什麼」**，從而避免未來的無效重複討論。

---

## 詳細重點整理
### 1. 決策脈絡的「腐敗」與代價
* **理由消失現象**：程式碼會留下來，但當時導致該決策的「限制」與「理由」會隨時間蒸發，導致後人需花費大量精力進行「逆向推敲」。
* **商業成本**：團隊會陷入「重複論證」的迴圈，成員對決策的信任感降低，感覺進度越開越倒退。
* **關鍵概念**：**「決策是時間點的產物」**，讓決策合理的理由是有保鮮期的。

### 2. Decision Record (DR) 的五大支柱
* **決策內容 (What)**：用一句話清晰陳述結論（例如：選擇 JWT 而非 Session）。
* **理由 (Why)**：記錄導向結論的具體限制（例如：為了水平擴展而採無狀態設計）。
* **被否決的方案 (Alternatives)**：記錄當時考慮過但放棄的選項，這能有效回答新成員「為什麼不用 X」的疑問。
* **重新檢視的條件 (Revisit conditions)**：定義該決策在什麼情況下會失效（例如：用戶數突破百萬、某依賴庫停更）。
* **負責人與日期**：建立責任歸屬。
* **關鍵概念**：**「Revisit conditions」** 是讓系統具備自省能力的關鍵，它承認沒有任何決策是永久正確的。

### 3. AI 在決策捕捉中的角色
* **效率瓶頸**：文件化的最大阻礙是「時間」。
* **AI 工作流**：不需要從零開始撰寫，而是將 Slack 討論、會議逐字稿或語音備忘錄丟給 AI（如 Claude），由其產出第一版草案。
* **人機協作**：人類只需花 5 分鐘進行校對，特別是填寫 AI 無法推論的「重新檢視條件」。
* **關鍵概念**：**「5 分鐘原則」**，將原本 30 分鐘的文件工作縮短至 5 分鐘，大幅提升團隊維持習慣的意願。

---

## 結論與行動建議
* **啟發金句**：**『程式碼會留下，但脈絡會蒸發；我們捕捉決策，是為了給未來的自己留下一道光。』**
* **具體行動建議：DR-5 捕捉法則**
    1.  **收集**：當團隊在 Slack 或會議達成共識後，立即複製該段對話。
    2.  **生成**：貼入文章提供的 AI Prompt，產出 5 個欄位的 DR 草案。
    3.  **校對**：重點檢查「Why」是否準確，並補上「重新檢視條件」。
    4.  **發布**：將結果貼回團隊文件中或 Slack 頻道。
    5.  **歸檔**：建立一個專屬的 `decisions/` 資料夾記錄所有 DR。
* **生活實踐建議**：
    * **建立個人決策日誌**：不只是工作，生活中重大的決策（如買房、換工作、購買高價產品）也可以套用這 5 個欄位，避免幾年後後悔卻想不起當時的考量。
    * **工具建議**：使用 Notion 或 GitHub 建立 Decision Log，並利用 AI 插件快速摘要日常對話。


---

# 我們不再讓 AI 做決策，而是讓它來捕捉決策

這是「我們實際如何構建」系列的第三篇文章。在這個系列中，Skip 和我將 CRAFT 方法論一層一層地展開，並同步應用在實際的客戶團隊上。

**Chuck Griess**
4 月 22 日

---

上週，我和某個客戶團隊進行架構審查。有人對他們用於儲存工作階段狀態（session state）的資料儲存模式提出了疑問：隨著系統規模擴大，這個模式的取捨開始浮現問題。這是一個合理該被提出的問題。

接下來的對話，是我在幾乎每個專案中都經歷過的某種版本。

> 感謝閱讀！免費訂閱以接收新文章並支持我們的工作。
>
> 已訂閱

「為什麼我們要這樣做？」「我想這是早期的決定。」「你知道當時的理由嗎？」「不太清楚。」「是誰做的決定？」「我想是 James 做的，但他已經不在這個專案了。」

就此打住。**理由消失了。當初讓這個決定顯得合理的各項限制也消失了。**留下的只是一段程式碼，執行著某件事，但沒有人真正明白為什麼。於是一個本該在除錯擴展問題的團隊，反而在逆向推敲一個八個月前、在沒有人記錄下來的對話中所做的決定。

**這就是在第一週看不見、在第八個月才無所遁形的代價。**

## 當決策未被記錄時，消失的是什麼

上個月，Skip 和我在 Series 1 寫了一篇名為〈Field Notes: How We Stopped Re-Litigating Every Decision〉的文章，指出了這種情況的商業成本：花費在重新推導已經得出過的結論上的精力、當成員覺得沒有任何事情是「真正定案」時所侵蝕的信任，以及那些感覺越開越倒退的進度會議。

**Decision Record（決策記錄）就是我們打造出來用以關閉這個迴圈的機制。**

CRAFT 憲法的第二條法則是：**決策必須明確。** 不是「我們談過了，大家點頭了」。不是「我想我們達成共識了」。而是寫下來，附上理由。這條法則之所以存在，是因為我們在客戶合作案中一再看到同樣的失敗模式：決策用口頭做出、沒人記錄為什麼、掌握來龍去脈的人離職或忙碌起來，六個月後一位新成員提出的問題，原本只要兩段文字就能立即回答。

問題不在於團隊做了不好的決定。大多數團隊在既有限制下，都做出了相當不錯的決定。

**問題在於，決策是一個時間點上的產物，而讓這個決策合理的理由是會腐敗的。程式碼會留下，但脈絡會蒸發。**

## Decision Record 是什麼

DR 是一份簡短、結構化的文件，包含五個欄位。當決策還新鮮時，你可以在十分鐘內填完；或者使用 Claude 從會議逐字稿中重建一份，大約也是這個時間。目的不是追求完整性，而是捕捉六個月後有人提出相關問題時，**真正會重要**的那些東西。

**做出了什麼決定。** 一句話。不是「我們討論了身份驗證的選項」，而是「我們選擇 JWT 而非 session cookies 來處理 API 身份驗證」。決策本身，清楚地陳述。如果你無法用一句話清楚表達，那或許決策根本還沒真正做出來。

**為什麼。** 導致這個結論的理由。這是最難填的欄位，也是最有價值的欄位。「感覺對」不算是一個條目。「JWT 避免了伺服器端的 session 儲存，這很重要，因為我們執行的是無狀態容器，需要水平擴展」才是一個條目。理由是讓決策在未來仍可被解讀的關鍵。少了它，你擁有的只是一份結論清單，沒有任何方式去評估這些決策現在是否仍然成立。

**考慮過但被否決的方案。** 當時檯面上的其他選項，以及每一個為何沒有勝出。**這是大多數團隊會略過的欄位，卻也是回答最多問題的欄位**：新成員問的「為什麼不用 X？」、利害關係人建議的一個你早已評估過的方向、除錯時突然看起來誘人的另一種做法。

如果你沒有記錄下被否決的方案，你就會再次評估同樣的選項，而且可能不只一次。

**什麼條件會讓我們重新檢視這個決策。** 讓這個決策變成錯誤的特定條件。某項限制改變。某個依賴消失。某個規模門檻被跨越。少了這個欄位，你擁有的是一份結論清單；有了這個欄位，你擁有的是一個能告訴你「它過期了」的系統。這是團隊最不願意填的欄位，因為它要求承認沒有任何決策是永久的。**而那種不自在，正是重點所在。**

**負責人與日期。** 一個做出或核定此決策的人。一個日期。就這樣。

## AI 在其中扮演什麼角色

我最常聽到對任何形式文件的反對意見就是：時間。團隊的步調很快，把東西寫下來感覺像是額外負擔。這個反對是合理的，也是我們在設計時特別考量的重點。

Decision Record 的工作流程，不需要在做完決策後封鎖三十分鐘從零開始寫 DR。它只需要有人把相關材料貼給 Claude。Slack 討論串、會議逐字稿（Fireflies 會自動幫我們記錄大多數會議）、一段快速的語音備忘錄、或是當理由還清晰時隨手寫下的三句話脈絡。

以下是我們使用的 prompt：

> You are helping a software team document a technical or product decision using a Decision Record. A Decision Record captures: what was decided, why, what alternatives were considered and rejected, and what conditions would cause this decision to be revisited.
>
> Based on the following notes, generate a first-draft Decision Record using these five fields:
>
> 1. What was decided (one sentence)
>
> 2. Why (the reasoning, not just the conclusion)
>
> 3. Alternatives considered and rejected (what was on the table and why it didn't win)
>
> 4. Revisit conditions (what would make this decision wrong — be specific)
>
> 5. Owner and date
>
> For any field you can't fill in confidently from the notes, write "Needs resolution" and explain what's missing. The "Revisit conditions" field almost always requires the human to fill in — flag it clearly.
>
> [Paste Slack thread, meeting notes, transcript excerpt, or conversation summary here]

做決策的人檢視這份草稿，修正理由中不對的地方，並填入重新檢視的條件。**那是 Claude 無法從會議逐字稿推論出來的部分：會讓決策變成錯誤的特定條件。這部分需要當時在場的那個人來填。**

有了原始材料之後，總耗時：5 分鐘，而不是 30 分鐘。

## 三個月下來，我們觀察到什麼

關於我在這裡的主張，我想謹慎一些。三個月是個短樣本。我能說的是，在執行 Decision Records 的各團隊之間，某些模式是一致的。

**「為什麼不用 X？」這個問題有了去處。** 在擁有 DR 日誌的團隊中，「為什麼我們不改做 X？」這個問題，要嘛能被 DR 回答，要嘛揭示出 X 從未被正式考慮過。兩種結果都有用。前者省下了一次對話，後者浮現出一個缺口。

**除錯的脈絡以特定方式改善。** 好處不是 DR 告訴你哪裡出錯，而是它告訴你**這段程式碼當初是被設計來做什麼、在什麼限制之下**。「這段程式碼正按照當初設計的方式運作，但讓這種設計合理的那個限制已經改變了」——這是一個與「這段程式碼在做某件事，但我們不知道為什麼」截然不同的除錯起點。

**新人上手多了一種新的文件類別。** 一位能存取系統 DR 日誌的新工程師，不需要等資深人員有空，就能自行回答許多「為什麼是這樣構建的？」的問題。組織的知識存在於文件中，而不是某個人的腦袋裡。

**我目前還無法回答的問題是：** 在沒有明確流程支撐的情況下，團隊是否能在第一個月之後仍維持這個習慣。DR 只有在真的被寫下來時才有效。我們還在摸索適當的執行機制是什麼，我也不打算假裝我們已經有了完整的答案。

下週，Skip 和我會深入探討 **Context Graph（脈絡圖）**：凌駕於 CRAFT 其他所有環節之上的文件。大多數團隊是在毫無前置脈絡下向 AI 下 prompt。我們則為每個專案維護一層結構化的脈絡層，並在任何正式工作開始前將其餵給 Claude。這對輸出品質的差異並不微妙。

如果這篇文章引起你的共鳴，歡迎訂閱。我們書寫的是軟體交付中實際正在發生的變化，不炒作、不打太極，只談我們在實際專案中看到的狀況。

> 已訂閱

---

## 附錄：Decision Record 範本 + Claude Prompt

### Decision Record 範本

**專案／功能：** [名稱或簡短識別]

**決策：** [用一句話陳述做出的決定。不是「我們討論了 X」，而是實際的結論。]

**日期：** [日期]

**負責人：** [一位做出或核定此決策的人]

**為什麼：**

[導致此結論的理由。在這個時間點上讓此決策成為正確選擇的特定因素、限制或觀察。「感覺對」不算條目。]

**考慮過但被否決的方案：**

- [方案 1]：[為何沒有勝出]
- [方案 2]：[為何沒有勝出]
- [依需要新增]

**重新檢視的條件：**

[此決策會變成錯誤的特定條件。某項會改變的限制、某個規模門檻、某個會消失的依賴、某個會變動的商業假設。要具體。如果你無法說出重新檢視的條件，可能代表你並不完全理解為什麼要做這個決策。]

**脈絡：**

[任何有助於理解此決策、但不屬於上述欄位的內容：當時所受的限制、時程壓力、此決策解決的問題、當時程式庫的狀態。選填，但對高風險決策很有用。]

### Claude Prompt：從現有筆記產生 Decision Record

```
You are helping a software team document a technical or product decision using a Decision Record. A Decision Record captures: what was decided, why, what alternatives were considered and rejected, and what conditions would cause this decision to be revisited.

Based on the following notes, generate a first-draft Decision Record using these five fields:

1. What was decided (one sentence)

2. Why (the reasoning that led to this conclusion, not just the conclusion itself)

3. Alternatives considered and rejected (what was on the table and why it didn't win)

4. Revisit conditions (the specific conditions under which this decision would be wrong)

5. Owner and date

For any field you can't fill in confidently from the notes, write "Needs resolution" and briefly explain what's missing. The "Revisit conditions" field almost always requires the human to fill in directly — flag it clearly and leave it for review.

[Paste Slack thread, meeting notes, Fireflies transcript excerpt, or conversation summary here]
```