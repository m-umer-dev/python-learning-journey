import csv


def load_sales(filename):
    sales = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            quantity = int(row["Quantity"])
            price = int(row["Price"])

            revenue = quantity * price

            cleaned_row = {
                "date": row["Date"],
                "product": row["Product"],
                "category": row["Category"],
                "quantity": quantity,
                "price": price,
                "city": row["City"],
                "salesperson": row["Salesperson"],
                "revenue": revenue
            }

            sales.append(cleaned_row)

    return sales


def product_revenue_summary(sales):
    product_revenue = {}

    for sale in sales:
        product = sale["product"]
        revenue = sale["revenue"]

        if product not in product_revenue:
            product_revenue[product] = 0

        product_revenue[product] += revenue

    return product_revenue


def sales_summary(sales):
    total_revenue = 0
    total_quantity = 0

    for sale in sales:
        total_revenue += sale["revenue"]
        total_quantity += sale["quantity"]

    total_orders = len(sales)

    average_order_value = total_revenue / total_orders

    highest_sale = max(
        sales,
        key=lambda sale: sale["revenue"]
    )

    product_summary = product_revenue_summary(sales)

    top_product = max(
        product_summary,
        key=product_summary.get
    )

    return {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "total_orders": total_orders,
        "average_order_value": average_order_value,
        "highest_sale": highest_sale,
        "top_product": top_product
    }


def category_revenue_summary(sales):
    category_revenue = {}

    for sale in sales:
        category = sale["category"]
        revenue = sale["revenue"]

        if category not in category_revenue:
            category_revenue[category] = 0

        category_revenue[category] += revenue

    return category_revenue


def city_revenue_summary(sales):
    city_revenue = {}

    for sale in sales:
        city = sale["city"]
        revenue = sale["revenue"]

        if city not in city_revenue:
            city_revenue[city] = 0

        city_revenue[city] += revenue

    return city_revenue


def salesperson_revenue_summary(sales):
    salesperson_revenue = {}

    for sale in sales:
        salesperson = sale["salesperson"]
        revenue = sale["revenue"]

        if salesperson not in salesperson_revenue:
            salesperson_revenue[salesperson] = 0

        salesperson_revenue[salesperson] += revenue

    return salesperson_revenue


def electronics_revenue_percentage(sales):
    total_revenue = 0
    electronics_revenue = 0

    for sale in sales:
        revenue = sale["revenue"]

        total_revenue += revenue

        if sale["category"] == "Electronics":
            electronics_revenue += revenue

    percentage = (electronics_revenue / total_revenue) * 100

    return percentage


def top_3_products(sales):
    product_revenue = product_revenue_summary(sales)

    sorted_products = sorted(
        product_revenue.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_products[:3]


def business_analysis(sales):
    category_revenue = category_revenue_summary(sales)
    city_revenue = city_revenue_summary(sales)
    salesperson_revenue = salesperson_revenue_summary(sales)
    electronics_percentage = electronics_revenue_percentage(sales)
    top_products = top_3_products(sales)

    return {
        "category_revenue": category_revenue,
        "city_revenue": city_revenue,
        "salesperson_revenue": salesperson_revenue,
        "electronics_percentage": electronics_percentage,
        "top_3_products": top_products
    }


sales = load_sales("sales_project.csv")

summary = sales_summary(sales)

print("Sales Summary:")
print(summary)

analysis = business_analysis(sales)

print("\nCategory Revenue:")
print(analysis["category_revenue"])

print(
    "Highest Revenue Category:",
    max(
        analysis["category_revenue"],
        key=analysis["category_revenue"].get
    )
)

print("\nCity Revenue:")
print(analysis["city_revenue"])

print(
    "Highest Revenue City:",
    max(
        analysis["city_revenue"],
        key=analysis["city_revenue"].get
    )
)

print("\nSalesperson Revenue:")
print(analysis["salesperson_revenue"])

print(
    "Highest Revenue Salesperson:",
    max(
        analysis["salesperson_revenue"],
        key=analysis["salesperson_revenue"].get
    )
)

print("\nElectronics Revenue Percentage:")
print(
    round(
        analysis["electronics_percentage"],
        2
    ),
    "%"
)

print("\nTop 3 Products by Revenue:")

for product, revenue in analysis["top_3_products"]:
    print(product, "→", revenue)
