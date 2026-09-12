import os
from bs4 import BeautifulSoup

def build_menu(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Update Breadcrumb
    breadcrumb = soup.find('div', class_='breadcrumb-text')
    if breadcrumb:
        p = breadcrumb.find('p')
        if p: p.string = "Tasty Foods. Pure Drinks. Good Coffee."
        h1 = breadcrumb.find('h1')
        if h1: h1.string = "Explore Our Menu"

    # Define Menu Categories
    menu_data = [
        ("Starter", "Start with something delicious.", ["Paneer Tikka - 6 pcs", "Crispy Corn", "Veg Manchurian Dry", "Chilli Paneer Dry", "Mushroom Chilli Dry", "Honey Chilli Potato", "Crispy Corn Pepper Salt", "Veg Spring Rolls", "Paneer 65"]),
        ("South Indian", "Crispy dosas, comforting classics and familiar favourites.", ["Idli - 3 pcs", "Vada - 2 pcs", "Idli Vada", "Plain Dosa", "Masala Dosa", "Onion Dosa", "Cheese Dosa", "Onion Uttapam", "Rava Kesari"]),
        ("Pizza", "Cheesy, comforting and made for sharing.", ["Onion Capsicum Pizza", "Margherita Pizza", "Cheese & Corn Pizza", "Veggie Loaded Pizza"]),
        ("Burger & Fries", "Perfect for quick bites and casual hangouts.", ["Aloo Tikki Burger", "Salted Fries", "Peri Peri Fries", "Cheesy Fries"]),
        ("Sandwich", "Simple café favourites for any time of the day.", ["Veg Grilled Sandwich", "Cheese & Corn Sandwich"]),
        ("Pasta", "Creamy, comforting pasta favourites.", ["White Sauce Pasta", "Red Sauce Pasta"]),
        ("Indian Snacks", "Classic evening snacks and favourites.", ["Paneer Pakoda", "Chole Bhature", "Bedami Poori Sabji", "Pao Bhaji", "Pyaz Pakoda"]),
        ("Chinese", "Big flavours for your Chinese cravings.", ["Hakka Noodles", "Garlic Noodles", "Veg Fried Rice", "Schezwan Fried Rice", "Garlic Fried Rice"]),
        ("Rice & Noodles", "Comforting rice and noodle dishes for every craving.", ["Masala Maggi", "Vegetable Maggi", "Veg Cheese Maggi", "Steamed Rice", "Jeera Rice", "Veg Hakka Noodles", "Veg Schezwan Noodles", "Chilli Garlic Noodles", "Veg Fried Rice", "Veg Manchurian Gravy", "Chilli Paneer Gravy", "Paneer in Schezwan Sauce"]),
        ("Main Course", "Rich, comforting Indian favourites.", ["Dal Makhani", "Dal Tadka", "Mix Vegetable", "Aloo Gobhi Adraki", "Malai Kofta", "Paneer Butter Masala", "Paneer Lababdar", "Kadhai Paneer", "Paneer Do Pyaza", "Shahi Paneer", "Palak Paneer", "Matar Paneer", "Paneer Bhurji"]),
        ("Bread Basket", "Complete your Indian meal with your choice of breads.", ["Tava Roti", "Tandoori Roti", "Butter Roti", "Butter Naan", "Garlic Naan", "Lacha Paratha", "Aloo Paratha", "Aloo Pyaaz Paratha", "Paneer Paratha", "Paneer Pyaaz Paratha"]),
        ("Dim Sums & Momos", "Steam or fry - choose your favourite.", ["Veg Steamed Momos", "Veg Fried Momos"]),
        ("Sides", "Simple sides to complete the table.", ["Boondi Raita", "Masala Papad", "Green Salad"]),
        ("Soups", "Warm and comforting bowls.", ["Tomato Soup", "Manchow Soup", "Sweet Corn Soup", "Lemon Coriander Soup"]),
        ("Indian Combos", "Complete meal options for when you want something satisfying.", ["Tandoori Thali", "Thali", "Kadhi Rice", "Rajma Rice", "Chole Rice"]),
        ("Chinese Combos", "Easy combinations for a complete Chinese meal.", ["Noodles + Manchurian", "Fried Rice + Manchurian", "Noodles + Chilly Paneer", "Fried Rice + Chilly Paneer"]),
        ("Beverages & Shakes", "From chai and coffee to indulgent shakes and refreshing coolers.", ["Chai", "Hot Coffee", "Fresh Lime Soda", "Masala Chaas", "Filter Coffee", "KitKat Shake", "Oreo Shake", "Chocolate Shake", "Vanilla Shake", "Cold Coffee", "Cold Coffee with Ice-Cream", "Mojito", "Lemon Ice Tea", "Lemon Soda", "Lassi (Sweet)", "Jamun Shots", "Mango Shake", "Banana Shake", "Sitafal Shake", "Jamfal Shake"]),
        ("Fresh Juices", "Refresh yourself with fruit favourites.", ["Anar", "Mausambi", "Orange", "Pineapple", "Watermelon", "Bel Panna", "Aam Panna", "Grapes", "Mix Fruit"])
    ]

    # Find product section
    product_section = soup.find('div', class_='product-section')
    if product_section:
        container = product_section.find('div', class_='container')
        if container:
            container.clear()
            
            # Add intro text
            intro_row = soup.new_tag('div', attrs={'class': 'row'})
            intro_col = soup.new_tag('div', attrs={'class': 'col-lg-8 offset-lg-2 text-center mb-5'})
            intro_title = soup.new_tag('div', attrs={'class': 'section-title'})
            intro_h3 = soup.new_tag('h3')
            intro_h3.append(soup.new_tag('span', attrs={'class': 'orange-text'}))
            intro_h3.span.string = "Our"
            intro_h3.append(" Menu")
            intro_p = soup.new_tag('p')
            intro_p.string = "From quick bites and evening snacks to complete meals and refreshing drinks, our menu brings together a wide selection of vegetarian favourites."
            intro_p2 = soup.new_tag('p')
            intro_p2.string = "Choose a classic, try something new or order a little of everything for the table."
            
            intro_title.extend([intro_h3, intro_p, intro_p2])
            intro_col.append(intro_title)
            intro_row.append(intro_col)
            container.append(intro_row)
            
            # Add Categories
            for cat_name, cat_desc, items in menu_data:
                # Category Header
                cat_row = soup.new_tag('div', attrs={'class': 'row mt-5'})
                cat_col = soup.new_tag('div', attrs={'class': 'col-lg-12'})
                cat_h4 = soup.new_tag('h4', attrs={'class': 'pb-2', 'style': 'border-bottom: 2px solid #F28123; color: #051922;'})
                cat_h4.string = cat_name
                cat_p = soup.new_tag('p', attrs={'class': 'text-muted'})
                cat_p.string = cat_desc
                cat_col.extend([cat_h4, cat_p])
                cat_row.append(cat_col)
                container.append(cat_row)
                
                # Items
                items_row = soup.new_tag('div', attrs={'class': 'row mb-4'})
                for item in items:
                    item_col = soup.new_tag('div', attrs={'class': 'col-lg-4 col-md-6 mb-3'})
                    item_box = soup.new_tag('div', attrs={'class': 'p-3', 'style': 'background: #f9f9f9; border-radius: 5px;'})
                    item_h5 = soup.new_tag('h5', attrs={'class': 'm-0', 'style': 'font-size: 1.1rem;'})
                    item_h5.string = item
                    item_box.append(item_h5)
                    item_col.append(item_box)
                    items_row.append(item_col)
                
                container.append(items_row)
            
            # Closing
            closing_row = soup.new_tag('div', attrs={'class': 'row mt-5 pt-5', 'style': 'border-top: 1px solid #ddd;'})
            closing_col = soup.new_tag('div', attrs={'class': 'col-lg-8 offset-lg-2 text-center'})
            closing_h3 = soup.new_tag('h3')
            closing_h3.string = "Not sure what to order?"
            closing_p = soup.new_tag('p')
            closing_p.string = "Start with a favourite, add something to share and finish with a cold coffee or shake. Whether you're visiting for snacks, lunch, dinner or a casual coffee, there is always something to try at Chia Cafe."
            closing_btns = soup.new_tag('div', attrs={'class': 'mt-4'})
            closing_btn1 = soup.new_tag('a', href='#', attrs={'class': 'boxed-btn mr-3'})
            closing_btn1.string = "Order Online"
            closing_btn2 = soup.new_tag('a', href='contact.html', attrs={'class': 'bordered-btn'})
            closing_btn2.string = "Contact Us"
            
            closing_btns.extend([closing_btn1, closing_btn2])
            closing_col.extend([closing_h3, closing_p, closing_btns])
            closing_row.append(closing_col)
            container.append(closing_row)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

if os.path.exists('menu.html'):
    build_menu('menu.html')
    print("Updated menu.html")
