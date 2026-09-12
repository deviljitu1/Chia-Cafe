import re

# ============================================
# Update headings in index.html
# ============================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    # Hero sliders
    '<h1>Tasty Foods. Pure Drinks. Good Coffee.</h1>':
        '<h1>Tasty Foods. Pure Drinks. <span class="orange-text">Good Coffee.</span></h1>',
    '<h1>100% Vegetarian Collection</h1>':
        '<h1>100% Vegetarian <span class="orange-text">Collection</span></h1>',
    '<h1>For Friends &amp; Families</h1>':
        '<h1>For Friends &amp; <span class="orange-text">Families</span></h1>',
    # About section (already has span — keep)
    # Product section — fix the typo class_= to class=
    '<span class_="orange-text">Explore</span> Our Menu':
        '<span class="orange-text">Explore</span> Our Menu',
    # Celebrations sub-heading
    '<h4>Make Your Special Moments More Memorable</h4>':
        '<h4>Make Your Special Moments <span class="orange-text">More Memorable</span></h4>',
    # Advertisement section
    '<h2>We are <span class="orange-text">Chia Cafe</span></h2>':
        '<h2>We are <span class="orange-text">Chia Cafe</span></h2>',  # already good
    # Shop banner
    '<h3>Ready for your <span class="orange-text">next food plan?</span></h3>':
        '<h3>Ready for your <span class="orange-text">next food plan?</span></h3>',  # already good
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html headings updated!")

# ============================================
# Update headings in about.html
# ============================================
with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    '<h1>The Story of Chia Cafe</h1>':
        '<h1>The Story of <span class="orange-text">Chia Cafe</span></h1>',
    '<h3>Our Food</h3>':
        '<h3>Our <span class="orange-text">Food</span></h3>',
    '<h3>For Friends &amp; Families</h3>':
        '<h3>For Friends &amp; <span class="orange-text">Families</span></h3>',
    '<h3>Celebrations</h3>':
        '<h3><span class="orange-text">Celebrations</span></h3>',
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("about.html headings updated!")

# ============================================
# Update headings in contact.html
# ============================================
with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    '<h1>Contact Chia Cafe</h1>':
        '<h1>Contact <span class="orange-text">Chia Cafe</span></h1>',
    '<h2>Get in Touch</h2>':
        '<h2>Get in <span class="orange-text">Touch</span></h2>',
    '<h4><i class="fas fa-map"></i> Shop Address</h4>':
        '<h4><i class="fas fa-map"></i> Shop <span class="orange-text">Address</span></h4>',
    '<h4><i class="far fa-clock"></i> Shop Hours</h4>':
        '<h4><i class="far fa-clock"></i> Shop <span class="orange-text">Hours</span></h4>',
    '<h4><i class="fas fa-address-book"></i> Contact</h4>':
        '<h4><i class="fas fa-address-book"></i> <span class="orange-text">Contact</span></h4>',
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("contact.html headings updated!")

# ============================================
# Update headings in gallery.html
# ============================================
with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    '<h1>Gallery</h1>':
        '<h1><span class="orange-text">Gallery</span></h1>',
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("gallery.html headings updated!")

print("\nAll headings across all pages now have two-tone colors!")
