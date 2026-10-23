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