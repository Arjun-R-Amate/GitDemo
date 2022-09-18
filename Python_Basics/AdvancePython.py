# Lambda function : In python lambda is an anonymous function. Lambda function can use for shorter time of period
# Lambda function takes many arguments but it have only one expression

x = lambda a, b : a * b
print(x(5, 4))

#  decorators, generators, Iterators

# Decorators : In python decorator is a function that takes another function as an argument to change the behaviour of orignal function without modifying original function.



# def myfun(func):
#     def inner(a, b):
#         if a < b:
#             a,b = b,a
#             func(a,b)
#         elif b != 0:
#             func(a, b)
#         else:
#             print("Zero division error")
#     return inner
#
# @myfun
# def div(a, b):
#     print (a/b)
#
# res = div(5, 0)
#
#
# import sys
# sys.exit(0)
#
# def decorator(func):
#     def inner():
#         print("Before execution.")
#         func()
#         print("After execution.")
#     return inner
#
# def myfun():
#     print("This is our main function.")
#
#
# result = decorator(myfun)()



# generators: In python generators can be used to create an iterator from iterable objects. In generator yield is keyword is used.
# yield keyword pause the iterations and return the value

# Generator Expression : In python generator expression also an anonymous function like lambda function . the syntax of
# generator expression is similar of list comprhenssion only sqaure brackets replaced in round brackets.
# List comprhension returns an new list wheareas generator expression returns an element by element.# Generator Expression : In python generator expression also an anonymous function like lambda function . the syntax of
# # generator expression is similar of list comprhenssion only sqaure brackets replaced in round brackets.
# # List comprhension returns an new list wheareas generator expression returns an element by element.

# exp = (x*2 for x in range(10))
# for item in exp:
#     print(item, end=" ")

# List comprhesnion = When we require shorter syntax that time we use list comprhension it returns new list
new_list = [x*2 for x in range(1, 11)]
print(new_list)

# The difference between generator expression and list comprhension is generator expression returns an element by elemet
# wheareasd list comprhension return an new list


import sys
sys.exit(0)
n = int(input("Enter number: "))
def fibonacci():
    first= 0
    second = 1
    for item in range(n):
        temp = first
        first = second
        second = temp + first
        yield temp

val = fibonacci()
for item in val:
    print(item, end=" ")






def gen():
    n = 0
    print("First Output.")
    yield n

    n +=1
    print("Second Output.")
    yield n

    n = n +1
    print("Third Output")
    yield n

val = gen()
for item in val:
    print(item)




# Iterators = In python iterators can be used to get an iterator from an iterable objects (list, tuple, set)
# Iterator can be implement an iterator protocol in which it executes iter and next functions.
# After iteration over the object then it shows an warning to StopIteration to avoid StopIteration we can use for loop

# list1 = [10, 25, 45, 65]
# val = iter(list1)
# for item in val:
#     print(item, end=" ")

# list1 = [10, 25, 45, 65]
# val = iter(list1)
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))

dictionary = {"name":"raj", "age":32, "address":"kop","state":"mh"}
variable = iter(dictionary)
for item in variable:
    print(item, dictionary[item])
# for item in variable:
#     print(item, dictionary[item])

