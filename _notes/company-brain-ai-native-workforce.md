---
title: '新商業物理學：打造AI原生公司大腦'
date: 2026-07-19
image: /images/AI筆記/company-brain-ai-native-workforce.jpg
category: AI筆記
tags: [Skill File, Company Brain, Context Engineering, AI原生公司, Skillify紀律]
description: 'Garry Tan 提出「新商業物理學」：透過將 AI 視為工作力而非自動完成工具，精簡團隊即可達到過去需千人規模的產出。'
quote: '💡「Model quality is rented, but if you build your brain, you own that brain.」模型品質是租來的，但你建構的大腦是你自己的。'
action: '🎯依 S-S-C-L 法則：Skillify（技能化每項完成的工作）、Space（釐清計算應在潛在或確定性空間）、Context（建構 Company Brain）、Library（將組織視為圖書館而非單一工作流）。'
source_has_timestamps: true
---
# The New Physics of Business — Garry Tan, Y Combinator

## [核心摘要]

Garry Tan 提出「新商業物理學」：透過將 AI 視為**工作力**而非自動完成工具，精簡團隊即可達到過去需千人規模的產出 。核心架構是將組織角色、流程、績效考核全部編碼為 **Skill File（技能檔案）**，搭配 **Company Brain（公司大腦）** 作為機構知識庫與圖書館員，確保 Agent 在正確時刻獲取正確上下文 。其個人產出已從 2013 年每日 14 行程式碼提升至約 **400 倍**，且關鍵不在模型權重，而在於「如何接線工作」（how you wire the work）。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

***

## [詳細重點整理]

### 1. 400 倍生產力跳躍 [00:00]

2013 年 Tan 作為 YC 合夥人兼全職工程師，每日僅能產出約 14 行可用邏輯程式碼，這在當時屬於正常水準 。2026 年他全職管理 YC、工時反而更少，卻透過管理 AI Agent 達到約 **400 倍**的產出提升；即使以最嚴苛的標準打折，底線仍有 **8 倍**、中位數約 **80 倍** 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**槓桿不在權重（Leverage is not in the weights）** — 2 倍人與 100 倍人使用完全相同的 Claude、相同權重、相同 API，差異在於如何接線工作 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

### 2. 接線工作：將 AI 視為工作力 [03:38]

Tan 強調最快的創辦人不把 AI 當作自動完成工具，而是當作**工作力** 。他提出核心對應關係： [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

| 組織概念 | AI 原生對應物 |
|---------|-------------|
| 員工 | Skill File（技能檔案，一個能力、一個職責） |
| 組織架構 | Resolver Table（解析器表，決定任務派發） |
| 內部流程 | Filing Rules（歸檔規則） |
| 績效考核 | Trigger Evals（觸發式評估測試） |

> 「當你坐下來用 Claude Code 或 Cursor，你不是在寫軟體。你在招聘、訓練、管理一支由 Markdown 構成的工作力。」 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**Skill File 即員工（Skill File is an employee）**

### 3. AI 原生組織的解剖 [04:11]

Winter 25 批次中有四分之一的公司程式碼庫達 **95% AI 生成**，該批次成為 YC 歷史上成長最快、利潤最高的批次 。具體案例： [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

- **Emergence**（Summer 24）：公開發布後 8 個月達九位數 ARR，跨越 $15M ARR 時僅 15 人 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)
- **Retail**（Winter 24）：$60M 營收，約 40 人 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

這種人均營收在軟體、石油、鐵路行業中從未出現過 。YC 內部非工程人員（媒體、活動、財務團隊）也都在建構 Skill File 與 Cron Job，一位財務人員用內部工具將上百個 Excel 工作簿合併為單一 App 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**AI 原生公司（AI-Native Company）** — 從第一天起就以精簡團隊、Skill File 驅動、創辦人仍在程式碼中的架構運作。

### 4. 潛在空間 vs 確定性空間 [08:38]

Tan 指出所有 AI 工程問題通常源自計算發生在錯誤的一側 ： [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

- **潛在空間（Latent Space）**：LLM 本身，負責品味判斷、理解人類模糊意圖、非確定性呼叫，用 Markdown 檔案引導 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)
- **確定性空間（Deterministic Space）**：工程師熟悉的領域，Agent 撰寫 TypeScript/Erlang 等程式碼 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

實例：Startup School 需將 800 人完美聚類座位，800 個座位的儲存計算必須在確定性空間，但「誰坐你旁邊最合適」的人類判斷由 LLM 處理，過去需一個月的工作現在約 10 分鐘、數百美元 Token 即可完成 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**計算位置感知（Computation Placement Awareness）**

### 5. 克服人類記憶限制：AI 即圖書館 [10:53]

人類工作記憶僅能同時持有 **7±2** 個項目（認知心理學經典論文），這也是本地電話號碼為 7 位數的原因 。AI Agent 則能持有 **100 萬 Token（約 1,000 頁）**，相當於同時在腦中打開三本《哈利波特》並在數秒內跨書搜尋與綜合 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

但三本書仍然太少——你的公司是一座圖書館 。決定 Agent 是天才還是金魚的關鍵問題是：**誰決定哪三本書被打開在桌上？** 這就是 **Context Engineering（上下文工程）** 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**上下文工程（Context Engineering）**

### 6. Context Engineering 與圖書館員 [12:53]

Company Brain = 圖書館 + 圖書館員 。有人認為這只是 RAG，Tan 回應：「檢索是基本元件，就像 Postgres 只是 B-Tree 一樣。困難的是周邊的一切」： [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

- 什麼內容被寫入知識庫
- 如何被豐富與連結
- 什麼被提升為熱記憶 vs 歸檔為冷參考
- 當兩個事實衝突時誰來仲裁

> 「檢索很容易。值得被檢索才是產品。」 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**記憶 + 衛生（Memory + Hygiene）** — 原語不是記憶，而是記憶加上衛生：每個事實的來源標記、新舊資訊衝突時的矛盾檢查、以及一位人類+Agent 圖書館員負責修剪 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

### 7. 建構 GBrain：管理機構知識 [13:28]

Tan 的個人 GBrain 已累積約 **22 萬頁**，主要由 Agent 從他的 Email、會議、20 年筆記與生活經驗中撰寫 。當創辦人寄來危機 Email 時，Agent 在他讀完信之前就已調出所有過往對話、三間遇到同樣瓶頸的投資組合公司、以及實際有效的解法 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

> 「這就是助理與同事的區別。」 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

GBrain 以 MIT 開源免費提供，Tan 認為這一層應像 Linux 一樣開放 。他建議 Open Claw 是法拉利、Codex 是可靠的 Honda，概念才是重點而非特定工具 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**公司大腦（Company Brain）**

### 8. Skillify 紀律 [15:17]

Tan 的核心紀律：**永遠不做一次性工作（Never do one-off work）** 。當你用 Agent 完成一項工作並對結果滿意後，不要停在那裡——將其 **Skillify（技能化）** 為可重用的 Skill File 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

> 「如果你得問第二次，你就失敗了。」 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

> 「捕獲所學的組織每天都在變聰明。不這樣做的組織每天早上醒來都失憶，無論模型多好。」 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**Skillify 紀律（The Skillify Discipline）** — Model quality is rented, but if you build your brain, you own that brain.

### 9. 豐盛是已出貨的軟體 [18:25]

Tan 分享一個案例：一位父親為患有罕見癲癇的兒子，建構了 8 萬個 Markdown 檔案的 Company Brain，靠自己推進到人類對該病症知識的邊界 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

> 「豐盛不是政策白皮書，它是已出貨的軟體。」 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

> 「每個太大無法閱讀的檔案庫、每個太髒無法清理的資料集、每個你被告知不要煮沸的海洋。我們現在可以煮沸海洋了。」 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

關鍵概念：**豐盛即出貨軟體（Abundance is shipped software）**

***

## [技術/數據對比]

| 維度 | 2013 年（傳統模式） | 2026 年（AI 原生模式） |
|------|------------------|---------------------|
| 每日程式碼產出 | ~14 行邏輯程式碼 | ~400 倍（保守 8 倍 / 中位 80 倍） |
| 工作記憶容量 | 7±2 項目 | 100 萬 Token（~1,000 頁 / 三本哈利波特） |
| 組織規模 | 需雇用數百人（銷售、客服、營運、財務） | 精簡團隊 + Skill File 驅動 Agent |
| 知識管理 | 人腦 + 檔案櫃 + 組織圖 | Company Brain（圖書館 + 圖書館員） |
| 座位聚類（800 人） | 約 1 個月人工 | ~10 分鐘、數百美元 Token |
| 營收/人均基準 | 軟體/石油/鐵路歷史最高 | 從未存在過的新基準 |

| 公司 | 批次 | 營收 | 人數 |
|------|------|------|------|
| Emergence | Summer 24 | 九位數 ARR（8 個月內） | 15 人（$15M ARR 時） |
| Retail | Winter 24 | $60M | ~40 人 |
| Winter 25 批次 | — | YC 歷史最快成長/最高利潤 | 25% 公司 95% AI 生成程式碼 |

***

## [結論與行動建議]

### 啟發金句

> **「Model quality is rented, but if you build your brain, you own that brain.」**
> 模型品質是租來的，但你建構的大腦是你自己的。

### 具體行動建議：S-S-C-L 法則

- **S**killify — 每完成一項工作立即技能化為可重用 Skill File
- **S**pace — 釐清計算應在潛在空間還是確定性空間
- **C**ontext — 建構 Company Brain，讓圖書館員決定哪三本書被打開
- **L**ibrary — 將組織視為圖書館而非單一工作流，知識持續複利

### 生活實踐建議

1. **日常 Skillify 流程**：每次用 AI 完成工作後，花 2 分鐘將 Prompt 與流程封裝為 Markdown Skill File，建立個人技能庫，避免重複請求 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)
2. **非工程人員也能 Agent 化**：如 YC 財務人員的案例，將重複性 Excel 工作封裝為 Skill File + Cron Job，讓非技術人員成為「Agent 管理者」。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)
3. **個人第二大腦**：用 GBrain 或類似工具整合 Email、會議筆記、決策紀錄，讓 Agent 在你讀信前就備好相關上下文 。 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)

***

## [參考連結]

原始 YouTube 影片：https://youtu.be/eBUyTS7SzV4 [youtube](https://www.youtube.com/watch?v=CjVQJdIrDJ0)
