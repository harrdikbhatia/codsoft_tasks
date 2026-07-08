import requests
from bs4 import BeautifulSoup
import re
import json

def get_images(url, keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        images = []
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src')
            if src and ('.jpg' in src or '.png' in src or '.webp' in src) and 'cdn' in src:
                if src.startswith('//'):
                    src = 'https:' + src
                images.append(src)
        
        # Make unique and remove small icons
        unique_images = list(set([img for img in images if 'icon' not in img.lower()]))
        return unique_images[:25]
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

silver = get_images("https://www.kushals.com/collections/silver-jewellery", "silver")
gold = get_images("https://www.kushals.com/collections/kundan-jewellery", "gold")
diamond = get_images("https://www.kushals.com/collections/zircon-jewellery", "diamond")

with open('images_data.json', 'w') as f:
    json.dump({'silver': silver, 'gold': gold, 'diamond': diamond}, f)

print(f"Fetched {len(silver)} silver, {len(gold)} gold, {len(diamond)} diamond images.")
