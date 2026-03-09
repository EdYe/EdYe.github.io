### 核心摘要

這部影片深入探討了為何「AI 評估 (Evals)」是現今打造優質 AI 產品最關鍵的技能，並透過實例展示如何透過錯誤分析與資料觀察，來系統化地提升 AI 應用的真實品質。

---

### 詳細重點整理

#### 1. 什麼是 AI 評估 (Evals)？為什麼它不可或缺？

* **超越單元測試**：Evals 是一種系統化衡量並改善 AI 應用程式的方法。它不僅僅是寫程式碼的單元測試，還涵蓋了更廣泛的數據分析與應用程式監控。 [[05:56](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=356)]
* **告別「憑感覺 (Vibe checks)」**：當 AI 應用出現錯誤（例如胡說八道或呼叫錯誤工具）時，不能只靠猜測或單純的「感覺」來盲目修改提示詞 (Prompt)。隨著應用規模擴大，單靠感覺會讓系統變得難以管理且容易出錯。 [[06:56](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=416)]
* **建立客觀指標**：Evals 幫助你建立衡量應用程式表現的指標，讓開發者具備明確的回饋訊號，能更有信心地進行迭代與實驗。 [[07:30](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=450)]

#### 2. 建立 Evals 的實戰教學 (Step-by-step)

* **步驟一：錯誤分析與開源編碼 (Open Coding)**
* 親自查看實際的使用者對話日誌 (Traces)。不要一開始就急著寫測試程式，而是記錄下你觀察到的第一個錯誤（例如：「不該提供虛擬導覽」）。 [[16:44](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=1004)]
* 這個步驟建議由具備領域知識的專案負責人（通常是產品經理）來執行。為了保持效率，不需透過委員會決議，可以直接指定一位你信任其品味的「仁慈的獨裁者 (Benevolent Dictator)」來主導。 [[25:18](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=1518)]


* **步驟二：利用 AI 進行主軸編碼 (Axial Coding)**
* 當你收集了約 100 筆手動筆記後，可以將資料匯出成 CSV，並交由 Claude 或 ChatGPT 等語言模型，將這些零散的筆記統整、歸類成幾個主要的「失敗模式 (Failure modes)」或標籤。 [[32:47](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=1967)] [[34:02](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=2042)]


* **步驟三：統計與優先排序**
* 將分類好的錯誤標籤透過樞紐分析表 (Pivot table) 進行盤點，計算各類錯誤發生的頻率。透過量化數據，你就能知道哪些問題是當務之急，進而對症下藥。 [[44:48](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=2688)]



#### 3. 利用大語言模型作為裁判 (LLM as a Judge)

* **對付主觀難題**：當你遇到無法單純用程式碼驗證的複雜且主觀的錯誤（例如：何時該轉接給真人客服）時，可以撰寫特定的提示詞，讓大語言模型擔任「裁判」。 [[47:35](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=2855)]
* **堅持二元判斷**：LLM 裁判的輸出必須是簡單的「二元制（對或錯 / True or False）」。千萬不要讓它給出 1 到 5 分的評分，因為模糊的分數難以作為決策依據，只會拖慢迭代速度。 [[52:24](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=3144)]
* **人類驗證與校準**：在正式上線前，務必將 LLM 裁判的判斷結果與你自己的判斷進行矩陣比對。如果兩者出現分歧，請持續調整裁判的提示詞，直到兩者對齊為止。絕不能盲目相信 LLM 的判斷即是真理。 [[56:28](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=3388)]

#### 4. 常見迷思與業界爭議

* **迷思一：買個工具就能全自動評估**。許多人以為買了一套軟體，AI 就能自己評估自己。但這行不通，人類的商業知識與對資料的觀察依然無可取代。 [[01:24:33](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=5073)]
* **迷思二：不看數據直接寫測試**。開發人員往往無法預先想出所有的失敗情境，你的評估標準絕對會隨著你看到真實數據後發生改變。因此，親自審視資料是投資報酬率最高的工作。 [[01:25:03](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=5103)]
* **關於「只靠感覺 (Vibes)」的爭議**：近期有些團隊（如 Claude Code）聲稱他們不寫 Eval，只依賴感覺。這是因為寫程式輔助工具的開發者本身就是重度使用者 (Dogfooding)，這種高頻率的自我測試與回饋循環，本質上就是一種廣義的 Eval，但這並不能套用在醫療或客服等無法輕易「自己試用」的產業上。 [[01:13:03](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=4383)]

---

### 結論與行動建議

* **💡 啟發性金句**：
> "The goal is not to do evals perfectly. It's to actionably improve your product." (做 Evals 的終極目標不是為了追求完美的評估分數，而是為了獲得能實際改善產品的行動方針。) [[01:26:52](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=5212)]


* **🎯 具體行動建議**：
* **不要害怕看數據**：只要建立好工作流程，後續每週可能只需花費 30 分鐘看一下實際的對話紀錄，就能為 AI 產品帶來驚人的進步。 [[01:31:43](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=5503)]
* **善用 AI 輔助，但保持人類在決策圈內**：你可以用 AI 幫你組織想法、分類錯誤，但最終的判斷與品質把關仍需依賴人類。 [[01:27:19](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=5239)]
* **聰明分配資源**：如果某個小錯誤可以透過修改基礎提示詞 (Prompt) 解決，就直接改掉，不需要為每一個小問題都建立一套複雜的 LLM 裁判評估。 [[01:06:02](http://www.youtube.com/watch?v=BsWxPI9UM4c&t=3962)]
