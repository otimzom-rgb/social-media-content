# 📥 Video Downloader

ดาวน์โหลดวิดีโอจาก YouTube, TikTok, Instagram, Twitch และอื่น ๆ

## ✨ ฟีเจอร์

✅ ดาวน์โหลดวิดีโอจาก YouTube, TikTok, Instagram  
✅ เลือกคุณภาพวิดีโอ (Best, 1080p, 720p, 480p)  
✅ ดาวน์โหลด Playlist ทั้งหมด  
✅ ดึงเสียง (MP3) จากวิดีโอ  
✅ ดึงข้อมูลวิดีโอ (Title, Duration, Views, etc.)  
✅ Auto retry เมื่อเกิด error  
✅ ตัวเลือก output folder  

## 📦 Requirements

```bash
yt-dlp>=2024.1.1
requests>=2.31.0
ffmpeg (system requirement)
```

## 🚀 วิธีใช้งาน

### 1. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

### 2. ติดตั้ง FFmpeg (สำคัญ!)

**Mac:**
```bash
brew install ffmpeg
```

**Ubuntu/Linux:**
```bash
sudo apt-get install ffmpeg
```

**Windows (Chocolatey):**
```bash
choco install ffmpeg
```

### 3. รัน Program

```bash
python video_downloader.py
```

### 4. เลือก Option

```
📥 Video Downloader
============================================================

1. Download Video
2. Download Playlist
3. Download Audio (MP3)
4. Get Video Info
5. Exit

📌 Select option (1-5): 1
```

## 🎯 Menu Options

| Option | Description |
|--------|-------------|
| 1 | ดาวน์โหลดวิดีโอเดี่ยว |
| 2 | ดาวน์โหลด Playlist ทั้งหมด |
| 3 | ดึงเสียง (MP3) |
| 4 | ดึงข้อมูลวิดีโอ |
| 5 | ออกจากโปรแกรม |

## 📝 Output Example

### Download Video
```
🎬 Downloading from: https://www.youtube.com/watch?v=...
📊 Quality: best

============================================================
✅ Downloaded successfully!
📁 File: video_title.mp4
📊 Size: 125.50 MB
📍 Location: /path/to/downloads/video_title.mp4
============================================================
```

### Get Video Info
```
📊 Getting video info from: https://www.youtube.com/watch?v=...

============================================================
📺 Title: Video Title
⏱️  Duration: 10:35
👤 Uploader: Channel Name
👁️  Views: 1,234,567
❤️  Likes: 45,678
📅 Uploaded: 20260515
============================================================
```

## 🎨 คุณภาพวิดีโอ

| Quality | Resolution | Size (approx) |
|---------|------------|---------------|
| Best | Auto | ที่ดีที่สุด |
| High | 1080p | 50-150 MB/min |
| Medium | 720p | 30-80 MB/min |
| Low | 480p | 10-30 MB/min |

## 🌍 Supported Platforms

✅ YouTube  
✅ TikTok  
✅ Instagram  
✅ Twitch  
✅ Facebook  
✅ Twitter/X  
✅ Dailymotion  
✅ Vimeo  
✅ และอื่น ๆ อีกมากมาย  

## 📁 Folder Structure

```
content-tools/video-downloader/
├── video_downloader.py
├── requirements.txt
├── README.md
└── downloads/                    # Output folder
    ├── video1.mp4
    ├── video2.mp4
    └── audio/
        └── song.mp3
```

## ⚙️ Advanced Usage

### ใช้ใน Python Script

```python
from video_downloader import VideoDownloader

# สร้าง instance
downloader = VideoDownloader(output_path="my_downloads")

# ดาวน์โหลดวิดีโอ
downloader.download_video("https://www.youtube.com/watch?v=...", quality="high")

# ดาวน์โหลด Playlist
downloader.download_playlist("https://www.youtube.com/playlist?list=...", quality="medium")

# ดึงเสียง
downloader.download_audio("https://www.youtube.com/watch?v=...")

# ดึงข้อมูลวิดีโอ
info = downloader.get_video_info("https://www.youtube.com/watch?v=...")
print(info)
```

## ⚠️ หมายเหตุ

- ❌ **ห้ามใช้ดาวน์โหลดเนื้อหาที่มีลิขสิทธิ์** โดยไม่ได้รับอนุญาต
- ⚠️ **เคารพสิทธิ์ผู้สร้างเนื้อหา**
- 📌 **ใช้ตรวจสอบนโยบายของเว็บไซต์** ก่อนดาวน์โหลด
- 🔒 **ไม่ใช้ดาวน์โหลดเพื่อวัตถุประสงค์ที่ผิดกฎหมาย**

## 🛠️ Troubleshooting

### "FFmpeg not found"
```bash
# ติดตั้ง FFmpeg
brew install ffmpeg  # Mac
sudo apt-get install ffmpeg  # Linux
choco install ffmpeg  # Windows
```

### "Failed to download"
- ✅ ตรวจสอบ URL
- ✅ ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต
- ✅ ลองดาวน์โหลดใหม่

### "No space left on device"
- ✅ ตรวจสอบพื้นที่ว่างในเครื่อง
- ✅ ลองคุณภาพที่ต่ำกว่า

## 👤 Creator

GitHub: [@otimzom-rgb](https://github.com/otimzom-rgb)

## 📄 License

MIT License
