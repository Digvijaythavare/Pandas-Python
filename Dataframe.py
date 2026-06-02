
import pandas as pd

Student_name = ["John","Bob","Eve","Alice","Charlie"]
Student_age = [20,23,22,29,21]
Student_grade = [85,90,78,92,88]
Student_city = ["New York","Los Angeles", "Chicago","Houston","Phoenis"]

Student_info = pd.DataFrame({
    "Name" : Student_name,
    "Age" : Student_age,
    "Grade" : Student_grade,
    "City" : Student_city
})

print(Student_info,)