---
title: 'Claude Code Dynamic Workflows：平行協調千個子代理'
date: 2026-06-30
image: /images/AI筆記/claude-code-dynamic-workflows.jpg
category: AI筆記
tags: [動態工作流程, 子代理, 並行編排, 編排模式, 對抗式驗證]
description: 'Claude Code Dynamic Workflows 是 Anthropic 於 2026 年 5 月 28 日隨 Claude Opus 4.8 推出的重大新功能，核心概念是讓 Claude 自動'
source_has_timestamps: false
---
Claude Code Dynamic Workflows 是 Anthropic 於 2026 年 5 月 28 日隨 Claude Opus 4.8 推出的重大新功能，核心概念是讓 Claude **自動撰寫一段 JavaScript 編排腳本**，在背景平行協調數十至上千個子代理（subagents）完成超大型任務，而不是塞在單一 context window 裡硬撐。 [claude](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

## 核心運作機制

當你描述任務後，Claude 動態生成編排腳本，決定如何切分任務、分配給多少並行 subagents，並做「對抗式驗證」（adversarial verification）——讓獨立 agent 互相挑錯，確認輸出可信後才回覆你。 並行上限是 16 個同時執行，但單一 workflow 最多可協調 **1,000 個子代理**。 進度會即時儲存，任務中斷後可從斷點繼續，不需重跑。 [abmedia](https://abmedia.io/claude-code-dynamic-workflows-opus-4-8-1000-subagents-parallel-2026)

## 六種 Orchestration Pattern

| Pattern | 說明 |
|---|---|
| **Classify-and-act** | 先分類任務再分派執行，適合混合型 codebase |
| **Fan-out-and-synthesize** | 大量平行執行後整合結果 |
| **Adversarial verification** | 多個 agent 互相攻防驗證，提高可信度 |
| **Generate-and-filter** | 大量生成後篩選最佳解 |
| **Tournament** | 多個解法競爭淘汰 |
| **Loop until done** | 持續迭代直到條件收斂 |

 [ihower](https://ihower.tw/notes/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98-AI/Claude+Code+Dynamic+Workflows)

## 適合的使用場景

以下場景最能發揮 Dynamic Workflows 的價值： [juejin](https://juejin.cn/post/7646636470158966826)

- **Codebase 全域掃描**：安全審計、dead code 偵測、auth 檢查、input validation 漏洞掃描
- **大規模遷移與重構**：跨數千個檔案的 API 升級、framework 置換、語言 port（例如 Bun 從 Zig 移植到 Rust，75 萬行、11 天完成）
- **深度研究與多角度壓力測試**：在提交重大決策前，讓多個 agent 從不同角度挑戰方案
- **超過 1,000 筆資料的排序與分析**
- **LLM 評估（LLM-as-a-judge）**：平行跑大量測試案例

## 什麼時候「不」適合用

官方建議至少符合以下三個條件再考慮使用：有很多**獨立 sub-tasks**、需要 review chain、接受**高 token 成本**（比一般 session 高 10–50 倍）。 日常小任務硬套只會更貴、更慢。 [shareuhack](https://www.shareuhack.com/zh-TW/posts/claude-code-dynamic-workflows-guide-2026)

## 如何啟動

- 在 prompt 中使用 **「workflow」** 這個字
- 開啟 **`ultracode`** 設定觸發
- 使用 **`/effort`** 或 **`/deep-research`** 指令 [shareuhack](https://www.shareuhack.com/zh-TW/posts/claude-code-dynamic-workflows-guide-2026)
- Max、Team、Enterprise 方案預設開啟；Pro 方案需在 `/config` 手動啟用 [claude](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

對你在 MediaTek 的工作來說，Dynamic Workflows 非常適合用在跨服務的 **codebase 安全審計**、**大規模 API 遷移**，或是拿來做 **LLM evaluation pipeline**（批量跑 judge）這類任務，能大幅取代原本需要手動設計 orchestration 的工作。 [ihower](https://ihower.tw/notes/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98-AI/Claude+Code+Dynamic+Workflows)
