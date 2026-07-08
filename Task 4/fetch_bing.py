import requests
import re
import json

queries = {
    'silver': ["Sterling Pendant", "Silver Chain Bracelet", "Eternity Silver Ring", "Silver Drop Earrings", "Minimalist Silver Choker"],
    'gold': ["Gold Plated Statement Ring", "Elegant Gold Drop Earrings", "24k Gold Chain", "Gold Solitaire Ring", "Vintage Gold Bangle"],
    'diamond': ["CZ Diamond Tennis Bracelet", "Solitaire Diamond Necklace", "Diamond Stud Earrings", "Diamond Halo Ring", "Luxury Diamond Choker"]
}

keywords = {
    "Sterling Pendant": "silver pendant necklace jewelry isolated",
    "Silver Chain Bracelet": "silver chain bracelet jewelry isolated",
    "Eternity Silver Ring": "silver eternity ring jewelry isolated",
    "Silver Drop Earrings": "silver drop earrings jewelry isolated",
    "Minimalist Silver Choker": "silver choker necklace jewelry isolated",
    
    "Gold Plated Statement Ring": "gold statement ring jewelry isolated",
    "Elegant Gold Drop Earrings": "gold drop earrings jewelry isolated",
    "24k Gold Chain": "gold chain necklace jewelry isolated",
    "Gold Solitaire Ring": "gold solitaire ring jewelry isolated",
    "Vintage Gold Bangle": "gold bangle jewelry isolated",
    
    "CZ Diamond Tennis Bracelet": "diamond tennis bracelet jewelry isolated",
    "Solitaire Diamond Necklace": "diamond solitaire necklace jewelry isolated",
    "Diamond Stud Earrings": "diamond stud earrings jewelry isolated",
    "Diamond Halo Ring": "diamond halo ring jewelry isolated",
    "Luxury Diamond Choker": "diamond choker necklace jewelry isolated"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

products = []
global_images = set()

for category, names in queries.items():
    for name in names:
        keyword = keywords[name]
        url = f"https://www.bing.com/images/search?q={keyword.replace(' ', '+')}"
        print(f"Fetching {url}")
        
        try:
            res = requests.get(url, headers=headers, timeout=10)
            imgs = re.findall(r'murl&quot;:&quot;(https?://[^&]+?)&quot;', res.text)
            
            # Add 5 unique images
            added = 0
            for img_url in imgs:
                if img_url not in global_images and ('.jpg' in img_url or '.png' in img_url or '.jpeg' in img_url):
                    global_images.add(img_url)
                    
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
