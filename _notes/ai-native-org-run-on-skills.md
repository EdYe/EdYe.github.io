---
title: 'AI 原生組織靠 Skills 運轉：治理與規模化'
date: 2026-08-29
image: /images/AI筆記/ai-native-org-run-on-skills.png
category: AI筆記
tags: [技能治理鴻溝, 代理式軟體堆疊, 漸進式揭露, 技能技術債, C-V-G法則]
description: 'AI 原生組織的真正競爭力不在於模型能力，而在於「技能（Skills）」如何被結構化、治理與規模化。在代理式工作流中，唯一真正承載組織 know-how 的層級正是 skills。'
quote: '「沒有治理的技能不是資產，而是另一種技術債；確定性從來不來自模型，而來自結構化的知識。」'
action: '🎯依 C-V-G 法則落地：建立附 metadata 與 owner 的可搜尋技能目錄、做版本與生命週期管理讓 harness 自動拉取最新版、由 architects 與 infra／cyber leads 各自認領領域制定 policies。'
source_has_timestamps: true
source_raw: AI-Native-Organisations-Run-on-Skills
---

# AI-Native Organisations Run on Skills: How to Structure and Scale Them

**講者：** Imad Touil（QuantumBlack, Distinguished Engineer）
**來源：** AI Engineer, 2026-08-28
**時長：** 20:30

---

## [核心摘要]

AI 原生組織的真正競爭力不在於模型能力，而在於「技能（Skills）」如何被結構化、治理與規模化。在代理式工作流中，hooks 僅回應事件、sub-agents 只保護 context window、MCP servers 幾乎無人自建——唯一真正承載組織 know-how 的層級是 skills。若缺乏治理，skills 會演化為新一類技術債；若妥善治理，則讓知識變得**可執行、可移植、成本低廉**，並使工作流具備確定性。

---

## [詳細重點整理]

### 1. 三個問題的舉手表態 [00:00]

以三個遞進問題開場：誰建過 skills？（多數人舉手）→ 誰在團隊內共享？（人數減少）→ 誰在組織層級治理與維護？（寥寥無幾）。這個遞減序列正是整場演講的核心問題意識。

**關鍵概念：技能治理鴻溝（Skills Governance Gap）**

### 2. 代理式軟體堆疊：內迴圈與外迴圈 [01:33]

堆疊分為兩個迴圈：

- **內迴圈（code / agents / harness）**：context manager、tools & MCPs、memory & states、skills loader。
- **外迴圈（workflows）**：skills、sub-agents、MCP servers、hooks。

底層還有 enablement components：environment sandbox、MCP gateway（統管組織內所有 MCP 工具）、model gateway（管理開源與 frontier models）、knowledge graph（抽象 IT 核心系統、codebase、skills registry）、workflow marketplace。Context layer 則包含 project instruction（如 `CLAUDE.md`）、tools & MCP schema、conversation history、retrieved contents。

**關鍵概念：代理式軟體堆疊（Agentic Software Stack）**

### 3. specify-plan-task-implement 只是一步 [02:56]

多數 coding agents 的四步流程（specify → plan → task → implement）看似完整，但在組織規模下，它僅是「產品增量（product increment）」這一步。真正端到端的生命週期遠比此複雜。

**關鍵概念：產品增量迷思（Product Increment Myth）**

### 4. 完整生命週期的真正內涵 [04:19]

從產品策略定義（success metrics、roadmap）、市場研究與競爭分析、客戶訪談，到 discovery 階段（問題陳述、解決方案驗證、實驗、user stories），再到資料準備（data catalog 清理、端點整合）、data product delivery（data pipeline、資料品質驗證、catalog data assets），最後才進入 product increment。

**關鍵概念：端到端價值流（End-to-End Value Stream）**

### 5. 組織同時運行多個生命週期 [05:39]

單一組織內散布多個不同的 SDLC：行動應用、內部員工平台、客戶面向平台等。沒有單一 workflow 能建造一切。產品上線後還需 platform engineering ops：infrastructure as code、效能優化、事件處理，然後重新進入規劃迴圈。圖中所展示的僅是實際複雜度的 10–20%。

**關鍵概念：多生命週期並存（Multiple Concurrent Lifecycles）**

### 6. 知識真正所在之處 [07:03]

Workflows 的四個核心組件分析：

| 組件 | 角色 | 是否承載 know-how |
|------|------|-------------------|
| Hooks | 事件觸發 | 否 |
| MCP Servers | 現成工具，幾乎無人自建 | 否 |
| Sub-Agents | 委派任務以保護 context window | 否 |
| **Skills** | **結構化知識單位** | **是** |

若 skills 結構不對，workflow 從未具備確定性。Workflows 本質上是 shape coding harness 行為的「harness blueprints」。

**關鍵概念：知識落點（Know-How Residency）**

### 7. 像設計微服務一樣設計 Skills [08:27]

Skills 應遵循微服務設計原則（此問題已被 microservices movement 解決過）：

- **Reusable**：可重用
- **Modular**：模組化
- **Discoverable**：可自動發現與捕獲
- **Portable**：跨 workflow 與跨 harness（如 Claude Code → Cursor 直接可用，因為大家已採同一標準）
- **Specialized**：專一化，一個 skill 定義一個任務，不做 monolith
- **Composable**：可組合，避免執行時衝突
- **Consistent & Deterministic**：一致性與確定性
- **Cost-Efficient**：成本效率

**關鍵概念：微服務化技能設計（Microservice-Inspired Skill Design）**

### 8. 漸進式揭露與 Token 成本 [09:48]

Skills 透過 **progressive disclosure pattern**，在對的時間、放入對的數量的技能到 context window 中，解決核心問題：降低 token 使用量。這定義了一個新的知識單位——讓組織 know-how 變得**可執行、可移植、便宜**。

**關鍵概念：漸進式揭露（Progressive Disclosure）**

### 9. 將法規技能組合為稽核軌跡 [11:09]

以資料保留政策為例，法規層級需要多個可組合 skills：

- Retention policy（資料保留政策）
- Disclosure standards（揭露標準）
- GDPR rules（GDPR 合規規則）
- Fill-in templates（範本填寫）

這些被 **regulatory disclosure review workflow** 在 runtime 自動拉取，確保 web、mobile 及各應用的資料操作皆遵循法規。產出為確定性結果：可儲存的稽核報告、改善識別、回饋至 codebase 的閉環。

**關鍵概念：可組合法規技能（Composable Regulation Skills）**

### 10. 未治理的 Skills 成為技術債 [12:30]

缺乏治理會產生新一類技術債，具體表現為：

- **重複建置**：同技術棧的團隊各自重建相同 skill
- **品質衰退**：未對最新模型重新測試，僅對原始任務驗證
- **無法發現**：沒有 catalog 就無法搜尋
- **無人擁有**：沒有 owner 就無人維護與擴展
- **不可組合**：缺乏 DDD 式領域對齊，skills 互相衝突
- **安全風險**：skills 帶有 scripts（確定性執行部分），拉取 public skill 無檢查 pipeline = 供應鏈風險（含 prompt injection）
- **權限缺失**：含敏感業務邏輯的 skill 不應人人可存取

**關鍵概念：技能技術債（Skills Technical Debt）**

### 11. 中央技能平台需要什麼 [13:52]

採用路徑分三層：**Individual**（結構化建立、測試、改進、使用）→ **Team**（共享協作、快速演化）→ **Centralized Platform**。

中央平台必須具備：

- **Catalog with metadata**：可搜尋的技能目錄
- **MCP 介接 + CLI**：可從 IDE 或 sandbox 拉取 skills
- **Dependencies**：技能間依賴關係管理
- **Versioning & lifecycle**：harness 自動捕獲最新版本並拉取
- **Access control**：誰存取什麼
- **Evaluation & observability**：品質與可觀測性

**關鍵概念：中央技能平台（Central Skills Platform）**

### 12. 治理與誰擁有哪些領域 [15:14]

「技術到此為止」——治理是技術無法解決的部分。需由 architects、engineer leads、infra leads、cyber leaders 坐下來，各自擁有領域（domain），確保 skills 依組織 policies 更新。治理到位後，所有團隊從同一中央平台拉取高品質 skills，使用後改進再推回。

**關鍵概念：領域驅動治理（Domain-Driven Governance）**

### 13. 模擬 15 個團隊六個月 [16:34]

模擬設定：15 個團隊、每隊 5–12 人，追蹤 skills per engineer contribution、平均 skills utilization、跨團隊重複率、品質與安全比率。

- **未治理**：各團隊生產力、品質、安全、成本差異極大；某些團隊成本極高但品質僅中等；缺乏 regulation skill 時，工程師反覆手動引導 agent，燒 token 且耗時。
- **治理後**：出現共同基準；新工程師建 skill 時，harness 自動發現既有 skill 並拉取，幾乎解決所有治理問題。

**關鍵概念：治理模擬（Governance Simulation）**

### 14. 同樣思路套用到整個 Workflows [17:58]

Skills 只是 workflows 的一個組件，解決 skills 不等於解決 workflows。同樣的集中化、版本控管、治理方法應延伸至整個 workflows：工程師可從中央平台拉取 workflow（含所需 skills），建造、測試、改進後推回。

**關鍵概念：工作流治理延伸（Workflow Governance Extension）**

### 15. Registry、Evaluation 與 Auto-Evolving Skills [19:22]

未來三大方向：

- **Skills Registry**：應儘早建立；IDP / Internal Developer Portal 廠商已開始整合此能力。
- **Skills Evaluation**：最佳實務是對 Anthropic best practices 做靜態測試——若 skill 未被正確喚起或結構不對，品質必然低落。
- **Auto-Evolving Skills**：閉環自動演化是下一個 hype，但若無治理 guardrails，自動演化只會在無監督下放大風險。

**關鍵概念：技能自動演化（Auto-Evolving Skills）**

---

## [技術/數據對比]

### 未治理 vs 治理後 Skills 對比

| 維度 | 未治理 | 治理後 |
|------|--------|--------|
| 重複建置 | 高（同棧團隊各自重建） | 低（harness 自動發現既有 skill） |
| 品質 | 衰退（未對新模型重測） | 穩定（持續 evaluation） |
| 發現性 | 無（無 catalog） | 可搜尋（metadata + MCP + CLI） |
| 所有權 | 不明 | 清楚（named human owners） |
| 安全 | 高風險（無檢查 pipeline） | 有 supply chain 檢查 |
| 權限控管 | 缺失 | access control 依敏感度分級 |
| Token 成本 | 高（反覆手動引導） | 低（progressive disclosure） |
| 跨團隊一致性 | 差（各隊差異極大） | 共同基準 |

### Skills 設計原則（對照微服務）

| 微服務原則 | Skills 對應 | 說明 |
|-----------|-------------|------|
| Reusability | Reusable | 跨任務重用 |
| Modularity | Modular | 獨立單元 |
| Service Discovery | Discoverable | catalog + metadata + search |
| Portability | Portable | 跨 harness（Claude Code ↔ Cursor） |
| Single Responsibility | Specialized | 一 skill 一任務 |
| API Composition | Composable | 組合不衝突 |
| Consistency | Deterministic | 確定性輸出 |
| Resource Efficiency | Cost-Efficient | progressive disclosure 降 token |

---

## [結論與行動建議]

### 啟發金句

> 「沒有治理的技能不是資產，而是另一種技術債；確定性從來不來自模型，而來自結構化的知識。」

### 具體行動法則

**C-V-G 法則（Catalog → Version → Govern）**

- **Catalog**：建立可搜尋的技能目錄，附 metadata、依賴關係、owner。
- **Version**：版本控管與生命週期管理，讓 harness 自動拉取最新版。
- **Govern**：architects / infra leads / cyber leaders 各自認領領域，制定 policies 並定期對新模型重測 skills。

採用路徑：**Individual → Team → Centralized Platform → Governed Domain**。

### 生活實踐建議

- **日常工作訊號**：當你對 AI coding assistant 重複輸入相同指令模式超過 3 次，就是萃取為 skill 的訊號。立即提取、加 metadata、命名 owner，並分享至團隊。
- **領域知識可執行化**：將合規要求（如 GDPR、資料保留政策）寫成可組合 skills，讓 regulatory review workflow 自動拉取並產出稽核報告，取代人工反覆引導。
- **安全意識**：拉取任何 public skill 前，視之為供應鏈決策——必須過 security pipeline 檢查 scripts 與 prompt injection。
- **避免自動演化陷阱**：在建立 auto-evolving 閉環之前，先確保 governance guardrails 到位，否則只是無監督地放大技術債。

---

## [參考連結]

- 原始 YouTube 影片：https://youtu.be/M05vON8i0aI
- 講者 LinkedIn：https://www.linkedin.com/in/imad-touil/
