import json
import re
import random

with open('images_data.json', 'r') as f:
    images_data = json.load(f)

# Filter out non-product images like icons
silver_images = [img for img in images_data['silver'] if 'wish_fill' not in img][:10]
gold_images = [img for img in images_data['gold'] if 'wish_fill' not in img][:10]
diamond_images = [img for img in images_data['diamond'] if 'wish_fill' not in img][:10]

silver_names = [
    "Sterling Silver Temple Ring",
    "Silver Ruby Temple Necklace",
    "Oxidised Silver Bangle",
    "Silver Temple Drop Pendant",
    "Antique Silver Temple Tikka",
    "Silver Green Stone Ring",
    "Silver Ruby Bangle Set",
    "Classic Silver Temple Necklace",
    "Silver Oxidised Tikka",
    "Elegant Silver Temple Ring"
]

gold_names = [
    "Victorian Gold Kundan Earring",
    "Gold Kundan White Earring",
    "Kundan Gold Kada",
    "Victorian Gold Kundan Necklace",
    "Kundan Gold Statement Ring",
    "Royal Gold Kundan Earring",
    "Gold Kundan Hair Brooch",
    "Elegant Gold Kundan Ring",
    "Kundan Ruby Gold Necklace",
    "Vintage Gold Kundan Kada"
]

diamond_names = [
    "Zircon Diamond Tennis Bracelet",
    "Diamond Zircon Drop Earring",
    "Zircon Diamond Choker Necklace",
    "Royal Diamond Zircon Bangle",
    "Zircon Diamond Solitaire Ring",
    "Elegant Zircon Diamond Tikka",
    "Zircon Diamond Ruby Nath",
    "White Gold Zircon Bracelet",
    "Diamond Zircon Stud Earring",
    "Rose Gold Zircon Bangle"
]

def generate_products(category, names, images, start_id):
    prods = []
    for i in range(10):
        # Generate a realistic price (2000 to 9999)
        price = (random.randint(20, 99)) * 100 + 99
        prods.append({
            "id": f"{category}-{start_id + i}",
            "name": names[i],
            "category": category,
            "price": f"{price:,}",
            "image": images[i]
        })
    return prods

all_products = []
all_products.extend(generate_products("silver", silver_names, silver_images, 0))
all_products.extend(generate_products("gold", gold_names, gold_images, 10))
all_products.extend(generate_products("diamond", diamond_names, diamond_images, 20))

products_json = json.dumps(all_products, indent=4)
new_js_code = f"window.products = {products_json};"

# Read script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Regex to find window.products = [ ... ];
# It matches from window.products = [ until the first ];
pattern = re.compile(r'window\.products\s*=\s*\[.*?\];', re.DOTALL)

if pattern.search(js):
    new_js = pattern.sub(new_js_code, js)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Successfully replaced window.products with 30 items.")
else:
    print("Could not find window.products array in script.js")
