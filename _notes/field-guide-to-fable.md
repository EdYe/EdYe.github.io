---
title: 'Fable 實戰指南：解放 Claude 的四大框架'
date: 2026-07-07
image: /images/AI筆記/field-guide-to-fable.jpeg
category: AI筆記
tags: [能力斷層, 情境優先於限制, 地圖與疆域, 保持在迴圈中, 不講理原則]
description: '模型能力並非均勻成長，而是以「跳躍式」（spiky）的方式提升，這造成使用者難以掌握模型真正能做到什麼的痛點。'
quote: '💡建造變得更容易，但創造價值依然困難（Building is easier, but generating value is still hard）'
action: '🎯採用M-U-L法則：先畫Map、再用Fable挖掘Unknown、最後Log記錄偏差，確保工程師掌握主導權'
source_has_timestamps: true
---
# Field Guide to Fable — Anthropic 工程師實戰指南

這是 Anthropic Claude Code 團隊成員 Thariq Shihipar 在 AI Engineer 大會上的演講，主題聚焦於 Anthropic 最新模型「Fable」的實戰使用方法論。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)

## [核心摘要]

模型能力並非均勻成長，而是以「跳躍式」（spiky）的方式提升，這造成使用者難以掌握模型真正能做到什麼的痛點。演講提出四大框架：解放 Claude（unhobbling）、找出未知數、面對失落感、以及變得「不講理」，教導工程師如何重新設計提示詞策略、發現隱藏需求，並藉由新模型打破「好、快、便宜」三選二的傳統取捨迷思。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)

## [詳細重點整理]

1. 能力斷層與解放 Claude [00:53]
講者以「寶可夢名字以 AW 結尾」的例子說明：一般對話模型答不出來，但 Claude Code 能寫程式抓取清單並過濾答案。這揭示模型知識與模型能否「運用」該知識之間存在落差。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)
關鍵概念：**能力斷層（Capability Overhang）**

2. 系統提示詞的演化 [05:58]
Claude Code 近期刪減了 80% 的系統提示詞，因為過度的範例與指令反而限制了比範例更具想像力的新模型。團隊改用「提供情境（context）」取代「條列限制（constraints）」的方式來引導模型。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)
關鍵概念：**情境優先於限制（Context over Constraints）**

3. 提問工具的躍進 [07:02]
「詢問使用者問題」工具在 Opus 4 時期幾乎無法正常運作，到 Opus 4.5 時能主動訪談使用者達 40 個問題，而在 Fable 上已能生成嵌入式 HTML 問卷報告。這展示同一工具隨模型迭代產生質變的過程。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)
關鍵概念：**工具能力的漸進解鎖**

4. 地圖不等於疆域 [09:10]
講者將自己心中的規劃比喻為「地圖」，而實際程式碼庫與現實限制才是「疆域」；當 Claude 遇到地圖未標示的情況即為「未知數」。他提出已知的已知、已知的未知、未知的已知、未知的未知四象限矩陣，協助工程師系統性挖掘盲點。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)
關鍵概念：**地圖與疆域（Map vs. Territory）**

5. 六種挖掘未知數的技巧 [10:59]
包括：請 Claude 做「盲點掃描（blind spot pass）」了解陌生模組、用多版本原型探索設計偏好、讓 Claude 反過來訪談自己、提供參考程式碼作為「另一份地圖」、記錄實作偏差日誌，以及事後由 Claude 出題驗收理解程度。這些方法核心在於讓工程師「保持在迴圈中（stay in the loop）」。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)
關鍵概念：**保持在迴圈中（Staying in the Loop）**

6. 面對「失落感」的心理轉折 [14:32]
講者坦言使用 Fable 後同時感受到「巨大的獲得」與「一絲失落」，因為過去手寫程式碼、與程式碼庫共存的樂趣正在改變，但過去程式設計伴隨的失敗與熬夜除錯的痛苦也隨之減少。他總結「唯一的出路就是穿越它（The only way out is through）」。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)
關鍵概念：**得與失的並存**

7. 打破「不可能三角」變得不講理 [16:36]
Anthropic 文化信奉「取捨並不真實存在」，講者反思過去在自己創辦的 YC 創業公司中總被迫在「好、快、便宜」中選二，而現今用 Fable 四小時內就能做出一份高品質的完整演講簡報，證明三者可同時兼得。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)
關鍵概念：**不講理原則（Being Unreasonable）**

## [結論與行動建議]

啟發金句：**「建造變得更容易，但創造價值依然困難（Building is easier, but generating value is still hard）」**。 [telegra](https://telegra.ph/file/cb5de4740a27c00f7ca74.mp4)

具體行動建議：可採用 **M-U-L 法則**——先畫出 Map（寫下已知的目標與規格）、再用 Fable 主動挖掘 Unknown（未知數，透過盲點掃描、原型測試、反向訪談）、最後 Log（記錄實作偏差並讓模型驗收理解），確保工程師始終掌握主導權。

生活實踐建議：面對新一代 AI 工具時，不要急著寫出冗長的「不可以做什麼」指令清單，而是先提供足夠的背景情境，並主動請 AI 進行「盲點掃描」，找出自己沒意識到的知識缺口——這個方法同樣適用於學習新技能、規劃專案，甚至是日常決策時釐清自己真正的需求。

## [參考連結]

https://youtu.be/9fubhllmsBU
