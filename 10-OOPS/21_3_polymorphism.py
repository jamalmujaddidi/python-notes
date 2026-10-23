from tkinter.scrolledtext import example

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