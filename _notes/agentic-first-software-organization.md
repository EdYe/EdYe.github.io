---
title: 'Agentic-First軟體組織建構法'
date: 2026-08-09
image: /images/AI筆記/agentic-first-software-organization.jpg
category: AI筆記
tags: [Agentic-First, DORA護欄效應, 模式接縫, 自我驗證迴圈, Token經濟學]
description: '本影片探討「Agentic-First 軟體組織」的建構方法，核心痛點在於：多數企業已導入 AI 編碼助手，卻未能實現可量化的產出與品質提升。'
quote: '💡「AI 不會創造新問題，它只會放大你已經有的問題。」'
action: '🎯依C-V-O法則：強制100%程式碼覆蓋率、建立check script讓Agent自驗證並由CI強制執行、對每一行AI生成程式碼負起所有權。'
source_has_timestamps: true
---
## [核心摘要]

本影片探討「Agentic-First 軟體組織」的建構方法，核心痛點在於：多數企業已導入 AI 編碼助手，卻未能實現可量化的產出與品質提升。Lean TECHniques 提出，當 Agent 承擔 SDLC 大部分工作時，**DORA 研究所定義的軟體交付基本功（快速回饋、自動化測試、程式碼審查）不僅不變，反而更加重要**——它們是防止 AI 失控的護欄。關鍵貢獻在於：透過 100% 程式碼覆蓋率、check script、agent.md 設定檔、品質閘道等機制，將 AI 速度優勢（2x–10x）轉化為整個 SDLC 的系統性增益，同時維持人類對不可逆動作的把關。

***

## [詳細重點整理]

### 1. Agentic-First 的定義與核心差異 [02:53]

**Chatbot 回應，Agent 行動。** 傳統聊天機器人僅提供建議（「這裡可能有問題」），而 Agent 會實際執行修復——修改程式碼、拉取日誌分析、提交 Pull Request。這代表從「prompt 到 PR」的典範轉移。多數組織擁有 AI 工具，但極少數已針對 Agent 重新設計流程。

**關鍵概念：Agentic-First（代理優先）**——以 Agent 為主要執行者來重新設計交付流程，而非僅在既有流程上疊加 AI 工具。

***

### 2. IKEA 案例：將人力推向高價值工作 [04:15]

IKEA 以 AI 處理半數來電量後，並未裁撤 8,500 名客服人員，而是將其重新培訓為「設計顧問」。因為顧客來電的真正目標不是查庫存，而是「這張茶几放在我家客廳好看嗎？」此舉創造了 **15 億美元的新營收流**。

此案例示範了兩個原則：將人力推向更高價值工作，以及圍繞 AI 重新設計業務流程。同樣的思維可套用至 SDLC——當 AI 處理掉繁瑣工作後，團隊能投入過去無暇顧及的技術債、文件更新、產品健康度分析。

**關鍵概念：高價值工作轉移（Higher-Value Work Displacement）**

***

### 3. AI 時代的軟體開發基本功 [06:50]

DORA（DevOps Research Assessment）研究歸納的高績效團隊能力——快速回饋、自動化測試、程式碼審查、穩定部署——**在 AI 主導的世界中全部仍然適用，且更加重要**。這些基本功是讓 AI「留在軌道上」的護欄。

Agent 並非完美：實際案例中，Agent 建立 API 端點、進行本地與 GitHub Copilot 程式碼審查，卻全部漏抓「端點無認證、資料暴露全球」的嚴重缺陷，最終由人類審查者攔截。Agent 的本質類似「聰明且有企圖心的初級工程師，熱愛到處複製貼上程式碼」。

**關鍵概念：DORA 護欄效應（DORA Guardrail Effect）**——基本功不僅維持品質，更是約束 AI 行為的系統性機制。

***

### 4. Brownfield 與 Greenfield 專案的 Agent 策略 [09:44]

**Brownfield（既有專案）：** 若程式庫存在不良模式，AI 會放大並持續擴散這些模式，而非自動改善。解法是建立「良好模式的接縫（seam）」——新增一個採用正確模式的功能，並在 `agent.md`、Copilot instructions 或 `claude.md` 中明確指示 Agent 遵循哪些檔案的模式、避免哪些檔案。這些設定檔的內容會在所有 prompt 與 AI 動作之前被完整貼入。

**Greenfield（全新專案）：** 若六人團隊同時啟用 Agent 卻未先建立模式，將導致模式混亂。正確做法是先由 2–3 人花一週建立模式，再引入其餘團隊。這些原則在 AI 出現前即為最佳實務，AI 只是讓忽視它們的後果更嚴重。

**關鍵概念：模式接縫（Pattern Seam）**——在程式庫中植入良好模式的參考點，引導 Agent 生成一致架構。

***

### 5. Agent-Ready 評估工具 [12:14]

Lean TECHniques 開發的 Agent-Ready Assessment 會掃描程式庫，檢查是否具備 Agent 就緒條件。約 90% 的檢查項目在 AI 出現前即是良好實務，其餘為 AI 專屬項目。評估結果產出待辦清單與「已做得不錯」的清單，並透過遊戲化（評分從 F 到 A）激勵團隊改善。

**關鍵概念：Agent-Ready 評估（Agent Readiness Assessment）**——系統化檢測程式庫是否具備讓 Agent 安全、高效運作的基礎條件。

***

### 6. 速度與品質的實際增益 [16:02]

在建立護欄的前提下，實測達到 **2x–10x 速度提升，同時維持或改善品質**。但速度差異只有在「為 Agent 建構護欄（harness）」後才會實現——若只加速編碼卻缺乏品質閘道，會因來回修改而拉長整體週期時間。必須優化整個 SDLC，而非僅編碼環節。

***

### 7. 開發者立即可行的實踐步驟 [17:30]

- **強制 100% 程式碼覆蓋率：** Agent 本質上傾向走捷徑以快速取悅使用者。若僅要求 90%，新增功能不會主動超越門檻。現今測試生成極快，覆蓋率不再是速度瓶頸。100% 覆蓋率更開啟了 **突變測試（Mutation Testing）** 的大門——翻轉布林值或字串值，驗證測試是否真的在測試預期行為。可明確忽略不需測試的項目。

- **建立 check/verify script：** 整合 formatter、linter、測試、安全掃描的腳本，並在 `agent.md` 中指示 Agent 完成後執行此腳本、若失敗則自行修復。這是給 Agent 最大的生產力提升——讓它能自我驗證，可自主運作數小時直到通過檢查。多數功能現在一小時內完成，甚至 15–20 分鐘。CI 管線應同步強制執行此腳本，防止 Agent 偶爾忽略指示（約 2% 機率）。

- **連接整個 SDLC 至 Agent：** 將 Jira、GitHub、AWS 等工具接入 Agent，可直接指令「實作 story ABC-123」，Agent 自動拉取使用者故事與驗收條件。GitHub PR 監看與自動修復、AI 程式碼審查、Plan Mode（先生成計畫供人類審查再執行）、Grill Me 技能（逐一釐清模糊需求）、Autopilot/Automode（僅在影響系統時請求人類介入）皆為可用機制。

- **你仍然擁有程式碼的所有權：** 不能將 bug 歸咎於 Copilot 或 Claude。點擊 approve 與 merge 的是你，建構工作流程的也是你。

**關鍵概念：自我驗證迴圈（Self-Verifying Loop）**——透過 check script 賦予 Agent 自主判斷完成狀態的能力。

***

### 8. 產品負責人的 AI 應用 [27:37]

當開發速度暴增，產品端成為瓶頸。產品負責人可將 Jira、客服工單、使用者錄影、公司 OKR、分析工具接入 Agent，讓 AI 聚類回饋主題、比對需求與原始產品目標、評估故事精煉度、比對 UX mock-up 與故事一致性。Scrum 缺乏「回顧已交付功能是否達成預期效益」的正式儀式，AI 可填補此缺口。

**關鍵概念：產品迴路閉合（Product Loop Closure）**——以 AI 串聯需求生成、交付、驗證的完整迴圈。

***

### 9. 2026：迴圈之年 [29:59]

Claude Code 創造者 Boris Cherny 的願景：2024 年我們問問題，2025 年我們下指令變更程式碼，**2026 年我們創造迴圈**——從構想到 PR 到審查，全程由 AI 在交付系統中預先驗證。但 Boris 擁有近乎無限的 token 預算，多數組織需要數千美元月費才能實現此規模的自主迴圈。

**關鍵概念：自驗證交付迴圈（Self-Verifying Delivery Loop）**

***

### 10. Token 成本管理 [32:18]

Token 很可能是 SDLC 中最便宜的項目——人力成本遠高於 token。但需注意：便宜模型若需多次重做，總成本可能更高；多框架（內建 plan/verify 階段）比單獨使用 CLI 消耗更多 token；無人監看的迴圈可能失控。

管理建議：
- 在組織與個人層級設定預算上限（所有 token 供應商皆內建）
- 導入 API Token Gateway 取得儀表板、控制與細粒度報告（代價為些微延遲）

**關鍵概念：Token 經濟學（Token Economics）**

***

### 11. 安全性 [34:20]

**「安全性正處於史上最差的時刻，且只會更好。」** Anthropic 的 Mythos 模型能極快速發現開源程式庫中的漏洞；Fable 發布後因國安限制被撤回（擔心護欄被繞過）。這迫使組織將過去被降優先級的安全債務推至待辦頂端，甚至暫停功能開發以準備 Mythos 上市。正面消息是：Agentic-First 交付讓修復速度大幅提升，安全與速度的取捨正在縮小。

**關鍵概念：安全債務強制攤提（Security Debt Forcing）**——AI 漏洞發現能力迫使長期被擱置的安全議題浮上檯面。

***

### 12. 權責與治理 [36:34]

PR 審查的瓶頸：當資深工程師花大量時間審查 AI 生成的程式碼，他們會從「推動者」變成「反對者」。解法是將傳統品質閘道全部納入 CI/CD——linter、100% 測試覆蓋、突變測試、**循環複雜度（Cyclomatic Complexity）** 檢查、檔案/模組/diff 大小限制、架構規則檢查、密鑰掃描——讓資深工程師從審查「AI 產出的雜質」解放，投入更高價值工作。

Dan Shipper 的原則：**「你必須站在 AI 生成的每一行程式碼後面。不要將你未親自審查的程式碼分享給任何人。」**

治理 Agent 如同治理有系統存取權的員工：
- 最小權限、沙箱化、臨時環境
- 短期且限範圍的憑證
- 工具與 MCP Server 的允許清單
- 完整可追溯性（構想→工單→程式碼→部署）
- 所有輸入視為敵意（prompt injection）
- 供應鏈攻擊防禦：自動化依賴更新但**冷卻 7 天以上**、鎖定 lock file、使用 artifact repository
- 人類保留於不可逆動作（一Way Door Decisions）

**關鍵概念：Agent 員工治理（Agent-as-Employee Governance）**

***

### 13. 可觀測性 [43:20]

可觀測性是治理、安全與成本的基石。需要為團隊建立控制與工具，以觀察、監控、警示任何風險。控制越多，移動越快。人類的新職責是發現控制缺口並建構工具填補。

***

### 14. 衡量與成功信號 [44:08]

企業最先衡量的是「AI 採用率」（DAU/WAU），但業務利害關係人真正在乎的是：**功能使用率 → 速度 → 品質**。DORA 指標為速度與品質的基線。**產品健康度**是關鍵品質護欄——每日檢視使用者 session、錯誤率、緩慢回應、流程成功率，以及 **rage clicking（暴怒點擊）** 指標。

Tim 提出 **Precision Product Ops**（精準產品營運）概念：類似精準農業逐種子追蹤產量，在產品營運中建構更細粒度的遙測。未來可超越 A/B 測試，同時測試多個變體，以證據驅動產品決策。最終目標：**為每個功能建立損益表**，讓產品人成為產品的投資者。

**關鍵概念：精準產品營運**

***

### 15. Lighthouse Team 企業案例 [50:06]

企業內單一 Lighthouse Team 的實測數據：

| 指標 | 結果 |
|------|------|
| AI 生成程式碼比例 | 99% |
| 產出速度 | 保守估計 2x |
| 品質提升 | 10x（審查者見到的缺陷減少 10 倍） |
| 故事完成時間 | 約 15 分鐘 |
| 程式碼覆蓋率 | 98%（差 2%） |
| 每 Sprint 所需故事數 | 3x（從 15 增至 45） |

一位原本的批評者經歷後轉變為支持者，並說出：「從 coder 到 builder」——身份認同從寫程式碼的人，轉變為建造事物的人。

***

### 16. 起步方式 [51:35]

從單一團隊開始，讓 Lighthouse Team 展示可能性，其他團隊自然靠攏。Agent-Ready Assessment 提供可消化的待辦清單。搭配草根推廣（Pair programming 示範、Lunch & Learn、Teams 頻道）與領導層問責，逐步擴展。

***

### 17. Q&A 精選 [53:25]

- **角色融合：** Boris Cherny 指出開發者趨向通才化，前端/後端界線模糊；PO/BA/QA 角色可被 AI 部分吸收，團隊規模縮小但協作更緊密（每 15–20 分鐘產出一個功能，四人團隊每小時至少四個展示項目）。
- **Legacy 系統 UI 測試：** 可用 AI 生成黑箱式 end-to-end 測試（輸入→驗證輸出），建立 characterization tests 作為安全網後再重構內部。Codex 將瀏覽器嵌入工具中支援錄製回放。Playwright MCP 搭配 Axe 可做 UI 與無障礙測試。
- **Agent 編排：** 進階使用者同時開 3–5 個 session 處理多個故事；Boris Cherny 多數工作從手機指揮；GitHub App 也支援行動端編排。
- **規模化關鍵：** 遊戲化評估分數（F→A）、Pair programming 社群示範、將反對者轉化為教師、草根加領導層問責雙軌並行。
- **Agile 流程弱點放大：** AI 暴露產品決策瓶頸（需求花一個月、開發只要幾天），可同時建造 3–4 個變體以證據輔助決策。

***

## [結論與行動建議]

**啟發金句：**

> 「AI 不會創造新問題，它只會放大你已經有的問題。」

**具體行動建議——C-V-O 法則：**

- **C**overage（覆蓋）：強制 100% 程式碼覆蓋率，開啟突變測試
- **V**erify（驗證）：建立 check script 並在 `agent.md` 指示 Agent 自驗、CI 強制執行
- **O**wnership（所有權）：你擁有每一行 AI 生成的程式碼，不可歸責於工具

**生活實踐建議：**

在企業 AI 系統導入中，將 C-V-O 法則應用於 MCP Server 部署流程：為每個 Agent 技能撰寫 100% 覆蓋率的驗收測試、建立可被 Agent 自動執行的驗證腳本（含安全掃描與架構規則檢查）、並在 `agent.md` 中明確記錄 MCP Server 的允許清單與最小權限範圍。在知識圖譜建構專案中，先由 2–3 人建立本體模式接縫（Pattern Seam），再引入團隊其餘成員與 Agent，避免模式擴散。針對企業 IdP 整合等不可逆動作，始終保留人類審查關卡。

***

## [參考連結]

- 原始 YouTube 影片：https://www.youtube.com/watch?v=_CMViG3bfK0 [youtube](https://www.youtube.com/watch?v=_CMViG3bfK0)
- Agent-Ready Assessment：https://learn.leantechniques.com/agent-ready-assessment [youtube](https://www.youtube.com/watch?v=_CMViG3bfK0)
- Scott Sauber LinkedIn：https://www.linkedin.com/in/scottsauber/ [youtube](https://www.youtube.com/watch?v=_CMViG3bfK0)
- Tim Gifford LinkedIn：https://www.linkedin.com/in/timgifford/ [youtube](https://www.youtube.com/watch?v=_CMViG3bfK0)
