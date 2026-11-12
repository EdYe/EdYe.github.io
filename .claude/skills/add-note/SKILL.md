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
   - raw-notes/<檔名>.md（說明文件）
   - 依序檢查圖片副檔名：.jpeg → .jpg → .png → .webp
   - 若找不到任何圖片，回報錯誤並停止

2. **讀取說明文件**
   - 完整讀取 raw-notes/<檔名>.md 的內容

3. **依照 CLAUDE.md 格式規範生成 Front Matter**
   - 欄位與提取規則（description、tags、category、quote、action、source_has_timestamps）一律依 CLAUDE.md「原始說明文件格式規範」

4. **建立 _notes/<英文檔名>.md**
   - 英文檔名使用小寫+連字號（從標題語意轉換）
   - 包含完整 Front Matter + 原始說明文件正文
   - **簡體字檢查**：寫入前掃描正文，將簡體字逐字轉為繁體。規則與檢查指令見 CLAUDE.md「正文繁體化規則」
     - 只做字形轉換，不改寫用詞、不做異體字正規化
     - 不得使用 OpenCC `cn→tw` 全文轉換（會誤傷既有繁體字）
     - 若有轉換，在步驟 8 回報中列出轉換的字

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
   網址：https://EdYe.github.io/notes/<英文檔名>
   約 60 秒後上線。
   ```

## 錯誤處理
- 若 git 認證失敗（push 被拒絕、OAuth 過期），暫停並提示使用者執行 `! git push` 手動修復，修復後從中斷處繼續
- 若筆記處理失敗（檔案缺失、格式錯誤），停止並回報原因

## 其他注意事項
- 若英文檔名已存在於 _notes/，詢問是否覆蓋
- 無法確定的欄位標記為 TODO，不要猜測
