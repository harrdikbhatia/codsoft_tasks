import requests
import re
import json
import random

queries = {
    'silver': [
        "925 Silver Anushka Pendant",
        "Silver Zircon Chain Bracelet",
        "Moments Snake Chain Bracelet",
        "Sparkling Silver Drop Earrings",
        "Antique Silver Choker",
        "Vintage Silver Ring",
        "Oxidised Silver Bangle",
        "Classic Silver Charm Necklace",
        "Elegant Silver Tikka",
        "Signature Silver Ring"
    ],
    'gold': [
        "22k Gold Wedding Jhumkas",
        "Traditional Gold Choker",
        "Kundan Gold Kada",
        "Royal Gold Drop Earrings",
        "Gold Statement Ring",
        "Vintage Gold Bangle Set",
        "Bridal Gold Necklace",
        "Elegant Gold Hair Brooch",
        "Classic Kundan Ring",
        "24k Gold Solitaire Ring"
    ],
    'diamond': [
        "Infinity Crystal Bangle",
        "Solitaire Drop Earrings",
        "Crystal Tennis Bracelet",
        "Diamond Choker Necklace",
        "Zircon Solitaire Ring",
        "Elegant Crystal Tikka",
        "Ruby Diamond Nath",
        "White Gold Zircon Bracelet",
        "Sparkle Stud Earrings",
        "Rose Gold Crystal Bangle"
    ]
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

products = []
global_images = set()

for category, names in queries.items():
    start_id = 0 if category == 'silver' else (10 if category == 'gold' else 20)
    for i, name in enumerate(names):
        # Add strict modifiers to avoid models and get product-only shots
        keyword = f"{name} jewelry isolated white background product shot -model -person -woman"
        url = f"https://www.bing.com/images/search?q={keyword.replace(' ', '+')}"
        
        try:
            res = requests.get(url, headers=headers, timeout=10)
            imgs = re.findall(r'murl&quot;:&quot;(https?://[^&]+?)&quot;', res.text)
            
            found_img = None
            for img_url in imgs:
                if img_url not in global_images and ('.jpg' in img_url or '.png' in img_url or '.jpeg' in img_url):
                    global_images.add(img_url)
                    found_img = img_url
                    break
                    
            if not found_img:
                # Fallback generic query
                keyword = f"{category} jewelry isolated white background"
                url = f"https://www.bing.com/images/search?q={keyword.replace(' ', '+')}"
                res = requests.get(url, headers=headers, timeout=10)
                imgs = re.findall(r'murl&quot;:&quot;(https?://[^&]+?)&quot;', res.text)
                for img_url in imgs:
                    if img_url not in global_images and ('.jpg' in img_url or '.png' in img_url or '.jpeg' in img_url):
                        global_images.add(img_url)
                        found_img = img_url
                        break
            
            if not found_img:
                found_img = "https://via.placeholder.com/640x640.png?text=Jewelry" # Extreme fallback
                
            price = (random.randint(20, 99)) * 100 + 99
            
            products.append({
                "id": f"{category}-{start_id + i}",
                "name": name,
                "category": category,
                "price": f"{price:,}",
                "image": found_img
            })
                        
        except Exception as e:
            print(f"Error for {name}: {e}")

products_json = json.dumps(products, indent=4)
new_js_code = f"window.products = {products_json};"

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

pattern = re.compile(r'window\.products\s*=\s*\[.*?\];', re.DOTALL)
if pattern.search(js):
    new_js = pattern.sub(new_js_code, js)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Successfully replaced window.products with clean, model-free images.")
else:
    print("Could not find window.products array in script.js")
