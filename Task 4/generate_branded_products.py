import json
import re
import random

with open('images_data.json', 'r') as f:
    images_data = json.load(f)

silver_images = [
    "https://www.kushals.com/cdn/shop/files/temple-necklace-ruby-green-gold-silver-temple-necklace-191815-1212890837.jpg?v=1766486329&width=1024",
    "https://www.kushals.com/cdn/shop/files/temple-finger-ring-white-gold-silver-temple-finger-ring-190556-1211744524.jpg?v=1766206132&width=1024",
    "https://www.kushals.com/cdn/shop/files/temple-bangle-ruby-oxidised-gold-silver-temple-bangle-pendant-180474-40557629440156.jpg?v=1735954829&width=1024",
    "https://www.kushals.com/cdn/shop/files/temple-pendant-ruby-gold-silver-temple-pendant-190591-1213043783.jpg?v=1766591906&width=640",
    "https://www.kushals.com/cdn/shop/files/temple-pendant-ruby-gold-silver-temple-pendant-190591-1213043784.jpg?v=1766591985&width=1024",
    "https://www.kushals.com/cdn/shop/files/temple-tikka-silver-temple-tikka-172580-1128066156.jpg?v=1739032468&width=1024",
    "https://www.kushals.com/cdn/shop/files/temple-tikka-silver-temple-tikka-188191-1231097945.jpg?v=1775232935&width=640",
    "https://www.kushals.com/cdn/shop/files/temple-finger-ring-green-oxidised-gold-silver-temple-finger-ring-178146-40516464803996.jpg?v=1735265615&width=640",
    "https://www.kushals.com/cdn/shop/files/temple-finger-ring-silver-temple-finger-ring-188186-1231097970.jpg?v=1775233126&width=640",
    "https://www.kushals.com/cdn/shop/files/temple-pendant-ruby-green-gold-silver-temple-pendant-190587-1213043787.jpg?v=1766592026&width=1024"
]

gold_images = [
    "https://www.kushals.com/cdn/shop/files/kundan-earring-kundan-earring-196768-1231172265.jpg?v=1775337635&width=1024",
    "https://www.kushals.com/cdn/shop/files/kundan-earring-white-victorian-kundan-earring-196878-1231172207.jpg?v=1775341373&width=1024",
    "https://www.kushals.com/cdn/shop/files/kundan-kada-white-victorian-kundan-kada-196792-1231172226.jpg?v=1775333828&width=640",
    "https://www.kushals.com/cdn/shop/files/kundan-finger-ring-white-victorian-kundan-finger-ring-196894-1231172165.jpg?v=1775342024&width=1024",
    "https://www.kushals.com/cdn/shop/files/kundan-finger-ring-kundan-finger-ring-196786-1231172243.jpg?v=1775337081&width=1024",
    "https://www.kushals.com/cdn/shop/files/kundan-finger-ring-white-victorian-kundan-finger-ring-196892-1231172175.jpg?v=1775342315&width=1024",
    "https://www.kushals.com/cdn/shop/files/kundan-finger-ring-white-victorian-kundan-finger-ring-196894-1231172165.jpg?v=1775342024&width=640",
    "https://www.kushals.com/cdn/shop/files/kundan-earring-kundan-earring-196768-1231172264.jpg?v=1775337644&width=1024",
    "https://www.kushals.com/cdn/shop/files/kundan-earring-white-victorian-kundan-earring-196874-1225077148.jpg?v=1772714006&width=1024",
    "https://www.kushals.com/cdn/shop/files/kundan-necklace-ruby-victorian-kundan-necklace-196764-1219326085.jpg?v=1770223722&width=1024"
]

diamond_images = [
    "https://www.kushals.com/cdn/shop/files/zircon-bracelet-zircon-bracelet-191931-1210585443.jpg?v=1765316107&width=640",
    "https://www.kushals.com/cdn/shop/files/zircon-earring-zircon-earring-187648-1195524388.jpg?v=1759245787&width=1024",
    "https://www.kushals.com/cdn/shop/files/zircon-necklace-zircon-necklace-193109-1219322237.jpg?v=1770240628&width=1024",
    "https://www.kushals.com/cdn/shop/files/zircon-bangle-zircon-bangle-196783-1219326028.jpg?v=1770220369&width=1024",
    "https://www.kushals.com/cdn/shop/files/zircon-finger-ring-zircon-finger-ring-193894-1227479673.jpg?v=1773743986&width=640",
    "https://www.kushals.com/cdn/shop/files/zircon-bangle-white-rose-gold-2-4-zircon-bangle-193933-1219322085.jpg?v=1770233385&width=1024",
    "https://www.kushals.com/cdn/shop/files/zircon-tikka-zircon-tikka-191102-1210585582.jpg?v=1765311413&width=1024",
    "https://www.kushals.com/cdn/shop/files/zircon-finger-ring-ruby-rodium-gold-zircon-finger-ring-185596-1244661354.jpg?v=1781629486&width=640",
    "https://www.kushals.com/cdn/shop/files/zircon-earring-sapphire-gold-zircon-earring-136753-37206969319580.jpg?v=1721895212&width=640",
    "https://www.kushals.com/cdn/shop/files/zircon-bracelet-zircon-bracelet-162529-1193747551.jpg?v=1758296691&width=1024"
]

silver_names = [
    "Classic Silver Charm Necklace",
    "Vintage Silver Ring",
    "Oxidised Silver Bangle",
    "925 Silver Anushka Pendant",
    "Antique Silver Choker",
    "Elegant Silver Tikka",
    "Traditional Silver Tikka",
    "Signature Silver Ring",
    "Sparkling Silver Ring",
    "Ruby Green Silver Pendant"
]

gold_names = [
    "Royal Gold Drop Earrings",
    "Classic Kundan Earrings",
    "Kundan Gold Kada",
    "Gold Statement Ring",
    "Elegant Kundan Ring",
    "Vintage Gold Ring",
    "24k Gold Solitaire Ring",
    "Traditional Gold Jhumkas",
    "Bridal Gold Earrings",
    "Bridal Gold Necklace"
]

diamond_names = [
    "Crystal Tennis Bracelet",
    "Solitaire Drop Earrings",
    "Diamond Choker Necklace",
    "Infinity Crystal Bangle",
    "Zircon Solitaire Ring",
    "Rose Gold Crystal Bangle",
    "Elegant Crystal Tikka",
    "Ruby Diamond Ring",
    "Sparkle Stud Earrings",
    "White Gold Zircon Bracelet"
]

def generate_products(category, names, images, start_id):
    prods = []
    for i in range(10):
        if category == 'silver':
            price = random.randint(500, 1000)
        elif category == 'gold':
            price = random.randint(1000, 1800)
        else: # diamond
            price = random.randint(2000, 3000)
            
        prods.append({
            "id": f"{category}-{start_id + i}",
            "name": names[i],
            "category": category,
            "price": f"{price:,}",
            "image": images[i],
            "isNew": i < 2  # first two products in each category get New Arrival flag
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
    print("Successfully replaced window.products with 30 BRANDED items.")
else:
    print("Could not find window.products array in script.js")
