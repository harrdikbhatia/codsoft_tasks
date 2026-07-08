import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_logic = """                    // Material logic
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
                    `;"""


new_logic = """                    // Material & Plating logic (Artificial/Imitation Jewellery)
                    let material = "High-Quality Brass Alloy";
                    let plating = "Premium Plating";
                    
                    if (product.category === 'silver' || nameLower.includes('silver')) {
                        material = "German Silver Alloy";
                        plating = "Oxidised Silver Finish";
                        if (nameLower.includes('925') || nameLower.includes('sparkling')) plating = "Rhodium Plating";
                    }
                    if (product.category === 'gold' || nameLower.includes('gold') || nameLower.includes('kundan')) {
                        material = "Copper-Brass Alloy";
                        plating = "18k Gold Plating (Micro-plated)";
                        if (nameLower.includes('antique') || nameLower.includes('vintage')) plating = "Antique Matte Gold Finish";
                    }
                    
                    // Stone logic
                    let stone = "No Stones";
                    if (nameLower.includes('zircon') || nameLower.includes('crystal') || nameLower.includes('diamond') || product.category === 'diamond') stone = "Premium American Diamonds (AD) / CZ";
                    if (nameLower.includes('kundan')) stone = "Synthetic Kundan / Glass Stones";
                    if (nameLower.includes('ruby')) stone = "Faux Ruby / Monalisa Stones";
                    if (nameLower.includes('emerald') || nameLower.includes('green')) stone = "Faux Emerald";
                    
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
                    `;"""

if old_logic in js:
    new_js = js.replace(old_logic, new_logic)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Replaced logic successfully!")
else:
    print("Could not find old logic in script.js")
