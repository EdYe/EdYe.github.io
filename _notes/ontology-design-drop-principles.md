---
title: '本體設計是工藝：Ontology四大原則'
date: 2026-08-09
image: /images/AI筆記/ontology-design-drop-principles.jpg
category: AI筆記
tags: [Ontology設計, 衍生屬性, 介面驅動工作流, 安全原語, 結構體]
description: 'Palantir DevCon 5 剖析 Ontology 進階功能：衍生屬性、介面、結構體、安全原語與物件背書連結，提煉四大本體設計原則解決企業資料痛點。'
quote: '💡「Ontology 設計是一門工藝（Tradecraft），而非單純的需求文件。本體即是你組織運作的軟體。」'
action: '🎯依D-R-O-P法則設計本體：以領域驅動定義物件、重複三次即重構為介面、鎖定核心開放延伸、用PECS實現即插即用彈性。'
source_has_timestamps: true
---
# [核心摘要]

本影片由 Palantir Group Lead Landon Carter 於 DevCon 5 主講，深入剖析 Ontology 語言的最新功能——**衍生屬性（Derived Properties）**、**介面（Interfaces）**、**結構體（Structs）**、**安全原語（Security Primitives）**與**物件背書連結型態（Object-Backed Link Types）**。核心貢獻在於將多年實戰經驗提煉為四大本體設計原則，解決企業資料模型在擴展性、語意精準度與安全粒度上的痛點，並展示如何將這些原語層層堆疊以達到子單元格安全與實體解析等深度資料建模能力 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

***

# [詳細重點整理]

## 1. Ontology 演進歷程與設計原則總覽 [00:00]

Ontology 發展歷經三階段：**Golden Tables**（資料整合）→ **營運決策**（透過 Actions、Logic、Functions 捕獲組織動態）→ **AI-First**（整合 LLM 與自動化）。Gotham 產品長期處理非結構化情報資料，累積了將非結構化資料「本體化」的深厚能力，這套經驗延伸至 Foundry 與 AIP，形成經過實戰驗證的深度本體系統 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

**關鍵概念：四大本體設計原則（Four Ontology Design Principles）**

- **領域驅動設計（Domain-Driven Design）**：真實世界物件應與本體中的虛擬分身一對一對應，捕捉語意意圖，而非僅複製資料集結構 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)
- **不重複原則（Don't Repeat Yourself, Rule of Three）**：同樣的東西建了三次就應重構，捕捉共用工作流或資料，有助於人類與 Agent 的上下文管理 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)
- **開放擴展、封閉修改（Open-Closed Principle）**：鎖定核心工作流不被意外破壞，同時允許其他開發者延伸新的工作流與資料型態 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)
- **生產者延伸、消費者超型（PECS — Producer Extends, Consumer Super）**：即共變與逆變（Covariance & Contravariance），透過介面設計實現即插即用的本體彈性 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

這四項原則本質上是**軟體設計原則**，可借鑑程式語言研究與軟體工程領域的長期成果 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

## 2. 介面（Interfaces）：多繼承與介面驅動工作流 [07:27]

介面允許建構**介面驅動工作流**，可套用至任何實作該介面的物件型態。範例中 `Building` 介面由 `Restaurant`、`OfficeBuilding`、`Arena` 三種物件型態實作，無需為每種型態建三份相同 App。Foundry Ontology 支援**多重繼承**，`Arena` 同時繼承 `Building` 與 `SchedulableResource`，可用於建築工作流或排程資源工作流。介面亦支援**多層級**，介面可延伸其他介面 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

**關鍵概念：組合優於繼承（Composition Over Inheritance）**

介面對應設計原則：領域驅動設計（抽象思考不被資料集怪癖綁架）、不重複原則（避免工作流複製）、開放封閉原則（鎖定核心介面、允許延伸）、PECS（`? extends Event` 可安全傳入 NBA Games；`? super Event` 可安全消費 DevCon Keynote）。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

## 3. 結構體、歸約器與主欄位（Structs, Reducers, Struct Main Fields） [12:37]

**結構體（Structs）** 將多個欄位群組為單一屬性，如 `Address` 包含街道、城市、州、郵遞區號，同時可捕捉元資料（來源、建立者、建立時間）。在 AIP Logic 中，結構體可將 LLM 推理過程本體化，例如 Slack Helper Bot 捕獲回應、最相關 Slack 訊息、文件 URL 與 LLM 推理邏輯，供下游處理 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

**關鍵概念：歸約器（Reducers）與結構主欄位（Struct Main Fields）**

- **Reducers**：Gotham 中每個屬性可有多值（不同來源、安全層級、時間版本）。Reducer 從清單中提取最相關值（如最近修改的地址），UI 預設顯示單一值，hover 時展開完整歷史 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)
- **Struct Main Fields**：定義結構中的「主欄位」（如 Geolocation 中的 GeoPoint），使該結構可如同一般 GeoPoint 屬性使用於所有 GeoPoint 工作流，元資料隱藏於 hover 展開 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

## 4. 衍生屬性（Derived Properties）：避免資料反規範化 [17:50]

以組織圖為例，`PeepNames` 與 `PeepCount` 可透過定義語意業務邏輯從連結物件推導，而非將資料反規範化（Denormalize）複製到本人物件上。資料維持**規範化格式**，避免資料 brittleness（當下屬改名或新增時資料不同步）。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

**關鍵概念：規範化推導（Normalized Inference）**

衍生屬性體現領域驅動設計：以語意方式表達物件，避免資料重複與反規範化的脆弱性 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

## 5. 安全層級堆疊：從資料集到子單元格安全 [19:40]

安全粒度可逐層提升：

| 安全層級 | 機制 | 說明 |
|---|---|---|
| Level 0 | 資料集安全 | 所有資料套用相同安全 |
| Row-wise | 限制檢視 / OSPs | 特定行機密（如 VIP 病患） |
| Cell-level | OSPs + 欄位安全 | 特定欄位不同安全標記 |
| Sub-cell | 衍生屬性 | 陣列中每個元素獨立安全層級 |
| Entity Resolution | 衍生屬性 + 連結 | 合併物件後各自保留原始安全  [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk) |

**關鍵概念：子單元格安全（Sub-Cell Security）**

透過衍生屬性將病患備註陣列拆分，每個元素可擁有獨立安全層級，如「病患懷疑配偶下毒」可標記為更高機密。實體解析（Entity Resolution）可合併 Diana Mercer 與 Diane Mercer 為同一人，合併後兩物件各自保留原始安全標記 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

## 6. 物件背書連結型態（Object-Backed Link Types） [23:13]

以員工與創業團隊為例，`VentureStaffing` 物件捕捉員工在特定團隊的工作元資料。某些工作流只需直接從 Employee 連結到 Venture（忽略 Staffing 中介），某些則需透過 Staffing 篩選（如找當前團隊）。**Object-Backed Link Types** 允許以 `VentureStaffing` 物件實作 Employee→Venture 連結，同時支援兩種使用模式 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

**關鍵概念：語意連結（Semantic Links）**

連結應代表語意上有意義的概念；有時中介物件是語意核心，有時只是輔助物件需被隱藏。Object-Backed Link Types 兩者皆可達成 。 [youtube](https://www.youtube.com/watch?v=_b2qsKz_Ifk)

***

# [結論與行動建議]

**啟發金句**

> 「Ontology 設計是一門工藝（Tradecraft），而非單純的需求文件。本體即是你組織運作的軟體。」

**具體行動建議 — D-R-O-P 法則**

- **D**omain-Driven：讓物件一對一映射真實世界概念
- **R**efactor（Rule of Three）：重複三次即重構為共用介面
- **O**pen-Closed：鎖定核心、開放延伸
- **P**ECS：以介面設計實現即插即用彈性

**生活實踐建議**

在設計 AI Agent 的知識圖譜或企業資料模型時，先從領域語意出發定義介面，再以結構體捕捉元資料與 LLM 推理過程，以衍生屬性維持資料規範化，最後以安全原語堆疊實現精細存取控制。避免直接在 Pipeline Builder 中「下一步到底」複製上游資料集結構，應退一步從第一原理思考工作流。

***

# [參考連結]

原始 YouTube 影片：[https://www.youtube.com/watch?v=_b2qsKz_Ifk](https://www.youtube.com/watch?v=_b2qsKz_Ifk)
