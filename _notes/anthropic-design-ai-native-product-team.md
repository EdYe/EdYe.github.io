---
title: 'Anthropic 設計主管談 AI 原生產品運作模式'
date: 2026-06-10
image: /images/AI筆記/anthropic-design-ai-native-product-team.jpg
category: AI筆記
tags: [Builder Pod模型, 品質決策, PLG增長, AI Agent管理, ROI衡量]
description: 'Claude Code 從內部 Side Project 成長為年化營收 $25 億美元、佔據 51% 程式碼市場的產品。Meaghan Choi 揭示背後關鍵：打破職能邊界的 Builder Pod 模型、品質決策下移到 Live Code，以及每位成員都必須管理 AI Agent 艦隊的新型管理哲學。'
quote: '你現在管理的不只是人，你管理的是人與 AI Agent 組成的混合艦隊——這兩件事所需的能力，比你想像的更相近。'
action: '用 3–5 人跨職能 Builder Pod 取代大型部門，品質判斷點從 PRD Review 移到 Working Prototype，並把管理 AI Agents 納入日常管理工作。'
source_has_timestamps: true
---
# 🧠 Anthropic 設計主管談 AI 原生產品運作模式

**影片原標題：** *Anthropic Head of Design on Why Your Whole Team Should Be Managing Agents | Meaghan Choi | E298*
**來源：** Product School · ProductCon New York · 2026.06.03 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

## [核心摘要]

Claude Code 從一個內部 Side Project 成長為年化營收 $25 億美元、佔據 51% 程式碼市場的產品 。Meaghan Choi（Anthropic Claude Code 與 Co-work 設計主管）揭示了背後的關鍵秘訣：**打破職能邊界的 Builder Pod 模型**、**將品質決策從 Mock/PRD 下移到 Live Code**，以及**每位成員都必須管理一支 AI Agent 艦隊**的新型管理哲學。 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

## [詳細重點整理]

### 1. Claude Code 的誕生 [00:00–05:30]
Claude Code 最初是 2024 年少數工程師探索「讓 Claude 代替人執行程式碼」的 Side Project 。核心突破點是將 Claude 接入擁有完整電腦存取權限的 Shell（SCL），一段內部 Slack 影片引爆了團隊的興奮感，但初版需要一小時設定、模型能力也還不夠成熟 。 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

**關鍵概念：** **Dogfooding 飛輪**——先讓 Anthropic 全員使用，驗證真實痛點後再外部發布 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

### 2. AI 原生的工作方式：職稱消亡 [05:30–08:00]
在 Anthropic，設計師 push code、工程師做設計，職稱僅代表「可能被諮詢的專業」，而非貢獻邊界 。理想的 **Builder Pod** 由 3–5 人組成，組合可以是任意比例的工程師、設計師、PM，目標是大家一起把東西做成可以運行的程式碼 。 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

**關鍵概念：** **Builder Pod Model**——以產出（Working Code）為核心、跨職能共同負責、無層級的小型交付單元 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

### 3. 品質決策下移到 Live Code [08:00–13:30]
過去的品質把關點在 PRD 討論或 Figma Mock Review，現在 Anthropic 已把這個關卡推移到 **在真實運行的程式碼中體驗** 。產品是否夠好出貨，由 Pod 自己決定：先達到足夠的內部 DAU（Daily Active Users）採用率，才開放外部 。 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

**關鍵概念：** **Live Code Quality Gate**——用實際可操作的產品（而非文件或原型）做品質判斷的基準點 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

### 4. 企業採用：開發者 PLG 路線 [11:00–14:00]
Claude Code 的企業滲透採用 **Bottom-Up PLG**：個人開發者先在個人或 Side Project 使用，成為內部倡導者，推動組織層級採用 。企業開始使用後，工程團隊會為其建立自定義工具、Database Connectors、內部基礎設施整合，進一步強化整個生態的使用體驗 。 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

**關鍵概念：** **Developer-Led PLG（產品導向增長）**——由技術使用者帶動企業內部擴散，而非由上而下的銷售模式 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

### 5. UI 設計哲學：介面只是媒介 [14:00–17:00]
Choi 自稱是「極簡主義者」，認為 CLI 是包裝在模型外最薄的一層，代表最純粹的技術接觸面 。UI 的本質是「傳達你要的輸出給設備或服務的工具」，最終重要的是 Work Product 本身，而非中間介面 。Co-work 等新產品則是為半技術背景使用者（如設計師、PM）降低進入門檻而生 。 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

**關鍵概念：** **Output-First UI 哲學**——介面設計以「最終輸出品質」為中心，而非以介面精緻度為目標 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

### 6. 每個人都在管理 AI Agent 艦隊 [17:00–18:00]
Choi 認為每位 IC（個人貢獻者）現在其實都是「小型管理者」，因為大家都在管理一群運作中的 Claude Agents 。人員管理者管理「人 + Agents」，這兩件事所需的技能比想像中更相似——都需要拆解任務、給予明確指令、追蹤產出品質 。 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

**關鍵概念：** **Agent Fleet Management**——將管理 AI Agent 視同管理人員的延伸，是現代產品管理者的核心新技能 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

### 7. AI ROI 衡量框架 [18:00–20:30]
Token 使用量是「**沒有使用 AI 的落後指標**」（零 Token = 該擔心），但也不應以 Token 量競爭，因為大量 Token 消耗可以完全不帶來任何產出 。真正的 ROI 回歸傳統產品指標：**採用率（Adoption）、留存率（Retention）、收益（Revenue）**——這些指標不管有沒有 AI 都依然有效 。 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

**關鍵概念：** **Token ≠ ROI**——Token 是使用 AI 的必要但不充分條件，最終應以業務結果衡量 AI 投資回報 [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

***

## [技術/數據對比]

| 指標 | 數據 |
|---|---|
| Anthropic Series H 估值 | 接近 **$1 兆美元** |
| 年化總營收 | **$300 億美元** |
| Claude Code 年化營收（2026.02） | **$25 億美元**，且年初至今已翻倍 |
| Claude Code 市場佔有率 | 程式碼工具市場 **51%** |
| Claude Code GA 時間 | **2025 年 5 月**  [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf) |

***

## [結論與行動建議]

**🔥 啟發金句：**
> **「你現在管理的不只是人，你管理的是人與 AI Agent 組成的混合艦隊——這兩件事所需的能力，比你想像的更相近。」** [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)

**⚡ 具體行動建議（B-P-L 法則）：**
- **B（Build First）**：放棄「先把 Mock 做好再開發」的習慣，直接做出 Working Code，在真實使用中判斷品質
- **P（Pod not Department）**：用 3–5 人的跨職能小 Pod 取代大型部門運作，讓每人都能貢獻到任何環節
- **L（Lead your Agent Fleet）**：把管理 AI Agents 當成日常管理工作的一部分，訓練自己有效地拆解任務、指派給 AI 並驗收產出

**🌱 生活實踐建議：**
作為 AI-Powered Application Architect，您可以立即將 **Builder Pod 模型**應用到您的產品開發流程中：組建一個 3 人核心 Pod（工程師 × 1 + PM/設計師 × 1 + 您自己），每個 Sprint 的品質判斷點從 PRD Review 移到 **Claude Code 實際產出的 Working Prototype**，以內部 DAU 作為對外發布的門檻指標。

***

## [參考連結]

- 🎬 原始影片：https://youtu.be/V8y3K0fLSKg?si=IJYyPjyyPLLuQqVS [unom.ac](https://www.unom.ac.in/webportal/uploads/naac/1/additional/5%20M.Sc.%20HRD%20Psychology.pdf)
- 📚 Product School AI 培訓：https://prdct.school/3RVzRDv
