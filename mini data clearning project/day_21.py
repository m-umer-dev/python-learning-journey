import csv
from datetime import datetime


def load_sales(filename):
    sales = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = datetime.strptime(
                row["Date"],
                "%Y-%m-%d"
            ).date()

            quantity = int(row["Quantity"])
            price = float(row["Price"])

            revenue = quantity * price

            sale = {
                "date": date,
                "product": row["Product"],
                "category": row["Category"],
                "quantity": quantity,
                "price": price,
                "city": row["City"],
                "salesperson": row["Salesperson"],
                "revenue": revenue
            }

            sales.append(sale)

    return sales


sales = load_sales("sales_project.csv")

print(sales[0]["date"])
print(type(sales[0]["date"]))


def show_date_parts(sales):
    for sale in sales:
        date = sale["date"]

        print(
            f"{sale['product']} → "
            f"Year: {date.year}, "
            f"Month: {date.month}, "
            f"Day: {date.day}"
        )


show_date_parts(sales)


def daily_revenue_summary(sales):
    daily_revenue = {}

    for sale in sales:
        date = sale["date"]
        revenue = sale["revenue"]

        if date not in daily_revenue:
            daily_revenue[date] = 0

        daily_revenue[date] += revenue

    return daily_revenue


daily_revenue = daily_revenue_summary(sales)

print("Daily Revenue:")
print(daily_revenue)


highest_revenue_date = max(
    daily_revenue,
    key=daily_revenue.get
)

print("Highest Revenue Date:")
print(highest_revenue_date)

print("Highest Revenue Amount:")
print(daily_revenue[highest_revenue_date])


def sort_sales_by_date(sales):
    return sorted(
        sales,
        key=lambda sale: sale["date"]
    )


sorted_sales = sort_sales_by_date(sales)

print("Sales Sorted By Date:")

for sale in sorted_sales:
    print(
        sale["date"],
        sale["product"],
        sale["revenue"]
    )


def monthly_revenue_summary(sales):
    monthly_revenue = {}

    for sale in sales:
        month = sale["date"].month
        revenue = sale["revenue"]

        if month not in monthly_revenue:
            monthly_revenue[month] = 0

        monthly_revenue[month] += revenue

    return monthly_revenue


monthly_revenue = monthly_revenue_summary(sales)

print("Monthly Revenue:")
print(monthly_revenue)


def date_analysis(sales):
    daily_revenue = daily_revenue_summary(sales)
    monthly_revenue = monthly_revenue_summary(sales)

    highest_revenue_date = max(
        daily_revenue,
        key=daily_revenue.get
    )

    highest_revenue_amount = daily_revenue[
        highest_revenue_date
    ]

    return {
        "daily_revenue": daily_revenue,
        "monthly_revenue": monthly_revenue,
        "highest_revenue_date": highest_revenue_date,
        "highest_revenue_amount": highest_revenue_amount
    }


analysis = date_analysis(sales)

print("Date Analysis:")
print(analysis)


def get_sales_for_month(sales, month):
    monthly_sales = []

    for sale in sales:
        if sale["date"].month == month:
            monthly_sales.append(sale)

    return monthly_sales


january_sales = get_sales_for_month(sales, 1)

print("January Sales:")

for sale in january_sales:
    print(
        sale["date"],
        sale["product"],
        sale["revenue"]
    )