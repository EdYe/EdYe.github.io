#!/usr/bin/env python3
"""把一張視覺筆記圖片轉成旁白影片（YouTube 16:9 + Shorts 9:16）。

用法：
  python3 scripts/make-video.py <專案資料夾> [版本名稱...]

專案資料夾需包含：
  video.json   區塊座標、各段旁白文字（見範例 ~/Movies/job-future-video/video.json）
  source.png   原始圖片（建議用 ASCII 檔名）
  voice/<版本>/<段落編號>.(m4a|wav|mp3)   自己錄的旁白（可選；沒有就用 edge-tts 產生暫用配音）
  bgm.mp3      背景音樂（可選）

輸出：<專案資料夾>/out/<版本>.mp4 與 RECORDING.md（錄音稿）。
需要：ffmpeg（含 libass）；暫用配音需要 edge-tts（pip install edge-tts，或以 EDGE_TTS 環境變數指定路徑）。
"""
import json, os, re, shutil, subprocess, sys
from pathlib import Path

FPS = 30
LEAD, TAIL, XFADE = 0.35, 0.7, 0.4
FONT = "Heiti TC"


def run(*args):
    subprocess.run([str(a) for a in args], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def duration(path):
    out = subprocess.run(["ffmpeg", "-i", str(path)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def even(x):
    return int(round(x / 2)) * 2


def tts(text, voice, dest):
    exe = os.environ.get("EDGE_TTS") or shutil.which("edge-tts")
    if not exe:
        sys.exit("找不到 edge-tts：請 pip install edge-tts，或錄好 voice/ 底下的旁白檔")
    run(exe, "--voice", voice, "--rate", "+5%", "--text", text, "--write-media", dest)


def prepare_audio(proj, ver, seg_id, text, voice):
    """優先用自己錄的聲音，否則用 edge-tts；統一去頭尾靜音、降噪、響度標準化。"""
    src = next((p for ext in ("m4a", "wav", "mp3")
                if (p := proj / "voice" / ver / f"{seg_id}.{ext}").exists()), None)
    human = src is not None
    if not human:
        src = proj / "tts" / ver / f"{seg_id}.mp3"
        src.parent.mkdir(parents=True, exist_ok=True)
        if not src.exists():
            tts(text, voice, src)
    dest = proj / "build" / ver / f"{seg_id}.wav"
    trim = "silenceremove=start_periods=1:start_threshold=-45dB"
    af = f"{'afftdn=nf=-25,' if human else ''}{trim},areverse,{trim},areverse,loudnorm=I=-16:TP=-1.5:LRA=11"
    run("ffmpeg", "-y", "-i", src, "-af", af, "-ar", 48000, "-ac", 2, dest)
    return dest, human


def split_cards(text, maxlen):
    """依標點切成字幕卡，過長的句子再依逗號合併切分。"""
    cards = []
    for sent in re.findall(r"[^。！？；]+[。！？；]?", text):
        parts = re.findall(r"[^，、：]+[，、：]?", sent)
        buf = ""
        for p in parts:
            if buf and len(buf) + len(p) > maxlen:
                cards.append(buf)
                buf = ""
            buf += p
        if buf:
            cards.append(buf)
    return [c.strip() for c in cards if c.strip()]


def ass_time(t):
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def write_ass(path, W, H, title, cues, total, vertical):
    size = 70 if vertical else 58
    margin = 250 if vertical else 45
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,{FONT},{size},&H00FFFFFF,&H00FFFFFF,&H00202020,&H80000000,-1,0,0,0,100,100,0,0,1,5,2,2,60,60,{margin},1
Style: Title,{FONT},78,&H00202020,&H00202020,&H0033D6FF,&H0033D6FF,-1,0,0,0,100,100,2,0,3,18,0,8,40,40,150,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [head]
    if vertical:
        lines.append(f"Dialogue: 1,{ass_time(0)},{ass_time(total)},Title,,0,0,0,,{title}\n")
    for start, end, text in cues:
        lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Sub,,0,0,0,,{text}\n")
    path.write_text("".join(lines), encoding="utf-8")


def strip_end_punct(s):
    return re.sub(r"[，、：；。]$", "", s)


def render_segment(proj, img, region, dur, W, H, vertical, zoom_in, dest, bg):
    cx, cy, cw, ch = region
    if vertical:
        bw, bh, top = W - 40, 1050, 330
    else:
        bw, bh, top = W - 120, 870, 40
    n = int(round(dur * FPS))
    s = min(bw / cw, bh / ch)
    if vertical and bh / ch > s:
        # 直式畫面放不下寬區塊：放大到可讀高度，再由左往右平移（4 倍取樣避免抖動）
        s = min(bh / ch, 2.6)
        sw, fh, fw = even(cw * s), even(ch * s), bw
        span = max(sw - fw, 0) * 4
        x = f"{span}*t/{dur:.3f}" if zoom_in else f"{span}*(1-t/{dur:.3f})"
        move = (f"scale={sw * 4}:{fh * 4}:flags=lanczos,loop=-1:1,fps={FPS},"
                f"crop={fw * 4}:{fh * 4}:'{x}':0,scale={fw}:{fh}:flags=area")
    else:
        fw, fh = even(cw * s), even(ch * s)
        z = f"1+0.06*on/{n}" if zoom_in else f"1.06-0.06*on/{n}"
        move = (f"scale={fw * 4}:{fh * 4}:flags=lanczos,"
                f"zoompan=z='{z}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s={fw}x{fh}:fps={FPS}")
    fy = top + (bh - fh) // 2
    fg = (f"[1]crop={cw}:{ch}:{cx}:{cy},{move},"
          f"pad={fw + 12}:{fh + 12}:6:6:white[fg];"
          f"[0][fg]overlay=(W-w)/2:{fy - 6}:shortest=1,format=yuv420p")
    run("ffmpeg", "-y", "-loop", 1, "-framerate", FPS, "-t", f"{dur:.3f}", "-i", bg,
        "-i", img, "-filter_complex", fg, "-frames:v", n, "-r", FPS,
        "-c:v", "libx264", "-crf", 18, "-preset", "fast", dest)


def build_version(proj, cfg, ver):
    vcfg = cfg["versions"][ver]
    W, H = vcfg["size"]
    vertical = H > W
    img = proj / cfg["image"]
    build = proj / "build" / ver
    build.mkdir(parents=True, exist_ok=True)

    bg = build / "bg.png"
    run("ffmpeg", "-y", "-i", img, "-vf",
        f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
        f"gblur=sigma=30,eq=brightness=-0.12:saturation=0.8", "-frames:v", 1, bg)

    segs, cues, offset, rec = [], [], 0.0, []
    maxlen = 13 if vertical else 22
    for i, (seg_id, region_name, text) in enumerate(vcfg["segments"]):
        wav, human = prepare_audio(proj, ver, seg_id, text, cfg.get("voice", "zh-TW-HsiaoChenNeural"))
        adur = duration(wav)
        dur = LEAD + adur + TAIL
        mp4 = build / f"{seg_id}.mp4"
        render_segment(proj, img, cfg["regions"][region_name], dur, W, H, vertical, i % 2 == 0, mp4, bg)

        cards = split_cards(text, maxlen)
        weights = [len(c) + 2 for c in cards]
        t = offset + LEAD
        for c, w in zip(cards, weights):
            d = adur * w / sum(weights)
            cues.append((t, t + d, strip_end_punct(c)))
            t += d
        segs.append((mp4, wav, dur, offset))
        rec.append((seg_id, text, adur, human))
        offset += dur - XFADE
    total = offset + XFADE

    ass = build / "subs.ass"
    write_ass(ass, W, H, cfg["title"], cues, total, vertical)

    args, chains = ["ffmpeg", "-y"], []
    for mp4, _, _, _ in segs:
        args += ["-i", mp4]
    for _, wav, _, _ in segs:
        args += ["-i", wav]
    n = len(segs)
    prev = "0:v"
    for i in range(1, n):
        off = segs[i][3]
        chains.append(f"[{prev}][{i}:v]xfade=transition=fade:duration={XFADE}:offset={off:.3f}[x{i}]")
        prev = f"x{i}"
    fontsdir = "/System/Library/Fonts"
    chains.append(f"[{prev}]subtitles=filename={ass}:fontsdir={fontsdir}[v]")
    for i, (_, _, _, off) in enumerate(segs):
        ms = int((off + LEAD) * 1000)
        chains.append(f"[{n + i}:a]adelay={ms}|{ms}[a{i}]")
    mix = "".join(f"[a{i}]" for i in range(n))
    bgm = proj / "bgm.mp3"
    if bgm.exists():
        args += ["-stream_loop", -1, "-i", bgm]
        chains.append(f"[{2 * n}:a]volume=0.08,atrim=0:{total:.3f},afade=t=out:st={total - 2:.3f}:d=2[bgm]")
        mix += "[bgm]"
        chains.append(f"{mix}amix=inputs={n + 1}:normalize=0:duration=longest[a]")
    else:
        chains.append(f"{mix}amix=inputs={n}:normalize=0:duration=longest[a]")

    out = proj / "out" / f"{ver}.mp4"
    out.parent.mkdir(exist_ok=True)
    args += ["-filter_complex", ";".join(chains), "-map", "[v]", "-map", "[a]",
             "-t", f"{total:.3f}", "-c:v", "libx264", "-crf", 20, "-preset", "medium",
             "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
    run(*args)
    print(f"{ver}: {out}（{total:.1f} 秒）")
    return rec


def write_recording_sheet(proj, cfg, recs):
    lines = [f"# 錄音稿：{cfg['title']}\n",
             "用 QuickTime（檔案 → 新增音訊錄製）或 iPhone 語音備忘錄錄製，",
             "存到下列路徑後重跑 `python3 scripts/make-video.py <專案資料夾>`，就會取代暫用配音。",
             "頭尾留白會自動裁掉，音量會自動標準化。\n"]
    for ver, rec in recs.items():
        lines.append(f"## {ver}\n")
        for seg_id, text, adur, human in rec:
            status = "✅ 已用你的錄音" if human else f"參考長度約 {adur:.0f} 秒"
            lines.append(f"### `voice/{ver}/{seg_id}.m4a`（{status}）\n\n{text}\n")
    (proj / "RECORDING.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    proj = Path(sys.argv[1]).expanduser().resolve()
    cfg = json.loads((proj / "video.json").read_text(encoding="utf-8"))
    versions = sys.argv[2:] or list(cfg["versions"])
    recs = {ver: build_version(proj, cfg, ver) for ver in versions}
    write_recording_sheet(proj, cfg, recs)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(f"ffmpeg 失敗：{' '.join(map(str, e.cmd))[:300]}\n{e.stderr.decode()[-1500:]}")
