---
title: 'Skill：Agent的程序性記憶封裝'
date: 2026-07-12
image: /images/AI筆記/skills-masterclass.jpg
category: AI筆記
tags: [Skill, Harness工程, 程序性記憶, Sub-agent, 漸進式載入]
description: 'Skill 是代理系統中可重複載入的「程序性記憶」——它將資深工程師的審查流程（如 PR Review 的步驟、驗證、陷阱）封裝為可被 Harness 發現、載'
quote: '💡不要要求模型靠 vibes 記住工作流程。把工作流程放在 Harness 找得到、測得了、改得動的地方。'
action: '🎯用 R-P-M-E 法則（重複性/程序性/錯誤代價/非顯而易見）四項皆是才建立 Skill，否則歸入 Instructions/Tools/Sub-agents'
source_has_timestamps: true
---

# Skills Masterclass | 技術深度解析：為代理系統建構 Skills

***

## [核心摘要]

Skill 是代理系統中可重複載入的「程序性記憶」——它將資深工程師的審查流程（如 PR Review 的步驟、驗證、陷阱）封裝為可被 Harness 發現、載入並執行的結構化資產。核心價值在於：解決 AI Agent 每次面對重複任務時「重新發明流程」的問題，將專家判斷從人腦搬移到 Harness 中，使審查品質從依賴個人變為系統化、可測量、可迭代的工程實踐 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

***

## [詳細重點整理]

### 1. 問題起點：審查品質無法規模化 [00:00]

每個工程團隊都有少數幾位資深 Reviewer，他們會檢查 auth middleware 是否移動、token 缺失時的 denied path、是否執行 focused check。但他們的時間有限，無法參與每個 PR，導致審查品質不均——有些 PR 獲得深度審查，有些只確認 CI 是否綠燈 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**審查品質的不可擴展性**——核心問題不是缺乏人才，而是缺乏可重複的流程捕獲機制。

***

### 2. Skill 的定義與本質 [00:42]

Skill 不是捕捉「人」，而是捕捉流程中「可重複的部分」。它可能是一個資料夾，包含 `skill.md`、腳本、模板、範例、參考文件與測試案例。不同產品（Claude Code Skills、Codex 本地 Skills、Superpower Skills）的封裝方式不同，但本質一致：**當某類重複任務出現時，賦予 Agent 程序、約束、偏好的工具、可仿效的範例，以及證明工作完成的驗證** 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**程序性封裝（Procedural Encapsulation）**——Skill 的核心是「可重複 + 可適應」，不是固定腳本，而是可根據當前 diff 動態調整的程序。

***

### 3. 從 Prompt 到 Instruction 到 Skill 的演進 [01:36]

以「Review this PR before merge」為例，流程演進分為四個層次：

- **層次一——更好的 Prompt**：寫「Please review carefully, look for bugs, missing tests, risky changes, security issues. Be concise.」稍有改善，但程序仍在使用者腦中，每次都要重寫。
- **層次二——Instructions（`agents.md`）**：將指導放入環境中，如「Prioritize correctness, security, test coverage, avoid style-only comments」。指導是被動的——能說「遵循審查慣例」卻無法自行發現變更檔案、選擇正確測試指令或生成結構化報告。
- **層次三——Tools**：Agent 能執行 `git diff`、`pnpm test auth`、讀檔案、查 CI 狀態。但工具本身不知道何時該跑哪個指令、哪些檔案值得深查。
- **層次四——Skill**：寫下嚴肅審查的完整流程——讀描述與變更檔案、分類變更風險、執行最便宜的 focused 驗證、回報有證據支撐的發現。包含 gotchas、偏好輸出格式、甚至腳本 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**Harness 工程原語階層**——Instructions（原語 1）塑形行為、Tools（原語 4）賦予行動力、Skills（原語 9）封裝程序。三者遞進，缺一不可。

***

### 4. Skill 在 Harness 工程中的定位 [03:00]

Harness 工程地圖包含 10 個原語：Instructions、Context Delivery、Context Management、Tool Interface、Execution Environment、Durable State、Orchestration、Sub-agents、**Skills and Procedures（原語 9）**、Proof and Learning。Skill 排在 Sub-agents（原語 8）之後的原因：Sub-agent 讓工作可拆分為多個有界迴圈，但若每個 worker 各自發明流程，就會產生「平行不一致」——一個 review agent 檢查測試，另一個只做摘要，第三個漏掉 auth 邊界。**Skill 給予這些 worker 一套共享的工作方式** 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**Skill vs Sub-agent 的分工原則**——若問題是「Agent 不斷重新發明流程」，做 Skill；若問題是「需要獨立 context window 或更窄的工具邊界或平行執行」，用 Sub-agent。Skill 是程序，Sub-agent 是執行者。

***

### 5. Skill 作為程序性記憶 [10:28]

在記憶體系地圖中，Skill 屬於 **Procedural Memory（程序性記憶）**。兩張地圖不矛盾，只是視角不同：

- **Semantic Memory（語意記憶）**：儲存事實——「此 repo 的 auth middleware 在 `source/server/auth`」「團隊偏好先跑 focused test 再跑廣域 test」。
- **Procedural Memory（程序性記憶）**：儲存流程——「合併前的 PR 審查序列」。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**雙重視角下的 Skill**——從 Harness 工程看，Skill 是可被發現、載入、執行的原語；從記憶架構看，Skill 是儲存「工作應如何進行」的程序性記憶。

***

### 6. 漸進式載入（Progressive Loading）[13:32]

Skill 資料夾可以是結構化的 context 來源，但**不需要在首次載入時就全部倒入 prompt**。Context Builder 的實際工作流程：

1. 看到使用者請求「review this PR before merge」
2. 比對可用 Skill 描述，決定匹配的 Skill
3. 首次只載入 `skill.md` 的 trigger 與 process 部分
4. 若 diff 觸及 auth middleware，才進一步拉取 auth review 參考檔案
5. 若 diff 觸及 migration，才拉取 database migration 檔案

**常見錯誤**：將整個 Skill 庫當成一個巨大的 prompt。當 auth PR 只改了 40 行，模型卻在讀 8000 字的審查哲學，這是在與模型注意力競爭 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**漸進式揭露（Progressive Disclosure）**——頂層 Skill 提供通用流程，深層參考檔案按需載入。Skill 資料夾的結構決定了漸進式載入是否可行。

***

### 7. Skill 的核心元件與邊界設計 [16:12]

一個好的 Skill 應包含以下元件：

| 元件 | 說明 | PR Review 範例 |
|------|------|----------------|
| **Trigger** | 何時載入 Skill | 被要求 review PR、inspect diff、check code before merge |
| **Non-trigger** | 何時不載入 | 只需摘要 PR、寫 release notes、實作修復 |
| **Inputs** | 預期輸入 | PR URL、branch name、local diff、changed files |
| **Process** | 主流程 | 讀 context → inspect diff → classify risk → check tests → run focused verification → report findings |
| **Preferred Tools** | 偏好工具 | git diff、file reads、repo search、test runner、CI status、browser（僅 UI 變更時） |
| **Output Format** | 輸出格式 | findings 優先，含 severity、file references、evidence、suggested fix |
| **Gotchas** | 陷阱提醒 | 不要將 diff 摘要混同為 review；不要報告 style 問題除非影響正確性；不要聲稱 test pass 除非實際執行並檢查 |

Trigger 與 Non-trigger 的設計比人們預期的更重要：trigger 太模糊則 Skill 永不載入；太寬泛則在不相關任務中出現 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**Skill 邊界即系統設計**——Skill 描述不是行銷文案，它是系統的一部分，必須明確說明何時使用、何時退讓。

***

### 8. 有 Skill vs 無 Skill 的實測對比 [20:15]

同一個 PR、同一個模型、同一組工具的兩次運行：

| 維度 | 無 PR Review Skill（Run 1） | 有 PR Review Skill（Run 2） |
|------|------------------------------|------------------------------|
| **審查深度** | 淺層摘要：PR 重構 auth middleware 為 shared helper，減少重複，為 helper 生成測試 | 深層程序化審查 |
| **發現品質** | 描述正確但無實質安全發現 | 「缺少 token 的請求仍可通過 admin guard」，附檔案位置、證據、驗證結果與修復建議 |
| **價值** | 類似 diff 摘要 | 發現了真正的安全邊界缺陷 |

Skill 不讓模型全知，但讓審查路徑不再隨機 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

***

### 9. Skill 評估迴圈 [22:32]

Skill 是程序，就必須像程序一樣測試。參考 agentskills.io 的實踐框架：

- 建立真實測試任務（如 5 個 seeded PR：auth middleware 缺 denied path test、database migration drop default、前端 mobile overflow bug、API response breaking change、純重構無行為變更）
- **先跑 Baseline（無 Skill）→ 再跑有 Skill 版本**
- 捕獲 outputs、timing、token cost、grading results
- 寫斷言（assertions）：是否識別 auth 邊界變更？是否區分 blocking findings 與 suggestions？是否每個 finding 含至少一個 file reference？是否未在無驗證證據下聲稱 test pass？
- 人類審查判斷重部分：finding 是否有用？是否漏掉真實 bug？

需量測的五個指標 ： [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

| 指標 | 說明 |
|------|------|
| **Bug Catch Rate** | Skill 是否比 baseline 更常抓到 seeded issue |
| **False Positive** | 是否發明 finding 或將無害差異變成 blocker |
| **Evidence Quality** | 每個 finding 是否含 file reference、command output、test result 或清晰推理路徑 |
| **Cost** | Skill 是否讓 token 用量暴增卻只有小幅改善，還是聚焦 Agent 並節省時間 |
| **Trigger Behavior** | 是否在該載入時載入、是否在不相關任務中保持沉默 |

關鍵概念：**Skill 評估迴圈（Skill Eval Loop）**——Baseline 對照 + 斷言 + 人類判斷 + 迭代。Evals 不必把一切變成 pass/fail，但必須確保 Skill 比直覺更好。

***

### 10. Skill 的五大失敗模式 [23:20]

| 失敗模式 | 描述 | 後果 |
|----------|------|------|
| **過度寬泛（Overbroad Scope）** | 一個 Skill 涵蓋 review、testing、planning、debugging、deployment、incident response | 變成第二個 system prompt，意見太多，到處觸發 |
| **觸發不足（Undertriggering）** | 描述寫「helps with quality」，模型無法連結到「review this PR」 | 有用的 Skill 從未被載入，等同廢棄文件 |
| **程序過時（Stale Procedure）** | Repo 從 jest 改為 vitest，Skill 仍指示跑 `npm test auth`；團隊改了審批規則但忘記更新 Skill | 舊程序因「聽起來官方」而持續誤導 |
| **Context 膨脹（Context Bloat）** | 每次載入整本手冊，40 行 diff 卻讀 8000 字審查哲學 | 與模型注意力競爭，實際 diff 被淹沒 |
| **虛假信心（False Confidence）** | Skill 讓工作更可重複，但未證明工作成功 | 缺乏驗證收據（receipts），無法確認審查真正執行 |

***

### 11. Skill 是活的工件（Living Artifacts）[25:05]

Anthropic 2026 年 6 月的 Claude Code Skills 文章指出：好的 Skill 通常從小開始，隨模型碰到 edge case 而改進。Skill 的生命週期管理：

- **起步**：從一個 recurring failure 開始，加入第一個 gotcha，在真實工作上運行
- **成長**：當 Agent 漏掉某事，判斷該修正屬於 Skill、腳本、測試、Instructions 還是產品本身
- **修剪**：模型持續進步——6 個月前必要的步驟現在可能是噪音。若 Skill 只增不減，終將變成另一個 stale context dump
- **所有權治理**：需要 Registry（登記）、Owners（負責人）、Promotion Path（從 experimental → shared）、Evals（重要 Skill 的評估）、Usage Signals（區分「沒人需要」與「模型找不到」）、Deprecation（過時程序的退出機制） [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**Skill 的生命週期管理**——Skill 不是寫完即定型的文件，而是需要持續維護、修剪、評估與淘汰的活工件。

***

### 12. 建立 Skill 的法則 [27:59]

當以下四個條件同時成立時，才應建立 Skill：

1. **任務重複**——這是一個反覆出現的工作
2. **程序重要**——執行方式直接影響品質
3. **錯誤昂貴**——做錯的代價高
4. **正確行為無法從 prompt 推導**——使用者的一句話不足以產生嚴肅結果

**不應建 Skill 的情況** ： [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

- 若指引只有一句話且全域適用 → 放入 project instructions
- 若 Agent 需要一個能力 → 做或暴露一個 Tool
- 若工作需要隔離 → 建立 Sub-agent
- 若流程重複且判斷重要 → 才做 Skill

關鍵概念：**四條件法則（Four-Condition Rule）**——這個判斷框架防止 Harness 淪為「雜物抽屜」。

***

### 13. PR Review 的完整 Harness 分層組裝 [29:07]

一個 PR Review 請求在 Harness 中需要組裝多個層次協同運作：

| Harness 原語 | 在 PR Review 中的角色 |
|--------------|----------------------|
| Instructions | 設定通用行為：優先 correctness、security、test coverage |
| Context Delivery | 帶入 PR 描述、diff、變更檔案、repo rules、CI logs |
| Context Management | 決定哪些材料此刻應可見 |
| Tool Interface | 讓 Agent 檢視檔案、搜尋 repo、執行測試、查 CI |
| Execution Environment | 決定指令在哪裡跑、能碰什麼 |
| Durable State | 帶入專案慣例或先前審查教訓 |
| Orchestration | 決定何時問人、何時重試、何時停止 |
| Sub-agents | 將審查拆分為有界迴圈（security sub-agent + front-end sub-agent + test sub-agent） |
| **Skills** | **提供 PR Review 程序** |
| Proof and Learning | 要求 receipts，將漏失回饋到 Skill |

Skill 不是孤立存在的——它是 Harness 中一個與多個原語協同運作的原語 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

***

### 14. 實踐標準 [31:32]

當 Agent 在重複任務上失敗時，不應先問「模型是否夠聰明」，而應問**哪一層走到了盡頭**：

- Instruction 是否缺失？
- 相關 PR context 是否缺席？
- Context Management 是否載入了錯誤材料？
- Agent 是否有正確工具？
- 指令是否在錯誤環境中執行？
- Memory 是否過時？
- Orchestration 是否太快？
- 工作是否應被委派？
- **Skill 是否缺失？**

對 Skill 本身，問題更簡單：這是一次性請求還是重複工作流程？若是重複的，程序是否重要？能否證明 Skill 優於 baseline？誰在 repo、模型或流程變更時負責更新它？——此時工作已從 prompt craft 進入 **Harness Engineering** 。 [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)

關鍵概念：**Harness 除錯思維**——將 Agent 失敗歸因到具體原語層，而非籠統歸咎模型能力。

***

## [結論與行動建議]

> **啟發金句**
> 「不要要求模型靠 vibes 記住工作流程。把工作流程放在 Harness 找得到、測得了、改得動的地方。」

**具體行動建議——R-P-M-E 法則**：

- **R**ecurring（重複性）：任務是否反覆出現？
- **P**rocedure（程序性）：執行方式是否直接影響品質？
- **M**istakes costly（錯誤代價）：做錯是否昂貴？
- **E**mergent（非顯而易見）：正確行為無法從 prompt 推導？

四項皆「是」→ 建 Skill；否則分別歸入 Instructions / Tools / Sub-agents。

**生活實踐建議**：

- 以 PR Review 為起點：用 Skill Creator 生成初稿，描述 trigger、non-trigger、process、gotchas，然後在 5 個真實 PR 上測試 over-trigger 與 under-trigger
- 建立 Skill 的漸進式載入結構：頂層 `skill.md` 只放通用流程，auth review、migration review、front-end review 各自獨立檔案，按需拉取
- 設置評估迴圈：每個重要 Skill 配備 seeded test case，定期跑 Baseline vs Skill 對照，量測 bug catch rate、false positive、evidence quality、cost、trigger behavior
- 建立治理機制：為每個 Skill 指定 owner、設定 review cadence（月度或 test runner 變更後）、建立從 experimental → shared 的 promotion path 與 deprecation 機制
- 定期修剪：模型進步後重新評估哪些步驟已成為噪音，避免 Skill 無限膨脹

***

## [參考連結]

- 原始影片：[Skills Masterclass | Technical Deep Dive on building Skills for Agentic Systems](https://youtu.be/nrh1YtPKRD0)  [youtube](https://www.youtube.com/watch?v=ICEDgpNICjk)
