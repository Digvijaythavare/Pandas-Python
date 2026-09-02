import csv

data = [
    ["Name", "Age", "City", "Marks"],
    ["Rahul", 21, "Pune", 85],
    ["Amit", 22, "Mumbai", 90],
    ["Priya", 20, "Nashik", 88]
]

with open("students.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully!")