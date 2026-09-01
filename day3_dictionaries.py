# Ex 01
person = {
    "name": "Umer",
    "age": 23,
    "city": "Lahore",
    "job": "Web Developer"
}

print(person)
print(person["name"])
print(person["age"])
print(person["city"])
print(person["job"])

# Ex 02
person["city"] = "Karachi"
person["job"] = "Data Analyst"

# Ex 03
person["country"] = "Pakistan"
del person ["age"]

# Ex 04
print("name" in person)
print("salary" in person)
print("country" in person)

# Ex 05
student = {
    "name": "Umer",
    "age": 23,
    "degree": "BSCS",
    "cgpa": 3.5
}

for key,value in student.items():
    print(key , ":" , value)

# Ex 06
students = [
    {"name": "Umer", "cgpa": 3.5},
    {"name": "Ali", "cgpa": 3.2},
    {"name": "Sara", "cgpa": 3.8}
]

for student in students:
    print(student["name"],"-",student["cgpa"])

# Ex 07
students = [
    {"name": "Umer", "cgpa": 3.5},
    {"name": "Ali", "cgpa": 3.2},
    {"name": "Sara", "cgpa": 3.8},
    {"name": "Ahmed", "cgpa": 2.9},
    {"name": "Ayesha", "cgpa": 3.7}
]

for student in students:
    if student["cgpa"] > 3.5:
        print(student)

# Ex 08
sales = [
    {"product": "Laptop", "sales": 120000},
    {"product": "Mouse", "sales": 5000},
    {"product": "Keyboard", "sales": 8000},
    {"product": "Monitor", "sales": 45000}
]

count = 0
for sale in sales:
    print(sale["product"],"-",sale["sales"])

for sale in sales:
    if sale["sales"] > 10000:
        count += 1
        print(sale["product"],"-",sale["sales"])

print("Products have sales greater than 10000 :",count)

# Challenege 01
student = {
    "name": "Umer",
    "age": 23,
    "degree": "BSCS",
    "cgpa": 3.5
}

for key,value in student.items():
    print(key,":",value)

# Challenege 02
students = [
    {"name": "Umer", "cgpa": 3.5},
    {"name": "Ali", "cgpa": 3.2},
    {"name": "Sara", "cgpa": 3.8}
]

for student in students:
    print(student["name"],"-",student["cgpa"])

# Challenege 03
sales = [
    {"product": "Laptop", "sales": 120000},
    {"product": "Mouse", "sales": 5000},
    {"product": "Keyboard", "sales": 8000},
    {"product": "Monitor", "sales": 45000}
]

for sale in sales:
    print(sale["product"],"-",sale["sales"])