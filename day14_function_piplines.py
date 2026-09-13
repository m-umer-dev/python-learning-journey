sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 2, "price": 100000},
    {"product": "Mouse", "category": "Electronics", "quantity": 5, "price": 2000},
    {"product": "Keyboard", "category": "Electronics", "quantity": 3, "price": 5000},
    {"product": "Chair", "category": "Furniture", "quantity": 4, "price": 15000},
    {"product": "Desk", "category": "Furniture", "quantity": 2, "price": 30000},
    {"product": "Monitor", "category": "Electronics", "quantity": 3, "price": 25000}
]

# Ex 01
def calculate_total_quantity(sales):
    total_quantity = 0
    for sale in sales:
        total_quantity += sale["quantity"]

    return total_quantity

result = calculate_total_quantity(sales)
print("Total Quantity:",result)

# Ex 02
def calculate_total_sales(sales):
    total_sale = 0
    for sale in sales:
        total_sale += sale["price"] * sale["quantity"]

    return total_sale

result = calculate_total_sales(sales)
print("Total Sale:",result)

# Ex 03
def calculate_average_price(sales):
    total_price = 0
    for sale in sales:
        total_price += sale["price"]

    return total_price/len(sales)

result = calculate_average_price(sales)
print("Average Price:",result)

# Ex 04
def get_electronics(sales):
    filter_product = []
    for sale in sales:
        if sale["category"] == "Electronics":
            filter_product.append(sale["product"])

    return filter_product

result = get_electronics(sales)
print("Electonice Products",result)

# Ex 05
def add_total_sales(sales):
    for sale in sales:
        sale["total_sale"] = sale["price"] * sale["quantity"]

    return sales

result = add_total_sales(sales)
print(result)

# Ex 06
def get_high_sales(sales, minimum):
    filter_high = []
    for sale in sales:
        if sale["total_sale"] > minimum:
            filter_high.append(sale)

    return filter_high

result = get_high_sales(sales, 50000)
print(result)

# Ex 07
def sort_by_sales(sales):
    result = sorted(sales, key=lambda sale: sale["total_sale"], reverse=True)
    return result

result = sort_by_sales(sales)
print(result)

# Ex 08
def get_top_3_products(sales):
    result = sort_by_sales(sales)
    return result[:3]

result = get_top_3_products(sales)
print(result)

# Ex 09
def sales_summary(sales):
    total_quan = calculate_total_quantity(sales)
    total_sale = calculate_total_sales(sales)
    avg_price = calculate_average_price(sales)

    return {
        "total_quantity":total_quan,
        "total_sales":total_sale,
        "average_price":avg_price
    }
    
result = sales_summary(sales)
print(result)

# Ex 10
def analyze_sales(sales):
    sales = add_total_sales(sales)
    sales = get_high_sales(sales, 50000)
    sales = sort_by_sales(sales)

    return sales

result = analyze_sales(sales)
print(result)

# Bonus Challenge
def category_summary(sales):
    summary = {}

    for sale in sales:
        category = sale["category"]

        if category not in summary:
            summary[category] = {
                "quantity": 0,
                "sales": 0
            }

        summary[category]["quantity"] += sale["quantity"]
        summary[category]["sales"] += sale["price"] * sale["quantity"]

    return summary


result = category_summary(sales)
print(result)