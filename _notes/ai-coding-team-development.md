---
title: 'AI Coding 時代團隊開發的三層次演進模型'
date: 2026-10-15
image: /images/影片筆記/ai-coding-team-development.jpg
category: 影片筆記
tags: [人機混合團隊, Spec鷹架, 認知負荷, 第一性原理, 執行與決策分離]
description: '這場 Keynote 的核心貢獻，是提出 AI Coding 時代團隊開發的三層次演進模型：一個人用 AI（spec 當鷹架而非藍圖）→ 一個人指揮 Agent'
quote: '💡AI 替你實作了，你反而要更瞭解整個專案——AI 強在執行，人強在全盤決策與對齊。'
action: '🎯S-S-S 法則：spec 當鷹架拆小用完即收，實作全派給 Agent、人只鎖死驗證／介面／use case，少看程式碼多監督驗證。'
source_has_timestamps: true
source_raw: AI Coding 新時代的團隊開發
---
## [核心摘要]

這場 Keynote 的核心貢獻，是提出 AI Coding 時代團隊開發的**三層次演進模型**：一個人用 AI（spec 當鷹架而非藍圖）→ 一個人指揮 Agent Team（人只觀察、Agent 專注做事）→ 一群人＋一群 Agent（執行團隊交給 AI，人組成決策團隊）。解決的痛點：傳統「人管人」的分工模式在 AI Agent 加入後徹底失效——**認知負荷**沒有因為自動化而減少，反而爆增；唯有徹底切分「執行」與「決策」，才能真正釋放 AI Native 團隊的產能。

## [詳細重點整理]

### 1. 開場與講者介紹 [00:00]

團隊開發的定義已經改變：過去是一群人的分工合作，現在必須把「一群 AI Agent」納入合作模式計算。講者陳宜昌（YC），Noopher AI 創辦人，前聯發科 AI 研究院資深技術經理，帶領開發台灣第一個繁體中文語言模型 Breeze 系列，並以 TASTE 技術獲選 ICLR 2026。8 年機器學習研發經驗，發表論文 8 篇以上（ICLR、ACL、Interspeech）。  
**關鍵概念：人機混合團隊（Human + Agent Team）**

### 2. 一個人＋AI：從聊天框到 Coding Agent 

2025 年 4 月的 AI 寫程式仍靠聊天框，實測發現瓶頸不在模型，而在「把 prompt 組織好」本身就很難。2025 年 11 月底 Claude Code Opus 4.5 問世，Coding Agent 進入你的電腦、看到同樣的程式碼，開發習慣從此改變。講者以 Open Vibe Developers 線上共學社群（8 場、每場 300-400 人）累積實戰心得，在 COSCUP 總結出三大原理：**規格先行**、**測試驅動開發（TDD）**、**照顧好 LLM 的 context**。  
**關鍵概念：Context 管理三原理**

### 3. 實戰案例：5000 行 spec 為何跑不動 

TASTE2（語音聊天機器人，token 級語音文字對齊的第二代系統）工程複雜度極高：模型從 batch mode 改 streaming、中文化、對話後訓練、async 後端、多使用者支援、動態調配 GPU。三個人的團隊能在 8 個月完成，靠的就是大量 AI Coding。

團隊遵循 spec-driven 開發，花一個月寫了 5000 行以上的 spec（還不含 reference 與測試程式碼範例），所有 edge case 都想到，結果生成的程式碼連基礎 module 都跑不起來。失敗根因：違反了「照顧好 context」原則——spec 充滿細節，context 沒有聚焦在要解決的問題上。

解法是回到軟體工程基本動作：**拆問題**。把系統拆成三個 submodule 加一個 orchestrator，每個 module 的 spec 變小，AI 理解變好，程式碼品質立刻提升——早上短短一小時就跑通可用的 submodule；orchestrator 因為各 module 已有實際程式碼作 interface 依據，串接也很快，一兩天整體跑通。  
**關鍵概念：Spec 是鷹架，不是藍圖**——藍圖是把所有細節想清楚照圖施工；鷹架是蓋程式碼時的輔助結構，蓋完就拆。好的程式碼本身就是更強且可驗證的 guiding。

### 4. 他山之石：海外開發者的兩大分歧 

**分歧一：先寫規格還是先做原型？**

- Matt Pocock（規格派）：用「Grill Me」skill 讓 AI 反覆拷問你，直到人機對齊才寫 spec 再開發
- Boris Cherny（Claude Code 創造者，原型派）：不寫 spec，直接用 prompt 做原型、測試、迭代；原型本身就是 spec，之後要嘛修對細節，要嘛看著原型重做一份
- 講者的取捨：任務難描述就走原型，好描述就走 spec。Spec 的優勢是寫完可以放著去喝咖啡；原型的優勢是不用經歷困難的 spec 討論——因為 AI Agent 的語言跟人類有落差，對齊成本很高

**分歧二：AI 寫的程式碼要看多少？**

- Simon Willison（Django 共同創造者）：一口氣讓 AI 產完，再用 AI 以「導覽」方式理解程式碼
- AutoGPT 開發者：幾乎不看 code，只管怎麼派 Agent 出去、怎麼驗收
- DHH：看系統狀態決定——新系統做原型可以全不看；像 Basecamp 的 legacy codebase 就要看更多
- Andrej Karpathy（vibe coding 名詞創造者）：改口稱 vibe coding 只適合拋棄式專案，專業工作仍需監督與驗證

共識：**少看程式碼，多監督與驗證**。  
**關鍵概念：Spec 派 vs 原型派**

### 5. 指揮 Agent Team：人定架構，逐張單對齊 

Noopher AI 的標準流程：人與人先訂架構（不講細節）→ AI 拆單，**每一單絕不 overlap**（前後端分離、module 分開）→ 每張單用 grill-with-docs skill 讓 Agent 問到對齊，spec 寫好放上 GitHub issue → pull 下來用 TDD 實作 → 做完即關 issue（鷹架用完就拆）。

grill-with-docs 的核心是兩份檔案：

- [**CONTEXT.md**](http://CONTEXT.md)：系統的統一詞彙表（如 meta-agent 與 member agent 的定義）
- **ADR（架構決策記錄）**：技術決策（如 meta-agent 只指揮不做實作，member agent 參與實際工作）

這兩份文件成為系統的「燈塔」，Agent 有疑惑時自己去查，不需要回頭問人，背後設計邏輯是 **DDD（領域驅動設計）**：程式結構與命名跟著業務領域走，讓人機對齊在 Agent 時代特別容易。

Review 階段用 skill 進行：單元測試、整合測試、spec review，以及**變異測試**（把程式碼關鍵處改方向，如小於改成大於，單元測試應亮紅燈，沒亮就代表測試有問題）。  
**關鍵概念：DDD 領域驅動對齊**

### 6. v1 subagent、v2 看板流，各自卡在哪裡

**v1（Claude Code 原生 subagent）**：設計 planner / worker / reviewer 三種角色，用 worktree 切割執行環境，meta-agent 由主視窗擔任，平行度高、寫 code 極快。問題：所有資訊都塞進唯一的主視窗，去上個廁所回來，Agent 的 A/B 選擇提問已被洗板，全部 subagent 停在原地等人——**人類的認知負荷沒有減少**。

**v2（看板流）**：Backlog / To do / Doing / Review / Done，Agent 在 ticket 上寫思路與決策，領單、做事、移動看板。問題：叫 Agent 學看板規則去移看板，是額外的 **Agent 認知負荷**——它被迫多做一件事。講者燒了一個月、10 億等級的 token 寫 skill 和 instruction 想修好系統，仍然沒完沒了。

管理啟示：老闆不要微觀管理——叫員工做一堆報告與進度回報，就分散了做正事的能量。  
**關鍵概念：認知負荷（人類的與 Agent 的）**

### 7. 回到第一性原理：開源 oat-agents 

第一性原理推論：其實不需要看板，只需要「監控員工的電腦」——看他在做什麼就進去看。所以只需要 v1 的結構，加上一個資訊流管理機制：每個 Agent 專心做事不被打擾，講者另外養一個**助理 Agent**去看所有員工 Agent 的狀態並匯報，解決人的認知負荷。

找不到現成開源方案，於是自刻 **oat-agents**（MIT 開源）：

- 結構極簡：一個 meta-agent + 一群 member agent，制度與角色全部用 plugin 自定義
- Agent 零額外負荷：用原生 Claude Code 與 Codex，不引入新 harness
- Worktree 檔案管理 + pod 環境隔離，每個 session 專心做自己的任務
- TUI 一個畫面看清所有 Agent 的狀態、脈絡、token 消耗與花費
- 用 tmux 進入任意 session 互動下命令

**關鍵概念：第一性原理（First Principles）**

### 8. People Team + Agent Team：實作交給 Agent，人做決策

分工的依據是能力邊界：

- **AI Agent 擅長**：執行力高、效率高、可平行化、極細心（改資料型別時所有該改的地方都會改，不犯人類的低級錯誤）、適合流程化機械式任務
- **AI Agent 做不好**：與人對齊（AI 語言與人有落差）、容易陷入細節看不到大局、技術選型時難跳脫框架找最優解——實測逼問後 AI 只會「花式吹捧」認同人類給的第三條路

組織設計：**執行團隊**完全由 AI 主控（實作、測試、除錯、review），人不寫程式碼；**決策團隊**由人組成（技術選型、架構方向與取捨）。人跟人之間分工 scope 拆開避免打架。打造原型時幾乎不看程式碼，只鎖死三個關卡：**驗證**、**介面**（前後端 interface、module data 介面）、**use case**（系統怎樣算跑通）。  
**關鍵概念：執行團隊與決策團隊徹底分離**

### 9. 理解工程與探索工程 

**理解工程**：AI 寫得快，但人與程式脫節就做不了好決策。新世代菜鳥不再有「只改一個小地方」的福利——AI 已幫你實作，你的任務是領導 AI，所以入職第一天就要懂整個系統；好在也可以反過來用 AI 去理解公司幾萬行的程式碼。

**探索工程**：帶著理解去看原型，做 A/B/C/D 版改進並用測試方法找出較優解；或拿著原型上網找相關資訊，打造新原型再試。走過的錯誤決策全部回歸原型，讓原型疊代出更好的版本。  
**關鍵概念：理解工程與探索工程**

### 10. AI Native 公司三件事與收尾

三件事：

1. 徹底切分執行與決策：執行全給 AI。好的 Agent 執行團隊要像生產線——持續運行、能被優化、能從中學習、與人對齊、隨時看得懂
2. 人的課題是定義目標、對標市場／客戶／成果——AI 只會「做」，不代表會產生「成果」
3. 人與人的合作 scope 盡量拆開，且每個人都要理解整個系統；弔詭的是，AI 替你實作了，你反而要更瞭解整個專案

收尾觀點：AI 時代最重要的是**判斷力**——決定做什麼的眼光與品味（看到別人看不到的機會），以及從 AI 的雜訊中找出真正訊號的判斷力。AI 可以拓寬認知：講者沒請會計師，靠 AI 自學記帳並用 AI Coding 寫出一套自動作帳系統，靠 AI 加速學習與經驗獲取。  
**關鍵概念：訊號 vs 雜訊的判斷力**

## [結論與行動建議]

**啟發金句**：「AI 替你實作了，你反而要更瞭解整個專案——AI 強在執行，人強在全盤決策與對齊。」

**具體行動建議（S-S-S 法則）**：

- **Spec 當鷹架（Scaffold）**：spec 拆小、模組切開、用完即收（GitHub issue 關掉），不寫 5000 行藍圖
- **Send-Verify 分離**：實作全部派給 Agent，人只鎖死驗證、介面、use case 三道關卡
- **Signal 篩選**：少看程式碼、多監督驗證，從 AI 的雜訊中判斷真正的訊號

**生活實踐建議**：

- 團隊導入：下次專案先由人開 30 分鐘架構會（不談細節），讓 AI 拆單並用 grill 式 skill 逐單對齊，spec 放 GitHub issue 隨做隨關
- 個人生產力：建立自己的 [CONTEXT.md](http://CONTEXT.md) 詞彙表 + ADR 決策記錄，讓 Agent 有疑問自己查文件而不是來問你，直接省掉重複對齊的時間
- 自我進化：像講者自學會計並用 AI Coding 打造自動作帳系統一樣，挑一個你不熟悉的領域，用 AI 加速學習並把流程工具化——把「不懂」變成「系統」

## [參考連結]

- 原始影片：[https://www.youtube.com/watch?v=-B9WLMJAiZM[youtube]](https://www.youtube.com/watch?v=-B9WLMJAiZM[youtube])