---
title: '刪除 CLAUDE.md：提示詞死重量與過剩'
date: 2026-07-28
image: /images/AI筆記/delete-your-claude-md.jpg
category: AI筆記
tags: [系統提示詞, CLAUDE.md, 產品過剩, 驗證優先, 例行任務自動化]
description: 'Claude Code 創造者 Boris Cherny 分享七個關鍵洞察：隨著模型智能提升，過去用來補償模型缺陷的系統提示詞已成為「死重量」，Anthropic 內部刪除了 80% 系統提示詞，模型反而更聰明。'
quote: '💡每一行提示詞都有租金要付——不貢獻價值，就刪除。'
action: '🎯D-R-V 法則：每六個月刪除 CLAUDE.md/Skills/Hooks 僅在犯錯時逐行加回、交付前先建立驗證器、以實證心態迭代任務。'
source_has_timestamps: true
---
# [核心摘要]

Claude Code 創造者 Boris Cherny 在 Y Combinator Startup School 2026 分享了七個關鍵洞察，核心主張是：**隨著模型智能提升，過去用來補償模型缺陷的系統提示詞已成為「死重量」**。Anthropic 內部刪除了 80% 的 Claude Code 系統提示詞，模型反而更聰明；Boris 公開建議使用者每六個月刪除 CLAUDE.md，僅在模型反覆犯錯時才逐行加回。此外，他揭示了「產品過剩」（Product Overhang）概念——模型能力與產品發揮之間的巨大鴻溝，正是下一個獨角獸的機會。Bun 的 53.5 萬行 Zig 程式碼在 11 天內被重寫為 Rust，驗證了「測試套件即裁判」的範式 。 [youtube](https://www.youtube.com/)

***

# [詳細重點整理]

### 1. 刪除 80% 系統提示詞 [01:16]

Opus 5 發布後，Anthropic 團隊刪除了 Claude Code 自身系統提示詞的 80%。原因是過去的提示詞在「修正」舊模型本應知道但不會做的行為，而 Opus 5 已具備這些能力，這些指令反而成為干擾。Boris 提供兩個工具讓使用者自行驗證：
- `claude --system-prompt`：可完全替換系統提示詞
- `CLAUDE_CODE_SIMPLE=1` 環境變數：刪除所有內建提示詞（含工具提示詞），Anthropic 內部用作消融實驗（ablation），結果顯示模型在無提示詞狀態下**略為更聰明**

關鍵概念：**提示詞租金（Prompt Rent）**——每一行提示詞在每一輪對話都會被讀取，每行指令都有「租金要付」，若不貢獻價值就應刪除 。 [youtube](https://www.youtube.com/)

### 2. 每六個月刪除你的 CLAUDE.md [03:41]

Boris 對所有 AI 產品開發者的明確建議：每六個月刪除 CLAUDE.md、Skills 與 Hooks，觀察模型在「淨空」狀態下的表現。重建方法是：
- 先刪除一切，直接使用
- 僅當模型在同一問題上反覆犯錯時，才加回一行指令
- 將每次提示詞調整視為「重新認識一個新生物」，而非「維護舊機器」

從 Sonnet 3.5 時期累積至今的設定檔，不是記憶，而是**已不存在模型的疤痕組織（Scar Tissue）** 。 [youtube](https://www.youtube.com/)

### 3. 產品過剩：Claude Code 的誕生 [05:10]

Boris 將 Claude Code 的起源歸納為可重複的公式——**產品過剩（Product Overhang）**：模型已有能力與產品所釋放能力之間的差距。兩年前，模型已能撰寫整個檔案，但所有產品仍停留在自動補全（autocomplete）層級。Claude Code 就是將最薄的框架放入這個缺口。Boris 強調，今日模型的過剩比當年更大、尚未被收割、且具商業價值——下一個 Claude Code 正在那個缺口中等待 。 [youtube](https://www.youtube.com/)

### 4. 11 天 Bun 重寫：Zig → Rust [07:07]

工程師 Jared 對 Bun（Anthropic 收購的 JavaScript 執行環境）發起挑戰，讓模型將整個程式碼庫從 Zig 重寫為 Rust。關鍵條件是 Bun 擁有龐大的測試套件（Bun 與 Node.js 皆有），能在每一步驟驗證模型是否正確。最終以一個動態工作流（Dynamic Workflow）執行，64 個 Claude 實例並行運作 11 天完成，成本約 16.5 萬美元。此成果已在生產環境中使用，Bun 倉庫現以 Rust 為主要語言。值得注意的是，過程中有人類方向引導（steering），且 Claude 審查器在合併前抓到三個關鍵 Bug，Zig 創造者公開反對此作法 。 [youtube](https://www.youtube.com/)

關鍵概念：**測試套件即裁判（Test Suite as Referee）**——測試套件在每一步驟告知模型是否正確，是使大規模自動化重寫成為可能的基礎設施。

### 5. 事實查核 [09:00]

影片對最瘋狂的聲稱進行了事實查核，所有來源皆公開：
- Bun 重寫：[bun.com/blog/bun-in-rust](https://bun.com/blog/bun-in-rust)
- Anthropic 收購 Bun：[anthropic.com/news](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone)
- Opus 5 ARC-3 成績：[arcprize.org/results](https://arcprize.org/results/anthropic-claude-opus-5)
- Boris 2004 年 TI-83 指南：[ticalc.org](https://www.ticalc.org/programming/columns/83plus-bas/cherny/) [youtube](https://www.youtube.com/)

### 6. 三句話提示詞：運行兩週仍未停止 [10:18]

Boris 在 Slack 中使用 Claude Tag（Claude 在 Slack 中運行的產品）發起一個任務，核心提示詞僅三句：
1. 將 Electron 桌面應用重寫為 Swift
2. 在 Mac 虛擬機上執行 Electron 應用，截圖，與 Swift 版本逐像素比對
3. 不要停止，直到完成

此任務已連續運行超過兩週（14-15 天），Claude 甚至自主開設 Slack 頻道直播進度並附截圖。Boris 認為當前核心技能已非提示詞工程，而是兩件事：**給模型一個稍微太難的任務**，以及**讓模型能驗證自己的工作**。頂尖 1% 使用者的共同特徵不是秘密提示詞，而是在交付任務前先建立驗證器（Verifier）。 [youtube](https://www.youtube.com/)

關鍵概念：**驗證優先（Verification-First）**——模型做工作，但驗證器是你的工作。

### 7. Claude 維護自己的程式碼庫 [13:06]

Anthropic 讓 Claude 在排程上維護自身程式碼庫，涵蓋 CLI、iOS、Android 與桌面應用。目前每天有 20-30 個例行任務（Routine）在所有程式碼庫上運行，有時涉及數百甚至數千個代理。具體範例包括：
- **清理死碼（Dead Code Cleanup）**：每天使用靜態與動態分析尋找死碼，自動發起 PR 刪除
- **抽象警察（Abstraction Police）**：每天跨程式碼庫尋找近似重複的抽象，自動統一為單一抽象
- 其他：發布命中率 100% 的實驗、在覆蓋率不足處補寫測試、刪除無價值測試

每個 Routine 都是一句話提示詞加上定時器。實作門檻極低——Cron job 加一行提示詞即可在今晚自行設定 。 [youtube](https://www.youtube.com/)

關鍵概念：**例行任務自動化（Routine Automation）**——護城河不在於 Routine 本身，而在於判斷什麼值得重複。

### 8. 實證心態 + TI-83 溯源 [15:36]

Boris 對「如何成為頂尖使用者」的回答：不要聽 LinkedIn 影響者，不要讀 Twitter。核心技能是**實證的（Empirical）**：忘記過去模型學到的東西、忘記課堂上的電腦科學理論，直接給模型任務，觀察它在哪裡掙扎，然後調整。關鍵特質是能**放下先驗假設**（letting go of priors），對曾失敗的方法保持重新嘗試的開放態度。20 年資歷的工程師最難適應，因為「過度規範化（Over-specifying）」過去正是他們的職責 。 [youtube](https://www.youtube.com/)

***

# [技術/數據對比]

| 項目 | 數據 |
|------|------|
| 系統提示詞刪除比例 | 80%（Opus 5 發布後） |
| Bun 程式碼轉換量 | 535,000 行 Zig → Rust |
| Bun 重寫耗時 | 11 天 |
| Bun 重寫並行實例數 | 64 個 Claude 實例 |
| Bun 重寫成本 | 約 165,000 美元（API 價格） |
| 傳統人工重寫預估時間 | 超過 1 年 |
| 三句話提示詞運行時間 | 超過 2 週（14-15 天） |
| 每日例行任務數量 | 20-30 個 |
| 例行任務每日代理數 | 數百至數千個 |
| Opus 5 ARC-3 基準測試成績 | 30%（前最佳 <8%） |

***

# [結論與行動建議]

> **啟發金句**：「每一行提示詞都有租金要付——不貢獻價值，就刪除。」

**具體行動建議 — D-R-V 法則：**
- **Delete（刪除）**：每六個月刪除 CLAUDE.md、Skills、Hooks，僅在模型反覆犯錯時逐行加回
- **Referee（裁判）**：在交付任務前先建立驗證機制（測試套件、截圖比對、覆蓋率檢查）
- **Verify（驗證）**：以實證心態迭代——給模型一個稍微太難的任務，觀察掙扎點，調整，重複

**生活實踐建議：**
- 在自己的程式碼庫中設定一個 Cron job，每天自動執行「死碼清理」或「測試覆蓋率補強」的一句話提示詞例行任務
- 使用 `CLAUDE_CODE_SIMPLE=1` 環境變數測試專案在無系統提示詞下的表現，作為提示詞價值的消融實驗
- 將任何重複性的程式碼維護工作（如統一抽象、刪除無用測試）轉化為定時 Routine，讓 Claude 成為 7×24 小時的程式碼維護工程師

***

# [參考連結]

- 原始 YouTube 影片：[https://youtu.be/Egd65CLmb6w](https://youtu.be/Egd65CLmb6w)
- YC 完整訪談 "Boris Cherny: Building Claude Code"：[https://www.youtube.com/watch?v=qyPCVqFUyDo](https://www.youtube.com/watch?v=qyPCVqFUyDo)
- Bun 重寫技術部落格：[https://bun.com/blog/bun-in-rust](https://bun.com/blog/bun-in-rust)
- Anthropic 收購 Bun 公告：[https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone)
- Opus 5 ARC-3 成績：[https://arcprize.org/results/anthropic-claude-opus-5](https://arcprize.org/results/anthropic-claude-opus-5)
