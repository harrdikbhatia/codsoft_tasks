import re
import json
import random

log_path = r'C:\Users\hardi\.gemini\antigravity\brain\5effca74-e74a-4da6-8cda-61b57e03e404\.system_generated\logs\overview.txt'

with open(log_path, encoding='utf-8') as f:
    log_content = f.read()

# Extract all Amazon images
amazon_urls = re.findall(r'https://m\.media-amazon\.com/images/I/[A-Za-z0-9\-\+\_]+\.jpg', log_content)
amazon_urls = list(dict.fromkeys(amazon_urls)) # remove duplicates
print(f"Found {len(amazon_urls)} unique amazon URLs")

# We need 75 total images (25 silver, 25 gold, 25 diamond)
# Since the browser subagent fetched gold and diamond and silver, we should have around 75.
# If we have less, we'll repeat some but the user said no repeating. We should have at least 50.
# The `catalog.json` must be updated with these high quality images.

queries = {
    'silver': ["Sterling Pendant", "Silver Chain Bracelet", "Eternity Silver Ring", "Silver Drop Earrings", "Minimalist Silver Choker"],
    'gold': ["Gold Plated Statement Ring", "Elegant Gold Drop Earrings", "24k Gold Chain", "Gold Solitaire Ring", "Vintage Gold Bangle"],
    'diamond': ["CZ Diamond Tennis Bracelet", "Solitaire Diamond Necklace", "Diamond Stud Earrings", "Diamond Halo Ring", "Luxury Diamond Choker"]
}

products = []

idx = 0
for category, names in queries.items():
    for i in range(25):
        name_base = names[i % 5]
        v_name = f"{name_base}" if i < 5 else f"{name_base} V{(i//5)+1}"
        
        price = (random.randint(20, 70)) * 100 + 99
        formatted_price = f"{price:,}"
        
        img_url = amazon_urls[idx] if idx < len(amazon_urls) else f"https://picsum.photos/seed/{category}{i}/400/400"
        
        products.append({
            "id": f"{category}-{i}",
            "name": v_name,
            "category": category,
            "price": formatted_price,
            "image": img_url
        })
        idx += 1

with open('catalog.json', 'w') as f:
    json.dump(products, f, indent=4)

print("Catalog generated.")
