import re

# 1. HTML section to inject
about_section_html = """
    <!-- About Us Section -->
    <section id="about" class="about-section">
        <div class="about-container">
            <div class="about-image">
                <img src="https://www.kushals.com/cdn/shop/files/kundan-necklace-ruby-kundan-necklace-148111-1250262102.jpg?v=1781604505&width=1024" alt="AURA Craftsmanship" loading="lazy">
            </div>
            <div class="about-text">
                <span class="about-subtitle">Our Heritage</span>
                <h2>Redefining Artificial Elegance</h2>
                <p>At AURA, we believe that luxury should be accessible without compromising on quality or craftsmanship. Founded with a passion for intricate details and timeless design, our collections bring you the finest in artificial jewellery.</p>
                <p>Every piece in our Silver, Gold, and Diamond simulant collections is meticulously crafted using high-grade alloys, premium micro-plating, and carefully selected stones. We strive to offer you statement pieces that not only elevate your everyday style but also capture the grandeur of traditional and contemporary art.</p>
                <div class="about-features">
                    <div class="feature">
                        <i class="ph-fill ph-gem"></i>
                        <span>Premium Stones</span>
                    </div>
                    <div class="feature">
                        <i class="ph-fill ph-medal"></i>
                        <span>High-Quality Plating</span>
                    </div>
                    <div class="feature">
                        <i class="ph-fill ph-leaf"></i>
                        <span>Skin Friendly</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inject before footer
target = "<!-- Footer -->"
if target in html and "id=\"about\"" not in html:
    html = html.replace(target, about_section_html + "\n    " + target)

# Update navbar links in index.html
html = html.replace('<a href="#">About Us</a>', '<a href="#about">About Us</a>')
# Update mobile nav links
html = html.replace('<a href="#">About Us</a>', '<a href="#about">About Us</a>') # handles any remaining
# Update footer links
html = html.replace('''<a href="javascript:void(0)" onclick="alert('About Us page coming soon!')">About Us</a>''', '<a href="#about">About Us</a>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

# Update product.html links
with open('product.html', 'r', encoding='utf-8') as f:
    phtml = f.read()

phtml = phtml.replace('<a href="#">About Us</a>', '<a href="index.html#about">About Us</a>')
phtml = phtml.replace('''<a href="javascript:void(0)" onclick="alert('About Us page coming soon!')">About Us</a>''', '<a href="index.html#about">About Us</a>')

with open('product.html', 'w', encoding='utf-8') as f:
    f.write(phtml)
print("Updated product.html")

# 2. CSS to inject
css_addition = """
/* ========================================= */
/* About Us Section                          */
/* ========================================= */
.about-section {
    padding: var(--space-xl) 5%;
    background-color: var(--clr-light-gray);
}

.about-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}

.about-image {
    position: relative;
}

.about-image img {
    width: 100%;
    height: auto;
    object-fit: cover;
    border-radius: 4px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.about-image::before {
    content: '';
    position: absolute;
    top: -20px;
    left: -20px;
    right: 20px;
    bottom: 20px;
    border: 2px solid var(--clr-primary);
    z-index: 0;
}

.about-text {
    padding: 2rem 0;
    position: relative;
    z-index: 1;
}

.about-subtitle {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--clr-primary);
    font-weight: 600;
    margin-bottom: 1rem;
    display: inline-block;
}

.about-text h2 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    color: var(--clr-dark);
}

.about-text p {
    color: var(--clr-mid-gray);
    line-height: 1.7;
    margin-bottom: 1.5rem;
    font-size: 1.05rem;
}

.about-features {
    display: flex;
    gap: 2rem;
    margin-top: 2.5rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(0,0,0,0.1);
}

.feature {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.feature i {
    font-size: 1.5rem;
    color: var(--clr-primary);
}

.feature span {
    font-weight: 500;
    font-size: 0.95rem;
    color: var(--clr-dark);
}

@media (max-width: 900px) {
    .about-container {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    
    .about-image::before {
        display: none;
    }
    
    .about-features {
        flex-direction: column;
        gap: 1rem;
    }
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.about-section {' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(css_addition)
    print("Updated styles.css")
else:
    print("About CSS already exists")
