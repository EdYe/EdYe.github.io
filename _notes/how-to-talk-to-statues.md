---
title: '用兩小時 Vibe Code 出對話雕像：API 膠水層的商業爆發力'
date: 2026-06-04
image: /images/AI筆記/how-to-talk-to-statues.jpg
category: AI筆記
tags: [Vibe Coding, API編排, 語音界面, 病毒傳播, 對話代理]
description: 'ElevenLabs 成長工程師 Joe Reeve 用兩小時 Vibe Code 出一個「對話雕像」App，只需對準雕像拍照，系統就能自動識別身份、生成歷史背'
quote: 'Vibe Coding 的關鍵不是解決困難的技術問題，而是把 API 膠水黏得漂亮，並把它的故事說好。'
action: '下次 Hackathon 直接用 Cursor + 現有 AI API，兩小時先跑出 Demo 影片，而非等架構完整再展示'
source_has_timestamps: true
---
# 📖 How to Talk to Statues — Joe Reeve, ElevenLabs

***

## [核心摘要]

ElevenLabs 成長工程師 Joe Reeve 用兩小時 Vibe Code 出一個「對話雕像」App，只需對準雕像拍照，系統就能自動識別身份、生成歷史背景、合成匹配語音並啟動對話代理——全程不到 30 秒。 此案例完整示範了「API 膠水層」的商業爆發力：0 自建模型、全部串接現有 API，卻引爆 150 萬次曝光，並促使博物館、拍賣行競相洽談合作。

***

## [詳細重點整理]

### 1. 雕像 App 的誕生與病毒傳播 [00:29]

週日閒來無事，Joe 用 Cursor 與單一 One-Shot Prompt，兩小時內完成整個 App。 週二發布後首日達 50,000 次曝光；隔日補發「Vibe Coding 版」後，瞬間衝上 **150 萬次**。博物館 CEO 直接找到他的 WhatsApp，開口就說：「我有 10 個人花了一年做這件事，你怎麼做到的？」

**關鍵概念：Vibe Coding（氛圍式程式設計）**——不以工程思維主導，而是描述意圖讓 AI 自行實作，快速驗證互動模式的最短路徑。

***

### 2. 技術架構：30 秒內的完整 Pipeline [01:51]

整條流水線：
- **拍照** → OpenAI Deep Research 識別雕像身份並生成歷史背景與語音描述
- **語音合成** → ElevenLabs Voice Design API 依描述生成匹配聲音
- **代理啟動** → ElevenLabs Agents 平台自動建立對話代理
- **開始對話** → 全程約 30 秒完成

**關鍵概念：One-Shot API Orchestration（一次性 API 編排）**——以最少程式碼將多個 AI API 串聯成完整產品，「膠水邏輯」本身即是核心競爭力。

***

### 3. 商業擴散與博物館洽談 [03:54]

病毒傳播後，Tripadvisor 競業、Bonhams、Christie's 拍賣行陸續接觸，希望讓用戶「與待售藏品對話」。 科學博物館 co-CEO 主動接洽，但表明目前仍在摸索方向。ElevenLabs 正計畫將技術內嵌至真實雕像（內建喇叭與麥克風），消除「螢幕隔離感」，讓互動更自然。

**關鍵概念：Ambient Voice Interface（環境語音介面）**——把技術隱藏進實體物件，使科技感消失，讓體驗本身成為前景。

***

### 4. 語音界面的核心挑戰 [10:16]

當前語音 AI 交互存在幾個根本矛盾：

- **資訊密度失衡**：語音輸出的資訊密度遠低於視覺閱讀，用戶更希望「語音輸入 → 圖表/UI 輸出」
- **禮貌障礙**：人們太有禮貌不敢打斷 AI，而打斷後 AI 又常重新開始而非承接
- **缺乏副語言暗示**：人類對話依賴眼神、點頭等信號，語音代理完全缺席
- **陪伴感意外重要**：語音回應即使資訊量低，也能降低孤獨感，提升持續互動意願

**關鍵概念：Parallel Modality Output（平行模態輸出）**——語音輸入 + 視覺輸出的混合模式，可能是下一代 AI 界面的勝出形態。

***

### 5. 病毒影片製作技法 [29:49]

Joe 用 **DJI 藍牙領夾麥** 收音，手機版 **CapCut** 剪輯，整段影片剪輯僅花 **20–25 分鐘**。 關鍵技巧：

- **Hook 在前 6–12 秒**：平均觀看時間即在此區間，錯過即流失
- **字幕必加**：顯著提升完播率
- **音樂先行**：雕像影片先選定帶有帝國氣息的配樂，再配合節奏剪輯畫面
- **ElevenLabs 音樂生成**：可先描述情緒 Vibe，自動生成配樂，再反向設計旁白

**關鍵概念：Hook-First Editing（鉤子優先剪輯法）**——以平台分析數據倒推剪輯策略，確保前段即完成意圖傳達。

***

## [技術架構對比]

| 環節 | 工具/服務 | 說明 |
|---|---|---|
| 雕像識別 | OpenAI Deep Research | 生成歷史資料與語音描述 |
| 語音生成 | ElevenLabs Voice Design API | 依文字描述合成匹配聲音 |
| 對話代理 | ElevenLabs Agents 平台 | 全託管部署，可接 MCP/Knowledge Files |
| 開發環境 | Cursor + One-Shot Prompt | 2 小時完成 MVP |
| 影片製作 | CapCut（手機）+ DJI 麥克風 | 20–25 分鐘完成剪輯 |

***

## [結論與行動建議]

**啟發金句：** 
> 「Vibe Coding 的關鍵不是解決困難的技術問題，而是把 API 膠水黏得漂亮，並把它的故事說好。」

**具體行動法則：P-V-S 法則**
- **P（Pipeline）**：先用現有 API 串出最短可行 Pipeline，而非自建模型
- **V（Viral Hook）**：產品 Demo 影片的 Hook 必須在前 10 秒，配樂優先
- **S（Story Glue）**：技術膠水層的「敘事」比技術本身更能創造商業機會

**生活實踐建議：**
- 作為 AI 產品經理，下次 Hackathon 或 PoC，直接用 Cursor + 現有 AI API，兩小時先跑出 Demo 影片，而非等架構完整再展示
- 製作產品展示影片時，先確定情緒 Vibe → 用 ElevenLabs 生成配樂 → 再錄製旁白，倒序製作反而更有感染力
- 評估語音 AI 產品時，優先考慮「語音輸入 + 視覺輸出」混合模式，純語音對話在資訊密度上存在結構性瓶頸

***

## [參考連結]

- 🎥 原始影片：https://youtu.be/u-rJwPPU3QA?si=Bh7Rs5BcOfUf8duh 
- 📝 技術部落格：https://elevenlabs.io/blog/talk-to-a-statue-building-a-multi-modal-elevenagents-powered-app 
- 🐦 Joe Reeve Twitter：https://x.com/isnit0
