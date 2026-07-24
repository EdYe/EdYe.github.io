---
title: 'Agentic 系統為何需要本體論'
date: 2026-07-24
image: /images/AI筆記/agentic-systems-need-ontology.jpg
category: AI筆記
tags: [神經符號AI, 本體論, OWL, Pydantic, 護欄設計]
description: 'Frank Coyle 指出，Agent 系統的多數失敗——重複退款、付款寄錯對象、訂單狀態異常——都源自模型外部缺乏一層形式化本體論作為邏輯護欄，解法是神經符號 AI。'
quote: 'LLM 的幻覺不是 bug，是 feature——關鍵不在消滅它，而在用邏輯護欄引導它。'
action: '在設計 Agent 工具呼叫迴圈時，於工具回傳結果與實際執行之間插入本體論驗證層，以 P-O-G 法則（Pydantic at the door、Ontology at the ledger、Guardrails before action）確保 Agent 通過驗證前不產生任何副作用'
source_has_timestamps: true
---
# Agentic 系統為何需要本體論

## [核心摘要]

Frank Coyle（UC Berkeley）指出，Agent 系統的多數失敗——重複退款、付款寄錯對象、訂單狀態出現「大概已出貨」——都源自同一個缺失：模型外部缺乏一層形式化本體論作為邏輯護欄。LLM 以機率方式推理，本質上會幻覺，再多的 prompt engineering 也無法填補這道鴻溝。解法是**神經符號 AI**（Neurosymbolic AI）：模型內部保持機率推理，外部用 RDFS、OWL 等標準定義實體型別、關係與約束，並以 Pydantic 驗證型別、本體論驗證結果，在 LLM 真正執行工具前攔截不合邏輯的行為。

***

## [詳細重點整理]

### 1. 教育理念與背景 [00:00]

Frank Coyle 自述在 Berkeley 教學逾 35 年，早期職業生涯在神經科學領域，如今因 Agent AI 帶動認知科學復興而重新投入。他引用藝術家 Sister Corita Kent 的哲學：「沒有失敗，沒有成功，只有創造」，並強調手寫筆記的重要性——打字時大腦專注於鍵盤字母，手寫則能調動全部感官系統，加速學習。

**關鍵概念：做中學** 

### 2. 兩條血脈：Agent 與本體論 [02:21]

Agent 概念可追溯至 AI 早期——McCarthy、Minsky（Society of Mind）、1956 年達特茅斯會議正式提出「人工智慧」一詞。Agent 的定義是：感知 → 決策 → 行動。本體論則更古老，源自亞里斯多德的「存在哲學」與存在類別，經 Von Quine 形式化，1993 年 Gruber 將其定義為「共享概念化的形式規範」。

**關鍵概念：共享概念化** 

### 3. 神經符號 AI：為機率模型裝上護欄 [04:04]

當前正發生機率系統與形式化表示的匯流。LLM 的幻覺不是 bug，而是 feature——人類同樣會想像不存在的事物並將其實現。**神經符號 AI** 將神經網路（機率推理）與符號 AI（規則系統、知識圖譜）結合，目標是讓 LLM 保持在護欄內行動。

**關鍵概念：神經符號 AI** 

### 4. 本體論的本質 [05:23]

本體論即實體及其關係的表示，實體附帶屬性。圖資料庫的興起是因為關聯式資料庫過於僵化——新增欄位需重整結構，而圖資料庫可直接附加新節點、屬性或關係。本體論可從兩個方向建構：

- **自上而下**：專家聚在一起分析領域，定義實體與關係
- **自下而上**：從客戶反饋等實際資料中萃取實體，逐步加入圖譜

**關鍵概念：自上而下 vs 自下而上建構** 

### 5. 專家系統時代與 AI 寒冬 [06:14]

自上而下建構本體論呼應 1980 年代的專家系統熱潮。日本啟動第五代電腦專案，美國投入巨資，但符號 AI 無法規模化，進入 AI 寒冬。神經網路在 1960 年代已被提出，但缺乏 GPU 運算力，直到 Nvidia 為遊戲開發的 GPU 被轉用於神經網路訓練，才促成今日的 AI 榮景。

**關鍵概念：可規模性** 

### 6. 複用既有分類體系 [07:55]

建構本體論不必從零開始，已有大量成熟標準可用：

- **schema.org**：提供一套完整的詞彙與關係定義
- **FOAF**（Friend of a Friend）：社群網路建模
- **Dublin Core**：研究論文與書籍的描述詞彙
- **DBpedia**：Wikipedia 底層的圖資料庫

**關鍵概念：領域複用** 

### 7. RDFS 與 OWL：推理與約束 [09:12]

本體論圖結構之外，可疊加 RDFS 與 OWL 等輔助技術來實現推理與約束：

- **RDFS Domain/Range**：若 `teaches` 的 domain 是 `teacher`，說「Bob teaches Scooter」即可推論 Bob 是老師；若 range 是 `student`，則推論 Scooter 是學生
- **OWL 傳遞性**（Transitive Property）：若 `ancestor` 具傳遞性，Sue 是 Mary 的祖先、Mary 是 Ann 的祖先 → Sue 是 Ann 的祖先
- **OWL 功能性屬性**（Functional Property）：`has_father` 是唯一值——若 Bob 和 BB 都被稱為 Jim 的父親，則推論 Bob = BB（同一人）

**關鍵概念：功能性屬性** 

### 8. Agent、迴圈與其脆弱性 [12:12]

Bohm 與 Jacopini（1966）證明：任何具備**循序、條件判斷、迴圈**三要素的語言都是 Turing Complete，可計算任何可計算之物。Agent 系統引入迴圈後，技術上已具備完整的計算能力。但迴圈帶來三大風險：無限迴圈、Agent 間通訊漂移、Token 消耗失控。Coyle 認為，這本質上是重新回到專家系統時代的符號 AI 精神。

**關鍵概念：Turing Complete** 

### 9. Claude 工具使用迴圈與本體論驗證器 [14:22]

Coyle 展示一段 Claude Agent 的程式碼，結構為 `while True` 迴圈：

1. LLM 收到 prompt 與工具定義，生成工具呼叫的參數（LLM 本身無法執行，只能預測下一步）
2. 檢查 `stop_reason`，若為 `tool_use` 則觸發工具執行
3. 工具回傳結果後，進入驗證器——這正是本體論介入的關鍵點
4. 驗證器以領域本體論檢查結果是否合理；不合理則回饋 LLM 或引入人工審核

核心架構：用本體論包圍輸入端，在工具執行前攔截錯誤。

**關鍵概念：本體論驗證器** 

### 10. Pydantic 守門，本體論記帳 [17:47]

具體防護策略分兩層：

- **Pydantic at the door**：用 Pydantic 為 Python 這類弱型別語言加上型別檢查，在入口攔截型別錯誤
- **Ontology at the ledger**：用本體論在帳本層級驗證業務邏輯

純粹的 Agent 應盡可能**無副作用**——不在未經驗證前修改資料庫，先通過本體論檢查再行動。

**關鍵概念：無副作用設計** 

### 11. 本體論能攔截而自然語言不能的錯誤 [18:52]

Coyle 展示 OWL 邏輯建構能攔截的具體錯誤類型，這些在純文字指令中極難表達：

| 錯誤類型 | 本體論攔截機制 | 說明 |
|---------|--------------|------|
| 同一訂單二次退款 | OWL 功能性屬性 | `refund` 操作具唯一性約束，不可重複執行 |
| 付款寄給客服而非買家 | OWL 互斥屬性 | `customer` 與 `support_rep` 為互斥實體，收款方型別不符 |
| 訂單狀態出現「大概已出貨」 | OWL 封閉列舉 | 狀態欄僅允許 `paid`、`shipped`、`refunded` 三值 |

***

## [結論與行動建議]

> **啟發金句**
>
> 「LLM 的幻覺不是 bug，是 feature——關鍵不在消滅它，而在用邏輯護欄引導它。」

> **行動法則：P-O-G 法則**
>
> - **P**ydantic at the door（型別守門）
> - **O**ntology at the ledger（邏輯記帳）
> - **G**uardrails before action（行動前驗證）

> **生活實踐建議**
>
> 在設計任何 Agent 工具呼叫迴圈時，於工具回傳結果與實際執行之間插入一個本體論驗證層。先複用 schema.org、DBpedia 等既有本體定義領域實體與約束，再以 Pydantic 處理型別層，以 OWL 功能性/互斥屬性處理業務邏輯層。確保 Agent 在通過驗證前不產生任何副作用（不寫入資料庫、不發送請求），將「難以用英文描述的業務規則」轉化為幾行程式碼的邏輯約束。

***

## [參考連結]

- 原始影片：https://youtu.be/Sir59K8ZDPU
- Frank Coyle 個人網站：https://www.frank-coyle.ai/
- Frank Coyle Twitter/X：https://x.com/coyle_frankp
- Frank Coyle LinkedIn：https://www.linkedin.com/in/frank-coyle/
