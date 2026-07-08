import json

with open('images_data.json', 'r') as f:
    data = json.load(f)

html = "<html><body style='display:flex; flex-wrap:wrap;'>"
html += "<h1>Silver</h1><div style='display:flex; flex-wrap:wrap;'>"
for url in data['silver']:
    if 'wish_fill' not in url:
        html += f"<div style='margin:10px; border:1px solid #ccc;'><img src='{url}' width='200'><p style='font-size:10px;'>{url}</p></div>"
html += "</div><h1>Gold</h1><div style='display:flex; flex-wrap:wrap;'>"
for url in data['gold']:
    if 'wish_fill' not in url:
        html += f"<div style='margin:10px; border:1px solid #ccc;'><img src='{url}' width='200'><p style='font-size:10px;'>{url}</p></div>"
html += "</div><h1>Diamond</h1><div style='display:flex; flex-wrap:wrap;'>"
for url in data['diamond']:
    if 'wish_fill' not in url:
        html += f"<div style='margin:10px; border:1px solid #ccc;'><img src='{url}' width='200'><p style='font-size:10px;'>{url}</p></div>"
html += "</div></body></html>"

with open('image_gallery.html', 'w') as f:
    f.write(html)
print("Gallery created.")
