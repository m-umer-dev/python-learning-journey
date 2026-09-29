import csv


def load_sales(filename):
    sales = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sale = {
                "date": row["Date"],
                "product": row["Product"],
                "category": row["Category"],
                "quantity": int(row["Quantity"]),
                "price": int(row["Price"]),
                "city": row["City"],
                "salesperson": row["Salesperson"]
            }

            sale["revenue"] = sale["quantity"] * sale["price"]

            sales.append(sale)

    return sales


def sales_summary(sales):
    total_revenue = 0
    total_orders = len(sales)
    product_revenue = {}

    for sale in sales:
        product = sale["product"]
        revenue = sale["revenue"]

        total_revenue += revenue

        if product not in product_revenue:
            product_revenue[product] = 0

        product_revenue[product] += revenue

    top_product = max(product_revenue, key=product_revenue.get)

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "top_product": top_product
    }


def product_revenue_summary(sales):
    result = {}

    for sale in sales:
        product = sale["product"]
        revenue = sale["revenue"]

        if product not in result:
            result[product] = 0

        result[product] += revenue

    return result


def category_city_revenue(sales):
    result = {}

    for sale in sales:
        category = sale["category"]
        city = sale["city"]
        revenue = sale["revenue"]

        if category not in result:
            result[category] = {}

        if city not in result[category]:
            result[category][city] = 0

        result[category][city] += revenue

    return result


def salesperson_category_revenue(sales):
    result = {}

    for sale in sales:
        salesperson = sale["salesperson"]
        category = sale["category"]
        revenue = sale["revenue"]

        if salesperson not in result:
            result[salesperson] = {}

        if category not in result[salesperson]:
            result[salesperson][category] = 0

        result[salesperson][category] += revenue

    return result


def get_high_value_orders(sales):
    high_value_orders = []

    for sale in sales:
        if sale["revenue"] >= 50000:
            high_value_orders.append(sale)

    return high_value_orders


def high_value_revenue(sales):
    high_value_orders = get_high_value_orders(sales)

    total = 0

    for sale in high_value_orders:
        total += sale["revenue"]

    return total


def products_above_revenue(sales, minimum):
    product_revenue = product_revenue_summary(sales)

    result = {}

    for product, revenue in product_revenue.items():
        if revenue > minimum:
            result[product] = revenue

    return result


def electronics_salesperson_revenue(sales):
    result = {}

    for sale in sales:
        if sale["category"] == "Electronics":
            salesperson = sale["salesperson"]
            revenue = sale["revenue"]

            if salesperson not in result:
                result[salesperson] = 0

            result[salesperson] += revenue

    return result


def business_report(sales):
    summary = sales_summary(sales)

    return {
        "total_revenue": summary["total_revenue"],
        "total_orders": summary["total_orders"],
        "top_product": summary["top_product"],
        "category_city_revenue": category_city_revenue(sales),
        "salesperson_category_revenue": salesperson_category_revenue(sales),
        "high_value_orders": get_high_value_orders(sales),
        "high_value_revenue": high_value_revenue(sales),
        "products_above_50000": products_above_revenue(sales, 50000),
        "electronics_salesperson_revenue": electronics_salesperson_revenue(sales)
    }


def top_salesperson_by_category(sales):
    data = salesperson_category_revenue(sales)
    result = {}

    categories = set()

    for salesperson in data:
        for category in data[salesperson]:
            categories.add(category)

    for category in categories:
        category_sales = {}

        for salesperson in data:
            if category in data[salesperson]:
                category_sales[salesperson] = data[salesperson][category]

        top_salesperson = max(
            category_sales,
            key=category_sales.get
        )

        result[category] = (
            top_salesperson,
            category_sales[top_salesperson]
        )

    return result


sales = load_sales("sales_project.csv")

report = business_report(sales)

print("BUSINESS REPORT")
print("----------------")

print("Total Revenue:", report["total_revenue"])
print("Total Orders:", report["total_orders"])
print("Top Product:", report["top_product"])

print("\nCategory + City Revenue:")
print(report["category_city_revenue"])

print("\nSalesperson + Category Revenue:")
print(report["salesperson_category_revenue"])

print("\nHigh-Value Orders:")
for sale in report["high_value_orders"]:
    print(sale)

print("\nHigh-Value Revenue:")
print(report["high_value_revenue"])

print("\nProducts Above 50,000 Revenue:")
print(report["products_above_50000"])

print("\nElectronics Revenue by Salesperson:")
print(report["electronics_salesperson_revenue"])

print("\nBonus - Top Salesperson by Category:")
print(top_salesperson_by_category(sales))
