#!/usr/bin/env python3
"""
Video Downloader
ดาวน์โหลดวิดีโอจาก YouTube, TikTok, Instagram
"""

import os
import sys
from pathlib import Path
from typing import Optional, Dict

try:
    import yt_dlp
except ImportError:
    print("❌ yt-dlp not installed. Installing...")
    os.system("pip install yt-dlp")
    import yt_dlp

class VideoDownloader:
    """
    ดาวน์โหลดวิดีโอจาก YouTube, TikTok, Instagram
    """
    
    def __init__(self, output_path: str = "downloads"):
        self.output_path = output_path
        self.create_output_dir()
        
        self.ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
            'socket_timeout': 30,
            'retries': 3,
        }
    
    def create_output_dir(self) -> None:
        """
        สร้างโฟลเดอร์ output
        """
        Path(self.output_path).mkdir(parents=True, exist_ok=True)
        print(f"✅ Output folder: {os.path.abspath(self.output_path)}")
    
    def download_video(self, url: str, quality: str = "best") -> bool:
        """
        ดาวน์โหลดวิดีโอ
        
        quality: 'best', 'high', 'medium', 'low'
        """
        if not self._validate_url(url):
            print(f"❌ Invalid URL: {url}")
            return False
        
        try:
            print(f"\n🎬 Downloading from: {url}")
            print(f"📊 Quality: {quality}")
            print("\n" + "="*60)
            
            # Set quality
            opts = self.ydl_opts.copy()
            if quality == "high":
                opts['format'] = 'bestvideo[height<=1080][ext=mp4]/best[ext=mp4]/best'
            elif quality == "medium":
                opts['format'] = 'bestvideo[height<=720][ext=mp4]/best[ext=mp4]/best'
            elif quality == "low":
                opts['format'] = 'bestvideo[height<=480][ext=mp4]/best[ext=mp4]/best'
            else:
                opts['format'] = 'best[ext=mp4]/best'
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                filepath = os.path.join(self.output_path, os.path.basename(filename))
                
                print("\n" + "="*60)
                print(f"✅ Downloaded successfully!")
                print(f"📁 File: {os.path.basename(filename)}")
                print(f"📊 Size: {self._get_file_size(filepath)}")
                print(f"📍 Location: {os.path.abspath(filepath)}")
                print("="*60)
                return True
        
        except Exception as e:
            print(f"\n❌ Error downloading video: {e}")
            print("="*60)
            return False
    
    def download_playlist(self, url: str, quality: str = "best") -> bool:
        """
        ดาวน์โหลด Playlist
        """
        if not self._validate_url(url):
            print(f"❌ Invalid URL: {url}")
            return False
        
        try:
            print(f"\n📋 Downloading playlist from: {url}")
            print(f"📊 Quality: {quality}")
            print("\n" + "="*60)
            
            # Set quality
            opts = self.ydl_opts.copy()
            opts['outtmpl'] = os.path.join(self.output_path, '%(playlist)s/%(title)s.%(ext)s')
            
            if quality == "high":
                opts['format'] = 'bestvideo[height<=1080][ext=mp4]/best[ext=mp4]/best'
            elif quality == "medium":
                opts['format'] = 'bestvideo[height<=720][ext=mp4]/best[ext=mp4]/best'
            elif quality == "low":
                opts['format'] = 'bestvideo[height<=480][ext=mp4]/best[ext=mp4]/best'
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                playlist_name = info.get('title', 'playlist')
                total_videos = len(info.get('entries', []))
                
                print("\n" + "="*60)
                print(f"✅ Playlist downloaded successfully!")
                print(f"📋 Playlist: {playlist_name}")
                print(f"🎬 Total videos: {total_videos}")
                print(f"📍 Location: {os.path.abspath(self.output_path)}")
                print("="*60)
                return True
        
        except Exception as e:
            print(f"\n❌ Error downloading playlist: {e}")
            print("="*60)
            return False
    
    def download_audio(self, url: str) -> bool:
        """
        ดาวน์โหลดแค่เสียง (MP3)
        """
        if not self._validate_url(url):
            print(f"❌ Invalid URL: {url}")
            return False
        
        try:
            audio_path = os.path.join(self.output_path, "audio")
            Path(audio_path).mkdir(parents=True, exist_ok=True)
            
            print(f"\n🎵 Downloading audio from: {url}")
            print("\n" + "="*60)
            
            opts = self.ydl_opts.copy()
            opts['format'] = 'bestaudio/best'
            opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
            opts['outtmpl'] = os.path.join(audio_path, '%(title)s.%(ext)s')
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = info.get('title', 'audio')
                
                print("\n" + "="*60)
                print(f"✅ Audio extracted successfully!")
                print(f"🎵 File: {filename}.mp3")
                print(f"📍 Location: {os.path.abspath(audio_path)}")
                print("="*60)
                return True
        
        except Exception as e:
            print(f"\n❌ Error downloading audio: {e}")
            print("="*60)
            return False
    
    def get_video_info(self, url: str) -> Optional[Dict]:
        """
        ดึงข้อมูลวิดีโอ
        """
        if not self._validate_url(url):
            print(f"❌ Invalid URL: {url}")
            return None
        
        try:
            print(f"\n📊 Getting video info from: {url}")
            print("\n" + "="*60)
            
            with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                
                video_info = {
                    'title': info.get('title'),
                    'duration': self._format_duration(info.get('duration')),
                    'uploader': info.get('uploader'),
                    'views': info.get('view_count'),
                    'likes': info.get('like_count'),
                    'upload_date': info.get('upload_date'),
                    'description': info.get('description', '')[:100] + '...',
                }
                
                print(f"📺 Title: {video_info['title']}")
                print(f"⏱️  Duration: {video_info['duration']}")
                print(f"👤 Uploader: {video_info['uploader']}")
                print(f"👁️  Views: {video_info['views']:,}")
                print(f"❤️  Likes: {video_info['likes'] or 'N/A'}")
                print(f"📅 Uploaded: {video_info['upload_date']}")
                print("="*60)
                
                return video_info
        
        except Exception as e:
            print(f"❌ Error getting video info: {e}")
            return None
    
    @staticmethod
    def _validate_url(url: str) -> bool:
        """
        ตรวจสอบ URL
        """
        valid_domains = ['youtube.com', 'youtu.be', 'tiktok.com', 'instagram.com', 'twitch.tv']
        return any(domain in url for domain in valid_domains)
    
    @staticmethod
    def _format_duration(seconds: int) -> str:
        """
        แปลงเวลา (วินาที) เป็น HH:MM:SS
        """
        if not seconds:
            return "N/A"
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        if hours > 0:
            return f"{hours}:{minutes:02d}:{secs:02d}"
        return f"{minutes}:{secs:02d}"
    
    @staticmethod
    def _get_file_size(filepath: str) -> str:
        """
        ดึงขนาดไฟล์
        """
        try:
            size_bytes = os.path.getsize(filepath)
            for unit in ['B', 'KB', 'MB', 'GB']:
                if size_bytes < 1024:
                    return f"{size_bytes:.2f} {unit}"
                size_bytes /= 1024
            return f"{size_bytes:.2f} TB"
        except:
            return "N/A"

def main():
    """
    Main function
    """
    downloader = VideoDownloader()
    
    print("\n📥 Video Downloader")
    print("="*60)
    print("\n1. Download Video")
    print("2. Download Playlist")
    print("3. Download Audio (MP3)")
    print("4. Get Video Info")
    print("5. Exit")
    print("\n" + "="*60)
    
    while True:
        choice = input("\n📌 Select option (1-5): ").strip()
        
        if choice == "1":
            url = input("\n🔗 Enter video URL: ").strip()
            if url:
                print("\nQuality options:")
                print("  1. Best (auto)")
                print("  2. High (1080p)")
                print("  3. Medium (720p)")
                print("  4. Low (480p)")
                quality_choice = input("\n📊 Select quality (1-4): ").strip()
                
                quality_map = {"1": "best", "2": "high", "3": "medium", "4": "low"}
                quality = quality_map.get(quality_choice, "best")
                
                downloader.download_video(url, quality)
        
        elif choice == "2":
            url = input("\n🔗 Enter playlist URL: ").strip()
            if url:
                quality_choice = input("\n📊 Select quality (1-4): ").strip()
                quality_map = {"1": "best", "2": "high", "3": "medium", "4": "low"}
                quality = quality_map.get(quality_choice, "best")
                downloader.download_playlist(url, quality)
        
        elif choice == "3":
            url = input("\n🔗 Enter video URL: ").strip()
            if url:
                downloader.download_audio(url)
        
        elif choice == "4":
            url = input("\n🔗 Enter video URL: ").strip()
            if url:
                downloader.get_video_info(url)
        
        elif choice == "5":
            print("\n👋 Goodbye!\n")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user.\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
