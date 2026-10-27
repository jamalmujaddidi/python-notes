# ================================================================
# 21.3 — POLYMORPHISM IN PYTHON
# ================================================================
#
# Polymorphism means "many forms". It allows the same method,
# function, or operator to behave differently depending on the
# object or data it works with.
#
# In Python, polymorphism commonly appears through:
#   1. Duck typing
#   2. Method overriding
#   3. Built-in functions and operators working with different types
#   4. Overloading-like behavior using default arguments and *args
#   5. Type-based dispatch with a library such as multipledispatch
#
# Important note about compile-time and run-time polymorphism:
# Some OOP resources classify polymorphism as compile-time and
# run-time. Python does not provide traditional signature-based
# method overloading built into the language. Examples that use
# default parameters, *args, or multipledispatch are handled at
# runtime; default parameters and *args are not true method overloads.
#


# ================================================================
# 21.3.1 — DUCK TYPING
# ================================================================
# Duck typing means that Python code can work with an object based
# on the behavior it provides, rather than requiring a particular
# class or inheritance relationship.

class PDFReport:
    def save(self):
        print("Saving report as a PDF file.")


class TextReport:
    def save(self):
        print("Saving report as a text file.")


def save_report(report):
    report.save()


pdf_report = PDFReport()
text_report = TextReport()

save_report(pdf_report)
save_report(text_report)

# Output:
# Saving report as a PDF file.
# Saving report as a text file.
#
# Explanation:
# - PDFReport and TextReport are separate classes.
# - Both provide a save() method.
# - save_report() calls that method without checking the object's class.
# - Each object supplies its own behavior.


# ================================================================
# 21.3.2 — POLYMORPHISM THROUGH METHOD OVERRIDING
# ================================================================
# Method overriding occurs when a child class provides its own
# implementation of a method inherited from its parent class.
# This allows the same method call to behave differently for
# different object types.

class Payment:
    def process(self):
        print("Processing a general payment.")


class CardPayment(Payment):
    def process(self):
        super().process()
        print("Processing payment by card.")


class CashPayment(Payment):
    def process(self):
        super().process()
        print("Processing payment in cash.")


card = CardPayment()
cash = CashPayment()

card.process()
cash.process()


# Output:
# Processing a general payment.
# Processing payment by card.
# Processing a general payment.
# Processing payment in cash.


class Employee ():
    def __init__(self):
        self.Employee_role = "Employee"

    def display (self):
        print(f"his is an {self.Employee_role} here")

class Manager (Employee):
    def __init__(self):
        super().__init__()
        self.role = "Manager"

    def display(self):
        super().display()
        print(f"he is the {self.role}")

m = Manager ()
m.display()
# ________________________________________
# Output:
# his is an Employee here
# he is the Manager


# ================================================================
# 21.3.3 — OVERLOADING-LIKE BEHAVIOR WITH DEFAULT ARGUMENTS AND *args
# ================================================================
# Traditional method overloading means defining multiple methods
# with the same name but different parameter lists.
# Python does not support that pattern directly. One method can,
# however, accept different numbers of arguments using default
# parameters and *args.

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for number in args:
            result *= number
        return result


calculator = Calculator()

print(calculator.multiply())
print(calculator.multiply(4))
print(calculator.multiply(2, 3))
print(calculator.multiply(2, 3, 4))

# Output:
# 1
# 4
# 6
# 24
#
# Explanation:
# - a and b default to 1 when they are not provided.
# - *args collects additional positional arguments into a tuple.
# - The method multiplies all the supplied values.
# - This is flexible argument handling, not traditional method overloading.


# ================================================================
# 21.3.4 — USING A DEFAULT PARAMETER FOR DIFFERENT ARGUMENT COMBINATIONS
# ================================================================
# The width parameter defaults to None. If the caller omits width,
# the method calculates the area of a square. Otherwise, it calculates
# the area of a rectangle.

class Area:
    def area(self, length, width=None):
        if width is None:
            return length * length
        return length * width


shape = Area()
print(shape.area(6, 7))
print(shape.area(6))

# Output:
# 42
# 36
#
# Explanation:
# - area(6, 7) calculates 6 * 7 = 42.
# - area(6) treats the shape as a square and calculates 6 * 6 = 36.
# - One method supports two argument combinations using a default value.


# ================================================================
# 21.3.5 — DEFINING THE SAME METHOD NAME TWICE IN A CLASS
# ================================================================
# Python does not keep two methods with the same name in a class
# namespace. The later definition replaces the earlier definition.
# This is not traditional method overloading.

class Product:
    def check(self, a, b):
        return a + b

    def check(self, a, b, c):
        return a + b + c


product = Product()
print(product.check(2, 3, 6))

# Output:
# 11
#
# Explanation:
# - The second check() definition replaces the first check() definition.
# - The remaining check() method requires three arguments (besides self).
# - product.check(2, 3, 6) returns 2 + 3 + 6 = 11.
# - Calling product.check(2, 3) would raise TypeError because the
#   active method requires the third argument as well.


# ================================================================
# 21.3.6 — USING *args WITH A SELECTOR PARAMETER
# ================================================================
# Here, datatype is a regular parameter that tells the method whether
# it should add integers or concatenate strings. The labels 'int' and
# 'str' are strings; they are not the int and str type objects.

class Data:
    def add(self, datatype, *args):
        if datatype == "int":
            result = 0
        elif datatype == "str":
            result = ""
        else:
            raise ValueError("datatype must be 'int' or 'str'")

        for item in args:
            result += item

        print(result)


data = Data()
data.add("int", 5, 10)
data.add("str", "Hi ", "Mr John Smith")

# Output:
# 15
# Hi Mr John Smith
#
# Explanation:
# - datatype selects the initial value and intended operation.
# - *args collects the remaining positional arguments into a tuple.
# - For integers, result starts at 0 and the values are added.
# - For strings, result starts as an empty string and values are joined.
# - The ValueError gives a clear message for an unsupported label.


# ================================================================
# 21.3.7 — USING DEFAULT ARGUMENTS TO SUPPORT OPTIONAL INPUT
# ================================================================
# If only one argument is provided, this method returns that value.
# If two arguments are provided, it returns their sum. This is another
# example of flexible behavior, not traditional method overloading.

class FlexibleAddition:
    def add_or_return(self, a, b=None):
        if b is None:
            return a
        return a + b


flexible = FlexibleAddition()
print(flexible.add_or_return(4))
print(flexible.add_or_return(4, 6))

# Output:
# 4
# 10


# ================================================================
# Polymorphism Using @singledispatchmethod Library:
# ================================================================

# singledispatchmethod is provided by Python's standard library,
# so you don't need to install an external package. It has been
# available since Python 3.8.
#
# Imagine a program that formats different kinds of messages.
# Numbers should be labelled as numbers, while strings should
# be labelled as messages.

# Example:


from functools import singledispatchmethod


class MessageFormatter:

    @singledispatchmethod
    def format(self, value):
        print("Unsupported data type.")

    @format.register
    def _(self, value: int):
        print(f"Number: {value}")

    @format.register
    def _(self, value: str):
        print(f"Message: {value}")


formatter = MessageFormatter()

formatter.format(25)
formatter.format("Hello, John Smith!")
formatter.format(32.4)

# Output:

# Number: 25
# Message: Hello, John Smith!
# Unsupported data type.

# Explanation:
# Here we called format () twice, using the same method name. But Python
# selected different implementations because we supplied different types
# of arguments.

# =======================================================================

# another Example of @singledispatchmethod


from functools import singledispatchmethod


class NotificationSender:

    @singledispatchmethod
    def send(self, message):
        raise TypeError(
            f"Unsupported type: {type(message).__name__}"
        )

    @send.register
    def _(self, message: str):
        print(f"Sending notification: {message}")

    @send.register
    def _(self, messages: list):
        print("Sending batch notifications:")
        for message in messages:
            print(f"- {message}")


sender = NotificationSender()

sender.send("Your order has been shipped.")

sender.send([
    "Payment received.",
    "Your delivery is scheduled for tomorrow."
])



# Output:

# Sending notification: Your order has been shipped.
# Sending batch notifications:
# - Payment received.
# - Your delivery is scheduled for tomorrow.

# Explanation:


# @singledispatchmethod allows one method name to support different
# implementations selected according to the type of its argument.
#
# For this example, send() handles strings and lists differently
# without requiring us to write explicit if/elif type checks inside
# the method.

# ================================================================
# 21.3.8 — MULTIPLE DISPATCH WITH THE multipledispatch LIBRARY
# ================================================================
# multipledispatch is a third-party library. Install it in the project's
# active virtual environment with:
#     python -m pip install multipledispatch
#
# Its @dispatch decorator selects an implementation based on the number
# and types of arguments. This is closer to traditional overloading,
# but dispatch selection happens at runtime and requires the library.

from multipledispatch import dispatch


class MultipleDispatch:
    @dispatch(int, int)
    def product(self, first, second):
        return first * second

    @dispatch(int, int, int)
    def product(self, first, second, third):
        return first * second * third

    @dispatch(float, float, float)
    def product(self, first, second, third):
        return first * second * third


multiple = MultipleDispatch()
print(multiple.product(2, 3))
print(multiple.product(2, 3, 2))
print(multiple.product(2.2, 3.4, 2.3))

# Output:
# 6
# 12
# 17.204
#
# Explanation:
# - @dispatch registers implementations for different signatures.
# - Two integers select the two-argument implementation.
# - Three integers select the three-integer implementation.
# - Three floats select the three-float implementation.
# - Because this library is external, it must be installed in the
#   same Python environment used to run this file.


# ================================================================
# 21.3 — SUMMARY
# ================================================================
# - Polymorphism means one interface can provide different behaviors.
# - Duck typing focuses on the behavior an object provides.
# - Method overriding lets child classes customize inherited behavior.
# - Default parameters and *args allow flexible argument combinations,
#   but do not create traditional multiple method definitions.
# - Defining the same method name twice in one class does not overload it;
#   the later definition replaces the earlier one.
# - multipledispatch is an external library for dispatching by argument
#   count and types at runtime.



