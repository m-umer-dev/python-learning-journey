# Ex 01
with open("customers.txt","r") as f:
    print(f.read())

# Ex 02
with open("customers.txt") as customer:
    for customer in customer:
        print(customer.strip())

# Ex 03
with open("customers.txt") as customers:
    customer = customers.readlines()
    print(customer)

# Ex 04
with open("products.txt","w") as f:
    f.write("Laptop\n Mouse\n Keyboard\n Monitor\n")

# Ex 05
with open("products.txt", "a") as f:
    f.write("Webcam\n Headphones\n")

# Ex 06
with open("sales.txt", "r") as f:
    for line in f:
        sales = int(line.strip())
        print(sales)

# Ex 07
total = 0
with open("sales.txt") as file:
    for line in file:
        sale = int(line.strip())
        total += sale

print(total)

# Ex 08
with open("sales.txt","r") as file:
    for line in file:
        sale = int(line.strip())
        if sale > 2000:
            print(sale)


# Ex 09
def load_sales(filename):
    sales = []
    with open(filename, "r") as file:
        for line in file:
            sale = int(line.strip())
            sales.append(sale)

    return sales

sales = load_sales("sales.txt")
print(sales)

# Ex 10
def analyze_sales(filename):
    total = 0
    count = 0
    with open(filename, "r") as file:
        for line in file:
            sale = int(line.strip())
            total += sale
            if sale > 2000:
                count += 1

    return total, count

total, high_count = analyze_sales("sales.txt")

print("Total:", total)
print("High sales:", high_count)