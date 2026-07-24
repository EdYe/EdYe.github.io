---
title: '為什麼殺掉多代理管線：ZS 製藥分析重建'
date: 2026-07-25
image: /images/AI筆記/kill-multi-agent-pipeline.jpg
category: AI筆記
tags: [推理所有權缺失, 上下文交接遺失, 確定性代理分離, 單代理推理所有權, 知識圖譜控制平面]
description: 'ZS Associates 原本打造一套模仿人類分析師行為的多代理管線，用於製藥商業分析，涵蓋訊號偵測、根因歸因、行動合成與展望預測，但各代理輸出前後矛盾。'
quote: '不要模仿人類的步驟來設計 AI 的架構——讓架構從觀察中自然生長。'
action: '拆分確定性與推理性任務、收斂至單一推理者，並用結構化知識圖譜約束代理的搜索空間'
source_has_timestamps: true
---
# 為什麼我們「殺掉」了多代理管線 — ZS Associates 的製藥分析系統重建實錄

來源影片：AI Engineer 頻道，講者 Subbiah Sethuraman（ZS AI 工程負責人）與 Abhilash Asokan（AI 工程總監） [youtube](https://www.youtube.com/?app=desktop&hl=ar)

***

## [核心摘要]

ZS Associates 原本打造一套模仿人類分析師行為的多代理管線（Multi-Agent Pipeline），用於製藥商業分析——涵蓋訊號偵測、根因歸因、行動合成與展望預測。各代理各自推導出「正確的事實」，卻因缺乏端到端推理的所有權，導致最終輸出前後矛盾（例如：正確找出「保險覆蓋降級」為根因，卻建議「增派業務代表」的錯誤行動）。團隊遂推翻舊架構，改以三大原則重建：訊號�測前移為確定性管線、推理收斂至單一代理、知識圖譜作為控制平面。最終系統在 20 分鐘內完成原本分析師需 3–4 週的工作 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

***

## [詳細重點整理]

### 1. 製藥商業分析與分析師的四步驟 [00:00]

製藥產業分為研發（藥物發現與臨床試驗）與商業兩大職能，後者涵蓋品牌績效、市場表現、業務代表（rep）投入效率、患者旅程與療程切換等分析場景 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

分析師的標準工作流程為四步：
- **訊號偵測**（Signal Detection）：偵測異常，例如某區域處方量下降
- **根因歸因**（Root Cause Attribution）：找出原因——是競爭藥品進入、保險覆蓋縮減、還是代表推廣不力
- **行動建議**（Action）：針對根因制定對策
- **展望預測**（Outlook）：評估行動實施後品牌銷售的改善預期 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：商業分析四步驟**

***

### 2. V1：每一步一個代理 [02:33]

團隊為四步驟各自建構獨立代理——訊號偵測代理、來源定位代理（Source Localization，判斷下降集中於哪個區域或保險方）、驅動因子歸因代理（Driver Attribution）、綜合合成代理（Synthesis），並由一個 **orchestrator agent** 串接所有代理 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

系統產出的資訊封包範例：品牌處方量在某區域 4 週內下降 18%，原因是保險方將藥品移至較差給付層級，建議增派業務代表說服醫生，展望為銷售回升 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：Orchestrator Agent**

***

### 3. 為何輸出不連貫 [03:26]

因果判定正確（患者無法負擔藥費），但行動建議完全偏離根因——未聚焦保險給付問題，反而建議「增派業務代表」。因行動錯誤，展望預測自然失準。每個代理推導出「正確的事實」，卻沒有任何單一代理掌握端到端的全貌 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：推理所有權缺失（Reasoning Ownership Gap）**

***

### 4. 失敗原因：訊號、交接遺失與缺失領域知識 [04:32]

三大根因：

- **語言模型不應做訊號偵測**：訊號偵測是統計問題（如處方量下降可由統計方法直接取得），不需要 LLM 判斷。代理有時將雜訊誤判為訊號 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)
- **上下文在代理交接中遺失**：驅動因子歸因代理正確識別「保險覆蓋下降」為原因，但綜合代理無法理解其權重與影響——為何「保險覆蓋縮減」比「代表拜訪不足」更重要。關鍵上下文在 handoff 中丟失 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)
- **缺乏共享的業務領域知識**：各代理不理解 KPI 之間的關係，例如 TRx（處方量）為何升降、KPI 如何驅動彼此，缺乏共同的事實基礎 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：上下文交接遺失（Context Handoff Loss）**

***

### 5. 重建起點：在空目錄中觀察 Claude Code [05:57]

團隊的第一直覺是回到設計板重新規劃拓撲、技能、工具與交接 schema。但他們選擇了不同的路徑：開啟一個空白目錄，給 Claude Code 僅 bash 工具與資料庫存取權，輸入一個已識別的訊號，然後觀察它實際做什麼 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

觀察發現：Claude Code 反覆地撰寫函數、查詢資料庫、推理——這啟發了團隊將整個流程收斂至單一代理的設計 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：觀察驅動架構（Observation-Driven Architecture）**

***

### 6. 確定性訊號偵測前置 [07:01]

訊號偵測從 agentic 系統中剝離，改為純確定性管線：使用不同統計方法，加上 guardrails、閾值與優先級排序。自動化管線掃描所有 KPI，偵測異常與趨勢，將訊號放入佇列。訊號進入佇列後，代理才被喚醒——**代理的職責是調查，而非識別訊號** 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：確定性與代理性分離（Deterministic-Agentic Separation）**

***

### 7. 收斂為單一代理 [08:05]

基於觀察 Claude Code 的行為模式，團隊將整個推理流程整合至單一代理。代理仍保留平行處理能力，但移除了「分散式推理」——判斷不分散於多代理之間，而是由單一代理端到端擁有 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

代理僅在需要專注調查時（如查詢某區域代表活動），才動態派生子代理執行聚焦任務，調查結果回傳主代理，推理與判斷仍由主代理控制 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：單代理推理所有權（Single-Agent Reasoning Ownership）**

***

### 8. 知識圖譜作為控制平面 [09:22]

單代理架構解決了連貫性問題，但代理仍缺乏業務上下文——不了解實體、領域、KPI 及其關聯。代理看資料表、自行推論關係，既不具擴展性，又常產生不存在於真實業務中的假關係 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

團隊與領域專家合作建構製藥商業知識圖譜，涵蓋地理實體、保險方、帳戶、品牌、KPI 之間的關聯，以及一級/二級/三級 KPI 的驅動關係 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

知識圖譜不只是資料查詢表，而是代理的**控制平面（Control Plane）**——它決定代理可以查什麼、走哪條路徑、評估哪些調查假設 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：知識圖譜控制平面**

***

### 9. 每條邊都是一個假設 [11:04]

知識圖譜的運作機制分為「定位在哪裡」與「為什麼發生」兩階段：

- **定位**：TRx 在全國下降 → 知識圖譜引導代理評估各維度（區域、保險方、帳戶的組合），找出下降集中點。這些排列組合由圖譜結構約束，避免盲目搜索 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)
- **為什麼**：定位後，代理利用 KPI 關聯圖譜評估各驅動因子。**每一條邊都是一個假設**——代理回到原始資料驗證該假設，看數字是否支持或反駁。支持則沿圖譜繼續遍歷，矛盾則回溯 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

代理在迴圈中反覆：進入圖譜 → 觀察鄰邊 → 形成假設 → 回到資料驗證 → 推理 → 遍歷或回溯，直到假設耗盡或找到根因 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

**關鍵概念：邊即假設**

***

### 10. 成果與關鍵啟示 [13:48]

經過 50+ 輪迭代與大量 token 消耗，系統在 20–30 分鐘內完成原本分析師需 3–4 週的工作 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

四大關鍵啟示：
- 不要將人類的設計約束強加到架構上——讓架構自然衍生
- 複雜工作流同時包含確定性部分與代理性部分——不要讓代理執行確定性任務
- 需要一個代理端到端擁有推理——它可以派生子代理、使用工具與技能，但判斷不能分散
- 圖譜不能僅作為查詢層——圖譜必須作為控制平面，引導代理導航與決策 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

***

## [技術/數據對比]

| 維度 | V1：多代理管線 | V2：重建架構 |
|---|---|---|
| 訊號偵測 | LLM 代理判斷（常誤判雜訊為訊號） | 確定性統計管線，含 guardrails 與閾值，前置運行  [youtube](https://www.youtube.com/?app=desktop&hl=ar) |
| 推理架構 | 多代理 + orchestrator，判斷分散 | 單一代理端到端擁有推理，子代理僅做聚焦調查  [youtube](https://www.youtube.com/?app=desktop&hl=ar) |
| 上下文管理 | 代理間 handoff 導致上下文遺失 | 單代理消除交接損失  [youtube](https://www.youtube.com/?app=desktop&hl=ar) |
| 領域知識 | 各代理缺乏共享業務上下文 | 知識圖譜作為控制平面，約束搜索空間  [youtube](https://www.youtube.com/?app=desktop&hl=ar) |
| 圖譜角色 | 無 | 控制平面（非查詢表），每條邊為可驗證假設  [youtube](https://www.youtube.com/?app=desktop&hl=ar) |
| 輸出連貫性 | 因果正確但行動矛盾 | 端到端連貫  [youtube](https://www.youtube.com/?app=desktop&hl=ar) |
| 效率 | 分析師需 3–4 週 | 系統 20–30 分鐘完成  [youtube](https://www.youtube.com/?app=desktop&hl=ar) |

***

## [結論與行動建議]

> **啟發金句**：不要模仿人類的步驟來設計 AI 的架構——讓架構從觀察中自然生長。

**具體行動建議：D-S-K 法則**

- **D**eterministic first（確定性優先）：先剝離所有可由統計/規則完成的工作，讓代理專注於需要推理的部分
- **S**ingle ownership（單一所有權）：確保一個代理端到端擁有推理鏈，避免上下文在交接中蒸發
- **K**nowledge graph as control plane（知識圖譜即控制平面）：圖譜不是查詢工具，而是約束與引導代理搜索空間的導航系統

**生活實踐建議**：在日常產品開發中，遇到 LLM 輸出「事實正確但邏輯不連貫」的問題時，第一直覺不應是增加更多代理或更複雜的交接 schema，而應退一步：拆分確定性與推理性任務、收斂至單一推理者、用結構化領域知識（知識圖譜）約束搜索空間。這套思路同樣適用於任何需要多步驟推理的 AI 應用場景，不限於製藥分析 。 [youtube](https://www.youtube.com/?app=desktop&hl=ar)

***

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/u6jJcIFDLE4 [youtube](https://www.youtube.com/?app=desktop&hl=ar)
- 講者 LinkedIn（Subbiah Sethuraman）：https://www.linkedin.com/in/subbiahsethuraman/ [youtube](https://www.youtube.com/?app=desktop&hl=ar)
- 講者 Medium（Subbiah Sethuraman）：https://subbiah-sethuraman.medium.com/ [youtube](https://www.youtube.com/?app=desktop&hl=ar)
