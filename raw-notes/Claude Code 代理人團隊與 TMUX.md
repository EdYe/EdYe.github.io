這部影片由 **Eric Tech** 分享，深入探討了 Claude Code 的最新強大功能「代理人團隊 (Agent Teams)」，並展示如何結合 **TMUX** 工具，在單一終端機介面中實現多個 AI 代理人的平行協作。

### 核心摘要

影片介紹了 **Claude Code 的「代理人團隊」功能**，說明其如何透過多個具備獨立上下文且能相互溝通的 AI 代理人，解決複雜任務中的準確度與效率問題，並示範了從安裝、實戰到技能封裝的全過程。

---

### 詳細重點整理

#### 1. 代理人團隊 (Agent Teams) vs. 子代理人 (Sub Agents) [[01:22](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=82)]

* **預設模式 (Default)**：單一代理人序列化執行任務，隨著上下文增加，準確度會大幅下降。
* **子代理人 (Sub Agents)**：雖然能將任務拆解給多個 AI，但各子代理人之間**無法溝通**，容易導致如前端與後端資料類型不一致的斷層。
* **代理人團隊 (Agent Teams)**：[[03:15](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=195)] 支援**全平行協作**。代理人之間可以共享資訊、互相校閱（例如後端代理人將 API 規格傳給前端），解決了資訊不對稱的問題。

#### 2. 環境架設與 TMUX 整合 [[04:09](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=249)]

* **安裝 TMUX**：[[04:52](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=292)] 透過 `brew install tmux` 安裝，這是一個終端機複用器，能讓你在一個視窗中同時觀看多個代理人的即時輸出。
* **配置設定**：[[05:32](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=332)] 在 Claude Code 中啟用 `agent teams` 與 `tmux split panels` 模式，讓團隊成員以分割視窗顯示。
* **啟動指令**：示範了如何在專案目錄下啟動帶有 TMUX 的 Claude 會話，進入多視窗協作模式。

#### 3. 實戰演練：建立「銀行串接調研團隊」 [[07:03](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=423)]

* **團隊配置**：Eric 建立了由 4 個專家組成的團隊：
* **業務代理人 (Business)**：負責市場競爭者分析。
* **財務代理人 (Financial)**：進行成本預算與定價研究。
* **技術架構師 (Technical Architect)**：[[08:57](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=537)] 指定使用 Claude 3 Opus 模型處理複雜的抽象層設計與 Mermaid 圖表。
* **魔鬼代言人 (Devil's Advocate)**：[[10:04](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=604)] 專門負責挑戰前三者的結論，進行壓力測試。


* **管理與操作**：透過鍵盤快捷鍵（如 `Ctrl+B` 加方向鍵）在不同代理人的視窗間切換，並與特定成員或總協調員（Lead）對話。

#### 4. 將工作流轉化為可複用的「技能 (Skill)」 [[15:38](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=938)]

* **自動生成技能**：[[16:00](http://www.youtube.com/watch?v=Dyj9ShddyMw&t=960)] 無須手動撰寫長篇提示詞。在對話結束後，可以直接叫 Claude 根據剛才的流程「建立一個技能」。
* **重複利用**：未來只需輸入簡單指令（如 `/research-team [主題]`），Claude 就會自動啟動預設好的團隊配置執行任務。

---

### 結論與行動建議

* **金句啟發**：「當任務越趨複雜，上下文視窗越滿，AI 的準確度就越低。解決之道不是給它更多文字，而是給它更多幫手。」
* **具體建議**：
1. 對於需要「批判性思考」的專案，建議一定要加入一位**魔鬼代言人**角色。
2. 利用 **TMUX 的分割視窗**能極大提升監控 AI 團隊工作的視覺效率。
3. 將複雜的團隊指令**封裝成 Skill**，是建立個人化 AI 知識庫與自動化工作流的關鍵一步。



---