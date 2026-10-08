---
title: '用 Claude Code 建立 AI 軟體工廠'
date: 2026-10-08
image: /images/影片筆記/claude-code-ai-software-factory.jpg
category: 影片筆記
tags: [AI 軟體工廠, 多代理人品質閘門, 檔案式狀態管理, 可觀測性, 閉環式交付]
description: '本片示範以 Claude Code 在既有專案內建置可重複執行的「AI 軟體工廠」：將功能需求自動流經規格、實作、多面向審查、修正與核准合併。核心價值不是追逐大'
quote: '💡真正的 AI 開發槓桿，不是讓 Agent 寫更多程式，而是把「需求、驗證、決策與回饋」變成可重複運轉的系統。'
action: '🎯F-G-O 法則：先固定 Spec→Build→Review→Approve 端到端流程、對高風險變更強制人工核准、讓每個 job 都可觀測可追查。'
source_has_timestamps: true
---
[核心摘要]

本片示範以 Claude Code 在既有專案內建置可重複執行的「AI 軟體工廠」：將功能需求自動流經規格、實作、多面向審查、修正與核准合併。核心價值不是追逐大型框架，而是建立可理解、可調整、可觀測且保留人類關卡的自有開發流程，並用 Git worktree 支援多功能平行開發。[[youtube](https://www.youtube.com/watch?v=ctoaIC4LHmI)]

## 詳細重點整理

### 1. 軟體工廠的 Agent 工作流 [00:00]

AI 軟體工廠把功能需求視為可控管的生產單位。基本流程是：

`Feature request → Spec writer → Builder → Security / UX / UI / Code review → 修正迴圈 → Approver → Merge 或人工審核`

- 規格 Agent 將自然語言需求轉為可實作、可驗收的規格。
- Builder Agent 依規格在獨立分支上完成實作。
- 不同審查 Agent 從安全、UX、UI 與程式品質切割檢查，降低單一 Agent 自我審核的盲點。
- Approver Agent 最後根據風險決定自動合併或升級為人工核准；涉及帳務、權限等高風險領域時，應強制由人處理。[[youtube](https://www.youtube.com/watch?v=ctoaIC4LHmI)]

關鍵概念：**多代理人品質閘門（Multi-Agent Quality Gates）**

### 2. 從 CI/CD 到 Agentic Factory [02:16]

傳統 CI/CD 擅長處理可確定的流程，例如測試、建置、部署；AI 軟體工廠補足的是這些確定性步驟之間的非結構化認知工作，例如理解需求、撰寫程式、判讀 UI 問題與提出修正方案。

有效架構不是讓 Agent 直接碰 production，而是把它放在可追蹤的 Git／PR 工作流內：

`觸發事件 → Agent 執行 → 提交 PR／分支 → 檢查與審核 → 人類或規則合併`

關鍵概念：**認知工作自動化（Cognitive Work Automation）**

### 3. 用 Claude Code 建立工廠骨架 [03:48]

實作採極簡設計，以 Claude Code 的 project skill、subagent 與 Markdown 作為主要元件，而不是先引進複雜工作流平台。

建議的專案結構：

```
.claude/
  skills/
    factory/
      SKILL.md              # 編排與操作規則
  agents/
    spec-writer.md
    builder.md
    security-reviewer.md
    ux-reviewer.md
    ui-reviewer.md
    code-reviewer.md
    approver.md

factory/
  backlog.md                # 待處理需求
  jobs/<feature-id>/        # 每項工作的狀態、規格、審查結果
  dashboard/                # 可視化或狀態讀取介面
```

關鍵在於由 Claude Code 擔任 **orchestrator**：它讀取 Skill 與工作狀態，決定下一個該啟動的子 Agent。Markdown 檔則成為人與 Agent 都可直接檢視及修改的狀態層。[[youtube](https://www.youtube.com/watch?v=ctoaIC4LHmI)]

關鍵概念：**檔案式狀態管理（File-based State Management）**

### 4. 功能從需求到合併 [10:20]

實測功能為調整課程頁面的付費牆邏輯。流程中先檢查 Git working tree 是否乾淨；未提交的變更會阻止工廠啟動，避免 Agent 在不確定的基線上工作。

成功啟動後：

- Spec writer 產出功能規格檔。
- Builder 在 feature branch 上完成修改與提交。
- 多個 reviewer 平行執行；通過者回報 pass，有疑慮者要求修正。
- Dashboard 顯示目前所屬階段，包括 `needs-human`。
- Approver 判定此變更需要人工確認，使用者確認後才將分支合併回 main。[[youtube](https://www.youtube.com/watch?v=ctoaIC4LHmI)]

這個設計的重點是「自主執行不等於無人監管」：人工不必參與每個細節，但必須掌握高風險決策、合併權與回滾權。

關鍵概念：**Human-in-the-Loop**

### 5. 可觀測性與資料留存取捨 [14:40]

每個功能工作的規格、建置紀錄、審查輸出與狀態，都寫進專案內的 Markdown 檔。好處是：

- 不依賴特定資料庫或 SaaS。
- 可在編輯器、終端機、Dashboard 與 Agent 間共用。
- 可讓後續 Agent 取得工作脈絡，利於除錯與稽核。

但這類資料未必需要進 Git。若把頻繁變動的暫存狀態提交，會污染 commit history 與搜尋結果；較實際的作法是將 `factory/` 的執行期資料加入 `.gitignore`，另行備份到雲端儲存或可查詢的觀測系統。[[youtube](https://www.youtube.com/watch?v=ctoaIC4LHmI)]

關鍵概念：**可觀測性（Observability）**

### 6. Git worktree 的平行開發 [16:16]

單一 working tree 無法安全地同時讓多個 Agent 修改不同功能。導入 Git worktree 後，每個功能會有自己的工作目錄與分支，因此可同時跑多條管線，例如：

- 功能 A：撰寫規格
- 功能 B：實作中
- 功能 C：安全與 UX 審查中

這不只提升吞吐量，也避免 Agent 彼此覆寫檔案或因切換 branch 而中斷工作。影片亦指出編排模型不必一定最昂貴，但較強的模型可用於複雜決策；可將高成本模型放在規格、核准與困難修正，較快模型配置給單純任務。[[youtube](https://www.youtube.com/watch?v=ctoaIC4LHmI)]

關鍵概念：**Git Worktree 隔離**

### 7. 工廠的下一步：事件驅動閉環 [23:57]

軟體工廠的輸入不應侷限於手動輸入功能描述，可延伸為：

- GitHub Issues 作為需求入口，讓團隊成員提交且留下追蹤脈絡。
- Slack 或其他 webhook 作為觸發來源。
- 串接 Sentry，把 production 的錯誤與上下文轉為待處理工作。
- 串接 CPU、記憶體與應用指標，將部署後觀測也納入流程。
- 若新功能造成異常，工廠應能提出或執行回滾，而不是在 merge 後就結束責任。[[youtube](https://www.youtube.com/watch?v=ctoaIC4LHmI)]

關鍵概念：**閉環式交付（Closed-loop Delivery）**

## 結論與行動建議

**啟發金句：** 真正的 AI 開發槓桿，不是讓 Agent 寫更多程式，而是把「需求、驗證、決策與回饋」變成可重複運轉的系統。

**F-G-O 法則：**

- **F — Flow：** 先固定單一功能的端到端流程：Spec → Build → Review → Approve。
- **G — Guardrails：** 對帳務、權限、資料刪除、production 部署設定強制人工核准。
- **O — Observability：** 每個 job 必須有狀態、產物、審查結論與可追查日誌。

**適合你的最小可行版本：**

1. 在既有專案中新增 `.claude/skills/factory`，先只支援「輸入功能 → 規格 → 實作 → code review → 人工 merge」。
2. 把 UX／UI／Security reviewer 設為第二階段再加入，避免一開始讓 Agent 網路過度複雜。
3. 每項功能以 `factory/jobs/<id>/` 保存 [`spec.md`](http://spec.md)、[`build.md`](http://build.md)、[`review.md`](http://review.md)、[`status.md`](http://status.md)。
4. 以 Git worktree 執行平行功能，但設定同時最多 2 個 job，先觀察合併衝突與成本。
5. 將 GitHub Issue、Sentry alert 或 webhook 接為入口前，先建立明確的風險分級與自動合併政策。

對你正在探索的 MCP、webhook、Actions 與 LLM gateway 工作流，最有價值的延伸是：將 Issue／Sentry 事件正規化成同一份 feature schema，再由工廠依風險、成本與優先度決定是否啟動、派發何種模型與是否必須人工核准。

## 參考連結

- [Build Your Own AI Software Factory with Claude Code](https://youtu.be/ctoaIC4LHmI?si=rhzTmqqxRy_nMc6d)