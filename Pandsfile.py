print("====== Pandas Tutorial ======")

filename = "Rawdata.txt"
number = str(input("Enter Mobile Number: "))
Name = str(input("Enter YOur Name: "))

with open(filename, "r") as file:
    data = file.read()

if number and Name in data:
    print("Member is found in file")
else:
    print("Number is not found in file")