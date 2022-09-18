#Write a program to add natural numbers using while loop and function?
def add_num(num):
    add = 0
    counter = 0
    while counter <= num:
        add = add + counter
        counter +=1
    return add
input_num = int(input("Enter the number: "))
result = add_num(input_num)
print(result)


import sys
sys.exit(0)

#: Write a program to add natural numbers by using while loop?
#: Always keep in mind while loop to (initialize counter , condition, increament or decreament counter)
num = int(input("Enter number you want to add: "))
add = 0
counter = 0
while counter <= num:
    add = add + counter
    counter = counter+1
print("Total addition upto", add)



#: Write a program to add a odd numbers from 1 to 50 ?
empty_list = []
for item in range(1, 51):
    if item %  2 == 1:
        empty_list.append(item)
print(empty_list)
print(sum(empty_list))




#: Q Write a program to add numbers from 1 to 50 and that only add even numbers.
empty_list = []
for item in range(1, 51):
    if item % 2 ==  0:
        empty_list.append(item)
print(empty_list)
print(sum(empty_list))



#: Q Write a program to add an numbers from 1 to 10
add = 0
for item in range(1, 11):
    add = add + item
print(add)



#: Q Write a program to add an numbers?
list1 = [12, 45, 68, 78, 45, 12]
add = 0
for item in list1:
    add = add + item
print(add)