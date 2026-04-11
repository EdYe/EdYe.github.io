---
title: 'AI Agent 評測體系設計：四層品質監控與機率性系統 CI'
date: 2026-04-11
image: /images/影片筆記/ai-agent-evaluation-system-design.jpeg
category: 影片筆記
tags: [AI評測, 機率性系統, 軌跡層, 評分函數, 持續改進]
description: '本影片深入探討了 AI Agent 開發中最具挑戰性的環節：評測（Evals）。開發者必須建立一套類似生產線質檢的「機率性評測體系」，從組件、軌跡、結果到系統監控四個維度確保 AI 決策的品質。'
quote: 'AI 的品質不是測試出來的，而是設計出來的；你無法測量你看不見的東西。'
action: '為 Agent 建立組件、軌跡、結果、監控四層指標，導入結構化追蹤並建立失敗資料庫。'
source_has_timestamps: true
---

## 核心摘要
本影片深入探討了 AI Agent（智能體）開發中最具挑戰性的環節：評測（Evals）。作者強調 AI Agent 並非確定性的軟體，傳統的單元測試已不足夠，開發者必須建立一套類似生產線質檢的「機率性評測體系」，從組件、軌跡、結果到系統監控四個維度，確保 AI 決策的品質與效率。

---

## 詳細重點整理
### 1. 為什麼傳統測試對 AI Agent 會失效？ [[00:51](http://www.youtube.com/watch?v=Kleu3ROhpvY&t=51)]
* **非確定性挑戰**：Agent 的輸入是自然語言，路徑不固定（可能 3 步也可能 25 步），傳統的「給定輸入必得相同輸出」的單元測試無法應對。
* **偽成功現象**：輸出看似正確，但中間的決策邏輯可能完全錯誤。
* **關鍵概念**：**Eval（評測）是針對「機率性系統」的 CI（持續集成）**，它不是簡單的對錯，而是在 0 到 1 之間的品質評分 [[01:53](http://www.youtube.com/watch?v=Kleu3ROhpvY&t=113)]。

### 2. 評測系統的三大支柱 [[02:01](http://www.youtube.com/watch?v=Kleu3ROhpvY&t=121)]
* **基準數據集 (Benchmark)**：一組精心挑選的輸入與參考輸出。
* **評分函數 (Scoring Functions)**：自動化裁判（如 LLM-as-a-judge）根據標準進行打分。
* **長期追蹤**：觀察品質趨勢而非單次結果，將生產環境的失敗轉化為新的測試案例。

### 3. AI 評測的四個核心層次 [[02:33](http://www.youtube.com/watch?v=Kleu3ROhpvY&t=153)]
* **組件層 (Component)**：工具與函數。這是確定性的，可用傳統單元測試確保 JSON 解析等基本功能。
* **軌跡層 (Trajectory)**：決策路徑。檢查 Agent 是否用了最精簡、正確的工具序列。
* **結果層 (Outcome)**：最終答案是否正確、有幫助且具備事實根據。
* **系統監控層 (System Monitoring)**：在大規模運行中觀察模式與品質衰退。
* **關鍵概念**：**「由外而內」測量**。先看結果，若失敗則拆解軌跡與組件找原因 [[04:23](http://www.youtube.com/watch?v=Kleu3ROhpvY&t=263)]。

### 4. 衡量品質的四個維度 [[04:42](http://www.youtube.com/watch?v=Kleu3ROhpvY&t=282)]
* **有效性 (Effectiveness)**：是否達成用戶目標。
* **效率 (Efficiency)**：是否浪費 Token 或步驟。
* **魯棒性 (Robustness)**：面對異常輸入或 API 失敗時的表現。
* **安全性 (Safety)**：是否遵守邊界與對齊原則。

---

## 結論與行動建議
* **啟發金句**：**「AI 的品質不是測試出來的，而是設計出來的；你無法測量你看不見的東西。」** [[05:27](http://www.youtube.com/watch?v=Kleu3ROhpvY&t=327)]
* **具體行動建議：4-4-1 實踐法則**
    1. **4 層檢視**：檢查你的 Agent 是否在「組件、軌跡、結果、監控」這四層都有對應的觀測指標。
    2. **4 維評分**：為每個任務設計評分表（Rubric），涵蓋有效性、效率、魯棒性與安全性。
    3. **1 個閉環**：建立「生產失敗案例 -> 標註 -> 加入評測集 -> 迴歸測試」的持續改進閉環 [[06:27](http://www.youtube.com/watch?v=Kleu3ROhpvY&t=387)]。
* **生活實踐建議**：
    * **結構化日誌**：從開發第一天就導入結構化追蹤（Tracing），記錄 Agent 的中間推理過程（Reasoning）。
    * **LLM 裁判**：定義明確的「好答案」標準，並讓另一個 LLM 扮演評審，減少人工審核成本。
    * **建立失敗資料庫**：將所有用戶反饋的錯誤轉化為自動化測試點，讓 Agent 的能力隨時間「複利」增長。

Https://youtu.be/Kleu3ROhpvY?si=YIIOUJ48VNkbM1K9
