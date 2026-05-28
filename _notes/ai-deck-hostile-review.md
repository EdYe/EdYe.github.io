---
title: '用 AI 建簡報，再派另一個 AI 來攻擊它'
date: 2026-05-28
image: /images/AI筆記/ai-deck-hostile-review.jpeg
category: AI筆記
tags: [工作流重構, 財務模型風險, 四階段工作流, 任務風險梯度, RALPH迴圈]
description: '用 AI 建立 Office 文件已非難事，但光靠 Prompt 得到的輸出不等於可信賴的成果。本影片揭示一個關鍵痛點：AI 生成的文件「看起來完成」遠早於「實際可信賴」，並提出以「來源管控→結構規格→分層創建→敵對審查'
quote: 'A prompt asks for an output. A workflow defines the stages the output has to pass through before it can be trusted.'
action: '下次建立重要簡報前，先寫出敘事脊幹，再開啟 AI 工具；驗收前執行一次「敵對審查 Prompt」只找問題不修復'
source_has_timestamps: true
---
# 🎯 [核心摘要]

用 AI 建立 Office 文件（PowerPoint、Excel）已非難事，但**光靠 Prompt 得到的輸出不等於可信賴的成果**。本影片揭示一個關鍵痛點：AI 生成的文件「看起來完成」遠早於「實際可信賴」，並提出以「來源管控 → 結構規格 → 分層創建 → 敵對審查」四階段工作流取代單一 Prompt，確保知識工作的品質與可驗證性。

***

# [詳細重點整理]

## 1. 超越單一資產思維 [00:00]

AI 工具已可同時草擬八份文件，但能力的提升也帶來更大的錯誤風險。 核心心態轉變：**不是把 AI「附加」到工作流程，而是讓 Agent 成為工作流程的核心**，並圍繞它重新設計整個流程。

**關鍵概念：** **以 Agent 為核心的工作流重構（Agentic Workflow Redesign）**

***

## 2. AI 文件的核心風險 [07:00]

真實案例：一份看起來完整的財務模型，收入增長列的公式錯誤卻被複製到所有未來年份，Excel 沒有顯示任何錯誤，估值輸出依然「看起來正確」。 **外觀完成 ≠ 邏輯正確**，這才是 AI 辦公文件最危險的陷阱。

**關鍵概念：** **財務模型偽裝（Financial Model in Costume）**

***

## 3. 四階段可信賴工作流 [05:25]

四個必經階段，缺一不可 ：

| 階段 | 內容 |
|---|---|
| **① 來源準備（Source Prep）** | 先建立來源清單（索引），標明每份資料的所有者、日期、狀態（現行/已過期/估算），並移除敏感資訊 |
| **② 結構規格（Structure Spec）** | 建立文件藍圖。PowerPoint 需有敘事脊幹（Narrative Spine）＋每張投影片的論點標題＋來源 ID；Excel 需有分頁架構＋計算流程 |
| **③ 分層創建（Layered Creation）** | PPT：先做故事板（論點+證據），再渲染視覺；Excel：第一層載入原始資料、第二層建立假設與計算邏輯、第三層產出彙總視圖 |
| **④ 敵對審查（Hostile Review）** | 用另一個 AI 模型以「懷疑一切」的角色審查，**只找問題，不修復**，列出所有無來源聲明、無追蹤數據的圖表、跨欄不一致的公式 |

***

## 4. 任務風險梯度 [10:07]

不同任務的 AI 風險等級不同，應對應不同的人工審查力度 ：

- **低風險：** 格式排版、圖表草稿、措辭一致性
- **中風險：** 來源引用、數據萃取
- **高風險：** 數值綜合計算、財務計算、法規合規語言、**將呈報高層決策的關鍵主張**

**關鍵概念：** **任務風險梯度（Task Risk Gradient）**

***

## 5. RALPH 迴圈：Codex × Opus 4.7 [14:30]

作者的個人工作流：用 **Codex 建立 Excel/PowerPoint 文件** → 交給 **Claude Opus 4.7 進行敵對審查** → 生成詳細修改清單 → 回傳 Codex 修正 → 再交給 Opus 確認 → 重複直到高品質。 最後加入語言檢查步驟，讓 Opus 清除文件中的 LLM 用語（如「Absolutely right」等）並確保符合人類閱讀習慣。

**關鍵概念：** **RALPH 迴圈（Reinforced Autonomous Loop for High-quality output）**

***

## 6. 為何需要自己建立這套系統 [17:18]

知識工作本質上**高度依賴領域知識（Domain Knowledge）**，無法被泛化成一個按鈕解決方案。 就像路克天行者必須自己打造光劍才能成為絕地武士，深度知識工作者必須理解系統如何運作，才能掌控它。

**關鍵概念：** **知識工作的情境依賴性（Contingent Domain Knowledge）**

***

# [結論與行動建議]

**啟發金句：**
> **「A prompt asks for an output. A workflow defines the stages the output has to pass through before it can be trusted.」**
> 一個 Prompt 只是要求產出；一個工作流定義的是產出在被信賴之前必須經歷的每個關卡。

**具體行動法則：S-S-C-V 四層工作流法則**
> **Sources（來源）→ Structure（結構）→ Create（創建）→ Verify（驗證）**

**生活實踐建議：**
- **下次建立重要簡報前**，先寫出敘事脊幹（受眾是誰？他們需要做什麼決策？需要相信什麼才能做決策？），再開啟 AI 工具
- **建立 Excel 財務模型時**，用三層分頁設計：原始資料 → 假設與計算 → 彙總輸出，並設定「如果改一個假設，相關輸出會正確改變嗎？」作為驗收標準
- **驗收任何 AI 文件前**，執行一次「敵對審查 Prompt」：*「以懷疑一切的審查者身份閱讀此文件，找出所有無來源聲明、無可追溯數據的圖表、跨欄不一致的公式——只列問題，不要修復」*

***

# [參考連結]

- 📺 原始影片：https://youtu.be/MFzxIT88zfg
- 📝 Truth Layer Guide + Prompts（Substack）：https://natesnewsletter.substack.com/p/ai-office-files-verify-workflow
