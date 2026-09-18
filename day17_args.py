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
    high = 0
    for number in numbers:
        if number >= high:
            high = number

    return high

result = find_max(10, 50, 20, 80, 30)
print(result)

# Ex 04
def count_items(*items):
    count = 0
    for item in items:
        count += 1

    return count


result = count_items("Laptop", "Mouse", "Keyboard", "Monitor")
print(result)