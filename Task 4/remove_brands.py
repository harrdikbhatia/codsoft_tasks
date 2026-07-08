import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Words to remove
words_to_remove = ["Tanishq ", "GIVA ", "Swarovski ", "Pandora "]

for word in words_to_remove:
    js = js.replace(word, "")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Removed brand names from script.js")
