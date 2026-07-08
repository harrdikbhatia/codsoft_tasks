import requests
from bs4 import BeautifulSoup
import json
import re

queries = {
    'silver': ["Sterling Pendant", "Silver Chain Bracelet", "Eternity Silver Ring", "Silver Drop Earrings", "Minimalist Silver Choker"],
    'gold': ["Gold Plated Statement Ring", "Elegant Gold Drop Earrings", "24k Gold Chain", "Gold Solitaire Ring", "Vintage Gold Bangle"],
    'diamond': ["CZ Diamond Tennis Bracelet", "Solitaire Diamond Necklace", "Diamond Stud Earrings", "Diamond Halo Ring", "Luxury Diamond Choker"]
}

# Mapping names to search keywords to ensure high relevance
keywords = {
    "Sterling Pendant": "silver pendant",
    "Silver Chain Bracelet": "silver bracelet",
    "Eternity Silver Ring": "silver ring",
    "Silver Drop Earrings": "silver earrings",
    "Minimalist Silver Choker": "silver choker",
    
    "Gold Plated Statement Ring": "kundan ring",
    "Elegant Gold Drop Earrings": "kundan earrings",
    "24k Gold Chain": "kundan necklace",
    "Gold Solitaire Ring": "gold ring",
    "Vintage Gold Bangle": "kundan bangle",
    
    "CZ Diamond Tennis Bracelet": "zircon bracelet",
    "Solitaire Diamond Necklace": "zircon necklace",
    "Diamond Stud Earrings": "zircon earrings",
    "Diamond Halo Ring": "zircon ring",
    "Luxury Diamond Choker": "zircon choker"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

products = []
global_images = set()

for category, names in queries.items():
    for name in names:
        keyword = keywords[name]
        url = f"https://www.kushals.com/search?q={keyword.replace(' ', '+')}"
        print(f"Fetching {url}")
        
        try:
            res = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            imgs = []
            
            for img in soup.find_all('img'):
                src = img.get('src') or img.get('data-src')
                if src and 'cdn' in src and 'icon' not in src.lower() and 'logo' not in src.lower() and 'gif' not in src.lower():
                    if src.startswith('//'):
                        src = 'https:' + src
                    # Remove query params to avoid duplicates with different sizes if necessary, or just keep it
                    imgs.append(src)
            
            # Add 5 unique images
            added = 0
            for img_url in imgs:
                if img_url not in global_images:
                    global_images.add(img_url)
                    
                    # Create 5 variations of the name
                    import random
                    price = (random.randint(20, 70)) * 100 + 99
                    formatted_price = f"{price:,}"
                    
                    v_name = f"{name}" if added == 0 else f"{name} V{added+1}"
                    
                    products.append({
                        "id": f"{category}-{len(products)}",
                        "name": v_name,
                        "category": category,
                        "price": formatted_price,
                        "image": img_url
                    })
                    added += 1
                    if added == 5:
                        break
            
            if added < 5:
                print(f"WARNING: Only found {added} images for {name}")
                
        except Exception as e:
            print(f"Error for {name}: {e}")

print(f"Total products generated: {len(products)}")

with open('catalog.json', 'w') as f:
    json.dump(products, f, indent=4)
