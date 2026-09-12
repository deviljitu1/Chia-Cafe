import os
from bs4 import BeautifulSoup

def update_header_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Update title
    if soup.title:
        soup.title.string = "Chia Cafe"

    # Update Header
    main_menu = soup.find('nav', class_='main-menu')
    if main_menu:
        ul = main_menu.find('ul')
        if ul:
            ul.clear()
            
            nav_items = [
                ("Home", "index.html"),
                ("About Us", "about.html"),
                ("Our Menu", "menu.html"),
                ("Gallery", "gallery.html"),
                ("Contact Us", "contact.html")
            ]
            for name, link in nav_items:
                li = soup.new_tag('li')
                if os.path.basename(filepath) == link:
                    li['class'] = 'current-list-item'
                a = soup.new_tag('a', href=link)
                a.string = name
                li.append(a)
                ul.append(li)

    # Update Footer
    footer_area = soup.find('div', class_='footer-area')
    if footer_area:
        row = footer_area.find('div', class_='row')
        if row:
            row.clear()
            
            # About Widget
            col1 = soup.new_tag('div', attrs={'class': 'col-lg-3 col-md-6'})
            box1 = soup.new_tag('div', attrs={'class': 'footer-box about-widget'})
            h2_1 = soup.new_tag('h2', attrs={'class': 'widget-title'})
            h2_1.string = "CHIA CAFE"
            p1_1 = soup.new_tag('p')
            p1_1.string = "Tasty Foods. Pure Drinks. Good Coffee."
            p1_2 = soup.new_tag('p')
            p1_2.string = "A vibrant restaurant-cum-café in Avanti Vihar, Raipur, serving vegetarian favourites, refreshing beverages, good coffee and memorable café experiences."
            box1.extend([h2_1, p1_1, p1_2])
            col1.append(box1)
            
            # Quick Links
            col2 = soup.new_tag('div', attrs={'class': 'col-lg-3 col-md-6'})
            box2 = soup.new_tag('div', attrs={'class': 'footer-box pages'})
            h2_2 = soup.new_tag('h2', attrs={'class': 'widget-title'})
            h2_2.string = "Quick Links"
            ul2 = soup.new_tag('ul')
            for name, link in nav_items:
                li2 = soup.new_tag('li')
                a2 = soup.new_tag('a', href=link)
                a2.string = name
                li2.append(a2)
                ul2.append(li2)
            box2.extend([h2_2, ul2])
            col2.append(box2)
            
            # Contact
            col3 = soup.new_tag('div', attrs={'class': 'col-lg-3 col-md-6'})
            box3 = soup.new_tag('div', attrs={'class': 'footer-box get-in-touch'})
            h2_3 = soup.new_tag('h2', attrs={'class': 'widget-title'})
            h2_3.string = "Contact"
            ul3 = soup.new_tag('ul')
            li3_1 = soup.new_tag('li')
            li3_1.string = "Global Enclave, near Vijay Nagar Chowk, Avanti Vihar, Sector 2, Shankar Nagar, Raipur, Chhattisgarh 492001"
            li3_2 = soup.new_tag('li')
            li3_2.string = "091555 15655"
            ul3.extend([li3_1, li3_2])
            box3.extend([h2_3, ul3])
            col3.append(box3)
            
            # Footer CTA
            col4 = soup.new_tag('div', attrs={'class': 'col-lg-3 col-md-6'})
            box4 = soup.new_tag('div', attrs={'class': 'footer-box subscribe'})
            h2_4 = soup.new_tag('h2', attrs={'class': 'widget-title'})
            h2_4.string = "Hungry?"
            p4 = soup.new_tag('p')
            p4.string = "Come say Chia."
            a4_1 = soup.new_tag('a', href='menu.html', attrs={'class': 'boxed-btn mb-2 d-block'})
            a4_1.string = "Explore Menu"
            a4_2 = soup.new_tag('a', href='contact.html', attrs={'class': 'bordered-btn d-block'})
            a4_2.string = "Contact Us"
            box4.extend([h2_4, p4, a4_1, a4_2])
            col4.append(box4)
            
            row.extend([col1, col2, col3, col4])

    # Copyright
    copyright_area = soup.find('div', class_='copyright')
    if copyright_area:
        p_copy = copyright_area.find('p')
        if p_copy:
            p_copy.clear()
            p_copy.append("© Chia Cafe. All Rights Reserved.")
            br = soup.new_tag('br')
            p_copy.append(br)
            p_copy.append("Good Food. Great Vibes. Everyday.")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

files = ['index.html', 'about.html', 'menu.html', 'gallery.html', 'contact.html']
for file in files:
    if os.path.exists(file):
        update_header_footer(file)
        print(f"Updated {file}")
