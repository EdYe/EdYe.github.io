---
title: 'Skill vs Prompt 的本質差異：程序可攜性才是 Agent 瓶頸'
date: 2026-06-23
image: /images/影片筆記/skill-vs-prompt-portable-procedure.jpg
category: 影片筆記
tags: [程序可攜性, Skill, 驗證契約, 可組合性, 程序複利]
description: 'AI Agent 的真正瓶頸不是記憶體，而是程序可攜性。當你在 Cursor、Claude Code、Codex 之間切換時，精心調教的 Agent 行為規則無法跨工具遷移'
quote: '你可以移動你的上下文，你可以移動你的程序，你可以把更好的工具插進同一個操作層——這才是「開放」真正的意義。'
action: '把反覆跟 AI 解釋超過 3 次的事情寫成 skill.md，每個 skill 定義完成證明，每次 session 後問「有沒有值得保存的程序？」'
source_has_timestamps: true
---

# [核心摘要]

AI Agent 的真正瓶頸不是記憶體，而是**程序可攜性**。當你在 Cursor、Claude Code、Codex 之間切換時，精心調教的 Agent 行為規則無法跨工具遷移，導致工作者不斷重新解釋相同的操作程序。Open Skills 提出「可攜式程序層」的解法：用標準化的 skill.md 文件，讓 Agent 程序成為你個人的資產而非被工具平台鎖定。 [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)

***

# [詳細重點整理]

## 1. 記憶不夠，程序才是核心 [00:00]

Open Brain（前一個計畫）解決了 Agent 的上下文記憶問題，但記憶解決後仍存在第二個更深的問題：即使 Agent 知道你的專案背景，它仍不知道「你怎麼工作」。 每次新 session 都必須重新解釋：搜尋要用即時資料、文章不能有 AI 腔、測試要真的開瀏覽器驗證——這些是**程序問題**，不是記憶問題。 [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)

**關鍵概念：程序性債務（Procedural Debt）**

## 2. 四大程序性債務症狀 [01:39]

程序性債務在嚴肅使用者的工作流中以四種型態出現 ： [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)

- **Prompt 膨脹**：把所有規則塞進巨大的系統提示，各規則互相搶奪注意力，導致 Agent 表現更差
- **重新解釋稅**：每次切換工具（Cursor → Claude Code → Codex）都得重新建立工作標準，這是「偽裝成工作的前置作業」
- **指令碎片化**：規則分散在不同工具的設定檔中，各自漂移、互不同步
- **弱驗證**：Agent 說「完成」但連結失效、行動裝置版面跑版、程式碼從未被測試

**關鍵概念：重新解釋稅（Re-explanation Tax）**

## 3. Skill 是什麼？與 Prompt 的本質差異 [05:36]

一個 Skill 是一個包含 `skill.md` 的小資料夾，定義了六個維度 ：何時使用、何時不使用、負責的工作範圍、需要的工具與檔案、輸出格式、以及**驗證標準**。 [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)

| 維度 | Prompt | Skill |
|------|--------|-------|
| 使用時機 | 一次性請求 | 可重複載入的程序 |
| 知識型態 | 模糊語義 | 明確觸發條件 |
| 驗證機制 | 無 | 內建 proof standard |
| 跨工具可攜 | ❌ | ✅ |

**關鍵概念：Agent 可操作程序（Agent-operable Procedure）**

## 4. Skills 是積木，Runbooks 是組合 [08:46]

Skills 是基本單元（primitives），Runbooks 是組合流程（composition）。以創作者工作流為例： [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)
- **語音備忘錄** → `media-transcription` skill → `brain-dump-processing` skill → `personal-voice` skill → `HTML-artifact-builder` skill → `personal-site-publisher` skill（含驗證）

這種架構確保每個 skill 只負責自己的合約，轉錄 skill 不需要知道如何發布，發布 skill 不需要知道如何測試瀏覽器。

**關鍵概念：可組合性（Composability）**

## 5. 驗證：Agent 工作的信任基礎 [11:09]

當 AI 主要生成文字時，人們可以容忍模糊的信心表達。但 Agent 執行動作後，必須要求**可驗證的證明** ：程式碼修改後哪個測試通過？頁面發布後檢查了哪個 URL？引用的是什麼日期的資料？好的 Skill 能預先定義「完成」的標準：「除非這個證據存在，否則不得宣稱完成。」 [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)

**關鍵概念：驗證契約（Verification Contract）**

## 6. 飛輪效應：Session → Skill 萃取 [12:53]

Open Skills 的 `session-to-skill-extractor` 機制，在每次重要 Agent session 結束後詢問：「我們是否發現了值得保存的非顯而易見程序？」 若有，將其提煉為 skill candidate，而不讓它消失在聊天記錄中。 [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)

**Open Brain 複利**：每次捕捉想法讓未來檢索更好。
**Open Skills 複利**：每次保存好程序讓未來工作更可靠。

**關鍵概念：程序複利飛輪（Procedure Compounding Flywheel）**

## 7. Open Brain + Open Skills 整合層 [15:27]

兩個系統分工互補 ： [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)

- **Open Brain** = Agent 的上下文層（專案背景、決策歷史、關鍵人物）
- **Open Skills** = Agent 的程序層（如何研究、如何撰寫、如何測試、如何發布）

在多模型世界中，當你必須切換到更好的新工具時，兩層都跟著走，不再被任何 SaaS 供應商鎖定。

**關鍵概念：可攜式操作層（Portable Operating Layer）**

***

# [結論與行動建議]

**啟發金句：**
> 「你可以移動你的上下文，你可以移動你的程序，你可以把更好的工具插進同一個操作層——這才是『開放』真正的意義。」 [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)

**具體行動建議（S-V-C 法則）：Skill → Verify → Compound**
1. **Skill**：把你反覆跟 AI 解釋超過 3 次的事情，寫成一個 `skill.md`
2. **Verify**：每個 skill 必須定義「完成的證明」，拒絕模糊的 done
3. **Compound**：每次重要 session 結束後，問：「有沒有值得保存的程序？」

**生活實踐建議：**
作為 AI 應用架構師，你可以立刻從三個場景實踐：
- **跨工具開發**：將 Claude Code 和 Cursor 的共用測試標準抽象為一個可攜式 `qa-verification` skill
- **內容發布**：建立個人 `voice-style` skill，不再讓每個 AI 工具各自猜測你的文風
- **團隊協作**：將 onboarding 流程做成 runbook，讓新成員或新 Agent 都能快速對齊工作標準

***

# [參考連結]

- 原始影片：https://youtu.be/9PUaEj0pMYE?si=EfEsGIs2phpo6bQ7 [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)
- Open Skills 完整指南（Newsletter）：https://natesnewsletter.substack.com/p/claude-codex-agent-skills [youtube](https://www.youtube.com/watch?v=4vWXpzlL7Mo)
