import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace hardcoded product.html links in grid rendering
js = js.replace("onclick=\"window.location.href='product.html'\"", "onclick=\"window.location.href='product.html?id=${product.id}'\"")
js = js.replace("<a href=\"product.html\" class=\"product-name\">${product.name}</a>", "<a href=\"product.html?id=${product.id}\" class=\"product-name\">${product.name}</a>")
js = js.replace("window.location.href = 'product.html';", "window.location.href = 'product.html?id=' + (product ? product.id : item.id);")

# Add the script to handle product.html dynamic loading
init_product_code = """
document.addEventListener('DOMContentLoaded', () => {
    // ... existing init code ...
    if(window.location.pathname.includes('product.html')) {
        const urlParams = new URLSearchParams(window.location.search);
        const productId = urlParams.get('id');
        if(productId) {
            const product = products.find(p => p.id === productId);
            if(product) {
                document.querySelector('.product-title').textContent = product.name;
                document.querySelector('.product-price-large').textContent = '₹' + product.price;
                document.querySelector('#main-product-img').src = product.image;
                document.querySelector('.breadcrumbs span').textContent = product.name;
                
                // Update thumbnails to all be the same for now to avoid broken images
                const thumbs = document.querySelectorAll('.thumbnail');
                thumbs.forEach(t => t.src = product.image);
                
                // Also update the frequently bought together first item
                const btItems = document.querySelectorAll('.bt-item img');
                if(btItems.length > 0) {
                    btItems[0].src = product.image;
                }
            }
        }
    }
});
"""

if "if(window.location.pathname.includes('product.html'))" not in js:
    # Append to the end of the file
    js += init_product_code

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated script.js to support dynamic product pages.")
