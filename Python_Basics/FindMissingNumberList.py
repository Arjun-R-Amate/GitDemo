#: Write a program to display student marks using function?
def student_marks(marks):
    stud_name = input("Enter the student name: ")
    for student in marks:
        if student == stud_name:
            return marks[student]
    else:
        return "No record found"

dictionary = {"ram": 68, "raj": 78, "krishna": 98, "dada": 90}
result = student_marks(dictionary)
print(result)

import sys
sys.exit(0)

#: Q Write a program to display an marks of student?
student_name = input("Enter the student name: ")
marks = {"ram": 68, "raj": 78, "krishna": 98, "dada": 90}
for student in marks:
    if student_name == student:
        print(marks[student])
        break
else:
    print("No entry with that name found.")




#: Q Find the missing number from list?
list1 = [1, 2, 4, 6, 9]
empty_list =[]
for item in range(1, max(list1)+1):
    if item not in empty_list:
        empty_list.append(item)
print(empty_list)