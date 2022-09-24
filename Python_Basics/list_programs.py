# Q 7 Reversing an list in python by using inbuilt reverse function?
list1 = [12, 45, 665, 78, 32]
list1.reverse()
print(list1)

# reverse an list by using an reversed function ?
# While using an reversesd function we need to type casting an given list
list2 = [12, 36, 45, 74, 85, 96]
list(reversed(list2))
print(list2)


# Reversing an technique by using list slicing method
list3 = [12, 32, 45, 65, 78]
print(list3[::-1])


# Reversing an list using list comprhension?
new_list = [12,36, 45, 74, 85, 14]
list5 = [new_list[len(new_list)- i] for i in range(1, len(new_list)+1)]
print(list5)



import sys
sys.exit(0)

#: Q. 6 Write a program in different way to clear an list in python ?
list1 = [12, 36, 45, 78, 41]
a = list1.clear()
print(a)

# using multiplication with 0

list2 = [14, 45, 65]
list2 = list2*0
print(list2)

# using del can be used to clear the list elements in a range.If we dont give an range all the elemnts are deleted?
list3 = [12, 45, 78, 65, 35]
del list3[:]
print(list3)


import sys
sys.exit(0)

# Q 5 = Find out the element exist in a list or not by using if else statement?
list1 = [12, 45, 78, 65, 35]
num = int(input("Enter the number you want to search: "))
if num in list1:
    print(num, "is exist in list")
else:
    print(num, " is not exist in list")

# Check element exist or not by using for loop?
list1 = [12, 45, 65, 78, 96]
a = int(input("Enter number: "))
for item in list1:
    if (item == a):
        print("number is exist")
        break
else:
    print("number is not exist")


# CHeck element exist or not in list by using count method ?
list1 = [12, 36, 45, 78, 95]
exist_count = list1.count(36)
if exist_count > 0:
    print("exist_count is exist")
else:
    print("exist_count does not exist")


import sys
sys.exit(0)

#: Q 4 Find out minimum number using if else?
a = 45
b = 51
if a <= b:
    print(a)
else:
    print(b)


# Using min function?
a = 6 ; b =48
val = min(a, b)
print(val)

import sys
sys.exit(0)

# Q.3 Find out maximum number of two numbers ?
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def maximum():
    if a >= b:
        print(a)
    else:
        print(b)
maximum()

a = max(45, 52)
print(a)


# find maximum value by using ternary operator

x = 4
y = 5
print(x if x >=y else y)


# Using lambda function ton find maximum value

a = 65
b = 45
val = lambda a, b: a if a >= b else b
print(val(a, b))

# Using list comprhension ?
# List comprhension returns an new entire list
a = 54; b = 58
list1 = [a if a > b else b]
print(list1)

import sys
sys.exit(0)
# Q 2 find out length of list by using append and len function ?
empty_list = []
empty_list.append("welcome")
empty_list.append("to")
empty_list.append("world")
empty_list.append("of")
empty_list.append("python")
print(empty_list)
print(id(empty_list), type(empty_list), len(empty_list))


# Q 1 Find out the lenth of the list ?
list1 = [12, 23, 45, 78, 46, 69]
print(len(list1))
counter = 0
for item in list1:
    counter +=1
print(counter)