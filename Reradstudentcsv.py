import pandas as pd

studentdata =  [
    ["Name", "Age", "City", "Marks"],
    ["Rahul", 21, "Pune", 85],
    ["Amit", 22, "Mumbai", 90],
    ["Priya", 20, "Nashik", 88]
]

data = pd.read_csv(studentdata)

print(data)