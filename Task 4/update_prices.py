import re
import random

random.seed(42) # For reproducible results

def new_price(match):
    cat = match.group(1)
    if cat == 'silver':
        # Silver: 5,000 to 25,000
        p = random.randint(5, 25) * 1000 + random.randint(0, 9) * 100 + 99
    elif cat == 'gold':
        # Gold: 35,000 to 180,000
        p = random.randint(35, 180) * 1000 + random.randint(0, 9) * 100 + 99
    elif cat == 'diamond':
        # Diamond: 75,000 to 450,000
        p = random.randint(75, 450) * 1000 + random.randint(0, 9) * 100 + 99
    else:
        p = random.randint(1, 5) * 1000 + 99
    
    # Format with commas (Indian numbering format if possible, but standard commas are fine too. E.g. 1,50,000)
    # Python's {:,} does western style (150,000), which is acceptable.
    # Let's write a simple indian comma formatter:
    s = str(p)
    if len(s) > 3:
        last_3 = s[-3:]
        rest = s[:-3]
        # split rest into chunks of 2 from right to left
        chunks = []
        while len(rest) > 2:
            chunks.append(rest[-2:])
            rest = rest[:-2]
        if rest:
            chunks.append(rest)
        chunks.reverse()
        p_str = ",".join(chunks) + "," + last_3
    else:
        p_str = s

    return f'"category": "{cat}",\n        "price": "{p_str}",'

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'"category":\s*"([^"]+)",\n\s*"price":\s*"[^"]+",'
new_text = re.sub(pattern, new_price, text)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated prices in script.js")
