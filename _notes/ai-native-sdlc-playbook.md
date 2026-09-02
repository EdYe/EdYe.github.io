---
title: 'AI 原生 SDLC 實戰手冊：六階段戰術集'
date: 2026-09-02
image: /images/AI筆記/ai-native-sdlc-playbook.jpg
category: AI筆記
tags: [已提交產出物, 意圖擷取, 計畫模式, 代理式審查, 閉合迴圈]
description: '程式碼不再是瓶頸，瓶頸移轉到建置階段的左右兩側。AI 原生 SDLC 把六階段從線性流程改造成迴圈，每階段以提交一份版本控管產出物作結，下一階段讀取它。'
quote: '迴圈持續運轉。人類判斷力，始終在它之上。——每個階段都提交一份下個階段可讀取的產出物；意圖、規格、計畫、diff 與審查發現，合起來就是稽核軌跡。'
action: '🎯從相依圖中任一「黏土色」無前置條件的戰術起步：先把構想擷取成版本控管的 intent.md，用 CLAUDE.md 與技能固化制度知識，再以 hooks 把治理下放到代理行動的當下。'
source_has_timestamps: false
source_raw: AI-native Software Development Life Cycle
---
# AI 原生 SDLC 實戰手冊（The AI-Native SDLC Playbook）

> **原文出處**：[claude.com/blog/the-ai-native-sdlc-playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)
> **作者**：Louis Claxton
> **發布日期**：2026 年 8 月 21 日
> **分類**：企業 AI（Enterprise AI）、Claude Code
> **閱讀時間**：5 分鐘

如何一階段一階段地，用 AI 徹底改造你的軟體開發生命週期。

---

## 程式碼不再是瓶頸

各組織已經開始用 AI 以一年前無法想像的速度撰寫程式碼，然而圍繞在程式碼周邊的流程，卻沒有以同樣的速度改變。

許多工程團隊仍然沿用相同的核准關卡、審查、交接與政策，這些都在拖累使用 [Claude Code](https://claude.com/product/claude-code) 這類代理式（agentic）編碼方案所帶來的生產力提升。

軟體開發生命週期（SDLC, Software Development Lifecycle）是把軟體從構想帶到正式環境的流程。多數組織都在跑某種版本的相同六個階段：規劃、設計、建置、測試、部署與維運。傳統上，每個階段都是由不同角色所擁有的獨立階段。產品經理撰寫需求，技術架構師將其轉為設計，工程師依設計建置，受監管企業的 QA 團隊進行驗證，發布團隊負責出貨，維運團隊監控上線中的系統。工作透過文件、票證與簽核在各階段之間流轉。

傳統 SDLC 流程繁重，目的是確保每一步都有當責與控管。然而，傳統 SDLC 是為了「撰寫與實作程式碼是最耗時、最昂貴的階段」這個時代所設計的效率極大化流程——而這個前提如今已不成立。PRD、估點儀式、產品安全審查，這些都是為了在可能長達數週、數月甚至數季的開發工作中強制達成對齊而存在的。

傳統 SDLC 的控管機制也預設了每一步都由人類執行。目前產生最多價值的組織，已經圍繞「代理式 AI 現在能做到什麼」重建了他們的流程，同時確保人類仍在迴圈之中（human in the loop）。在本指南中，我們會走過 Anthropic 應用 AI 團隊（Applied AI team）在 SDLC 各階段內部整合 Claude 的多項最佳實務，用以加速開發、讓流程跑得更快——這些做法都來自與客戶合作的經驗啟發。

當程式碼不再是瓶頸、而建置階段的速度快過傳統 SDLC 所能容納時，有三件事會成立：

- **瓶頸移轉到建置階段的左右兩側。** 主要是規劃、審查／測試與部署，這些仍以人類速度在運行。
- **控管機制與現實脫節，變得難以維持。** 當程式碼是由人寫的，逐行手動審查是合理的；但一旦大部分 diff 都由代理產出，這種方式就跟不上了。
- **治理成本上升**，因為例外狀況仍需要走每週或每月才開一次的會議與委員會流程。

![建置不再是限制因素](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8739a1b934ffe55bfc9715_44592f18.png)

*圖說：建置不再是限制因素——圍繞在它周邊、以人類速度運行的步驟才是。人類速度的階段長度維持不變，而建置階段則壓縮到以小時計。*

我們以安全性瓶頸為例。安全團隊的人力配置是以人類產出為基準的，因此當代理讓程式碼產出倍增時，要嘛審查佇列不斷堆積，要嘛程式碼在審查不足的情況下就出貨。受監管的組織兩種結果都無法接受，所以它的安全與政策檢查必須跟上代理的速度。

為了更好地實現代理式 AI 的生產力紅利並確保其安全，傳統 SDLC 生命週期需要經歷與實作階段同等程度的轉型。

### 目錄

1. [程式碼不再是瓶頸](#程式碼不再是瓶頸)
2. [戰術集（Plays）](#戰術集plays)
3. [階段 1 —— 規劃（Plan）](#01-規劃plan)
4. [階段 2 —— 設計（Design）](#02-設計design)
5. [階段 3 —— 建置（Build）](#03-建置build)
6. [階段 4 —— 測試（Test）](#04-測試test)
7. [階段 5 —— 部署（Deploy）](#05-部署deploy)
8. [階段 6 —— 維運（Maintain）](#06-維運maintain)
9. [結語](#結語)

---

## 什麼是 AI 原生 SDLC？

AI 原生 SDLC（AI-native SDLC）是一個重新想像過的流程，它把舊有的控管目標與新的執行方式結合起來。流程不再是線性流動，而是變成一個迴圈，並且在每一個節點都嵌入 AI。AI 原生 SDLC 促成自動化的交接與後續戰術的觸發，有助於解決傳統 SDLC 各階段之間交接手動又笨重的問題。

你也會聽到有人把這個轉變稱為代理式 SDLC（agentic SDLC）、AI SDLC，或單純叫做代理式軟體開發（agentic software development）——名稱不同，指的是同一件事。

![AI 原生 SDLC 的循環流程圖](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8858c2eccce183e7553cf2_53b010df.png)

*圖說：AI 原生 SDLC 的六階段迴圈架構。*

### AI 原生 SDLC 六個階段的轉變

下表凸顯了傳統 SDLC 與由 Claude 支援的 AI 原生 SDLC 這兩個光譜端點之間的差異。多數組織會落在兩欄之間的某個位置。

| 階段 | 傳統 SDLC | AI 原生 SDLC |
| --- | --- | --- |
| 規劃（Plan） | 需求由委員會蒐集，透過工作坊與簽核逐步萃取，再由人工撰寫成文 | Claude 直接從來源綜整痛點，並將其擷取進 `intent.md`，該檔案既可供人類閱讀，也可供機器執行 |
| 設計（Design） | 規格由分析師撰寫，再由設計師解讀 | 需求與設計壓縮進與代理進行的單一工作階段（session），由編碼為技能（skills）的標準引導，並在 git 中版本控管 |
| 建置（Build） | 測試與程式碼皆為手寫，文件在主要開發完成後才補寫 | 測試與程式碼由 AI 產生，制度知識則以版本控管、機器可讀的 `CLAUDE.md` 檔案與技能形式維護 |
| 測試（Test） | QA 關卡設在階段交界處 | 持續評測（evals）貫穿整個實作過程 |
| 部署（Deploy） | 人類審查每一行程式碼，治理發生在審查週期中，且往往不一致 | 多層次的代理式審查，人工審查則保留給受監管與關鍵程式碼。治理在 AI 行動的當下即被強制執行，並以 hooks 作為核准關卡 |
| 維運（Maintain） | 人類盯著正式環境找 bug | 代理監控線上部署。任何被突破的控管帶（control band）都會被診斷，並以新的 `intent.md` 形式寫回迴圈中 |

貫穿右欄的主線是**已提交的產出物（committed artifact）**。每個階段都以將一份產出物寫入版本控管作結（包括 `intent.md`、`spec.md`、`plan.md`、diff 與其測試、附帶審查發現的 PR，以及事故紀錄），而下一個階段則以讀取它作為開始。在早期階段，`.md` 檔案是主要的產出物形式，因為產品負責人與代理都能讀取同一份檔案並據以行動。從建置階段開始，產出物就變成程式碼與其相關紀錄。這一連串的 commit 同時也是稽核軌跡：誰要求了什麼、代理產出了什麼、以及誰核准了它。

**人類仍需為每一個需要判斷力的決策負責。** 在代理式 SDLC 的世界裡，人類的注意力會隨著必須被審查的產出物而轉移。

> 每個階段都會提交一份下個階段可讀取的產出物。意圖（intent）、規格（spec）、計畫（plan）、diff 與審查發現，合起來就是稽核軌跡。

---

## 戰術集（Plays）

這些戰術（plays）是本手冊的核心，被分組進六個非線性的階段（規劃、設計、建置、測試、部署、維運），共同涵蓋完整的生命週期。

每個戰術涵蓋：

- 什麼會改變；
- 如何起步；
- 具體的實作步驟；
- 治理考量；以及
- 如何衡量它是否奏效。

這些步驟是模組化的，組織可以根據自身獨特需求，在不同時間點選擇優先轉型不同的階段。每個戰術都在「前置條件（Prerequisites）」下標明其相依性，相依關係圖也進一步做了說明。

一個階段以提交產出物作結，而該次 commit 則啟動下一個階段。被接受的 `intent.md` 觸發需求與設計流程，通過的 `spec.md` 觸發計畫模式（plan mode），合併的 PR 觸發流水線，而正式環境中被突破的控管帶則寫出下一份 `intent.md`，迴圈就此延續。

一開始，你會手動提示每一個步驟；而終局狀態則是一個迴圈——每一份被接受的產出物都會觸發下一道關卡。人類的注意力集中在這些關卡上，審查代理標記出來的內容，而不是從零開始每一個階段。

![戰術相依關係圖](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8855c75344623fc81efcb8_5d5a3c05.png)

*圖說：戰術依所屬階段列出；箭頭則指出採用它們的順序。兩者並不相同。可以從任何一個「黏土色（clay）」戰術開始——沒有箭頭指向它，所以它不需要任何前置條件。對於其他任何戰術，指向它的箭頭就是必須先採用的戰術。*

---

**01**

## 規劃（Plan）

構想不必再等著別人來幫忙寫成文件。意圖以發起人自己的話語一次擷取完成，成為一份下個階段可據以行動的版本控管產出物。

### 擷取為 intent.md

啟動軟體開發流程的 `intent.md` 可以透過不同途徑產生。某人有了一個構想、一張票證被建立，或是一起事故透過警報浮現（見階段 6：維運）。

當某人有了構想時，他們與 Claude 一起腦力激盪，產出一份 markdown 原型規格（proto-spec）。在傳統 SDLC 中，同一個人接下來必須說服產品團隊的某位成員與他一起、或代替他把構想寫成文件。

Claude 產生的原型規格是人類可讀、版本控管的，且下一個階段可以立即取用。這份原型規格被存為 `intent.md`。

無論意圖是源自事件觸發或是代理，適用的步驟都相同：產品負責人在 `intent.md` 被提交前，審查並修正這份由代理撰寫的檔案。

**傳統做法**
一個構想要經過待辦清單條目、使用者故事、故事點與細化會議，才會有人能對它採取行動。每一次交接都會轉移所有權，因此最終抵達工程團隊的東西，已經與發起人原本的意思相隔好幾步了。

**AI 原生做法**
發起人與 Claude 腦力激盪，並把結果寫成 `intent.md`——一份以發起人自身用語寫成的原型規格。這份產出物包含了「想要什麼」、「為什麼」以及「在什麼限制條件下」。重複性的流程則透過技能（skills）編碼下來。

#### 如何起步

**前置條件**

無。

**基礎設施**

讓非工程師也能使用 Claude（claude.ai 或 [Cowork](https://claude.com/product/cowork)）；一份大家同意的 `intent.md` 範本；一個共享、版本控管、且產品負責人會關注的意圖存放位置。對單一產品而言，最簡單的存放位置就是產品 repo 中的一個 `intent/` 資料夾。這樣的設定讓產出物鏈條緊鄰著由它衍生出來的程式碼。只有當意圖橫跨多個 repository 時，專屬的意圖 repo 才值得那些額外開銷；而在 monorepo 中，它就是一個目錄。階段 3：建置的側欄會說明這個存放位置如何與既有的 Jira 或需求管理工具（已經持有紀錄）產生關聯。

設定這件事對平台或工程團隊而言是一次性的任務。需要一位技術團隊成員來架設意圖存放位置，並決定誰可以寫入，因為會有許多貢獻者來自組織的各個角落。

一旦 repository 建立完成，沒有 git 經驗的貢獻者也不需要直接使用 git。取而代之的是，一個連到版本控管系統（例如 GitHub）的連接器（connector），讓 Claude 可以從 claude.ai 或 Cowork 代表他們提交 markdown 檔案。

#### 執行方式

1. 發起人用自己的話向 Claude 描述問題。發起人可以描述他們今天做不到什麼、誰受到這個構想影響、更好的樣子長什麼樣，或什麼不在範圍內。不需要任何正式語言。
2. 持續腦力激盪，直到構想變得具體。Claude 會問出分析師會問的問題：範圍、使用者、限制條件，以及成功的樣貌。
3. 請 Claude 使用組織的範本把結果寫成 `intent.md`——該範本可以編碼成一項由技術團隊成員設定、並經主管簽核的技能。內容可涵蓋問題、提議成果、受影響的使用者與系統、限制條件，以及待解問題。
4. 發起人修正 Claude 誤解的任何地方。
5. 將 `intent.md` 提交到共享存放位置。作者與時間戳記加入紀錄，產品負責人則從這裡接手這個構想。

```markdown
# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.

## Problem
Customers phone the contact center to ask where their claim is.
Handlers spend roughly a third of call time on status-only queries.

## Proposed outcome
Customers see claim status, next step and expected date in the portal.

## Affected users and systems
Claims handlers, portal team, claims-core API.

## Constraints
No new PII in the portal session. Existing authentication only.

## Open questions
Do third-party loss adjusters need access too?
```

> **中文參考翻譯**
> **意圖：理賠狀態自助查詢**
> 作者：J. Ortiz（理賠營運）。狀態：草稿。
> **問題**：客戶打電話到客服中心詢問理賠進度。客服人員約有三分之一的通話時間花在純查詢狀態的問題上。
> **提議成果**：客戶可在入口網站看到理賠狀態、下一步與預計日期。
> **受影響的使用者與系統**：理賠客服人員、入口網站團隊、claims-core API。
> **限制條件**：入口網站 session 中不得新增 PII。僅使用既有的身分驗證機制。
> **待解問題**：第三方公證人是否也需要存取權限？

#### 治理考量

證據就是已提交的 `intent.md`，其中列出了作者、時間戳記與完整的修訂歷史，並記錄在意圖存放位置的 git 歷史中。產品負責人負責核准，而把意圖送入階段 2：設計的「接受或拒絕」決策，則以合併（merge）或關閉審查（closing review）的形式被記錄下來。

#### 如何衡量

**領先指標（Leading indicator）**

從第一次對話到 `intent.md` 被提交所花的時間，可從意圖存放位置的 git 歷史讀出（其記錄了作者與時間戳記）。預期會從長達數週的需求誘導與細化週期，降到以小時計。

**落後指標（Lagging indicator）**

存活率——亦即產品負責人接受進入階段 2：設計、而非直接關閉的 `intent.md` 檔案佔比。接受或拒絕的決策會以產出物的合併或審查關閉來記錄。此外，還包括同一項變更中，在第一次 `spec.md` commit 之後才對 `intent.md` 所做的修改次數。

---

**02**

## 設計（Design）

需求與設計收攏進單一工作階段。政策在規格撰寫當下就被套用，而不是在數週後的審查中才被發現。

### 需求與設計

一旦獲得產品負責人核准，Claude 便接手已被接受的 `intent.md`，產出一份需求與設計規格。這個過程由組織針對品牌、安全、法遵與 UX 所建立的[技能（skills）](https://code.claude.com/docs/en/skills)引導。

產品負責人審查這份規格，但不撰寫它。這個流程的目標是產生一份工程團隊可據以規劃的規格，並標記出需要留意的地方。

前端工作是最清楚的例子。一旦 `intent.md` 被接受，產品負責人便根據 `intent.md` 在 [Claude Design](https://claude.com/product/design)（beta）中做出設計稿，反覆迭代，然後匯出到 Claude Code 進行建置。

**傳統做法**
需求與設計是由不同團隊執行的不同階段。分析師把構想形式化為需求，設計師再把那些需求解讀回設計。這種分離的存在是為了當責，但既慢又有損耗。

**AI 原生做法**
兩個階段在單一次的提示工作階段中完成。Claude 接收 `intent.md`，產出一份受組織技能約束的需求與設計規格，並標記出需要留意的地方。

#### 如何起步

**前置條件**

已撰寫 `intent.md` 檔案，且品牌、安全、法遵與 UX 政策已寫成技能。

**基礎設施**

一位擁有 Claude 存取權的產品負責人。不需要工程技能。

#### 執行方式

1. 產品負責人開啟一個工作階段，載入組織的技能，並附上 `intent.md`。
2. 產品負責人的提示要指向 `intent.md`、指名限制條件，並要求標記出疑慮。一開始先手動執行，之後將其編碼為組織層級的 slash 指令。接下來，把意圖存放位置中 `intent.md` 的接受動作設為觸發器，用一個在合併時觸發的非互動式工作，載入組織技能執行這道流程，並以 pull request 的形式提交 `spec.md`（階段 5：部署中的 CI/CD 戰術涵蓋了這些串接細節）。從那一刻起，產品負責人第一次介入的時機就是審查。
3. 同一位產品負責人對照原始構想審查規格。這份規格是否解決了所陳述的問題？`intent.md` 中的待解問題是否已被回答或往下傳遞？
4. 優先處理被標記的疑慮，因為那些正是分析師本來會往上升級的點。產品負責人要在工程團隊看到規格之前，與各政策擁有者逐一解決這些疑慮。
5. 將 `spec.md` 與 `intent.md` 一併提交。這組檔案記錄了「被要求了什麼」與「決定了什麼」。
6. 產品負責人決定規格與意圖是否推進到建置階段，並就組織歸類為較高風險的事項諮詢技術主管。這個判斷永遠由人類團隊成員做出，而接受規格就是啟動階段 3：建置中「計畫模式」戰術的動作。

#### 實際長相（提示範例）

```markdown
Read the attached intent.md and produce a requirements and design spec for integrating it into our existing codebase. Apply the skills available to you so the plan conforms to our brand guidelines, security policies and UX standards. Document the spec fully as spec.md, ready to hand to the engineering team. Describe clearly any areas of concern, especially where you cannot satisfy contradicting policies.
```

> **中文參考翻譯**：閱讀附上的 intent.md，並產出一份需求與設計規格，說明如何將其整合進我們既有的程式碼庫。套用你可用的技能，讓計畫符合我們的品牌準則、安全政策與 UX 標準。將規格完整記錄為 spec.md，準備好交給工程團隊。清楚描述任何需要留意的地方，特別是你無法同時滿足互相衝突的政策之處。

#### 治理考量

與其在數週後的審查中才被發現，現行政策在規格撰寫的當下就被讀取並套用。組織的技能被當作規格的約束條件。規格本身、產生它的提示，以及當時生效的技能版本，全都記錄在版本控管中。產品負責人簽核規格，並把被標記的疑慮轉交給指定的政策擁有者。

#### 如何衡量

**領先指標**

同一項變更中，`intent.md` commit 與 `spec.md` commit 之間的經過時間（兩個 git 時間戳記），與舊有的「需求＋設計」週期相比。

**落後指標**

建置開始後的需求返工。計算同一項變更中，日期晚於第一次 `plan.md` commit 的 `spec.md` commit 次數。Git log 可直接提供這項數據。

---

**03**

## 建置（Build）

沒有經過核准的計畫，就不實作任何東西。制度知識變成代理會讀取的檔案，而護欄以程式碼的形式運行，而非仰賴習慣。

### 以 Claude Code 計畫模式作為預設起點

工程師以[計畫模式（plan mode）](https://code.claude.com/docs/en/permission-modes)啟動 Claude Code 工作階段，把階段 2：設計中通過的 `spec.md` 交給 Claude，讓它反過來訪談自己，反覆迭代計畫直到工程師滿意為止。

**傳統做法**
工程師讀完設計就開始寫程式。變更要怎麼做、動到哪些檔案、要寫哪些測試，全都留在工程師腦中，頂多是一則票證留言。沒有其他人能審查它。審查者第一次看到的東西就是完成的 diff，到那時候返工已經很慢了。

**AI 原生做法**
工作從一份書面計畫開始，這份計畫由 Claude 在計畫模式中產出——在該模式下它可以讀取程式碼庫但不做任何變更。工程師在程式碼被寫出之前先修正計畫，通過的版本則以 `plan.md` 提交，供後續階段對照檢查。

#### 如何起步

**前置條件**

如果已有意圖產出物（`intent.md` 或 `spec.md`）則使用之，另外有 `CLAUDE.md` 檔案會有幫助。

**基礎設施**

具備 repository 存取權的 Claude Code。

#### 執行方式

1. 工程師以計畫模式與 Claude 啟動工作階段。
2. 工程師把 `intent.md` 與 `spec.md` 交給 Claude，要求一份實作計畫，內容需指名哪些檔案會變更、工作順序，以及能證明其正確性的測試。
3. 拷問這份計畫：問它這項變更可能弄壞什麼、哪一步風險最高，以及 Claude 選擇不採用的其他方案有哪些。
4. 反覆迭代，直到一位從未看過這段對話的工程師，光憑這份計畫就能實作出這項變更為止。
5. 將通過的計畫提交為 `plan.md`。這份計畫加入稽核軌跡，而 PR 審查戰術（階段 5：部署）會拿最終的 diff 與它對照檢查。
6. 接受計畫，讓 Claude 實作。有了扎實的計畫，實作往往一次就能過。
7. 當實作偏離計畫時，在同一個 commit 中更新 `plan.md`。可考慮使用 hook 來強制兩者同步。

#### 實際長相（plan.md）

```markdown
# Plan: claims status self-service (from intent.md 2026-06-02)

## Files that change
portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py,
claims-api/tests/test_status.py

## Order of work
1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.

## Risks
The claims-core API rate-limits at 50 rps; the panel must cache.

## Proof
test_status.py covers the four claim states; screenshot matches the
approved mock.
```

> **中文參考翻譯**
> **計畫：理賠狀態自助查詢**（來自 2026-06-02 的 intent.md）
> **會變更的檔案**：portal/src/claims/StatusPanel.tsx（新增）、claims-api/routes/status.py、claims-api/tests/test_status.py
> **工作順序**：1. 在既有驗證機制之後新增狀態端點。2. 針對該端點建置面板。3. 接進入口網站導覽列。
> **風險**：claims-core API 的速率限制為 50 rps；面板必須做快取。
> **證明**：test_status.py 涵蓋四種理賠狀態；截圖與已核准的設計稿相符。

#### 治理考量

設計審查發生在任何程式碼被產生之前——此時改變方向還只是編輯一份文件的事。計畫模式本身就強制了這一點，因為在工程師接受計畫之前，Claude 無法編輯檔案。計畫及其修訂版本，連同是誰接受了它，都會被記錄下來。例行變更由工程師核准，而任何組織歸類為較高風險的事項則交由技術主管或架構師處理。

#### 如何衡量

**領先指標**

第一次實作就成功合併的變更佔比，以及從計畫核准到 PR 合併的時間（所需資料存在 PR 中繼資料中）。

**落後指標**

每項變更的返工循環次數（同樣來自 PR 中繼資料），以及合併後的 diff 仍與已提交 `plan.md` 相符的頻率。

### Claude Code 自動模式

Claude Code 也可以在自動模式（auto mode）下運行——工程師核准計畫後，在滿意並經過迭代的前提下，Claude 會逐項套用變更，而不需要每次編輯都詢問。隨著後續戰術中的護欄逐漸成熟（調校過的 `CLAUDE.md`、編碼政策的技能、阻擋不安全動作的 hooks，以及 Claude 可執行的測試套件），自動接受（auto-accept）會成為例行工作的預設模式：緊湊的 `spec.md`、小範圍的影響半徑，以及測試已涵蓋的程式碼。

這個轉變的方向是，從使用者盯著代理逐項編輯並審查動作，轉向在較長的自主工作階段之後審查產出物。自動接受模式進一步讓個人與團隊在搭配 worktrees 使用時能達成平行化，這也是自主運行 SDLC、並如階段 6：維運所描述地閉合迴圈的根本要素。

---

> ### 側欄：既有系統與真實來源（Source of Truth）
>
> *適用於流程產出的每一份產出物。*
>
> 既有的 SDLC 流程很可能已經在追蹤產出物了，只是不是以 markdown 檔案的形式。工作項目可能在 Jira 中、需求在某個內建法規追溯性的工具中、設計在 Figma 中，而變更核准在變更委員會中。這些系統難以取代，因為稽核員與監管機關已經接受它們，其他團隊也依賴它們，所以 AI 原生 SDLC 必須配合既有現況。
>
> 在轉型到 AI 原生 SDLC 時，針對流程產出的每一份產出物，指定**一個**系統作為真實來源，其他所有系統則持有副本或指向原件的連結。以下配置都可以設定成單一真實來源，選擇會因產出物而異：
>
> **以 repo 作為真實來源。** Markdown 產出物是權威紀錄，既有系統則參照 commit 中的檔案。對工程主導的組織而言，這往往是最乾淨的配置之一，因為所有紀錄都存在同一個工具中，並由同一個時間戳記權威來源管理。
>
> **以既有系統作為真實來源。** Jira、ServiceNow 或需求工具持有權威紀錄，markdown 產出物則是工作副本。Claude 在工作階段開始時讀取紀錄，並在產出規格或計畫的同一個工作階段中，透過 [MCP](https://code.claude.com/docs/en/mcp) 連接器把結果寫回去。
>
> **以「連結」作為最低標準。** 所有產出物都記下紀錄 ID，所有既有系統紀錄都包含 markdown 檔案的 commit SHA。在轉型到 AI 原生 SDLC 時，連結是個不錯的起點，代價是接受存在兩個真實來源。
>
> 既有系統與 markdown 優先的系統可以並存，只要兩者之間有連結，或是其中一個被宣告為真實來源。

---

### CLAUDE.md

[`CLAUDE.md`](https://code.claude.com/docs/en/memory) 提供 Claude 一位新進成員所需要的脈絡，涵蓋慣例、指令、架構，以及團隊最常犯的錯誤。過去存在人們腦中與 wiki 上的知識，變成代理在每個工作階段開始時都會讀取的一份檔案，由整個團隊維護，並在每次犯錯後迭代改進。

#### 如何起步

**前置條件**

無。

**基礎設施**

一個 repo、已安裝的 Claude Code，以及一位非常熟悉程式碼庫的工程師。

#### 執行方式

1. 在 repo 中執行 `/init`。Claude 會根據它找到的內容產生一份初始的 `CLAUDE.md`。
2. 把產生的檔案精簡到只剩新進成員第一天需要的東西。保留建置、測試與 lint 指令、真正重要的慣例，以及 Claude 一直搞錯的事情。
3. 把 `CLAUDE.md` 簽入 git 的 repo 根目錄，讓整個團隊共用同一個版本，變更也像程式碼一樣被審查。
4. 這裡有個實用規則：當 Claude 犯同一個錯兩次時，就把修正寫進 `CLAUDE.md`。
5. 保持在一頁以內，因為 Claude 在工作階段開始時會讀取全部內容，任何過時的東西都是在白白佔用上下文。

#### 實際長相（CLAUDE.md）

```javascript
# Payments service

## Commands
- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)

## Conventions
- Java 21, Spring Boot 3. No new Lombok.
- Money is always BigDecimal, never double.
- Every endpoint needs an integration test in src/itest.

## Architecture
- api/ holds REST controllers, core/ holds domain logic,
  adapters/ talks to external systems.
- Kafka events are defined in schemas/; never edit generated classes.

## Things Claude gets wrong
- Do not bump dependency versions; the platform team owns them.
- The legacy v1/ package is frozen; changes go in v2/.
```

> **中文參考翻譯**
> **付款服務**
> **指令**：建置 `make build`；測試 `make test`（單元）、`make itest`（整合，需要 docker）；Lint `make lint`（在 CI 中執行；推送前先修好）。
> **慣例**：Java 21、Spring Boot 3，不新增 Lombok。金額一律用 BigDecimal，絕不用 double。每個端點都需要在 src/itest 中有整合測試。
> **架構**：api/ 放 REST controllers，core/ 放領域邏輯，adapters/ 負責與外部系統溝通。Kafka 事件定義在 schemas/；絕不編輯產生出來的類別。
> **Claude 常犯的錯**：不要升級相依套件版本，那是平台團隊負責的。舊版 v1/ 套件已凍結；變更請寫在 v2/。

#### 治理考量

`CLAUDE.md` 受版本控管，因此代理所依循的指令是可審查、可稽核的。團隊慣例透過這份檔案落實，對它的變更記錄在 git 歷史中，而程式碼擁有者（code owners）在 PR 審查中核准這些變更。

#### 如何衡量

**領先指標**

Claude 重複犯下 `CLAUDE.md` 本該攔下的錯誤的頻率。對 `CLAUDE.md` 的修正或變更應在 git 歷史中被追蹤。

**落後指標**

團隊新成員從加入到第一個 PR 合併所需的時間（來自 PR 歷史）。

### 技能作為制度知識

技能（Skills）是組織讓制度知識可操作化的方式。這些指令是明確的、受版本控管的、被廣泛套用的，並在政策變更時集中更新。經驗法則是：**為必須被一致套用的制度知識撰寫技能；不要為屬於 `CLAUDE.md` 或提示的組件撰寫技能。**

#### 如何起步

**前置條件**

無硬性要求。擁有 `CLAUDE.md` 會有幫助，因為它讓代理的工作知識留在 repo 中，但技能並不依賴它。

**基礎設施**

一項有指定擁有者且有書面真實來源的政策。

#### 執行方式

1. 挑一項今天執行得不一致的知識。可能是一項安全標準、一項 API 設計慣例，或一條品牌規則。
2. 把它寫成一項技能——一個包含 `SKILL.md` 的資料夾，其 frontmatter 說明何時觸發，本文說明要做什麼。由工程師依據政策擁有者的真實來源撰寫，並用 Claude 協助。
3. 把技能放在 repo 的 `.claude/skills/<name>/` 中，讓它隨程式碼一起發布；或透過[外掛（plugin）](https://code.claude.com/docs/en/plugin-marketplaces)在全組織範圍散布。
4. 測試技能是否會被觸發。用不同的說法請 Claude 執行相關任務，確認每次技能都會載入。
5. 當政策變更時，修改技能，並讓政策擁有者簽核該項變更。
6. 工程師在下一次工作階段中會自動取得新版本。

#### 實際長相（.claude/skills/secure-api-review/SKILL.md）

```markdown
---
name: secure-api-review
description: Apply the API security standard. Use whenever creating or
  modifying an external-facing endpoint, reviewing API code, or
  generating an OpenAPI spec.
---
# Secure API review

When you create or change an API endpoint:
1. Authentication: every endpoint requires the gateway JWT;
   no anonymous routes outside /health.
2. Input validation: validate request bodies against the OpenAPI
   schema and reject unknown fields.
3. Audit: every state-changing endpoint emits an audit event with
   actor, action, entity and timestamp.
4. Data classification: fields tagged pii in the schema must never
   appear in logs or error messages.

Run scripts/check-endpoints.sh and include its output in your summary.
```

> **中文參考翻譯**
> **名稱**：secure-api-review。**描述**：套用 API 安全標準。凡是建立或修改對外端點、審查 API 程式碼，或產生 OpenAPI 規格時皆使用。
> **安全 API 審查**：當你建立或變更 API 端點時：1.**身分驗證**：每個端點都需要 gateway JWT；除 /health 之外不得有匿名路由。2.**輸入驗證**：依 OpenAPI schema 驗證 request body，並拒絕未知欄位。3.**稽核**：每個會改變狀態的端點都要發出稽核事件，包含行為者、動作、實體與時間戳記。4.**資料分類**：schema 中標記為 pii 的欄位絕不可出現在日誌或錯誤訊息中。執行 scripts/check-endpoints.sh 並將其輸出納入你的摘要。

#### 治理考量

技能是一種控管機制，但屬於「建議性」的。它讓 Claude 在程式碼撰寫當下很可能套用該政策，但沒有任何機制強制工作階段必須遵守。一項必須永遠成立的政策，需要在技能背後有某種決定性（deterministic）機制支撐，例如阻擋動作的 hook，或在 PR 階段重新檢查政策的審查流程。**技能讓違規變得罕見，hook 讓違規幾乎不可能。** 技能的呼叫記錄在工作階段追蹤紀錄中，政策擁有者則像審查程式碼一樣審查技能的變更。

#### 如何衡量

**領先指標**

從政策擁有者核准政策變更，到更新後的技能被合併所花的時間（取自技能資料夾上的 PR）。

**落後指標**

PR 審查中引用該政策的發現數量——一旦技能在程式碼撰寫當下就套用政策，這個數字應趨近於零。若沒有趨近於零，那要嘛是技能沒有被觸發，要嘛是它的內容已經與官方政策產生偏移。

### Hooks 作為建置期護欄

技能是建議性控管，而 [hook](https://code.claude.com/docs/en/hooks) 則是其背後的決定性層。Claude 的大部分動作是實作過程中的檔案編輯與 shell 指令，因此建置階段往往是 hooks 觸發最頻繁的地方。

建置階段的 hooks 可以：

- 阻擋對受保護路徑的編輯，例如產生出來的類別或已凍結的套件；
- 在檔案編輯後執行格式化工具與 linter，讓偏移永遠不會累積；
- 讓憑證不會出現在 diff 中。

為任何必須無例外成立的技能政策提供後盾。Hook 會在每一個符合條件的動作上執行，所以建置階段的 hooks 應該要快，且範圍侷限在被變更的檔案上。像完整測試套件這類較重的檢查，則屬於 commit 或 PR 階段。

一個會向人類請求核准的 hook 屬於階段 5：部署中的關卡，因為在建置過程中跳出核准提示，等於把人重新放回所有平行工作階段的關鍵路徑上。

### 平行工作階段與子代理

一位工程師可以同時推進多條工作流。

**平行工作階段（parallel session）** 是另一個完整的 Claude Code 實例，在自己的 [git worktree](https://code.claude.com/docs/en/worktrees) 中處理不同的任務。每個獨立的工作階段彼此毫不知情，唯一共享的是那位在駕馭它們的工程師。

**[子代理（subagent）](https://code.claude.com/docs/en/sub-agents)** 則在單一工作階段內運行，是一個有自己上下文視窗與工具限制的受限助手，適合處理在多個任務中重複出現的工作，例如驗證應用程式是否如預期運行。

平行工作階段提高一位工程師同時進行中的任務數量，而子代理則讓每個工作階段專注在自己的任務上。工程師的工作是駕馭與審查它們全部。

**傳統做法**
一位工程師一次做一項任務，並把一天或一週中相當大的比例花在建置、測試與審查上。等待時切換到其他任務是可能的，但上下文切換的疲勞感大到很少有人會選擇這麼做。

**AI 原生做法**
一位工程師同時跑多個 Claude 工作階段，各自在自己的 worktree 中處理自己的任務。重複性的工作變成有自己上下文與工具限制的子代理。工程師的工作轉向編排（orchestrating），最終則轉向建構與監控迴圈。

#### 如何起步

**前置條件**

`CLAUDE.md`，因為所有工作階段都會讀取這份檔案。回饋迴圈（階段 4：測試）在這裡也有幫助，因為當工作階段能自我驗證時，工程師需要的監督就更少。

**基礎設施**

一個 git repository（隔離性來自 worktrees），以及調校過的權限設定，讓工作階段不會在組織認定為安全的指令上卡在核准提示。

#### 執行方式

1. 工程師把工作拆成觸及不同檔案的任務，利用計畫模式戰術（階段 3：建置）產出的計畫來看出哪些工作是彼此獨立的。共用檔案的任務則在單一工作階段中依序執行。
2. 每個平行任務都有自己的 worktree，例如在一個終端機執行 `claude --worktree feature-auth`，在另一個執行 `claude --worktree fix-rate-limit`。Worktree 是位於自己分支上的獨立 checkout，可避免工作階段在檔案上互相碰撞。
3. 兩到三個工作階段是合理的起點。實務上的上限，是一個人能好好審查多少條工作流，所以只有在審查跟得上時才增加工作階段。
4. 把重複性的工作變成子代理，定義在 `.claude/agents/` 的 markdown 檔案中，各自帶有名稱、何時使用的描述，以及它可以動用的工具。範例包括：在主代理完成後移除多餘複雜度的程式碼簡化器、實際執行應用程式並檢查行為的驗證器、以及探索程式碼庫並回報結果而不會灌爆主上下文的研究員。把這些定義簽入 git，讓整個團隊共用。

#### 實際長相（.claude/agents/verifier.md）

```javascript
---
name: verifier
description: Runs the app and checks the change works before the session
  reports done
tools: Bash, Read
---
Start the app with make run. Exercise the changed behavior and the two
nearest neighboring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

> **中文參考翻譯**
> **名稱**：verifier。**描述**：在工作階段回報完成之前，執行應用程式並檢查變更是否有效。**工具**：Bash、Read。
> 用 `make run` 啟動應用程式。實際操作被變更的行為，以及最接近的兩個相鄰流程。回報你執行了什麼、看到了什麼，以及任何與 plan.md 不符的行為。不要修任何東西；只回報。

#### 治理考量

更多工作階段意味著更多產出，因此控管必須來自 repo 中的設定。那裡的 hooks 與權限設定會套用到所有工作階段，而工作階段做了什麼都會被記錄，並歸屬到執行它的那位工程師身上。

#### 如何衡量

**領先指標**

在審查品質維持不墜的前提下，每位工程師的並行工作階段數（由 OpenTelemetry 匯出資料計算），以及一天中花在駕馭而非等待上的時間佔比。

**落後指標**

每位工程師每週合併的變更數，並搭配由 PR 歷史判定的返工率一起看。

---

**04**

## 測試（Test）

每個工作階段在人類看到之前都會先檢查自己的工作，而用來駕馭代理的設定，也會像它所產出的程式碼一樣接受迴歸測試。

### 給 Claude 一個回饋迴圈

永遠給 Claude 一個能驗證自己工作的方式，無論是測試、建置，還是螢幕截圖比對。工作階段會在工程師看到之前，先檢查自己的工作並修正自己的錯誤。

回饋迴圈不應與驗證器子代理（階段 3：建置）混淆。回饋迴圈貫穿整項任務，工作跑幾次它就跑幾次。而驗證器子代理則是打包最終檢查的一種方式——在工作階段認為工作已完成時，用一個全新的上下文視窗跑一次。如此一來，判定結果就不會被產出這段程式碼的既有假設所染色。

**傳統做法**
「程式碼可以運作」的訊號來得很晚。CI 是幾分鐘後，測試人員是幾天後，正式環境是幾週後。當程式碼是由代理產出時，遲來的訊號意味著必須有人檢查它的所有輸出，而那個人就變成了瓶頸。

**AI 原生做法**
在人看到之前，工作階段就被賦予了檢查自己工作的方式。執行測試、執行建置、截圖。Claude 反覆迭代直到檢查通過，所以抵達工程師手上的東西已經先通過了。設定這個迴圈是執行該工作階段的工程師的責任，以下步驟就是寫給他們的。

#### 如何起步

**前置條件**

無。

**基礎設施**

一套各以單一指令就能在本地執行的測試套件與建置。對於 UI 工作，讓 Claude 能看到結果至關重要，可以是瀏覽器工具，或是透過 MCP 接進來的截圖工具。

#### 執行方式

1. 如果今天檢查工作需要一連串指令加上一些環境知識，就把它包成單一目標，例如 `make test` 或 `npm test`，並在失敗時回傳非零值。
2. 在 `CLAUDE.md` 的 Commands 區塊中，列出每個指令並附上健康輸出的範例。
3. 陳述一個目標並讓它可量化，好讓 Claude 不必問你就能檢查工作，例如：「test_status.py 中的所有測試都通過」、「截圖與附上的設計稿相符」，或「端點回傳 200 且包含新欄位」。
4. 修 bug 時，先寫失敗的測試。請 Claude 把 bug 重現為一個測試、執行它，並確認它因為你預期的原因而失敗。提交那個測試。接著才請 Claude 在不編輯測試的前提下讓它通過——並用最後一步的測試檔 hook 來強制這項限制。一個在修復前就存在、且代理無法改寫的測試，就是 bug 已經消失的證明。
5. 對於 UI 工作，用視覺檢查閉合迴圈。給 Claude 一個瀏覽器或截圖工具、給它設計稿，讓它反覆迭代：實作、截圖、比對、調整。兩三輪是正常的，而且每一輪結果都應該更好。
6. 讓驗證成為「完成」定義的一部分。指令寫在 `CLAUDE.md` 中：在回報任務完成之前執行測試，並秀出輸出。
7. 最後，迴圈本身也需要保護，因為一個在修程式碼的代理，絕不能有能力削弱針對那段程式碼的檢查。一個在修復任務期間阻擋編輯測試檔的 hook 可以做到這點。另一種做法是在審查時檢查 diff，並拒絕任何動到測試的變更。

#### 實際長相（CLAUDE.md 的驗證區塊）

```javascript
## Verifying your work

- Build: make build (must finish with "Build succeeded")
- Test: make test (all green; never skip or delete a failing test)
- Lint: make lint (zero warnings)

Run all three before reporting any task complete, and paste the output.
If a test fails, fix the code, not the test.
```

> **中文參考翻譯**
> **驗證你的工作**
> 建置：`make build`（必須以 "Build succeeded" 結束）。測試：`make test`（全綠；絕不跳過或刪除失敗的測試）。Lint：`make lint`（零警告）。
> 在回報任何任務完成之前，執行這三項並貼上輸出。若測試失敗，修的是程式碼，不是測試。

#### 治理考量

**強制執行什麼**

任務回報完成前必須先驗證，以及在修復任務期間阻擋代理編輯測試檔——當組織希望這兩點有保障時，皆以 hooks 實作。

**證據是什麼**

Claude 實際執行並貼出的 `make test` 原始輸出、建置日誌，或截圖比對結果，因此證據來自工具鏈本身。

**記錄在哪裡**

在工作階段的逐字紀錄中（由 OpenTelemetry 匯出轉送到組織的可觀測性堆疊），以及 PR 的檢查執行紀錄中——審查者與後續任何稽核員都能看到。

**由誰核准**

審查該 PR 的程式碼擁有者。因為機械性的證據已經附上，他們可以專注在意圖與風險上。

#### 如何衡量

**領先指標**

代理撰寫變更的首次 CI 成功率，這是 CI 系統本來就支援的。

**落後指標**

每個 PR 的審查時間（來自 PR 中繼資料）——一旦測試接住了過去要靠審查者接住的問題，這個數字應該會下降；以及來自事故追蹤系統的變更失敗率。

### CI 中的持續評測

評測（Evals）是階段關卡式 QA 的 AI 原生對應物。實務上，這意味著一套會在代理設定變更時執行的測試套件。當換上新模型或改寫提示時，評測套件會告訴你代理是否仍以相同標準完成工作。

評測應被視為一套「活的」套件。隨著模型進步，曾經具鑑別度的案例會失去鑑別度，必須從持續監控中衍生出新的案例補進來。

依使用情境不同，有些團隊可能偏好以固定節奏離線執行這些評測，而非在每次變更時執行。以下步驟是針對持續評測的做法。

#### 如何起步

**前置條件**

`CLAUDE.md` 與回饋迴圈（階段 4：測試）。

**基礎設施**

能以非互動方式執行 Claude Code 的 CI，以及一把有評測執行預算的 API key。

#### 執行方式

1. 平台工程師從近期工作中蒐集 20 到 50 項真實任務，連同其預期／可接受的結果。
2. 把每項任務寫成一個評測，也就是提示加上定義「可接受」的檢查項（測試通過、lint 乾淨、行為未改變、政策被遵守）。
3. 套件在 CI 中以非互動方式，依排程執行，並在 `CLAUDE.md`、技能或 hooks 有任何變更時執行——因為這些設定在駕馭代理，理應接受程式碼所享有的迴歸測試。
4. 以結果作為設定變更的關卡。會拉低通過率的技能變更，必須先經審查才能合併。
5. 每一起正式環境事故都要產出一個評測，由擁有該事故的團隊撰寫，並作為迴歸測試留在套件中。

#### 實際長相（.github/workflows/agent-evals.yml）

{% raw %}
```yaml
name: Agent evals
on:
  pull_request:
    paths: ['CLAUDE.md', '.claude/**']
  schedule:
    - cron: '0 2 * * *'
jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - name: Run eval suite
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for eval in evals/*.json; do
            claude -p "$(jq -r '.prompt' $eval)" \
              --allowedTools "Read,Edit,Bash(make test)" \
              --output-format json > result.json
            ./evals/check.sh "$eval" result.json
          done
```
{% endraw %}

#### 治理考量

評測給了 QA 一道跟得上代理產出速度的關卡。通過率門檻以合併檢查（merge check）的形式強制執行，每次執行都會被記錄以便跨時間比較結果，而擁有該項設定變更的團隊負責核准它。

#### 如何衡量

**領先指標**

評測通過率隨時間的變化（套件每次執行都會回報），以及一起正式環境事故需要多久才會變成一個常設評測。

**落後指標**

在 CI 中攔截到的迴歸數量，對比在正式環境中發現的迴歸數量（來自事故追蹤系統）。

---

**05**

## 部署（Deploy）

審查雙向運行，治理在代理行動的當下就被強制執行。代理可以做到正式環境關卡為止的一切，但不能跨過它。

### PR 審查迴圈中的 AI

Claude 既給予審查，也接受審查。它依組織政策審查進來的 PR，也處理自己 PR 上收到的審查意見。這讓工程師在 PR 審查中能專注於行為本身，歸結起來就是判斷意圖與風險。

**傳統做法**
審查量能是依人類產出來規劃的。一個 PR 要等審查者把它全部讀完，審查品質隨審查者的負載而變動，作者不斷催促，而積壓則持續增長。

**AI 原生做法**
所有 PR 都經過同一組審查流程，發現依嚴重程度排序。人類的注意力上移一個層級，去看這項變更是否做到了計畫所意圖的事，以及風險是否可接受。

#### 如何起步

**前置條件**

來自階段 3：建置的更新版 `CLAUDE.md`；若審查流程要落實書面政策則需要技能，以及已定義的子代理。

**基礎設施**

一個已安裝 Claude 整合的 repo——可以是由管理員啟用的託管式 [Code Review](https://code.claude.com/docs/en/code-review)（研究預覽）服務，或是在你自己的 CI 中執行的 [claude-code-action](https://code.claude.com/docs/en/github-actions)，並在需要時透過 AWS Bedrock、Google Vertex 或 Microsoft Foundry 進行模型呼叫（CI/CD 戰術涵蓋了部署選項）。要求程式碼擁有者核准的分支保護政策也很值得設置。

#### 執行方式

1. 託管式 Code Review 服務是最快的起步方式。管理員啟用它並選取 repositories。當你需要掌控流水線，或希望 API 呼叫透過自己的雲端合約時，則用 claude-code-action 在自己的 CI 中執行審查（CI/CD 戰術涵蓋了這些串接細節）。
2. 技術主管在 repo 根目錄撰寫審查政策 `REVIEW.md`，依組織在意的審查面向分區：bug 與邏輯錯誤；安全性與漏洞；以及對規格（需求戰術的 `spec.md`）、實作計畫（計畫模式戰術的 `plan.md`）與設計原則的符合度。`REVIEW.md` 也定義了什麼算是「重要（Important）」而非「吹毛求疵（Nit）」，以及什麼該略過。
3. 技術主管設定人工介入門檻。審查發現本身不會核准或阻擋 PR，分支保護仍要求程式碼擁有者的核准。若平台工程師想以發現數量作為合併關卡，可以讀取檢查執行所發布的機器可讀嚴重度統計。
4. 當審查者或作者在審查留言上標記 `@claude` 時，Claude 會處理該留言並推送修正。PR 討論串同時記錄了請求與變更。這個修正迴圈透過 claude-code-action 運行。在託管服務中，留言 `@claude review` 則是請求一次全新的審查。對於由 Claude 開啟的 PR，還可以更進一步，讓 Claude 一路把 PR 顧到合併。有些團隊把這個迴圈包成自訂的 slash 指令，掃過 PR 上未解決的審查留言與失敗的檢查，處理它們並推送修正，直到 PR 全綠、只等程式碼擁有者核准為止。
5. 審查發現回饋進 `CLAUDE.md`。當審查第二次標記出同一個錯誤時，該項修正就在該次審查中被寫進 `CLAUDE.md`；而因為審查會讀取 `CLAUDE.md`，這個錯誤從下一個 PR 起就會被攔下。審查也會標記出某項變更已讓 `CLAUDE.md` 過時。
6. 技術主管每月調校一次設定，透過對審查發現評分讓審查者變得更好，並在 `REVIEW.md` 中限制吹毛求疵的數量。產生出來的路徑，以及任何 CI 已經在強制執行的項目，都應排除在外。

#### 實際長相（REVIEW.md）

```markdown
# Review instructions

## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles

## What Important means here
Reserve Important for findings that would break behavior, leak data
or breach a policy. Style and naming are nits.

## Cap the nits
Report at most five nits per review; summarize the rest as a count.

## Do not report
Generated files under src/gen/ and anything CI already enforces.
```

> **中文參考翻譯**
> **審查指示**
> **審查面向**：執行三個面向，並為每項發現標記所屬面向——Bug：邏輯錯誤、壞掉的邊界情況、隱微的迴歸；安全：注入風險、身分驗證漏洞、日誌中的 PII；合規：變更符合 spec.md、plan.md 與我們的設計原則。
> **這裡「重要」的定義**：「重要」保留給會破壞行為、洩漏資料或違反政策的發現。樣式與命名屬於吹毛求疵。
> **限制吹毛求疵的數量**：每次審查最多回報五項；其餘以數量摘要呈現。
> **不要回報**：src/gen/ 底下產生出來的檔案，以及任何 CI 已經在強制執行的項目。

#### 治理考量

職責分離被保留下來，因為撰寫程式碼的代理沒有任何途徑可以核准它。`REVIEW.md` 中的審查政策套用到所有 PR，而發現、修正、評分與核准都記錄在 PR 歷史中，因此 PR 就是稽核紀錄。核准來自人類，透過分支保護機制，並以審查發現作為判斷依據。

關於這些控管在正式環境規模下如何組合運作，請參見 [Anthropic 如何確保其 AI 原生 SDLC 的安全](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)。

#### 如何衡量

**領先指標**

首次審查所需時間（應降到以分鐘計），以及不需人類碰觸分支就解決的審查留言佔比（資料直接存在 Git 中）。

**落後指標**

合併前攔截到的缺陷與漏洞數，對比逃逸到正式環境的數量（來自 PR 歷史與事故追蹤系統）。

### Hooks 作為核准關卡

建置階段把 hooks 當作護欄使用，在沒有人類介入的情況下允許或阻擋動作（階段 3：建置）。Hook 也可以「詢問」，暫停動作直到特定人員核准——這正是發布關卡所需要的。

這個戰術放在階段 5：部署，是因為發布關卡是最清楚的案例；但 hooks 並非部署專屬：Claude 在哪裡行動，它們就在哪裡運行。舉例來說，hooks 可以在階段 3：建置期間阻擋沒有變更票證的 migration 與基礎設施編輯，也可以在階段 4：測試期間阻止代理在修復任務中編輯測試檔。

#### 如何起步

**前置條件**

無。

**基礎設施**

一份書面清單，列出變更流程所需的各項核准。

#### 執行方式

1. 工程領導層會同變更管理與法遵單位，列出必須保留的人工核准關卡，例如變更管理簽核、發布授權，以及對受保護路徑的編輯。
2. 平台工程師把每一道關卡表達為一個 hook——一段在 Claude 行動前執行的腳本，可以允許、詢問或阻擋。
3. 團隊層級的 hooks 放在 git 中的 `.claude/settings.json`，不可協商的 hooks 則放在由平台或 IT 管理員擁有的託管設定（managed settings）中，個別工程師無法將其關閉。
4. 阻擋時應該說明理由，因此當 hook 攔下一個動作時，原因與取得核准的途徑都會出現在 Claude 的輸出中。

#### 實際長相（.claude/settings.json）

```json
{
    "hooks": {
      "PreToolUse": [
        {
          "matcher": "Bash",
          "hooks": [
            { "type": "command",
              "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh" }
          ]
        }
      ]
    }
}
```

#### 關卡本身（.claude/hooks/production-gate.sh）

```bash
#!/bin/bash
# Production deploys require a named release authorization
cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
   if [ -z "$RELEASE_APPROVAL" ]; then
     echo "Production deploys need a release authorization." >&2
     exit 2 # exit 2 blocks the action; the message goes to Claude
   fi
fi
exit 0
```

> **中文參考說明**：正式環境部署需要一份具名的發布授權。若指令同時包含 `deploy` 與 `production` 且 `RELEASE_APPROVAL` 為空，就輸出「正式環境部署需要發布授權」並以 exit 2 阻擋該動作（exit 2 會阻擋動作，訊息會傳給 Claude）。

#### 治理考量

Hooks 就是核准關卡。關卡條件每一次、對每個人都會被強制執行。允許與阻擋的決策都附帶時間戳記被記錄下來。關卡也定義了什麼算是核准——無論那是一張已核准的變更票證，還是發布經理的簽核。

---

> ### 實例演練：受監管企業的託管設定
>
> *由平台團隊透過 MDM 或管理主控台部署；工程師無法編輯或覆寫其中任何一項。*
>
> ```json
> {
>   "permissions": {
>     "deny": [
>       "Read(.env*)", "Read(./secrets/**)",
>       "WebFetch", "Bash(curl *)", "Bash(wget *)"
>     ],
>     "allow": [
>       "Bash(git *)", "Bash(make build)",
>       "Bash(make test)", "Bash(make lint)"
>     ],
>     "disableBypassPermissionsMode": "disable"
>   },
>   "allowManagedPermissionRulesOnly": true,
>   "sandbox": {
>     "enabled": true,
>     "failIfUnavailable": true,
>     "allowUnsandboxedCommands": false,
>     "network": { "allowedDomains": ["git.internal.example.com",
>                  "registry.npmjs.org"] },
>     "credentials": {
>       "files": [
>         { "path": "~/.ssh", "mode": "deny" },
>         { "path": "~/.aws/credentials", "mode": "deny" }
>       ],
>       "envVars": [ { "name": "GITHUB_TOKEN", "mode": "deny" } ]
>     }
>   },
>   "allowManagedHooksOnly": true,
>   "disableSideloadFlags": true,
>   "allowManagedMcpServersOnly": true,
>   "strictKnownMarketplaces": [
>     { "source": "github", "repo": "example-corp/approved-plugins" }
>   ],
>   "requiredMinimumVersion": "2.1.193"
> }
> ```
>
> **從控管角度看，每一行買到了什麼**
>
> `permissions.deny` 讓密鑰不進入代理的上下文，並阻擋透過工具進行的任意網路外連；`permissions.allow` 則預先核准安全的內圈工作，讓拒絕清單不至於演變成提示疲勞。
>
> `disableBypassPermissionsMode` 加上 `allowManagedPermissionRulesOnly`，意味著沒有任何工程師、專案檔案或命令列旗標能放寬這些規則。
>
> `sandbox` 補上權限機制補不了的缺口。工具層級對 WebFetch 的拒絕，並不能阻止 shell 指令連上網路；作業系統層級的網域白名單則直接阻斷外連。
>
> `failIfUnavailable` 與 `allowUnsandboxedCommands` 讓沙箱成為一道關卡：當沙箱無法初始化時，Claude Code 拒絕啟動；而在沙箱內失敗的指令，也無法拿到沙箱外重試。
>
> `credentials` 補上拒絕規則留下的缺口。`permissions.deny` 管的是 Claude 的檔案工具，但沙箱化的 shell 指令預設仍可能讀取 `~/.ssh` 或 `~/.aws/credentials`；這個區塊拒絕那些讀取動作，並從每一個沙箱化指令的環境中剝除指名的密鑰。
>
> `allowManagedHooksOnly` 意味著本戰術中的核准關卡是唯一會執行的 hooks；沒有任何本機設定能新增或取代它們。
>
> `disableSideloadFlags` 與 `strictKnownMarketplaces` 意味著工程師機器上的每一項技能、代理、hook 與 MCP server，都是透過組織核准的外掛市集而來，絕不會來自家目錄。
>
> `allowManagedMcpServersOnly` 讓代理的工具表面成為一份由平台團隊擁有的白名單。
>
> `requiredMinimumVersion` 拒絕在低於核准下限的版本上啟動，因此這些控管是由組織確實評估過的建置版本所強制執行的。
>
> 請把上述內容當成待客製的起點，而非照抄的建議。每一項拒絕都在與能力做取捨，正確的平衡點取決於該 repo 的資料分級。設定參考文件記載了每一個鍵值，包括僅限託管使用的那些：[code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings)

---

#### 如何衡量（針對 hooks 本身）

**領先指標**

在每一道核准關卡上等待的時間。每個 hook 決策都會附帶時間戳記與允許／阻擋判定寫入 OpenTelemetry 匯出資料，因此每道關卡的等待時間都是可見的。

**落後指標**

導入 hooks 前後，抵達正式環境的關卡違規數（來自事故追蹤系統）。

### CI/CD 整合與部署

在 CI/CD 流水線內以非互動方式執行 Claude Code，把執行環境沙箱化好讓長時間運行的代理安全運作，透過 MCP 整合暴露部署能力，並在代理真正需要之前先演練好回滾路徑。

**傳統做法**
流水線執行決定性的腳本，任何需要判斷力的事情都要等人。例如：分診不穩定的測試、撰寫變更日誌，或釐清建置為何壞掉。部署與回滾則是人在壓力下依循的操作手冊。

**AI 原生做法**
Claude 在流水線內以非互動方式執行那些需要判斷力的步驟，在具備受限憑證的沙箱中運行。部署工具透過 MCP 暴露給代理，因此撰寫並測試該項變更的工作流程，也能在組織依環境定義的關卡內把它出貨並回滾。

#### 如何起步

**前置條件**

PR 審查迴圈中的 Claude，以及 hooks 作為核准關卡——因為關卡必須先存在，自動化才不會加速任何東西闖過去。

**基礎設施**

已安裝 claude-code-action 的 CI 平台，或任何能呼叫 `claude -p` 的 runner；透過 API 取得模型存取權，或在流量必須留在組織雲端合約內時使用 Bedrock、Foundry 或 Vertex；對應部署目標的 MCP servers；以及一個沒有常駐正式環境憑證的代理工作沙箱設定檔。

#### 執行方式

1. 平台工程師從唯讀的判斷步驟開始。在流水線工作中使用 `claude -p` 來分診失敗的建置、摘要不穩定的測試，或草擬變更日誌。
2. 在既有關卡之後加入寫入步驟，例如修 lint、更新產生的文件，或透過 `@claude` 標記處理審查留言。代理寫出的任何東西都會以 PR 形式經過分支保護抵達，代理沒有任何途徑可以推送到 main。
3. 執行環境要沙箱化。代理工作在容器中、依網路政策、使用短期受限 token 運行，且預設不持有正式環境憑證。
4. 透過 MCP 暴露部署能力。部署、狀態查詢與回滾成為工具，並依環境限定範圍，因此代理的部署權力是一份白名單，而不是一支帶著憑證的 shell 腳本。
5. 依環境分級自主程度。在開發環境中，代理可以自由部署。在正式環境中，代理準備發布、由發布經理授權，並由 hook 強制執行正式環境關卡。預備環境則落在中間。
6. 回滾應該是流水線中演練得最熟的路徑——一道代理可以執行、且在預備環境中定期演練的單一指令。閉合迴圈戰術（階段 6：維運）會在控管帶被突破時呼叫這個回滾，所以它必須事先被驗證過。

#### 實際長相（流水線步驟）

```markdown
- name: Triage failed build
  if: failure()
  run: >
    claude -p "Read the build log at out/build.log. Identify the most
    likely cause, say whether the failure looks flaky or real, and write a
    three-line summary for the PR thread." >> triage.md
```

> **中文參考翻譯**：名稱：分診失敗的建置。條件：失敗時執行。指令：`claude -p "閱讀 out/build.log 的建置日誌。指出最可能的原因，說明這次失敗看起來是不穩定（flaky）還是真的問題，並為 PR 討論串寫一段三行摘要。"`

#### 治理考量

治理原則是：**代理可以行動到正式環境關卡為止，但不能通過它。** 以下控管落實這項原則。

- 分支保護把代理寫出的任何東西變成 PR，沒有直達 main 的路徑。
- 正式環境部署 hook 會阻擋發布，直到具名的發布經理授權為止。每一次非互動執行都以代理自身的身分進行，因此流水線日誌能區分代理做了什麼、與觸發它的工程師做了什麼。
- 依環境分級的權限，設定代理在抵達關卡的路上可以做多少事。

#### 如何衡量

**領先指標**

未呼叫人類就完成分診的流水線失敗佔比（取自 CI/CD 流水線日誌）。

**落後指標**

DORA（DevOps Research and Assessment）指標，這是 CI 系統與部署工具本來就會產出的。

---

**06**

## 維運（Maintain）

迴圈就此閉合。一個觸發器在無人介入呼叫路徑的情況下喚起 Claude，而它所發現的東西則以 `intent.md` 的形式重新進入流水線。

### 維運與閉合迴圈

到目前為止，我們討論的是如何把 Claude 加進 SDLC 流程的每一個階段，而每個階段都需要人類啟動最初的步驟。然而，這個階段把焦點轉向讓 Claude 自主運行，以閉合迴圈。

舉例來說，一個持續運行的監控代理，可以在一張 bug 票證被提出後，建立一份 `intent.md`，並流經需求、計畫、建置、測試與審查各階段。階段 6：維運以無介面（headless）方式運行，各階段之間有獨立的信心關卡（confidence gate）——可以是決定性的檢查，或是一個對抗性的審查代理——來決定上一階段的輸出是繼續往下走，還是升級交給人類。

**傳統做法**
維運是被動的階段。所有票證或事故都在等一個人採取行動、重啟流程。警報在凌晨三點響起，可能被錯過；票證可能躺在待辦清單裡直到有人撿起來；而若另一場火先燒起來，事後檢討的行動項目可能根本沒進到程式碼庫。

**AI 原生做法**
一個觸發器——例如控管帶被突破、一張票證、一則頻道訊息或一份排程——在無人介入路徑的情況下喚起 Claude。Claude 進行診斷、只透過有關卡的途徑行動，並把它發現的東西寫成 `intent.md`，接著就走完上述各階段。人們負責分診與審查那份工作，而不必再去啟動它。

### 閉合迴圈

一支決定性的腳本監看正式環境，並在控管帶被突破時喚起 Claude。突破監控是這個自主運行迴圈模式的一個有用範例，而本階段末尾的 [Claude Tag](https://claude.com/product/tag)（公開 beta）章節則涵蓋透過不同管道抵達的工作。

#### 如何起步

**前置條件**

`intent.md`，它給了迴圈一個可以重新啟動的結構化輸出。以及 Claude 加速的 PR 審查、作為動作邊界的 hooks，還有 CI/CD 的回滾路徑（最高自主層級會呼叫它）。

**基礎設施**

一個偵測腳本可查詢的指標儲存庫（Prometheus、CI 系統的 API 或同等物）、對 repository 的讀取權限、一個在 CI 中以非互動方式執行 Claude Code 的方式，或用 [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) 建立一個接收 webhook 的服務。

#### 執行方式

1. 服務擁有者或平台工程師挑選一項具備穩定滾動基準線的指標，例如 CI 測試失敗率、部署後 5xx 比率，或 PR 週期時間。
2. 他們撰寫偵測腳本，通常是滾動視窗上的平均值與標準差，搭配規則（Western Electric 或類似規則），讓控管帶既能抓到尖峰、也能抓到緩慢的偏移。腳本受版本控管並有單元測試，而偵測維持完全決定性，不涉及任何模型。
3. 回應層級定義在版本控管的設定中（下方的 `bands.yaml`）。在 1σ 時腳本只記錄；在 2σ 時它以唯讀方式喚起 Claude 進行診斷；在 3σ 時 Claude 可以行動，但僅限於開啟一個進入審查關卡的 PR，或觸發預先核准的操作手冊。
4. 觸發層可以是 GitHub 或 GitLab 中的排程工作流、既有監控堆疊發出的 webhook，或網路內的 Cron Job。Claude 以無狀態方式運行，可以是 CI runner 上的非互動步驟，或是沙箱化容器中的 Agent SDK 服務——CI/CD 戰術涵蓋了部署與模型存取的選項。因為執行是無狀態且非互動的，一個迴圈可以在沒有任何人啟動的情況下開始與結束。
5. 代理以階段 1：規劃的格式把診斷結果寫成 `intent.md`，涵蓋異常狀況與其證據、提議成果、受影響系統，以及任何待解問題。從那裡，這項發現就像其他任何東西一樣走過整條流水線。
6. 服務擁有者或值班工程師分診這個佇列，把面向產品的發現轉給產品負責人。選擇立即修復、排程處理，或駁回。駁回會用來調校控管帶，並有助於降低噪音。
7. 當修復上線後，為該起事故新增一個評測（見持續評測戰術），確保未來能防範這類問題。

#### 實際長相（例如監控 CI 測試失敗率的 bands.yaml）

```yaml
metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
  1sigma: { action: log }
  2sigma: { action: diagnose,
            tools: "Read,Grep,Bash(gh run view *)" }
  3sigma: { action: propose,
            routes: [pull_request, runbook:rollback-deploy] }
```

#### 治理考量

層級邊界由版本控管的設定強制執行，並以權限與託管設定拒絕正式環境存取。呼叫、發現與分診決策都附帶時間戳記被記錄。服務擁有者負責分診與核准發現，由此產生的變更走一般的 PR 審查關卡，而代理可以觸發的操作手冊都是事先核准過的。

#### 如何衡量

**領先指標**

從控管帶被突破到 `intent.md` 進入分診佇列所需的時間，對比舊有從事故到事後檢討行動的時間。偵測腳本的日誌記錄了突破的時間戳記與事故層級。

**落後指標**

最終成為已合併修正的發現佔比（分診佇列對比實際 PR 歷史），以及同類事故的重複發生率——隨著修正把案例加進評測套件，這個數字應該會下降。

#### 範例

- 當 CI 測試失敗率突破 3σ 時，代理隔離該不穩定測試或開啟一個 revert PR，由審查關卡決定。
- 當部署後 5xx 比率在有部署發生的時間窗內突破 3σ 時，代理觸發既有的回滾流水線。
- 當 PR 週期時間觸發偏移規則時，代理為工程領導層撰寫一份報告——這顯示這套框架不只對正式環境指標有效，對流程指標同樣有效。

偵測維持決定性。Claude 只在控管帶被突破後才被喚起，而層級決定了它可以做什麼。

### 週期性程式碼庫掃描

一次安全掃描，是在特定模型之下、對某個程式碼庫在某個時間點的陳述——而這兩半都會過期：程式碼每週都在變，而每一代模型都會找到前一代漏掉的漏洞。AI 原生的答案是：讓掃描依排程執行、呼叫路徑中沒有人類，並讓它找到的東西走過與程式碼庫任何其他變更相同的關卡。

[Claude Security](https://claude.com/product/claude-security) 是排程掃描的託管形式。連接一個 GitHub repository，掃描便在 Anthropic 的基礎設施上以 Claude Mythos 5 執行，每一項發現在被回報前都經過驗證，並附上信心評分。建議的修補程式則在網頁版 Claude Code 中審查與套用。組織能取得這些發現，而不需要取得模型本身的存取權。

**傳統做法**
安全掃描是一個事件——在發布或稽核前啟動一次掃描。報告送進追蹤系統，待辦清單靠人工逐項處理，直到下一個事件。這期間寫的程式碼，只由 PR 審查所能攔下的東西來覆蓋。

**AI 原生做法**
掃描依排程對每一個已連接的 repository 執行，使用當前最強的模型，發現在任何人閱讀之前就先經過驗證。每一項發現的處理方式與被突破的控管帶相同：能塞進一個 PR 的修正走審查關卡，任何更大的東西則變成一份 `intent.md`。覆蓋率的日期是從最近一次執行算起，而不是從第一次算起。

#### 如何起步

**前置條件**

PR 審查關卡與作為核准關卡的 hooks（階段 5：部署），好讓發現像其他任何變更一樣走過審查。以及階段 1：規劃的 `intent.md` 格式，供大到單一 PR 裝不下的發現使用。

**基礎設施**

Claude Security 以公開 beta 形式提供給 Claude Enterprise 組織。它需要在目標 repositories（雲端託管的 github.com）上安裝 Anthropic GitHub App、啟用網頁版 Claude Code、開啟 Extra Usage 並設定支出上限、為執行掃描的人員配置 premium 席次，並由管理員在 `claude.ai/admin-settings/claude-code` 開啟此功能。掃描依 Mythos 5 費率按用量計費，因此支出上限應與 repositories 的規模與數量相稱。

#### 執行方式

1. 安全主管連接 repositories，並依 repo、服務或團隊將它們組織成專案，讓發現的歸屬從一開始就清楚。
2. 對最關鍵的 repositories 執行第一次完整掃描，包括那些先前被其他工具或較早期模型掃描過的。把第一次掃描當成基準線。第一次掃描很可能會在被認為乾淨的程式碼中發現問題。
3. 為每個專案設定排程。對積極開發中的服務，每週是合理的預設值；若 repository 很大或內容混雜，就把掃描範圍限縮到某個目錄或分支。
4. 帶著信心評分分診發現。駁回時附上理由，讓駁回被記錄下來，同一項發現才不會在下次執行時又被當成新的回報。
5. 對於範圍明確的發現，在網頁版 Claude Code 中打開建議的修補程式、審查它，並像其他任何變更一樣送過 PR 審查關卡。提出修正的代理沒有任何途徑可以核准它。
6. 對於超過單一修補程式範圍的問題，例如架構性弱點或跨服務重複出現的模式，用階段 1 的格式寫成 `intent.md`，從規劃階段開始跑。
7. 當修正發布到正式環境後，為該漏洞類別在持續評測戰術的套件中新增一個評測，讓駕馭代理的那組設定從此之後都會針對該類別受測。
8. 以 CSV 或 Markdown 匯出發現，或使用 webhooks，讓組織既有的追蹤與稽核系統維持為紀錄系統（system of record）——稽核員本來就期待在那裡看到它們。

#### 治理考量

掃描在組織的管理控管之下運行，也就是說連接了哪些 repositories、誰持有掃描席次，以及支出上限，全都是集中設定的。每一項發現都有驗證結果與信心評分，每一次駁回都有理由，因此掃描歷史就是一份「發現了什麼、修了什麼、有意識地接受了什麼」的稽核紀錄。

修正是透過 PR 審查關卡與分支保護抵達正式環境，而不是直接從掃描本身。Claude Security 是對既有靜態分析與相依套件掃描的補強。決定性的檢查留在 CI 中，模型驅動的掃描則涵蓋那些檢查天生找不到的、依賴上下文的漏洞。

#### 如何衡量

**領先指標**

已排程的已連接 repositories 佔比，以及從發現被回報到其修補程式進入 PR 審查關卡的時間（從掃描歷史與 PR 中繼資料讀出）。

**落後指標**

排程掃描找到的漏洞數，對比在正式環境中或由外部回報所發現的漏洞數（來自事故追蹤系統）；以及已跑過數輪的 repositories 上每次掃描發現數的趨勢——隨著修正與評測累積，這個數字應該會下降。

### Claude 值班：Claude Tag

事故也可能透過其他途徑抵達，例如 Slack 或 Teams 這類職場通訊應用。事故可能長得像晚上十點在事故頻道中要求緊急修復的一則 Slack 訊息，而現在這種訊息可以立即被處理。Claude Tag（公開 beta，目前於 Slack 提供）讓 Claude 以自己的身分成為那些頻道的成員，因此每一起新事故都有一位第一線應變者，而應變過程本身也成為迴圈與未來事故記憶的一部分。

對話與制度知識留在頻道中，頻道中的任何人都能引導與執行應變。任何團隊成員都能即時測試假設、探索新選項並進行調查，而頻道歷史則增添了可稽核性。透過 MCP 存取，Claude 驗證指標已回到基準線並在討論串中確認，接著把事後檢討寫入一份受版本控管的經驗教訓檔案，供未來的調查閱讀。

事故並不是 Claude Tag 唯一接手的工作。透過 MCP 在票證上被標記，或在頻道中被詢問時，Claude 都以相同方式分診工作。小而範圍明確的修正以 PR 形式走過審查關卡，任何更大的東西則寫成 `intent.md` 進入階段 1：規劃——到這個時候，迴圈就開始自我餵養了。參見：[Claude Tag 如何在 Anthropic 為 CI/CD 值班](https://claude.com/blog/ai-ci-cd-on-call)。

![頻道就是稽核軌跡](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8760aded54a2a8319cd5b9_fe6d780d.png)

*圖說：頻道就是稽核軌跡：請求、診斷、人工授權與修正，全都留在事故被處理的地方。*

---

## 結語

模型與框架（harnesses）變得更加先進，讓組織不只能轉型自己生產程式碼的方式，更能轉型整個軟體開發生命週期。

這場轉型讓人類判斷力持續居於流程核心，同時也顧及大型企業組織的治理與法規要求。

本指南匯整了我們應用 AI 團隊每天為客戶執行的許多真實最佳實務，希望你覺得它是一份實用且可付諸行動的資源。

> **迴圈持續運轉。人類判斷力，始終在它之上。**

---

### 資源與致謝

以下文件是平台團隊建立這些控管所需要的，大致依照你會導入它們的順序排列。

- [為你的組織設定 Claude Code —— 管理員決策地圖；從這裡開始](https://code.claude.com/docs/en/admin-setup)
- [設定參考與優先順序，包含每一個僅限託管的鍵值](https://code.claude.com/docs/en/settings)
- [來自 Claude 管理主控台的伺服器託管設定](https://code.claude.com/docs/en/server-managed-settings)
- [權限（Permissions）](https://code.claude.com/docs/en/permissions)
- [沙箱化 —— 作業系統層級的檔案系統與網路隔離](https://code.claude.com/docs/en/sandboxing)
- [Hooks —— 指南](https://code.claude.com/docs/en/hooks-guide)
- [Hooks —— 參考文件](https://code.claude.com/docs/en/hooks)
- [技能（Skills）](https://code.claude.com/docs/en/skills)
- [外掛與私有市集 —— 技能與 hooks 如何在全組織散布](https://code.claude.com/docs/en/plugin-marketplaces)
- [託管 MCP —— 集中控管代理的工具表面](https://code.claude.com/docs/en/managed-mcp)
- [企業部署總覽 —— Bedrock、Vertex、Foundry](https://code.claude.com/docs/en/third-party-integrations)
- [企業網路設定](https://code.claude.com/docs/en/network-config)
- [監控（OpenTelemetry）](https://code.claude.com/docs/en/monitoring-usage)
- [分析儀表板](https://code.claude.com/docs/en/analytics)
- [Compliance API —— 企業活動摘要、對話擷取與刪除](https://platform.claude.com/docs/en/manage-claude/compliance-api)
- [安全模型](https://code.claude.com/docs/en/security)
