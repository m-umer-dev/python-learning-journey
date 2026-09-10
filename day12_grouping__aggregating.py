sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 2, "price": 100000},
    {"product": "Mouse", "category": "Electronics", "quantity": 5, "price": 2000},
    {"product": "Keyboard", "category": "Electronics", "quantity": 3, "price": 5000},
    {"product": "Chair", "category": "Furniture", "quantity": 4, "price": 15000},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 30000},
    {"product": "Monitor", "category": "Electronics", "quantity": 3, "price": 25000}
]

# Ex 01
count_category = {}

for sale in sales:
    category = sale["category"]

    if category not in count_category:
        count_category[category] = 0

    count_category[category] += 1

print(count_category)