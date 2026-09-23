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


sales = load_sales("sales_project.csv")

total_revenue = 0

for sale in sales:
    total_revenue += sale["revenue"]

print("Total Revenue:", total_revenue)


total_quantity = 0

for sale in sales:
    total_quantity += sale["quantity"]

print("Total Quantity:", total_quantity)


total_orders = len(sales)

print("Total Orders:", total_orders)


average_order_value = total_revenue / total_orders

print("Average Order Value:", average_order_value)


highest_sale = max(
    sales,
    key=lambda sale: sale["revenue"]
)

print("Highest-Value Sale:")
print("Product:", highest_sale["product"])
print("Revenue:", highest_sale["revenue"])

product_summary = product_revenue_summary(sales)

print("Product Revenue Summary:")
print(product_summary)

top_product = max(
    product_summary,
    key=product_summary.get
)

print("Top Product:", top_product)
print("Revenue:", product_summary[top_product])

summary = sales_summary(sales)

print("Sales Summary:")
print(summary)