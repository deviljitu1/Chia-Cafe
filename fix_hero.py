css_path = 'assets/css/main.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add position relative and z-index to hero text to ensure it's on top of any overlay
if 'position: relative; z-index: 99;' not in css:
    css = css.replace('.hero-text {\n  display: table;', '.hero-text {\n  display: table;\n  position: relative;\n  z-index: 99;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Hero text z-index updated!")
