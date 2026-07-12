---
name: add-note
description: 新增單張視覺筆記到 Gallery 網站
user-invocable: true
argument-hint: "<檔名（不含副檔名）> [--dry-run]"
context: fork
agent: general-purpose
---

# /add-note - 新增單張視覺筆記

## 使用方式
```
/add-note <檔名（不含副檔名）> [--dry-run]
```

範例：
```
/add-note IMG_9274
/add-note IMG_9274 --dry-run
```

## --dry-run 模式

加上 `--dry-run` 時，只顯示會被處理的內容，不做任何實際變更：
- 列出來源檔案（.md 和圖片）
- 顯示將產生的 Front Matter 預覽
- 顯示目標路徑（_notes/ 和 images/）
- 不建立檔案、不複製圖片、不執行 git 操作

## 執行步驟

1. **預檢驗證（Pre-flight）**
   - 執行 `git status` 確認 git 認證正常，若失敗則提示使用者修復後再繼續
   - raw-notes/<檔名>.md（說明文件）
   - 依序檢查圖片副檔名：.jpeg → .jpg → .png → .webp
   - 若找不到任何圖片，記錄錯誤並跳過此筆記（批次模式時繼續處理下一篇）

2. **讀取說明文件**
   - 完整讀取 raw-notes/<檔名>.md 的內容

3. **依照 CLAUDE.md 格式規範生成 Front Matter**
   - 從「核心摘要」提取 description（截斷至 80 字）
   - 從「詳細重點整理」章節標題提取 tags（3-5個）
   - 依自動判斷邏輯決定 category
   - 從「💡啟發性金句」提取 quote（若有）
   - 從「🎯具體行動建議」提取 action 一句摘要（若有）
   - 判斷是否含 [MM:SS] 時間戳 → source_has_timestamps

4. **建立 _notes/<英文檔名>.md**
   - 英文檔名使用小寫+連字號（從標題語意轉換）
   - 包含完整 Front Matter + 原始說明文件正文

5. **驗證並複製圖片**
   - 確認 raw-notes/ 中圖片的實際副檔名（依序檢查 .jpeg、.jpg、.png、.webp）
   - 使用磁碟上實際存在的副檔名，而非假設
   - 將 Front Matter 中的 image 路徑設為實際存在的副檔名
   - 建立 images/<category>/ 目錄（若不存在）
   - 複製圖片到 images/<category>/<英文檔名>.<實際副檔名>

6. **更新搜尋索引**
   - 執行：node scripts/rebuild-index.js

7. **Git 部署**
   - git add .
   - git commit -m "新增筆記：<title>"
   - git push（若 push 失敗，提示使用者檢查認證狀態，不要自動重試）

8. **回報結果**
   ```
   ✅ 新增完成！
   標題：<title>
   分類：<category>
   標籤：<tags>
   網址：https://你的帳號.github.io/notes/<英文檔名>
   約 60 秒後上線。
   ```

## 錯誤處理
- 若 git 認證失敗（push 被拒絕、OAuth 過期），暫停並提示使用者執行 `! git push` 手動修復，修復後從中斷處繼續
- 若單篇筆記處理失敗（檔案缺失、格式錯誤），跳過該筆記並記錄原因，繼續處理其餘筆記
- 批次處理結束後，顯示摘要表格：已處理 / 已跳過 / 失敗，含各筆記的錯誤原因

## 其他注意事項
- 若英文檔名已存在於 _notes/，詢問是否覆蓋
- 無法確定的欄位標記為 TODO，不要猜測
