import csv

with open("sales_project.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row.items())