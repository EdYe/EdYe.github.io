---
title: 'Agentic AI Engineer：迴圈式自動建構 AI Agent'
date: 2026-07-01
image: /images/AI筆記/agentic-ai-engineer.jpg
category: AI筆記
tags: [Spec驅動開發, Eval驅動開發, LLM-as-Judge, 失敗模式分析, Agent自動化]
description: '這部影片由 Mutagent 共同創辦人 Bene 與 CTO Burak 主講，介紹「Agentic AI Engineer」概念'
quote: '把建構 AI Agent 的離線與線上迴圈完全交給 Agent 自己跑，人類的工作就變成『設計帶有明確評估終止閘門的迴圈』，而不是親自跑迴圈。'
action: '依 Spec→Eval→Diagnose 三步驟迴圈取代人工巡查，建立可規模化的 Agent 評估終止閘門'
source_has_timestamps: true
---
# 核心摘要

這部影片由 Mutagent 共同創辦人 Bene 與 CTO Burak 主講，介紹「**Agentic AI Engineer**」概念——將軟體工程中盛行的 Coding Agent Loop 套用到 AI Agent 的建構流程上 。核心痛點是：傳統建構 AI Agent 的離線（迭代開發）與線上（部署監控）循環高度依賴人工審查與人工建置，導致無法規模化擴展到上百個 Agent；解法是用一套由 Orchestrator 統籌的多代理人團隊，自動完成 spec、build、evaluate、diagnose、monitor、optimize 六大階段 。 [youtube](https://www.youtube.com/?v=R-Honjmorr4)

## 詳細重點整理

**1. 雙迴圈架構與人力瓶頸 [00:22]**
講者點出 Agent 開發存在兩個迴圈：建置時的「離線迴圈」（迭代、測試、評估、改進）與部署後的「線上迴圈」（監控追蹤、診斷、回饋優化）。目前這兩個迴圈多靠人工執行，速度慢且難以擴展，人工審查與建置時間成為最大瓶頸。關鍵概念：**離線迴圈與線上迴圈（Offline/Online Loop）**。

**2. 六階段生命週期總覽 [01:24]**
完整流程依序為 Spec（定義職責與決策邏輯）→ Build（在特定框架或 Coding Agent 中實作）→ Evaluate（定義關鍵評估指標，等同單元測試）→ Ship（部署上線）→ Diagnose（監控觸發後做根因分析）→ Optimize（針對失敗模式產生變更）後重新進入評估循環。關鍵概念：**Eval 驅動開發迴圈（Eval-Driven Development Loop）**。

**3. 冷啟動 vs. 既有 Agent 優化路徑 [06:03]**
建構新 Agent 時走「冷啟動路徑」，需從零設計 Spec；若 Agent 已上線運行，則走「既有功能優化路徑」，直接針對現有表現做迭代改善。關鍵概念：**冷啟動路徑（Cold Start Path）**。

**4. Spec 驅動開發：定義邊界與成功標準 [07:16]**
Spec 須清楚定義 Agent 的上下文需求、所需整合與工具、要負責與不負責的任務範圍，以及限制條件；Spec 與實作細節解耦，成為未來開發對照的藍圖。關鍵概念：**Spec 驅動開發（Spec-Driven Development）**。

**5. Build 階段的框架彈性 [08:53]**
Spec 完成後，可選擇任意目標平台或框架實作，因為 Agent 生態系變化極快（如 Hermes、Deep Agents 等新框架不斷出現），保持框架彈性可避免被單一 Harness 的能力瓶頸卡住。關鍵概念：**框架不可知性（Framework-Agnostic Design）**。

**6. Eval Suite 的建構與發現性本質 [11:21]**
評估套件包含「評估指標」與「資料集」兩部分；起初可由領域專家手寫或用歷史/合成資料起步，但完整 Eval Suite 是隨時間從使用者回饋與生產失敗案例「逐步發現」出來的，尤其需涵蓋邊緣案例。關鍵概念：**Eval 即發現過程（Eval as a Discovery Process）**。

**7. 為何需要 Evaluator Agent [13:41]**
當資料集動輒上百筆，人工逐一檢視 Trace 極耗時，導致評估循環時間拉長、無法平行擴展多個 Agent 功能；讓 Agent 自動篩選 Trace、執行評估，才能把人力瓶頸轉化為可規模化的自動迴圈。關鍵概念：**評估即終止閘門（Eval as Termination Gate）**。

**8. 評估設計：軌跡完整性與二元判準 [15:30]**
評估應檢查 Agent 的完整執行軌跡（Trajectory）——上下文是否完整、每一步工具輸出是否正確；採用**二元評估（Binary Evals）**優於模糊評分制，因為二元結果能直接觸發具體行動，且需校準 LLM-as-Judge 以降低同一案例多次評分不一致的噪音問題。關鍵概念：**LLM-as-Judge 校準**。

**9. Diagnose 階段：失敗模式分群與根因分析 [19:05]**
上線後收集失敗訊號，依根因（如 Prompt 段落問題、工具缺失或失效）將失敗模式分群，再生成新的偵測性評估與修復建議；長期累積後形成「已學習失敗模式」資料庫，並用程式碼可檢測指標取代逐筆人工讀 Trace，因為海量 Trace 的閱讀成本可能超過執行成本本身。關鍵概念：**已學習失敗模式（Learned Failure Modes）**。

**10. 自主優化迴圈與產品 Demo [22:48 / 27:14]**
最終形成自主優化迴圈：基於 Eval Suite 變更 Agent 設定、執行類似自動研究的實驗，達標即自動部署；現場展示 Mutagent 平台的 Evaluator Agent 與 Diagnose Agent，後者可從 LangFuse 等可觀測性平台擷取 Trace，用多層篩選挑出代表性樣本，產出含根因鏈、修復建議與假設區塊的 HTML 報告，最終生成可直接交給 Coding Agent 執行的 Markdown 任務清單。關鍵概念：**多層追蹤篩選（Multi-Tier Trace Segmentation）**。

## 結論與行動建議

**啟發金句：** 「把建構 AI Agent 的離線與線上迴圈完全交給 Agent 自己跑，人類的工作就變成『設計帶有明確評估終止閘門的迴圈』，而不是親自跑迴圈 。」 [youtube](https://www.youtube.com/?v=R-Honjmorr4)

**具體行動建議——S-E-D 法則：** **Spec**（先寫清楚邊界與成功標準）→ **Eval**（用二元判準建立可規模化的評估閘門）→ **Diagnose**（讓 Agent 自動分群失敗模式並產出修復建議），三步驟循環取代人工巡查。

**生活實踐建議：** 即使不開發 AI Agent，產品經理也可將此邏輯套用在日常專案管理——先寫清楚需求 Spec、用明確的二元驗收標準取代模糊打分、定期把使用者回饋分群找根因，避免「人工審查」變成團隊效率的隱形瓶頸。

## 參考連結

https://youtu.be/pSto5YaNGUo?si=OJLjVgNehF64RoxH
