import re

# 1. Update HTML Files
def update_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove Blog and Update Quick Links
    old_links = """                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('Our Story page coming soon!')">Our Story</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('Blog coming soon!')">Blog</a></li>
                    <li><a href="javascript:void(0)" onclick="alert('Contact Us page coming soon!')">Contact Us</a></li>
                </ul>"""
    # handle both index.html and product.html (product might have different #about links initially)
    if "Quick Links" in html:
        # We will just regex replace the whole ul
        pattern = r'<h3>Quick Links</h3>\s*<ul>\s*<li><a href="[^"]*">About Us</a></li>\s*<li><a href="[^"]*"[^>]*>Our Story</a></li>\s*<li><a href="[^"]*"[^>]*>Blog</a></li>\s*<li><a href="[^"]*"[^>]*>Contact Us</a></li>\s*</ul>'
        
        if filename == 'index.html':
            replacement = """<h3>Quick Links</h3>
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#about">Our Story</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                </ul>"""
        else:
            replacement = """<h3>Quick Links</h3>
                <ul>
                    <li><a href="index.html#about">About Us</a></li>
                    <li><a href="index.html#about">Our Story</a></li>
                    <li><a href="index.html#contact">Contact Us</a></li>
                </ul>"""
            
        html = re.sub(pattern, replacement, html)

    # Inject Contact Section into index.html
    contact_html = """
    <!-- Contact Us Section -->
    <section id="contact" class="contact-section">
        <div class="contact-container">
            <div class="contact-info">
                <span class="about-subtitle">Get in Touch</span>
                <h2>Contact Us</h2>
                <p>Have a question or need assistance with your order? Our dedicated team is here to help you experience the luxury of AURA.</p>
                <div class="contact-details">
                    <div class="contact-item">
                        <i class="ph ph-map-pin"></i>
                        <div>
                            <h4>Visit Our Boutique</h4>
                            <p>AURA Fine Artificial Jewellery<br>M-Block Market, Greater Kailash-1<br>New Delhi, Delhi 110048<br>India</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <i class="ph ph-phone"></i>
                        <div>
                            <h4>Call Us</h4>
                            <p>+91 98765 43210<br>Mon-Sat: 10:00 AM - 8:00 PM</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <i class="ph ph-envelope"></i>
                        <div>
                            <h4>Email Us</h4>
                            <p>hello@aurajewellery.in<br>support@aurajewellery.in</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="contact-form-container">
                <form class="contact-form" onsubmit="event.preventDefault(); alert('Thank you for your message! We will get back to you soon.');">
                    <div class="form-group">
                        <input type="text" placeholder="Your Name" required>
                    </div>
                    <div class="form-group">
                        <input type="email" placeholder="Your Email" required>
                    </div>
                    <div class="form-group">
                        <input type="text" placeholder="Subject" required>
                    </div>
                    <div class="form-group">
                        <textarea placeholder="Your Message" rows="5" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary btn-full">Send Message</button>
                </form>
            </div>
        </div>
    </section>
"""
    if filename == 'index.html' and 'id="contact"' not in html:
        # inject before footer
        html = html.replace('<!-- Footer -->', contact_html + '\n    <!-- Footer -->')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filename}")

update_html('index.html')
update_html('product.html')

# 2. Update CSS
css_addition = """
/* ========================================= */
/* Contact Section                           */
/* ========================================= */
.contact-section {
    padding: var(--space-xl) 5%;
    background-color: var(--clr-white);
    border-top: 1px solid var(--clr-light-gray);
}

.contact-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
}

.contact-info h2 {
    font-size: 2.5rem;
    color: var(--clr-black);
    margin-bottom: 1rem;
}

.contact-info p {
    color: var(--clr-dark-gray);
    margin-bottom: 2.5rem;
    line-height: 1.6;
}

.contact-details {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.contact-item {
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
}

.contact-item i {
    font-size: 1.8rem;
    color: var(--clr-champagne);
    margin-top: 0.2rem;
}

.contact-item h4 {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    color: var(--clr-black);
}

.contact-item p {
    margin-bottom: 0;
    color: var(--clr-dark-gray);
    line-height: 1.6;
    font-size: 0.95rem;
}

.contact-form-container {
    background-color: var(--clr-light-gray);
    padding: 3rem;
    border-radius: 4px;
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 1rem;
    border: 1px solid var(--clr-mid-gray);
    border-radius: 4px;
    font-family: var(--font-body);
    font-size: 0.95rem;
    background-color: var(--clr-white);
    transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--clr-champagne);
}

.btn-full {
    width: 100%;
    text-align: center;
}

@media (max-width: 900px) {
    .contact-container {
        grid-template-columns: 1fr;
        gap: 3rem;
    }
    
    .contact-form-container {
        padding: 2rem;
    }
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.contact-section' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(css_addition)
    print("Updated styles.css")
