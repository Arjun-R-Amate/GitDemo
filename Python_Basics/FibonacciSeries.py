
#: Q Write a fibonacci series using while loop ?
n = int(input("Enter number you want to fibonacci: "))
counter = 0
first = 0
second = 1
while counter < n:
    print(first, end=" ")
    temp = first
    first = second
    second = temp + first
    counter +=1


#: Q Write a program for fibonacci series using for loop?
n = int(input("Enter number you want to fibonacci: "))
first = 0
second = 1
for item in range(n):
    print(first, end=" ")
    temp = first
    first = second
    second = temp + first
