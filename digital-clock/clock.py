#!/usr/bin/env python3
"""
Digital Clock - Multi Timezone Display
แอปพลิเคชันแสดงเวลาดิจิทัลแบบ Real-time สำหรับหลายโซนเวลาทั่วโลก
"""

import tkinter as tk
from tkinter import font as tkfont
import pytz
from datetime import datetime
import threading
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("🌍 Global Time Zones")
        self.root.geometry("1000x700")
        self.root.config(bg="#0f0f1e")
        
        # Timezones
        self.timezones = {
            "Bangkok 🇹🇭": "Asia/Bangkok",
            "Tokyo 🇯🇵": "Asia/Tokyo",
            "New York 🇺🇸": "America/New_York",
            "London 🇬🇧": "Europe/London",
            "Sydney 🇦🇺": "Australia/Sydney",
            "Dubai 🇦🇪": "Asia/Dubai",
            "Los Angeles 🇺🇸": "America/Los_Angeles",
            "Paris 🇫🇷": "Europe/Paris",
        }
        
        # Fonts
        self.title_font = tkfont.Font(family="Arial", size=20, weight="bold")
        self.time_font = tkfont.Font(family="Courier New", size=32, weight="bold")
        self.date_font = tkfont.Font(family="Arial", size=12)
        
        # Create UI
        self.create_ui()
        
        # Start update thread
        self.running = True
        self.update_thread = threading.Thread(target=self.update_time_thread, daemon=True)
        self.update_thread.start()
        
        # Close handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_ui(self):
        """Create UI elements"""
        # Title
        title = tk.Label(
            self.root,
            text="🌍 Global Time Zones",
            font=self.title_font,
            bg="#0f0f1e",
            fg="#00d4ff"
        )
        title.pack(pady=20)
        
        # Clock frames container
        container = tk.Frame(self.root, bg="#0f0f1e")
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create clock frames (2x4 grid)
        self.clock_frames = {}
        row, col = 0, 0
        for timezone_name in self.timezones.keys():
            frame = tk.Frame(
                container,
                bg="#1a1a2e",
                relief=tk.RAISED,
                bd=2
            )
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Timezone label
            tz_label = tk.Label(
                frame,
                text=timezone_name,
                font=("Arial", 12, "bold"),
                bg="#1a1a2e",
                fg="#00d4ff"
            )
            tz_label.pack(pady=10)
            
            # Time display
            time_label = tk.Label(
                frame,
                text="00:00:00",
                font=self.time_font,
                bg="#1a1a2e",
                fg="#00ff41"
            )
            time_label.pack()
            
            # Date display
            date_label = tk.Label(
                frame,
                text="0000-00-00",
                font=self.date_font,
                bg="#1a1a2e",
                fg="#ffd700"
            )
            date_label.pack(pady=10)
            
            self.clock_frames[timezone_name] = {
                "time_label": time_label,
                "date_label": date_label
            }
            
            col += 1
            if col == 2:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(row + 1):
            container.grid_rowconfigure(i, weight=1)
        for i in range(2):
            container.grid_columnconfigure(i, weight=1)
    
    def update_time_thread(self):
        """Update time in background thread"""
        while self.running:
            try:
                self.root.after(0, self.update_clocks)
                time.sleep(1)
            except:
                pass
    
    def update_clocks(self):
        """Update all clock displays"""
        for timezone_name, tz_str in self.timezones.items():
            tz = pytz.timezone(tz_str)
            now = datetime.now(tz)
            
            # Format time
            time_str = now.strftime("%H:%M:%S")
            date_str = now.strftime("%Y-%m-%d")
            
            # Update labels
            self.clock_frames[timezone_name]["time_label"].config(text=time_str)
            self.clock_frames[timezone_name]["date_label"].config(text=date_str)
    
    def on_closing(self):
        """Handle window close"""
        self.running = False
        self.root.destroy()

def main():
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
