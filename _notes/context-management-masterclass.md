---
title: '上下文管理大師課：Agent為何變笨'
date: 2026-07-12
image: /images/AI筆記/context-management-masterclass.jpg
category: AI筆記
tags: [上下文管理, 四操作框架, 上下文隔離, 提示快取失效, Codex與Hermes對比]
description: 'Agent 在長任務中「變笨」的真正原因，通常不是模型本身退步，而是上下文窗口被雜訊淹沒。影片以真實 StreamIt 直播除錯案例貫穿全場，剖析上下文管理的核心職責。'
quote: '💡你的 Agent 沒有變笨，是它的窗口變髒了。模型沒有退化，退化的是你放進窗口的東西。'
action: '🎯遇到 Agent 表現退化時，依序檢查 Select、Compress、Write、Isolate 四操作，並先確認能否看到窗口中實際送達模型的內容。'
source_has_timestamps: true
---
# Context Management Masterclass — Technical Deep Dive

***

## [核心摘要]

Agent 在長任務中「變笨」的真正原因，通常不是模型本身退步，而是上下文窗口被雜訊淹沒。影片以一個真實的 StreamIt 直播串流除蟲案例貫穿全場，剖析**上下文管理**作為 Harness Engineering 第三原語的核心職責：決定每一回合究竟有哪些內容真正進入模型視野 。提出 **Select（篩選）、Compress（壓縮）、Write（寫入磁碟）、Isolate（隔離子代理）** 四大操作，並對比 Codex 與 Hermes 兩套 Harness 在每一環節的相反設計賭注 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

***

## [詳細重點整理]

### 1. StreamIt Bug：Agent 在第 40 回合「斷線」 [00:00]

StreamIt 是一個將手機 WebRTC 影像透過 Node 伺服器以 FFmpeg 重新編碼後推送到 YouTube 的直播應用。在處理「行動網路下影片卡頓、解析度下降、音訊雜訊」的 Bug 時，Agent 前半段表現良好，但約在第 40 回合開始出現異常行為：重複打開已編輯過的檔案、提出先前已排除的修復方案、甚至推翻先前共同做出的決策 。關鍵洞察是：**模型本身沒有退化**——同樣的權重、同樣的設定，改變的只是「模型眼前看到的內容」。窗口被日誌、半讀檔案和工具輸出塞滿，真正重要的資訊被擠出注意力範圍 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：上下文管理失敗（Context Management Failure）**

***

### 2. 長上下文退化的四種模式 [02:34]

Drew Breunig 提出長上下文退化的四種模式，每一種的修復方式不同 ： [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

- **Poisoning（污染）**：錯誤的事實或不良的工具結果進入上下文後，持續被當作真實資訊引用
- **Distraction（分心）**：上下文過長，模型過度依賴窗口內容而非訓練知識
- **Confusion（混淆）**：多餘材料進入上下文，導致模型產出更差的答案
- **Clash（衝突）**：上下文累積了互相矛盾的事實或工具結果，內部衝突降低推理品質

在 StreamIt 案例中同時發生了 Distraction（Docker 日誌數千行吃掉大部分窗口）和 Clash（設計文件描述管線已將每幀正規化為 1080p，但部署中的程式碼尚未實作，Agent 選擇信任文件而非現實）。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：四種上下文退化模式（P-D-C-C）**

***

### 3. 上下文管理的定位與邊界 [04:14]

上下文管理是 Harness Engineering 十大原語中的第三個，位於 Context Delivery 之後、Tool Layer 之前 。其核心職責是決定「此刻這一回合，什麼內容進入模型的提示」。需要與兩個鄰近概念區分： [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

- **RAG**：決定「什麼知識可以被拉進來」
- **Memory**：決定「什麼在跨執行間留存」

用一個比喻理解三者差異：Delivery 是「書架上有哪些書可拿」；Memory 是「哪些書會永久放在架上」；Context Management 是「此刻桌上放哪幾本」。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：三層邊界（Delivery / Memory / Context Management）**

***

### 4. 天真方法與四個操作 [05:34]

最簡單的做法是「把所有看似相關的東西全塞進窗口」。短任務或許可行，但長任務中工具輸出逐回合堆積，模型花了注意力在讀歷史日誌而非回答當前行為 。影片引用 Lance Martin（LangChain）提出的四個操作框架：**Select（篩選）、Compress（壓縮）、Write（寫入）、Isolate（隔離）**，並依「在真實任務中出問題的順序」逐一拆解 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：四操作框架（Select-Compress-Write-Isolate）**

***

### 5. Move 1 — Select：拉取本回合所需的切片 [07:14]

篩選的精髓是「不要把所有東西丟進去，只拉取這一回合真正需要的切片」。對 StreamIt 而言，當工作涉及編碼器重啟問題時，應帶入編碼器程式碼與最近的伺服器日誌，而非分數疊加渲染或 YouTube 認證流程 。篩選本身必須低成本且近似（如 embedding 檢索、按相關性排序、描述索引），因為 Agent 不可能讀完整個 repo 來判斷相關性。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

工具選擇是篩選失效的典型場景：研究顯示當工具數量達到數十個時開始出問題，約一百個時出現真正失敗。成熟 Harness 會先檢索相關工具，而非每次都註冊全部工具 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**跨時間篩選的兩種策略對比：**
- **Codex / Claude Code**：隔離每個 Session，無法直接載入其他 Session 的對話，只透過 AGENTS.md 做專案層級的篩選
- **Hermes（Nous Research）**：將所有 Session 存入 SQLite（含 FTS5 全文檢索），讓模型可以搜尋並拉取舊 Session 中相關的片段

**Lost in the Middle 效應：** 模型可靠使用上下文開頭和結尾的資訊，對中間部分不可靠。即使選對了檔案，若埋在巨大窗口的中間，模型也會略過 。因此篩選是兩個決策：**「放什麼進來」**和**「放在哪裡」**。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Lost in the Middle（中間遺失效應）**

***

### 6. Move 2 — Compress：好的壓縮保留什麼 [12:55]

壓縮的目標不是「變短」，而是「在不丟失下一回合所需資訊的前提下變短」。好的壓縮摘要應保留五類資訊： [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

1. 目標（Goal）
2. 已鎖定的約束與決策（Constraints & Decisions）
3. 進度與阻礙（Progress & Blockers）
4. 關鍵檔案與事實（Key Files & Facts）
5. 下一步（Next Step）

這就像是「休假前寫給同事的交接筆記」。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**Codex vs Hermes 在壓縮上的對比：**
- **Hermes**：在每回合前檢查是否接近壓縮閾值（預設窗口 50%，可推至 70-80%），觸發時重建整個 Prompt，但穩定部分（身份與工具指引）保持逐位元組一致以利快取 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)
- **Codex**：不做大規模壓縮事件，而是對每個進入項目施加硬限制（單項不超過 10k tokens、超過 1000 tokens 的項目標記人工審查、技能預算為窗口的 2%） [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**壓縮的兩個隱藏成本：**

1. **有損性（Lossy）**：激進壓縮可能將 Docker 日誌壓成「影片品質不穩」一句話，丟掉真正的關鍵證據（如解析度在 1280×720 與 904×508 之間震盪、編碼器重啟數百次） [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)
2. **壓縮本身就是一次 LLM 呼叫**：消耗時間與 Token，過度頻繁觸發會「花 Token 來省 Token」並打斷 Agent 動能 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：有損壓縮（Lossy Compaction）**

***

### 7. Move 3 — Write：將不可丟失的內容寫入磁碟 [19:14]

如果壓縮是有損的，那麼對於「絕對不能丟」的內容，解法是根本不放在對話中。寫入磁碟是第三個操作 。對 StreamIt 而言，Agent 將已確認的事實寫入一個工作筆記檔案（嫌疑是編碼器重啟風暴、日誌特徵、相關檔案、已排除的修復及原因），該檔案存在磁碟上，不佔窗口空間，壓縮時也不受影響 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**Dex Horthy（HumanLayer）的 Research → Plan → Implement 工作流：**
- **Research 階段**：Agent 探索並寫出相關檔案、行號、嫌疑程式碼到 research file
- **Plan 階段**：Agent 將計畫變更寫入 plan file，人類審核計畫而非直接看 diff
- **Implement 階段**：Agent 從 plan file 在全新窗口中執行，不拖著整個研究對話

Dex 報告此方式可將工作上下文控制在窗口的 40% 以下，並在幾乎不手動開啟檔案的情況下交付大量程式碼 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**邊界提醒：** 為當前任務寫的暫存筆記是上下文管理；若該筆記旨在跨 Session 留存並影響未來執行，則屬於 Memory（原語六）。同一個磁碟檔案，不同用途 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Research → Plan → Implement 工作流**

***

### 8. Move 4 — Isolate：用子代理隔離上下文 [21:14]

有時一個窗口是錯誤的工作單位，應將工作拆分到多個獨立上下文。隔離的精髓是「給子任務自己的上下文，讓它執行，只帶回結果」。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

StreamIt 案例中，搜尋巨大的 Docker 日誌正適合交給子代理：子代理在自己的上下文中讀完整日誌、消耗所需 Token，然後回報「226 次重啟，以下是解析度崩潰序列」——主窗口永遠不會看到那數千行日誌 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

隔離帶來的是**總容量**（五個窗口能裝的比一個多），代價是**協調成本**（一旦需要協調多個窗口，就進入 Orchestrator 領域）。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：上下文隔離（Context Isolation）**

***

### 9. 被忽略的 Prompt Cache 成本 [22:51]

現代模型會快取 Prompt 前綴：若前幾千個 Token 與上一回合逐位元組相同，則以折扣價處理（最高可省 90%）。但只要在前綴中改動一個位元組，其後所有 Token 都失效，需全價重算 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

這改變了四個操作的思維：每次重新篩選、重新排序或壓縮，都可能使快取失效。**每回合都重新洗牌窗口的 Harness 可以是正確的，但同時是慢的和昂貴的** 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**Codex vs Hermes 的快取策略：**
- **Hermes**：每個 Session 只建一次系統提示並跨回合重用，只有壓縮時才重建；將易變內容放在使用者訊息而非快取前綴中 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)
- **Codex**：在規則中明確寫道「增量建構上下文，不要重寫歷史，避免頻繁變更導致快取失效」 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

組裝順序是效能決策，不只是正確性決策。穩定內容（身份、指令、工具）放前面，易變內容放後面 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Prompt Cache Invalidation（提示快取失效）**

***

### 10. Codex vs Hermes 全方位對比 [25:45]

| 維度 | Codex（OpenAI CLI） | Hermes（Nous Research） |
|------|---------------------|------------------------|
| 篩選策略 | 專案層級（AGENTS.md），Session 隔離 | 跨 Session 搜尋（SQLite + FTS5） |
| 壓縮策略 | 進門時硬限制（每項 ≤10k tokens） | 窗口接近閾值時大規模重建（預設 50%） |
| 快取策略 | 增量建構，避免重寫歷史 | 每 Session 建一次提示，壓縮時才重建 |
| 設計賭注 | 門口紀律（Discipline at the door） | 彈性窗口帶回溯（Flexible window with reach-back） |
| 適用場景 | 單一 repo、單一 Session | 跨多 Session、需回溯歷史工作 |

兩者共享的模式：有界組裝、穩定快取前綴、漸進式揭露（先載入輕量描述，需要時才載入完整內容）。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

***

### 11. 可觀測性：你看不見窗口，就無法修復 [27:09]

當 Agent 出問題時，第一直覺常是改 Prompt 或換模型，但真正有幫助的是「看看上下文裡到底有什麼」。Codex 可追蹤 Token 預算並顯示窗口使用量。第一次查看時通常是驚喜：一半窗口是被遺忘的日誌、重複的註解、或 20 回合前不再相關的工具結果 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

建議的習慣：在思考優化或修復之前，**先看窗口**。可使用 LangFuse、LangSmith 或任何支援 OpenTelemetry 慣例的追蹤工具，擷取每次呼叫的完整 Prompt、訊息和工具清單 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

**關鍵概念：Context Observability（上下文可觀測性）**

***

### 12. 實戰工作流：Research → Plan → Implement [28:34]

將四個操作整合為一個工作流 ： [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

1. **Research 階段**：Agent 探索並將發現（相關檔案、嫌疑程式碼）寫入 research file → 這是提前使用 Write 操作
2. **Plan 階段**：Agent 將計畫變更寫入 plan file → 人類審核計畫而非直接看 diff，若 Agent 誤解編碼器行為，可在此以一則評論的成本捕獲，而非一天的代價
3. **Implement 階段**：Agent 從 plan file 在全新窗口中執行 → 不拖著整個研究對話，窗口保持乾淨

核心原理：窗口裡的垃圾越少，模型對任務的注意力越集中 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

***

### 13. 回到 StreamIt Bug：修復方案 [30:34]

回顧四個操作來診斷問題：當 Agent 變笨時，逐一檢查 Select、Compress、Write、Isolate 哪一環出錯，以及「我能否看到窗口中的內容」。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

StreamIt 的問題出在 **Select 和 Compress**：Docker 日誌佔據大部分上下文並淹沒了訊號，隨後草率的壓縮又將訊號完全刪除 。修復方案：**將日誌交給子代理處理（Isolate），讓子代理將發現寫入檔案（Write）**，這樣既不會塞滿主窗口，也不會被壓縮摘要刪除。窗口乾淨後，Agent 找到了真正問題——編碼器上游的解析度崩潰 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

***

### 14. 給所有人的建議：看見真正送達模型的內容 [33:42]

無論是自建 Harness 還是使用 Claude Code 或 Codex，最有效用的習慣是：**查看實際發送給模型的請求**（系統提示、訊息、工具清單的原始格式，而非 UI 中經過潤飾的版本）。半數「為什麼它這樣做」的疑惑，答案都是同一個：AGENTS.md 從未被載入、技能描述未被載入、或壓縮悄悄刪除了 Agent 後來矛盾的決策 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

使用 LangFuse、LangSmith 等追蹤工具可以擷取每次呼叫的完整 Prompt、訊息和工具清單，也讓整個生態系統變得可理解——你能看到各種 Plugin、Extension、Skill 實際注入了什麼 。 [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)

***

## [結論與行動建議]

### 啟發金句

> 「你的 Agent 沒有變笨，是它的窗口變髒了。模型沒有退化，退化的是你放進窗口的東西。」

### 具體行動法則：S-C-W-I 法則

當 Agent 在長任務中表現退化時，依序檢查四個操作：

- **S — Select（篩選）**：模型是否看到了正確的內容？還是正確內容被埋在窗口中間？
- **C — Compress（壓縮）**：摘要是否丟棄了關鍵細節？
- **W — Write（寫入）**：是否有本應寫入磁碟的工作遺失在對話中？
- **I — Isolate（隔離）**：是否有巨型上下文淹沒了子任務？

外加第五個問題：**「我能否看到窗口中的內容？」** 若答案是否，就從可觀測性開始。

### 生活實踐建議

在日常使用 Claude Code 或 Codex 時：

1. 養成「先看窗口」的習慣——在嘗試優化前，先檢查實際送達模型的 Prompt、訊息和工具清單
2. 對長任務採用 Research → Plan → Implement 工作流，每階段都寫入磁碟，實作階段從 plan file 開全新窗口
3. 將大型日誌或搜尋任務交給子代理處理，只帶回結果而非完整過程
4. 留意 Harness 的 Changelog——若 Agent 突然變差，很可能是上下文管理策略被調整了
5. 使用 LangFuse / LangSmith 等工具建立常態化的 Prompt 追蹤，而非偶爾查看

***

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/mM_Wxemh3lU [youtube](https://www.youtube.com/watch?v=SdoPo1UH6Ew)
- Lance Martin / LangChain 四操作框架：https://www.langchain.com
- HumanLayer（Dex Horthy）：https://humanlayer.com
- LangFuse：https://langfuse.com
- LangSmith：https://smith.langchain.com
