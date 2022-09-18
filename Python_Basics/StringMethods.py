#: Q Write a program wheather to check string is palindrome or not?
string3 = input("Enter a string you want to check: ")
res =string3[::-1]
if string3 == res:
    print(string3, "is an palindrome.")
else:
    print(string3, "is not an palindrome.")



import sys
sys.exit(0)

#: Q. List elements divide by 3 ?
list1 = [12, 45, 78, 69, 36, 46, 78]
empty_list = []
for item in list1:
    result = item/3
    empty_list.append(result)
print(empty_list)



#: Q How to remove white spaces from string?
#: Ans = By using strip method we can remove the white spaces of both side from string.
string2 = "    welcome to world of python     "
result = string2.strip()
print(result)


#: Q. String split method ?
#: Ans = String split method is used to split the string with given seperator and it returns an new list.
string1 = "welcome to, world, of python"
result = string1.split(",")
print(result, type(result))
print(id(string1))
print(id(result))

