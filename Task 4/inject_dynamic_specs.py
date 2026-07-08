import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = "document.querySelector('.breadcrumbs span').textContent = product.name;"

dynamic_logic = """
                // Dynamic Description and Specs
                const descEl = document.querySelector('.product-desc');
                const specsEl = document.querySelector('.accordion-content ul');
                
                if (descEl && specsEl) {
                    let desc = `Elevate your everyday style with our beautiful ${product.name}. Carefully crafted to catch the light from every angle, this timeless piece is a staple for any jewelry collection.`;
                    
                    const nameLower = product.name.toLowerCase();
                    
                    // Material logic
                    let material = "Premium Alloy";
                    if (product.category === 'silver' || nameLower.includes('silver')) material = "925 Sterling Silver";
                    if (product.category === 'gold' || nameLower.includes('gold') || nameLower.includes('kundan')) material = "22k Gold Plated";
                    if (nameLower.includes('24k')) material = "24k Pure Gold";
                    
                    // Stone logic
                    let stone = "None";
                    if (nameLower.includes('zircon') || nameLower.includes('crystal') || nameLower.includes('diamond') || product.category === 'diamond') stone = "AAAA Grade Cubic Zirconia";
                    if (nameLower.includes('kundan')) stone = "Uncut Kundan Stones";
                    if (nameLower.includes('ruby')) stone = "Lab-created Ruby";
                    if (nameLower.includes('emerald') || nameLower.includes('green')) stone = "Emerald Simulant";
                    
                    // Type specific logic
                    let extraSpec = "";
                    if (nameLower.includes('ring')) extraSpec = `<li><strong>Size:</strong> Adjustable (US 5 to 9)</li>`;
                    else if (nameLower.includes('necklace') || nameLower.includes('pendant') || nameLower.includes('choker')) extraSpec = `<li><strong>Length:</strong> 16" with 2" extender</li>`;
                    else if (nameLower.includes('bracelet') || nameLower.includes('bangle') || nameLower.includes('kada')) extraSpec = `<li><strong>Diameter:</strong> 2.4 / 2.6 inches</li>`;
                    else if (nameLower.includes('earring') || nameLower.includes('jhumka') || nameLower.includes('stud')) extraSpec = `<li><strong>Closure:</strong> Secure Push-back</li>`;
                    else if (nameLower.includes('tikka')) extraSpec = `<li><strong>Style:</strong> Traditional Maang Tikka</li>`;
                    
                    // Generate random but deterministic weight based on product name length so it stays constant for the same product
                    const weight = ((product.name.length % 10) + 2.5).toFixed(1);
                    
                    let specsHTML = `
                        <li><strong>Material:</strong> ${material}</li>
                        <li><strong>Stone:</strong> ${stone}</li>
                        ${extraSpec}
                        <li><strong>Weight:</strong> ${weight}g</li>
                    `;
                    
                    descEl.textContent = desc;
                    specsEl.innerHTML = specsHTML;
                }
"""

if target in js:
    new_js = js.replace(target, target + dynamic_logic)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Injected dynamic specs generator successfully.")
else:
    print("Could not find the target string in script.js to inject logic.")
