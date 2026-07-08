import requests
from bs4 import BeautifulSoup
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def get_giva_images():
    url = "https://www.giva.co/collections/silver-rings"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        if src and 'cdn' in src and ('.jpg' in src or '.webp' in src):
            if src.startswith('//'):
                src = 'https:' + src
            images.append(src)
    return list(set(images))

def get_tanishq_images():
    url = "https://www.tanishq.co.in/shop/gold-rings"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        if src and ('.jpg' in src or '.webp' in src):
            if src.startswith('//'):
                src = 'https:' + src
            images.append(src)
    return list(set(images))

def get_swarovski_images():
    url = "https://www.swarovski.com/en-US/c-0101/Categories/Jewelry/Bracelets/"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        if src and ('.jpg' in src or '.webp' in src) and 'swarovski' in src.lower():
            if src.startswith('//'):
                src = 'https:' + src
            images.append(src)
    return list(set(images))

results = {
    'giva': get_giva_images(),
    'tanishq': get_tanishq_images(),
    'swarovski': get_swarovski_images()
}

print(f"GIVA: {len(results['giva'])}")
print(f"Tanishq: {len(results['tanishq'])}")
print(f"Swarovski: {len(results['swarovski'])}")

with open('scraped_brands.json', 'w') as f:
    json.dump(results, f, indent=4)
