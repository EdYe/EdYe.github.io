#!/bin/bash
# batch-convert.sh (修正版)
# 使用方式：./scripts/batch-convert.sh [--force]

# Bug 修正：移除 set -e，改為迴圈內明確錯誤處理，避免意外中止整個批次

RAW_DIR="raw-notes"
NOTES_DIR="_notes"
IMAGES_DIR="images"
TODAY=$(date +%Y-%m-%d)
SUCCESS=0
SKIP=0
FAIL=0

echo "======================================"
echo "  視覺筆記批次轉換工具"
echo "  開始時間：$(date '+%Y-%m-%d %H:%M:%S')"
echo "======================================"

if [ ! -d "$RAW_DIR" ]; then
  echo "❌ 找不到 $RAW_DIR 目錄"
  exit 1
fi

mkdir -p "$NOTES_DIR"

for md_file in "$RAW_DIR"/*.md; do
  [ -f "$md_file" ] || continue

  base=$(basename "$md_file" .md)

  # 尋找對應圖片（支援 .jpeg / .jpg / .png）
  img_file=""
  img_ext=""
  for ext in jpeg jpg png; do
    if [ -f "$RAW_DIR/${base}.${ext}" ]; then
      img_file="$RAW_DIR/${base}.${ext}"
      img_ext="$ext"
      break
    fi
  done

  if [ -z "$img_file" ]; then
    echo "⚠️  跳過（找不到對應圖片）：$base"
    SKIP=$((SKIP + 1))
    continue
  fi

  # 檢查是否已處理過（以 source_raw 欄位比對英文檔名）
  if [ "$1" != "--force" ] && grep -rl "source_raw: ${base}$" "$NOTES_DIR/" 2>/dev/null | grep -q .; then
    echo "⏭️  已處理，略過：$base（加 --force 可強制重新處理）"
    SKIP=$((SKIP + 1))
    continue
  fi

  echo ""
  echo "🔄 處理中：$base"

  # ── 修正重點：用 temp file 建立 prompt，避免引號衝突 ──
  TMPFILE=$(mktemp -t claude_prompt)
  STDERR_TMP=$(mktemp -t claude_stderr)
  trap 'rm -f "$TMPFILE" "$STDERR_TMP"' EXIT

  {
    printf "請讀取 CLAUDE.md 的格式規範，然後處理以下說明文件。\n\n"
    printf "今天日期：%s\n" "$TODAY"
    printf "原始檔名（不含副檔名）：%s\n\n" "$base"
    printf "說明文件內容：\n"
    printf "=====開始=====\n"
    cat "$md_file"
    printf "\n=====結束=====\n\n"
    printf "請輸出完整的 Jekyll .md 檔案內容（只輸出檔案內容本身，不要任何前言或解釋）：\n"
    printf "1. Front Matter（依照 CLAUDE.md 規範，包含 title/date/image/category/tags/description，以及 quote/action/source_has_timestamps，並加入 source_raw: %s）\n" "$base"
    printf "2. 空一行\n"
    printf "3. 原始說明文件完整正文（不修改任何文字）\n"
  } > "$TMPFILE"

  # 傳入 temp file 內容給 claude（stderr 分開捕捉，避免污染輸出）
  OUTPUT=$(claude -p "$(cat "$TMPFILE")" 2>"$STDERR_TMP")
  EXIT_CODE=$?
  rm -f "$TMPFILE"

  if [ $EXIT_CODE -ne 0 ]; then
    echo "❌ 處理失敗：$base"
    cat "$STDERR_TMP"
    rm -f "$STDERR_TMP"
    trap - EXIT
    FAIL=$((FAIL + 1))
    continue
  fi
  rm -f "$STDERR_TMP"
  trap - EXIT

  # 從輸出提取 category
  CATEGORY=$(echo "$OUTPUT" | grep '^category:' | head -1 \
    | sed "s/category: *//;s/'//g;s/\"//g" | tr -d '\r\n ')

  if [ -z "$CATEGORY" ]; then
    CATEGORY="學習筆記"
  fi

  # Bug 修正：從 Claude 輸出的 image 欄位提取英文檔名，確保圖片路徑一致
  IMG_FIELD=$(printf '%s\n' "$OUTPUT" | grep '^image:' | head -1 \
    | sed "s|image: *||;s|'||g;s|\"||g" | tr -d '\r\n ')
  ENG_BASE=$(basename "$IMG_FIELD" | sed 's/\.[^.]*$//')

  if [ -z "$ENG_BASE" ]; then
    echo "⚠️  無法從輸出提取英文檔名，使用原始檔名：$base"
    ENG_BASE="$base"
  fi

  # 建立圖片目錄並複製（使用英文檔名）
  mkdir -p "$IMAGES_DIR/$CATEGORY"
  cp "$img_file" "$IMAGES_DIR/$CATEGORY/${ENG_BASE}.${img_ext}"

  # 儲存處理好的 .md（Bug 修正：使用 printf 避免 echo 解讀反斜線；使用英文檔名）
  printf '%s\n' "$OUTPUT" > "$NOTES_DIR/${ENG_BASE}.md"

  echo "✅ 完成：$base → _notes/${ENG_BASE}.md, images/$CATEGORY/${ENG_BASE}.${img_ext}"
  SUCCESS=$((SUCCESS + 1))
done

echo ""
echo "======================================"
echo "  批次轉換完成"
echo "  ✅ 成功：$SUCCESS 個"
echo "  ⏭️  略過：$SKIP 個"
echo "  ❌ 失敗：$FAIL 個"
echo "======================================"

if [ $SUCCESS -gt 0 ]; then
  echo ""
  echo "🔄 重建搜尋索引..."
  node scripts/rebuild-index.js && echo "✅ 搜尋索引已更新"

  echo ""
  echo "🚀 部署到 GitHub Pages..."
  git add .
  git commit -m "批次新增 $SUCCESS 筆視覺筆記 ($TODAY)"
  git push
  echo "✅ 部署完成！約 60 秒後網站生效。"
fi
