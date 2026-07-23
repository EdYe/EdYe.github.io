---
title: '打造長格式AI主持人的完整工作流'
date: 2026-07-23
image: /images/AI筆記/ai-presenter-flow-agent-elevenlabs.jpg
category: AI筆記
tags: [角色生成, 主提示詞, Agent自動分段, 皮膚增強, 語音克隆]
description: '本影片完整示範如何從零打造一位「長格式 AI 主持人」——具備一致的臉孔、一致的聲音，以及可連續講述數分鐘的完整表演。'
quote: '💡「與其花十分鐘完美化第一張圖，不如生成三張圖從中挑選最強的那一張。」'
action: '🎯依T-C-V-F法則：標記角色（Tag）、貼入完整台詞（Complete）、確保視覺一致（Visual Consistency）、修正拼接與替換語音（Fix & Fuse）。'
source_has_timestamps: true
---
## [核心摘要]

本影片完整示範如何從零打造一位「長格式 AI 主持人」——具備一致的臉孔、一致的聲音，以及可連續講述數分鐘的完整表演。核心痛點在於：多數 AI 影片工具每次只能生成 10 秒短片，長篇對話需要手動拆分腳本並逐段重新撰寫 prompt。本工作流透過 **Google Flow Agent** 搭配一支「主提示詞（Master Prompt）」，讓 Agent 自動將完整台詞拆分為連續片段，一次生成整段影片，再用 **ElevenLabs** 進行語音克隆以確保聲音一致性，徹底解決手動分段與語音不連續的問題。

***

## [詳細重點整理]

### 1. AI 角色生成：三種路徑 [00:54]

建立 AI 角色有三種方式：

- **Google Flow 內建角色預設**：在專案中開啟 Character 區段，選擇預設會自動生成角色 prompt，可直接編輯或從頭撰寫 [00:54]
- **Higsfield AI Influencer**：選擇角色類型、性別、族群、年齡等參數，直接生成角色圖片，不需手寫 prompt [01:36]
- **Claude 角色提示詞產生器 + 任意圖像模型**：透過免費 Claude 工具回答幾個角色問題後自動生成詳細 prompt，再貼入 Google Flow（使用 Nano Banana Pro 模型），也可替換為 ChatGPT、Cream 等其他模型 [02:03]

**關鍵概念：** **角色提示詞產生器（Character Prompt Generator）**——將角色描述需求結構化，降低手寫 prompt 的不確定性。

講者強調**幾乎不用第一次生成的結果**，建議生成 2-3 個版本從中挑選最自然的表情與五官，因為微小的表情差異會大幅影響角色的真實感 [02:45]。

### 2. 場景搭建與皮膚增強 [03:12]

角色確定後，需將角色置入匹配的場景：

- 從 Pinterest 找到訪談風格的參考圖，上傳至 ChatGPT 請其描述場景為 prompt [03:18]
- 將該 prompt 連同角色圖片一起貼入 Google Flow 生成最終場景 [03:26]
- 同一場景也用 ChatGPT 生成了一版，講者偏好 ChatGPT 的版本 [03:33]

**關鍵概念：** **參考圖反推提示詞（Reference-to-Prompt）**——用現成圖片逆向生成場景描述，確保畫面氛圍與角色定位一致。

接著進行**皮膚增強**：AI 生成的人像常有「塑膠感皮膚」，透過 **Topaz Bloom**（或任意皮膚增強/放大工具）處理，能還原自然皮膚紋理。長格式影片中角色會持續出現在畫面上數分鐘，這些細節累積效果顯著 [03:47]。

完成後將增強圖片上傳回 Google Flow 的 Character 面板，選擇語音、自訂說話方式、命名角色，角色即設定完成 [04:27]。

### 3. 長格式對話生成：主提示詞 + Flow Agent [04:53]

Google Flow 使用 **Gemini Omni Flash** 模型，單次最多生成 **10 秒** 影片 [04:53]。傳統做法需將長台詞手動拆成多段、每段各寫一個 prompt。本工作流的核心突破是設計了一支**主提示詞（Master Prompt）**，搭配 Google Flow Agent 自動化整個流程 [05:08]。

主提示詞包含五個結構區塊：

| 區塊 | 功能 |
|------|------|
| **角色標記（@Tag）** | 輸入 `@` 選擇角色，告知 Flow 哪個角色執行對話 |
| **完整台詞** | 一次貼入全部台詞，無需手動分段 |
| **指令區段（Delivery Style）** | 自訂語氣風格，如「溫柔微笑、快速對話節奏」或「嚴肅訪談風格」 |
| **視覺一致性** | 指示模型在每個片段中保持角色外觀與場景一致 |
| **攝影機方向** | 控制鏡頭風格，預設每段使用兩個靜態鏡頭以增加自然感，也可改為全程正面單鏡頭 |

**關鍵概念：** **Agent 自動分段（Agent-Driven Segmentation）**——Flow Agent 自動將長台詞按 10 秒上限拆分為連續片段，同時保留每個字的正確順序，免除手動切腳本的負擔 [05:59]。

在 Prompt Settings 中可關閉「每段生成前請求確認」，讓 Agent 全自動跑完整個流程 [06:59]。數秒內所有片段即生成完畢 [07:16]。

### 4. 錯誤修正與片段拼接 [08:04]

Google Flow 大多數情況能準確還原台詞，但偶爾會出現重複單字、漏字或小錯誤。修正方式：

- 開啟有誤的片段 → 點擊 **Reuse Prompt** → 重新生成，通常下次即修正 [08:24]
- 若仍有問題 → 編輯 prompt、縮短該段台詞 → 再次生成 [08:31]

片段拼接有兩種方式：

- **Google Flow 內建場景**：建立 Scene，依序加入各片段，可直接預覽並匯出 [08:44]
- **外部影片編輯器**（講者偏好）：使用 **DaVinci Resolve**，匯入所有片段、依序排列、修剪多餘停頓與靜音，再匯出影片 [09:05]

### 5. 語音一致性：ElevenLabs 雙工作流 [09:23]

若整支影片僅使用 Flow 生成的片段，語音已經一致，可略過此步驟。但若需加入 Flow 之外的額外台詞，或讓主持人使用自訂語音，則需透過 **ElevenLabs** 處理 [09:23]。

**語音克隆流程：**

- 開啟 Voices → Create Voice → 選擇 Voice Cloning → 上傳音訊/影片樣本（可用自己的聲音或 Flow 生成的聲音）→ 命名並儲存 [09:57]

**兩種使用方式：**

- **Voice Changer（變聲器）**：上傳要替換語音的影片/音訊 → 選擇克隆語音 → 生成新音軌 [10:17]
- **Text to Speech（文字轉語音）**：貼入新腳本 → 選擇同一克隆語音 → 生成音訊。需注意語速、語調與原始 Flow 語音會有小差異，但多數情境下已足夠 [10:33]

最後回到影片編輯器，用克隆音軌替換原始音訊 [10:54]。後續可在編輯器中做調色、遮罩隱藏浮水印等最終修飾 [11:01]。

***

## [技術/數據對比]

| 維度 | 傳統手動流程 | 本工作流（Master Prompt + Flow Agent） |
|------|-------------|---------------------------------------|
| 對話拆分 | 手動將台詞切成 10 秒段落 | Agent 自動分段，保留字序 |
| Prompt 撰寫 | 每段需各寫一個 prompt | 一次貼入完整台詞，單一主提示詞 |
| 視覺一致性 | 每段需手動確保角色與場景一致 | 提示詞內建一致性指令 |
| 生成流程 | 逐段手動觸發 | 關閉確認後全自動連續生成 |
| 語音處理 | 僅限 Flow 內建語音 | ElevenLabs 克隆 + Voice Changer + TTS |

***

## [結論與行動建議]

> **啟發金句：** 「與其花十分鐘完美化第一張圖，不如生成三張圖從中挑選最強的那一張。」

**具體行動建議 — T-C-V-F 法則：**

- **T（Tag）**：用 `@` 標記角色，讓 Flow 知道誰在說話
- **C（Complete）**：一次貼入完整台詞，讓 Agent 自動分段
- **V（Visual Consistency）**：在提示詞中明確指示保持角色與場景一致
- **F（Fix & Fuse）**：用 Reuse Prompt 修正錯誤片段，再用編輯器拼接與替換語音

**生活實踐建議：** 身為 AI 應用架構師，可將此工作流應用於產品 Demo 影片、內部培訓教材或技術說明影片的快速製作。以一支主提示詞作為「模板」，團隊成員只需替換台詞內容即可批量生成不同主題的 AI 主持人影片。語音克隆部分可建立公司專屬語音庫，確保品牌形象一致性。建議先從 30 秒以內的短台詞開始測試，熟悉分段準確率後再逐步拉長至數分鐘的完整腳本。

***

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/00UsxuaG-5w
- 免費 Master Prompt + Claude 角色提示詞產生器：https://genaikeera.notion.site/ai-avatar-starter-kit

***

# AI虛擬人像入門套件（AI Avatar Starter Kit）| 打造你自己的 AI 虛擬人像

🌸 **AI 虛擬人像入門套件**

打造你自己的會說話 AI 虛擬人像所需的一切：角色生成器、Google Flow 代理（Agent）主提示詞，以及我實際使用的工具。

▶️ 新來的嗎？先觀看完整教學影片，再到下方領取免費資源。

▶ 在 YouTube 觀看第 03 集教學

---

## 🚀 快速開始 — 4 個步驟

**建立角色（Create Character）**：使用以提示詞驅動的圖像生成器，或像 Higgsfield 這類專門工具，生成獨特的 AI 角色，接著強化皮膚質感以提升真實感。

**生成影片（Generate Video）**：將角色與對白上傳至 Google Flow，搭配主提示詞（master prompt）自動生成連貫一致的影片片段。

**組裝素材（Assemble Footage）**：將所有生成的片段匯入影片剪輯軟體，安排順序並剪去不必要的停頓或錯誤。

**完成收尾（Finalize）**：視需要使用 ElevenLabs 等 AI 工具調整語音，接著匯出完成的長版影片。

---

## 1️⃣ 生成你的角色

🖱️

**開啟角色提示詞生成器 →**

只要點選幾個選項，就能立即為你寫出一段精煉、可直接使用的角色提示詞！

免費・直接在瀏覽器中開啟

---

## 2️⃣ AI 影片主提示詞（複製貼上即可使用）

💡 **使用方式：** 將兩個佔位符 `[CHARACTER]`（角色）與 `[PASTE YOUR DIALOGUE]`（貼上你的對白）替換掉，接著在 Google Flow 中選取「代理模式（Agent Mode）」後，將整段貼上。其餘部分保持原樣即可。

> **注意：** 以下主提示詞需完整複製貼上至 Google Flow 中使用，內容維持原文英文，以確保工具正確辨識指令。

```text
@[CHARACTER] Speaks the following dialogue exactly as written. Do not omit, paraphrase, reorder, or add any words. : [PASTE YOUR DIALOGUE HERE]

## Instructions
- Dialogue Delivery Style: [e.g. warm and conversational]
- Split the dialogue into consecutive 10-second video segments while preserving every word in the exact order.
- Do not shorten, paraphrase, skip, or modify any part of the dialogue.
- Generate all segments as one seamless continuous performance.
- Use natural lip sync, realistic facial expressions, eye contact, blinking, subtle breathing, and expressive but restrained hand gestures.
- Ensure every segment connects seamlessly with the next.
- No background music.

## Visual Consistency
Maintain absolute consistency with the reference image. Keep the subject's appearance, clothing, hairstyle, facial features, lighting, environment, furniture, props, and overall composition identical across every segment.

## Camera Direction
Use exactly two static shots in each 10-second segment. Each shot may use a different camera angle and/or shot size, but the camera must remain locked off with no pans, tilts, handheld movement, tracking shots, or dolly movement. Choose any two combinations from the following:

Camera Angles
- Front-facing
- Left three-quarter
- Slightly elevated front-facing
- High three-quarter from above

Shot Sizes
- Medium shot
- Medium close-up
- Close-up

Use a single clean cut between the two shots while maintaining uninterrupted dialogue, timing, facial expressions, hand gestures, and visual continuity.
```

**中文參考翻譯（僅供理解，實際使用請貼上方英文原文）：**

`@[角色]` 逐字說出以下對白，不得省略、改寫、調換順序或增加任何字詞：`[貼上你的對白]`

**指示（Instructions）**
- 對白表達風格（Dialogue Delivery Style）：〔例如：溫暖且口語化〕
- 將對白拆分為連續的 10 秒影片片段，並完整保留每個字詞的原始順序。
- 不得縮短、改寫、跳過或修改對白的任何部分。
- 將所有片段生成為一段無縫連貫的演出。
- 使用自然的嘴型同步（lip sync）、真實的臉部表情、眼神接觸、眨眼、細微的呼吸動作，以及有表現力但克制的手勢。
- 確保每個片段之間無縫銜接。
- 不加背景音樂。

**視覺一致性（Visual Consistency）**
與參考圖片保持絕對一致。角色的外觀、服裝、髮型、五官、光線、環境、家具、道具與整體構圖，在每個片段中都必須完全相同。

**運鏡指示（Camera Direction）**
每個 10 秒片段須使用剛好兩個靜態鏡頭。每個鏡頭可使用不同的攝影角度與／或景別，但鏡頭必須固定不動，不得有平移、傾斜、手持晃動、跟拍或推軌移動。從以下選項中任選兩種組合：

攝影角度（Camera Angles）
- 正面
- 左側四分之三側面
- 略微仰角正面
- 高角度四分之三俯視

景別（Shot Sizes）
- 中景
- 中特寫
- 特寫

兩個鏡頭之間使用一次乾淨的轉場切換，並維持對白不中斷、節奏、臉部表情、手勢與視覺連貫性。

---

## 🛠️ 我使用的工具

| 工具 | 用途 | 連結 |
| --- | --- | --- |
| Google Flow | 生成並動畫化你的 AI 虛擬人像影片 | 開啟 |
| ChatGPT | 生成場景描述與替代圖像 | 開啟 |
| ElevenLabs | 為角色提供自然的 AI 配音 | 開啟 |
| Higgsfield | 透過人口統計預設值建立角色圖像 | 開啟 |
| Topaz Bloom | 圖像放大與畫質強化 | 開啟 |

---

## 💡 專業提示

💡

生成多個角色變化版本。第一個結果不一定是最好的。

清楚描述表達風格。語氣與節奏對最終演出效果有很大影響。

在剪輯前先重新生成。這通常比在後期修正錯誤更快。

---

## 保持聯繫

✉️

當我發布新的 AI 影片製作資源時，會不定期收到更新通知。絕不濫發垃圾郵件。

在此註冊

---

*原文來源：[AI Avatar Starter Kit | Build Your Own AI Avatar](https://genaikeera.notion.site/ai-avatar-starter-kit)*