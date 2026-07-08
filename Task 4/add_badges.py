import re

# Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = '<img src="${product.image}" alt="${product.name}" loading="lazy">'
replacement = '${product.isNew ? \'<span class="new-badge">New Arrival</span>\' : \'\'}\n                        <img src="${product.image}" alt="${product.name}" loading="lazy">'

if target in js:
    js = js.replace(target, replacement)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated script.js successfully")
else:
    print("Could not find target in script.js")

# Update styles.css
css_addition = """

/* New Arrival Badge */
.new-badge {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: var(--clr-primary);
    color: var(--clr-white);
    padding: 4px 10px;
    font-size: 0.65rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 4px;
    z-index: 2;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.new-badge {' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(css_addition)
    print("Updated styles.css successfully")
else:
    print("Badge already exists in styles.css")
