#!/usr/bin/env python3
"""
Random Joke Generator
แอปพลิเคชันสำหรับสร้างตลกแบบสุ่มจาก API
"""

import requests
import json
from typing import Dict, Optional
import time

class JokeGenerator:
    """
    สร้างตลกแบบสุ่มจาก JokeAPI
    """
    
    def __init__(self):
        self.api_urls = {
            "jokeapi": "https://official-joke-api.appspot.com",
            "jokesdb": "https://jokesdb.p.rapidapi.com/joke",
        }
        self.headers = {
            'User-Agent': 'Random-Joke-Generator/1.0'
        }
    
    def get_random_joke_jokeapi(self, category: str = "general") -> Optional[Dict]:
        """
        ดึงตลกสุ่มจาก JokeAPI
        
        Categories: general, knock-knock, programming, kpop
        """
        try:
            if category == "random":
                url = f"{self.api_urls['jokeapi']}/jokes/random"
            else:
                url = f"{self.api_urls['jokeapi']}/jokes/{category}/random"
            
            response = requests.get(url, headers=self.headers, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('type') == 'single':
                return {
                    'joke': data.get('joke'),
                    'category': data.get('category', 'unknown'),
                    'source': 'JokeAPI'
                }
            elif data.get('type') == 'twopart':
                return {
                    'setup': data.get('setup'),
                    'delivery': data.get('delivery'),
                    'category': data.get('category', 'unknown'),
                    'source': 'JokeAPI'
                }
        except Exception as e:
            print(f"❌ Error fetching from JokeAPI: {e}")
        
        return None
    
    def get_random_joke_uselessfacts(self) -> Optional[Dict]:
        """
        ดึงข้อเท็จจริงสุ่มจาก Useless Facts API
        """
        try:
            url = "https://uselessfacts.jsoup.com/random.json"
            response = requests.get(url, headers=self.headers, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            return {
                'fact': data.get('text'),
                'category': 'fact',
                'source': 'Useless Facts API'
            }
        except Exception as e:
            print(f"❌ Error fetching from Useless Facts API: {e}")
        
        return None
    
    def get_random_joke_trivia(self) -> Optional[Dict]:
        """
        ดึงคำถาม Trivia สุ่มจาก Open Trivia Database
        """
        try:
            url = "https://opentdb.com/api.php?amount=1"
            response = requests.get(url, headers=self.headers, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            if data.get('results'):
                question = data['results'][0]
                return {
                    'question': question.get('question'),
                    'category': question.get('category'),
                    'difficulty': question.get('difficulty'),
                    'type': 'trivia',
                    'source': 'Open Trivia Database'
                }
        except Exception as e:
            print(f"❌ Error fetching from Trivia API: {e}")
        
        return None
    
    def display_joke(self, joke: Dict) -> None:
        """
        แสดงตลกในรูปแบบสวยงาม
        """
        if not joke:
            print("❌ ไม่สามารถดึงตลกได้")
            return
        
        source = joke.get('source', 'Unknown')
        print("\n" + "="*60)
        print(f"📝 Source: {source}")
        print("="*60)
        
        if 'joke' in joke:
            print(f"\n😂 {joke['joke']}")
        
        if 'setup' in joke:
            print(f"\n🤔 Setup: {joke['setup']}")
            print(f"\n😄 Delivery: {joke['delivery']}")
        
        if 'fact' in joke:
            print(f"\n💡 Fact: {joke['fact']}")
        
        if 'question' in joke:
            print(f"\n❓ Question: {joke['question']}")
            print(f"📚 Category: {joke.get('category', 'Unknown')}")
            print(f"🎯 Difficulty: {joke.get('difficulty', 'Unknown')}")
        
        if 'category' in joke:
            print(f"\n📂 Category: {joke['category']}")
        
        print("\n" + "="*60)

def main():
    """
    Main function
    """
    generator = JokeGenerator()
    
    print("\n🎭 Random Joke Generator")
    print("="*60)
    print("\n1. Get Random Joke (General)")
    print("2. Get Programming Joke")
    print("3. Get Knock-Knock Joke")
    print("4. Get Random Fact")
    print("5. Get Trivia Question")
    print("6. Get Multiple Jokes")
    print("7. Exit")
    print("\n" + "="*60)
    
    while True:
        choice = input("\n📌 Select option (1-7): ").strip()
        
        if choice == "1":
            joke = generator.get_random_joke_jokeapi("random")
            generator.display_joke(joke)
        
        elif choice == "2":
            joke = generator.get_random_joke_jokeapi("programming")
            generator.display_joke(joke)
        
        elif choice == "3":
            joke = generator.get_random_joke_jokeapi("knock-knock")
            generator.display_joke(joke)
        
        elif choice == "4":
            fact = generator.get_random_joke_uselessfacts()
            generator.display_joke(fact)
        
        elif choice == "5":
            trivia = generator.get_random_joke_trivia()
            generator.display_joke(trivia)
        
        elif choice == "6":
            print("\n🎲 Getting Multiple Jokes...\n")
            jokes = [
                generator.get_random_joke_jokeapi("random"),
                generator.get_random_joke_uselessfacts(),
                generator.get_random_joke_trivia()
            ]
            for i, joke in enumerate(jokes, 1):
                print(f"\n\n🔹 Joke #{i}")
                generator.display_joke(joke)
                time.sleep(1)
        
        elif choice == "7":
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
