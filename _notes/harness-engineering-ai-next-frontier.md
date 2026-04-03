---
title: 'Harness Engineering：AI下一個前沿'
date: 2026-04-03
image: /images/AI筆記/harness-engineering-ai-next-frontier.jpeg
category: AI筆記
tags: [Harness Engineering, Context Engineering, 約束設計, 生成評估分離, AI Agent]
description: '這部影片深入探討了 2026 年 AI 工程界最火熱的核心概念：Harness Engineering（馬具工程）。它揭示了當大模型能力趨於商品化時，決定 AI Agent 性能與穩定性的不再只是 Prompt'
quote: 'Agent 不難，Harness 才難。'
action: '在專案根目錄創建 agent.md，建立確定性驗證層，設計模塊化可替換的 Harness。'
source_has_timestamps: true
---

## 核心摘要
這部影片深入探討了 2026 年 AI 工程界最火熱的核心概念：**Harness Engineering（馬具工程）**。它揭示了當大模型（LLM）能力趨於商品化時，決定 AI Agent 性能與穩定性的不再只是 Prompt，而是為模型搭建的「運行系統」。透過約束與結構化設計，將概率性的模型推理轉化為可預測的生產力工具。

---

## 詳細重點整理

### 1. 什麼是 Harness Engineering？ [[00:42](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=42)]
* **定義與隱喻**：Harness 原意為「馬具」。模型如強壯的烈馬，而 Harness 則是控制方向、速度與工作的整套裝備。
* **工程內涵**：它不是教模型如何回答，而是**設計模型如何工作**。處理的是任務拆解、上下文管理、工具編排、狀態交接與失敗恢復。
* **關鍵概念**：**「Harness 是整輛車」**，包含方向盤、剎車與維護計劃，而不僅僅是指令（Prompt）或地圖（Context）。 [[03:37](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=217)]

### 2. 從 Prompt 到 Harness 的演進鏈條 [[02:18](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=138)]
* **Prompt Engineering (2022-2024)**：關注「問什麼」，屬於單輪文本優化。
* **Context Engineering (2025)**：關注「讓模型看到什麼」，如 RAG、記憶注入與對話歷史管理。
* **Harness Engineering (2026+)**：關注「模型怎麼幹活」，涵蓋權限、驗證、日誌、重試與人類接管機制。
* **關鍵概念**：**包含關係**——Harness 包含 Context，Context 包含 Prompt。 [[03:24](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=204)]

### 3. 三大巨頭的設計範式 (Anthropic, OpenAI, Google) [[05:39](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=339)]
* **Anthropic 的 3A 架構**：Planner（規劃）、Generator（生成）、Evaluator（評估）。強調「評估器分離」，避免模型自我表揚的系統性缺陷。 [[07:13](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=433)]
* **OpenAI 的三支柱**：知識庫增強、架構約束（硬性 Linter 與測試）、垃圾回收機制（清理系統熵增）。 [[09:11](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=551)]
* **Google DeepMind 的 Aletheia**：Generator、Verifier、Revisor 三位一體，透過循環迭代直到通過驗證。 [[10:35](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=635)]
* **關鍵概念**：**「生成與評估分離」**已成為行業共識。

### 4. 反直覺的設計原則：約束的力量 [[12:36](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=756)]
* **Vercel 的經驗**：移除 80% 不必要的工具後，Agent 的成功率反而提升。
* **Stripe 的實踐**：讓 Agent 在與人類相同的隔離沙盒（Devbox）中運行，提供版本化的製品（Artifacts）作為記憶。
* **關鍵概念**：**「約束提升自主性」**。為了獲得 AI 的可靠性，環境需要更多護欄而非更多自由。 [[13:15](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=795)]

---

## 結論與行動建議

* **啟發金句**：**「Agent 不難，Harness 才難。」** —— 取自 OpenAI 工程師，強調系統工程才是 AI 落地的最後一公里。 [[22:23](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=1343)]

* **具體行動建議：AI 開發三步走法則** [[21:52](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=1312)]
    1. **短期（立即執行）**：在專案根目錄創建 `agent.md` 或 `instructions.md`。每當 Agent 犯下重複性錯誤，就增加一條硬性規則，將經驗「外顯化」。
    2. **中期（基礎設施）**：建立**確定性驗證層**。引入 Linter、結構化測試與 Pre-commit hooks，用傳統代碼規範來約束模型的概率輸出。
    3. **長期（架構設計）**：設計**模塊化可替換的 Harness**。確保當模型升級（如從 4.0 到 5.0）時，可以平滑遷移並撤除不再需要的補丁。

* **生活與實踐建議：建立「外部記憶錨點」** [[15:57](http://www.youtube.com/watch?v=Xq-s_hAjADw&t=957)]
    * **製品導向工作流**：效法 Anthropic，不要依賴模型的對話記憶，而是要求 Agent 隨時更新「進度日誌」或「需求清單」文件。
    * **觀察紀錄**：定期進行「垃圾回收」，掃描 Agent 產出的代碼或內容是否符合架構一致性，對抗系統隨機性帶來的混亂（商徵）。

---
**相關影片連結**：[https://www.youtube.com/watch?v=Xq-s_hAjADw](https://www.youtube.com/watch?v=Xq-s_hAjADw)
