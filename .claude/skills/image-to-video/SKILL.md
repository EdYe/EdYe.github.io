---
name: image-to-video
description: 把一張視覺筆記圖片轉成旁白影片（YouTube 16:9 + Shorts 9:16），使用者自錄聲音、全免費工具。Use when the user wants to turn a note image into a video, or re-render a video after recording voice.
user-invocable: true
argument-hint: "<圖片路徑或 slug> [--rerender]"
---

# /image-to-video - 視覺筆記轉影片

## 使用方式
```
/image-to-video raw-notes/你目前的工作有未來嗎.png     # 新影片：產生旁白稿 + 暫用配音版影片
/image-to-video job-future-video --rerender             # 使用者錄完音後重新合成
```

渲染器是 `scripts/make-video.py`（只依賴 ffmpeg；暫用配音需 edge-tts）。範例專案：`~/Movies/job-future-video/`。

## 前提
- 發布平台：YouTube、Shorts、LinkedIn。
- 正式配音是使用者自己的聲音。edge-tts 只用來產生暫用配音，方便預覽和抓時間長度。
- 不使用付費服務。
- 影片和音檔放在 `~/Movies/<slug>/`，**絕不放進 repo**（本 repo 會自動 push 到 GitHub Pages）。
- 不動 `_notes/`。

## 新影片流程

1. **準備**
   - 檢查是否已安裝 edge-tts：`which edge-tts`。沒有的話建一個 venv 安裝，或請使用者執行 `pip3 install edge-tts`，再透過 `EDGE_TTS=<路徑>` 傳給腳本。
   - slug 用英文小寫加連字號，例如 `job-future-video`。
   - 執行 `mkdir -p ~/Movies/<slug>`，再把圖片複製成 `~/Movies/<slug>/source.png`。一定要用 ASCII 檔名，因為 ffmpeg 的 subtitles 路徑無法處理中文。
   - 用 `sips -g pixelWidth -g pixelHeight` 讀取圖片尺寸。
2. **讀圖並切分區塊**
   - 用 Read 看圖，找出標題、核心摘要、各編號章節、結尾（例如法則或口訣）的區塊。
   - 以 `[x, y, w, h]` 記錄每個區塊的座標。
   - 驗證座標：先用 `ffmpeg crop` 把每個區塊切出來，再用 `xstack` 拼成一張對照圖並 Read 檢查。文字不能被切斷；有切斷就調整座標再檢查一次。
   - 驗證用的圖檔放在 scratchpad，完成後刪除。
3. **寫 `video.json`**（格式見範例專案）
   - `title`、`image`、`voice`：預設 `zh-TW-HsiaoChenNeural`。
   - `regions`：區塊名稱對應座標。
   - `versions.youtube`：`size [1920,1080]`，每段旁白 70–170 字，總長約 2.5–3 分鐘，總字數約 900 字。
     - 結構：開場提問 → 核心摘要 → 各章節 → 結尾法則 → 呼籲訂閱。
   - `versions.shorts`：`size [1080,1920]`，**60 秒以內**，約 200 字，挑 4–5 個最有衝擊力的區塊。第一句必須是鉤子。
   - 旁白規則：
     - 內容只能來自圖片，不加入圖片沒有的論點。
     - 使用繁體中文口語。
     - 用。！？；斷句，字幕會依照這些標點切卡。
     - 英文縮寫用頓號分開（例如「R、T、O」），TTS 才會逐字母念。
4. **渲染**：`python3 scripts/make-video.py ~/Movies/<slug>`。要只跑單一版本，就在後面加上版本名稱，例如 `shorts`。
5. **驗證**（只看靜態畫格，不能只憑感覺判斷）
   - 每個版本抽 4 個時間點的畫格，用 `hstack`／`xstack` 拼起來後 Read。檢查四件事：
     - 中文字沒有變成方塊；
     - 區塊內容可讀；
     - 字幕沒有壓到圖片；
     - Shorts 的字幕位置高於底部約 400px 的平台 UI 區。
   - 檢查有沒有音軌：`ffmpeg -i out/x.mp4 2>&1 | grep -E "Duration|Audio"`。
   - 檢查響度：`ffmpeg -i out/x.mp4 -af ebur128 -f null - 2>&1 | grep "I:"`，目標是約 -16 LUFS。
6. **回報**
   - 兩個輸出檔的路徑、長度，以及各自要發布到哪個平台。
   - 錄音稿在 `~/Movies/<slug>/RECORDING.md`。說明錄好的檔案要存成 `voice/<版本>/<段號>.m4a`，可以用 QuickTime 或語音備忘錄錄。
   - 提醒使用者完整看一次影片，因為鏡頭移動是否順暢，從靜態畫格看不出來。

## --rerender 流程
1. 列出 `~/Movies/<slug>/voice/` 底下已有的錄音，以及哪些段落還在用暫用配音。
2. 執行 `python3 scripts/make-video.py ~/Movies/<slug>`。
3. 依第 5 步驗證；回報兩版的新長度，並說明哪些段落仍是暫用配音（見重新產生的 `RECORDING.md`）。

## 腳本行為備忘
- 有錄音就優先使用錄音，自動去除頭尾靜音並降噪。所有音檔都會用 loudnorm 統一到 -16 LUFS。
- 暫用配音的快取檔以旁白文字的雜湊值命名，所以修改 `video.json` 的文字後會自動重新產生。
- 字幕依標點切成字幕卡，播放時間依字數比例分配。
- 橫式畫面：區塊在模糊背景上做 zoompan 推移；動畫前先放大 4 倍，避免畫面抖動。
- 直式畫面：寬的區塊先放大到可讀高度（最多 2.6 倍），再左右平移。
- 背景音樂（可選）：放一個 `bgm.mp3` 在專案資料夾，會自動以低音量混入。
- 若修改了 `scripts/make-video.py`，要 commit 並 push；影片和音檔不要 commit。
