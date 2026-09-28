---
title: '企業AI化兩大基礎：詮釋資料與本體論'
date: 2026-09-28
image: /images/影片筆記/ontology-vs-metadata.jpg
category: 影片筆記
tags: [詮釋資料, 本體論, 事實圖資料庫, 圖建模, 概念清晰度]
description: '本片釐清企業 AI 化的兩大資料基礎：Metadata（詮釋資料） 描述資料的屬性，Ontology（本體論） 定義概念之間的關係與語意。LLM 本質上是「相似...'
quote: '💡AI 找的是最相似的，不是最正確的——你要親手為它蓋一座事實的地基。'
action: '🎯依「M-O-G 法則」落地：先做 Metadata 標準化，再定義本體論的概念與關係，最後依真實業務流程重做圖建模並以 AI 可消化的方式餵入。'
source_has_timestamps: true
---
## [核心摘要]

本片釐清企業 AI 化的兩大資料基礎：**Metadata（詮釋資料）** 描述資料的屬性，**Ontology（本體論）** 定義概念之間的關係與語意。LLM 本質上是「相似度驅動」而非「事實驅動」，幻覺難以根除；解法是在向量資料庫之上，附加一層以本體論建模的**事實圖資料庫（Graph DB）**，讓 AI 從「找最像的」進化到「回答正確的」。落地順序：先把 Metadata 做好，本體論才有穩固地基 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

## [詳細重點整理]

### 1. 議題設定：LLM 懂不懂你的公司術語？ [00:00]

生成式 AI 擅長產出文字，卻未必理解企業內部的專有名詞與定義，這正是本體論近期受到關注的原因。來賓為 En-core 執行長 Sunyoung Kim，主持人為 Tony Ko 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

**關鍵概念：企業知識語意落差**

### 2. Metadata 是什麼：資料的資料 [00:24]

Metadata 是描述資料的資訊，例如姓名、電話、email 等欄位定義，以及建立時間等屬性；實際的值（如某人的名字）才是資料本身 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

在結構化資料上掛好 Metadata 的效益：

- 多 Agent／多系統協作時，有標準就能減少術語混淆、簡化整合
- 將結構資訊餵給 AI，能更快、更穩地建立可靠可信的資料

**關鍵概念：Metadata 標準化**

### 3. 先 Metadata、後 Ontology 的正確順序 [00:65]

過去的努力多集中在結構化資料；現在需求已擴及半結構化與非結構化資料，需要整合式地收集並管理 Metadata。Metadata 打好基礎，本體論才容易建構；沒有地基硬蓋，只會把事情複雜化 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

**關鍵概念：資料治理先後序**

### 4. Ontology 的起源與現代定義 [00:89]

本體論可追溯到古希臘亞里斯多德——「事物有哪些共同特徵、該如何分類」（如動物 vs. 植物）。現代最廣泛使用的定義來自 1990 年代初的 Tom Gruber：**「共享概念化的明確規格」**（an explicit specification of a shared conceptualization）。長期停留在理論層，隨運算能力提升與大數據／機器學習時代普及，近年因知識圖譜與更成熟的解決方案，再度成為焦點 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

**關鍵概念：共享概念化（Shared Conceptualization）**

### 5. Metadata vs. Ontology 的本質差異 [01:19]

Metadata 管屬性與值，Ontology 管關係與語意。本體論像一張「人與電腦都能理解的概念與關係地圖」：Metadata 描述「顧客」這個項目，本體論則明確表達「VIP 顧客」與其他概念之間的關聯，讓 AI 能夠辨識 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

**關鍵概念：語意關係圖（Semantic Map）**

### 6. 為何 RAG 仍不夠：相似度 ≠ 正確性 [01:42]

多數 AI 應用以 LLM 為核心，設計上就是相似度驅動——「找最像的」而非「找正確的」。這是向量資料庫與 RAG 興起的原因，但幻覺仍不斷發生。進一步的改良：掛上一層融合本體論概念的**事實圖資料庫**，效能與正確度都會提升。AI 的演進也從「加速找答案、減少幻覺」走向「理解脈絡的推理」，以真正交付使用者要的東西 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

**關鍵概念：事實層（Fact-based Layer）**

### 7. 為何談 Ontology 必提 Graph DB [03:00]

本體論有多種實作方式，但傳統 RDBMS 有極限：要抵達目標資料需大量 JOIN，路徑一長就容易偏離、直覺性差、彈性受限。但把 RDBMS schema 原封不動搬進圖資料庫沒有用——只是換了系統的同一套東西。正確做法是理解真實業務流程與既有 RDBMS 結構，重新設計圖建模，因此需要具備領域經驗、資料理解，以及資料流、治理與業務優化視角的專家 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

**關鍵概念：圖建模重設計（Graph Remodeling）**

### 8. 喂圖給 AI 的關鍵 Know-how [03:44]

向量 DB 之所以在 RAG 中受歡迎，是因為 AI 容易消化。圖資料庫最終也是為 AI 服務，若叫 AI 直接讀原始圖結構，它反而會混淆——「怎麼提供」本身就是關鍵 know-how 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

**關鍵概念：AI 可消化的知識表示（Machine-consumable Knowledge）**

### 9. 未來人才需求：哲學式思考勝過工程 [04:09]

要在本體論路上走得遠，除了工程，人文式的思考可能更重要。技術某種程度上 AI 自己就能處理，但概念清晰度——「什麼哲學指引方向」——以及描繪大局、理解意義的能力，需要人文思維。這條路起點更接近哲學而非商業或經濟學，隨時間才變得實證化 。[[youtube](https://www.youtube.com/watch?v=ve7AA01vplE)]

**關鍵概念：概念清晰度（Conceptual Clarity）**

## [技術/數據對比]


| 面向   | Metadata         | Ontology          |
| ---- | ---------------- | ----------------- |
| 定義   | 描述資料的資料（欄位、屬性）   | 共享概念化的明確規格        |
| 處理對象 | 屬性與值             | 概念間的關係與語意         |
| 典型例子 | 姓名、電話、email、建立時間 | 「VIP 顧客」與其他概念的關聯  |
| 主要效益 | 跨系統術語一致、整合容易     | 讓 AI 辨識關係、支撐事實推理  |
| 建構順序 | 先做，是地基           | 後做，需要 Metadata 基礎 |



| 資料儲存方案         | 問題/優勢                    | 適用情境     |
| -------------- | ------------------------ | -------- |
| RDBMS          | 大量 JOIN、路徑長易偏離、彈性受限      | 傳統交易型系統  |
| 向量 DB + RAG    | AI 易消化，但相似度驅動、幻覺仍在       | 快速檢索     |
| Graph DB + 本體論 | 事實為本、正確度提升，但需重新圖建模、需領域專家 | 事實層 + 推理 |


## [結論與行動建議]

**啟發金句：** 「AI 找的是最相似的，不是最正確的——你要親手為它蓋一座事實的地基。」

**具體行動建議：M-O-G 法則（Metadata → Ontology → Graph）**

- **M**etadata first：先完成資料的標準化描述（含半結構化與非結構化資料）
- **O**ntology second：在穩固地基上定義概念與關係，勿過早複雜化
- **G**raph last：依真實業務流程重新做圖建模，並以「AI 可消化」的方式喂入

**生活實踐建議：**

- 在 AI 專案中（例如你的 MCP 應用開發），先用統一的欄位定義與命名規範整理資料來源，再設計概念之間的關聯，而不是直接把 RDBMS schema 原樣塞進向量庫或圖庫
- 建知識庫或 RAG 系統時，為公司／個人文件補上結構化描述（來源、日期、主題），並在檢索層之上加一層明確的「事實關係表」，降低幻覺
- 個人知識管理同理：先把筆記的屬性（標籤、日期、出處）整理乾淨，再建立筆記之間的連結關係，最後讓 AI 基於這個「事實網」回答問題

## [參考連結]

- 原始影片：[Ontology vs Metadata: What's the Difference? \[TalkIT Global 184, En-core\]](https://www.youtube.com/watch?v=ve7AA01vplE)（2026-04-05，長度 4:46）

