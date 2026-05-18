"""
สร้างหนังสั้น Motion Graphics ละครคุณธรรม "ความสำคัญของการศึกษา"
Platform: TikTok / Instagram Reels (9:16)
ขนาด: 1-2 นาที
"""

from moviepy.editor import (
    TextClip, CompositeVideoClip, ColorClip
)
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# ====== ตั้งค่า ======
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 24
OUTPUT_FILE = "education_shorts.mp4"

# ====== ฉากข้อมูล ======
SCENES = [
    {
        "duration": 5,
        "bg_color": (135, 206, 235),  # Sky blue
        "text": ["🌅 ตอนเช้า บ้านธรรมดา", "", "ลูก: 'ทำไมต้องไปโรงเรียนล่ะ หนูเบื่ออ่า'"],
        "text_size": 50,
        "emoji": "🌅"
    },
    {
        "duration": 10,
        "bg_color": (255, 250, 205),  # Light yellow
        "text": ["📚 แม่กับลูกนั่งลง", "", "แม่: 'การศึกษาคือรากฐาน", "ของชีวิตที่ดี'"],
        "text_size": 48,
        "emoji": "📚"
    },
    {
        "duration": 10,
        "bg_color": (230, 230, 250),  # Lavender
        "text": ["✨ เรื่องที่แม่จำได้", "", "แม่: 'ครูของแม่เปลี่ยนชีวิต'", "แม่มีชีวิตที่ดีวันนี้"],
        "text_size": 48,
        "emoji": "✨"
    },
    {
        "duration": 10,
        "bg_color": (144, 238, 144),  # Light green
        "text": ["💡 ลูกรู้สึกตัว", "", "ลูก: 'ลูกจะเรียนให้ดี!", "เพื่ออนาคตที่สดใส'"],
        "text_size": 48,
        "emoji": "💡"
    },
    {
        "duration": 15,
        "bg_color": (255, 182, 193),  # Light pink
        "text": ["🌟 บทสรุป", "", "การศึกษา = ชีวิตที่ดี", "📚✨ 'เรียนให้ดี เพื่ออนาคต'"],
        "text_size": 52,
        "emoji": "🌟"
    }
]

def create_motion_graphics_video(output_file=OUTPUT_FILE):
    """
    สร้างวิดีโอ Motion Graphics ละครคุณธรรม
    """
    print("🎬 เริ่มสร้างวิดีโอ Motion Graphics...")
    
    all_clips = []
    current_time = 0
    
    # ===== สร้างแต่ละฉาก =====
    for i, scene in enumerate(SCENES):
        print(f"  🎨 สร้างฉาก {i+1}/{len(SCENES)}...")
        
        # สร้าง color clip เป็นพื้นหลัง
        color_clip = ColorClip(size=(VIDEO_WIDTH, VIDEO_HEIGHT), color=scene["bg_color"])
        color_clip = color_clip.set_duration(scene["duration"])
        color_clip = color_clip.set_start(current_time)
        all_clips.append(color_clip)
        
        # เพิ่ม Emoji ที่ด้านบน
        emoji = scene.get("emoji", "")
        if emoji:
            emoji_clip = TextClip(
                emoji,
                fontsize=80,
                color='white',
                method='caption'
            )
            emoji_clip = emoji_clip.set_duration(scene["duration"])
            emoji_clip = emoji_clip.set_position(('center', VIDEO_HEIGHT // 8))
            emoji_clip = emoji_clip.set_start(current_time)
            all_clips.append(emoji_clip)
        
        # เพิ่มข้อความ
        y_pos = VIDEO_HEIGHT // 3
        for line in scene["text"]:
            if line:
                txt_clip = TextClip(
                    line,
                    fontsize=scene.get("text_size", 50),
                    color='white',
                    font='Arial-Bold',
                    method='caption',
                    size=(VIDEO_WIDTH - 100, None),
                    align='center',
                    stroke_color='black',
                    stroke_width=2
                )
                txt_clip = txt_clip.set_duration(scene["duration"])
                txt_clip = txt_clip.set_position(('center', y_pos))
                txt_clip = txt_clip.set_start(current_time)
                all_clips.append(txt_clip)
                y_pos += 120
            else:
                y_pos += 40
        
        current_time += scene["duration"]
    
    # ===== สร้าง final video =====
    print(f"  💾 กำลังประมวลผล...")
    final_video = CompositeVideoClip(all_clips, size=(VIDEO_WIDTH, VIDEO_HEIGHT))
    
    # ===== บันทึกไฟล์ =====
    print(f"  📝 บันทึกไฟล์: {output_file}")
    final_video.write_videofile(
        output_file,
        fps=FPS,
        codec='libx264',
        audio=False,
        verbose=False,
        logger=None
    )
    
    print(f"✅ เสร็จสิ้น! บันทึกเป็น: {output_file}")
    print(f"⏱️  ความยาว: {sum(s['duration'] for s in SCENES)} วินาที")
    print(f"📱 พร้อมลง TikTok/Instagram Reels (9:16)")

# ====== ใช้งาน ======
if __name__ == "__main__":
    create_motion_graphics_video()
