# Ex 01
with open("data.csv") as file:
    for line in file:
        print(line.strip())

# Ex 02
with open("data.csv") as file:
    for line in file:
        record = line.split(",")
        print(f"{record[0]} → {record[2]}")

# Ex 03
with open("data.csv") as file:
    for line in file:
        record = line.split(",")
        record[1] = int(record[1])
        record[3] = int(record[3])
        print(f"{record[0]} {record[1]} {record[3]}")

# Ex 04
Employees = []
with open("data.csv") as file:
    for line in file:
        record = line.split(",")
        employee = {
            "name" : record[0],
            "age" : record[1],
            "department" : record [2],
            "salary" : record[3]
        }

        Employees.append(employee)

print(Employees)

# Ex 05
for employee in Employees:
    if employee["department"] == "IT":
        print(employee["name"])

# Ex 06
total = 0
for employee in Employees:
    salary = int(employee["salary"])
    total += salary

print(f"Total salary: {total}")

# Ex 07 & 08
total = 0
avg = 0
for employee in Employees:
    total += int(employee["salary"])
    avg = total/len(employee)
    if salary > 60000:
        print(employee["name"])

    
print(f"Average salary: {avg}")

# Ex 09
def load_employees(filename):
    Employees = []
    with open(filename) as file:
        for line in file:
            record = line.split(",")
            employee = {
                "name" : record[0],
                "age" : record[1],
                "department" : record [2],
                "salary" : record[3]
            }

            Employees.append(employee)

    return Employees

employees = load_employees("data.csv")
print(employees)

# Ex 10
def analyze_employees(filename):

    Employees = []
    total_employees = 0
    total_salary = 0
    average_salary = 0
    number_of_IT_employees = 0

    with open(filename) as file:
        for line in file:
            employee = line.split(",")
            employees = {
                "name" : employee[0],
                "age" : employee[1],
                "department" : employee[2],
                "salary" : employee[3]
            }

            Employees.append(employees)

        for employe in Employees:
            total_employees = len(employe)
            total_salary += int(employe["salary"])
            average_salary = total_salary / total_employees
            if employe["department"] == "IT":
                number_of_IT_employees += 1

    return total_employees, total_salary, average_salary, number_of_IT_employees

total_employees, total_salary, average_salary, it_employees = analyze_employees("data.csv")

print(total_employees, total_salary, average_salary, it_employees)
        