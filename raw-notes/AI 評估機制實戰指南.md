這部影片由 Hamel Husain 深入淺出地講解了如何為真實世界的 AI 產品建立有效的「AI 評估（Evaluations / Evals）」機制，並分享了許多避免踩坑的實戰經驗。以下是為您整理的重點筆記：

### 🎯 核心摘要

**建立有效 AI 評估機制的第一步，不是盲目追求自動化分數，而是親自查看真實的使用者對話紀錄，並將問題分類，再針對具體痛點設計二元標準的 LLM 裁判。**

---

### 📝 詳細重點整理

#### 1. 評估的起點：親自查看與標註數據 (Look at the Traces)

* **不要一開始就依賴自動化工具**：許多團隊會直接套用現成的「幻覺分數」或「毒性分數」，但這些通用指標往往無法反映產品真正面臨的問題。
* **手動檢查 100 筆紀錄**：直接查看 AI 系統中的 "Traces"（包含使用者對話與系統背後呼叫工具的完整歷程）。在過程中，只要簡單寫下「哪裡出錯了」（例如：對話突然中斷、沒有正確轉接真人客服），不需要立刻解決問題 [[04:40](http://www.youtube.com/watch?v=uiza7wp1KrE&t=280)]。
* **利用 AI 輔助分類**：將手動紀錄的筆記匯出成試算表後，可以請 Claude 或 ChatGPT 幫忙進行「開放編碼 (Open Coding)」與「主軸編碼 (Axial Coding)」，快速將錯誤歸納出 5-6 個主要類別 [[09:44](http://www.youtube.com/watch?v=uiza7wp1KrE&t=584)]。

#### 2. 選擇合適的評估方式：程式碼驗證 vs. LLM 裁判

* **簡單問題用程式碼驗證**：如果 AI 只是把「今天的日期」弄錯，你只需要在提示詞 (Prompt) 中加入日期，或寫一個簡單的程式碼進行比對 (Code-based eval)，不需要動用昂貴的 LLM 裁判 [[19:21](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1161)]。
* **複雜且主觀的問題才使用 LLM 裁判**：例如「AI 是否在該轉接真人客服時成功轉接？」，這類涉及對話脈絡的情境，就很適合設計一個「LLM 作為裁判 (LLM as a Judge)」來自動評估 [[21:05](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1265)]。

#### 3. 設計 LLM 裁判的關鍵原則

* **絕對不要使用 1-5 分的連續評分**：LLM 非常不擅長給出精確的連續分數。平均分數「3.2 分」和「3.7 分」的差異讓人無法理解，也無法作為產品是否能上線的決策依據。評估標準應該要是明確的**「二元分類 (True/False 或 Pass/Fail)」** [[24:38](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1478)]。
* **要求輸出解釋與分數**：為了方便後續除錯，最好要求 LLM 裁判同時輸出「判斷理由」以及「二元分數」 [[26:25](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1585)]。

#### 4. 驗證你的裁判：如何知道 LLM 評估得準不準？

* **警惕「一致性 (Agreement)」陷阱**：不要單純計算 LLM 裁判與人類標註的「一致性」。如果某個錯誤只發生 10% 的時間，LLM 只要永遠盲猜「沒錯誤」，就能獲得 90% 的超高一致性，但這個裁判其實毫無用處 [[28:50](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1730)]。
* **使用 TPR 與 TNR**：應該改看「真陽性率 (True Positive Rate)」和「真陰性率 (True Negative Rate)」，以確認模型能確實抓出錯誤，且不會誤判 [[30:23](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1823)]。
* **觀察混淆矩陣 (Confusion Matrix)**：把人類標註和 LLM 裁判的結果並列比對，看看「偽陽性」和「偽陰性」發生在哪裡，再藉此去優化 LLM 裁判的提示詞 [[31:12](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1872)]。

---

### 💡 結論與行動建議

* **🏆 啟發金句**：
> *"If people don't trust your evals, they won't even trust you."* (如果團隊不信任你做出的 AI 評估指標，他們就永遠不會信任你這個人。) [[22:40](http://www.youtube.com/watch?v=uiza7wp1KrE&t=1360)]


* **👣 行動建議 (Step-by-step)**：
1. **開始看 Log**：無論產品規模多小，先手動閱讀 100 筆真實使用者的互動紀錄，直到達到「理論飽和 (Theoretical Saturation)」，也就是你覺得已經看不太到新種類的錯誤為止 [[42:26](http://www.youtube.com/watch?v=uiza7wp1KrE&t=2546)]。
2. **分類痛點**：將發現的錯誤分門別類，找出發生頻率最高、最影響體驗的痛點。
3. **打造內部工具**：利用 AI 幫團隊快速寫一個簡單的標註介面，讓人工審查對話紀錄的過程變得輕鬆且容易量化。
4. **建立並迭代 LLM 裁判**：針對最大的痛點設計二元制 (True/False) 的 LLM 裁判，並對照人類標註的結果來驗證裁判的準確度。



---