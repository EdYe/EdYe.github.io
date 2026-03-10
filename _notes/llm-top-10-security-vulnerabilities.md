---
title: 'OWASP LLM 十大安全威脅解析'
date: 2026-03-10
image: /images/影片筆記/llm-top-10-security-vulnerabilities.png
category: 影片筆記
tags: [提示詞注入, 敏感資訊洩漏, 供應鏈漏洞, 過度授權, 資料中毒]
description: '這部影片深入解析了 OWASP LLM 十大安全威脅，揭示攻擊者如何透過提示詞操控、資料中毒或供應鏈漏洞來威脅 AI 系統'
quote: '飲用水中只要混入一點點毒素，就會讓所有人受害。'
action: '建立 AI Gateway 作為過濾層，落實資料最小化，對關鍵決策進行人工審核。'
source_has_timestamps: true
source_raw: LLM十大安全漏洞
---
這部影片由 IBM Technology 頻道製作，詳細解析了 **OWASP (開放網路軟體安全計畫)** 針對 **大型語言模型 (LLM)** 所提出的十大安全漏洞（Top 10）。隨著 AI 技術快速普及，這份清單旨在幫助開發者與企業識別並防範針對 AI 系統的新興攻擊手法。

### 核心摘要

這部影片深入解析了 **OWASP LLM 十大安全威脅**，揭示攻擊者如何透過提示詞操控、資料中毒或供應鏈漏洞來威脅 AI 系統，並強調了部署 AI 應用時必須具備的防禦機制。

---

### 詳細重點整理

#### 1. 提示詞注入攻擊 (Prompt Injection) [[01:08](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=68)]

這是 LLM 最常見的威脅，分為直接與間接兩種：

* **直接注入：** 攻擊者直接在對話框輸入指令，試圖繞過系統限制（例如：透過扮演化學系學生的方式，誘騙 AI 給出爆炸物配方 [[02:11](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=131)]）。
* **間接注入：** 攻擊者在 AI 會讀取的網頁或文件中埋藏惡意指令。當使用者要求 AI 摘要該文件時，AI 會執行文件中隱藏的惡意命令 [[03:04](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=184)]。
* **防禦建議：** 導入 **AI 防火牆 (AI Gateway)** 來過濾輸入與輸出，並進行系統性的滲透測試 [[06:02](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=362)]。

#### 2. 敏感資訊洩漏與資料安全性 [[07:03](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=423)]

AI 可能在訓練或推論過程中不經意流出機密資料：

* **資訊洩漏：** 若模型在含有個人身分資訊 (PII)、健康資料或企業財務數據的資料庫上訓練，攻擊者可能透過巧妙提問讓 AI 吐出這些機密 [[08:01](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=481)]。
* **模型反轉攻擊：** 攻擊者透過大量自動化請求，試圖提取模型內部的智慧財產權（Model Inversion Attack） [[09:01](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=541)]。
* **防禦建議：** 實施資料清洗 (Sanitization)、嚴格的存取控制 (Access Control)，並確保整體安全態勢管理 [[11:38](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=698)]。

#### 3. 供應鏈漏洞與資料中毒 [[11:45](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=705)]

AI 的開發極度依賴第三方組件：

* **供應鏈風險：** 許多開發者從 HuggingFace 等平台下載未經審查的模型或資料，這可能引入惡意組件 [[12:34](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=754)]。
* **資料中毒 (Data Poisoning)：** 攻擊者在訓練資料或 RAG（檢索增強生成）的參考源中混入錯誤資訊，破壞模型的準確性與可信度 [[15:10](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=910)]。
* **防禦建議：** 審查資料來源 (Vetting)、追蹤資訊來源 (Provenance) 並持續進行弱點掃描 [[14:47](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=887)]。

#### 4. 過度授權與輸出處理不當 [[19:15](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=1155)]

當 AI 被賦予過多權限或其輸出未經檢查時：

* **輸出處理不當：** 若 LLM 生成的程式碼被系統直接執行，可能引發 SQL 注入或跨站腳本攻擊 (XSS) [[19:55](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=1195)]。
* **過度授權 (Excessive Agency)：** 若給予 AI 調用 API、執行應用程式或控制實體設備的權限，一旦模型產生幻覺或被注入惡意指令，後果將不堪設想 [[20:18](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=1218)]。

#### 5. 錯誤資訊與服務阻斷 (DoS) [[23:06](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=1386)]

* **錯誤資訊：** AI 產生的幻覺或被人為操縱的資訊可能導致決策失誤，必須透過交叉驗證來確保可靠性 [[23:26](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=1406)]。
* **無限消耗 (Unbounded Consumption)：** 類似網路攻擊中的 DDoS，攻擊者透過發送極其複雜的請求來癱瘓 AI 服務，或造成嚴重的財務損失（Denial of Wallet） [[23:47](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=1427)]。

---

### 結論與行動建議

影片最後強調，AI 安全不應僅依賴模型本身的限制，而應採取多層次的防禦策略：

* **具體建議：**
1. 建立 **AI Gateway**：作為使用者與模型間的過濾層。
2. 落實 **資料最小化原則**：訓練資料應先剔除敏感 PII。
3. **批判性思考**：不要盲目信任 AI 輸出的結果，務必對關鍵決策進行人工審核。


* **啟發性金句：** 「飲用水中只要混入一點點毒素，就會讓所有人受害。」(Just a little bit of toxin in the drinking water makes us all sick.) —— 說明了資料中毒對 AI 長期準確性的嚴重影響 [[15:57](http://www.youtube.com/watch?v=gUNXZMcd2jU&t=957)]。

**相關連結：** [https://youtu.be/gUNXZMcd2jU](https://www.google.com/search?q=https://youtu.be/gUNXZMcd2jU)

---
