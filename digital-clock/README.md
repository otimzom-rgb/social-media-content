# 🕐 Digital Clock - Multi Timezone

แสดงเวลาจริงใน 8 โซนเวลาต่างๆ พร้อม Dark Theme ที่สวยงาม

## 🌍 โซนเวลา

- 🇹🇭 Bangkok (Thailand)
- 🇯🇵 Tokyo (Japan)
- 🇺🇸 New York (USA)
- 🇬🇧 London (UK)
- 🇦🇺 Sydney (Australia)
- 🇦🇪 Dubai (UAE)
- 🇺🇸 Los Angeles (USA)
- 🇫🇷 Paris (France)

## 🚀 วิธีใช้งาน

```bash
# ติดตั้ง
pip install -r requirements.txt

# รัน
python clock.py
```

## ✨ Features

✅ แสดงเวลาจริง 8 โซนเวลา  
✅ อัพเดตอัตโนมัติทุก 1 วินาที  
✅ Dark Theme สวยงาม  
✅ แสดงวันที่ + เวลา  
✅ Responsive Design  

## 🎨 สี

- Background: `#1a1a2e` (Dark)
- Title: `#00d4ff` (Cyan)
- Time: `#00ff41` (Green)
- Date: `#a8dadc` (Light)

## 📝 Customization

เปลี่ยนโซนเวลาใน `clock.py`:

```python
self.timezones = {
    "Bangkok 🇹🇭": "Asia/Bangkok",
    "Singapore 🇸🇬": "Asia/Singapore",  # เพิ่ม
    "Hong Kong 🇭🇰": "Asia/Hong_Kong",  # เพิ่ม
}
```

## 📦 Requirements

- tkinter
- pytz

---

**ลองรันตอนนี้เลย!** ⏰✨
