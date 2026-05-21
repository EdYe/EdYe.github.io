圖片尚未存在，image 欄位標記為 TODO。以下是完整的 Jekyll .md 檔案內容：

```markdown
---
title: 'Claude 思考槓桿：自適應推理的成本效益控制'
date: 2026-05-21
image: TODO
category: AI筆記
tags: [思考槓桿, 努力等級, 自適應思考, 成本效益, 任務分層]
description: '此影片為 Anthropic 於 2026 年 5 月 6 日舉辦的開發者大會「Code w/ Claude 2026」的技術場次，由 Anthropic 的'
quote: '思考不是越多越好，而是恰到好處才是智慧。'
action: '依任務複雜度對應 effort 等級（E-M-H 分層法則），以最低可接受等級控制成本。'
source_has_timestamps: true
source_raw: The Thinking Lever
---

# 🎬 The Thinking Lever — Code w/ Claude 2026 重點筆記

## [核心摘要]

此影片為 Anthropic 於 2026 年 5 月 6 日舉辦的開發者大會「Code w/ Claude 2026」的技術場次 ，由 Anthropic 的 Matt Bleifer 主講 。核心主題是：Claude 的**自適應思考（Adaptive Thinking）**機制讓開發者擁有一個全新的決策槓桿——控制 Claude 「要思考多深」，並在成本、延遲與回答品質三者之間取得最佳平衡 。 [claude](https://claude.com/code-with-claude/session/sf-the-thinking-lever)

***

## [詳細重點整理]

### 1. 核心問題的提出 [00:00]

過去，開發者對 Claude 的推理深度幾乎沒有控制權。現在，透過**思考預算（Thinking Budget）**與**努力等級（Effort Level）**，開發者可以精確決定「這個任務值得 Claude 花多少算力去思考」 。 [claude](https://claude.com/code-with-claude/session/sf-the-thinking-lever)

**關鍵概念：思考槓桿（The Thinking Lever）** — 一個在品質與效率之間動態調撥資源的控制機制 [youtube](https://www.youtube.com/watch?v=5CjdS_9xI9E)

***

### 2. Effort Level 五個等級介紹 [約 05:00]

Claude 目前提供五個努力等級，由低到高分別為 `low`、`medium`、`high`、`xhigh`、`max` 。 [moksaweb](https://moksaweb.com/claude-code-effort-level/)

| 等級 | 適用場景 | 特性 |
|------|----------|------|
| `low` | 簡單任務、子代理（subagent） | 最省 Token、速度快  [x](https://x.com/PawelHuryn/status/2043236719953129793) |
| `medium` | 速度與性能的平衡點 | Claude Code 自 3 月 6 日起的預設值  [x](https://x.com/PawelHuryn/status/2043236719953129793) |
| `high` | 複雜推理、代理任務 | 標準 API 預設行為  [x](https://x.com/PawelHuryn/status/2043236719953129793) |
| `xhigh` | 深度分析任務 | 高成本、高品質  [buildthisnow](https://www.buildthisnow.com/blog/models/claude-opus-4-7) |
| `max` | 最頂尖任務（如 ARC AGI 2 測試） | 無限制，最深推理，Opus 4.6+ 限定  [anthropic](https://www.anthropic.com/news/claude-opus-4-6) |

**關鍵概念：努力分層（Effort Tiering）** — 非連續的離散控制點，取代過去需要手動設定 token 數的方式 [buildthisnow](https://www.buildthisnow.com/blog/models/claude-opus-4-7)

***

### 3. 從手動 Token 預算到自適應思考 [約 10:00]

舊有的 `thinking: {type: "enabled", budget_tokens: N}` 寫法在新版（Opus 4.7 起）已被移除，取而代之的是**自適應思考（Adaptive Thinking）** 。Claude 不再被動消耗固定 token，而是根據任務複雜度動態決定實際思考量 。 [x](https://x.com/PawelHuryn/status/2043236719953129793)

**關鍵概念：自適應思考（Adaptive Thinking）** — Claude 以 effort 等級為指引，自行決定最佳推理深度，而非固定預算上限 [x](https://x.com/PawelHuryn/status/2043236719953129793)

***

### 4. 成本、延遲、品質的三角取捨 [約 15:00]

研究數據顯示，`low` 到 `max` 等級之間，token 消耗成本差距高達 **2.7 倍** 。開發者需依據任務性質在三個維度做取捨： [pub.towardsai](https://pub.towardsai.net/i-tested-all-5-effort-levels-of-claude-opus-4-7-2f335c626786)

- **成本敏感型**（大量並發子代理）：使用 `low` 或 `medium`
- **品質優先型**（複雜程式碼審查、推理鏈）：使用 `high` 至 `max`
- **延遲敏感型**（即時互動場景）：避免 `xhigh`/`max`，選用 `medium` [docs.litellm](https://docs.litellm.ai/docs/providers/anthropic_effort)

**關鍵概念：效益邊際遞減（Diminishing Returns on Effort）** — 超過特定等級後，品質提升幅度趨緩但成本持續攀升 [pub.towardsai](https://pub.towardsai.net/i-tested-all-5-effort-levels-of-claude-opus-4-7-2f335c626786)

***

### 5. Claude Code 實務操作 [約 18:00]

在 Claude Code 中，可透過指令 `/effort` 或修改 `settings.json` 即時切換努力等級 。API 調用則使用 `effort` 參數，可不依賴 extended thinking 單獨使用 。 [platform.claude](https://platform.claude.com/docs/en/build-with-claude/effort)

**關鍵概念：任務分層策略（Task-Level Effort Routing）** — 根據任務類型動態路由至不同 effort 等級，降低整體運算成本 [moksaweb](https://moksaweb.com/claude-code-effort-level/)

***

## [結論與行動建議]

**啟發金句：**
> 「思考不是越多越好，而是恰到好處才是智慧。」

**具體行動建議 — E-M-H 分層法則：**
- **E**valuate（評估）：先判斷任務是否需要深度推理
- **M**atch（匹配）：將任務難度對應至適當的 effort 等級
- **H**arvest（收割）：在品質達標的前提下，選最低可接受等級以控制成本

**生活實踐建議：**
- **多代理架構**：主代理用 `high`，協作子代理用 `low`/`medium`，可大幅降低整體 Token 支出
- **CI/CD 流程**：自動化測試用 `low`，程式碼 review 用 `high`，安全審計用 `max`
- **Claude Code 日常開發**：維持預設 `medium`，遇到卡關的複雜問題再手動升至 `high`

***

## [參考連結]

- 🎥 原始影片：https://youtu.be/T7KqH7kYnE4
- 📄 官方 Session 頁面：https://claude.com/code-with-claude/session/sf-the-thinking-lever [claude](https://claude.com/code-with-claude/session/sf-the-thinking-lever)
- 📖 Effort API 文件：https://platform.claude.com/docs/en/build-with-claude/effort [platform.claude](https://platform.claude.com/docs/en/build-with-claude/effort)
```

image 欄位標記為 `TODO`，因為 `images/AI筆記/the-thinking-lever.*` 尚無任何圖片存在，請補上圖片後再改為正確路徑（格式：`/images/AI筆記/the-thinking-lever.jpeg`）。
