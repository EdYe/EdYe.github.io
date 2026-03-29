---
title: 'Gemini Live API語音代理開發'
date: 2026-03-29
image: /images/影片筆記/gemini-live-api-voice-agent.jpeg
category: 影片筆記
tags: [Gemini Live API, 語音代理, WebSocket, 多模態, 即時對話]
description: '介紹Gemini Live API的強大功能，展示如何利用Gemini 3.1 Flash-Lite模型，透過WebSocket建立低延遲、具備情感理解的即時語音對話應用'
quote: 'Gemini 3真正開啟了「行動時代」（Era of Action）。'
action: '先從GitHub的gemini-live-api-examples專案著手，快速建立一個能跑起來的Localhost示範'
source_has_timestamps: true
---

**《Building Voice Agents with Gemini 3》** 這部影片詳細介紹了如何利用 Google 最新的 Gemini 3.1 Flash-Lite 模型構建具備語音、影像雙向互動能力的即時 AI 代理。

---

### 核心摘要
這部影片介紹了 **Gemini Live API** 的強大功能，展示開發者如何利用 **Gemini 3.1 Flash-Lite** 模型，透過 WebSocket 建立低延遲、具備情感理解且能處理影音雙向流的即時語音對話應用。

---

### 詳細重點整理

#### 1. Gemini Live API 的核心優勢與多模態能力
* **原生音訊處理**：不同於傳統「語音轉文字再轉語音」的模式，Gemini 3 採原生音訊輸入輸出，能精準捕捉語氣、情感並實現自然對話 [[00:52](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=52)]。
* **多模態輸入**：支援即時音訊（16kHz PCM）與影像幀（每秒 1 幀 JPEG），讓 AI 能「看見」使用者的環境並做出反應 [[05:37](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=337)]。
* **多國語言與中斷機制**：支援超過 70 種語言，且具備語音活動檢測（VAD），使用者可隨時打斷 AI 說話，互動感極為真實 [[04:59](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=299)]。

#### 2. 開發實作：從 AI Studio 到 Python SDK
* **Google AI Studio 測試**：開發者可先在 AI Studio 選擇 `gemini-3.1-flash-lite` 模型，自定義系統指令（如設定愛爾蘭口音）與選取語音角色 [[01:29](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=89)]。
* **SDK 整合步驟**：
    1.  **取得 API Key**：在 AI Studio 建立專屬金鑰 [[10:48](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=648)]。
    2.  **環境設定**：複製 GitHub 範例代碼，建立 Python 虛擬環境並安裝 `google-genai` SDK [[12:07](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=727)]。
    3.  **配置對話 Session**：設定回應模態（Audio）、語音角色、系統指令以及工具呼叫（Tool Use）能力 [[13:57](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=837)]。

#### 3. 技術架構與串流處理細節
* **WebSocket 連線**：API 基於有狀態的 WebSocket 連線，開發者需處理 Session 管理，包括連線中斷後的重新啟動 [[06:09](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=369)]。
* **整合路徑選擇**：
    * **Server-to-Server**：安全性高，適合整合私有工具 API，但延遲較大 [[06:42](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=402)]。
    * **Client-to-Server**：效能最佳，但需使用暫時性 Token（Ephemeral Tokens）以防 API Key 外洩 [[07:15](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=435)]。
* **夥伴解決方案**：若需快速上線生產環境，建議使用 LiveKit、Daily (Pipecat) 或 Firebase AI SDK 等夥伴工具，簡化 WebRTC 整合難度 [[08:42](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=522)]。

#### 4. 生產環境的限制與最佳實踐
* **Session 時長限制**：純語音 session 限 15 分鐘，影音混合則為 2 分鐘。為延長時長，需實作「上下文視窗壓縮」（Context Window Compression） [[19:50](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=1190)]。
* **斷線重連機制**：WebSocket 通常在 10 分鐘左右會收到「Go Away」訊息，開發者必須實作 Session Resumption 並在重連期間緩衝音訊 [[20:21](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=1221)]。

---

### 結論與行動建議
**金句標註：** 「Gemini 3 真正開啟了『行動時代』（Era of Action）。」 [[05:13](http://www.youtube.com/watch?v=XV5bhkDpL7U&t=313)]

**具體建議：**
1.  **精確定義工具與角色**：在 System Instruction 中明確定義 AI 的人格特質與工具呼叫權限，這是確保語音代理專業度的關鍵。
2.  **優化延遲感**：建議傳送 20ms 到 40ms 的音訊區塊（Chunks），以獲得最流暢的對話體驗。
3.  **初學者路徑**：先從 GitHub 的 `gemini-live-api-examples` 專案著手，快速建立一個能跑起來的 Localhost 示範。