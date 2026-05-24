---
title: '打造 AI-Native 工程組織：瓶頸已從寫程式轉移至驗證與審查'
date: 2026-05-24
image: /images/影片筆記/running-ai-native-engineering-org.jpeg
category: 影片筆記
tags: [AI原生組織, 瓶頸遷移, 規劃文化, 人員配置, 代碼審查]
description: '當 AI 輔助編碼成為組織預設工作模式時，瓶頸已從「寫程式」轉移至「驗證、審查與維護」。Anthropic Claude Code 工程負責人 Fiona Fung 分享五大組'
quote: 'What served you prior may no longer.——過去讓你成功的，未必還適用今天。'
action: 'Claudify（讓 Claude 做能做的）、Code Wins（以 Prototype 取代辯論）、Kill Old Processes（主動刪除舊流程）'
source_has_timestamps: true
---
# Running an AI-Native Engineering Org

## 核心摘要

當 AI 輔助編碼成為組織預設工作模式時，**瓶頸已從「寫程式」轉移至「驗證、審查與維護」**。Anthropic Claude Code 工程負責人 Fiona Fung 透過自身帶領 Claude Code 團隊的實戰經驗，揭示了舊流程如何「悄悄失效」，並分享了五大面向的組織重塑策略——從規劃文化、代碼審查、人員配置，到知識管理，核心訴求是：**持續審視舊流程是否仍有其存在意義**。 [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

***

## 詳細重點整理

### 1. 瓶頸已轉移 [00:52]

過去數十年，**工程師的編碼時間**是最稀缺的資源，所有流程（需求規劃、設計文件、Code Review）都是為了保護這個資源而設計的。 現在 Claude 已讓編碼、寫測試、重構都不再是瓶頸，新的瓶頸變成： [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

- **Verification（驗證正確性）**：產出量激增，「程式碼是否正確」更需被嚴格把關
- **Who reviews（誰來審查）**：角色邊界模糊，人人都在提交變更
- **How is it maintained（如何維護）**：高吞吐量帶來更高的維護成本

> **關鍵概念：瓶頸遷移（Bottleneck Migration）** — 就像 2000 年代從「Server Room Build Queue」到雲端 CI/CD 的轉變，AI 時代的瓶頸再次位移。

***

### 2. 必須重寫的團隊規範 [06:55]

以下舊流程在 Claude Code 團隊已「悄悄停止運作」： [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

| 舊規範 | 新做法 |
|---|---|
| 長篇設計文件（Design Doc）| 討論在 PR 或 Prototype 中進行 |
| 「誰改了這段程式？」追責思維 | 改問「你真正想找到什麼答案？讓 Claude 幫你」 |
| 技術辯論用白板開會 | 直接生成 3 個不同版本的 PR 來比較 |
| iOS/Android 分開獨立團隊 | 工程師可跨平台 Flex，考慮合併 |
| Onboarding 需大量找人詢問 | 以 Claude 作為 Tech Deep Dive 的第一對象 |

> **關鍵概念：「靜默失效（Quietly Stops Working）」** — 流程往往在失效後仍被慣性執行，需定期主動稽核。

***

### 3. 規劃文化：Code Wins [07:52]

**「Building is cheap, argument is expensive」** 是新的技術辯論準則。 與其開會白板討論，不如直接生成多版本 prototype 比較實作影響。Test-Driven Development 在 AI 輔助下也重新變得「有樂趣」——先寫測試讓它 fail，再讓 Claude 修 bug，流程體驗大幅改善。 [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

> **關鍵概念：Code-First Decision Making** — 以可執行的程式碼取代抽象的文字討論。

***

### 4. 人員配置：兩種核心 Profile [12:27]

角色邊界持續模糊（設計師直接用 Claude 做 UI 修正、工程師讓 Claude 輔助內容文案），Fiona 聚焦培養兩種人才 ： [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

1. **Creative Builders with Product Sense**：有產品直覺的創意建造者
2. **Deep System Expertise**：具備深層系統架構能力的專家

「Product Sense」的培養核心方法是 **Dog Fooding（Anthropic 內部稱 Ant Fooding）**：主管必須親身使用自己團隊的產品，才能「用身體感受產品」（feel it in your bones）。

> **關鍵概念：Ant Fooding** — 管理者親身使用產品是建立 Product Sense 的最直接路徑。

***

### 5. 代碼審查與知識管理的新秩序 [11:08]

Code Review 由 Claude 負責風格、Lint、明顯 Bug 與規格漂移偵測，但**人類必須保留在迴圈中**，尤其是 ： [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

- 法律合規審查
- 風險容忍度判斷（Trust Boundary）
- 產品品味（如 Fiona 把 Claude 的 snowman 做成「Mr. Peanut」的案例）

知識來源也從「文件」轉移至「程式碼本身即真理」——所有 Spec、規格都應 check-in 進 codebase，讓 Claude 得以直接驗證。

> **關鍵概念：Code as Source of Truth（程式碼即真相）** — 文件容易過時，程式碼才是最即時的知識載體。

***

## 技術/數據對比

| 指標 | 導入 AI 前 | 導入後趨勢 |
|---|---|---|
| Onboarding Ramp-up 時間 | 較長，需頻繁向隊友詢問 | 顯著下降 |
| PR Cycle Time | 受限工程師產能 | 下降（但需分拆各階段分析） |
| Claude-assisted Commits | 偶爾 | 近 100%（幾乎每個 commit 都有 Claude 協作）|
| 設計文件工作量 | 高（需長篇 Design Doc）| 大幅降低，改為 PR / Prototype |

 [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

***

## 結論與行動建議

**啟發金句：**
> **「What served you prior may no longer.」**——過去讓你成功的，未必還適用今天。 [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

**具體行動法則：C-C-K 法則**
- **Claudify（Claude 化）**：只要 Claude 能做的，就讓 Claude 做
- **Code Wins（程式勝出）**：以可執行的 Prototype 取代抽象辯論
- **Kill Old Processes（主動殺死舊流程）**：給予團隊明確的「刪除舊流程許可」

**生活實踐建議：**
立即盤點你團隊中一個「每個人都覺得低效但沒人動」的會議或流程（如每週冗長的 Status Update 會議），問自己：這個流程的原始目的是什麼？Claude 能否替代或簡化它？從最「高稅」的那個工作流開始實驗。 [youtube](https://www.youtube.com/watch?v=l9hUGbg0Ljo)

***

## 參考連結

- 原始影片：[https://youtu.be/IA5LWIGqnyM](https://youtu.be/IA5LWIGqnyM)
