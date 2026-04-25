---
title: 'Claude Code 五種工作流模式全解析：從序列流到自主模式'
date: 2026-04-25
image: /images/影片筆記/claude-code-workflows-explained.jpeg
category: 影片筆記
tags: [子代理人, 上下文隔離, Worktree工作樹, 代理人團隊, 自主模式]
description: '這段影片深入解析了 Claude Code 的五種進階工作流模式，旨在教導使用者如何從單純的「一對一對話」轉型為「管理開發團隊」的思維。透過善用內建子代理人、並行終端，避免上下文腐爛。'
quote: '別把 Claude Code 只當成一個工具，要把他當成你的開發團隊來經營。'
action: '善用 Explore/Plan/General 子代理人，使用 claude -w 建立 Worktree 隔離環境，以 -p 旗標自動化重複任務。'
source_has_timestamps: true
---

## 核心摘要
這段影片深入解析了 Claude Code 的五種進階工作流模式，旨在教導使用者如何從單純的「一對一對話」轉型為「管理開發團隊」的思維。透過善用內建子代理人、並行終端、自動化腳本與實驗性的團隊協作功能，開發者能有效避免「上下文腐爛（Context Rot）」，極大化開發效率與代碼品質。

---

## 詳細重點整理

### 1. 隱藏的內建子代理人 (Built-in Sub-agents) [[00:47](http://www.youtube.com/watch?v=38t5UBCa4OI&t=47)]
* **重點內容說明**：Claude Code 在背後會根據任務複雜度自動啟動三種子代理人：
    * **Explore**：使用 Haiku 模型，唯讀模式，負責快速搜索與總結檔案資訊。
    * **Plan**：在 `/plan` 模式下啟動，負責在制定策略前研究代碼庫。
    * **General Purpose**：使用 Sonnet 模型，具備完全的讀寫權限，處理複雜的多步驟任務。
* **關鍵概念**：**上下文隔離**。子代理人擁有獨立的上下文視窗，能防止主對話內容過於臃腫。

### 2. 模式一：序列流 (Sequential Flow) [[02:44](http://www.youtube.com/watch?v=38t5UBCa4OI&t=164)]
* **重點內容說明**：最基礎的使用方式，任務按順序執行並疊加上下文。然而，長期使用會遇到「上下文腐爛 [[04:01](http://www.youtube.com/watch?v=38t5UBCa4OI&t=241)]」，導致 Claude 開始遺忘細節。
* **關鍵概念**：**維護與清理**。應善用 `claude.md` 結構、`/clear` 與 `/compact` 指令來保持對話的精準度。

### 3. 模式二：操作員模式 (The Operator) [[04:35](http://www.youtube.com/watch?v=38t5UBCa4OI&t=275)]
* **重點內容說明**：當多個任務彼此獨立時（如：修復 Bug 與 設計新頁面），應開啟多個終端機並行運作。
* **關鍵概念**：**Worktree 工作樹**。使用 `claude -w` [[05:31](http://www.youtube.com/watch?v=38t5UBCa4OI&t=331)] 指令可為每個任務建立獨立的專案副本與分支，確保環境純淨且互不干擾。

### 4. 模式三：分割與合併 (Split and Merge) [[07:29](http://www.youtube.com/watch?v=38t5UBCa4OI&t=449)]
* **重點內容說明**：在單一會話中，讓 Claude 將大任務拆分給多個子代理人同時執行（例如同時研究 5 個競爭對手），最後再由主代理人彙整結果。
* **關鍵概念**：**中心輻射架構 (Hub-and-Spoke)** [[09:29](http://www.youtube.com/watch?v=38t5UBCa4OI&t=569)]。子代理人僅能與主代理人溝通，彼此之間無法對話，適合處理大量平行資料收集。

### 5. 模式四：代理人團隊 (Agent Teams) [[11:45](http://www.youtube.com/watch?v=38t5UBCa4OI&t=705)]
* **重點內容說明**：最進階且實驗性的模式（需開啟 `experimental_agent_teams_1` [[12:33](http://www.youtube.com/watch?v=38t5UBCa4OI&t=753)]），代理人之間能透過共享任務清單直接協作與溝通。
* **關鍵概念**：**跨領域協作**。適合需要前端、後端與測試人員頻繁同步的複雜專案，但 Token 消耗量高達一般模式的 4-7 倍。

### 6. 模式五：無頭/自主模式 (Headless/Autonomous) [[14:15](http://www.youtube.com/watch?v=38t5UBCa4OI&t=855)]
* **重點內容說明**：使用 `-p` 參數 [[14:53](http://www.youtube.com/watch?v=38t5UBCa4OI&t=893)] 賦予 Claude 完全自主權，無需人工介入確認。可結合 Cron 排程執行例行性任務，如：每日早晨自動產出前日工作總結報告。
* **關鍵概念**：**自動化與信任度**。最適合執行「結果易於驗證」的批次處理任務。

---

## 結論與行動建議
* **啟發金句**：『別把 Claude Code 只當成一個工具，要把他當成你的開發團隊來經營。』
* **具體行動建議：3-W-P 核心法則**
    1. **3 (3 Sub-agents)**：意識到內建的 Explore/Plan/General 功能，善用 `/plan` 先行研究再動手。
    2. **W (Worktree)**：只要處理不相關的功能，一律使用 `claude -w` 開啟獨立工作樹，維持代碼潔淨。
    3. **P (-p flag)**：將重複性的代碼審查或文檔產出封裝成 `-p` 指令，放入自動化腳本中。
* **生活實踐建議**：
    * **建立「上下文審查日記」**：每週檢查一次你的 `claude.md`，將常用的規則與專案架構更新進去，這就像是為你的 AI 團隊更新「員工手冊」。
    * **工具建議**：練習在 VS Code 中開啟分欄終端機，搭配 `-w` 標籤，體驗同時指揮多個 AI 代理人的「操作員」手感。

影片來源：[Every Claude Code Workflow Explained (& When to Use Each)](http://www.youtube.com/watch?v=38t5UBCa4OI)
