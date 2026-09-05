# Ex 01 & 02 & 03
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

student_1 = student("Ali",23)
student_2 = student("Ahmed",25)

print("Name:",student_1.name)
print("Age:",student_1.age)
print(student_1.introduce())
print("Name:",student_2.name)
print("Age:",student_2.age)
print(student_2.introduce())

# Ex 04
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return f"{self.name} → {self.salary}"

employee_1 = Employee("Ali",50000)
employee_2 = Employee("Ahmed",70000)
employee_3 = Employee("Sara",60000)

print(employee_1.get_salary())
print(employee_2.get_salary())
print(employee_3.get_salary())

# Ex 05
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return f"Total: {self.price * self.quantity}"


producy_1 = Product("Laptop",100000,2)
print(producy_1.name)
print(f"Price = {producy_1.price}")
print(f"Quantity = {producy_1.quantity}")
print(producy_1.total_price())

# Ex 06
class Sale:
    def __init__(self,product,price,quantity):
        self.product = product
        self.price = price
        self.quanity = quantity

    def total(self):
        return self.price * self.quanity

sale_1 = Sale("laptop",100000,2)
sale_2 = Sale("Mouse",2000,5)
sale_3 = Sale("Keyboard",5000,3)

print(f"{sale_1.product} → {sale_1.price} × {sale_1.quanity}")
print(f"{sale_2.product} → {sale_2.price} × {sale_2.quanity}")
print(f"{sale_3.product} → {sale_3.price} × {sale_3.quanity}")
print(sale_1.total() + sale_2.total() + sale_3.total())

# Ex 07
class Employee:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        return self.name

class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size


manager_01 = Manager("Ali",5)
print(f"My name is {manager_01.name}")
print(f"Team size: {manager_01.team_size}")