import re

# 1. Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_html = """                <div class="about-logo-display">
                    <h1>AURA</h1>
                    <span>Fine Artificial Jewellery</span>
                </div>"""
new_html = """                <img src="images/aura_logo.jpg" alt="AURA Logo" loading="lazy">"""

if old_html in html:
    html = html.replace(old_html, new_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html")
else:
    print("Could not find logo display in index.html")

# 2. Update CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_css = """.about-image {
    position: relative;
    height: 100%;
}

.about-logo-display {
    width: 100%;
    height: 100%;
    min-height: 450px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
    border-radius: 4px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

.about-logo-display h1 {
    font-family: var(--font-heading);
    font-size: 5rem;
    letter-spacing: 12px;
    color: var(--clr-black);
    margin: 0;
    margin-right: -12px; /* offset tracking */
}

.about-logo-display span {
    font-family: var(--font-body);
    font-size: 0.9rem;
    letter-spacing: 4px;
    color: var(--clr-champagne);
    text-transform: uppercase;
    margin-top: 1rem;
    font-weight: 500;
}"""

new_css = """.about-image {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}

.about-image img {
    width: 100%;
    max-width: 500px;
    height: auto;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.08);
}"""

if old_css in css:
    css = css.replace(old_css, new_css)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated styles.css")
else:
    print("Could not find css block")
