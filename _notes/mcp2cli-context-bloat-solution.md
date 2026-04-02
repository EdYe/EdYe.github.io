---
title: 'MCP2CLI：解決 AI 上下文膨脹問題'
date: 2026-04-02
image: /images/影片筆記/mcp2cli-context-bloat-solution.jpeg
category: 影片筆記
tags: [MCP2CLI, 上下文膨脹, Token效率, 環境變數隔離, 技能系統]
description: '本影片深入探討了 AI 模型使用 MCP 時，因工具描述與輸出過多導致的「上下文膨脹」問題。透過介紹新工具 MCP2CLI'
quote: '真正的效率不在於擁有多少工具，而是在於如何讓工具在不佔用空間的情況下，隨時為你所用。'
action: '3-S 效能法則：隔離MCP工具、技能化描述、串流大型輸出'
source_has_timestamps: true
---

## 核心摘要
本影片深入探討了 AI 模型使用模型上下文協定（MCP）時，因工具描述與輸出過多導致的「上下文膨脹（Context Bloat）」問題。透過介紹新工具 **MCP2CLI**，展示了如何將 MCP 轉換為命令列工具（CLI），大幅節省 Token 消耗並提升 AI 代理（Agent）的執行效率，是開發者優化 AI 工作流的核心指南。

---

## 詳細重點整理

### 1. 解決 MCP 上下文膨脹的核心挑戰 [[00:22](http://www.youtube.com/watch?v=LqN_ItMqovA&t=22)]
* **問題描述**：當連接多個 MCP 工具時，所有工具描述都會塞進上下文視窗，導致空間被無關資訊填滿。
* **解決方案演進**：從 Docker 的 Code Mode 到 Cloudflare 的可執行代碼提案，最後引出 **MCP2CLI**。
* **關鍵概念**：**運行時轉換（Runtime Conversion）**，將工具動時轉為 Bash 指令，而非在構建時（Build time）寫死，確保工具更新能即時同步。

### 2. MCP2CLI 的技術優勢與緩存機制 [[02:54](http://www.youtube.com/watch?v=LqN_ItMqovA&t=174)]
* **緩存設計**：內建緩存機制（預設存活時間 1 小時），解決頻繁呼叫導致的轉換延遲。
* **多協議支持**：基於 MCP Python SDK 構建，能同時處理 OpenAPI 與 REST APIs，讓不具備 MCP 伺服器的 API 也能透過 CLI 使用。
* **關鍵概念**：**Token 效率**，透過 Tik Token 測試證明，此方法能顯著降低成本並加快執行速度。

### 3. 安全性與環境隔離 [[04:00](http://www.youtube.com/watch?v=LqN_ItMqovA&t=240)]
* **安裝建議**：建議使用 `npx` 或不預先安裝的方式執行，以保持工作環境乾淨。
* **敏感資料保護**：不將 API Key 直接放在指令參數中，而是透過環境變數或專門的秘密管理器（Secret Manager）注入。
* **關鍵概念**：**環境變數隔離**，避免敏感資訊在進程列表中被洩漏。

### 4. 實戰應用：從 Superbase 到自動化測試 [[05:36](http://www.youtube.com/watch?v=LqN_ItMqovA&t=336)]
* **多工具協作**：同時連接 Superbase（後端）、GitHub（版本控制）、Puppeteer（瀏覽器測試）與 Context7（文檔檢索）。
* **技能系統（Skills）**：相較於在 `claude.md` 寫死指令，自定義「Skills」能讓 AI 更清楚何時該呼叫特定工具。
* **關鍵概念**：**管道輸出（Piping Output）**，當工具輸出過大時，將結果導向檔案並使用 `grep` 提取關鍵資訊，而非全部塞入對話。 [[11:06](http://www.youtube.com/watch?v=LqN_ItMqovA&t=666)]

---

## 結論與行動建議

* **啟發金句**：**「真正的效率不在於擁有多少工具，而是在於如何讓工具在不佔用空間的情況下，隨時為你所用。」**

* **具體行動建議：3-S 效能法則**
    1. **S**eparate (隔離)：將 MCP 工具從 LLM 的靜態上下文分離，改用 **MCP2CLI** 進行動態呼叫。
    2. **S**kill-based (技能化)：為每個 MCP 伺服器編寫專屬的 **Skill 描述**，明確告知 AI 工具的使用時機。
    3. **S**tream (串流)：對於長度超過 1000 tokens 的工具輸出，強制執行 **"Pipe to File"** 指令，再由 AI 進行二次過濾。

* **生活實踐建議**：
    * **建立技術錨點**：在進行 AI 專案開發時，優先檢查 `claude.md` 或 `cursor.rules` 是否包含了針對大型輸出的處理邏輯。
    * **觀察紀錄**：紀錄使用 MCP2CLI 前後，單次對話消耗的 Token 數量變化，量化你的開發成本優化進度。
