
data = [
 {'name': 'James Wallace', 'product': 68, 'price': 136069, 'category': 'Веб'},
 {'name': 'James Wallace', 'product': 157, 'price': 182392, 'category': 'моб'},
 {'name': 'Curtis Ray', 'product': 998, 'price': 27804, 'category': 'оконное'},
 {'name': 'James Wallace', 'product': 828, 'price': 90712, 'category': 'сайт'},
 {'name': 'Felicia Olson', 'product': 15, 'price': 127342, 'category': 'моб'},
 {'name': 'Joni Fleckenstein', 'product': 630, 'price': 154492, 'category': 'консоль'},
 {'name': 'Laura Foley', 'product': 797, 'price': 129804, 'category': 'Веб'},
 {'name': 'Adam Doyle', 'product': 1074, 'price': 133982, 'category': 'оконное'},
 {'name': 'William Carlson', 'product': 800, 'price': 87844, 'category': 'сайт'},
 {'name': 'James Wallace', 'product': 210, 'price': 166251, 'category': 'сервер'},
 {'name': 'Shyla Brown', 'product': 711, 'price': 102940, 'category': 'моб'},
 {'name': 'Rodney Dankert', 'product': 278, 'price': 106846, 'category': 'оконное'},
 {'name': 'Christina Haddad', 'product': 205, 'price': 11107, 'category': 'сервер'},
 {'name': 'William Carlson', 'product': 264, 'price': 53204, 'category': 'Веб'},
 {'name': 'James Wallace', 'product': 1049, 'price': 138668, 'category': 'моб'},
 {'name': 'Adeline Brann', 'product': 971, 'price': 139399, 'category': 'сайт'},
 {'name': 'Nancy Sanchez', 'product': 1088, 'price': 117700, 'category': 'моб'},
 {'name': 'Rodney Rollins', 'product': 370, 'price': 185819, 'category': 'оконное'},
 {'name': 'Charles Gentges', 'product': 196, 'price': 191932, 'category': 'моб'},
 {'name': 'Jonas Harris', 'product': 1030, 'price': 117724, 'category': 'моб'},
 {'name': 'Diane Chiodo', 'product': 508, 'price': 58784, 'category': 'сервер'},
 {'name': 'Debra Ashcraft', 'product': 133, 'price': 100704, 'category': 'моб'},
 {'name': 'James Wallace', 'product': 794, 'price': 178368, 'category': 'Веб'},
 {'name': 'Eric Hernandez', 'product': 776, 'price': 65141, 'category': 'моб'},
 {'name': 'Eugene Watson', 'product': 287, 'price': 59846, 'category': 'Веб'},
 {'name': 'Keith Brown', 'product': 947, 'price': 130215, 'category': 'оконное'},
 {'name': 'James Wallace', 'product': 1071, 'price': 165618, 'category': 'консоль'},
 {'name': 'Linda Williams', 'product': 175, 'price': 7529, 'category': 'Веб'},
 {'name': 'Tyler Mann', 'product': 493, 'price': 48993, 'category': 'консоль'},
 {'name': 'Fred Pitcak', 'product': 702, 'price': 59533, 'category': 'консоль'},
 {'name': 'Paul Hufft', 'product': 426, 'price': 123595, 'category': 'Веб'},
 {'name': 'Margaret Gagnon', 'product': 849, 'price': 111315, 'category': 'консоль'},
 {'name': 'Kathy Clark', 'product': 157, 'price': 4820, 'category': 'консоль'},
 {'name': 'Laura Foley', 'product': 292, 'price': 95077, 'category': 'моб'},
 {'name': 'Keith Brown', 'product': 186, 'price': 110273, 'category': 'консоль'},
 {'name': 'Keith Brown', 'product': 831, 'price': 128506, 'category': 'моб'},
 {'name': 'Keith Brown', 'product': 123, 'price': 21833, 'category': 'оконное'},
 {'name': 'James Wallace', 'product': 63, 'price': 24982, 'category': 'Веб'}
]



customer_categories = {}
for entry in data:
    name = entry['name']
    category = entry['category']
    if name in customer_categories:
        customer_categories[name].add(category)
    else:
        customer_categories[name] = {category}


for name, categories in customer_categories.items():
    if len(categories) > 2:
        print(f"Заказчик {name} требует разработку продуктов в категориях {categories}.")
