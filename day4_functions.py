# Ex 01
def greet():
    print("Hello, Umer!")

greet()

# Ex 02
def greet(name):
    print(f"Hello, {name}!")

greet("Umer")
greet("Ali")
greet("Sara")

# Ex 03
def introduce(name, city):
    print(f"My name is {name}")
    print(f"I live in {city}")

introduce("Umer", "Lahore")

# Ex 04
def add(a, b):
    return a+b

result = add(10, 20)
print(result)

# Ex 05
def calculate_total(sales):
    total = 0
    for sale in sales:
        total += sale

    return total

sales = [1200, 2500, 1800, 3200, 2100]
print(calculate_total(sales))

# Ex 06
def count_high_sales(sales):
    count = 0
    for sale in sales:
        if sale > 2000:
            count += 1

    return count

sales = [1200, 2500, 1800, 3200, 2100]
print(count_high_sales(sales))

# Ex 07
def show_student(student):
    print(f"Name: {student['name']}")
    print(f"Degree: {student['degree']}")
    print(f"CGPA: {student['cgpa']}")

student = {
    "name": "Umer",
    "age": 23,
    "degree": "BSCS",
    "cgpa": 3.5
}
show_student(student)

# Ex 08
def find_high_cgpa(students):
    for student in students:
        if student["cgpa"] > 3.5:
            print(student["name"],"-",student["cgpa"])

students = [
    {"name": "Umer", "cgpa": 3.5},
    {"name": "Ali", "cgpa": 3.2},
    {"name": "Sara", "cgpa": 3.8},
    {"name": "Ahmed", "cgpa": 2.9},
    {"name": "Ayesha", "cgpa": 3.7}
]

find_high_cgpa(students)

# Ex 09
def get_high_sales(sales):
    new_list = []
    for sale in sales:
        if sale > 2000:
            new_list.append(sale)

    return new_list

sales = [1200, 2500, 1800, 3200, 2100]
result = get_high_sales(sales)
print(result)