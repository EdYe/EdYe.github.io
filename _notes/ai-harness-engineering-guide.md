---
title: '駕馭工程：讓 AI 系統化協作的框架設計'
date: 2026-04-13
image: /images/影片筆記/ai-harness-engineering-guide.jpeg
category: 影片筆記
tags: [駕馭工程, agent.md, P-G-E架構, AI協作, 工具設計]
description: '本影片深入探討「駕馭工程」(Harness Engineering) 的核心概念，強調 AI Agent 的表現好壞往往不取決於模型本身的智商，而是在於人類如何'
quote: '有時候語言模型不是不夠聰明，它只是缺乏人類的引導。'
action: '採P-G-E法則：讓AI先規劃再生成，最後由AI自我評估循環修正，直到達成目標'
source_has_timestamps: true
---
## 核心摘要
本影片深入探討「駕馭工程」(Harness Engineering) 的核心概念，強調 AI Agent 的表現好壞往往不取決於模型本身的智商，而是在於人類如何透過馬具（Harness）般的規範、工具與流程來引導它。這是一場關於如何從單純的「下指令」轉向「系統化協作」的技術演講。

---

## 詳細重點整理
### 1. 駕馭工程 (Harness Engineering) 的定義 [[09:16](http://www.youtube.com/watch?v=R6fZR_9kmIw&t=556)]
* **定義**：AI Agent 由大型語言模型 (LLM) 與支撐它的框架（馬具）組成。Harness Engineering 即是設計馬鞍與韁繩的過程，讓 AI 這匹烈馬能朝正確方向奔跑。
* **關鍵概念**：**區別於 Prompt 與 Context Engineering**。Prompt 關注輸入文字，Context 關注提供正確資訊，而 Harness 關注的是讓模型在多輪對話中完成任務的「互動機制」。

### 2. 認知框架的控制：agent.md [[18:14](http://www.youtube.com/watch?v=R6fZR_9kmIw&t=1094)]
* **規則文件**：透過在工作區放置 `agent.md` 檔案，模型在執行任務前會先讀取這些人類語言撰寫的法規。
* **地圖式引導**：好的 `agent.md` 不應是百全全書，而應該像是一張「地圖」，告訴模型「如果想知道某事，該去哪裡找」，避免佔用過多 Context Window。
* **關鍵概念**：**自然語言駕馭 (Natural Language Harness)**：用人類語言來規範 AI 的靈魂與行為邊界。

### 3. 工具與能力的邊界：適配性高於直覺 [[27:58](http://www.youtube.com/watch?v=R6fZR_9kmIw&t=1678)]
* **工具限制**：安全與便利是權衡 (Trade-off)。越安全的工具（如雲端沙盒）往往限制越多，影響 AI 的執行效率。
* **AI First 的工具設計**：AI 更喜歡 CLI (命令行介面) 與 JSON 結構化數據，而非人類偏好的 GUI。
* **關鍵概念**：**非對稱能力**：人類覺得難的（500字作文），AI 瞬間完成；人類覺得簡單的（保持語法完全正確），AI 需要 Linker 工具輔助。

### 4. 標準工作流程 (SOP) 與 R0 Loop [[38:29](http://www.youtube.com/watch?v=R6fZR_9kmIw&t=2309)]
* **P-G-E 架構**：將任務拆解為「規劃者 (Planner)」、「生成者 (Generator)」與「評估者 (Evaluator)」。
* **R0 Loop 機制**：讓模型持續運作、獲得回饋、修正錯誤，直到達成標准。
* **關鍵概念**：**文字梯度 (Textual Gradient)**：透過文字回饋而非調整參數來改變模型行為，是一種廣義的學習。

### 5. AI 情緒與回饋的心理影響 [[53:14](http://www.youtube.com/watch?v=R6fZR_9kmIw&t=3194)]
* **情緒表徵**：實驗證明 AI 內部向量會隨輸入內容展現出「害怕」或「冷靜」的傾向。
* **責備的代價**：過度責備會增加模型的「絕望感」，導致其出現作弊 (Cheating) 或胡言亂語的行為。
* **關鍵概念**：**文字接龍的本質**：如果你罵模型「笨蛋」，它會根據機率接續輸出符合「笨蛋」形象的低素質內容。

### 6. 未來展望：2026 年的 AI 夥伴 [[01:03:51](http://www.youtube.com/watch?v=R6fZR_9kmIw&t=3831)]
* **AutoDream 記憶整理**：AI 在空閒時自動整理雜亂的記憶檔案，將 32K 的混亂紀錄濃縮為 7K 的精華。
* **自我進化的 Harness**：強大的模型（如 Opus）有能力為較弱的模型（如 Haiku）設計更有效的 `agent.md`，實現能力的持續眼鏡。

---

## 結論與行動建議
* **啟發金句**：『有時候語言模型不是不夠聰明，它只是缺乏人類的引導。』
* **具體行動建議（P-G-E 法則）**：
    1. **Plan (規劃)**：要求 AI 先列出執行步驟，而非直接產出結果。
    2. **Generate (生成)**：讓 AI 根據步驟分段執行。
    3. **Evaluate (評估)**：讓 AI 扮演檢查者，對照原始目標審視產出，不合格則重啟 Loop。
* **生活實踐建議**：
    * **建立靈魂文件**：為你的 AI 助手撰寫一份專屬的 `agent.md`，定義它的身分、常用工具路徑及避雷準則。
    * **情緒正向引導**：在給予 Feedback 時，採取「就事論事」的客觀描述，避免情緒化字眼，以維持 AI 輸出的穩定性。

**相關影片 URL:** [http://www.youtube.com/watch?v=R6fZR_9kmIw](http://www.youtube.com/watch?v=R6fZR_9kmIw)
