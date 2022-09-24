#Q.1 Write a program to find out factorial number using given number ?
# 5 * 4 * 3 * 2 * 1
# Q find the number of trailing zeros in that tutorial ?

total = 1
number = int(input("Enter number you want to factorial: "))
for item in range(number,0,-1):
    total *=item
print(total)