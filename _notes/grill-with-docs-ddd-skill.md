---
title: '停用 /grill-me：用通用語言與 ADR 解決 AI 記憶斷層'
date: 2026-05-15
image: /images/AI筆記/grill-with-docs-ddd-skill.jpeg
category: AI筆記
tags: [通用語言, 領域驅動設計, ADR, context.md, AI編程]
description: '/grill-me skill 的根本缺陷在於每次新 session 都得重新解釋專案術語，共識無法被持久化。引入 DDD 的通用語言概念，開發出進化版 /grill-with-docs 解決記憶斷層痛點。'
quote: 'The same techniques that work with humans also work with AI——讓人類協作更順暢的溝通框架，同樣讓人機協作更精準。'
action: '為專案建立 context.md 定義術語，重要決策寫 ADR，改用 /grill-with-docs 開啟每次 AI 編程 session'
source_has_timestamps: true
---
# 📝 停用 /grill-me？更強的 AI 編程技法來了
**影片：** *I stopped using /grill-me for coding. Here's what I use instead* | Matt Pocock | 2026-05-14  [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

***
## [核心摘要]
`/grill-me` skill 雖廣受好評，但其根本缺陷在於——每次新 session 都得重新解釋專案術語，**共識無法被持久化**。作者引入 **領域驅動設計（DDD）** 中的「通用語言（Ubiquitous Language）」概念，開發出進化版 `/grill-with-docs`，將訪談過程與術語文件化機制合而為一，解決了 AI 對話「記憶斷層」的痛點。 [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

***
## [詳細重點整理]
### 1. /grill-me 的成功與限制 [00:00–02:47]
`/grill-me` skill 的核心機制是讓 LLM 像偵探一樣逐層追問，直到達成「共同理解」（shared understanding）。它廣受工程師好評，甚至有人用它訪談自己、為母親撰寫悼詞。然而它有一個致命缺陷：每次新 session，AI 對「non-obvious terms」（如 `standalone video`）毫無記憶，開發者必須反覆解釋相同術語，效率大打折扣。 [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

**關鍵概念：** **共識脆弱性（Shared Understanding Fragility）**——每次 session 重新建立共識的成本累積，是 `/grill-me` 的核心痛點。

***
### 2. 通用語言（Ubiquitous Language）的引入 [02:47–04:32]
解法來自 Eric Evans 的《Domain-Driven Design》（藍皮書）。**Ubiquitous Language** 的核心思想是：程式碼、開發者、領域專家，三者應使用同一套語言，讓術語在文件、對話、程式碼中保持一致。作者在實踐中發現，先用 `/ubiquitous-language` skill 整理術語，再搭配 `/grill-me`，兩個 skill 同時使用效果更好——這就催生了合體版本。 [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

**關鍵概念：** **Ubiquitous Language（通用語言）**——DDD 核心概念，消弭「說的」與「寫的」之間的語意落差。

***
### 3. /grill-with-docs：進化版 Skill [04:32–07:27]
`/grill-with-docs` 在 `/grill-me` 原有訪談邏輯之上，新增三個機制： [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

- **讀取 `context.md`：** 自動載入專案的現有術語表（Bounded Context），讓 AI 在訪談前就「懂你的語言」
- **即時挑戰模糊語言：** 訪談中主動對照術語表，要求開發者精確定義新概念
- **即時更新 `context.md`：** 每次訪談後，新術語自動寫回文件，形成累積效應

**關鍵概念：** **Bounded Context（限界上下文）**——一個子系統內使用一致語言的邊界，`context.md` 就是它的文字具現。

***
### 4. ADR：補足 context.md 無法描述的決策 [07:27–08:25]
對於「無法直接用術語描述、但決策影響深遠」的設計選擇，作者引入 **Architectural Decision Record（ADR）**。ADR 是存放在 repo 中的 Markdown 文件，只記錄「難以逆轉、若無背景脈絡會令人驚訝、且涉及真實取捨」的決策。例如：為何採用 `ON DELETE RESTRICT` 而非 cascade 刪除。 [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

**關鍵概念：** **ADR（架構決策記錄）**——輕量級決策日誌，讓 AI 理解「為什麼這樣做」，而非只知道「做了什麼」。

***
### 5. Live Demo 重點觀察 [08:25–12:24]
作者在真實專案中演示，AI 在 session 開始時即主動讀取 `context.md`，自動識別 `standalone video` 的已有定義，並立刻提出術語碰撞問題（`pitched standalone video` vs `unattached standalone video`）。這種**語言先行、實作後行**的模式，讓設計決策（如 1:N 關係、status 轉換、刪除策略）在撰碼前就被充分釐清。 [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

**關鍵概念：** **語言先行（Language-First）**——先定義共同語言，再討論實作細節，從源頭降低 AI 生成程式碼的語意偏差。

***
### 6. 三大具體效益 [12:24–13:26]
使用 `/grill-with-docs` 後可觀察到三個明顯效益： [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

- **回覆更簡潔：** AI 可用術語代替冗長描述，token 消耗下降
- **思考鏈更精準：** AI 內部推理也使用共同語言，減少偏移
- **程式碼更易導航：** 變數名稱、檔案名稱與術語表一致，搜尋與維護成本降低

***
## [技術/數據對比]
| 維度 | `/grill-me` | `/grill-with-docs` |
|---|---|---|
| 適用情境 | 無程式碼基底（如寫作、規劃）| 有既有程式碼基底的專案 |
| 術語持久化 | ❌ 每次 session 重新建立 | ✅ 寫入 `context.md` 累積沿用 |
| 文件整合 | ❌ 無 | ✅ 讀取 & 更新 `context.md`、支援 ADR |
| DDD 對應 | 無 | Ubiquitous Language + Bounded Context |
| 語言精確度挑戰 | 被動 | 主動挑戰模糊語言 |

 [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

***
## [結論與行動建議]
**啟發金句：**
> **「The same techniques that work with humans also work with AI.」** ——讓人類協作更順暢的溝通框架，同樣讓人機協作更精準。 [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

**具體行動建議（L-A-D 法則）：**
- **L（Language）：** 為專案建立 `context.md`，列出所有 non-obvious 術語
- **A（ADR）：** 每個難以逆轉的重要決策，寫一份 ADR 存入 repo
- **D（Docs-First）：** 使用 `/grill-with-docs` 取代 `/grill-me` 開啟每次 AI 編程 session

**生活實踐建議：**
對於 AI-Powered Application Architect，建議立即在現有專案中建立 `context.md`，把常見的業務術語（如「工單」、「任務」、「流程節點」等）加以定義，並在 Claude / Cursor 的 `.claud/` 設定中加入 context pointer。初次設定投入約 30 分鐘，但往後每次 AI session 的對齊成本將顯著下降，等同於為 AI 建立了一個「不會遺忘」的領域知識庫。 [youtube](https://www.youtube.com/watch?v=DrC6PZgijsc)

***
## [參考連結]
- 📺 原始影片：https://youtu.be/6BB6exR8Zd8
- 🛠️ Matt Pocock 的 Skills 頁面：https://aihero.dev/s/qsbMhn
- 📧 AI Hero Newsletter：https://aihero.dev/s/CtdFKk
