# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案說明

Jekyll + GitHub Pages 的視覺筆記圖片展示網站，部署於 `https://EdYe.github.io`。每張圖片對應 `_notes/` 底下一個含 Front Matter 的 `.md` 說明文件，支援標籤分類（6 類）與 Fuse.js 模糊搜尋。

## 重要指令

```bash
# 重建 Fuse.js 搜尋索引（每次新增或修改 _notes/ 後執行）
node scripts/rebuild-index.js

# 批次處理 raw-notes/ 底下所有未處理的檔案
./scripts/batch-convert.sh

# 本地預覽（需安裝 github-pages gem）
bundle exec jekyll serve
```

## Git

每次操作：stage 所有變更 → commit → push。無需確認，直接執行。

## Skills

`/add-note` 技能定義在 `.claude/skills/add-note/add-note.md`，負責單張筆記的完整新增流程（預檢→生成 Front Matter→複製圖片→更新搜尋索引→部署）。其他自訂技能查 `.claude/skills/` 目錄。

---

## 原始說明文件格式規範

每個 `raw-notes/*.md` 固定包含：

- `核心摘要`：一段話總結 → description（截斷至 80 字）
- `詳細重點整理`：數個編號章節 → 章節標題做為 tags 來源
- `結論與行動建議`：含 💡金句 + 🎯行動建議

### 自動判斷分類邏輯

| 內文關鍵字 | category |
|---|---|
| `[MM:SS]` 時間戳格式 | 影片筆記 |
| 閱讀、書摘、作者 | 閱讀筆記 |
| AI、Agent、LLM、模型 | AI筆記 |
| 習慣、生產力、時間管理 | 生產力 |
| 大腦、心理、行為、認知 | 心理學 |
| 其他 | 學習筆記 |

### Tags 提取規則

- 優先取「詳細重點整理」各節的核心名詞（每節 1 個）
- 補充核心摘要中的關鍵概念
- 共 3-5 個繁體中文關鍵字

### Front Matter 輸出格式

```yaml
---
title: '從核心摘要第一句提取主題（不超過25字）'
date: YYYY-MM-DD
image: /images/<category>/<英文檔名>.<副檔名>
category: <影片筆記|閱讀筆記|AI筆記|生產力|心理學|學習筆記>
tags: [3到5個繁中關鍵字]
description: '核心摘要前80字'
quote: '💡啟發性金句內容（若無則省略此行）'
action: '🎯行動建議一句話摘要（若無則省略此行）'
source_has_timestamps: true 或 false
---
（保留原始說明文件的完整正文，不修改）
```

注意：
- 英文檔名使用小寫 + 連字號，例如：`ai-devx-strategy`
- 無法確定的欄位標記為 `TODO`，不猜測
- 圖片副檔名依實際存在的為準（依序檢查 .jpeg → .jpg → .png → .webp）

---

## 禁止行為

- 不得直接修改 `_notes/` 已存在且無 TODO 的檔案
- 不得刪除任何圖片
- 不得更改 `index.html` 的 Fuse.js 搜尋邏輯，除非明確指示
