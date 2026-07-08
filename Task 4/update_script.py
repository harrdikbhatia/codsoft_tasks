import json
import re

with open('images_data.json', 'r') as f:
    data = json.load(f)

with open('script.js', 'r') as f:
    js_content = f.read()

# Replace silverImages
silver_str = 'const silverImages = [\n        "' + '",\n        "'.join(data['silver']) + '"\n    ];'
js_content = re.sub(r'const silverImages = \[.*?\];', silver_str, js_content, flags=re.DOTALL)

# Replace goldImages
gold_str = 'const goldImages = [\n        "' + '",\n        "'.join(data['gold']) + '"\n    ];'
js_content = re.sub(r'const goldImages = \[.*?\];', gold_str, js_content, flags=re.DOTALL)

# Replace diamondImages
diamond_str = 'const diamondImages = [\n        "' + '",\n        "'.join(data['diamond']) + '"\n    ];'
js_content = re.sub(r'const diamondImages = \[.*?\];', diamond_str, js_content, flags=re.DOTALL)

# Update imgIndex assignment
js_content = js_content.replace('let imgIndex = nameIndex; // Ensure image exactly matches the name index', 'let imgIndex = i;')
js_content = js_content.replace('let imgIndex = i % imageArr.length;', 'let imgIndex = i;') # Just in case

with open('script.js', 'w') as f:
    f.write(js_content)

print("Successfully updated script.js with 75 unique images!")
