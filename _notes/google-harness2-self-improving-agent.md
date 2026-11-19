---
title: 'Google Harness²：自我改進的 AI Agent 架構'
date: 2026-11-19
image: /images/AI筆記/google-harness2-self-improving-agent.jpg
category: AI筆記
tags: [Model-Harness 分離, Propose-Probe-Compose, 雙層遞迴, 證據支持教訓, 零重訓練增益]
description: 'Google Research 開源了 Harness²，核心貢獻是證明 AI Agent 的效能瓶頸往往不在模型本身，而在包裹模型的 Harness（設定環境）。在不更換模型、不重新訓練的前提下...'
quote: '💡廚師不變，翻新廚房就能多拿 11.8 分——你等的下一個模型，可能不如你今天就能改寫的設定檔。'
action: '🎯P-P-C 法則：面對表現不佳的 Agent，先 Propose 多個設定修改，再 Probe 平行實測比較，最後 Compose 保留有效組合。'
source_has_timestamps: false
source_raw: 'Google Harness²: NEW Self-Improving AI Agent'
---
# Google Harness²：自我改進的 AI Agent 架構

## [核心摘要]

Google Research 開源了 Harness²，核心貢獻是證明 **AI Agent 的效能瓶頸往往不在模型本身，而在包裹模型的 Harness（設定環境）**。在不更換模型、不重新訓練的前提下，僅讓 Agent 自己改寫系統提示、記憶、技能檔案等八個組成部分，就能在辦公、專業與實驗室任務上提升 4.5 至 11.8 個百分點，解決了「每次都要等更強新模型」的痛點 。

## [詳細重點整理]

### 1. 同一顆大腦，更好的廚房

Agent 由兩部分組成：**Model（模型）** 是大腦，**Harness（工具架構）** 是包圍大腦的一切——指令、規則、記憶、工具、技能與輔助 Agent。以廚師比喻：廚師再強，廚房雜亂照樣端出爛菜。傳統做法是人們把廚房「設計一次、永久使用」，但真實工作會不斷丟來沒人預料過的新任務，Google 稱之為 **Open World（開放世界）** 問題 。

- 關鍵概念：**Model-Harness 分離**

### 2. 三組基準測試的實測數據

以 Gemini 5 與 Gemini 3 Flash 兩種模型、四種模型-Harness 組合測試（詳見下方對比表）。所有提升皆來自**單輪改進**，且 Google 指出多輪改進會讓效益持續疊加。模型權重（weights）完全不變，改變的只有「廚房」。專案上線約兩週即獲得逾 12,600 個 GitHub 星標與 1,200 個 fork 。

- 關鍵概念：**Zero-Retraining Gain（零重訓練增益）**

### 3. Propose → Probe → Compose 三步循環 

- **Propose（提出）**：Harness Editor 建議設定變更，分為「通用型」與「任務特化型」兩類。
- **Probe（探測）**：把每個建議的變更分別套用，讓多個版本的 Agent 跑同一個任務。
- **Compose（組合）**：Harness Composer 並排比較各版本表現，只保留有效的變更，組成最終設定。

整個過程**不需要答案**（works without ground truth feedback），靠「比較」而非「對答案」來學習——如同早上試跑兩條路線去健身房，看誰先到就知道哪條快 。

- 關鍵概念：**Ground-Truth-Free Learning**

### 4. 可改寫的八個 Harness 組件

1. System Prompt（系統提示）
2. Guardrails（安全護欄）
3. Memory（記憶）
4. Tool Guidance（工具使用指引）
5. Subagents（子代理）
6. Skills（技能）
7. Scripts（腳本）
8. Plugins（外掛）

Google 按功能分組：System Prompt、Guardrails、Memory、Skills 控制 Agent **開始任務時知道什麼**；Tool Guidance 與 Scripts 控制**怎麼用工具**；Subagents 控制**怎麼分派工作**；Plugins 控制**每一步內部發生什麼**。若你已在用 Claude Code、具備 skill files、memory files 與 subagents 的環境，這些正是同一批積木——差別只在 Harness² 讓 Agent 自己改寫，而非人工手改 。

- 關鍵概念：**Harness 八層可編輯面**

### 5. 隱藏的第二循環：Harness-Level Recursion 

第一層循環發生在單一任務內，稱為 **Task-Level Recursion（任務層遞迴）**。真正的重點是疊在其上的第二層：**Harness-Level Recursion（架構層遞迴）**。每個任務結束後，Experience Reflector 回顧整個過程，把「贏的設定」與「任務中學到的教訓」存入 **Improvement Harness**（一份關於如何改進自己的筆記本）。下一次新任務出現時，系統會先讀這本筆記再提出建議——改進 Agent 的機制本身也在被改進 。

Google 強調只保存 **Evidence-Supported Lessons（有證據支持的教訓）**：不保存隨機猜測，只保存能用實際運行結果背書的結論。記憶塞滿垃圾會讓 Agent 變差；塞滿被驗證過的教訓則會讓它越來越強。

- 關鍵概念：**雙層遞迴**

### 6. 擴展策略：Parallel vs. Sequential 

- **Parallel（平行）**：同時測試多組設定。預算設為 3 時，測三組通用設定＋三組任務特化設定，再合成三個組合設定。探索更廣。
- **Sequential（序列）**：完成一輪後取最佳設定，在其上再跑一輪、再一輪。打磨更深。

兩種方式的效益都隨預算提高而增加。目前支援兩種執行器：**OpenCode** 與 **Codex**，代表它建立在人們今天真正在用的工具上，而非實驗室專屬環境 。

- 關鍵概念：**廣度探索 vs. 深度精煉**

### 7. 三個現實限制 

- **成本放大**：每次 Probe 都是一次完整的 Agent 運行。測六組設定等於跑六次，API 費用倍增。Google 建議先在小任務集上試驗。
- **研究專案性質**：Google 明言這不是官方支援產品，版本 0.1.0，預期有粗糙邊緣。
- **技術門檻**：需 Linux + Python 3.12、Node.js 與 Google Cloud 設定，不是點一下就能用的無程式碼應用 。
- 關鍵概念：**Probe 即成本**

補充數據：所有提升來自單輪改進；模型為 Gemini 5 與 Gemini 3 Flash，共四種模型-Harness 組合；上線兩週 GitHub 破 12,600 星、1,200 forks 。

## [結論與行動建議]

**啟發金句**：廚師不變，翻新廚房就能多拿 11.8 分——你等的下一個模型，可能不如你今天就能改寫的設定檔。

**具體行動建議（P-P-C 法則）**：面對表現不佳的 Agent，先 Propose 多個設定修改，再 Probe 平行實測比較，最後 Compose 保留有效組合——把「換模型」的直覺，換成「實測設定」的紀律。

**生活實踐建議**：如果你在 Claude Code 或 MCP 工作流中維護 skill files 與 memory，當某個 Agent（例如 SEO 寫作或影片腳本 Agent）表現不佳時，不要急著換模型或重寫提示詞——先列出三個候選規則修改，各自實測同一任務，保留結果最好的版本，並把「被證據支持的教訓」寫回 memory 檔案。即使不部署 Harness² 本身，這套「證據支持教訓」的紀律就能讓你的 Agent 作業系統隨每次任務累積改進。

## [參考連結]

- 原始影片：[Google Harness²: NEW Self-Improving AI Agent!](https://www.youtube.com/watch?v=jFvogJ9KGVw)（Julian Goldie SEO，2026-10-20，長度 12:16）
- 影片說明欄提及的官方資源：Harness² GitHub 專案（google-research/harness2）、專案頁 [harness2.github.io](http://harness2.github.io)、論文 arXiv:2610.14224