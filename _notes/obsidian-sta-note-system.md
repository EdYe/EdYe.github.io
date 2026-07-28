---
title: 'Obsidian STA 筆記法：打造學術知識庫'
date: 2026-07-28
image: /images/影片筆記/obsidian-sta-note-system.jpg
category: 影片筆記
tags: [STA筆記系統, 原子句, 雙重連結驗證, 結構化查詢, 知識組織策略]
description: '本影片展示了如何以 Obsidian 為工具，仿照 Wikipedia 的組織邏輯，建立一套可擴展的個人學術知識庫。核心方法論為 STA 筆記系統。'
quote: '💡「原子句會替你寫論文——因為寫作的本質，就是將已知斷言按邏輯順序組合。」'
action: '🎯依 S-T-A 法則：Source 筆記存來源不可改、Topic 筆記擷取斷言附雙重連結、Argument 筆記獨立存放個人推想。'
source_has_timestamps: true
---
## [核心摘要]

本影片展示了如何以 Obsidian 為工具，仿照 Wikipedia 的組織邏輯，建立一套可擴展的個人學術知識庫。核心方法論為 **STA 筆記系統**（Source-Topic-Argument），將筆記分為來源筆記、主題筆記與論證筆記三類，解決了傳統「摘要式筆記」無法規模化與無法重用於學術寫作的痛點。講者 Ilya Shabanov 憑此系統，提前 5 個月完成 PhD 並發表四篇第一作者論文 。 [youtube](https://www.youtube.com/)

***

## [詳細重點整理]

### 1. 為何需要資訊策略 [00:00]

一項 Nature 研究指出，約 78% 的博士生每週工作超過 40 小時，意即多數人靠「磨」的方式完成學位。引用孫子兵法「戰術無戰略，乃敗前之噪音」，強調 PhD 的本質是知識的競爭，因此需要一套**知識組織策略**，而非埋頭苦幹 。 [youtube](https://www.youtube.com/)

**關鍵概念：知識組織策略（Knowledge Organization Strategy）**

***

### 2. 以 Wikipedia 為藍圖 [02:15]

Wikipedia 沒有任何資料夾結構，而是以概念為核心、透過連結互相串聯。每一項斷言（claim）都能追溯到具體參考來源，將推測與事實分離。Wikipedia 刻意不收錄論文摘要，因為「摘要即壓縮」，壓縮後的知識難以檢索。其兩大組織方法為：**連結**（串接概念）與**參考文獻**（區分推測與事實）。 [youtube](https://www.youtube.com/)

**關鍵概念：連結式知識架構（Linked Knowledge Architecture）**

***

### 3. Obsidian 基礎操作 [05:23]

Obsidian 充當個人 Wikipedia 的「瀏覽器」，而筆記本身是硬碟上的純文字檔案（Markdown）。這確保資料完全本地儲存，即便軟體收費也能存取所有內容——這也是講者放棄 Notion 和 Evernote 的原因。核心操作包括 ： [youtube](https://www.youtube.com/)

- 安裝 **Editing Toolbar** 外掛，免去手動輸入 Markdown 語法
- 使用 **Callouts**（呼叫框）整理定義、摘要、AI 生成內容，可摺疊隱藏
- 以 `[[]]` 建立筆記間連結，支援模糊搜尋
- 在連結前加 `!` 可嵌入圖片或整篇筆記內容
- 圖片拖入後自動複製進 Vault，確保離線可用

**關鍵概念：本地知識庫（Local Knowledge Vault）**

***

### 4. PDF 整合與資料夾結構 [~08:00]

建立三個資料夾：**Notes**（主題筆記）、**Sources**（來源筆記與 PDF）、**Support**（圖片與附件）。在來源筆記中以 `---` 開啟 Properties 面板，將 author、journal、title 等欄位設為連結（如 `[[PNAS]]`），點擊即可建立對應筆記。閱讀 PDF 時以分割視窗並排：左側筆記、右側 PDF，避免嵌入式 PDF 干擾捲動 。 [youtube](https://www.youtube.com/)

**關鍵概念：中繼資料連結（Metadata Linking）**

***

### 5. Obsidian Bases：替代 Zotero 的利器 [~16:30]

**Bases** 是 Obsidian 最被低估的功能，運作邏輽類似 Excel：行是筆記、列是屬性，可新增篩選器。例如建立一個 `papers` Base，篩選 `sources` 資料夾內所有檔案，顯示 author、journal、title 等欄位。進階用法包括按評分排序論文、建立閱讀清單、按年份分組。講者認為 Bases 的彈性與速度遠超 Zotero 的笨重介面，可完全取代後者 。 [youtube](https://www.youtube.com/)

**關鍵概念：結構化查詢（Structured Query）**

***

### 6. STA 筆記系統 [21:01]

最大挑戰不是技術，而是**心態轉變**：從「按順序為單篇論文做摘要」轉為「按主題擷取斷言」。摘要如同行李箱——壓縮完美但難以尋找特定物品；你需要的是衣櫃——分類清楚、隨取即用。系統由三類筆記構成 ： [youtube](https://www.youtube.com/)

| 筆記類型 | 內容 | 可變性 | 角色 |
|---------|------|-------|------|
| **Source（來源筆記）** | 他人所言、PDF、原始資料 | 不可變，寫完即存 | 錨點與驗證入口 |
| **Topic（主題筆記）** | 從來源擷取的斷言，每條連回來源筆記 | 可解讀但不可推測 | 迷你文獻回顧 |
| **Argument（論證筆記）** | 自己的想法、問題、假設 | 純推測，完全個人 | 思考與創意的載體 |

**關鍵概念：STA 筆記分類法（Source-Topic-Argument Classification）**

***

### 7. 擷取斷言與反向連結 [~23:00]

閱讀論文時，將每個 claim 壓縮為一句話放入對應的主題筆記，並附上來源連結（如 `[[Vanvic 2020]]`）。主題筆記中的每條斷言都像**原子句**——簡潔、完整、不需額外補充。隨著累積，主題筆記自動形成該領域的迷你文獻回顧；來源筆記則透過反向連結（backlinks）顯示它涉及哪些主題。雙向連結讓知識網絡自然生長 。 [youtube](https://www.youtube.com/)

**關鍵概念：原子句（Atomic Sentences）**

***

### 8. PDF 雙重連結驗證 [~27:00]

每條斷言配備兩個連結：一個指向 PDF 中的具體句子（右鍵 → Copy link to selection），用於快速核實；另一個指向來源筆記本身，用於連接知識網絡。這解決了一個常見錯誤：論文引言中引用的 claim 其實來自該論文的參考文獻第 24、25 號，而非論文本身。PDF 連結讓你立即跳回原文驗證。**PDF++** 外掛可自動化此流程，並在 PDF 上顯示高亮標記 。 [youtube](https://www.youtube.com/)

**關鍵概念：雙重連結驗證（Dual-Link Verification）**

***

### 9. Web Clipper 與非 PDF 來源 [~32:00]

對於網頁等非 PDF 來源，使用 **Obsidian Web Clipper** 擴充功能匯入完整頁面（含圖片、文字、連結）。來源筆記的鐵律：**必須連結到原始素材**（PDF、文字或網頁），這是唯一能核實主題筆記中斷言真偽的方式。講者強調，隨著你作為研究者的成長，你會重新審視同一篇論文並發現新的意義，因此原始素材的留存至關重要 。 [youtube](https://www.youtube.com/)

**關鍵概念：原始素材溯源（Raw Material Traceability）**

***

### 10. 原子句拼圖與 AI 寫作 [~33:00]

主題筆記中的原子句如同拼圖碎片，可手動組合成段落，也可透過 AI（加入適當 prompt）自動拼接成學術段落初稿，且自動包含正確的參考文獻連結。結果雖不完美，但已是非常好的初稿。長期而言，**原子句會替你寫論文**——因為寫作的本質就是將已知斷言按邏輯順序組合 。 [youtube](https://www.youtube.com/)

**關鍵概念：知識積木（Knowledge Building Blocks）**

***

### 11. 論證筆記 [~35:00]

論證筆記（Argument Notes）存放純粹的個人推測、問題、假設與想法，與來源和主題筆記嚴格分離。範例包括：與學界人士的 email 討論串、論文大綱草稿、研究問題等。這種分離確保你永遠清楚「哪些是他人所言、哪些是自己所想」，是嚴謹研究的基礎 。 [youtube](https://www.youtube.com/)

**關鍵概念：推測隔離（Speculation Isolation）**

***

### 12. 即時示範 [38:15]

講者實際示範以 STA 系統閱讀一篇論文並擷取斷言的完整流程，展示從 PDF 高亮 → 擷取斷言 → 連結至主題筆記 → 反向連結自動生成的全鏈路操作 。 [youtube](https://www.youtube.com/)

***

### 13. 結論與新想法生成 [49:06]

系統的最終價值在於：當主題筆記累積足夠的原子句後，新的研究想法會自然從斷言之間的關聯中湧現。講者另外示範如何利用 Obsidian Bases 的交叉篩選功能，發現隱藏在筆記中的新想法連結 。 [youtube](https://www.youtube.com/)

***

## [結論與行動建議]

> **啟發金句：「原子句會替你寫論文——因為寫作的本質，就是將已知斷言按邏輯順序組合。」**

**具體行動法則：S-T-A 法則**
- **S（Source）**：每篇論文建一個來源筆記，連結 PDF，不可修改
- **T（Topic）**：從來源中擷取斷言放入主題筆記，每條附雙重連結（PDF + 來源筆記）
- **A（Argument）**：自己的所有想法、問題、假設獨立存放，與前兩者嚴格分離

**生活實踐建議**
以 AI 產品經理的工作為例：在評估新技術或競品時，可將每篇研究報告或產品分析建立為 Source 筆記，從中擷取關鍵發現放入 Topic 筆記（如「LLM 成本趨勢」「多模態能力對比」），再將自己的產品策略判斷寫入 Argument 筆記。當需要撰寫技術評估報告或產品 Roadmap 時，直接從 Topic 筆記中調取原子句拼接成段落初稿，大幅縮短寫作週期並確保每個論點都有可追溯的來源。

***

## [參考連結]

- 原始影片：[https://youtu.be/S_-uD3GtFno](https://youtu.be/S_-uD3GtFno)
- Obsidian Bases 教學：[https://effortlessacademic.com/using-obsidian-bases-for-academic-note-taking/](https://effortlessacademic.com/using-obsidian-bases-for-academic-note-taking/)
- PDF 處理教學：[https://effortlessacademic.com/working-with-pdfs-in-obsidian-pdf-plugin-and-full-text-search/](https://effortlessacademic.com/working-with-pdfs-in-obsidian-pdf-plugin-and-full-text-search/)
- Web Clipper 教學：[https://effortlessacademic.com/capture-any-content-to-obsidian-with-webclipper-ai/](https://effortlessacademic.com/capture-any-content-to-obsidian-with-webclipper-ai/)
- 15 Best Obsidian Plugins for Academics：[https://effortlessacademic.com/best-obsidian-plugins-for-academics/](https://effortlessacademic.com/best-obsidian-plugins-for-academics/)
