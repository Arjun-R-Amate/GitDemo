# write a python program to swap two elements in a list ?
# input = [12, 36, 45, 78]  and output = [45, 36, 23, 90]

# Swap eleemnt in string list ==> Using string join() , replace() and split() method
test_list = ["welcome", "to", "learn", "python", "course"]
print("The original list is: "+ str(test_list), type(test_list))
res = ",".join(test_list)
print(res, type(res))
print(id(res))
main = res.replace("w", "W").replace("e", "E").replace("p", "P").split(",")
print(main, type(main))
print(id(main))


import sys
sys.exit(0)

# Pythion  swap elements in string list
#method1 : using replace() + list comprhension


test_list = ["welcome", "to", "learn", "python", "course"]
print(str(test_list))
# swap elements in string list using replace method and list comprhension
res = [item.replace("w", "W").replace("l", "L").replace("p","J")for item in test_list]
print(str(res))


import sys
sys.exit(0)

# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    # 19, 65
    return list


# Driver function
List = [23, 65, 19, 90]
pos1 = 2
pos2 = 1

call = swapPositions(List, pos1-1, pos2-1)
print(call)