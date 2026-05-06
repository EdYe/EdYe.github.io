---
title: 'MarkItDown：微軟最被低估的 Agent 工具，25 倍壓縮辦公室檔案'
date: 2026-05-06
image: /images/AI筆記/markitdown-hidden-agent-tool.jpeg
category: AI筆記
tags: [MarkItDown, 文件格式轉換, AI Agent知識庫, Markdown通用語, 資料蒸餾]
description: 'MarkItDown 是微軟開源的檔案轉換工具，能將 PDF、Excel、PowerPoint、Word、圖片等各種格式一鍵轉為 Markdown 文件，解決 AI Agent 無法解析辦公室二進位檔案的'
quote: '你的 Agent 不是因為模型不夠強而失敗，而是因為它讀不懂你的檔案。'
action: 'M-F-V 法則：用 MarkItDown 將工作資料夾 Markdown 化（Markdown化）→ 建立統一知識庫（Flatten整平）→ 生成 Force-Directed Graph HTML 可視化（Visualize）。'
source_has_timestamps: true
---
# Microsoft's HIDDEN Agent Tool — MarkItDown 完整筆記

**頻道：** Jay E | RoboNuggets｜**發布日：** 2025年5月3日｜**片長：** 10分02秒

***

## [核心摘要]

**MarkItDown** 是微軟開源的檔案轉換工具，能將 PDF、Excel、PowerPoint、Word、圖片等各種格式一鍵轉為 **Markdown 文件**，解決 AI Agent 無法解析辦公室二進位檔案的根本痛點。它已在 GitHub 上獲得超過 10 萬顆星，是目前 Agent 知識庫建構中最被低估的實用工具之一。

***

## [詳細重點整理]

### 1. 為什麼 Markdown 是 AI Agent 的通用語言 [00:21]
Markdown 在機器可讀性與人類閱讀性之間取得完美平衡。Andrej Karpathy（前 Tesla AI 主管、OpenAI 共同創辦人）在 Sequoia 火爐談話中明確建議：**優先安裝 `.md` 技能，而非 `.sh` 腳本**，並呼籲用 Markdown 建立 LLM 知識庫，該推文已獲 2,000 萬次瀏覽。

> **關鍵概念：Markdown 通用語（Lingua Franca）** — 任何 LLM 與 Agent 都能解析，同時對人類仍保持可讀性的格式標準。

***

### 2. 企業現實：多數檔案不是 Markdown [01:17]
現實工作環境中，企業檔案以 Excel、PowerPoint、PDF、JPEG 等格式為主，這些**辦公室二進位格式**讓 AI Agent 無法直接讀取，形成**資訊檢索關鍵阻礙**。

> **關鍵概念：辦公室二進位格式阻礙（Office Binary Blocker）** — Agent 遇到非文字格式時，會明確回報無法分析，導致整個工作流中斷。

***

### 3. MarkItDown 的三大核心優勢 [02:36]
- **可搜尋知識庫**：所有文件統一轉為 Markdown 後，即可建立公司內部第二大腦或客戶資料庫
- **大幅壓縮檔案大小**：實測將 ~1,000 KB 的辦公室檔案壓縮至約 40 KB，達到 **25 倍縮減比**
- **加速資訊檢索**：相同問題下，讀取 Markdown 的 Agent 能即時完成分析並給出建議，而讀取原始 Office 檔案的 Agent 完全無法作答

> **關鍵概念：資料蒸餾（Data Distillation）** — 將多格式、高體積的原始資料壓縮為 Agent 可消化的輕量知識單元。

***

### 4. 實際操作示範 [04:51]
1. 複製 GitHub 連結（`github.com/microsoft/markitdown`）交給 Agent
2. 告訴 Agent 指定資料夾路徑，下達「用 MarkItDown 把這些檔案全部展平為 Markdown」
3. 完成後再用單一 prompt 建立 **Obsidian 風格的力導向圖（Force-Directed Graph）**，以 HTML 互動頁面可視化整個知識庫結構

> **關鍵概念：知識庫可視化（Knowledge Graph Rendering）** — 以 Obsidian 介面概念，將 Markdown 節點以泡泡大小代表內容量，點擊可直接開啟原始 MD 檔案。

***

### 5. 整合 Karpathy LLM Wiki 原則 [08:34]
將 LLM Wiki 知識庫 Markdown URL 直接交給 Agent，要求它對應個人或公司的現況提出整合建議。Agent 會閱讀整份文件並給出個人化執行路徑（示範中顯示該用戶已完成約 60% 的知識庫建構）。

> **關鍵概念：上下文個人化（Contextual Personalization）** — 用 Agent 本身對使用者的了解，將通用框架轉化為量身定制的行動計畫。

***

## [技術/數據對比]

| 指標 | Office 原始檔案 | Markdown 轉換後 |
|------|----------------|-----------------|
| 檔案總大小 | ~1,000 KB | ~40 KB（**縮小 25 倍**） |
| Agent 可讀性 | ❌ 二進位格式無法解析 | ✅ 完整解析 |
| 資訊檢索速度 | ❌ 分析失敗 | ✅ 即時回答並給建議 |
| 可搜尋性 | 低 | 高 |
| 費用 | — | **免費、開源** |

***

## [結論與行動建議]

**💡 啟發金句：**
> 「你的 Agent 不是因為模型不夠強而失敗，而是因為它讀不懂你的檔案。」

**🎯 具體行動建議 — M-F-V 法則：**
- **M（Markdown化）**：用 MarkItDown 將現有工作資料夾全部轉為 `.md`
- **F（Flatten整平）**：建立統一 Markdown 知識庫，讓 Agent 一次讀取所有資訊
- **V（Visualize可視化）**：生成 Force-Directed Graph HTML 頁面，即時掌握知識庫全貌

**🏠 生活實踐建議：**
- **個人用戶**：把你的筆記、會議記錄、研究 PDF 全部批次轉為 Markdown，打造個人第二大腦
- **PM/架構師**：將客戶需求文件、規格書、歷史 Excel 報告轉為 Markdown，建立可被 Agent 搜尋的專案知識庫
- **AI 應用開發者**：在 n8n / Make 工作流中加入 MarkItDown 節點，作為所有文件進入 Agent 前的「前處理閘道」

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/CRTxKRRZqeo
- 🛠️ Microsoft MarkItDown GitHub：https://github.com/microsoft/markitdown
