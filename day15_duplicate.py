sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 2, "price": 100000},
    {"product": "Mouse", "category": "Electronics", "quantity": 5, "price": 2000},
    {"product": "Keyboard", "category": "Electronics", "quantity": 3, "price": 5000},
    {"product": "Chair", "category": "Furniture", "quantity": 4, "price": 15000},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 30000},
    {"product": "Monitor", "category": "Electronics", "quantity": 3, "price": 25000}
]

# Ex 01
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
print(set(numbers))

# Ex 02
result = []
for sale in sales:
    result.append(sale["category"])

print("Unique Category:",set(result))

# Ex 03
uniq_products = {sale["product"] for sale in sales}
print("Unique Products:",uniq_products)

# Ex 04
uniq_price = {sale["price"] for sale in sales}
print("Unique Prices:",uniq_price)

# Ex 05
customers = [
    {"name": "Ali", "city": "Lahore"},
    {"name": "Umer", "city": "Lahore"},
    {"name": "Ahmed", "city": "Karachi"},
    {"name": "Zain", "city": "Islamabad"},
    {"name": "Sara", "city": "Lahore"},
    {"name": "Hamza", "city": "Karachi"}
]
uniq_city = {customer["city"] for customer in customers}
print("Unique City:",uniq_city)

# Ex 06
uniq_category = {sale["category"] for sale in sales}
print("Unique Category:",uniq_category)

# Ex 07
store_a = {"Electronics", "Furniture", "Clothing", "Books"}
store_b = {"Electronics", "Books", "Sports", "Furniture"}

print(store_a & store_b)

# Ex 08
print(store_a - store_b)

# Ex 09
print(store_a | store_b)

# Ex 10
def get_unique_cities(customers):
    result = {customer["city"] for customer in customers}
    return result

result = get_unique_cities(customers)
print("Unique City", result)

# Bonus Challenge
def get_unique_categories(sales):
    unique_category = {sale["category"] for sale in sales}
    return unique_category

def count_unique_categories(sales):
    count_uniq_category = get_unique_categories(sales)
    return len(count_uniq_category)

result = get_unique_categories(sales)
result1 = count_unique_categories(sales)
print(result)
print(result1)