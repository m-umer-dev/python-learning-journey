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

# Ex 02
count_quantity = {}

for sale in sales:
    category = sale["category"]

    if category not in count_quantity:
        count_quantity[category] = 0

    count_quantity[category] += sale["quantity"]

print(count_quantity)

# Ex 03 & 05 & 06
count_sale = {}

for sale in sales:
    category = sale["category"]
    total = sale["quantity"] * sale["price"]

    if category not in count_sale:
        count_sale[category] = 0

    count_sale[category] += total

print(count_sale)

highest = 0
lowest = float("inf")

for key, value in count_sale.items():
    if value > highest:
        highest = value
        high_product_name = key

    if value < lowest:
        lowest = value
        low_product_name = key

print("Higest Sale:",high_product_name)
print("Lowest Sale",low_product_name)

# Ex 04
product_sale = {}


for sale in sales:
    product = sale["product"]
    total = sale["quantity"] * sale["price"]
    product_sale[product] = total

print(product_sale)

# Ex 07
avg_price = 0
total = 0

for sale in sales:
    total += sale["price"]

avg_price = total/len(sales)
print(avg_price)

# Ex 08
count_sale = {}
total_per_cat = {}
avg_per_cat = {}

for sale in sales:
    category = sale["category"]
    total = sale["quantity"] * sale["price"]

    if category not in count_sale:
        count_sale[category] = 0
        total_per_cat[category] = 0

    count_sale[category] += 1
    total_per_cat[category] += total

for key, value in count_sale.items():
    avg_per_cat[key] = total_per_cat[key]/value

print(avg_per_cat)

# Ex 09
def category_sales_summary(sales):
    count_sale = {}

    for sale in sales:
        category = sale["category"]
        total = sale["quantity"] * sale["price"]

        if category not in count_sale:
            count_sale[category] = 0

        count_sale[category] += total

    return count_sale

count_sale = category_sales_summary(sales)
print(count_sale)

# Ex 10
def analyze_categories(sales):
    result = {}
    for sale in sales:
        category = sale["category"]
        if category not in result:
            result[category] = {
                "products": 0,
                "quantity": 0,
                "sales": 0
            }
            
        result[category]["products"] += 1
        result[category]["quantity"] += sale["quantity"]
        result[category]["sales"] += sale["quantity"] * sale["price"]

    return result

result = analyze_categories(sales)
print(result)