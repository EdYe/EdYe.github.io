# /add-note - 新增單張視覺筆記

## 使用方式
```
/add-note <檔名（不含副檔名）>
```

範例：
```
/add-note IMG_9274
```

## 執行步驟

1. **確認來源檔案存在**
   - raw-notes/<檔名>.md（說明文件）
   - raw-notes/<檔名>.jpeg / .jpg / .png（圖片）

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

5. **複製圖片**
   - 建立 images/<category>/ 目錄（若不存在）
   - 複製圖片到 images/<category>/<英文檔名>.<副檔名>

6. **更新搜尋索引**
   - 執行：node scripts/rebuild-index.js

7. **Git 部署**
   - git add .
   - git commit -m "新增筆記：<title>"
   - git push

8. **回報結果**
   ```
   ✅ 新增完成！
   標題：<title>
   分類：<category>
   標籤：<tags>
   網址：https://你的帳號.github.io/notes/<英文檔名>
   約 60 秒後上線。
   ```

## 注意事項
- 若英文檔名已存在於 _notes/，詢問是否覆蓋
- 無法確定的欄位標記為 TODO，不要猜測
