# 🕐 Digital Clock - Multi Timezone Display

แอปพลิเคชันแสดงเวลาดิจิทัลแบบ Real-time สำหรับหลายโซนเวลาทั่วโลก

## ✨ ฟีเจอร์

✅ แสดงเวลาจริงสำหรับ 8 โซนเวลา  
✅ อัพเดตอัตโนมัติทุก 1 วินาที  
✅ แสดงวันที่ในแต่ละโซน  
✅ UI สวยงามด้วย Dark Theme  
✅ Threading สำหรับการอัพเดตที่ smooth  

## 🕐 โซนเวลาที่รองรับ

1. 🇹🇭 Bangkok (Thailand) - Asia/Bangkok
2. 🇯🇵 Tokyo (Japan) - Asia/Tokyo
3. 🇺🇸 New York (USA) - America/New_York
4. 🇬🇧 London (UK) - Europe/London
5. 🇦🇺 Sydney (Australia) - Australia/Sydney
6. 🇦🇪 Dubai (UAE) - Asia/Dubai
7. 🇺🇸 Los Angeles (USA) - America/Los_Angeles
8. 🇫🇷 Paris (France) - Europe/Paris

## 📦 Requirements

```
pytz
```

## 🚀 วิธีใช้งาน

### 1. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

### 2. รัน Clock

```bash
python clock.py
```

### 3. แสดงผล

```
🌍 Global Time Zones

┌─────────────────┬─────────────────┐
│  Bangkok        │  Tokyo          │
│  13:45:32       │  14:45:32       │
│  2026-05-18     │  2026-05-18     │
└─────────────────┴─────────────────┘

┌─────────────────┬─────────────────┐
│  New York       │  London         │
│  00:15:32       │  05:15:32       │
│  2026-05-18     │  2026-05-18     │
└─────────────────┴─────────────────┘
```

## 🎨 การปรับแต่ง

### เปลี่ยนโซนเวลา

แก้ไข `TIMEZONES` ใน `clock.py`:

```python
self.timezones = {
    "Bangkok 🇹🇭": "Asia/Bangkok",
    "Tokyo 🇯🇵": "Asia/Tokyo",
    "Singapore 🇸🇬": "Asia/Singapore",  # เพิ่มโซนใหม่
}
```

### เปลี่ยนสี

```python
"#0f0f1e"  # Background color
"#00d4ff"  # Title color
"#00ff41"  # Time color
"#ffd700"  # Date color
```

### เปลี่ยนขนาดฟอนต์

```python
self.time_font = tkfont.Font(family="Courier New", size=40, weight="bold")
```

## 📁 โครงสร้าง

```
digital-clock/
├── clock.py
├── requirements.txt
└── README.md
```

## 🛠️ Technical Details

- **GUI Framework**: Tkinter
- **Timezone Library**: pytz
- **Threading**: Python threading module
- **Update Interval**: 1 second
- **Display Format**: HH:MM:SS (24-hour)

## 🎯 ใช้งาน

- ⏰ ดูเวลาในหลายประเทศพร้อมกัน
- 🌍 ติดตามเวลาทั่วโลก
- 📊 Business & Communication
- 🎓 Time Zone Reference
- 🖥️ Desktop Widget

## 👤 Creator

GitHub: [@otimzom-rgb](https://github.com/otimzom-rgb)

## 📄 License

MIT License
