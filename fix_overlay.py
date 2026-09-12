css_path = 'assets/css/main.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Reduce overlay opacity
css = css.replace('opacity: 0.7;', 'opacity: 0.4;')
css = css.replace('opacity: 0.8;', 'opacity: 0.4;')
css = css.replace('opacity: 0.9;', 'opacity: 0.4;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Overlay opacity lowered!")
