# Ex 01
product = ("Laptop","Mouse","Keyboard","Monitor")
print(product)

# Ex 02
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[2])
print(numbers[-1])

# Ex 03
cities = ("Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta")
print(len(cities))

# Ex 04
cities = ("Lahore", "Karachi", "Islamabad", "Peshawar")
print("Lahore" in cities)
print("Multan" in cities)

# Ex 05
numbers = (10, 20, 10, 30, 40, 10, 50)
print(numbers.count(10))

# Ex 06
employee = ("Ali", 25, "Lahore", 75000)
name = employee[0]
age = employee[1]
city = employee[2]
salary = employee[3]
print(name,age,city,salary)

# Ex 07
def get_product():
    return "Laptop",100000,"Electronics"

product,price,category = get_product()
print(product,price,category)

# Ex 08
employee = {
    "name": "Ali",
    "department": "IT",
    "salary": 75000
}
for key,value in employee.items():
    print(f"{key} = {value}")

# Ex 09
employees = (
    ("Ali", 75000),
    ("Ahmed", 55000),
    ("Sara", 80000),
    ("Hamza", 60000)
)
for employee in employees:
    if employee[1] > 60000:
        print(employee[0])


# Ex 10
sales = (
    ("Laptop", "Electronics", 100000),
    ("Mouse", "Electronics", 2000),
    ("Chair", "Furniture", 15000),
    ("Desk", "Furniture", 30000)
)
total = 0
high = 0
for sale in sales:
    print(sale)
    total += sale[2]
    if sale[2] >= high:
        high = sale[2]
        high_product = sale[0]

print("Total =",total)
print("Most expensive =",high_product)

# Bonus Challenge
def analyze_product(product):
    name, category, price = product
    return name, category, price


product = ("Laptop", "Electronics", 100000)
product, category, price = analyze_product(product)

print(product)
print(category)
print(price)
