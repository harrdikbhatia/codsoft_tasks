document.addEventListener('DOMContentLoaded', () => {
    
    // ==========================================
    // Navbar Scroll Effect
    // ==========================================
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // ==========================================
    // Mobile Navigation Toggle
    // ==========================================
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const closeMenuBtn = document.getElementById('close-menu');
    const mobileNav = document.getElementById('mobile-nav');

    if (mobileMenuToggle && mobileNav) {
        mobileMenuToggle.addEventListener('click', () => {
            mobileNav.classList.add('open');
        });
    }

    if (closeMenuBtn && mobileNav) {
        closeMenuBtn.addEventListener('click', () => {
            mobileNav.classList.remove('open');
        });
    }

    // ==========================================
    // Product Data Generation (75 Items)
    // ==========================================
    window.products = [
    {
        "id": "silver-0",
        "name": "Classic Silver Charm Necklace",
        "category": "silver",
        "price": "25,199",
        "image": "https://www.kushals.com/cdn/shop/files/temple-necklace-ruby-green-gold-silver-temple-necklace-191815-1212890837.jpg?v=1766486329&width=1024",
        "isNew": true
    },
    {
        "id": "silver-1",
        "name": "Vintage Silver Ring",
        "category": "silver",
        "price": "5,499",
        "image": "https://www.kushals.com/cdn/shop/files/temple-finger-ring-white-gold-silver-temple-finger-ring-190556-1211744524.jpg?v=1766206132&width=1024",
        "isNew": true
    },
    {
        "id": "silver-2",
        "name": "Oxidised Silver Bangle",
        "category": "silver",
        "price": "12,399",
        "image": "https://www.kushals.com/cdn/shop/files/temple-bangle-ruby-oxidised-gold-silver-temple-bangle-pendant-180474-40557629440156.jpg?v=1735954829&width=1024",
        "isNew": false
    },
    {
        "id": "silver-3",
        "name": "925 Silver Anushka Pendant",
        "category": "silver",
        "price": "9,199",
        "image": "https://www.kushals.com/cdn/shop/files/temple-pendant-ruby-gold-silver-temple-pendant-190591-1213043783.jpg?v=1766591906&width=640",
        "isNew": false
    },
    {
        "id": "silver-4",
        "name": "Antique Silver Choker",
        "category": "silver",
        "price": "22,199",
        "image": "https://www.kushals.com/cdn/shop/files/temple-pendant-ruby-gold-silver-temple-pendant-190591-1213043784.jpg?v=1766591985&width=1024",
        "isNew": false
    },
    {
        "id": "silver-5",
        "name": "Elegant Silver Tikka",
        "category": "silver",
        "price": "23,699",
        "image": "https://www.kushals.com/cdn/shop/files/temple-tikka-silver-temple-tikka-172580-1128066156.jpg?v=1739032468&width=1024",
        "isNew": false
    },
    {
        "id": "silver-6",
        "name": "Traditional Silver Tikka",
        "category": "silver",
        "price": "6,099",
        "image": "https://www.kushals.com/cdn/shop/files/temple-tikka-silver-temple-tikka-188191-1231097945.jpg?v=1775232935&width=640",
        "isNew": false
    },
    {
        "id": "silver-7",
        "name": "Signature Silver Ring",
        "category": "silver",
        "price": "7,399",
        "image": "https://www.kushals.com/cdn/shop/files/temple-finger-ring-green-oxidised-gold-silver-temple-finger-ring-178146-40516464803996.jpg?v=1735265615&width=640",
        "isNew": false
    },
    {
        "id": "silver-8",
        "name": "Sparkling Silver Ring",
        "category": "silver",
        "price": "12,899",
        "image": "https://www.kushals.com/cdn/shop/files/temple-finger-ring-silver-temple-finger-ring-188186-1231097970.jpg?v=1775233126&width=640",
        "isNew": false
    },
    {
        "id": "silver-9",
        "name": "Ruby Green Silver Pendant",
        "category": "silver",
        "price": "24,099",
        "image": "https://www.kushals.com/cdn/shop/files/temple-pendant-ruby-green-gold-silver-temple-pendant-190587-1213043787.jpg?v=1766592026&width=1024",
        "isNew": false
    },
    {
        "id": "gold-10",
        "name": "Royal Gold Drop Earrings",
        "category": "gold",
        "price": "1,78,399",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-earring-kundan-earring-196768-1231172265.jpg?v=1775337635&width=1024",
        "isNew": true
    },
    {
        "id": "gold-11",
        "name": "Classic Kundan Earrings",
        "category": "gold",
        "price": "1,74,699",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-earring-white-victorian-kundan-earring-196878-1231172207.jpg?v=1775341373&width=1024",
        "isNew": true
    },
    {
        "id": "gold-12",
        "name": "Kundan Gold Kada",
        "category": "gold",
        "price": "91,799",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-kada-white-victorian-kundan-kada-196792-1231172226.jpg?v=1775333828&width=640",
        "isNew": false
    },
    {
        "id": "gold-13",
        "name": "Gold Statement Ring",
        "category": "gold",
        "price": "1,06,099",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-finger-ring-white-victorian-kundan-finger-ring-196894-1231172165.jpg?v=1775342024&width=1024",
        "isNew": false
    },
    {
        "id": "gold-14",
        "name": "Elegant Kundan Ring",
        "category": "gold",
        "price": "75,699",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-finger-ring-kundan-finger-ring-196786-1231172243.jpg?v=1775337081&width=1024",
        "isNew": false
    },
    {
        "id": "gold-15",
        "name": "Vintage Gold Ring",
        "category": "gold",
        "price": "1,22,499",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-finger-ring-white-victorian-kundan-finger-ring-196892-1231172175.jpg?v=1775342315&width=1024",
        "isNew": false
    },
    {
        "id": "gold-16",
        "name": "24k Gold Solitaire Ring",
        "category": "gold",
        "price": "74,399",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-finger-ring-white-victorian-kundan-finger-ring-196894-1231172165.jpg?v=1775342024&width=640",
        "isNew": false
    },
    {
        "id": "gold-17",
        "name": "Traditional Gold Jhumkas",
        "category": "gold",
        "price": "1,21,199",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-earring-kundan-earring-196768-1231172264.jpg?v=1775337644&width=1024",
        "isNew": false
    },
    {
        "id": "gold-18",
        "name": "Bridal Gold Earrings",
        "category": "gold",
        "price": "58,699",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-earring-white-victorian-kundan-earring-196874-1225077148.jpg?v=1772714006&width=1024",
        "isNew": false
    },
    {
        "id": "gold-19",
        "name": "Bridal Gold Necklace",
        "category": "gold",
        "price": "59,599",
        "image": "https://www.kushals.com/cdn/shop/files/kundan-necklace-ruby-victorian-kundan-necklace-196764-1219326085.jpg?v=1770223722&width=1024",
        "isNew": false
    },
    {
        "id": "diamond-20",
        "name": "Diamond Tennis Bracelet",
        "category": "diamond",
        "price": "2,51,999",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-bracelet-zircon-bracelet-191931-1210585443.jpg?v=1765316107&width=640",
        "isNew": true
    },
    {
        "id": "diamond-21",
        "name": "Solitaire Drop Earrings",
        "category": "diamond",
        "price": "2,10,099",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-earring-zircon-earring-187648-1195524388.jpg?v=1759245787&width=1024",
        "isNew": true
    },
    {
        "id": "diamond-22",
        "name": "Diamond Choker Necklace",
        "category": "diamond",
        "price": "4,48,799",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-necklace-zircon-necklace-193109-1219322237.jpg?v=1770240628&width=1024",
        "isNew": false
    },
    {
        "id": "diamond-23",
        "name": "Infinity Diamond Bangle",
        "category": "diamond",
        "price": "3,49,199",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-bangle-zircon-bangle-196783-1219326028.jpg?v=1770220369&width=1024",
        "isNew": false
    },
    {
        "id": "diamond-24",
        "name": "Diamond Solitaire Ring",
        "category": "diamond",
        "price": "2,68,199",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-finger-ring-zircon-finger-ring-193894-1227479673.jpg?v=1773743986&width=640",
        "isNew": false
    },
    {
        "id": "diamond-25",
        "name": "Rose Gold Diamond Bangle",
        "category": "diamond",
        "price": "3,57,499",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-bangle-white-rose-gold-2-4-zircon-bangle-193933-1219322085.jpg?v=1770233385&width=1024",
        "isNew": false
    },
    {
        "id": "diamond-26",
        "name": "Elegant Diamond Tikka",
        "category": "diamond",
        "price": "3,96,999",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-tikka-zircon-tikka-191102-1210585582.jpg?v=1765311413&width=1024",
        "isNew": false
    },
    {
        "id": "diamond-27",
        "name": "Ruby Diamond Ring",
        "category": "diamond",
        "price": "2,60,999",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-finger-ring-ruby-rodium-gold-zircon-finger-ring-185596-1244661354.jpg?v=1781629486&width=640",
        "isNew": false
    },
    {
        "id": "diamond-28",
        "name": "Sparkle Stud Earrings",
        "category": "diamond",
        "price": "1,73,199",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-earring-sapphire-gold-zircon-earring-136753-37206969319580.jpg?v=1721895212&width=640",
        "isNew": false
    },
    {
        "id": "diamond-29",
        "name": "White Gold Diamond Bracelet",
        "category": "diamond",
        "price": "98,399",
        "image": "https://www.kushals.com/cdn/shop/files/zircon-bracelet-zircon-bracelet-162529-1193747551.jpg?v=1758296691&width=1024",
        "isNew": false
    }
];

    // ==========================================
    // Product Rendering & Filtering (Homepage)
    // ==========================================
    const productGrid = document.getElementById('product-grid');
    const filterBtns = document.querySelectorAll('.filter-btn');

    function renderProducts(filterValue = 'all') {
        if (!productGrid) return;
        
        let htmlContent = '';
        
        products.forEach(product => {
            if (filterValue === 'all' || (filterValue === 'new' && product.isNew) || product.category === filterValue) {
                htmlContent += `
                <div class="product-card fade-in" data-category="${product.category}">
                    <div class="product-image">
                        ${product.isNew ? '<span class="new-badge">New Arrival</span>' : ''}
                        <img src="${product.image}" alt="${product.name}" loading="lazy">
                        <div class="product-actions">
                            <button class="icon-btn" aria-label="Add to wishlist"><i class="ph ph-heart"></i></button>
                            <button class="icon-btn" aria-label="Quick view" onclick="window.location.href='product.html?id=${product.id}'"><i class="ph ph-eye"></i></button>
                        </div>
                    </div>
                    <div class="product-info">
                        <span class="product-category">${product.category.charAt(0).toUpperCase() + product.category.slice(1)} Collection</span>
                        <a href="product.html?id=${product.id}" class="product-name">${product.name}</a>
                        <span class="product-price">₹${product.price}</span>
                    </div>
                </div>
                `;
            }
        });
        
        productGrid.innerHTML = htmlContent;
    }

    // Initial render
    if (productGrid) {
        const urlParams = new URLSearchParams(window.location.search);
        const filterParam = urlParams.get('filter');
        
        if (filterParam && ['silver', 'gold', 'diamond', 'new'].includes(filterParam)) {
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
    }

    if (filterBtns.length > 0 && productGrid) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all buttons
                filterBtns.forEach(b => b.classList.remove('active'));
                // Add active class to clicked button
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');
                renderProducts(filterValue);
            });
        });
    }

    // ==========================================
    // Product Gallery (Product Details Page)
    // ==========================================
    const mainImg = document.getElementById('main-product-img');
    const thumbWrappers = document.querySelectorAll('.thumb-wrapper');

    if (mainImg && thumbWrappers.length > 0) {
        thumbWrappers.forEach(wrapper => {
            wrapper.addEventListener('click', function() {
                // Remove active class from all wrappers
                thumbWrappers.forEach(t => t.classList.remove('active'));
                
                // Add active class to clicked wrapper
                this.classList.add('active');
                
                // Get the img inside this wrapper
                const img = this.querySelector('.thumbnail');
                if(!img) return;
                
                const newSrc = img.getAttribute('src');
                const newTransform = img.style.transform;
                
                // Add a small fade effect
                mainImg.style.opacity = 0;
                setTimeout(() => {
                    mainImg.setAttribute('src', newSrc);
                    mainImg.style.transform = newTransform || "none";
                    mainImg.style.opacity = 1;
                }, 300);
            });
        });
    }

    // ==========================================
    // Accordion (Product Details Page)
    // ==========================================
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    if (accordionHeaders.length > 0) {
        accordionHeaders.forEach(header => {
            header.addEventListener('click', function() {
                // Toggle icon
                const icon = this.querySelector('i');
                if (icon.classList.contains('ph-caret-down')) {
                    icon.classList.replace('ph-caret-down', 'ph-caret-up');
                } else {
                    icon.classList.replace('ph-caret-up', 'ph-caret-down');
                }

                // Toggle content
                const content = this.nextElementSibling;
                if (content.style.maxHeight) {
                    content.style.maxHeight = null;
                } else {
                    content.style.maxHeight = content.scrollHeight + "px";
                }
            });
        });
    }

    // ==========================================
    // Quantity Selector
    // ==========================================
    const qtyMinus = document.getElementById('qty-minus');
    const qtyPlus = document.getElementById('qty-plus');
    const qtyInput = document.getElementById('qty-input');

    if (qtyMinus && qtyPlus && qtyInput) {
        qtyMinus.addEventListener('click', () => {
            let val = parseInt(qtyInput.value);
            if (val > 1) {
                qtyInput.value = val - 1;
            }
        });

        qtyPlus.addEventListener('click', () => {
            let val = parseInt(qtyInput.value);
            qtyInput.value = val + 1;
        });
    }
    
    // ==========================================
    // Product Variant Selector
    // ==========================================
    const variantBtns = document.querySelectorAll('.variant-btn');
    if(variantBtns.length > 0){
        variantBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                variantBtns.forEach(b => b.classList.remove('active'));
                this.classList.add('active');
            });
        });
    }
});

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

    // Wishlist Drawer Elements
    const wishlistOverlay = document.getElementById('wishlist-drawer-overlay');
    const wishlistDrawer = document.getElementById('wishlist-drawer');
    const closeWishlistBtn = document.getElementById('close-wishlist-btn');
    const wishlistItemsContainer = document.getElementById('wishlist-items-container');

    // State (Load from localStorage)
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let wishlist = JSON.parse(localStorage.getItem('wishlist')) || [];
    
    // Migrate old string-based wishlist to objects
    if (wishlist.length > 0 && typeof wishlist[0] === 'string') {
        wishlist = [];
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
    }

    // --- UTILS ---
    function updateBadges() {
        if(cartBadge) {
            const totalItems = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
            cartBadge.textContent = totalItems;
            cartBadge.style.display = totalItems > 0 ? 'block' : 'none';
        }
        if(wishlistBadge) {
            wishlistBadge.textContent = wishlist.length;
            wishlistBadge.style.display = wishlist.length > 0 ? 'block' : 'none';
        }
    }

    // --- SEARCH ---
    function showSuggestions() {
        searchResults.innerHTML = '<div style="padding: 10px; color: #888; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 5px;">Popular Suggestions</div>';
        
        // Pick 4 representative products as suggestions
        const suggestions = [products[0], products[5], products[10], products[3]].filter(Boolean);
        
        suggestions.forEach(product => {
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
                window.location.href = 'product.html?id=' + (product ? product.id : item.id);
            });
            searchResults.appendChild(item);
        });
    }

    if(searchBtn && searchOverlay) {
        searchBtn.addEventListener('click', () => {
            searchOverlay.classList.add('active');
            showSuggestions();
            setTimeout(() => searchInput.focus(), 300);
        });
        
        closeSearchBtn.addEventListener('click', () => {
            searchOverlay.classList.remove('active');
            searchInput.value = '';
        });
        
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            searchResults.innerHTML = '';
            
            if(query.length < 2) {
                showSuggestions();
                return;
            }
            
            const results = products.filter(p => p.name.toLowerCase().includes(query)).slice(0, 6);
            
            if(results.length === 0) {
                searchResults.innerHTML = '<p style="padding: 10px;">No results found.</p>';
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
                    window.location.href = 'product.html?id=' + (product ? product.id : item.id);
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
            const qty = item.quantity || 1;
            total += item.price * qty;
            const el = document.createElement('div');
            el.className = 'cart-item';
            el.innerHTML = `
                <img src="${item.image}" alt="${item.name}">
                <div class="cart-item-details">
                    <div class="cart-item-title">${item.name}</div>
                    <div class="cart-item-price">₹${item.price.toLocaleString('en-IN')}</div>
                    <div class="cart-item-actions">
                        <div class="cart-qty-controls">
                            <span>Qty: ${qty}</span>
                        </div>
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
        
        // Checkout Logic
        const checkoutBtns = document.querySelectorAll('.cart-footer .btn-primary');
        const checkoutDrawer = document.getElementById('checkout-drawer');
        const checkoutOverlay = document.getElementById('checkout-drawer-overlay');
        const closeCheckoutBtn = document.getElementById('close-checkout-btn');
        const checkoutForm = document.getElementById('checkout-form');
        
        const closeCheckout = () => {
            if (checkoutDrawer) checkoutDrawer.classList.remove('open');
            if (checkoutOverlay) checkoutOverlay.classList.remove('active');
        };
        
        if (closeCheckoutBtn) closeCheckoutBtn.addEventListener('click', closeCheckout);
        if (checkoutOverlay) checkoutOverlay.addEventListener('click', closeCheckout);

        checkoutBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                if(cart.length === 0) {
                    if (window.showToast) window.showToast("Your cart is empty. Please add some items first.");
                    return;
                }
                
                // Update checkout button text to show total
                const submitBtn = document.getElementById('checkout-submit-btn');
                if (submitBtn) {
                    submitBtn.textContent = `Place Order (${cartTotalPrice.textContent})`;
                }
                
                // Close cart drawer
                closeCart();
                
                // Open checkout drawer
                if (checkoutDrawer && checkoutOverlay) {
                    checkoutDrawer.classList.add('open');
                    checkoutOverlay.classList.add('active');
                    if (checkoutForm) checkoutForm.style.display = 'block';
                    const successDiv = document.getElementById('checkout-success');
                    if (successDiv) successDiv.style.display = 'none';
                }
            });
        });
        
        // Payment Method Toggle Logic
        const paymentRadios = document.querySelectorAll('input[name="payment_method"]');
        const cardDetails = document.getElementById('payment-card-details');
        const upiDetails = document.getElementById('payment-upi-details');
        
        paymentRadios.forEach(radio => {
            radio.addEventListener('change', (e) => {
                if (e.target.value === 'card') {
                    if(cardDetails) cardDetails.style.display = 'block';
                    if(upiDetails) upiDetails.style.display = 'none';
                } else if (e.target.value === 'upi') {
                    if(cardDetails) cardDetails.style.display = 'none';
                    if(upiDetails) upiDetails.style.display = 'block';
                } else if (e.target.value === 'cod') {
                    if(cardDetails) cardDetails.style.display = 'none';
                    if(upiDetails) upiDetails.style.display = 'none';
                }
            });
        });
        
        if (checkoutForm) {
            checkoutForm.addEventListener('submit', (e) => {
                e.preventDefault();
                
                // Basic Validation based on payment method
                const selectedPayment = document.querySelector('input[name="payment_method"]:checked')?.value;
                if (selectedPayment === 'card') {
                    const cardNum = document.getElementById('card-num')?.value;
                    if (!cardNum) {
                        if (window.showToast) window.showToast("Please enter your card number.");
                        return;
                    }
                } else if (selectedPayment === 'upi') {
                    const upiId = document.getElementById('upi-id')?.value;
                    if (!upiId) {
                        if (window.showToast) window.showToast("Please enter your UPI ID.");
                        return;
                    }
                }
                
                const name = document.getElementById('checkout-name').value;
                const submitBtn = document.getElementById('checkout-submit-btn');
                const originalText = submitBtn.textContent;
                
                submitBtn.textContent = 'Processing...';
                submitBtn.disabled = true;
                
                setTimeout(() => {
                    // Clear cart
                    cart = [];
                    localStorage.setItem('cart', JSON.stringify(cart));
                    updateBadges();
                    // Generate random order ID
                    const orderId = 'AURA-' + Math.floor(10000 + Math.random() * 90000);
                    
                    // Show success screen instead of closing
                    checkoutForm.style.display = 'none';
                    const successDiv = document.getElementById('checkout-success');
                    const orderIdSpan = document.getElementById('confirmed-order-id');
                    if (successDiv && orderIdSpan) {
                        orderIdSpan.textContent = orderId;
                        successDiv.style.display = 'block';
                    }
                    
                    // Handle Track Order button click
                    const trackBtn = document.getElementById('track-order-btn');
                    if (trackBtn) {
                        trackBtn.onclick = () => {
                            closeCheckout();
                            window.openSupportDrawer('track');
                            setTimeout(() => {
                                const trackForm = document.getElementById('track-form');
                                if (trackForm) {
                                    const inputs = trackForm.querySelectorAll('input');
                                    if (inputs.length > 0) inputs[0].value = orderId;
                                }
                            }, 100);
                        };
                    }
                    
                    checkoutForm.reset();
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    
                    // Show personalized success toast
                    setTimeout(() => {
                        if (window.showToast) {
                            window.showToast(`Thank you ${name}! Your luxury pieces are being prepared.`);
                        }
                    }, 400);
                }, 1500);
            });
        }
    }

    // --- ADD TO CART / WISHLIST GLOBALLY ---
    window.addToCart = function(productName, productPrice, productImage, quantity = 1) {
        const existingItem = cart.find(i => i.name === productName);
        if (existingItem) {
            existingItem.quantity = (existingItem.quantity || 1) + quantity;
        } else {
            cart.push({name: productName, price: productPrice, image: productImage, quantity: quantity});
        }
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
            
            const qtyInput = document.getElementById('qty-input');
            const qty = qtyInput ? parseInt(qtyInput.value) : 1;
            
            window.addToCart(name, price, image, qty);
        });
    }

    // --- WISHLIST DRAWER LOGIC ---
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
    }

    // Init
    updateBadges();
});

// ==========================================
// HIGH-END UI INTERACTIONS (ABOUT US SECTION)
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Scroll Reveal (Intersection Observer)
    const aboutSection = document.querySelector('.about-section');
    if (aboutSection) {
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.2 // Trigger when 20% of section is visible
        };
        
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    // Optional: stop observing once revealed
                    // observer.unobserve(entry.target); 
                }
            });
        }, observerOptions);
        
        observer.observe(aboutSection);
    }
    
    // 2. Dynamic 3D Mouse Tracking for Logo
    const aboutImageContainer = document.querySelector('.about-image');
    const aboutImg = document.querySelector('.about-image img');
    
    if (aboutImageContainer && aboutImg) {
        aboutImageContainer.addEventListener('mousemove', (e) => {
            // Get dimensions of the container
            const rect = aboutImageContainer.getBoundingClientRect();
            
            // Calculate mouse position relative to the center of the image (-1 to 1)
            const x = (e.clientX - rect.left - (rect.width / 2)) / (rect.width / 2);
            const y = (e.clientY - rect.top - (rect.height / 2)) / (rect.height / 2);
            
            // Increase the multiplier for more dramatic tilt (highlighted)
            const tiltX = y * -35; // Rotate around X axis based on Y movement
            const tiltY = x * 35;  // Rotate around Y axis based on X movement
            
            // Apply transform and dynamic glow (increased scale for highlighted effect)
            aboutImg.style.transform = `scale(1.15) rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
            aboutImg.style.transition = 'transform 0.1s ease-out, filter 0.1s ease-out';
            
            // Dynamic metallic glow based on mouse position - vastly increased brightness and opacity
            const glowX = x * 40;
            const glowY = y * 40;
            aboutImg.style.filter = `drop-shadow(${glowX}px ${glowY}px 45px rgba(212, 175, 55, 0.8)) brightness(1.25)`;
        });
        
        // Reset on mouse leave
        aboutImageContainer.addEventListener('mouseleave', () => {
            aboutImg.style.transform = 'scale(1) rotateX(0deg) rotateY(0deg)';
            aboutImg.style.transition = 'transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94), filter 0.6s ease';
            aboutImg.style.filter = 'drop-shadow(0 15px 25px rgba(0, 0, 0, 0.1)) brightness(1)';
        });
    }
});


document.addEventListener('DOMContentLoaded', () => {
    // ... existing init code ...
    if(document.querySelector('.product-detail') !== null) {
        const urlParams = new URLSearchParams(window.location.search);
        let productId = urlParams.get('id');
        
        // If opened directly from an IDE without an ID, fallback to the first product 
        // to prevent hardcoded DOM values from causing mismatched pricing and names
        if (!productId) {
            productId = products[0].id;
            window.history.replaceState({}, '', '?id=' + productId);
        }
        
        if(productId) {
            const product = products.find(p => p.id === productId);
            if(product) {
                document.querySelector('.product-title').textContent = product.name;
                document.querySelector('.product-price-large').textContent = '₹' + product.price;
                document.querySelector('#main-product-img').src = product.image;
                document.querySelector('.breadcrumbs span').textContent = product.name;
                // Dynamic Description and Specs
                const descEl = document.querySelector('.product-desc');
                const specsEl = document.querySelector('.accordion-content ul');
                
                if (descEl && specsEl) {
                    let desc = `Elevate your everyday style with our beautiful ${product.name}. Carefully crafted to catch the light from every angle, this timeless piece is a staple for any jewelry collection.`;
                    
                    const nameLower = product.name.toLowerCase();
                    
                    // Material & Plating logic (Fine Jewellery)
                    let material = "Solid 14k Gold";
                    let plating = "Fine Polish";
                    
                    if (product.category === 'silver' || nameLower.includes('silver')) {
                        material = "Solid 925 Sterling Silver";
                        plating = "Oxidised Sterling Silver";
                        if (nameLower.includes('925') || nameLower.includes('sparkling')) plating = "Rhodium Finish";
                    }
                    if (product.category === 'gold' || nameLower.includes('gold') || nameLower.includes('kundan')) {
                        material = "Solid 18k Gold";
                        plating = "18k Gold Finish";
                        if (nameLower.includes('antique') || nameLower.includes('vintage')) plating = "Antique 18k Gold Finish";
                    }
                    
                    // Stone logic
                    let stone = "No Stones";
                    if (nameLower.includes('zircon') || nameLower.includes('crystal') || nameLower.includes('diamond') || product.category === 'diamond') stone = "Natural Diamonds";
                    if (nameLower.includes('kundan')) stone = "Polki Diamonds / Precious Kundan";
                    if (nameLower.includes('ruby')) stone = "Natural Rubies";
                    if (nameLower.includes('emerald') || nameLower.includes('green')) stone = "Natural Emeralds";
                    
                    // Type specific logic
                    let extraSpec = "";
                    if (nameLower.includes('ring')) extraSpec = `<li><strong>Size:</strong> Adjustable (Free Size)</li>`;
                    else if (nameLower.includes('necklace') || nameLower.includes('pendant') || nameLower.includes('choker')) extraSpec = `<li><strong>Length:</strong> Adjustable Dori / Chain</li>`;
                    else if (nameLower.includes('bracelet') || nameLower.includes('bangle') || nameLower.includes('kada')) extraSpec = `<li><strong>Size:</strong> 2.4 / 2.6 inches</li>`;
                    else if (nameLower.includes('earring') || nameLower.includes('jhumka') || nameLower.includes('stud')) extraSpec = `<li><strong>Closure:</strong> Secure Push-back</li>`;
                    else if (nameLower.includes('tikka')) extraSpec = `<li><strong>Style:</strong> Traditional Maang Tikka</li>`;
                    
                    // Generate random but deterministic weight based on product name length
                    const weight = ((product.name.length % 15) + 8.5).toFixed(1); // slightly heavier for brass/alloy
                    
                    let specsHTML = `
                        <li><strong>Base Material:</strong> ${material}</li>
                        <li><strong>Plating:</strong> ${plating}</li>
                        <li><strong>Stones:</strong> ${stone}</li>
                        ${extraSpec}
                        <li><strong>Weight:</strong> ${weight}g</li>
                        <li style="margin-top:8px; color:var(--clr-primary); font-size:0.85rem;"><em>Care: Keep away from moisture, perfumes, and harsh chemicals to maintain plating.</em></li>
                    `;
                    
                    descEl.textContent = desc;
                    specsEl.innerHTML = specsHTML;
                }

                
                // Update thumbnails to simulate different angles
                const thumbs = document.querySelectorAll('.thumbnail');
                if(thumbs.length > 0) {
                    thumbs[0].src = product.image;
                    thumbs[0].style.transform = "scaleX(1)";
                }
                if(thumbs.length > 1) {
                    thumbs[1].src = product.image;
                    thumbs[1].style.transform = "scaleX(-1)";
                }
                if(thumbs.length > 2) {
                    thumbs[2].src = product.image;
                    thumbs[2].style.transform = "scale(1.5) translateY(10%)";
                }
                
                // Update Frequently Bought Together section
                const btItems = document.querySelectorAll('.bt-item');
                if (btItems.length >= 2) {
                    const firstImg = btItems[0].querySelector('img');
                    if (firstImg) firstImg.src = product.image;
                    
                    const relatedProduct = products.find(p => p.category === product.category && p.id !== product.id) || products[1];
                    const secondImg = btItems[1].querySelector('img');
                    const secondTextNodes = btItems[1].querySelectorAll('p');
                    
                    if (secondImg) secondImg.src = relatedProduct.image;
                    if (secondTextNodes.length >= 2) {
                        secondTextNodes[0].textContent = relatedProduct.name;
                        secondTextNodes[1].textContent = '₹' + relatedProduct.price;
                    }
                    
                    const price1 = parseInt(product.price.replace(/[^0-9]/g, ''));
                    const price2 = parseInt(relatedProduct.price.replace(/[^0-9]/g, ''));
                    const totalPrice = price1 + price2;
                    
                    const btTotalEl = document.querySelector('.bt-total .total-price');
                    if (btTotalEl) {
                        btTotalEl.textContent = '₹' + totalPrice.toLocaleString('en-IN');
                    }
                    
                    const btnAddBoth = document.querySelector('.bt-total .btn-primary');
                    if (btnAddBoth) {
                        btnAddBoth.onclick = () => {
                            window.addToCart(product.name, price1, product.image);
                            window.addToCart(relatedProduct.name, price2, relatedProduct.image);
                        };
                    }
                }
                
                // Update Related Products section
                const relatedGrid = document.querySelector('.related-products .product-grid');
                if (relatedGrid) {
                    const relatedList = products.filter(p => p.id !== product.id).slice(0, 3);
                    let relatedHTML = '';
                    relatedList.forEach(p => {
                        relatedHTML += `
                        <div class="product-card">
                            <div class="product-image">
                                <img src="${p.image}" alt="${p.name}">
                                <div class="product-actions">
                                    <button class="icon-btn" aria-label="Add to wishlist"><i class="ph ph-heart"></i></button>
                                    <button class="icon-btn" aria-label="Quick view" onclick="window.location.href='product.html?id=${p.id}'"><i class="ph ph-eye"></i></button>
                                </div>
                            </div>
                            <div class="product-info">
                                <span class="product-category">${p.category.charAt(0).toUpperCase() + p.category.slice(1)} Collection</span>
                                <a href="product.html?id=${p.id}" class="product-name">${p.name}</a>
                                <span class="product-price">₹${p.price}</span>
                            </div>
                        </div>
                        `;
                    });
                    relatedGrid.innerHTML = relatedHTML;
                }
                
                // Update Dynamic Reviews
                const reviewsList = document.getElementById('dynamic-reviews-list');
                if (reviewsList) {
                    const reviewTemplates = [
                        { title: "Absolutely Stunning!", body: "The quality is incredible. It looks like real luxury and is very high quality. I wear it everyday.", author: "Sarah M.", stars: 5, date: "October 12, 2025" },
                        { title: "Beautiful but delicate", body: "The piece itself is gorgeous. A bit delicate for my liking, but overall a great purchase for the price.", author: "Emily R.", stars: 4, date: "September 28, 2025" },
                        { title: "Exceeded my expectations", body: "I was hesitant to buy fine jewellery online, but this blew me away. The quality is immaculate.", author: "Priya S.", stars: 5, date: "November 05, 2025" },
                        { title: "Perfect gift!", body: "Bought this for my anniversary and she loved it. The packaging was also very premium.", author: "Rahul K.", stars: 5, date: "December 15, 2025" },
                        { title: "Looks expensive", body: "No one can tell this isn't real gold/diamonds. It has a beautiful weight to it.", author: "Anita D.", stars: 5, date: "January 08, 2026" },
                        { title: "So elegant", body: "Wore this to a wedding and got so many compliments. Highly recommend!", author: "Megha V.", stars: 4, date: "February 20, 2026" }
                    ];
                    
                    // Deterministic pseudo-random logic based on product name length
                    const nameLen = product.name.length;
                    const index1 = nameLen % reviewTemplates.length;
                    let index2 = (nameLen + 3) % reviewTemplates.length;
                    if (index1 === index2) index2 = (index2 + 1) % reviewTemplates.length; // Ensure they are different
                    
                    const rev1 = reviewTemplates[index1];
                    const rev2 = reviewTemplates[index2];
                    
                    const generateStars = (count) => {
                        let starsHtml = '';
                        for(let i = 0; i < 5; i++) {
                            if(i < count) starsHtml += '<i class="ph-fill ph-star"></i>';
                            else starsHtml += '<i class="ph ph-star"></i>';
                        }
                        return starsHtml;
                    };
                    
                    reviewsList.innerHTML = `
                        <div class="review-card">
                            <div class="review-header">
                                <div class="reviewer-info">
                                    <strong>${rev1.author}</strong>
                                    <span class="verified"><i class="ph-fill ph-check-circle"></i> Verified Buyer</span>
                                </div>
                                <div class="stars">${generateStars(rev1.stars)}</div>
                            </div>
                            <h4 class="review-title">${rev1.title}</h4>
                            <p class="review-body">${rev1.body}</p>
                            <span class="review-date">${rev1.date}</span>
                        </div>
                        <div class="review-card">
                            <div class="review-header">
                                <div class="reviewer-info">
                                    <strong>${rev2.author}</strong>
                                    <span class="verified"><i class="ph-fill ph-check-circle"></i> Verified Buyer</span>
                                </div>
                                <div class="stars">${generateStars(rev2.stars)}</div>
                            </div>
                            <h4 class="review-title">${rev2.title}</h4>
                            <p class="review-body">${rev2.body}</p>
                            <span class="review-date">${rev2.date}</span>
                        </div>
                    `;
                }
            }
        }
    }
});

// ==========================================
// CUSTOMER SUPPORT DRAWER LOGIC
// ==========================================

const supportContent = {
    shipping: {
        title: "Shipping & Returns",
        html: `
            <h4 style="margin-bottom: 10px; color: var(--clr-black);">Shipping Policy</h4>
            <p style="margin-bottom: 20px; color: var(--clr-dark-gray);">Shipping charges are fully included in the product price. There are no hidden fees or extra shipping costs at checkout. Orders are typically processed within 24-48 hours and delivered within 3-5 business days domestically, and 7-14 business days internationally.</p>
            
            <h4 style="margin-bottom: 10px; color: var(--clr-black);">Returns Policy</h4>
            <p style="color: var(--clr-dark-gray);">We accept returns within 7 days of delivery for store credit or exchange, provided the item is unworn and in its original packaging with tags attached. Please note that custom or personalized pieces are final sale.</p>
        `
    },
    care: {
        title: "Jewellery Care",
        html: `
            <p style="margin-bottom: 20px; color: var(--clr-dark-gray);">To maintain the brilliance and longevity of your AURA jewellery, please follow these essential care instructions:</p>
            <ul style="list-style-type: disc; margin-left: 20px; margin-bottom: 20px; color: var(--clr-dark-gray);">
                <li style="margin-bottom: 10px;">Keep away from moisture, perfumes, and harsh chemicals.</li>
                <li style="margin-bottom: 10px;">Remove jewellery before swimming, bathing, or exercising.</li>
                <li style="margin-bottom: 10px;">Store each piece individually in the provided AURA pouch to prevent scratching.</li>
                <li style="margin-bottom: 10px;">Gently clean with a soft, dry lint-free cloth after wear.</li>
            </ul>
            <p style="color: var(--clr-dark-gray);">With proper care, our original fine jewellery pieces are designed to last a lifetime.</p>
        `
    },
    faq: {
        title: "FAQ",
        html: `
            <div style="margin-bottom: 15px;">
                <strong style="color: var(--clr-black); display: block; margin-bottom: 5px;">What materials do you use?</strong>
                <p style="color: var(--clr-dark-gray); margin-bottom: 10px;">We use solid 14k/18k gold and 925 sterling silver, finished with premium rhodium or antique polish. Our stones are ethically sourced natural diamonds, rubies, and emeralds.</p>
            </div>
            <div style="margin-bottom: 15px;">
                <strong style="color: var(--clr-black); display: block; margin-bottom: 5px;">Is your jewellery hypoallergenic?</strong>
                <p style="color: var(--clr-dark-gray); margin-bottom: 10px;">Yes, all our pieces are lead and nickel-free, making them safe for sensitive skin.</p>
            </div>
            <div>
                <strong style="color: var(--clr-black); display: block; margin-bottom: 5px;">Do you offer a warranty?</strong>
                <p style="color: var(--clr-dark-gray);">We offer a 6-month warranty against manufacturing defects and plating issues under normal wear.</p>
            </div>
        `
    },
    track: {
        title: "Track Order",
        html: `
            <p style="margin-bottom: 20px; color: var(--clr-dark-gray);">Enter your order details below to check the real-time status of your shipment.</p>
            <form id="track-form" onsubmit="event.preventDefault(); alert('Tracking system is currently undergoing maintenance. Please check back later.');">
                <input type="text" placeholder="Order Number (e.g. AURA-12345)" required style="width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid var(--clr-mid-gray); border-radius: 4px; font-family: inherit;">
                <input type="email" placeholder="Email Address" required style="width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid var(--clr-mid-gray); border-radius: 4px; font-family: inherit;">
                <button type="submit" class="btn btn-primary" style="width: 100%;">Track Package</button>
            </form>
        `
    }
};

window.openSupportDrawer = function(topic) {
    const drawer = document.getElementById('support-drawer');
    const overlay = document.getElementById('support-drawer-overlay');
    const titleEl = document.getElementById('support-drawer-title');
    const contentEl = document.getElementById('support-content-container');
    
    if (drawer && overlay && supportContent[topic]) {
        titleEl.textContent = supportContent[topic].title;
        contentEl.innerHTML = supportContent[topic].html;
        
        drawer.classList.add('open');
        overlay.classList.add('active');
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const drawer = document.getElementById('support-drawer');
    const overlay = document.getElementById('support-drawer-overlay');
    const closeBtn = document.getElementById('close-support-btn');
    
    const closeDrawer = () => {
        if(drawer) drawer.classList.remove('open');
        if(overlay) overlay.classList.remove('active');
    };
    
    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    if (overlay) overlay.addEventListener('click', closeDrawer);
});

// ==========================================
// NEWSLETTER SUBSCRIPTION LOGIC
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    const newsletterForms = document.querySelectorAll('.newsletter-form');
    
    // Create a custom toast notification container if it doesn't exist
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.style.cssText = `
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 10px;
        `;
        document.body.appendChild(toastContainer);
    }

    window.showToast = function(message) {
        const toast = document.createElement('div');
        toast.style.cssText = `
            background-color: var(--clr-black);
            color: var(--clr-white);
            padding: 15px 25px;
            border-radius: 4px;
            font-family: var(--font-body);
            font-size: 0.95rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            border-left: 4px solid var(--clr-champagne);
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        `;
        
        toast.innerHTML = `<i class="ph-fill ph-check-circle" style="color: var(--clr-champagne); margin-right: 10px; vertical-align: middle; font-size: 1.2rem;"></i> <span style="vertical-align: middle;">${message}</span>`;
        
        toastContainer.appendChild(toast);
        
        // Animate in
        setTimeout(() => {
            toast.style.opacity = '1';
            toast.style.transform = 'translateY(0)';
        }, 10);
        
        // Animate out and remove
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(20px)';
            setTimeout(() => {
                toast.remove();
            }, 400);
        }, 4000);
    }

    if (newsletterForms.length > 0) {
        newsletterForms.forEach(form => {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                const emailInput = form.querySelector('input[type="email"]');
                if (emailInput && emailInput.value) {
                    window.showToast("Thank you for subscribing! You will now receive our exclusive updates.");
                    form.reset();
                }
            });
        });
    }
});

// ==========================================
// CONTACT FORM LOGIC & PROFANITY FILTER
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const formError = document.getElementById('form-error');
    
    // Simple list of inappropriate words for filtering
    const badWords = ['spam', 'scam', 'fake', 'crap', 'shit', 'fuck', 'bitch', 'ass', 'idiot', 'stupid', 'damn'];
    
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const message = document.getElementById('contact-message').value.toLowerCase();
            const subject = document.getElementById('contact-subject').value.toLowerCase();
            const name = document.getElementById('contact-name').value;
            
            // Filter check
            let hasBadWord = false;
            for (let i = 0; i < badWords.length; i++) {
                if (message.includes(badWords[i]) || subject.includes(badWords[i])) {
                    hasBadWord = true;
                    break;
                }
            }
            
            if (hasBadWord) {
                if(formError) {
                    formError.textContent = 'Your message contains inappropriate language and cannot be sent. Please revise and try again.';
                    formError.style.display = 'block';
                }
                return;
            }
            
            // Hide error if successful
            if(formError) {
                formError.style.display = 'none';
            }
            
            // Simulate successful submission
            const btn = contactForm.querySelector('button[type="submit"]');
            const originalText = btn.textContent;
            btn.textContent = 'Sending...';
            btn.disabled = true;
            
            setTimeout(() => {
                if (window.showToast) {
                    window.showToast(`Thank you ${name}! Our team will get back to you soon.`);
                } else {
                    alert(`Thank you ${name}! Our team will get back to you soon.`);
                }
                contactForm.reset();
                btn.textContent = originalText;
                btn.disabled = false;
            }, 1000);
        });
    }
});
