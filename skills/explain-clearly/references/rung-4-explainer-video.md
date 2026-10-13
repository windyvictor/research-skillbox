# R4 — 图解视频（Explainer Video）

Karpathy 原话："The output format I am most bullish on is fully custom / bespoke explainer
videos generated on any arbitrary topic."

这一级的价值：**读者零力气**。不用读、不用点、不用找。旁白按时序推进，画面同步跟上。
代价是产出成本最高，所以只在值得的时候用。

---

## 1. 何时升到 R4

- 内容是**一条线性叙事**（有起点、有转折、有终点）。
- 有**时间演化**（先这样，然后那样，最后收敛）。
- 值得被**反复观看**（要发给别人、要在课上放、要当内容发布）。
- 主题需要**仪式感**（重大结论、报告开场、课程引入）。

**不要升的情形**：内容有分支（读者想跳着看 → 用 R3）；只需要一个结论（用 R0）；
你自己 3 分钟就能讲完（那就直接讲）。

## 2. 3b1b 风格要素（3Blue1Brown）

- **深色底**（近黑，如 `#0b0f14`），高对比浅色线条。视觉焦点在几何体上。
- **几何动画驱动**：图形自己移动/变换/生长，而不是切幻灯片。
- **旁白驱动节奏**：一句旁白对应一次画面揭示。**画面跟着话走，不是话跟着画面走。**
- **逐句揭示**：不要一次上满一屏。信息按理解顺序出现。
- **连续推导**：同一构图内完成一长串变形，减少跳切。
- **克制**：无花哨转场、无音效堆砌、无片头 Logo 动画。片头 2 秒内进正题。

## 3. 四步流水线

顺序不可颠倒。**先写脚本，再配音，再配画，最后合成。**

### 第 1 步：写脚本（旁白）

- 每句话 = 一个 **scene**（场景）。一句话太长就拆成两个 scene。
- 旁白用 **R1 受控写法**：一句一事、主动语态、无冗余副词。这是决定视频好不好懂的
  **最大变量**，比画面精美度重要得多。
- 篇幅基准：**每 100 字中文 ≈ 30 秒**（正常语速）。一个主题控制在 60–180 秒。
- 写完通读一遍，删掉所有"接下来我们来看""正如大家所知"。

### 第 2 步：配音（TTS 三种方案）

| 方案 | 命令 / 依赖 | 优点 | 缺点 |
|---|---|---|---|
| **A. macOS 本地（免费、离线）** | `say -v Tingting -o out.aiff --data-format=LEF32@22050 "文本"` | 零依赖、离线、隐私好、**用本地算力** | 音色机械 |
| **B. edge-tts（免费、在线）** | `pip install edge-tts` → `edge-tts --voice zh-CN-XiaoxiaoNeural --text "..." --write-media out.mp3` | 音色自然、免费、无需 key | 需要联网 |
| **C. ElevenLabs（最自然、需 key）** | 需要 API key；`POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}` | 最自然、可克隆音色 | 付费、需联网 |

中文音色：`say -v '?' | grep zh_` 查看（常用 `Tingting` / `Meijia`）。
英文音色：`Samantha` / `Alex`。

**无 API key 时的正确做法**（Karpathy 本人也这么说）：让模型帮你找**用本地算力的免费替代**
——即方案 A 或 B。不要因为缺 key 就放弃这一级。

### 第 3 步：画面

每个 scene 一张图（或一组帧）：

| 画法 | 工具 | 适合 |
|---|---|---|
| SVG 手写坐标系/几何体 | 直接写 SVG，再用 `cairosvg` 或 `rsvg-convert` 转 PNG | 几何、曲线、示意 |
| 程序化绘图 | Python + matplotlib / Pillow（图、标注、排版） | 数据图、公式 |
| HTML 截图 | Playwright / Puppeteer 对单页截图 | 排版自由、可复用 R3 的 HTML |
| 纯色 + 大字幕 | ffmpeg `drawtext` | 只有口播的极简片 |

**多帧动画**：同一 scene 内想要动，就生成序列帧（如 60 帧），用 `-framerate 30 -i f%04d.png`
合成。做不到就先做**静态图 + 音频长度铺满**，这是最稳的基线。

### 第 4 步：合成（ffmpeg）

**ffmpeg 不一定预装。** 免 brew 的可靠获取方式：

```bash
pip install imageio-ffmpeg          # 自带静态 ffmpeg 二进制
python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
```

拿到二进制路径后（下称 `$FF`）：

```bash
# 单个 scene：静态图 + 音频 → 分段 mp4
"$FF" -y -loop 1 -i scene01.png -i scene01.wav \
      -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 30 \
      -c:a aac -b:a 192k -shortest -vf scale=1920:1080 scene01.mp4

# 多个分段：concat demuxer（列表里必须写绝对路径）
printf "file '%s'\n" "$PWD"/seg_*.mp4 > list.txt
"$FF" -y -f concat -safe 0 -i list.txt -c copy final.mp4

# 加淡入淡出（每段首尾 0.3s）
"$FF" -y -i seg.mp4 -vf "fade=t=in:st=0:d=0.3,fade=t=out:st=4.7:d=0.3" seg_f.mp4
```

**一键成片**：`scripts/build_explainer_video.py` 把上面全串起来。

## 4. 自动化脚本：`scripts/build_explainer_video.py`

```bash
python3 scripts/build_explainer_video.py scenes.json -o out/explainer.mp4
```

输入 `scenes.json`（示例见 `assets/video-scenes.example.json`）：

```json
{
  "title": "什么是输出升维",
  "tts": "say",
  "voice": "Tingting",
  "size": [1920, 1080],
  "fps": 30,
  "gap": 0.4,
  "scenes": [
    { "id": "01", "text": "一句话说不清的时候，不要说得更久。", "image": "frames/01.png" },
    { "id": "02", "text": "换一种介质。", "image": "frames/02.png" }
  ]
}
```

脚本行为：
1. 用 `say`（或 `edge-tts`，若 `tts` 字段指定且已安装）为每个 scene 生成配音；
2. 探测每个音频时长，按"音频时长 + gap"生成该段的视频；
3. 无 `image` 的场景用纯色底 + 居中大字幕（需 `--drawtext` 且提供字体路径）；
4. concat 所有分段成最终 mp4；
5. 打印每段时长表与总时长。

依赖缺失时脚本会打印**可直接粘贴的替代命令**，不会静默失败。

## 5. 质量控制清单

- [ ] 旁白每句都能独立成段（不能有"这个""它"指代上一句）。
- [ ] 每段停留 = 旁白时长 + 0.3~0.5s（不给人踩尾巴的感觉）。
- [ ] 总时长符合主题重量（30 秒讲清楚就别做 3 分钟）。
- [ ] 分辨率 1920×1080（**宽高必须是偶数**，否则 H.264 报错）。
- [ ] 帧率统一 30fps；CRF 18–22。
- [ ] 音量归一化：`-af loudnorm=I=-16:TP=-1.5:LRA=11`。
- [ ] 首 2 秒内进正题，无 Logo 动画。
- [ ] 有字幕文件（`.srt`）——很多人静音看。
- [ ] 深色底 + 浅色字，手机小屏也能看清（字号 ≥ 48px 等效）。

## 6. 常见坑

| 坑 | 症状 | 解法 |
|---|---|---|
| 分辨率奇数 | `width not divisible by 2` | `-vf scale=1920:1080` |
| concat 相对路径 | `No such file or directory` | 列表里写绝对路径，加 `-safe 0` |
| `say` 输出格式 | ffmpeg 不识别 aiff | `--data-format=LEF32@22050`，或转 `-ar 44100 -ac 1` |
| 分段音频被截 | 最后一句听不全 | 去掉 `-shortest`，或给图加 `-t <音频时长+gap>` |
| 中文 drawtext 方块 | 字体缺中文 | 指定 `fontfile=/System/Library/Fonts/PingFang.ttc` |
| 无 ffmpeg | 命令找不到 | `pip install imageio-ffmpeg` 取二进制 |
| 内容太长 | 观感像讲座 | 拆成系列短片，每片一个主张 |
