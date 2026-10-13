#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_explainer_video.py — R4 图解视频一键成片

输入：一个 scenes.json（见 assets/video-scenes.example.json）
输出：一个 mp4（每个 scene = 一段「配音 + 静止画面」，全部拼接）

流水线（顺序不可颠倒）
    1. 旁白配音  say（本地免费 / 离线）或 edge-tts（免费 / 在线）
    2. 探测每段时长
    3. 每段：图 or 纯色底 + 大字幕 + 音频 → 分段 mp4
    4. concat 所有分段 → 最终 mp4
    5. 可选：叠加 BGM、输出 SRT 字幕

用法
    python3 build_explainer_video.py scenes.json -o out/explainer.mp4
    python3 build_explainer_video.py scenes.json --dry-run          # 只打印命令
    python3 build_explainer_video.py scenes.json --tts edge-tts --voice zh-CN-XiaoxiaoNeural
    python3 build_explainer_video.py scenes.json --drawtext --fontsize 56
    python3 build_explainer_video.py scenes.json --music bgm.mp3 --srt out/explainer.srt

依赖
    必需：python3（标准库）、macOS 的 say（或已安装 edge-tts）、ffmpeg
    ffmpeg 缺失时的免 brew 获取方式：
        pip install imageio-ffmpeg
    可选：Pillow（生成纯色底帧，非必需，ffmpeg 的 color 源可替代）
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

FONT_CANDIDATES = [
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "C:/Windows/Fonts/msyh.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]


# ---------------------------------------------------------------- 工具

def info(msg: str) -> None:
    print(f"[build] {msg}", flush=True)


def warn(msg: str) -> None:
    print(f"[warn ] {msg}", file=sys.stderr, flush=True)


def die(msg: str, hint: str = "") -> None:
    print(f"[error] {msg}", file=sys.stderr, flush=True)
    if hint:
        print(hint, file=sys.stderr, flush=True)
    sys.exit(1)


def find_ffmpeg(explicit: str | None = None) -> str | None:
    if explicit:
        return explicit if Path(explicit).exists() or shutil.which(explicit) else None
    env = os.environ.get("FFMPEG")
    if env and Path(env).exists():
        return env
    which = shutil.which("ffmpeg")
    if which:
        return which
    try:
        import imageio_ffmpeg  # type: ignore
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def run(cmd: list[str], *, dry: bool) -> int:
    printable = " ".join(f'"{c}"' if " " in c else c for c in cmd)
    if dry:
        print("  $ " + printable)
        return 0
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        warn(f"命令失败（{proc.returncode}）：{printable}")
        tail = (proc.stderr or "").strip().splitlines()[-6:]
        for line in tail:
            print("      " + line, file=sys.stderr)
    return proc.returncode


def wav_duration(path: Path) -> float:
    """用标准库 wave 读时长（amix/mp3 不支持时走 ffmpeg 探测）。"""
    try:
        with wave.open(str(path)) as w:
            return w.getnframes() / float(w.getframerate() or 1)
    except Exception:
        return 0.0


def ffprobe_duration(ffmpeg: str, path: Path) -> float:
    """用 ffmpeg -i 的 stderr 里读 Duration（不依赖 ffprobe）。"""
    proc = subprocess.run([ffmpeg, "-hide_banner", "-i", str(path)],
                          capture_output=True, text=True)
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", proc.stderr or "")
    if not m:
        return 0.0
    h, mi, s = int(m.group(1)), int(m.group(2)), float(m.group(3))
    return h * 3600 + mi * 60 + s


def fmt_ts(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def wrap_cjk(text: str, width: int = 20) -> str:
    """按字宽折行，避免中文字幕冲出画面。"""
    out, buf = [], ""
    for ch in text:
        buf += ch
        if len(buf) >= width and ch in "，。！？；、,.:;":
            out.append(buf)
            buf = ""
    if buf:
        out.append(buf)
    return "\n".join(out)


def pick_font(explicit: str | None) -> str | None:
    if explicit:
        return explicit if Path(explicit).exists() else None
    for cand in FONT_CANDIDATES:
        if Path(cand).exists():
            return cand
    return None


# ---------------------------------------------------------------- TTS

def tts_say(text: str, voice: str, out_wav: Path, rate: int | None, dry: bool) -> bool:
    if not shutil.which("say"):
        warn("找不到 say（仅 macOS 可用）。改用 --tts edge-tts，或换一台机器配音。")
        return False
    cmd = ["say", "-v", voice, "-o", str(out_wav),
           "--file-format=WAVE", "--data-format=LEI16@22050"]
    if rate:
        cmd += ["-r", str(rate)]
    cmd += ["--", text]
    if run(cmd, dry=dry) != 0:
        return False
    return True


def tts_edge(text: str, voice: str, out_mp3: Path, dry: bool) -> bool:
    exe = shutil.which("edge-tts")
    if exe:
        cmd = [exe, "--voice", voice, "--text", text, "--write-media", str(out_mp3)]
    else:
        cmd = [sys.executable, "-m", "edge_tts", "--voice", voice,
               "--text", text, "--write-media", str(out_mp3)]
    if run(cmd, dry=dry) != 0:
        warn("edge-tts 不可用。安装：pip install edge-tts（需要联网）")
        return False
    return True


# ---------------------------------------------------------------- 分段构建

def build_segment(ffmpeg: str, *, image: Path | None, audio: Path | None, text: str,
                  out: Path, dur: float, size: tuple[int, int], fps: int,
                  drawtext: bool, font: str | None, fontsize: int, bg: str,
                  tmp: Path, dry: bool) -> int:
    w, h = size
    cmd = [ffmpeg, "-y", "-hide_banner", "-loglevel", "error"]

    if image and image.exists():
        cmd += ["-loop", "1", "-i", str(image)]
    else:
        dur = max(dur, 1.0)
        cmd += ["-f", "lavfi", "-i", f"color=c={bg}:s={w}x{h}:r={fps}"]

    if audio and audio.exists():
        cmd += ["-i", str(audio)]

    # 视频滤镜：缩放 + 补齐（保证宽高偶数、比例不破）
    vf = (f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
          f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color={bg},setsar=1")

    if drawtext and text:
        if not font:
            warn("未找到可用中文字体，跳过字幕。用 --font 指定字体路径。")
        else:
            txt_file = tmp / (out.stem + ".txt")
            txt_file.write_text(wrap_cjk(text, width=max(12, int(w / fontsize * 0.9))),
                                encoding="utf-8")
            vf += (f",drawtext=fontfile='{font}':textfile='{txt_file}'"
                   f":fontcolor={bg if bg == 'white' else 'white'}"
                   f":fontsize={fontsize}:x=(w-text_w)/2:y=(h-text_h)/2:line_spacing=18")

    dur = max(dur, 1.0)
    cmd += ["-vf", vf, "-c:v", "libx264", "-tune", "stillimage",
            "-pix_fmt", "yuv420p", "-r", str(fps), "-preset", "medium", "-crf", "20"]

    if audio and audio.exists():
        # say 默认输出 22050Hz 单声道；统一到 44.1kHz 立体声，便于后续混音与播放器兼容
        cmd += ["-af", "apad", "-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "192k"]

    cmd += ["-t", f"{dur:.3f}", str(out)]
    return run(cmd, dry=dry)


# ---------------------------------------------------------------- 主流程

def main() -> int:
    ap = argparse.ArgumentParser(description="R4 图解视频一键成片")
    ap.add_argument("scenes", help="scenes.json 路径")
    ap.add_argument("-o", "--out", default="explainer.mp4", help="输出 mp4 路径")
    ap.add_argument("--workdir", default="", help="中间产物目录（默认 out 同级的 _build）")
    ap.add_argument("--ffmpeg", default="", help="ffmpeg 可执行文件路径")
    ap.add_argument("--tts", default="", choices=["", "say", "edge-tts", "none"],
                    help="配音方式（默认读 json 的 tts 字段，缺省 say）")
    ap.add_argument("--voice", default="", help="音色（默认读 json 的 voice 字段）")
    ap.add_argument("--rate", type=int, default=0, help="say 语速，词/分钟（默认系统值）")
    ap.add_argument("--gap", type=float, default=-1, help="每段末尾留白秒数（默认读 json，缺省 0.4）")
    ap.add_argument("--size", default="", help="分辨率，如 1920x1080（默认读 json）")
    ap.add_argument("--fps", type=int, default=0, help="帧率（默认读 json，缺省 30）")
    ap.add_argument("--bg", default="0x0b0f14", help="背景色（纯色底与补边用）")
    ap.add_argument("--drawtext", action="store_true", help="第 1 图缺失时把旁白画到画面中央")
    ap.add_argument("--font", default="", help="字幕字体文件路径")
    ap.add_argument("--fontsize", type=int, default=52, help="字幕字号")
    ap.add_argument("--music", default="", help="BGM 音频文件（循环铺底，音量 12%）")
    ap.add_argument("--srt", default="", help="同时输出 SRT 字幕路径")
    ap.add_argument("--dry-run", action="store_true", help="只打印将执行的命令")
    ap.add_argument("--keep", action="store_true", help="保留中间产物")
    args = ap.parse_args()

    spec_path = Path(args.scenes).expanduser().resolve()
    if not spec_path.exists():
        die(f"找不到清单文件：{spec_path}")
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    scenes = spec.get("scenes") or []
    if not scenes:
        die("清单里没有 scenes。")

    out_path = Path(args.out).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    work = Path(args.workdir).expanduser().resolve() if args.workdir \
        else out_path.parent / "_build"
    work.mkdir(parents=True, exist_ok=True)

    # 参数合并：命令行 > json > 默认
    tts = args.tts or spec.get("tts") or "say"
    voice = args.voice or spec.get("voice") or ("Tingting" if tts == "say" else "zh-CN-XiaoxiaoNeural")
    gap = args.gap if args.gap >= 0 else float(spec.get("gap", 0.4))
    fps = args.fps or int(spec.get("fps", 30))
    if args.size:
        w, h = (int(x) for x in args.size.lower().replace("*", "x").split("x"))
    else:
        w, h = (spec.get("size") or [1920, 1080])[:2]
    w, h = int(w) // 2 * 2, int(h) // 2 * 2     # H.264 要求偶数宽高
    size = (w, h)

    ffmpeg = find_ffmpeg(args.ffmpeg or None)
    if not ffmpeg:
        die("找不到 ffmpeg。",
            "  免 brew 获取方式：pip install imageio-ffmpeg\n"
            "  然后重跑本脚本；或显式指定：--ffmpeg /path/to/ffmpeg")

    font = pick_font(args.font or None) if args.drawtext else None

    info(f"清单 {spec_path.name} · {len(scenes)} 个 scene · {w}x{h}@{fps}fps · TTS={tts}/{voice}")
    info(f"ffmpeg = {ffmpeg}")
    info(f"中间产物 = {work}")

    tmp = Path(tempfile.mkdtemp(prefix="tts_", dir=str(work)))
    segments: list[Path] = []
    timeline: list[tuple[int, str, float, float]] = []   # (seq, text, start, end)
    cursor = 0.0

    for idx, sc in enumerate(scenes, 1):
        sid = str(sc.get("id") or f"{idx:02d}")
        text = (sc.get("text") or "").strip()
        audio: Path | None = None

        # --- 1. 配音
        if tts != "none" and text:
            if tts == "say":
                cand = tmp / f"{sid}.wav"
                if tts_say(text, voice, cand, args.rate or None, args.dry_run):
                    audio = cand
            else:
                cand = tmp / f"{sid}.mp3"
                if tts_edge(text, voice, cand, args.dry_run):
                    audio = cand

        # --- 2. 时长
        if sc.get("duration"):
            dur = float(sc["duration"])
        elif audio and audio.exists():
            dur = wav_duration(audio) if audio.suffix == ".wav" else 0.0
            if dur <= 0:
                dur = ffprobe_duration(ffmpeg, audio)
        else:
            dur = 2.0
        if audio and audio.exists() and sc.get("gap") is None:
            dur += gap
        elif audio and audio.exists():
            dur += float(sc["gap"])

        # --- 3. 画面
        img = sc.get("image")
        image = (spec_path.parent / img).resolve() if img else None
        seg = work / f"seg_{sid}.mp4"

        info(f"  scene {sid}: 旁白 {len(text)} 字 · 时长 {dur:.2f}s"
             f" · 画面 {'有' if (image and image.exists()) else '纯色底'}")

        rc = build_segment(ffmpeg, image=image, audio=audio, text=text, out=seg,
                           dur=dur, size=size, fps=fps, drawtext=args.drawtext,
                           font=font, fontsize=args.fontsize, bg=args.bg,
                           tmp=tmp, dry=args.dry_run)
        if rc != 0 and not args.dry_run:
            die(f"scene {sid} 渲染失败。常见原因：分辨率奇数、图片路径错、字体文件无效。")
        if image and not image.exists():
            warn(f"scene {sid} 的图片不存在：{image}（已用纯色底替代）")

        segments.append(seg)
        timeline.append((idx, text, cursor, cursor + dur))
        cursor += dur

    # --- 4. 拼接
    list_file = work / "concat.txt"
    list_file.write_text(
        "".join(f"file '{p.as_posix()}'\n" for p in segments), encoding="utf-8")
    info(f"拼接 {len(segments)} 段 → {out_path.name}（预计总长 {cursor:.1f}s）")
    rc = run([ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
              "-f", "concat", "-safe", "0", "-i", str(list_file),
              "-c", "copy", str(out_path)], dry=args.dry_run)
    if rc != 0 and not args.dry_run:
        warn("-c copy 拼接失败，回退到重编码拼接")
        run([ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
             "-f", "concat", "-safe", "0", "-i", str(list_file),
             "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", str(out_path)], dry=args.dry_run)

    # --- 5. BGM & 字幕
    if args.music and not args.dry_run:
        music = Path(args.music).expanduser().resolve()
        if music.exists():
            mixed = work / (out_path.stem + "_music.mp4")
            info(f"叠加 BGM：{music.name}（音量 12%，尾部 2s 淡出）")
            run([ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
                 "-i", str(out_path), "-stream_loop", "-1", "-i", str(music),
                 "-filter_complex",
                 f"[1:a]volume=0.12,afade=t=out:st={max(0, cursor - 2):.2f}:d=2[m];"
                 f"[0:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]",
                 "-map", "0:v", "-map", "[a]", "-c:v", "copy",
                 "-c:a", "aac", "-b:a", "192k", "-shortest", str(mixed)], dry=False)
            mixed.replace(out_path)
        else:
            warn(f"BGM 文件不存在：{music}")

    if args.srt:
        srt = Path(args.srt).expanduser().resolve()
        lines = []
        for i, (_, text, st, en) in enumerate(timeline, 1):
            lines.append(f"{i}\n{fmt_ts(st)} --> {fmt_ts(en)}\n{text}\n")
        srt.parent.mkdir(parents=True, exist_ok=True)
        srt.write_text("\n".join(lines), encoding="utf-8")
        info(f"字幕已写入 {srt}")

    # --- 6. 报告
    print()
    print("场景时长表")
    print(f"  {'#':>3}  {'起':>7}  {'止':>7}  {'时长':>6}  旁白")
    for i, text, st, en in timeline:
        t = text if len(text) <= 30 else text[:30] + "…"
        print(f"  {i:>3}  {st:>6.2f}s  {en:>6.2f}s  {en - st:>5.2f}s  {t}")
    print(f"  总时长 {cursor:.2f}s（{cursor / 60:.1f} 分钟）")
    if not args.dry_run:
        info(f"完成 → {out_path}")

    if not args.keep and not args.dry_run and tmp.exists():
        shutil.rmtree(tmp, ignore_errors=True)

    if args.dry_run:
        print()
        print("这是 dry-run，未生成任何文件。去掉 --dry-run 即执行。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
