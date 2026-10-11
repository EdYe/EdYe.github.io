# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案說明

Jekyll + GitHub Pages 的視覺筆記圖片展示網站，部署於 `https://EdYe.github.io`。每張圖片對應 `_notes/` 底下一個含 Front Matter 的 `.md` 說明文件，支援標籤分類（6 類）與 Fuse.js 模糊搜尋。

## 重要指令

```bash
# 重建 Fuse.js 搜尋索引（每次新增或修改 _notes/ 後執行）
node scripts/rebuild-index.js

# 批次處理 raw-notes/ 底下所有未處理的檔案（--force 重新處理已處理過的）
./scripts/batch-convert.sh

# 本地預覽（需安裝 github-pages gem）
bundle exec jekyll serve
```

沒有測試或 lint；驗證方式是執行 `rebuild-index.js` 確認筆數與分類統計正確。

## 架構

- **首頁是純前端渲染**：`index.html` 不使用 Liquid 迴圈，而是 `fetch('/search-index.json')` 後用 JS 產生卡片、標籤雲、分類篩選與 Fuse.js 搜尋。因此 `search-index.json`（已 commit）是首頁唯一資料來源，沒重建索引的筆記不會出現在 Gallery。
- **筆記頁由 Jekyll 產生**：`_notes/` 是 collection，輸出到 `/notes/:name`，套用 `_layouts/note.html`（`_config.yml` 設了預設 layout 與 `future: true`）。
- **`rebuild-index.js` 自帶簡易 Front Matter 解析器**，只認單行 `key: value` 與 `[a, b]` 陣列，不支援多行 YAML。Front Matter 的值必須寫在同一行。
- **`batch-convert.sh` 會把本檔當成 prompt 使用**：它對每個 raw note 執行 `claude -p "請讀取 CLAUDE.md 的格式規範…"`，所以修改下方格式規範會直接影響批次輸出。這個腳本會另外寫入 `source_raw: <原始檔名>` 欄位，用來判斷是否已處理過；完成後也會自動重建索引並 `git add . && commit && push`。腳本只檢查 `.jpeg/.jpg/.png` 圖片，不包含 `.webp`。
- `raw-notes/` 的內容已加入 gitignore，並在 `_config.yml` 排除，不會部署，只是本機輸入區。圖片放在 `images/<category>/<slug>.<ext>`。

## Git

每次操作：stage 所有變更 → commit → push。無需確認，直接執行。

## Skills

`/add-note` 技能定義在 `.claude/skills/add-note/SKILL.md`，負責單張筆記的完整新增流程（預檢→生成 Front Matter→複製圖片→更新搜尋索引→部署）。其他自訂技能查 `.claude/skills/` 目錄。

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
（保留原始說明文件的完整正文；唯一允許的修改是簡體字轉繁體）
```

注意：
- 英文檔名使用小寫 + 連字號，例如：`ai-devx-strategy`
- 無法確定的欄位標記為 `TODO`，不猜測
- 圖片副檔名依實際存在的為準（依序檢查 .jpeg → .jpg → .png → .webp）

---

## 禁止行為

- 不得直接修改 `_notes/` 已存在且無 TODO 的檔案（例外：簡體字轉繁體，見下方「正文繁體化規則」）
- 不得刪除任何圖片
- 不得更改 `index.html` 的 Fuse.js 搜尋邏輯，除非明確指示

---

## 正文繁體化規則

全站正文一律使用繁體中文。寫入 `_notes/` 前必須將正文中的簡體字逐字轉為繁體。

**允許**：簡體字 → 對應繁體字的逐字轉換（如 `问题陈述` → `問題陳述`、`专业声誉` → `專業聲譽`）。

**禁止**：
- 改寫用詞（如 `模块` → `模組`、`软件` → `軟體`）—— 只做字形轉換，不做詞彙替換
- 異體字正規化（如 `平台` → `平臺`、`了解` → `瞭解`、`解雇` → `解僱`、`啓發` → `啟發`）
- 任何其他正文改動

**不要使用 OpenCC / `opencc-js` 的 `cn→tw` 或 `s2twp` 做全文轉換**：它會把既有繁體字誤判為簡體，造成 `面對` → `麵對`、`只是` → `隻是` 這類錯誤。

**檢查方式**（Big5 無法編碼的漢字即為簡體字候選）：

```bash
python3 - <<'EOF'
import glob
for p in sorted(glob.glob('_notes/*.md')+glob.glob('raw-notes/*.md')):
    for c in set(open(p,encoding='utf-8').read()):
        if '\u4e00'<=c<='\u9fff':
            try: c.encode('big5')
            except UnicodeEncodeError: print(p,c)
EOF
```

已知誤報（為合法繁體字，不要轉換）：`肽`、`酶`、`啓`。
