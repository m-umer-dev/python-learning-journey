import csv

with open("sales_project.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        print("Product:", row["Product"])
        print("Quantity:", row["Quantity"])
        print("Price:", row["Price"])

        row["Quantity"] = int(row["Quantity"])
        row["Price"] = int(row["Price"])

        print("Quantity type:", type(row["Quantity"]))
        print("Price type:", type(row["Price"]))

        quantity = int(row["Quantity"])
        price = int(row["Price"])

        revenue = quantity * price

        print(f'{row["Product"]} → {revenue}')


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



sales = load_sales("sales_project.csv")

print(sales)
print(len(sales))
