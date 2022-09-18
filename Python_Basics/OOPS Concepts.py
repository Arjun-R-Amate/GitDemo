#: Q What is OOPS and pillers or types of oops ?
#: Ans = object oriented programming contains classes and objects.
# Class is an blueprint for creating an object
# object is used to access the properties and methods of specific class , object is the instance of the class.
# __init__(self) is a constructor which is used to initialise the properties of class , self is the current reference of the instace
#Abstraction,  Polymorphism, Encapsulation, Inheritance  these are main types of OOPS

#Abstraction
# abstraction means hiding implementation details and show essential data.
# A class containgin one or more abstract methods is known as abstarct class
# abstract methods do not contain any implementation instead all the implementation can be defined in the methods of
# sub-classes that inherit the abstract class.
# An abstract class is created by importing an class named ABC from the abc module
# Abstract class can not be instantiated i.e. we can not create an object for abstract class.


from abc import ABC
class Shape(ABC):
    def calculate_area(self):
        pass

class Rectangle(Shape):
    lenght = 10
    breadth = 5
    def calculate_area(self):
        return self.lenght * self.breadth

class Circle(Shape):
    radius = 4
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

obj = Rectangle()
print(obj.calculate_area())
obj1 = Circle()
print(obj1.calculate_area())

import sys
sys.exit(0)

# Polymorphism = In python polymorphism can be achived by using method overloading and method overriding
# Polymorphism means implement same thing in different ways
# Polymorphism means same function name but different signatures.
# Method Overloading : operator overloading and method overloading
# : When adding an two numbers done arithmetic addition
def addition(a, b):
    return (a + b)
result = addition("hello" ," " "welcome")
print(result)

class Moverloading:
    def dispaly(self, a= None, b = None):
        print(a, b)
obj = Moverloading()
obj.dispaly()
obj.dispaly(10)
obj.dispaly(10, 20)

# Method overriding: method name and number of arguments are same in base class and derived class this concept is known as method overriding
# Method overriding needs an inheritance concepts
class Parent:
    def transportation(self):
        print("Cycle")

class Child(Parent):
    def transportation(self):
        print("Bike")

obj = Child()
obj.transportation()

import sys
sys.exit(0)

# Encapsulation : In python encapsulation can achived by changing an scope from public variables and methods to private variable and methods
# Here we can restict the access of variables and methods
# by using __ at begining of variable and method name
# Private variables and private methods are accessed only within that class not outside of that class.
# Public variables and public methods can be accessed inside as well as outside the class.
# Protected variable can be accessed within that package
# Global variable can be accessed inside as well as outside the function.
class Encap:
    __a = 10
    def ply(self):
        print(self.__a)
        print("Weloxcmwe")
obj= Encap()
obj.ply()

# with the help of init constructor we can access the private variables and private methods.

class Encassu:
    __name = "raj"
    def __init__(self):
        print(self.__name)

    def reading(self):
        print(self.__name, "is reading an book")
obj = Encassu()
obj.reading()

import sys
sys.exit(0)
# Inheritance = Derived/child class inhertis the properties and methods from Base/Parent class is known as Inheritance.
#(Types of inheritance = Single, Multi-level, Multiple, Hierarchical)
#Hierarchical Inheritance == one parent inherit into multiple child
class Parent:
    def __init__(self, pname, page):
        self.parentname =pname
        self.parentage = page

    def watching_tv(self):
        print(self.parentname, "is watching an television.")

class Child1(Parent):
    def __init__(self, pname, page, c1name, c1age):
        Parent.__init__(self, pname, page)
        self.child1name = c1name
        self.child1age = c1age

    def reading_book(self):
        print(self.child1name, "is reading an books")


class Child2(Parent):
    def __init__(self, pname, page, c2name, c2age):
        Parent.__init__(self, pname, page)
        self.child2name = c2name
        self.child2age = c2age

    def reading_books(self):
        print(self.child2name, "is reading an books")


obj = Child1("Ram", 65, "ketan", 25)
print(obj.parentname, obj.parentage, obj.child1name, obj.child1age)
obj.watching_tv()
obj.reading_book()
obj1 = Child2("Ram", 65, "nitin", 22)
print(obj1.parentname, obj1.parentage, obj1.child2name, obj1.child2age)
obj.watching_tv()
obj.reading_book()

import sys
sys.exit(0)
#Multiple - Inheritance == one child inherits properties from fathert and mother
class Parent:
    def __init__(self, pname, page):
        self.parentname = pname
        self.parentage = page

    def watching_tv(self):
        print(self.parentname, "is watching an television.")

class Mother:
    def __init__(self, mname, mage):
        self.mothername = mname
        self.motherage = mage

    def cooking(self):
        print(self.mothername, "is cooking food")

class Child(Parent, Mother):
    def __init__(self, pname, page, mname, mage, cname, cage):
        Parent.__init__(self, pname, page)
        Mother.__init__(self, mname, mage)
        self.childname = cname
        self.childage = cage

    def playing(self):
        print(self.childname, "is playing crickert")

obj = Child("raja", 65, "rani", 60, "rajan", 35)
print(obj.parentname, obj.parentage)
obj.watching_tv()
print(obj.mothername, obj.motherage)
obj.cooking()
print(obj.childname, obj.childage)
obj.playing()


#Multi-Level Inheritance
class Parent:
    def __init__(self, pname, page, paddress):
        self.parentname = pname
        self.parentage = page
        self.parentaddress = paddress

    def reading(self):
        print(self.parentname, "is reading an newspaper ")

class Child1(Parent):
    def __init__(self, pname, page, paddress, c1name, c1age):
        Parent.__init__(self, pname, page, paddress)
        self.child1name = c1name
        self.child1age = c1age

    def playing(self):
        print(self.child1name, "is playing an crickect")

class Child2(Child1):
    def __init__(self, pname, page, paddress, c1name, c1age, c2name, c2age):
        Child1.__init__(self, pname, page, paddress, c1name, c1age)
        self.child2name = c2name
        self.child2age = c2age

    def studying(self):
        print(self.child2name, "is studying")

obj = Child2("Ram", 65, "Pune", "Raj", 25, "Rajesh", 22)
print(obj.parentname, obj.parentage, obj.parentaddress)
obj.reading()
print(obj.child1name, obj.child1age)
obj.playing()
print(obj.child2name, obj.child2age)
obj.studying()

import sys
sys.exit(0)

# Single inheritance
class Parent:
    def __init__(self, pname, page):
        self.parentname = pname
        self.parentage = page

    def reading(self):
        print(self.parentname, "is reading a newspaper")

class Child(Parent):
    def __init__(self, pname, page, cname, cage):
        Parent.__init__(self,pname,page)
        self.childname = cname
        self.childage = cage

    def playing(self):
        print(self.childname, "is playing cricket")
obj = Child("Ram",58, "raj", 20)
print(obj.parentname)
print(obj.parentage)
print(obj.childname)
print(obj.childage)
obj.reading()
obj.reading()