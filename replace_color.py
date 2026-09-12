import os

def replace_color_in_file(filepath, old_colors, new_color):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for old_color in old_colors:
        content = content.replace(old_color, new_color)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated colors in {filepath}")
    else:
        print(f"No colors updated in {filepath}")

if __name__ == "__main__":
    css_file = 'assets/css/main.css'
    old_colors = ['#F28123', '#f28123']
    new_color = '#0E4935' # Dark Green from the menu
    
    replace_color_in_file(css_file, old_colors, new_color)
    
    # Also update any inline styles in HTML files if necessary (e.g., about.html, menu.html, etc.)
    html_files = ['index.html', 'about.html', 'menu.html', 'gallery.html', 'contact.html']
    for file in html_files:
        if os.path.exists(file):
            replace_color_in_file(file, old_colors, new_color)
