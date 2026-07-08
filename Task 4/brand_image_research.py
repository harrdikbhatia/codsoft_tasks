import requests
import re
import json

def search_bing_images(query):
    url = f"https://www.bing.com/images/search?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=headers, timeout=10)
        imgs = re.findall(r'murl&quot;:&quot;(https?://[^&]+?)&quot;', res.text)
        return imgs[:5] # return top 5
    except Exception as e:
        print(f"Error for {query}: {e}")
        return []

queries = [
    "site:tanishq.co.in tanishq gold ring",
    "site:giva.co giva silver pendant",
    "site:swarovski.com swarovski diamond bracelet",
    "site:pandora.net pandora silver charm"
]

results = {}
for q in queries:
    results[q] = search_bing_images(q)
    print(f"Query: {q}")
    for img in results[q]:
        print(f" - {img}")

with open('research_results.json', 'w') as f:
    json.dump(results, f, indent=4)
