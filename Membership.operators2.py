#Membership operators = used to sets weather a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

students = {"Nitya", "Kavya", "Shidhant"}

student = input("Enter the name of the student: ")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")