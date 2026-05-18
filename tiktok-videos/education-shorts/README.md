# 🎬 Social Media Content - Education Shorts

สร้างหนังสั้น Motion Graphics ละครคุณธรรม **"ความสำคัญของการศึกษา"** สำหรับ TikTok / Instagram Reels

## 📋 ข้อมูลโปรเจกต์

- **ประเภท**: Motion Graphics Video
- **หัวข้อ**: ความสำคัญของการศึกษา (ตัวละคร: แม่ลูก)
- **Platform**: TikTok / Instagram Reels
- **ขนาด**: 9:16 (Vertical)
- **ความยาว**: 50 วินาที (1-2 นาที)

## 🎯 ฉากในวิดีโอ

1. **ฉากที่ 1** (5 วินาที) - 🌅 ตอนเช้า บ้านธรรมดา
2. **ฉากที่ 2** (10 วินาที) - 📚 แม่อธิบายให้ลูก
3. **ฉากที่ 3** (10 วินาที) - ✨ เรื่องส่วนตัวของแม่
4. **ฉากที่ 4** (10 วินาที) - 💡 ลูกรู้สึกตัว
5. **ฉากที่ 5** (15 วินาที) - 🌟 บทสรุป

## 🚀 วิธีใช้งาน

### 1. Clone Repository
```bash
git clone https://github.com/otimzom-rgb/social-media-content.git
cd social-media-content
```

### 2. ไปโฟลเดอร์โปรเจกต์
```bash
cd tiktok-videos/education-shorts
```

### 3. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 4. สร้างวิดีโอ
```bash
python education_shorts.py
```

### 5. ได้ไฟล์
```
education_shorts.mp4  ✅ พร้อมลง TikTok/Instagram Reels
```

## 🤖 GitHub Actions (Automatic)

เมื่อ push ขึ้น main branch:

✅ รันอัตโนมัติสร้างวิดีโอ  
✅ Upload ไป **Artifacts** (เก็บ 30 วัน)  
✅ สร้าง **Release** ใหม่  
✅ Auto commit ไฟล์ video  

### ดูผลลัพธ์:
- 📦 **Artifacts**: https://github.com/otimzom-rgb/social-media-content/actions
- 📌 **Releases**: https://github.com/otimzom-rgb/social-media-content/releases

## 📁 โครงสร้าง Folder

```
social-media-content/
├── .github/workflows/
│   └── create-video.yml              # GitHub Actions Workflow
├── tiktok-videos/
│   └── education-shorts/
│       ├── education_shorts.py       # Main Script
│       ├── requirements.txt          # Python Dependencies
│       ├── README.md                 # Folder Info
│       └── education_shorts.mp4      # Output Video (Generated)
├── README.md                         # Project Info
└── .gitignore                        # Git Ignore Rules
```

## 📦 Dependencies

- moviepy==1.0.3
- Pillow==10.0.0
- numpy==1.24.0

## 🎨 ปรับแต่งได้

แก้ไข `SCENES` ใน `education_shorts.py`:

```python
"duration": 5,              # เปลี่ยนระยะเวลา (วินาที)
"bg_color": (135, 206, 235),  # เปลี่ยนสี RGB
"text": ["บรรทัดที่ 1", "", "บรรทัดที่ 2"],  # เปลี่ยนข้อความ
"emoji": "🌅",              # เปลี่ยน Emoji
"text_size": 50,            # เปลี่ยนขนาดตัวอักษร
```

## 📱 ใช้ได้กับ

✅ TikTok  
✅ Instagram Reels  
✅ YouTube Shorts  
✅ Facebook  

## 👤 Creator

GitHub: [@otimzom-rgb](https://github.com/otimzom-rgb)  
Repository: [social-media-content](https://github.com/otimzom-rgb/social-media-content)

## 📄 License

MIT License - สามารถใช้งานและแก้ไขได้อย่างอิสระ

---

**สร้างเนื้อหา Motion Graphics ด้วย Python ได้ง่าย ๆ! 🚀✨**
