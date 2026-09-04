# Ex 01
try:
    number = int("hello")
    print(number)
except ValueError:
    print("Invalid number")

# Ex 02
try:
    number = int("100")
    print("Number:",number)
except:
    print("Invalid Number")

# Ex 03
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Ex 04
try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

# Ex 05
try:
    age = int(input("Enter your age: "))
    print("Age:",age)
except ValueError:
    print("Please enter a valid number")

# Ex 06
with open("sales_day6.txt") as f:
    for line in f:
        try:
            sale = int(line.strip())
            print(sale)
        except ValueError:
            print("Invalid sales value: ",line.strip())

# Ex 07
total = 0
with open("sales_day6.txt") as f:
    for line in f:
        try:
            sale = int(line.strip())
            total += sale
        except ValueError:
            print("Invalid sales value: ",line.strip())

print(total)

# Ex 08
total = 0
count = 0
with open("sales_day6.txt") as f:
    for line in f:
        try:
            sale = int(line.strip())
            total += sale
        except ValueError:
            count += 1
            print("Invalid sales value: ",line.strip())

print("Total:",total)
print("Invalid records:",count)

# Ex 09
def analyze_sales(filename):
    total = 0
    count = 0
    with open(filename) as f:
        for line in f:
            try:
                sale = int(line.strip())
                total += sale
            except ValueError:
                count += 1
                print("Invalid sales value: ",line.strip())

    return total, count

total, invalid_count = analyze_sales("sales_day6.txt")

print("Total:", total)
print("Invalid records:", invalid_count)

# Ex 10
def analyze_ages(filename):
    total_age = 0
    valid_age = 0
    invalid_age = 0
    with open(filename) as f:
        for line in f:
            try:
                age = int(line.strip())
                total_age += age
                valid_age += 1
            except ValueError:
                invalid_age += 1
                print("Invalid age value: ",line.strip())

    return total_age, valid_age, invalid_age

total_age, valid_age, invalid_age = analyze_ages("customer_ages.txt")

print("Total age:", total_age)
print("Valid age:", valid_age)
print("Invalid age:", invalid_age)