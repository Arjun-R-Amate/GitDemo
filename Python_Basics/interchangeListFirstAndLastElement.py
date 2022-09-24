#: Q Write a program to interchange first element with last element and last element with first element ?
# input = [12, 45, 65, 87, 98] output = [98, 87, 65, 45, 12]

#: Using pop method to store removed elememt into an variable and use
def swap(list1):
    first = list1.pop(0)
    last = list1.pop(-1)
    list1.insert(0, last)
    list1.append(first)

    return list1

mylistr = [10, 45, 36, 45, "welcome"]
var = swap(mylistr)
print(var)

import sys
sys.exit(0)

#: Ans = > store first and last element of the list into an one variable and swap those
def swap(list1):
    get = list1[0],list1[-1]
    list1[-1], list1[0] = get
    return list1

mylist = [12, 36, 45, 69, 78]
vart = swap(mylist)
print(vart)



import sys
sys.exit(0)

def swaplist(newlist):
    size = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size-1] = temp
    return newlist
myList = [12, 45, 65, 87, 98]
obj = swaplist(myList)
print(obj)


import sys
sys.exit(0)

def swap(my_list):
    my_list[-1], my_list[0] = my_list[0], my_list[-1]
    return my_list

my_list = [12, 45, 65, 87, 98]
call = swap(my_list)
print(call)