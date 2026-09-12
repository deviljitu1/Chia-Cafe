import re
import glob

# 1. Update HTML files to remove Home link
html_files = glob.glob('*.html')
for filename in html_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # The Home link can have current-list-item class or not
        # Let's use regex to remove it
        # Example: <li class="current-list-item"><a href="index.html">Home</a></li>
        # Or: <li><a href="index.html">Home</a></li>
        content = re.sub(r'<li[^>]*><a href="index\.html">Home</a></li>\s*', '', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Removed Home link from {filename}")
    except Exception as e:
        print(f"Failed to process {filename}: {e}")

# 2. Update CSS to perfectly balance the 2:2 menu
css_file = 'assets/css/main.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace the margin hack
css_content = re.sub(r'nav\.main-menu ul > li:first-child\s*{\s*margin-left:\s*120px;\s*}', '', css_content)
css_content = re.sub(r'nav\.main-menu ul > li:nth-child\(2\)\s*{\s*margin-right:\s*170px;\s*}', 'nav.main-menu ul > li:nth-child(2) {\n    margin-right: 200px;\n  }', css_content)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated main.css layout for 2:2 menu split!")
