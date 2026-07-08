import requests
import re
import json

queries = {
    'silver': ["Sterling Pendant", "Silver Chain Bracelet", "Eternity Silver Ring", "Silver Drop Earrings", "Minimalist Silver Choker"],
    'gold': ["Gold Plated Statement Ring", "Elegant Gold Drop Earrings", "24k Gold Chain", "Gold Solitaire Ring", "Vintage Gold Bangle"],
    'diamond': ["CZ Diamond Tennis Bracelet", "Solitaire Diamond Necklace", "Diamond Stud Earrings", "Diamond Halo Ring", "Luxury Diamond Choker"]
}

keywords = {
    "Sterling Pendant": "silver pendant tanishq",
    "Silver Chain Bracelet": "silver chain bracelet tanishq",
    "Eternity Silver Ring": "silver ring tanishq",
    "Silver Drop Earrings": "silver drop earrings tanishq",
    "Minimalist Silver Choker": "silver choker necklace kushals",
    
    "Gold Plated Statement Ring": "gold statement ring tanishq",
    "Elegant Gold Drop Earrings": "gold drop earrings tanishq",
    "24k Gold Chain": "gold chain necklace tanishq",
    "Gold Solitaire Ring": "gold solitaire ring tanishq",
    "Vintage Gold Bangle": "gold bangle tanishq",
    
    "CZ Diamond Tennis Bracelet": "diamond tennis bracelet tanishq",
    "Solitaire Diamond Necklace": "diamond solitaire necklace tanishq",
    "Diamond Stud Earrings": "diamond stud earrings tanishq",
    "Diamond Halo Ring": "diamond ring tanishq",
    "Luxury Diamond Choker": "diamond choker necklace kushals"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

products = []
global_images = set()

for category, names in queries.items():
    cat_products = 0
    for name in names:
        keyword = keywords[name]
        url = f"https://www.bing.com/images/search?q={keyword.replace(' ', '+')}"
        
        try:
            res = requests.get(url, headers=headers, timeout=10)
            imgs = re.findall(r'murl&quot;:&quot;(https?://[^&]+?)&quot;', res.text)
            
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
                    cat_products += 1
                    if added == 5:
                        break
                        
        except Exception as e:
            pass
            
    # Pad if we didn't hit 25 for this category
    while cat_products < 25:
        url = f"https://www.bing.com/images/search?q={category}+jewelry+tanishq"
        res = requests.get(url, headers=headers, timeout=10)
        imgs = re.findall(r'murl&quot;:&quot;(https?://[^&]+?)&quot;', res.text)
        
        for img_url in imgs:
             if img_url not in global_images and ('.jpg' in img_url or '.png' in img_url):
                 global_images.add(img_url)
                 import random
                 price = (random.randint(20, 70)) * 100 + 99
                 products.append({
                        "id": f"{category}-{len(products)}",
                        "name": f"{category.capitalize()} Collection Piece {cat_products+1}",
                        "category": category,
                        "price": f"{price:,}",
                        "image": img_url
                 })
                 cat_products += 1
                 if cat_products >= 25:
                     break

print(f"Total products generated: {len(products)}")

with open('catalog.json', 'w') as f:
    json.dump(products, f, indent=4)
