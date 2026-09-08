# Ex 01
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number * number for number in numbers]
print(result)

# Ex 02
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number for number in numbers if number%2 == 0]
print(result)

# Ex 03
names = ["umer", "ali", "ahmed", "hamza"]
result = [name.upper() for name in names]
print(result)

# Ex 04
ages = [12, 18, 15, 21, 17, 30, 14]
result = [age for age in ages if age >= 18]
print(result)

# Ex 05
employees = [
    {"name": "Ali", "salary": 50000},
    {"name": "Ahmed", "salary": 70000},
    {"name": "Umer", "salary": 90000},
    {"name": "Hamza", "salary": 45000}
]
result = [employee for employee in employees if employee["salary"] > 60000 ]
print(result)

# Ex 06
result = [employee["name"] for employee in employees]
print(result)

# Ex 07
result = [employee["name"] for employee in employees if employee["salary"] > 60000 ]
print(result)

# Ex 08
with open("sales.csv") as file:
    file.readline()
    sales = []
    for line in file:
        data = line.strip().split(',')
        Employees = {
            "product" : data[0],
            "category" : data[1],
            "quantity" : int(data[2]),
            "price" : int(data[3])
        }
        sales.append(Employees)

    result = [sale["product"] for sale in sales]
    print(result)


# Ex 09
result = [sale["product"] for sale in sales if sale["category"] == "Electronics"]
print(result)

# Ex 10

result = [sale["product"] for sale in sales if sale["quantity"] * sale["price"] > 50000 ]
print(result)
