sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 2, "price": 100000},
    {"product": "Mouse", "category": "Electronics", "quantity": 5, "price": 2000},
    {"product": "Keyboard", "category": "Electronics", "quantity": 3, "price": 5000},
    {"product": "Chair", "category": "Furniture", "quantity": 4, "price": 15000},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 30000},
    {"product": "Monitor", "category": "Electronics", "quantity": 3, "price": 25000}
]

# Ex 01 & 02
numbers = [45, 12, 89, 23, 5, 67]
small_to_large = sorted(numbers)
large_to_small = sorted(numbers,reverse=True)
print(small_to_large)
print(large_to_small)

# Ex 03 & 04
price_large = sorted(sales, key=lambda sale: sale["price"])
price_small = sorted(sales, key=lambda sale: sale["price"], reverse=True)
print(price_large)
print(price_small)

# Ex 05 & 06
cheap_pro = min(sales, key=lambda sale: sale["price"])
exp_pro = max(sales, key=lambda sale: sale["price"])
print(cheap_pro)
print(exp_pro)

# Ex 07
three_exp_pro = sorted(sales, key=lambda sale: sale["price"], reverse=True)
print(three_exp_pro[:3])

# Ex 08
sort_quan = sorted(sales, key=lambda sale: sale["quantity"],reverse=True)
print(sort_quan)

# Ex 09
sort_total = sorted(sales, key=lambda sale: sale["quantity"] * sale["price"], reverse=True)
print(sort_total)

# Ex 10
def top_selling_product(sales):
    top_sell_pro = max(sales, key=lambda sale: sale["quantity"] * sale["price"])
    return top_sell_pro

result = top_selling_product(sales)
print(result)

# Bonus Challenge
def top_3_products(sales):
    three_exp_pro = sorted(sales, key=lambda sale: sale["quantity"] * sale["price"], reverse=True)
    return three_exp_pro[:3]

pro_result = top_3_products(sales)
print(pro_result)