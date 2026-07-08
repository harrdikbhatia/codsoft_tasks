import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Chunk 1: Elements
old_elements = """    const cartBadge = document.getElementById('cart-badge');
    const wishlistBadge = document.getElementById('wishlist-badge');"""
new_elements = """    const cartBadge = document.getElementById('cart-badge');
    const wishlistBadge = document.getElementById('wishlist-badge');

    // Wishlist Drawer Elements
    const wishlistOverlay = document.getElementById('wishlist-drawer-overlay');
    const wishlistDrawer = document.getElementById('wishlist-drawer');
    const closeWishlistBtn = document.getElementById('close-wishlist-btn');
    const wishlistItemsContainer = document.getElementById('wishlist-items-container');"""
js = js.replace(old_elements, new_elements)

# Chunk 2: Migration
old_state = """    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let wishlist = JSON.parse(localStorage.getItem('wishlist')) || [];"""
new_state = """    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let wishlist = JSON.parse(localStorage.getItem('wishlist')) || [];
    
    // Migrate old string-based wishlist to objects
    if (wishlist.length > 0 && typeof wishlist[0] === 'string') {
        wishlist = [];
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
    }"""
js = js.replace(old_state, new_state)

# Chunk 3: window.toggleWishlist
old_toggle = """    window.toggleWishlist = function(productName) {
        const index = wishlist.indexOf(productName);
        if(index > -1) {
            wishlist.splice(index, 1);
        } else {
            wishlist.push(productName);
        }
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        updateBadges();
        return index === -1; // returns true if added, false if removed
    };"""
new_toggle = """    window.toggleWishlist = function(productName) {
        const index = wishlist.findIndex(i => i.name === productName);
        if(index > -1) {
            wishlist.splice(index, 1);
        } else {
            const product = window.products.find(p => p.name === productName);
            if (product) {
                wishlist.push({name: product.name, price: product.price, image: product.image, id: product.id});
            } else {
                wishlist.push({name: productName, price: 0, image: ''});
            }
        }
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        updateBadges();
        
        // Open wishlist drawer automatically when adding
        if (index === -1 && wishlistDrawer) {
            wishlistDrawer.classList.add('open');
            if (wishlistOverlay) wishlistOverlay.classList.add('active');
            window.renderWishlist();
        }
        
        return index === -1; // returns true if added, false if removed
    };"""
js = js.replace(old_toggle, new_toggle)

# Chunk 4: Drawer Logic
old_alert = """    // Wishlist Top Button Alert
    if(wishlistBtn) {
        wishlistBtn.addEventListener('click', () => {
            if(wishlist.length === 0) {
                alert('Your wishlist is empty.');
            } else {
                alert('You have ' + wishlist.length + ' items in your wishlist: \\n' + wishlist.join('\\n'));
            }
        });
    }"""
new_logic = """    // --- WISHLIST DRAWER LOGIC ---
    window.renderWishlist = function() {
        if(!wishlistItemsContainer) return;
        wishlistItemsContainer.innerHTML = '';
        
        if(wishlist.length === 0) {
            wishlistItemsContainer.innerHTML = '<p style="padding: 20px; text-align: center; color: #888;">Your wishlist is empty.</p>';
            return;
        }
        
        wishlist.forEach((item, index) => {
            const el = document.createElement('div');
            el.className = 'cart-item';
            el.innerHTML = `
                <img src="${item.image}" alt="${item.name}">
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.name}</div>
                    <div class="cart-item-price">₹${item.price}</div>
                    <div class="cart-item-actions" style="margin-top: 10px; display: flex; justify-content: space-between; align-items: center;">
                        <button class="btn-primary add-to-cart-from-wishlist" style="padding: 5px 15px; font-size: 0.8rem; border-radius: 4px;" data-index="${index}">Add to Cart</button>
                        <button class="remove-wishlist-item" style="background: none; border: none; color: #888; cursor: pointer; text-decoration: underline; font-size: 0.8rem;" data-index="${index}">Remove</button>
                    </div>
                </div>
            `;
            wishlistItemsContainer.appendChild(el);
        });
        
        document.querySelectorAll('.remove-wishlist-item').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const i = parseInt(e.target.getAttribute('data-index'));
                wishlist.splice(i, 1);
                localStorage.setItem('wishlist', JSON.stringify(wishlist));
                updateBadges();
                window.renderWishlist();
                
                // Update heart icon if visible
                const name = wishlist[i]?.name;
                document.querySelectorAll('.product-name').forEach(el => {
                    if (el.textContent === name) {
                        const heartBtn = el.closest('.product-info').previousElementSibling.querySelector('.icon-btn[aria-label="Add to wishlist"] i');
                        if (heartBtn) {
                            heartBtn.classList.remove('ph-heart-fill');
                            heartBtn.classList.add('ph-heart');
                            heartBtn.style.color = '';
                        }
                    }
                });
            });
        });

        document.querySelectorAll('.add-to-cart-from-wishlist').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const i = parseInt(e.target.getAttribute('data-index'));
                const item = wishlist[i];
                const price = typeof item.price === 'string' ? parseInt(item.price.replace(/[^0-9]/g, '')) : item.price;
                window.addToCart(item.name, price, item.image, 1);
                
                wishlist.splice(i, 1);
                localStorage.setItem('wishlist', JSON.stringify(wishlist));
                updateBadges();
                window.renderWishlist();
            });
        });
    }

    if(wishlistBtn && wishlistDrawer) {
        wishlistBtn.addEventListener('click', () => {
            wishlistDrawer.classList.add('open');
            if (wishlistOverlay) wishlistOverlay.classList.add('active');
            window.renderWishlist();
        });
        
        const closeWishlist = () => {
            wishlistDrawer.classList.remove('open');
            if (wishlistOverlay) wishlistOverlay.classList.remove('active');
        };
        
        if (closeWishlistBtn) closeWishlistBtn.addEventListener('click', closeWishlist);
        if (wishlistOverlay) wishlistOverlay.addEventListener('click', closeWishlist);
    }"""
js = js.replace(old_alert, new_logic)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Injected wishlist drawer logic successfully.")
