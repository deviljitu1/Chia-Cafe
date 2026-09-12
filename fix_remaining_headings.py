import re
import glob

# The files that still have single-color h1 tags based on our grep output:
files_to_fix = [
    '404.html',
    'cart.html',
    'checkout.html',
    'news.html',
    'shop.html',
    'single-news.html',
    'single-product.html'
]

replacements = {
    '<h1>404 - Not Found</h1>': '<h1>404 - <span class="orange-text">Not Found</span></h1>',
    '<h1>Oops! Not Found.</h1>': '<h1>Oops! <span class="orange-text">Not Found.</span></h1>',
    '<h1>Cart</h1>': '<h1><span class="orange-text">Cart</span></h1>',
    '<h1>Check Out Product</h1>': '<h1>Check Out <span class="orange-text">Product</span></h1>',
    '<h1>News Article</h1>': '<h1>News <span class="orange-text">Article</span></h1>',
    '<h1>Shop</h1>': '<h1><span class="orange-text">Shop</span></h1>',
    '<h1>Single Article</h1>': '<h1>Single <span class="orange-text">Article</span></h1>',
    '<h1>Single Product</h1>': '<h1>Single <span class="orange-text">Product</span></h1>',
}

for filename in files_to_fix:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated headings in {filename}")
    except Exception as e:
        print(f"Failed to process {filename}: {e}")
