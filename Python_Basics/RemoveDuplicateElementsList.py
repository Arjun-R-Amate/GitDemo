#: Q How to remove duplicate elements from list ?
# Ans = By converting list into an set and set does not allowed duplicate elements and again set object convert back into list.
# Ans = By using dict.fromkeys method we can remove duplicate elements and again back convert into an list.

def remove_duplicate(list1):
    return list(dict.fromkeys(list1))
mylist = [1, 4, 5, 7, 6, 8, 1, 4, 2, 3, 7, 8, 9, 8, 1, 8,  5]
result = remove_duplicate(mylist)
print(result)



import sys
sys.exit(0)

list1 = [1, 4, 5, 7, 6, 8, 1, 4, 2, 3, 7, 8, 9, 8, 1, 8,  5]
result = list(set(list1))
print(result)
result1 = list(dict.fromkeys(list1))
print(result1)