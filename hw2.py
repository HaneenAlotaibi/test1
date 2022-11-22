from csv import DictReader

categories = {}
with open('category.csv', 'r', encoding='utf-8-sig') as category_file:
    rows = DictReader(category_file)
    for row in rows:
        categories[row['pk']] = {
            'name': row['name'],
        }

subcategories = {}
with open('subcategories.csv', 'r', encoding='utf-8-sig') as subcategories_file:
    rows = DictReader(subcategories_file)
    for row in rows:
        subcategories[row['pk']] = {
            'name': row['name'],
            'fk': row['fk'],
        }

brands = {}
with open('brands.csv', 'r', encoding='utf-8-sig') as brands_file:
    rows = DictReader(brands_file)
    for row in rows:
        brands[row['pk']] = {
            'name': row['name'],
            'fk': row['fk'],
        }

products = {}
with open('products.csv', 'r', encoding='utf-8-sig') as products_file:
    rows = DictReader(products_file)
    for row in rows:
        products[row['pk']] = {
            'name': row['name'],
            'description': row['description'],
            'price': row['price'],
            'quantity': int(row['quantity']),
            'image_name': row['image_name'],
            'fk': row['fk'],
        }

for product in products.values():
    brand = brands[product['fk']]
    subcategory = subcategories[brand['fk']]
    category = categories[subcategory['fk']]
    product_details = f"{product['name']} - ${product['price']} ({product['description']})"
    print(f"{category['name']} -> {subcategory['name']} -> {brand['name']} -> {product_details}")
    if product['image_name'] == '':
        print('Error: Missing image name.')
    if product['quantity'] > 3:
        print('Error: Quantity can not be more than three.')
