---
title: 'AI技能庫v1.1：新增Wayfinder規劃術'
date: 2026-07-09
image: /images/AI筆記/ai-skills-repo-v1-1-wayfinder.jpg
category: AI筆記
tags: [規格導向命名, 事實與決策分離, 流程串接, 臭味喚名, 共享地圖式規劃]
description: 'Matt Pocock 發布 AI 開發技能庫 v1.1 更新，將零散規劃技能整合成完整 SDLC 流程，並新增 Wayfinder 解決大型專案規劃困境。'
quote: '💡一個模糊的想法太大，裝不進單一 agent session，還籠罩在迷霧中——這正是 Wayfinder 存在的理由。'
action: '🎯套用 G-S-T-I-C 法則（Grill → Spec → Tickets → Implement → Code Review）作為日常 AI 協作開發的標準流程骨架。'
source_has_timestamps: true
---
# Matt Pocock AI 開發技能庫 v1.1 更新筆記

本文整理 Matt Pocock 發布之 AI 開發技能庫（skills repo）v1.1 版本重點，涵蓋新版 SDLC 流程、Grilling 技能修正與全新 Wayfinder 大型規劃技能。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

## [核心摘要]

Matt Pocock 發布其 AI 開發技能庫（skills repo）的 v1.1 更新，核心貢獻是把原本零散的「規劃型技能」整合成一套完整的**軟體開發生命週期（SDLC）流程**，並新增 **Wayfinder** 技能來解決大型專案「規劃過大、超出單一 agent session 智慧區（smart zone）」的痛點。此版本同時修正了 grilling 技能中「多問題同時詢問」與「自我 grilling」等已知 bug。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

## [詳細重點整理]

1. 技能改名：to-spec 與 to-tickets [00:37]
原本的 to-prd 改名為 **to-spec**，to-issues 改名為 **to-tickets**，因為 PRD（產品需求文件）語意過窄且過去內容常「外溢」超出 PRD 範疇；issues 一詞則過度偏向 GitHub/Linear 特定工具語言。關鍵概念：**規格導向命名（spec-driven naming）**，強調命名要精確反映實際產出物。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

2. Grilling 技能改進 [02:34]
新增「不要同時問多個問題」的強化提示、在對話結束時加入**確認閥（confirmation gate）**，要求使用者明確確認雙方已達成共識後才進入實作，避免 grilling 結束後直接跳進 implementation。此外區分「事實（facts，探索程式碼庫得出）」與「決策（decisions，需使用者決定）」以修正 agent 自我 grilling 的怪異行為，關鍵概念：**事實與決策分離（facts vs. decisions）**。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

3. 完整開發生命週期流程 [04:06]
新流程為：grilling → spec → tickets → implement → code review → commit，其中 **implement** 技能刻意保持極簡（TDD、定期型別檢查、單測試檔案、最終全套測試）以填補「規劃到實作」之間的空隙。關鍵概念：**流程串接（flow chaining）**，每個技能負責生命週期中的一個明確階段。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

4. Code Review 與重構臭味 [06:45]
Code review 技能從兩個軸並行子代理審查：**標準軸**（是否符合 repo 的 coding standards.md）與**規格軸**（是否忠實實現原始 spec/issue）。新版引入 Martin Fowler《Refactoring》中定義的「程式碼異味」術語（如神秘命名、重複程式碼、特徵依戀、資料泥團、原始型別偏執、訊息鏈等），利用這些術語已深植於 LLM 先驗知識中的特性，只需一句話描述即可觸發 agent 精準辨識問題，關鍵概念：**臭味喚名（smell naming as prompt lever）**。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

5. Wayfinder：大型規劃新技能 [07:52]
**Wayfinder** 專為「想法太模糊、太大、無法在單一 agent session 完成」的情境設計，會在 GitHub issue 上建立共享地圖（map），並拆分成多張帶阻塞關係（blocking relationships）的子 issue，逐一擊破直到路線清晰。子任務類型包含 research（研究型 AFK 任務）、grilling（需人機對話決策）、prototype（先做低成本原型再討論）與一般 tasks（設定、資料搬移等），關鍵概念：**共享地圖式規劃（shared map planning）**。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

6. 支援技能：research 與 prototype [11:21]
新的 **research** 技能會啟動背景 agent，針對主要來源進行調查並寫成 markdown 筆記，使用者可以邊等邊工作；**prototype** 技能則讓 agent 自行選擇建立「邏輯原型」或「UI/狀態原型」，用來在動工前提高討論的具體程度，尤其適合牽涉前端的專案。關鍵概念：**低成本具象化（cheap concrete artifact）**。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

7. TDD 技能簡化 [12:12]
TDD 技能改為「僅供參考」，不再規定具體對話步驟，只強調測試撰寫順序為 **red before green**，並將重構抽離出主迴圈，不再是傳統的 red-green-refactor，而是單純的 red-green，重構工作移交給 code review 階段處理。關鍵概念：**紅綠分離（decoupling refactor from TDD loop）**。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

## [技術/數據對比]

| 項目 | v1 舊版 | v1.1 新版 |
|---|---|---|
| PRD 相關技能 | to-prd | **to-spec**（更廣義、涵蓋技術與非技術內容） |
| Issue 相關技能 | to-issues | **to-tickets**（脫離 GitHub/Linear 特定術語） |
| TDD 循環 | red-green-refactor | red-green（重構移至 code review） |
| 大型規劃 | 僅有 Grill with Docs | 新增 **Wayfinder**（拆分多 session、GitHub 共享地圖） |

## [結論與行動建議]

**啟發金句**：「一個模糊的想法太大，裝不進單一 agent session，還籠罩在迷霧中——這正是 Wayfinder 存在的理由。」 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

**具體行動建議**：可套用 **G-S-T-I-C 法則**（Grill → Spec → Tickets → Implement → Code Review）作為日常 AI 協作開發的標準流程骨架。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

**生活實踐建議**：面對任何「太大、太模糊」的專案（不限於寫程式），可借用 Wayfinder 的思路——先在協作工具上建立共享地圖、拆解成有依賴關係的小任務，逐一厘清後再制定最終規格，作者本人甚至用它來規劃非程式類的新課程。 [youtube](https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD)

## [參考連結]

https://youtu.be/A8mokin_YOs?si=TR5dk2rhoQSoBjVD
