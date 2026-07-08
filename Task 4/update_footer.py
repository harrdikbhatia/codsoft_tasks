import re

old_footer_links = """            <div class="footer-links">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Our Story</a></li>
                    <li><a href="#">Blog</a></li>
                    <li><a href="#">Contact Us</a></li>
                </ul>
            </div>

            <div class="footer-links">
                <h3>Collections</h3>
                <ul>
                    <li><a href="#">Silver Jewellery</a></li>
                    <li><a href="#">Gold Plated</a></li>
                    <li><a href="#">Diamond Simulants</a></li>
                    <li><a href="#">New Arrivals</a></li>
                </ul>
            </div>

            <div class="footer-links">
                <h3>Customer Support</h3>
                <ul>
                    <li><a href="#">Shipping & Returns</a></li>
                    <li><a href="#">Jewellery Care</a></li>
                    <li><a href="#">FAQ</a></li>
                    <li><a href="#">Track Order</a></li>
                </ul>
            </div>"""

new_footer_links = """            <div class="footer-links">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="javascript:void(0)" onclick="alert('About Us page coming soon!')">About Us</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('Our Story page coming soon!')">Our Story</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('Blog coming soon!')">Blog</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('Contact Us page coming soon!')">Contact Us</a></li>
                </ul>
            </div>

            <div class="footer-links">
                <h3>Collections</h3>
                <ul>
                    <li><a href="index.html?filter=silver#collections">Silver Jewellery</a></li>
                    <li><a href="index.html?filter=gold#collections">Gold Plated</a></li>
                    <li><a href="index.html?filter=diamond#collections">Diamond Simulants</a></li>
                    <li><a href="index.html#collections">New Arrivals</a></li>
                </ul>
            </div>

            <div class="footer-links">
                <h3>Customer Support</h3>
                <ul>
                    <li><a href="javascript:void(0)" onclick="alert('Shipping & Returns policy coming soon!')">Shipping & Returns</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('Jewellery Care guide coming soon!')">Jewellery Care</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('FAQ page coming soon!')">FAQ</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('Order tracking feature coming soon!')">Track Order</a></li>
                </ul>
            </div>"""

for filename in ['index.html', 'product.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if old_footer_links in html:
        new_html = html.replace(old_footer_links, new_footer_links)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Replaced footer links in {filename}")
    else:
        print(f"Could not find exact footer links block in {filename}")

# Now update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_render_init = """    // Initial render
    if (productGrid) {
        renderProducts('all');
    }"""

new_render_init = """    // Initial render
    if (productGrid) {
        const urlParams = new URLSearchParams(window.location.search);
        const filterParam = urlParams.get('filter');
        
        if (filterParam && ['silver', 'gold', 'diamond'].includes(filterParam)) {
            // Activate the correct filter button visually
            if (filterBtns) {
                filterBtns.forEach(b => {
                    b.classList.remove('active');
                    if (b.getAttribute('data-filter') === filterParam) {
                        b.classList.add('active');
                    }
                });
            }
            renderProducts(filterParam);
            
            // Optional: Smooth scroll to collections if there's a hash, though browser does it automatically
        } else {
            renderProducts('all');
        }
    }"""

if old_render_init in js:
    js = js.replace(old_render_init, new_render_init)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Replaced script.js initial render logic")
else:
    print("Could not find initial render block in script.js")
