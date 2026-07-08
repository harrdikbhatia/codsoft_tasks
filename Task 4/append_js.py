import os

js_code = """
// ==========================================
// NAVIGATION ICONS LOGIC (Search, Wishlist, Cart)
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    // Elements
    const searchBtn = document.getElementById('nav-search-btn');
    const wishlistBtn = document.getElementById('nav-wishlist-btn');
    const cartBtn = document.getElementById('nav-cart-btn');
    
    const searchOverlay = document.getElementById('search-overlay');
    const closeSearchBtn = document.getElementById('close-search-btn');
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    const cartOverlay = document.getElementById('cart-drawer-overlay');
    const cartDrawer = document.getElementById('cart-drawer');
    const closeCartBtn = document.getElementById('close-cart-btn');
    const cartItemsContainer = document.getElementById('cart-items-container');
    const cartTotalPrice = document.getElementById('cart-total-price');
    
    const cartBadge = document.getElementById('cart-badge');
    const wishlistBadge = document.getElementById('wishlist-badge');

    // State (Load from localStorage)
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let wishlist = JSON.parse(localStorage.getItem('wishlist')) || [];

    // --- UTILS ---
    function updateBadges() {
        if(cartBadge) {
            cartBadge.textContent = cart.length;
            cartBadge.style.display = cart.length > 0 ? 'block' : 'none';
        }
        if(wishlistBadge) {
            wishlistBadge.textContent = wishlist.length;
            wishlistBadge.style.display = wishlist.length > 0 ? 'block' : 'none';
        }
    }

    // --- SEARCH ---
    if(searchBtn && searchOverlay) {
        searchBtn.addEventListener('click', () => {
            searchOverlay.classList.add('active');
            setTimeout(() => searchInput.focus(), 300);
        });
        
        closeSearchBtn.addEventListener('click', () => {
            searchOverlay.classList.remove('active');
        });
        
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            searchResults.innerHTML = '';
            if(query.length < 2) return;
            
            const results = products.filter(p => p.name.toLowerCase().includes(query)).slice(0, 5);
            
            if(results.length === 0) {
                searchResults.innerHTML = '<p>No results found.</p>';
                return;
            }
            
            results.forEach(product => {
                const item = document.createElement('div');
                item.className = 'search-result-item';
                item.style.cursor = 'pointer';
                item.innerHTML = `
                    <img src="${product.image}" alt="${product.name}">
                    <div>
                        <div class="cart-item-title">${product.name}</div>
                        <div class="cart-item-price">₹${product.price}</div>
                    </div>
                `;
                item.addEventListener('click', () => {
                    window.location.href = 'product.html';
                });
                searchResults.appendChild(item);
            });
        });
    }

    // --- CART DRAWER ---
    function renderCart() {
        if(!cartItemsContainer) return;
        cartItemsContainer.innerHTML = '';
        let total = 0;
        
        if(cart.length === 0) {
            cartItemsContainer.innerHTML = '<p>Your cart is empty.</p>';
            cartTotalPrice.textContent = '₹0';
            return;
        }
        
        cart.forEach((item, index) => {
            total += item.price;
            const el = document.createElement('div');
            el.className = 'cart-item';
            el.innerHTML = `
                <img src="${item.image}" alt="${item.name}">
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.name}</div>
                    <div class="cart-item-price">₹${item.price}</div>
                    <div class="cart-item-actions">
                        <span>Qty: 1</span>
                        <button class="remove-item" data-index="${index}">Remove</button>
                    </div>
                </div>
            `;
            cartItemsContainer.appendChild(el);
        });
        
        cartTotalPrice.textContent = '₹' + total.toLocaleString('en-IN');
        
        document.querySelectorAll('.remove-item').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const i = parseInt(e.target.getAttribute('data-index'));
                cart.splice(i, 1);
                localStorage.setItem('cart', JSON.stringify(cart));
                updateBadges();
                renderCart();
            });
        });
    }

    if(cartBtn && cartDrawer) {
        cartBtn.addEventListener('click', () => {
            cartDrawer.classList.add('open');
            cartOverlay.classList.add('active');
            renderCart();
        });
        
        const closeCart = () => {
            cartDrawer.classList.remove('open');
            cartOverlay.classList.remove('active');
        };
        
        closeCartBtn.addEventListener('click', closeCart);
        cartOverlay.addEventListener('click', closeCart);
    }

    // --- ADD TO CART / WISHLIST GLOBALLY ---
    window.addToCart = function(productName, productPrice, productImage) {
        cart.push({name: productName, price: productPrice, image: productImage});
        localStorage.setItem('cart', JSON.stringify(cart));
        updateBadges();
        
        // Open drawer automatically
        if(cartDrawer) {
            cartDrawer.classList.add('open');
            cartOverlay.classList.add('active');
            renderCart();
        } else {
            alert(productName + ' added to cart!');
        }
    };

    window.toggleWishlist = function(productName) {
        const index = wishlist.indexOf(productName);
        if(index > -1) {
            wishlist.splice(index, 1);
        } else {
            wishlist.push(productName);
        }
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        updateBadges();
        return index === -1; // returns true if added, false if removed
    };

    // Attach to product cards dynamically rendered
    document.addEventListener('click', (e) => {
        // Add to Wishlist via Heart Icon on Grid
        const heartBtn = e.target.closest('.icon-btn[aria-label="Add to wishlist"]');
        if(heartBtn) {
            const card = heartBtn.closest('.product-card');
            if(card) {
                const name = card.querySelector('.product-name').textContent;
                const added = window.toggleWishlist(name);
                const icon = heartBtn.querySelector('i');
                if(added) {
                    icon.classList.remove('ph-heart');
                    icon.classList.add('ph-heart-fill');
                    icon.style.color = 'var(--clr-rose)';
                } else {
                    icon.classList.remove('ph-heart-fill');
                    icon.classList.add('ph-heart');
                    icon.style.color = '';
                }
            }
        }
    });

    // Product detail page Specific logic
    const detailAddToCartBtn = document.querySelector('.product-actions-panel .btn-primary');
    if(detailAddToCartBtn) {
        detailAddToCartBtn.addEventListener('click', () => {
            const name = document.querySelector('.product-title').textContent;
            const priceText = document.querySelector('.product-price-large').textContent;
            const price = parseInt(priceText.replace(/[^0-9]/g, ''));
            const image = document.getElementById('main-product-img').src;
            window.addToCart(name, price, image);
        });
    }

    // Wishlist Top Button Alert
    if(wishlistBtn) {
        wishlistBtn.addEventListener('click', () => {
            if(wishlist.length === 0) {
                alert('Your wishlist is empty.');
            } else {
                alert('You have ' + wishlist.length + ' items in your wishlist: \\n' + wishlist.join('\\n'));
            }
        });
    }

    // Init
    updateBadges();
});
"""

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(js_code)

print("Appended logic to script.js")
