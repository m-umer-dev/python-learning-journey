def load_sales(filename):
    with open(filename) as file:

        sales = []
        total = 0
        grand_total = 0
        electronic_sale = 0
        highest = 0
        total_quan = 0

        file.readline()
        for line in file:
            data = line.strip().split(',')
            sale = {
                "product" : data[0],
                "category" : data[1],
                "quantity" : int(data[2]),
                "price": int(data[3])
            }
            sales.append(sale)

        for sale in sales:

            total = sale["quantity"] * sale["price"]
            print(f"{sale['product']} → {total}")
            grand_total += total
            if total > highest:
                highest = total
                product_name = sale["product"]

        print(f"Most expensive sale: {product_name}")
        print(f"Total: {highest}")

        print(f"Grand Total: {grand_total}")

        for sale in sales:
            total_quan += sale["quantity"] 
            if sale["category"] == "Electronics":
                print(sale["product"])
                electronic_sale += sale["quantity"] * sale["price"]

        print(f"Electronics total: {electronic_sale}")
        print(f"Total quantity: {total_quan}")
        print(f"Total Sale: {len(sales)}")


load_sales("sales.csv")
