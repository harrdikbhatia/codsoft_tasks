from PIL import Image
import math
import os

source_path = r"C:\Users\hardi\.gemini\antigravity\brain\1547c0fa-d652-48dd-a691-828562c0e5a9\media__1782999223892.png"
dest_path = r"d:\E COMMERCE WEBSITE JEWELLARY\images\aura_logo_cutout.png"

# Open the image
img = Image.open(source_path)
img = img.convert("RGBA")

data = img.getdata()
new_data = []

# Get the background color from the top left corner (or assume ivory-ish)
# The image has rounded corners, so top-left might be white or transparent if it's already masked, 
# but it's likely a solid image. Let's sample a pixel slightly inward.
bg_color = img.getpixel((50, 50)) 

threshold = 25 # tolerance

for item in data:
    r, g, b, a = item
    # calculate distance
    dist = math.sqrt((r - bg_color[0])**2 + (g - bg_color[1])**2 + (b - bg_color[2])**2)
    
    if dist < threshold:
        # Make transparent
        new_data.append((r, g, b, 0))
    else:
        # If it's on the edge, we could do partial transparency (anti-aliasing)
        # but for simplicity, we'll keep it solid or apply a simple fade
        if dist < threshold + 20:
            alpha = int(255 * (dist - threshold) / 20)
            new_data.append((r, g, b, alpha))
        else:
            new_data.append(item)

img.putdata(new_data)

# Now, crop the image to the bounding box of non-transparent pixels
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# Add a little padding
padding = 20
width, height = img.size
new_img = Image.new("RGBA", (width + padding*2, height + padding*2), (0, 0, 0, 0))
new_img.paste(img, (padding, padding))

new_img.save(dest_path, "PNG")
print(f"Saved cutout to {dest_path}")
