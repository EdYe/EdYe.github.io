# 視覺筆記 Gallery 專案規範

## Workflows

When processing raw notes with /add-note, always check the raw-notes directory for all unprocessed files, copy associated images (check for both .jpg and .jpeg extensions), rebuild the search index, and push to git upon completion.

### /add-note 指令行為
- **預檢**：執行前先驗證 git 認證（`git status`）和圖片檔案存在（依序 .jpeg/.jpg/.png/.webp）
- **--dry-run**：加上此參數時只預覽，不做任何實際變更
- **錯誤恢復**：單篇失敗時跳過並繼續；認證失敗時暫停等待使用者修復後繼續
- **批次摘要**：處理結束後顯示已處理/已跳過/失敗的摘要表格

## Git

For git operations: always stage all changes, commit with a descriptive message, and push to origin/main unless told otherwise. Do not ask for confirmation on routine commit-and-push requests.

## Skills & Commands

When working with custom skills/slash commands, look for skill definitions in `.claude/skills/` directory. If a skill is not found, check the directory structure before reporting an error.

---

## 專案說明
這是一個 Jekyll + GitHub Pages 的視覺筆記圖片展示網站。
每張圖片對應一個 _notes/ 底下的 .md 說明文件，支援標籤分類與 Fuse.js 模糊搜尋。

---

## 目錄結構
```
專案根目錄/
├── raw-notes/          # 原始輸入：圖片 + 說明 .md（同檔名）
├── _notes/             # Jekyll 筆記（含 Front Matter）
├── images/<category>/  # 依分類存放的圖片
├── _layouts/           # Jekyll 模板
├── search-index.json   # Fuse.js 搜尋索引（自動產生）
├── index.html          # Gallery 首頁
├── _config.yml         # Jekyll 設定
└── scripts/            # 工具腳本
```

---

## 原始說明文件格式規範

每個 raw-notes/*.md 固定包含以下區塊：

### 必要區塊
- `核心摘要`：一段話總結 → 做為 description（截斷至 80 字）
- `詳細重點整理`：數個編號章節 → 章節標題做為 tags 來源
- `結論與行動建議`：含 💡金句 + 🎯行動建議

### 自動判斷分類邏輯
- 內文含 [MM:SS] 時間戳格式 → category: 影片筆記
- 內文含「閱讀」「書摘」「作者」 → category: 閱讀筆記
- 內文含「AI」「Agent」「LLM」「模型」 → category: AI筆記
- 內文含「習慣」「生產力」「時間管理」 → category: 生產力
- 內文含「大腦」「心理」「行為」「認知」 → category: 心理學
- 其他 → category: 學習筆記

### Tags 提取規則
- 優先取「詳細重點整理」各節的核心名詞（每節取 1 個）
- 補充從核心摘要中提取的關鍵概念
- 共 3-5 個繁體中文關鍵字

### Front Matter 輸出格式
```yaml
---
title: '從核心摘要第一句提取主題（不超過25字）'
date: YYYY-MM-DD
image: /images/<category>/<英文檔名>.jpeg
category: <影片筆記|閱讀筆記|AI筆記|生產力|心理學|學習筆記>
tags: [3到5個繁中關鍵字]
description: '核心摘要前80字'
quote: '💡啟發性金句內容（若無則省略此行）'
action: '🎯行動建議一句話摘要（若無則省略此行）'
source_has_timestamps: true 或 false
---
（保留原始說明文件的完整正文，不修改）
```

### 注意事項
- 若某欄位無法從內文確定，標記為 'TODO' 而非猜測
- 英文檔名使用小寫 + 連字號，例如：ai-devx-strategy
- 禁止修改原始說明文件的正文內容

---

## 標準新增流程（每次新增圖片時執行）

1. 確認 raw-notes/ 底下有 <檔名>.jpeg 和 <檔名>.md
2. 讀取 .md，依上方規範生成 Front Matter
3. 將完整 .md（Front Matter + 正文）存到 _notes/<英文檔名>.md
4. 依偵測到的 category 複製圖片到 images/<category>/<英文檔名>.jpeg
5. 執行 node scripts/rebuild-index.js 更新搜尋索引
6. 執行 git add . && git commit -m "新增筆記：<title>" && git push
7. 回報：「✅ 已上線：https://<帳號>.github.io/notes/<英文檔名>」

---

## 批次處理現有檔案

若需要一次處理 raw-notes/ 底下所有未處理的檔案，執行：
```bash
./scripts/batch-convert.sh
```

---

## 禁止行為
- 不得直接修改 _notes/ 已存在且無 TODO 的檔案
- 不得刪除任何圖片
- 不得更改 index.html 的 Fuse.js 搜尋邏輯，除非明確指示
