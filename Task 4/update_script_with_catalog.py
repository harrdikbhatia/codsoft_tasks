import json
import re

with open('catalog.json', 'r') as f:
    products = json.load(f)

with open('script.js', 'r') as f:
    js_content = f.read()

# Find `const products = [`
start_idx = js_content.find('const products = [')
# Find the end of the generation block
end_marker = "    // ==========================================\n    // Product Rendering & Filtering (Homepage)\n    // =========================================="
end_idx = js_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_products_js = f"const products = {json.dumps(products, indent=4)};\n\n"
    new_content = js_content[:start_idx] + new_products_js + js_content[end_idx:]
    
    with open('script.js', 'w') as f:
        f.write(new_content)
    print("Successfully replaced products array in script.js")
else:
    print("Could not find start or end markers")
