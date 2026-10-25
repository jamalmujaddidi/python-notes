# Polymorphism in Python
#
# Polymorphism in Python allows different classes
# to have methods with the same name but different
# behaviours.
#
# In object-oriented programming, Polymorphism means "many forms"
# and allows the same method, function or operator to behave
# differently depending on the object or data it works with.

# Types of Polymorphism

# 1_ Compile-time Polymorphism
# 2_Run-time Polymorphism

# example of Compile-time Polymorphism

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

calc = Calculator()
print(calc.multiply())
print(calc.multiply(4))
print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))


# Output
# 1
# 4
# 6
# 24


# ================================================================


# Runtime Polymorphism (Overriding)
# Runtime polymorphism means that the behavior of a method is
# decided while program is running, based on the object calling it.
# This happens through Method Overriding a child class provides its
# own version of a method already defined in the parent class.


class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())


# Output
# Bark
# Meow
# Some generic sound


class Area:
    def shap (self , length , width= None):
        if width is None:
            return length * length
        return length * width

a = Area()
print(a.shap(6,7))

# Output
# 42
# Notice that the same method name, shap(), handles different
# argument combinations and produces different results.


# Example: This code demonstrates overloading-like behavior
# using default and variable-length arguments. While Python
# does not support true method overloading, the same method
# can handle different numbers of arguments.

class Calculation:
    def cal(self,a = 1 , b = 1 ,*args ):
        result = a*b
        for num in args:
            result *= num
        return result

c = Calculation()
print(c.cal())
print (c.cal(2))
print (c.cal(2,5))
print (c.cal(2,5,7))
print (c.cal(2, 3,4, 5, 6))


# Output
# 1
# 2
# 10
# 70
# 720


class Product:
    def check (self, a, b):
        p = a +b
        return p

    def check (self, a, b, c ):
        p = a + b + c
        return p

t = Product()
print (t.check(2, 3, 6))


# Output
# 11

# Explanation:
#
# The first product() function accepts two arguments.
# The second product() function accepts three arguments.
# Python does not maintain both definitions of a function with the same name.
# When the second product() function is defined, it replaces the first one.
# Therefore, product(4, 5, 5) calls the second function.
# The function multiplies 4 × 5 × 5 and returns 100.
# If product(4, 5) is called, Python raises a TypeError because the active
# product() function requires three arguments.

# Using Variable Arguments (*args)
# The *args syntax allows a function to accept a variable number of positional
# arguments. The function can then determine how to process those arguments.


class Data:
    def add(self, datatype, *args):
        if datatype == 'int':
            res = 0
        elif datatype == 'str':
            res = ''
        for item in args:
            res += item
        print(res)
d = Data()
d.add('int', 5, 10)
d.add('str', 'Hi ', 'Mr John')


# Output
# 11
# Hi Mr John

# Explanation:
#
# datatype specifies how the arguments should be processed.
# *args accepts any number of additional positional arguments.
# For integers, the function starts with 0 and adds each value.
# For strings, the function starts with an empty string and
# concatenates the values.
# This approach allows one function to handle different numbers
# of arguments.

# Using Default Arguments
# Default arguments can be used when a function should
# work with optional parameters.

class Multiplication:

    def mul(self, a = None, b = None):

        if a is not None and b is None:
            print (a)

        else:
            print((a + b))

m = Multiplication()
m.mul(4)
m.mul(4,6)

# Output
# 5
# 2
# Explanation:
#
# a and b are assigned None by default.
# When both arguments are provided, their values are added.
# When only a is provided, b remains None.
# The conditional statement determines which operation should
# be performed.
# This approach is useful when only a small number of argument
# combinations are required.


# Example of multiple_dispatch

class Multiple_dispatch:
    from multipledispatch import dispatch

    @dispatch(int, int)
    def product(first, second):
        result = first * second
        print(result)

    @dispatch(int, int, int)
    def product(first, second, third):
        result = first * second * third
        print(result)

    @dispatch(float, float, float)
    def product(first, second, third):
        result = first * second * third
        print(result)


md = Multiple_dispatch()
md.product(2, 3, )
md.product(2, 3 ,2)
md.product(2.2, 3.4, 2.3)


# Output:
# 6
# 12
# 17.204
# Explanation:
# •	@dispatch registers different versions of the product() function.
# •	Each version specifies the expected argument types.
# •	The appropriate function is selected based on the number and
# types of arguments.
# •	This provides behavior closer to traditional method overloading.
# •	multipledispatch is useful when different argument signatures
# require different implementations.


