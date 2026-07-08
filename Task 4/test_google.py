import requests
import re

url = "https://www.google.com/search?tbm=isch&q=silver+pendant+jewelry"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
res = requests.get(url, headers=headers)
imgs = re.findall(r'(https://encrypted-tbn0\.gstatic\.com/images\?q=[^"]+)', res.text)
print(len(imgs), imgs[:2])
