import re

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find all <h3> tags with the specific style
# <h3 style='font-family: "Fredoka", sans-serif; color: #84A57B; font-weight: 600; font-size: 2rem;'>Starter</h3>
# And replace the color with #0E4935, and wrap the last word in <span class="orange-text">

def replacer(match):
    prefix = match.group(1) # <h3 style='...'
    text = match.group(2)   # Starter
    suffix = match.group(3) # </h3>
    
    # Change the color to dark green
    new_prefix = prefix.replace('color: #84A57B;', 'color: #0E4935;')
    
    # Split text by space
    words = text.split()
    if len(words) == 1:
        # If 1 word, just wrap it in orange-text to keep it light green, or maybe dark green?
        # Let's make the first half of the word dark and second half light? No, that's weird.
        # Let's just make it dark green with light green span for the whole word.
        new_text = f'<span class="orange-text">{text}</span>'
    else:
        # If multiple words, split in half
        mid = len(words) // 2
        first_half = ' '.join(words[:mid])
        second_half = ' '.join(words[mid:])
        new_text = f'{first_half} <span class="orange-text">{second_half}</span>'
        
    return f"{new_prefix}{new_text}{suffix}"

# Regex to match the h3 tags
pattern = re.compile(r"(<h3[^>]*style=['\"][^>]*color:\s*#84A57B[^>]*>)(.*?)(</h3>)", re.IGNORECASE)

new_content = pattern.sub(replacer, content)

# There is also one h3 that might have been missed or have different color, let's check for any h3 in menu-category-header
# Let's also fix the main headings in menu.html if they exist (e.g. "Our Menu")

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("menu.html headings updated!")
