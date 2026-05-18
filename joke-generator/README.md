# 🎭 Random Joke Generator

แอปพลิเคชันสำหรับสร้างตลกแบบสุ่มและข้อมูลสนุก ๆ จากหลาย API

## ✨ ฟีเจอร์

✅ ดึงตลกสุ่มจาก JokeAPI  
✅ ดึงข้อเท็จจริงสุ่มจาก Useless Facts API  
✅ ดึงคำถาม Trivia จาก Open Trivia Database  
✅ รองรับหลายหมวดหมู่ (General, Programming, Knock-Knock)  
✅ แสดงผลแบบ Interactive Menu  
✅ ดึงหลายตลกพร้อมกัน  

## 🌐 APIs ที่ใช้

### 1. **JokeAPI**
- URL: `https://official-joke-api.appspot.com`
- หมวดหมู่: General, Programming, Knock-Knock, K-POP
- ประเภท: Single joke หรือ Two-part joke

### 2. **Useless Facts API**
- URL: `https://uselessfacts.jsoup.com`
- ข้อมูลสุ่มที่สนุก ๆ

### 3. **Open Trivia Database**
- URL: `https://opentdb.com`
- คำถาม Trivia หลายระดับความยาก
- หมวดหมู่: Arts, Science, Sports, History, etc.

## 📦 Requirements

```
requests>=2.31.0
```

## 🚀 วิธีใช้งาน

### 1. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

### 2. รัน Generator

```bash
python joke_generator.py
```

### 3. เลือก Option

```
🎭 Random Joke Generator

1. Get Random Joke (General)
2. Get Programming Joke
3. Get Knock-Knock Joke
4. Get Random Fact
5. Get Trivia Question
6. Get Multiple Jokes
7. Exit

📌 Select option (1-7): 1
```

## 📋 ตัวอย่าง Output

### Random Joke
```
============================================================
📝 Source: JokeAPI
============================================================

😂 Why did the programmer quit his job?
Because he didn't get arrays.

📂 Category: General

============================================================
```

### Two-Part Joke
```
============================================================
📝 Source: JokeAPI
============================================================

🤔 Setup: Knock knock.

😄 Delivery: Who's there? Interrupting cow. Interrupting cow w—
MOOOO!

📂 Category: Knock-knock

============================================================
```

### Trivia Question
```
============================================================
📝 Source: Open Trivia Database
============================================================

❓ Question: What is the capital of France?
📚 Category: Geography
🎯 Difficulty: Easy

============================================================
```

## 🎨 Menu Options

| Option | Description |
|--------|-------------|
| 1 | ดึงตลกสุ่มแบบทั่วไป |
| 2 | ดึงตลกด้านการเขียนโปรแกรม |
| 3 | ดึง Knock-Knock Joke |
| 4 | ดึงข้อเท็จจริงสุ่ม |
| 5 | ดึงคำถาม Trivia |
| 6 | ดึงตลก 3 เรื่องพร้อมกัน |
| 7 | ออกจากโปรแกรม |

## 🛠️ การปรับแต่ง

### เพิ่ม API ใหม่

```python
def get_random_joke_custom(self) -> Optional[Dict]:
    """
    ดึงตลกจาก API ที่กำหนดเอง
    """
    try:
        url = "https://your-api.com/endpoint"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        return {
            'joke': data.get('joke_text'),
            'source': 'Custom API'
        }
    except Exception as e:
        print(f"Error: {e}")
    
    return None
```

### เพิ่มหมวดหมู่ใหม่

```python
# ในฟังก์ชัน main()
elif choice == "8":
    joke = generator.get_random_joke_jokeapi("your-category")
    generator.display_joke(joke)
```

## 📁 โครงสร้าง

```
joke-generator/
├── joke_generator.py
├── requirements.txt
└── README.md
```

## 🎯 ใช้งาน

- 😂 ตลกสำหรับเพื่อน ๆ
- 🧠 เรียนรู้ข้อมูลสนุก ๆ
- 📊 Quiz/Trivia Game
- 🤖 Bot Integration
- 📱 Social Media Content

## ⚠️ หมายเหตุ

- ต้องมีการเชื่อมต่ออินเทอร์เน็ต
- API อาจมีข้อจำกัดการเรียกใช้
- บางข้อมูลอาจเป็นภาษาอังกฤษ

## 👤 Creator

GitHub: [@otimzom-rgb](https://github.com/otimzom-rgb)

## 📄 License

MIT License
