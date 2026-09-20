# Ex 01
def show_numbers(*numbers):
    for number in numbers:
        print(number)


show_numbers(10, 20, 30, 40, 50)

# Ex 02
def calculate_total(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total

result = calculate_total(10, 20, 30, 40)
print(result)

# Ex 03
def find_max(*numbers):
    high = numbers[0]
    for number in numbers:
        if number >= high:
            high = number

    return high

result = find_max(10, 50, 20, 80, 30)
print(result)

# Ex 04
def count_items(*items):
    return len(items)

result = count_items("Laptop", "Mouse", "Keyboard", "Monitor")
print(result)

# Ex 05
def show_skills(name, *skills):
    print("Employee:", name)

    for skill in skills:
        print(skill)


show_skills(
    "Ali",
    "Python",
    "SQL",
    "Excel",
    "Power BI"
)

# Ex 06
def show_details(**details):
    for key, value in details.items():
        print(f"{key} = {value}")


show_details(
    name="Ali",
    age=25,
    city="Lahore"
)

# Ex 07
def employee_info(**details):
    for key, value in details.items():
        print(f"{key} = {value}")


employee_info(
    name="Ali",
    department="IT",
    salary=75000,
    experience=2
)

# Ex 08
def get_salary(**employee):
    return employee["salary"]


salary = get_salary(
    name="Ali",
    department="IT",
    salary=75000
)

print(salary)

# Ex 09
def sales_total(*sales):
    total = 0

    for sale in sales:
        total += sale

    return total


result = sales_total(10000, 20000, 15000, 5000)
print(result)

# Ex 10
def analyze_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return total, average, maximum


result = analyze_numbers(10, 20, 30, 40, 50)
print(result)

total, average, maximum = analyze_numbers(10, 20, 30, 40, 50)

print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)

# Bounus Challenge
def analyze_employee(name, *skills, **details):
    print("Name:", name)

    print("\nSkills:")
    for skill in skills:
        print(skill)

    print("\nDetails:")
    for key, value in details.items():
        print(f"{key} = {value}")


analyze_employee(
    "Ali",
    "Python",
    "SQL",
    "Excel",
    department="Data",
    salary=75000,
    city="Lahore"
)
