css_path = 'assets/css/main.css'
with open(css_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

changes = 0

for i, line in enumerate(lines):
    original = line
    
    # BODY TEXT: line ~27 — body color should be dark
    if 'color: #84A57B;' in line and i < 30:
        line = line.replace('color: #84A57B;', 'color: #333333;')
    
    # HEADING COLOR: line ~57
    if 'color: #84A57B;' in line and 45 <= i <= 60:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # LINK HOVER: line ~44
    if 'color: #84A57B;' in line and 42 <= i <= 46:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # PRELOADER: line ~153
    if 'color: #84A57B;' in line and 150 <= i <= 160:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # PRELOADER border lines ~208, ~222
    if 'border-left: 3px solid #84A57B;' in line:
        line = line.replace('border-left: 3px solid #84A57B;', 'border-left: 3px solid #0E4935;')
    
    # .orange-text: line ~405
    if 'color: #84A57B;' in line and 403 <= i <= 407:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # .blue-bg: line ~409
    if 'background-color: #84A57B;' in line and 407 <= i <= 411:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # boxed-btn bg: line ~415
    if 'background-color: #84A57B;' in line and 413 <= i <= 418:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # bordered-btn border: line ~424
    if 'border: 2px solid #84A57B;' in line:
        line = line.replace('border: 2px solid #84A57B;', 'border: 2px solid #0E4935;')
    
    # read-more-btn: line ~431
    if 'color: #84A57B;' in line and 429 <= i <= 433:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # read-more-btn:hover: line ~439
    if 'color: #84A57B;' in line and 437 <= i <= 441:
        line = line.replace('color: #84A57B;', 'color: #1A6B4A;')
    
    # section-title underline: line ~460
    if 'background-color: #84A57B;' in line and 458 <= i <= 462:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # breadcrumb-text p color: line ~482
    if 'color: #84A57B;' in line and 480 <= i <= 484:
        line = line.replace('color: #84A57B;', 'color: #C5D9B2;')
    
    # breadcrumb overlay: line ~513
    if 'background-color: #84A57B;' in line and 510 <= i <= 516:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # navbar-nav link: line ~524
    if 'color: #84A57B;' in line and 522 <= i <= 526:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # mean-bar reveal bg: line ~629
    if 'background-color: #84A57B;' in line and 627 <= i <= 631:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # mean-container reveal color: line ~637
    if 'color: #84A57B;' in line and 635 <= i <= 639:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # mean-container reveal span bg: line ~641
    if 'background-color: #84A57B;' in line and 639 <= i <= 643:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # separate-header link: line ~678
    if 'color: #84A57B;' in line and 676 <= i <= 680:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # nav active link: line ~693
    if 'color: #84A57B;' in line and 691 <= i <= 695:
        line = line.replace('color: #84A57B;', 'color: #C5D9B2;')
    
    # nav hover link: line ~697
    if 'color: #84A57B;' in line and 695 <= i <= 699:
        line = line.replace('color: #84A57B;', 'color: #C5D9B2;')
    
    # header icons hover: line ~713
    if 'color: #84A57B;' in line and 711 <= i <= 715:
        line = line.replace('color: #84A57B;', 'color: #C5D9B2;')
    
    # sticky header bg: line ~725
    if 'background-color: #84A57B;' in line and 723 <= i <= 727:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # search overlay bg: line ~744
    if 'background-color: #84A57B;' in line and 742 <= i <= 746:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # search input border: line ~787
    if 'border-bottom: 1px solid #84A57B;' in line:
        line = line.replace('border-bottom: 1px solid #84A57B;', 'border-bottom: 1px solid #C5D9B2;')
    
    # search button bg: line ~799
    if 'background-color: #84A57B;' in line and 797 <= i <= 801:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # footer-area bg: line ~865
    if 'background-color: #84A57B;' in line and 863 <= i <= 867:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # footer widget underline: line ~884
    if 'background-color: #84A57B;' in line and 882 <= i <= 886:
        line = line.replace('background-color: #84A57B;', 'background-color: #84A57B;')  # keep accent
    
    # footer subscribe button: line ~912
    if 'background-color: #84A57B;' in line and 910 <= i <= 914:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # footer subscribe button hover: lines ~923-924
    if 'background-color: #84A57B;' in line and 921 <= i <= 925:
        line = line.replace('background-color: #84A57B;', 'background-color: #1A6B4A;')
    if 'color: #84A57B;' in line and 922 <= i <= 926:
        line = line.replace('color: #84A57B;', 'color: #fff;')
    
    # copyright bg: line ~936
    if 'background-color: #84A57B;' in line and 934 <= i <= 938:
        line = line.replace('background-color: #84A57B;', 'background-color: #0A2318;')
    
    # copyright link: line ~949
    if 'color: #84A57B;' in line and 947 <= i <= 951:
        line = line.replace('color: #84A57B;', 'color: #84A57B;')  # keep as accent
    
    # social icon number color: line ~991
    if 'color: #84A57B;' in line and 989 <= i <= 993:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # boxed-btn hover bg: line ~1016
    if 'background-color: #84A57B;' in line and 1014 <= i <= 1018:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    # boxed-btn hover color: line ~1017
    if 'color: #84A57B;' in line and 1015 <= i <= 1019:
        line = line.replace('color: #84A57B;', 'color: #fff;')
    
    # bordered-btn hover bg: line ~1027
    if 'background-color: #84A57B;' in line and 1025 <= i <= 1029:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # sub-menu hover: line ~1038
    if 'color: #84A57B;' in line and 1036 <= i <= 1040:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # tags link: line ~1060
    if 'color: #84A57B;' in line and 1058 <= i <= 1062:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # tof-btn hover: line ~1086
    if 'color: #84A57B;' in line and 1084 <= i <= 1088:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # footer pages hover: line ~1125
    if 'color: #84A57B;' in line and 1123 <= i <= 1127:
        line = line.replace('color: #84A57B;', 'color: #C5D9B2;')
    
    # footer subscribe button hover: line ~1135-1136
    if 'background-color: #84A57B;' in line and 1133 <= i <= 1137:
        line = line.replace('background-color: #84A57B;', 'background-color: #1A6B4A;')
    if 'color: #84A57B;' in line and 1134 <= i <= 1138:
        line = line.replace('color: #84A57B;', 'color: #fff;')
    
    # social icons hover: line ~1140
    if 'color: #84A57B;' in line and 1138 <= i <= 1142:
        line = line.replace('color: #84A57B;', 'color: #C5D9B2;')
    
    # social-link-team hover: lines ~1156-1157
    if 'background-color: #84A57B;' in line and 1154 <= i <= 1158:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    if 'color: #84A57B;' in line and 1155 <= i <= 1159:
        line = line.replace('color: #84A57B;', 'color: #fff;')
    
    # input submit hover: lines ~1179-1180
    if 'background-color: #84A57B;' in line and 1177 <= i <= 1181:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    if 'color: #84A57B;' in line and 1178 <= i <= 1182:
        line = line.replace('color: #84A57B;', 'color: #fff;')
    
    # pagination hover: line ~1200
    if 'background-color: #84A57B;' in line and 1198 <= i <= 1202:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # icons hover: line ~1210
    if 'color: #84A57B;' in line and 1208 <= i <= 1212:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # cart-btn hover: lines ~1247-1248
    if 'background-color: #84A57B;' in line and 1245 <= i <= 1249:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    if 'color: #84A57B;' in line and 1246 <= i <= 1250:
        line = line.replace('color: #84A57B;', 'color: #fff;')
    
    # sub-menu hover !important: line ~1268
    if 'color: #84A57B !important;' in line:
        line = line.replace('color: #84A57B !important;', 'color: #0E4935 !important;')
    
    # comment link hover: line ~1288
    if 'color: #84A57B;' in line and 1286 <= i <= 1290:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # product-share hover: line ~1298
    if 'color: #84A57B;' in line and 1296 <= i <= 1300:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # search-bar-icon hover: line ~1355
    if 'color: #84A57B;' in line and 1353 <= i <= 1357:
        line = line.replace('color: #84A57B;', 'color: #C5D9B2;')
    
    # hero-area overlay: line ~1398
    if 'background-color: #84A57B;' in line and 1396 <= i <= 1400:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # hero subtitle: line ~1404
    if 'color: #84A57B;' in line and 1402 <= i <= 1406:
        line = line.replace('color: #84A57B;', 'color: #C5D9B2;')
    
    # input submit bg: line ~1461
    if 'background-color: #84A57B;' in line and 1459 <= i <= 1463:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # single-homepage-slider bg: line ~1508
    if 'background-color: #84A57B;' in line and 1506 <= i <= 1510:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # slider overlay: line ~1519
    if 'background-color: #84A57B;' in line and 1517 <= i <= 1521:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # owl carousel nav: line ~1528 (already tracked above)
    if i >= 1526 and i <= 1530 and 'color: #84A57B;' in line:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # list icon dotted border: line ~1587
    if 'border: 2px #84A57B dotted;' in line:
        line = line.replace('border: 2px #84A57B dotted;', 'border: none;\n  background-color: rgba(14, 73, 53, 0.1);')
    if 'color: #84A57B;' in line and 1580 <= i <= 1584:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # list-section bg: line ~1558
    if 'background-color: #f5f5f5;' in line and 1556 <= i <= 1560:
        line = line.replace('background-color: #f5f5f5;', 'background-color: #FAF7F2;')
    
    # logo-carousel bg: line ~860
    if 'background-color: #f5f5f5;' in line and 858 <= i <= 862:
        line = line.replace('background-color: #f5f5f5;', 'background-color: #EBE5DB;')
    
    # footer padding: line ~867
    if 'padding: 150px 0;' in line and 863 <= i <= 870:
        line = line.replace('padding: 150px 0;', 'padding: 70px 0;')
    
    # shop banner sale-percent: line ~2140
    if 'color: #84A57B;' in line and 2138 <= i <= 2142:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # shop banner sale-percent span: line ~2147
    if 'color: #84A57B;' in line and 2145 <= i <= 2149:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # cart-btn main def bg: line ~2446
    if 'background-color: #84A57B;' in line and 2444 <= i <= 2448:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    # product card h3 color: line ~2858
    if 'color: #84A57B;' in line and 2856 <= i <= 2860:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # product card hover glow: line ~2831
    if 'rgba(132, 165, 123, 0.25)' in line:
        line = line.replace('rgba(132, 165, 123, 0.25)', 'rgba(14, 73, 53, 0.2)')
    
    # menu pills hover: line ~2967
    if 'color: #84A57B;' in line and 2965 <= i <= 2969:
        line = line.replace('color: #84A57B;', 'color: #0E4935;')
    
    # menu pills active bg: line ~2972
    if 'background-color: #84A57B;' in line and 2970 <= i <= 2974:
        line = line.replace('background-color: #84A57B;', 'background-color: #0E4935;')
    
    if line != original:
        changes += 1
    lines[i] = line

with open(css_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Line-by-line fix complete! {changes} lines changed.")
