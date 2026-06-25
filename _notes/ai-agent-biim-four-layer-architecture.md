---
title: '企業級 AI Agent 的四層架構：BIIM 法則'
date: 2026-06-25
image: /images/AI筆記/ai-agent-biim-four-layer-architecture.jpg
category: AI筆記
tags: [四層Agent架構, 任務導向模型選型, DNA指令工程, 記憶治理策略, 多模型交叉驗證]
description: '影片提出企業級 AI Agent 的四層架構：大腦（LLM 選型）— 整合（工具與 API）— 指令（DNA 級別的系統提示）— 記憶（RAG 與長短期知識）'
quote: '不要把 Agent 當聊天機器人，而要當一個帶大腦、手腳、DNA 和記憶的自動化同事來設計。'
action: '採用 B-I-I-M 法則，從 Brain → Integrations → Instructions → Memory 依序設計每個 Agent'
source_has_timestamps: true
---
[核心摘要]

影片提出企業級 AI Agent 的四層架構：**大腦（LLM 選型）— 整合（工具與 API）— 指令（DNA 級別的系統提示）— 記憶（RAG 與長短期知識）**，對應從模型選擇、系統設計到運維治理的完整思考路徑。 解決的痛點是：多數組織只會「用 Copilot 聊天」，卻不會把 Agent 變成可以在背景持續可靠執行業務流程的自動化系統。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

[詳細重點整理]

1. 從 Copilot 到「睡覺也在跑」的 Agent [00:00]

- 核心觀念是把 Agent 當作一個「會自動運作的系統」，而不是單一對話助手，要能在你睡覺時持續讀取資料、觸發流程、產出結果。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 打好基礎需要先有穩定的資料庫與儲存庫（repositories），再在其上讓 Agent 主動「採取行動」而不只是回答問題。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**持續運作型 Agent**

2. 四層架構總覽：Brain / Integrations / Instructions / Memory [00:22]

- Agent 被拆成四層：**Brain（LLM 大腦）、Integrations（整合的工具與系統）、Instructions（行為 DNA）、Memory（可檢索的知識與上下文）**。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 設計時應從大腦開始，向外擴到工具、規則與知識，確保每一層都與目標任務對齊，而不是先亂接一堆 API 再來補救。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**四層 Agent 架構**

3. Brain：為任務挑對 LLM，而不是一味用最大模型 [00:27]

- 適合作為大腦的模型包含 ChatGPT、Claude、Gemini 以及像 Llama 這類開源模型，必須根據雲端/本地與任務性質做取捨。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 比喻是「不要用大鐵鎚釘圖釘」：許多人在自動化中濫用超大模型，結果反而變慢且成本高，對於高頻、重複性流程反而應選擇經過任務蒸餾的小模型。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**任務導向模型選型**

4. 小模型在自動化中的優勢 [00:54]

- 針對固定流程，作者實際使用「非常小的模型」讀文件與處理 Email 請求，因為需求是「快而穩」，而不是「極度聰明」。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 自動化場景中，過度聰明反而危險，明確邊界與可預測輸出才是關鍵，因此要刻意降低模型自由度與推理複雜度。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**窄域小模型自動化**

5. Integrations：手腳層—把 Agent 接到真實系統 [01:01]

- 整合層就是 Agent 的「手和腳」，將它連到 Email、CRM、Slack、後端資料庫或 HR 系統等，讓它不只是說話，而是能操作業務系統。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 這一步應在定義階段就處理，因為許多關鍵資料根本沒有 API 或無法觸發事件，如果不先檢查，架構會是「紙上談兵」。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**行動與整合邊界**

6. 提前確認資料與觸發點可行性 [01:17]

- 對 HR、財務等系統，要先問清楚：是否有 API？是否能由外部觸發？否則 Agent 無法真正落地自動化，而只能停留在「回答問題」層級。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 建議在設計階段就列出所有「需要互動的系統」及其可用的觸發與授權機制，避免後期整合卡關。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**可接入性審查**

7. Instructions：DNA 層—用精準 Prompt 設計 Agent 行為 [02:20]

- 指令層被稱為 Agent 的「DNA」，包括系統提示、行為規則、流程步驟等，是驅動 Agent 以特定風格與邏輯運作的核心。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 可以先用 LLM 來幫忙寫 Prompt：「我要建立一個 Agent 做 X，請幫我設計指令」，再針對實際場景調教，強調緊密邊界與明確框架可顯著降低疏失與調整成本。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念： **DNA 級別指令工程**

8. 指令設計原則：窄邊界、高可預測 [02:54]

- 越「緊」的指令與框架，輸出越穩定，可大幅減少迭代時的挫折與不可預測行為，對企業安全尤為重要。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 實務上可將任務拆成步驟式規則、輸入輸出格式、禁止行為與錯誤處理策略，全部寫進系統提示裡，形成可維運的行為準則。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**高約束指令設計**

9. Memory：RAG 與長短期記憶的區分 [03:03]

- 記憶層即典型的檢索增強生成（RAG）設計：準備好品牌策略、文件、SOP 等作為 Agent 的知識來源，像訓練一位實習生一樣給它「該知道的資料」。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 記憶分為載入時預設記憶（長期）與運行中對話記憶（短期），系統可以選擇是否保留互動中學到的內容，依照用例決定是否「持續學習」。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**長短期記憶分層**

10. 為什麼新請求不一定要進記憶 [03:22]

- 作者實作中的 Agent，在載入時就設定好記憶，新請求預設不回寫記憶，以防使用者亂輸入資料污染企業知識庫。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 若是需要長期演進的專家型 Agent，則可以設計短期記憶與長期知識庫的「升級門檻」，由人或守門流程決定哪些新知識可以被永久記住。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**記憶污染防護**

11. 需明確定義要記什麼、忘什麼 [04:09]

- 企業要清楚界定：哪些是必須集體永久記憶的（公司用例、SOP、關鍵決策），哪些只是對話上下文，不應長期保留。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 這實際上是知識治理問題：記太多會亂、記太少又無法複利，需結合合規與安全政策來設計記憶策略。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**記憶治理策略**

12. 安全與正確性：關鍵問題與防護欄 [04:20]

- 必須識別哪些問題 Agent 一定要以特定方式回答，以及哪些輸出是「絕對不能觸碰」的紅線，進而在指令與檢查層設置防護欄。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 一種做法是用多模型交叉驗證：在 LLM 啟動時跑一串驗證腳本，確認其回答關鍵問題時仍符合預期標準，才能投入正式流量。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**多模型交叉驗證**

13. 啟動流程中的自我驗證 Script [04:59]

- 作者會在每次啟動 LLM 時，透過自動化 Script 檢查其在一組預定測試題上的回答，以確保行為未因模型更新或設定變更而偏移。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 這種「啟動即測試」機制，是將傳統軟體 CI/CD 概念帶入 LLM/Agent 運維的實作案例，用於提升結果可預測性。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

關鍵概念：**啟動時品質檢查**

[技術/數據對比]

影片沒有提供具體數字或 Benchmark，而是概念性的對比，主要對比方向如下：

- 大模型 vs 小模型：大模型更通用但延遲高、成本高，小模型經任務蒸餾後更適合高頻、固定流程的自動化。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)
- 靜態記憶 vs 動態學習：靜態記憶避免污染，動態學習可隨時間成長，但需配合治理與審核機制。 [youtube](https://www.youtube.com/watch?v=R6xVJQeBhX4)

[結論與行動建議]

- 啟發金句：  
  **「不要把 Agent 當聊天機器人，而要當一個帶大腦、手腳、DNA 和記憶的自動化同事來設計。」**（綜合影片內容整理）

- 具體行動建議（適合你作為 AI 應用架構師/Product Manager）  
  建議採用一條簡單法則：**B-I-I-M 法則（Brain–Integrations–Instructions–Memory）**  
  - Brain：先以用例決定模型等級與部署方式（雲端/本地、小模型/大模型）。  
  - Integrations：在寫任何 Prompt 前，先盤點所有要接的系統與 API 可接入性。  
  - Instructions：將業務流程寫成可維護的系統提示模板，視為產品規格的一部分。  
  - Memory：為每個 Agent 定義長短期記憶策略與升級/清除規則，並在 DevOps 流程中加入記憶檢查。  

- 生活/工作實踐建議（企業落地版本）  
  - 從一個「讀信→分流→回覆草稿」的窄域 Agent 開始，刻意選用小模型，並限制其可執行操作，實際驗證四層架構。  
  - 建立一份「Agent 啟動檢查清單」，包含：指令版本、測試問題集、關鍵禁區檢查，讓每次部署 Agent 都像部署後端服務一樣可控。  
  - 在團隊中把「記什麼、忘什麼」當成正式議題，與法務/資訊安全共同制定 Agent 記憶策略與數據保留政策。  

[參考連結]

- 原始影片：<https://youtu.be/4wMRXmLpdA8?si=JQrxsVfwZJmdMTM->  
