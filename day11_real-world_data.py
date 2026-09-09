# Ex 01
names = [" Umer ", " ali", "AHMED ", " hamza "]
clean_name = [name.strip().title() for name in names]
print(clean_name)

# Ex 02
ages = ["23", "25", "19", "31"]
convert_ages = [int(age.strip()) for age in ages]
print(convert_ages)

# Ex 03
customers = [
    {"name": " Umer ", "age": "23", "city": "lahore"},
    {"name": "Ali", "age": "25", "city": "LAHORE"},
    {"name": " Ahmed ", "age": "19", "city": "Islamabad"},
    {"name": "Hamza", "age": "31", "city": "lahore"}
]
for customer in customers:
    customer["name"] = customer["name"].strip().title()
    customer["age"] = int(customer["age"].strip())
    customer["city"] = customer["city"].strip().title()

print(customers)

# Ex 04
filter_customers = [customer["name"] for customer in customers if customer["age"] >= 25]
print(filter_customers)

# Ex 05
filter_city = [customer["name"] for customer in customers if customer["city"] == "Lahore"]
print(filter_city)

# Ex 06
products = [
    {"product": "Laptop", "quantity": 2, "price": 100000},
    {"product": "Mouse", "quantity": 5, "price": 2000},
    {"product": "Keyboard", "quantity": 3, "price": 5000},
    {"product": "Chair", "quantity": 4, "price": 15000}
]

for product in products:
    product["total"] = product["quantity"] * product["price"]

print(products)

# Ex 07
high_sale = [product["product"] for product in products if product["total"] > 50000]
print(high_sale)

# Ex 08
def clean_customer(customer):
    customer["name"] = customer["name"].strip().title()
    customer["age"] = int(customer["age"].strip())
    customer["city"] = customer["city"].strip().title()

    return customer

customers = [
    {"name": " Umer ", "age": "23", "city": "lahore"},
    {"name": "Ali", "age": "25", "city": "LAHORE"},
    {"name": " Ahmed ", "age": "19", "city": "Islamabad"},
    {"name": "Hamza", "age": "31", "city": "lahore"}
]
for customer in customers:
    clean_customer(customer)

print(customers)

# Ex 09
customer = {
    "name": "Ali",
    "age": "unknown",
    "city": "Lahore"
}
try:
    customer["age"] = int(customer["age"])
except ValueError:
    customer["age"] = 0

print(customer)

# Ex 10
def process_customers(customers):
    for customer in customers:
        try:
            customer["name"] = customer["name"].strip().title()
            customer["age"] = int(customer["age"].strip())
            customer["city"] = customer["city"].strip().title()
        except ValueError:
            customer["age"] = 0

    filter_customer = [customer["name"] for customer in customers if customer["age"] >= 20 and customer["city"] == "Lahore"]

    return customers, filter_customer


customers = [
    {"name": " Umer ", "age": "23", "city": "lahore"},
    {"name": "Ali", "age": "25", "city": "LAHORE"},
    {"name": " Ahmed ", "age": "19", "city": "Islamabad"},
    {"name": "Hamza", "age": "31", "city": "lahore"},
    {"name": "Sara", "age": "unknown", "city": "Lahore"}
]

customer,filter_customer = process_customers(customers)
print(customer)
print(filter_customer)