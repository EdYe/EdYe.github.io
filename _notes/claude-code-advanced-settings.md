---
title: 'Claude Code 十二個進階設定技巧'
date: 2026-03-26
image: /images/AI筆記/claude-code-advanced-settings.jpg
category: AI筆記
tags: [Claude Code, 進階設定, 子代理, 上下文管理, Hook]
description: '本影片詳細介紹了 12 個隱藏在 Claude Code 設定文件與環境變數中的進階技巧，旨在幫助開發者突破預設限制，提升 AI Agent 的執行效率與處理能力'
quote: '大多數你在使用 Claude Code 時遇到的問題，其實都已經有內建的修復方案，只是它們被埋在很少人討論的設定檔裡。'
action: '開啟 .claude/settings.json，優先調整 cleanupPeriodDays 與終端輸出限制'
source_has_timestamps: true
---

這是一份為您整理的 Claude Code 高階設定指南筆記：

### **核心摘要**
本影片詳細介紹了 12 個隱藏在 **Claude Code** 設定文件與環境變數中的進階技巧，旨在幫助開發者突破預設限制，提升 AI Agent 的執行效率、私隱性與大型專案處理能力。

---

### **詳細重點整理**

#### **1. 突破數據保留與上下文限制**
* **延長對話記憶**：預設情況下，Claude 只保留一個月的對話紀錄。透過修改 `settings.json` 中的 `cleanupPeriodDays` 欄位（例如設為 `365`），可保留一整年的對話內容，方便長期專案追蹤。[[01:04](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=64)]
* **增加終端輸出讀取量**：Claude 預設僅讀取 3 萬字元的終端輸出。在現今 100 萬 Token 的模型時代，建議將此限制調升至 `150,000` 字元，避免編譯日誌或測試結果因過長而被截斷。[[02:56](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=176)]
* **大型檔案完整讀取技巧**：Claude 即使有大上下文，一次讀取檔案也有限制（約 2000 行）。筆記建議在 `claude.md` 加入指令，讓 Claude 在遇到大檔案時自動使用 `offset` 或 `head` 等指令分段讀取。[[05:41](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=341)]

#### **2. 子代理 (Sub-agents) 與團隊協作優化**
* **精準指派子代理**：使用 `--agent` 標籤可直接執行特定功能的子代理，無需等待主代理重新加載。[[03:36](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=216)]
* **子代理進階配置**：
    * **技能繼承**：使用 `skill` 標籤讓子代理繼承特定技能。[[04:02](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=242)]
    * **努力程度 (Effort)**：根據任務複雜度調整 Token 使用與思考強度。[[04:12](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=252)]
    * **沙盒隔離 (Isolation)**：設定代理在獨立的臨時工作樹（Work Tree）運作，實驗性修改不影響主代碼庫。[[04:45](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=285)]
* **代理團隊 (Agent Teams)**：這是一個實驗性功能，允許一個團隊領導者協調多個能彼此通訊、分享資訊的成員對話。[[07:56](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=476)]

#### **3. 工作流與開發規範管理**
* **路徑特定規則 (Path-specific rules)**：在專案中配置針對特定路徑的規則，實現「關注點分離」。例如處理前端時只載入 React 相關指令，避免 Claude 因指令過多而混淆。[[01:31](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=91)]
* **自動壓縮觸發點**：預設在上下文滿 95% 時才壓縮，這往往會降低輸出品質。建議將 `autoCompactPercentageOverride` 設為 `75%`，保持回覆的精準度。[[06:41](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=401)]
* **自定義 GitHub 提交資訊**：若不希望 Claude 在 Commit 中顯示為共同作者（Co-author），可在 `settings.json` 的 `attribution` 鍵值中將相關欄位留空。[[10:07](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=607)]

#### **4. 私隱保護與快捷功能**
* **停用遙測數據 (Telemetry)**：透過在 `settings.json` 加入三個特定變數（禁用數據追蹤、錯誤報告及回饋顯示），可在保留自動更新功能的同時，保護開發私隱。[[10:49](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=649)]
* **提示詞暫存 (Prompt Stashing)**：輸入到一半想換任務？按下 `Ctrl + S` 即可暫存目前的提示詞，完成緊急任務後會自動彈回輸入框。[[11:19](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=679)]

---

### **結論與行動建議**

* **關鍵技術建議：善用「Exit Code 2」控制工作流** [[12:08](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=728)]
    影片特別強調，在 Hook 中使用 **Exit Code 2** 是強制 AI 修正行為的核心。例如：當 Claude 嘗試使用你不喜歡的套件（如 `pip`）時，Hook 可以攔截並回傳錯誤訊息，強迫它改用正確的指令（如 `uv`）。
* **金句啟發**：
    > 「大多數你在使用 Claude Code 時遇到的問題，其實都已經有內建的修復方案，只是它們被埋在很少人討論的設定檔裡。」

* **下一步行動**：
    1. 開啟您的 `.claude/settings.json`。
    2. 優先調整 `cleanupPeriodDays` 與終端輸出限制。
    3. 安裝開源工具 **Claude CTX** 來管理多個不同專案的配置檔（Profiles）。[[08:40](http://www.youtube.com/watch?v=pDoBe4qbFPE&t=520)]
