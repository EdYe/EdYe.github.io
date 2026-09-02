---
title: '語意層與本體論：打造可信賴 AI 的地基'
date: 2026-09-02
image: /images/AI筆記/semantic-layer-ontology-trusted-ai.jpg
category: AI筆記
tags: [可信賴AI, 情境層, 能力問題, 語意壓縮, AI冰山]
description: '可信賴 AI 的瓶頸不在模型，而在語意基礎建設：LLM 參數層天生已剝除資料出處，檢索層（語意層＋知識圖譜）是補回情境與血脈的唯一機會。'
quote: '模型是人人買得到的商品；你的 ontology 是組織的數位指紋——偷不走，更外包不得。AI 時代的護城河，不在你能買到什麼模型，而在你連得起什麼資料。'
action: '🎯依 C-Q-O 法則：Case 挑一個答錯代價最高且 ROI 可證明的小用例；Questions 用該部門商業語言寫下 10–15 個能力問題；Ontology 只為這些問題建最小 ontology，接上檢索層、量測準確度後迭代。'
source_has_timestamps: true
source_raw: How Semantic Layers and Ontologies Create Trusted AI
---
**影片資訊**：《How Semantic Layers and Ontologies Create Trusted AI》— ThoughtSpot《The Data & AI Chief》Podcast 第 135 集（2026-04-22，53 分 20 秒）。主持人 Cindi Howson（ThoughtSpot 首席資料與 AI 策略長），來賓為 Jessica Talisman（The Ontology Pipeline 創辦人、前 Adobe 資深資訊架構師）與 Tony Seale（The Knowledge Graph Guys 創辦人）。 [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

## [核心摘要]

可信賴 AI 的瓶頸不在模型，而在語意基礎建設：LLM 參數層天生已剝除資料出處，檢索層（語意層＋知識圖譜）是補回情境與血緌的唯一機會。企業應以能力問題驅動、從小用例建 ontology——它是組織的「數位指紋」，在 AI 商品化時代更是不可外包的唯一護城河 。 [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

## [詳細重點整理]

1. 開場定位：語意層是「下一個兆美元機會」[00:00]
- 語意層與情境層是可信賴 AI 的關鍵成分，部分創投稱其為「下一個兆美元機會」[01:27]
- 專家背景互補：Jessica Talisman 有 25 年圖書資訊學（library science）與企業 AI 經驗；Tony Seale 十餘年為一級投資銀行交付任務關鍵知識圖譜
- 開場即點題：AI 時代是「網路形狀」，緊抓「箱子形狀」舊思維者將被淘汰；ontology 是組織的數位指紋與護城河
- 關鍵概念：**可信賴 AI（Trusted AI）** [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

2. BI 語意層 vs AI 情境層 [02:21]
- 語意層三階段演化：1990 年代 BusinessObjects 起源 → 指標層（metric layer）→ 現階段納入受控詞彙與人機可讀標籤；但傳統語意層「止於標籤」[03:52]
- 詞彙歧異實例：美式 revenue＝英式 bookings／turnover；ontology 提供正式結構，定義概念之間如何關聯 [05:00]
- 情境層＝語意＋資料項目＋網路。AI 作答流程：自然語言問題 → 依語意消歧概念 → 沿概念關係遍歷（revenue→profitability→outcome）→ 下鑽至特定資料點（某客戶的實際營收）→ 精準回答 [05:55]
- Ontology 是企業運作本質的萃取：業務專家語言中的名詞成為概念、動詞成為連結；context 源自概念間的關係 [08:26]
- 同詞異義陷阱：sales 對業務員＝訂單開立（佣金依據）、對現金基礎財務＝款項入帳——同一名詞、截然不同的結果 [09:28]
- 關鍵概念：**情境層（Context Layer）** [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

3. 知識圖譜的本質：三元組與符號 AI [09:22]
- 知識圖譜＝資料意義的網路，也是一種架構（如同 data architecture）：結構化概念、關係並建模資料，以三元組（subject–predicate–object）陳述描述 [10:32]
- 「這不就是邏輯資料建模？」——否：知識圖譜仍分概念／邏輯／實體三層，但奠基於開放標準，屬符號 AI（symbolic AI）；詞彙＝概念層、ontology＝邏輯層、知識圖譜＝兩者之結合 [12:00]
- 應用最成熟產業：醫療居首（成功的基因體 AI 研究依賴 ontology）、金融次之；互操作性是研究與創新的前提 [13:04]
- 關鍵概念：**三元組（Triple Statements）** [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

4. 網路形狀革命：關係升級為一等公民 [14:04]
- 與關聯式建模的差異一：資料形狀從矩形箱子（集合思維）變為網路，關係與實體同等重要，不再只是表格 join [14:04]
- AI 本身就是神經網路——把資料放上與 AI 相同的形狀，模型天然契合此結構 [15:14]
- 差異二：傳統模型 schema 與資料分離存放；知識圖譜從抽象概念層到具體資料點是同一網路，可無縫往返，實體模型「幾乎消失」[15:38]
- 關鍵概念：**一等公民關係（First-class Relationships）** [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

5. 打造企業 Ontology：大處思考、小處交付 [17:04]
- 從單一小流程開始建模，別妄想一次模型化全公司；能撐起 agent 間溝通的企業目前寥寥無幾 [17:06]
- 紀律優先、model first：「連一個簡單 chatbot 都撐不起來，就還沒到位」[18:00]
- 資料建模技能的衰落歸因於視覺化資料探索工具（拿到 dump 直接上）；AI 與 chatbot 時代必須重拾建模紀律 [19:16]
- Dave McClean 名言「thinking big but delivering small」：先選高價值、ROI 可證明的用例，ontology 的 class 本身沒有價值 [20:23]
- 用商業語言寫能力問題（competency questions），由問題「衍生」ontology，避免陷入哲學迷宮；每個 class 都要對應可回答、具高商業價值的問題 [21:11]
- 參考金融業出身的 DPROD（語意資料產品規格）：將資料產品直接綁定 ontology class [21:58]
- 別執著圖形視覺化：圖譜常淪為一團無定形「毛球（hairball）」，對決策無用；知識圖譜像家中電線——按開關、燈就亮 [22:27]
- 資料中的連線跟隨人際連線：組織轉型挑戰與技術挑戰一樣大 [23:27]
- 關鍵概念：**能力問題（Competency Questions）** [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

6. Adobe 實戰案例：前銷與後銷的語意斷層 [25:00]
- 場景為 Adobe DX 事業群（Adobe Analytics、AEP）；最大痛點是 pre-sale 與 post-sale 之間巨大的理解與語言斷層 [25:14]
- 第一順位：以語意層調和詞彙——全公司統一術語，或用 ontology 連結歧異詞彙 [25:40]
- 應用：以 ontology 支援完整客戶旅程——簽約後自動分派 solutions consultant、即時識別學習與教育支援需求 [26:54]
- 用知識圖譜打造 auto-tagger，自動標記文件與學習物件並分派給 post-sale 客戶 [27:37]
- 前後對比：過去在 SQL 環境「縫合（stitching）」資料 → 現在以 AI 為協作夥伴＋ontology／知識圖譜 [28:07]
- 關鍵概念：**語意調和（Semantic Reconciliation）** [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

7. OSI 與 YAML：語意壓縮的妥協 [28:38]
- OSI（Open Semantic Interchange）由 Snowflake 領頭，ThoughtSpot、dbt、Atlan 為貢獻者，Databricks 近期加入 [28:38]
- 「縫合」是舊肌肉：複雜 SQL join 與手工映射本質上不具語意性 [29:31]
- YAML 也不是語意的：Adobe 曾把 ontology 壓平成 YAML config 檔上線，大量語意當場被剝除 [29:46]
- 務實立場：關聯式資料庫不會也不該消失；語意層是「疊加」在既有基礎建設上的介面層 [31:31]
- OSI 是產業正面的一步，但仍是妥協：矩形形狀會壓縮語意。Ontology 支援豐富階層——各部門共用抽象的「sale」概念、再以子類繼承（動物界分類法類比），連關係本身都能繼承；星狀綱要則必須把這一切壓平 [31:55]
- 時代論：工業時代＝機器隱喻與箱子；AI 時代＝網路形狀，緊抓箱形思維者將被拋下 [34:26]
- 關鍵概念：**語意壓縮（Semantic Compression）** [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

8. 補上出處缺口：資料血緌 [34:19]
- LLM 雙層結構：參數層（出廠即以網路訓練，出處大多已被剝除）＋檢索層（RAG 等）——檢索層是注入 context 與 provenance 的唯一機會 [35:30]
- 千年知識生態靠 provenance 演化（站在巨人肩膀上）；LLM 會抄襲且未必告知，接收其輸出若不保留出處，等於切斷知識演化血緌 [36:44]
- 圖書資訊學已有數世紀的 scholarly communication 傳統；圖書館目錄本身就有 ontology 骨幹，連結 Wikipedia、Wikidata [37:37]
- 核心主張：「你收到資訊的準確度，取決於該資訊來自 LLM 時的血緌／出處」[38:23]
- 關鍵概念：**資料出處（Provenance）** [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)

9. Ontology 是你最有價值的 IP [39:27]
- AI 商品化時代，內部資料關係是唯一護城河；把 ontology 放在第三方代管，等於把核心資產置於險境 [podcasts.apple](https://podcasts.apple.com/us/podcast/how-semantic-layers-and-ontologies-create-trusted-ai/id1509495585?i=1000763041334)
- AI 冰山：別盯著頂端的演算法與模型；領導者要看水面下的資料基礎建設，並「把現有模型的能力回頭用在自己的內部基礎建設上，建出豐富 ontology、連結自身資訊」 [linkedin](https://www.linkedin.com/posts/thoughtspot_thedataaichief-activity-7452703317757104128-d2zS)
- 警語：若讓他人拿走你的 ontology、學到你與世界分佈之外的知識本質，等於送走公司所有有價值的東西 [podcasts.apple](https://podcasts.apple.com/us/podcast/how-semantic-layers-and-ontologies-create-trusted-ai/id1509495585?i=1000763041334)
- Ontology 是組織的數位指紋：每個組織獨一無二，你對事物的定義未必與 LLM 相同——這正是差異化所在 [podcasts.apple](https://podcasts.apple.com/us/podcast/how-semantic-layers-and-ontologies-create-trusted-ai/id1509495585?i=1000763041334)
- 關鍵概念：**AI 冰山（AI Iceberg）** [podcasts.apple](https://podcasts.apple.com/us/podcast/how-semantic-layers-and-ontologies-create-trusted-ai/id1509495585?i=1000763041334)



## [結論與行動建議]

**啟發金句**：模型是人人買得到的商品；你的 ontology 是組織的數位指紋——偷不走，更外包不得。AI 時代的護城河，不在你能買到什麼模型，而在你連得起什麼資料。

**具體行動建議——C-Q-O 法則** ： [youtube](https://www.youtube.com/watch?v=P7fRamgIWqI)
- C（Case）：挑一個「答錯代價最高」且 ROI 可證明的小用例，大處思考、小處交付
- Q（Questions）：用該部門的商業語言寫下 10–15 個能力問題
- O（Ontology）：只為這些問題建模最小 ontology，接上檢索層、量測準確度後迭代；先撐起一個簡單 chatbot，再談自治企業

**生活實踐建議**：
- 在自家 MCP／RAG 工作流放入一份輕量 ontology（名詞＝概念、動詞＝關係），先讓內部問答 bot 通過「簡單 chatbot 測試」
- 為 AI 諮詢／架構審查服務新增「語意資產健檢」項目：盤點各部門同詞異義（sales、customer 的定義衝突），並檢查 ontology 是否被第三方 SaaS 代管
- 個人知識庫每則引用保留來源與日期；RAG 系統保留 citation 欄位，避免血緌斷裂、LLM 抄襲不自知的問題在自己的系統重演

## [參考連結]

- 原始 YouTube：[How Semantic Layers and Ontologies Create Trusted AI](https://youtu.be/P7fRamgIWqI)
- [The Ontology Pipeline® — Jessica Talisman](https://jessicatalisman.substack.com/p/the-ontology-pipeline)
- [Why Early Knowledge Graph Adopters Will Win the AI Race](https://www.knowledge-graph-guys.com/blog/why-early-knowledge-graph-adopters-will-win-the-ai-race)
- [Spec-First Development: Why LLMs Thrive on Structure, Not Vibes](https://www.knowledge-graph-guys.com/blog/vibes-vs-spec-first-development)
- [The Knowledge Graph Academy](https://www.knowledge-graph-guys.com/academy)