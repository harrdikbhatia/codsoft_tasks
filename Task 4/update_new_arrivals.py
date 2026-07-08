import re

# 1. Update HTML files
footer_old = '<li><a href="index.html#collections">New Arrivals</a></li>'
footer_new = '<li><a href="index.html?filter=new#collections">New Arrivals</a></li>'

filter_buttons_old = """        <div class="filters-container">
            <button class="filter-btn active" data-filter="all">All Pieces</button>
            <button class="filter-btn" data-filter="silver">Silver</button>
            <button class="filter-btn" data-filter="gold">Gold</button>
            <button class="filter-btn" data-filter="diamond">Diamond</button>
        </div>"""
filter_buttons_new = """        <div class="filters-container">
            <button class="filter-btn active" data-filter="all">All Pieces</button>
            <button class="filter-btn" data-filter="new" style="color: #d4af37; border-color: #d4af37;">New Arrivals</button>
            <button class="filter-btn" data-filter="silver">Silver</button>
            <button class="filter-btn" data-filter="gold">Gold</button>
            <button class="filter-btn" data-filter="diamond">Diamond</button>
        </div>"""

for filename in ['index.html', 'product.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace(footer_old, footer_new)
    if filename == 'index.html':
        html = html.replace(filter_buttons_old, filter_buttons_new)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filename}")

# 2. Update script.js logic
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_render_old = "if (filterValue === 'all' || product.category === filterValue) {"
js_render_new = "if (filterValue === 'all' || (filterValue === 'new' && product.isNew) || product.category === filterValue) {"
js = js.replace(js_render_old, js_render_new)

js_url_old = "if (filterParam && ['silver', 'gold', 'diamond'].includes(filterParam)) {"
js_url_new = "if (filterParam && ['silver', 'gold', 'diamond', 'new'].includes(filterParam)) {"
js = js.replace(js_url_old, js_url_new)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated script.js")

# 3. Update styles.css badge design
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_old = """/* New Arrival Badge */
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
}"""

css_new = """/* New Arrival Badge (Highlighted) */
.new-badge {
    position: absolute;
    top: 12px;
    left: -6px;
    background: linear-gradient(135deg, #d4af37 0%, #aa7c11 100%);
    color: #fff;
    padding: 6px 14px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    border-radius: 0 4px 4px 0;
    z-index: 2;
    box-shadow: 0 4px 12px rgba(212, 175, 55, 0.4);
    animation: pulseGlow 2s infinite;
}

.new-badge::before {
    content: '';
    position: absolute;
    top: 100%;
    left: 0;
    border-width: 6px 6px 0 0;
    border-style: solid;
    border-color: #8c660e transparent transparent transparent;
}

@keyframes pulseGlow {
    0% { box-shadow: 0 4px 12px rgba(212, 175, 55, 0.4); }
    50% { box-shadow: 0 4px 20px rgba(212, 175, 55, 0.8); }
    100% { box-shadow: 0 4px 12px rgba(212, 175, 55, 0.4); }
}"""

if css_old in css:
    css = css.replace(css_old, css_new)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated styles.css")
else:
    print("Could not find old css block")
