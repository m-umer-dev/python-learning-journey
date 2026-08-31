# Ex 01
name = "Muhammad Umer"
city = "Lahore"

print(name)
print(name[0])
print(name[-1])
print(len(name))
print(city.upper())
print(name.lower())

# Ex 02
name = "   Muhammad Umer   "
email = "   UMER@GMAIL.COM   "

print(name.strip())
email = email.strip()
email = email.lower()
print(email)

# Ex 03
text = "I am learning WordPress"

print(text.replace("WordPress","Python"))

# Ex 04
email = "umer@gmail.com"

print("@" in email)
print("gmail" in email)
print("yahoo" in email)

# Ex 05
full_name = "Muhammad Umer Amir"

full_name = full_name.split()
for name in full_name:
    print(name)

# Ex 06
cities = [" Lahore ", "LAHORE", "lahore", " Karachi ", "KARACHI"]

for city in cities:
    city = city.strip()
    city = city.lower()
    print(city)

# Ex 07
emails = [
    "umer@gmail.com",
    "ali@yahoo.com",
    "sara@gmail.com",
    "ahmed@outlook.com",
    "john@gmail.com"
]

for email in emails:
    if "gmail" in email:
        print(email)


# Challenge 01
customers = [
    "  Umer Amir  ",
    "ALI KHAN",
    "  sara ahmed",
    "JOHN DOE  ",
    "  ahmed ali "
]

for customer in customers:
    customer = customer.strip()
    customer = customer.lower()
    print(customer)


# Bonus
emails = [
    " Umer@Gmail.com ",
    "ali@Yahoo.com",
    " SARA@gmail.com ",
    "ahmed@Outlook.com",
    "john@GMAIL.com"
]

for email in emails:
    email = email.strip()
    email = email.lower()
    if "gmail" in email:
        print(email)