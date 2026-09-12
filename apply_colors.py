import os
import re

css_path = 'assets/css/main.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace dark blue/black with forest green
css = css.replace('#051922', '#0C2B1D')

# Append body background if not already there
if '#FAF7F2' not in css:
    css += "\n\n/* Custom Cafe Colors */\nbody { background-color: #FAF7F2; }\nh1, h2, h3, h4, h5, h6 { color: #0C2B1D; }\n"

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update HTML files just in case there are inline colors
html_files = ['index.html', 'about.html', 'menu.html', 'gallery.html', 'contact.html']
for hf in html_files:
    if os.path.exists(hf):
        with open(hf, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Replace inline styles or classes if needed
        html = html.replace('#051922', '#0C2B1D')
        html = html.replace('background-color: #FAFAFA;', 'background-color: #FAF7F2;')
        html = html.replace('background-color: #f5f5f5;', 'background-color: #FAF7F2;')
        
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(html)

print("Colors applied successfully!")
