# Ex 01
num = [10,25,30,15,40]

print(num)
print(num[0])
print(num[4])
print(len(num))

# Ex 02
sales = [1200, 2500, 1800, 3200, 2100]

print(sum(sales))
print(max(sales))
print(min(sales))
print(len(sales))

# Ex 03
sales = [1200, 2500, 1800, 3200, 2100]

for sale in sales:
    print("Sale:",sale)

# Ex 04
sales = [1200, 2500, 1800, 3200, 2100]

for sale in sales:
    if sale > 2000:
        print(sale)


# Challenge 01
sales = [1200, 2500, 1800, 3200, 2100]

for sale in sales:
    if sale < 2000:
        print(sale)

# Challenge 02
for sale in sales:
    if sale > 2000:
        print(sale,"→ High")
    else:
        print(sale,"→ Low")

# Challenge 03
total = 0
for sale in sales:
    total += sale

print(total)

# Challenge 04
count = 0
for sale in sales:
    if sale > 2000:
        count +=1

print("count = ",count)

# Challenge 05
products = ["Laptop", "Mouse", "Keyboard"]

print(products[0])
print(products[-1])
products[1] = "Wireless Mouse"
products.append("Monitor")
products.remove("Keyboard")
print(products)

# Bonus Challenge
sales = [1200, 2500, 1800, 3200, 2100, 4500, 900]

large_count = 0
less_count = 0
total = 0

for sale in sales:
    if sale > 2000:
        large_count +=1
        total += sale
    else:
        less_count += 1

print("Sales above 2000:",large_count)
print("Sales 2000 or below:",less_count)
print("Total Sales above 2000:",total)