

"""
Topic 21.2: Inheritance in Python
=================================

21.2.0 Overview of Inheritance
21.2.1 Introduction to Inheritance
21.2.2 Parent Classes and Child Classes
21.2.3 Inheriting Attributes and Methods
21.2.4 The __init__() Method in Inheritance
21.2.5 Using super()

Inheritance is an OOP feature that allows a class to inherit
accessible attributes and methods from another class.

It promotes code reusability because common functionality can
be defined in a parent class and reused by child classes.

Terminology:
- Parent class: The class from which another class inherits.
- Child class: The class that inherits from another class.
- Base class: Another name for a parent class.
- Derived class: Another name for a child class.

General syntax:

class ChildClass(ParentClass):
    pass
"""


# ============================================================
# 21.2.0 - Overview of Inheritance
# ============================================================

# Inheritance allows a child class to reuse and extend
# the functionality of an existing parent class.
#
# Example hierarchy:
#
#             Animal
#             /    \
#           Dog    Cat
#
# Both Dog and Cat inherit from Animal.
# However, Dog and Cat do not automatically inherit from
# each other because they are sibling classes.


# ============================================================
# 21.2.1 - Introduction to Inheritance
# ============================================================

class Animal:

    def eat(self):
        print("This animal is eating.")


class Dog(Animal):

    def bark(self):
        print("The dog is barking.")


class Cat(Animal):

    def meow(self):
        print("The cat is meowing.")


dog1 = Dog()
cat1 = Cat()

dog1.eat()
dog1.bark()

cat1.eat()
cat1.meow()

# Output:
# This animal is eating.
# The dog is barking.
# This animal is eating.
# The cat is meowing.

# Explanation:
# 1. Dog inherits the eat() method from Animal.
# 2. Cat also inherits the eat() method from Animal.
# 3. Dog defines its own bark() method.
# 4. Cat defines its own meow() method.
# 5. cat1.bark() would raise an AttributeError because
#    Cat does not inherit from Dog and does not define bark().
#
# Main advantage:
# Inheritance promotes code reusability by allowing multiple
# child classes to reuse common methods from a parent class.


# ============================================================
# 21.2.2 - Parent Classes and Child Classes
# ============================================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    pass


student1 = Student("John Smith", 24)

print(student1.name)
print(student1.age)

student1.display_info()

# Output:
# John Smith
# 24
# Name: John Smith
# Age: 24

# Explanation:
# 1. Person is the parent class.
# 2. Student is the child class because it inherits from Person.
# 3. Student does not define its own __init__() method.
# 4. Therefore, Python can use the inherited Person.__init__().
# 5. The inherited initializer assigns name and age to student1.
# 6. Student can also use the inherited display_info() method.
#
# Important:
# name and age are instance attributes initialized on student1.
# They are not automatically class attributes of Student.


# ============================================================
# 21.2.3 - Inheriting Attributes and Methods
# ============================================================

class PersonWithStudy:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class StudentWithStudy(PersonWithStudy):

    def study(self):
        print(f"{self.name} is studying.")


student2 = StudentWithStudy("John Smith", 24)

student2.display_info()
student2.study()

# Output:
# Name: John Smith
# Age: 24
# John Smith is studying.

# Explanation:
# StudentWithStudy inherits:
# - The __init__() method from PersonWithStudy.
# - The display_info() method from PersonWithStudy.
#
# StudentWithStudy also defines its own study() method.
#
# The child class can therefore reuse inherited functionality
# and add new functionality of its own.
#
# Inherited methods can access attributes initialized on the
# current instance, such as self.name and self.age.


# ============================================================
# 21.2.4 - The __init__() Method in Inheritance
# ============================================================

# Case 1: The child class does not define __init__().


class PersonForInit:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class StudentInheritsInit(PersonForInit):
    pass


student3 = StudentInheritsInit("John Smith", 24)

print(student3.name)
print(student3.age)

# Output:
# John Smith
# 24

# Explanation:
# Since StudentInheritsInit does not define __init__(),
# it can use the initializer inherited from PersonForInit.


# Case 2: The child class defines its own __init__().


class StudentOwnInit(PersonForInit):

    def __init__(self, student_id):
        self.student_id = student_id


student4 = StudentOwnInit("S101")

print(student4.student_id)

# Output:
# S101

# Explanation:
# StudentOwnInit defines its own __init__(), so Python uses
# that initializer when creating a StudentOwnInit instance.
#
# The parent initializer is NOT called automatically.
# Therefore, name and age have not been initialized on student4.
#
# Uncommenting the following line raises AttributeError:
#
# print(student4.name)


# ============================================================
# 21.2.5 - Using super()
# ============================================================

# super() provides access to methods in the next class in the
# method resolution order (MRO).
#
# In this example, super().__init__() calls the parent
# initializer without repeating its attribute assignments.


class PersonBase:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class StudentWithSuper(PersonBase):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student5 = StudentWithSuper("John Smith", 24, "S102")

print(student5.name)
print(student5.age)
print(student5.student_id)

student5.display_info()

# Output:
# John Smith
# 24
# S102
# Name: John Smith
# Age: 24

# Explanation:
# 1. StudentWithSuper defines its own __init__().
# 2. super().__init__(name, age) calls the next class's
#    initializer in the MRO, which is PersonBase here.
# 3. PersonBase.__init__() initializes name and age.
# 4. StudentWithSuper.__init__() then initializes student_id.
# 5. student5 can also call display_info(), inherited from
#    PersonBase.
#
# Using super() avoids repeating the parent's initialization code.


# ============================================================
# Summary
# ============================================================

# 1. Inheritance allows a child class to reuse and extend
#    functionality from a parent class.
#
# 2. The syntax is:
#       class ChildClass(ParentClass):
#           pass
#
# 3. Child classes can use accessible inherited methods.
#
# 4. A child class can define its own additional methods
#    and attributes.
#
# 5. If a child class does not define __init__(), it can use
#    an inherited initializer.
#
# 6. If a child class defines its own __init__(), Python does
#    not automatically call the parent's initializer.
#
# 7. super().__init__(...) is a common way to call the next
#    class's initializer in the MRO.
#
# 8. Sibling classes do not automatically inherit methods
#    from each other.



"""
Topic 21.2.6: The super() Function in Python
============================================


super() is a built-in Python function that provides a proxy
for accessing methods in the next class in the Method
Resolution Order (MRO).

In simple inheritance examples, this often means calling
a method defined in the parent class.

However, super() does not always call the direct parent.
Its behavior follows the MRO.
"""


# ============================================================
# 21.2.6.0 - Introduction to super()
# ============================================================

# super() is commonly used in inheritance to:
#
# 1. Call an inherited initializer.
# 2. Reuse a method defined in another class in the MRO.
# 3. Avoid repeating code from a parent class.
# 4. Support cooperative multiple inheritance.
#
# General syntax:
#
# super().method_name(arguments)


# ============================================================
# 21.2.6.1 - Calling a Parent Initializer with super()
# ============================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student1 = Student("John Smith", 24, "S101")

print(student1.name)
print(student1.age)
print(student1.student_id)

# Output:
# John Smith
# 24
# S101

# Explanation:
# 1. Person.__init__() initializes name and age.
# 2. Student.__init__() calls super().__init__(name, age).
# 3. The parent's initializer initializes those attributes.
# 4. Execution returns to Student.__init__().
# 5. Student.__init__() then initializes student_id.
#
# super() does not create a separate Person instance.
# The attributes are initialized on the existing Student instance.
#
# Python automatically supplies self when calling the bound
# initializer, so we do not write:
#
# super().__init__(self, name, age)


# ============================================================
# 21.2.6.2 - Calling Parent Methods with super()
# ============================================================

class PersonIntroduction:
    def introduce(self):
        print("I am a person.")


class StudentIntroduction(PersonIntroduction):
    def introduce(self):
        super().introduce()
        print("I am also a student.")


student2 = StudentIntroduction()
student2.introduce()

# Output:
# I am a person.
# I am also a student.

# Explanation:
# StudentIntroduction overrides introduce().
#
# Inside the overriding method, super().introduce() calls
# the next implementation in the MRO.
#
# The child then continues executing its own code.
#
# This allows the child to reuse and extend existing behavior
# instead of replacing it completely.


# ============================================================
# 21.2.6.3 - Understanding Method Resolution Order (MRO)
# ============================================================

# Method Resolution Order (MRO) is the order in which Python
# searches classes for an attribute or method.


class MROAnimal:
    def speak(self):
        print("Animal makes a sound.")


class MRODog(MROAnimal):
    pass


dog1 = MRODog()
dog1.speak()

# Output:
# Animal makes a sound.

# Explanation:
# Python first searches MRODog for speak().
# MRODog does not define speak(), so Python searches MROAnimal.
# It finds and executes the inherited method.


# Display the MRO as class names.

print([cls.__name__ for cls in MRODog.mro()])

# Output:
# ['MRODog', 'MROAnimal', 'object']

# Explanation:
# Python searches in this order:
#
# 1. MRODog
# 2. MROAnimal
# 3. object
#
# object is the common base class at the root of the
# hierarchy for ordinary Python classes.


# ============================================================
# 21.2.6.4 - mro() Method vs __mro__ Attribute
# ============================================================

# mro() is a method that returns a list of classes.
# __mro__ is an attribute that contains a tuple of classes.


print([cls.__name__ for cls in MRODog.mro()])
print([cls.__name__ for cls in MRODog.__mro__])

# Output:
# ['MRODog', 'MROAnimal', 'object']
# ['MRODog', 'MROAnimal', 'object']


# Check their types.

print(type(MRODog.mro()))
print(type(MRODog.__mro__))

# Output:
# <class 'list'>
# <class 'tuple'>

# Differences:
#
# mro() method:
# - Called with parentheses: MRODog.mro()
# - Returns a list of classes.
#
# __mro__ attribute:
# - Accessed without parentheses: MRODog.__mro__
# - Contains a tuple of classes.
#
# Both expose the class's MRO.
# A metaclass can customize the order calculated by overriding
# mro() during class creation.


# ============================================================
# 21.2.6.5 - super() in Multiple Inheritance
# ============================================================

# Multiple inheritance occurs when a class inherits from
# more than one parent class.


class FirstParent:
    def show(self):
        print("Method from FirstParent")


class SecondParent:
    def show(self):
        print("Method from SecondParent")


class CombinedChild(FirstParent, SecondParent):
    pass


combined1 = CombinedChild()
combined1.show()

# Output:
# Method from FirstParent

print([cls.__name__ for cls in CombinedChild.mro()])

# Output:
# ['CombinedChild', 'FirstParent', 'SecondParent', 'object']

# Explanation:
# Python checks CombinedChild first.
# Since it does not define show(), Python checks FirstParent.
# It finds show() there and stops searching.
# SecondParent.show() is not called by this example.


# ------------------------------------------------------------
# super() follows the MRO, not simply the direct parent
# ------------------------------------------------------------

class Root:
    def show(self):
        print("Root")


class Left(Root):
    def show(self):
        print("Left")
        super().show()


class Right(Root):
    def show(self):
        print("Right")
        super().show()


class Bottom(Left, Right):
    def show(self):
        print("Bottom")
        super().show()


bottom1 = Bottom()
bottom1.show()

# Output:
# Bottom
# Left
# Right
# Root


# Display the method resolution order.

print([cls.__name__ for cls in Bottom.mro()])

# Output:
# ['Bottom', 'Left', 'Right', 'Root', 'object']

# Explanation:
# 1. Bottom.show() prints "Bottom".
# 2. super() in Bottom continues to Left.show().
# 3. super() in Left continues to Right.show().
# 4. super() in Right continues to Root.show().
# 5. Root.show() does not call super(), so the chain ends.
#
# Notice:
# super() inside Left does not simply call Left's direct
# parent, Root. It continues to the next class in the MRO,
# which is Right in this inheritance hierarchy.
#
# Cooperative methods must call super() when appropriate
# for the chain to continue.


# ============================================================
# 21.2.6.6 - Summary
# ============================================================

# 1. super() provides access to methods in the next class
#    in the Method Resolution Order (MRO).
#
# 2. super().__init__(...) is commonly used to call an
#    inherited initializer without repeating initialization.
#
# 3. super() can call methods other than __init__().
#
# 4. When a child overrides a method, super() can call the
#    next implementation and allow the child to extend it.
#
# 5. MRO determines the order Python follows when searching
#    for methods.
#
# 6. mro() returns a list of classes.
#
# 7. __mro__ provides the MRO as a tuple of classes.
#
# 8. In multiple inheritance, super() follows the MRO rather
#    than always calling a fixed or direct parent.
#
# 9. For cooperative multiple inheritance, participating
#    methods should use super() appropriately and have
#    compatible method signatures.



# ============================================================
# 21.2.7 - Method Overriding in Python
# ============================================================

# Method overriding occurs when a child class defines a method
# with the same name as a method defined in its parent class.
#
# The child class provides its own implementation of that method.
#
# Method overriding allows a child class to customize behavior
# inherited from its parent class.


# ============================================================
# 21.2.7.1 - Basic Method Overriding
# ============================================================

class Vehicle:
    def start(self):
        print("The vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print("The car is starting with a key.")


car1 = Car()
car1.start()

# Output:
# The car is starting with a key.

# Explanation:
# Car inherits from Vehicle but defines its own start() method.
# Python finds Car.start() first and executes it.
#
# The method defined in Vehicle is not deleted or replaced
# globally. It is simply overridden for Car instances.


# ============================================================
# 21.2.7.2 - Different Child Classes Overriding the Same Method
# ============================================================

class Payment:
    def pay(self):
        print("Processing payment.")


class CashPayment(Payment):
    def pay(self):
        print("Payment made using cash.")


class CardPayment(Payment):
    def pay(self):
        print("Payment made using a card.")


cash = CashPayment()
card = CardPayment()

cash.pay()
card.pay()

# Output:
# Payment made using cash.
# Payment made using a card.

# Explanation:
# CashPayment and CardPayment both inherit from Payment.
#
# Each child class overrides pay() with its own implementation.
# The same method name produces different behavior depending
# on the type of instance used to call it.


# ============================================================
# 21.2.7.3 - Method Overriding and MRO
# ============================================================

class Device:
    def info(self):
        print("This is an electronic device.")


class Phone(Device):
    def info(self):
        print("This is a mobile phone.")


phone1 = Phone()
phone1.info()

# Output:
# This is a mobile phone.

print([cls.__name__ for cls in Phone.mro()])

# Output:
# ['Phone', 'Device', 'object']

# Explanation:
# MRO stands for Method Resolution Order.
#
# Python searches Phone first and finds info() there.
# Therefore, Device.info() is not executed automatically.
#
# MRO determines the order in which Python searches for
# a method, but it does not automatically execute every
# implementation of that method.


# ============================================================
# 21.2.7.4 - Calling the Parent Method Using super()
# ============================================================

class Employee:
    def introduce(self):
        print("I work for the company.")


class Manager(Employee):
    def introduce(self):
        super().introduce()
        print("I also manage a team.")


manager1 = Manager()
manager1.introduce()

# Output:
# I work for the company.
# I also manage a team.

# Explanation:
# Manager overrides introduce().
#
# super().introduce() calls the next implementation in the MRO.
# In this example, it calls Employee.introduce().
#
# After the parent method finishes, execution returns to
# Manager.introduce(), which prints its additional message.
#
# This allows a child class to reuse and extend the parent's
# behavior rather than replacing it completely.


# ============================================================
# 21.2.7.5 - Calling a Specific Parent Method Directly
# ============================================================

class Account:
    def account_type(self):
        print("General account.")


class SavingsAccount(Account):
    def account_type(self):
        print("Savings account.")


account1 = SavingsAccount()

account1.account_type()
Account.account_type(account1)

# Output:
# Savings account.
# General account.

# Explanation:
# account1.account_type() calls the overridden method
# defined in SavingsAccount.
#
# Account.account_type(account1) directly calls the method
# defined in Account.
#
# Because account_type() is an instance method, we explicitly
# pass account1 as the self argument when calling it through
# the class.
#
# Unlike super(), this direct call explicitly names the
# implementation to execute.


# ============================================================
# Method Overriding with Constructors
# ============================================================

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


# ============================================================
# 21.2.7.6 - Calling an Instance Method Through the Class
# ============================================================

class Speaker:
    def announce(self):
        print("The announcement has started.")


speaker1 = Speaker()

speaker1.announce()
Speaker.announce(speaker1)

# Output:
# The announcement has started.
# The announcement has started.

# Explanation:
# When we call speaker1.announce(), Python automatically
# passes speaker1 as self.
#
# When we call Speaker.announce(speaker1), we must provide
# the instance explicitly.
#
# Calling Speaker.announce() without an instance raises
# TypeError because the required self argument is missing.


# ============================================================
# 21.2.7.7 - Important Rules of Method Overriding
# ============================================================

# 1. A child class can override an inherited method by
#    defining a method with the same name.
#
# 2. During normal method lookup, Python uses the MRO to
#    determine which implementation to find.
#
# 3. Python does not automatically execute both the parent
#    and child implementations of an overridden method.
#
# 4. Use super().method_name() to call the next implementation
#    in the MRO when appropriate.
#
# 5. A specific parent implementation can also be called
#    directly using ParentClass.method_name(self).
#
# 6. When calling an instance method through its class,
#    the instance must be passed explicitly.
#
# 7. Overriding allows child classes to customize inherited
#    behavior while keeping a common method name.


# ============================================================
# 21.2.7.8 - Summary
# ============================================================

# Method overriding allows a child class to provide its own
# implementation of a method defined in its parent class.
#
# Python finds the child's implementation first when normal
# lookup locates the method in the child class.
#
# The parent's implementation remains available.
#
# We can use super() to call the next implementation in the
# MRO, or explicitly call a particular parent's method.
#
# Method overriding is useful when a child class needs to
# customize or extend inherited behavior.




# ============================================================
# 21.2.8 - Types of Inheritance in Python
# ============================================================

# Inheritance types describe how parent and child classes
# are connected in a class hierarchy.
#
# The five commonly taught types are:
#
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# ============================================================
# 21.2.8.1 - Single Inheritance
# ============================================================

# Single inheritance occurs when a child class inherits
# directly from one parent class.


class Appliance:
    def switch_on(self):
        print("The appliance is switched on.")


class WashingMachine(Appliance):
    def wash_clothes(self):
        print("The washing machine is washing clothes.")


machine = WashingMachine()

machine.switch_on()
machine.wash_clothes()

# Output:
# The appliance is switched on.
# The washing machine is washing clothes.

# Explanation:
# WashingMachine inherits from one parent class: Appliance.
#
# switch_on() is inherited from Appliance.
# wash_clothes() is defined in WashingMachine.
#
# Structure:
#
# Appliance
#     |
# WashingMachine


# Another Example

class Employee:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"Employee name: {self.name}")


class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing Python code.")


developer1 = Developer("John Smith")

developer1.show_details()
developer1.write_code()


# Output:
# Employee name: John Smith
# John Smith is writing Python code.
#
#
# What happens?
#
# Developer inherits __init__() and show_details() from
# Employee. It also defines its own write_code() method.
#
# This is single inheritance because Developer directly
# inherits from one parent class.


# ============================================================
# 21.2.8.2 - Multiple Inheritance
# ============================================================

# Multiple inheritance occurs when one child class inherits
# directly from two or more parent classes.


class Printer:
    def print_document(self):
        print("Printing the document.")


class Scanner:
    def scan_document(self):
        print("Scanning the document.")


class OfficeMachine(Printer, Scanner):
    def make_copy(self):
        print("Making a copy of the document.")


office_machine = OfficeMachine()

office_machine.print_document()
office_machine.scan_document()
office_machine.make_copy()

# Output:
# Printing the document.
# Scanning the document.
# Making a copy of the document.

# Explanation:
# OfficeMachine inherits from both Printer and Scanner.
#
# It can use print_document() from Printer,
# scan_document() from Scanner,
# and its own make_copy() method.
#
# Structure:
#
# Printer       Scanner
#     \          /
#      \        /
#     OfficeMachine


# Anothr Example

class Camera:
    def take_photo(self):
        print("Taking an aerial photograph.")


class GPS:
    def show_location(self):
        print("Displaying the drone's location.")


class Drone(Camera, GPS):
    def fly(self):
        print("The drone is flying.")


drone1 = Drone()

drone1.take_photo()
drone1.show_location()
drone1.fly()


# Output:
# Taking an aerial photograph.
# Displaying the drone's location.
# The drone is flying.
#
#
# What happens?
#
# Drone inherits from both Camera and GPS. Therefore, its instance can
# call methods from both parent classes, as well as its own fly() method.
#
# This is multiple inheritance because one child class inherits directly
# from more than one parent class.




# ============================================================
# 21.2.8.3 - Multilevel Inheritance
# ============================================================

# Multilevel inheritance occurs when inheritance forms
# a chain of classes.


class Account:
    def show_account_type(self):
        print("This is a bank account.")


class BankAccount(Account):
    def deposit(self):
        print("Money deposited successfully.")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Calculating savings interest.")


savings = SavingsAccount()

savings.show_account_type()
savings.deposit()
savings.calculate_interest()

# Output:
# This is a bank account.
# Money deposited successfully.
# Calculating savings interest.

# Explanation:
# BankAccount inherits from Account.
# SavingsAccount inherits from BankAccount.
#
# Therefore, SavingsAccount can use methods from both
# BankAccount and Account, as well as its own methods.
#
# Structure:
#
# Account
#    |
# BankAccount
#    |
# SavingsAccount


# another example

class Content:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        print(f"Title: {self.title}")


class Course(Content):
    def __init__(self, title, subject):
        super().__init__(title)
        self.subject = subject

    def show_subject(self):
        print(f"Subject: {self.subject}")


class OnlineCourse(Course):
    def __init__(self, title, subject, platform):
        super().__init__(title, subject)
        self.platform = platform

    def show_platform(self):
        print(f"Platform: {self.platform}")


course1 = OnlineCourse("Python Programming", "Computer Science", "Online")

course1.show_title()
course1.show_subject()
course1.show_platform()


# Output:
# Title: Python Programming
# Subject: Computer Science
# Platform: Online

# How does it work?
# Course inherits from Content.
#
# OnlineCourse inherits from Course.
#
# super() calls the next initializer in the MRO,
# so the title and subject attributes are initialized
# before platform.
#
# The OnlineCourse instance can use methods from all three classes.



# ============================================================
# 21.2.8.4 - Hierarchical Inheritance
# ============================================================

# Hierarchical inheritance occurs when two or more child
# classes inherit from the same parent class.


class Shape:
    def describe(self):
        print("This is a geometric shape.")


class Circle(Shape):
    def draw_circle(self):
        print("Drawing a circle.")


class Rectangle(Shape):
    def draw_rectangle(self):
        print("Drawing a rectangle.")


circle = Circle()
rectangle = Rectangle()

circle.describe()
circle.draw_circle()

rectangle.describe()
rectangle.draw_rectangle()

# Output:
# This is a geometric shape.
# Drawing a circle.
# This is a geometric shape.
# Drawing a rectangle.

# Explanation:
# Circle and Rectangle both inherit from Shape.
#
# Both child classes can use describe().
# Circle defines draw_circle(), while Rectangle defines
# draw_rectangle().
#
# Structure:
#
#          Shape
#          /   \
#     Circle   Rectangle



# Another Example
# A school has different types of members. Both teachers and
# students share common information, but each has different
# responsibilities.


class SchoolMember:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Teacher(SchoolMember):
    def teach(self):
        print(f"{self.name} is teaching mathematics.")


class Student(SchoolMember):
    def study(self):
        print(f"{self.name} is studying mathematics.")


teacher1 = Teacher("John Smith")
student1 = Student("David")

teacher1.introduce()
teacher1.teach()

student1.introduce()
student1.study()


# Output:
# My name is John Smith.
# John Smith is teaching mathematics.
# My name is David.
# David is studying mathematics.


# Explanation

# This is hierarchical inheritance because two child classes,
# Teacher and Student, inherit directly from the same parent class,
# SchoolMember.



# ============================================================
# 21.2.8.5 - Hybrid Inheritance
# ============================================================

# Hybrid inheritance combines two or more inheritance
# patterns within the same class hierarchy.
#
# This example combines multilevel inheritance and
# multiple inheritance.


class Transport:
    def move(self):
        print("The transport is moving.")


class Car(Transport):
    def drive(self):
        print("The car is being driven.")


class ElectricFeature:
    def charge_battery(self):
        print("The battery is charging.")


class ElectricCar(Car, ElectricFeature):
    def show_type(self):
        print("This is an electric car.")


electric_car = ElectricCar()

electric_car.move()
electric_car.drive()
electric_car.charge_battery()
electric_car.show_type()

# Output:
# The transport is moving.
# The car is being driven.
# The battery is charging.
# This is an electric car.

# Explanation:
# 1. Car inherits from Transport.
# 2. ElectricCar inherits from both Car and ElectricFeature.
# 3. The Transport -> Car -> ElectricCar chain demonstrates
#    multilevel inheritance.
# 4. ElectricCar(Car, ElectricFeature) demonstrates
#    multiple inheritance.
#
# Combining these patterns creates hybrid inheritance.
#
# Simplified structure:
#
# Transport       ElectricFeature
#     |                 |
#    Car                |
#       \              /
#         ElectricCar


# Another example

# Imagine a game in which a Warrior can attack, a Mage can cast
# spells, and a Spellblade combines both abilities.


class Character:
    def introduce(self):
        print("I am a game character.")


class Warrior(Character):
    def attack(self):
        print("The warrior attacks with a sword.")


class Mage(Character):
    def cast_spell(self):
        print("The mage casts a magic spell.")


class Spellblade(Warrior, Mage):
    def use_combo(self):
        print("The spellblade combines sword and magic.")


hero = Spellblade()

hero.introduce()
hero.attack()
hero.cast_spell()
hero.use_combo()

print([cls.__name__ for cls in Spellblade.mro()])


# Output:
# I am a game character.
# The warrior attacks with a sword.
# The mage casts a magic spell.
# The spellblade combines sword and magic.
# ['Spellblade', 'Warrior', 'Mage', 'Character', 'object']


# Explanation

# This is hybrid inheritance because it combines two inheritance patterns:
# - Hierarchical inheritance: Warrior and Mage both inherit from Character.
# - Multiple inheritance: Spellblade inherits directly from both Warrior and Mage.
# The MRO shows how Python searches the classes for a method. Here, Spellblade
# comes first, followed by Warrior, Mage, Character, and finally object.




# ============================================================
# 21.2.8.6 - Comparison of Inheritance Types
# ============================================================

# Single Inheritance:
# One child class inherits directly from one parent class.
#
# Multiple Inheritance:
# One child class inherits directly from multiple parent classes.
#
# Multilevel Inheritance:
# Classes form an inheritance chain.
#
# Hierarchical Inheritance:
# Multiple child classes share one parent class.
#
# Hybrid Inheritance:
# Two or more inheritance patterns are combined in one hierarchy.


# ============================================================
# 21.2.8.7 - Summary
# ============================================================

# 1. Inheritance promotes code reusability.
#
# 2. A child class can use accessible inherited methods
#    and can define additional methods of its own.
#
# 3. Single and multiple inheritance describe how many
#    parent classes a child class directly inherits from.
#
# 4. Multilevel and hierarchical inheritance describe
#    different class-hierarchy structures.
#
# 5. Hybrid inheritance combines multiple inheritance patterns.
#
# 6. Python supports multiple inheritance and uses the
#    Method Resolution Order (MRO) to resolve method lookup.



# ============================================================
# 21.2.9 - Practical Inheritance Examples and Exercises
# ============================================================

# This section combines the inheritance concepts studied so far:
#
# 1. Inheriting attributes and methods
# 2. Single and multilevel inheritance
# 3. Multiple inheritance
# 4. Using super() in constructors
# 5. Method overriding
# 6. Using super() in an overridden method


# ============================================================
# 21.2.9.1 - Inheriting Attributes and Methods
# ============================================================

# A child class can inherit an initializer and methods
# from its parent class without defining them again.


class LibraryItem:
    def __init__(self, title):
        self.title = title

    def display_info(self):
        print(f"Book title: {self.title}")


class Book(LibraryItem):
    def read(self):
        print(f"Reading: {self.title}")


book1 = Book("Python Basics")

book1.display_info()
book1.read()

# Output:
# Book title: Python Basics
# Reading: Python Basics

# Explanation:
# Book inherits __init__() and display_info() from LibraryItem.
# Book defines its own read() method.
#
# Since Book does not define __init__(), Python uses the
# inherited initializer to initialize the title attribute.


# ============================================================
# 21.2.9.2 - Multilevel Inheritance and super()
# ============================================================

# Multilevel inheritance forms a chain of classes.
# super() allows each child initializer to reuse the next
# initializer in the Method Resolution Order (MRO).


class Wallet:
    def __init__(self, owner):
        self.owner = owner


class SavingsWallet(Wallet):
    def __init__(self, owner, balance):
        super().__init__(owner)
        self.balance = balance


class RewardsWallet(SavingsWallet):
    def __init__(self, owner, balance, reward_rate):
        super().__init__(owner, balance)
        self.reward_rate = reward_rate

    def display_details(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance}")
        print(f"Reward rate: {self.reward_rate}%")


wallet1 = RewardsWallet("John Smith", 1200, 5)

wallet1.display_details()

# Output:
# Owner: John Smith
# Balance: $1200
# Reward rate: 5%

# Explanation:
# Wallet initializes the owner attribute.
# SavingsWallet initializes the balance attribute.
# RewardsWallet initializes the reward_rate attribute.
#
# Each initializer uses super() to call the next initializer.
# All three attributes belong to the same RewardsWallet instance.
#
# Inheritance chain:
#
# Wallet
#    |
# SavingsWallet
#    |
# RewardsWallet


# ============================================================
# 21.2.9.3 - Multiple Inheritance
# ============================================================

# A child class can inherit methods from more than one
# parent class.


class MusicPlayer:
    def play_music(self):
        print("Playing music.")


class VoiceAssistant:
    def respond(self):
        print("The voice assistant is responding.")


class SmartSpeaker(MusicPlayer, VoiceAssistant):
    def connect(self):
        print("The smart speaker is connected.")


speaker1 = SmartSpeaker()

speaker1.play_music()
speaker1.respond()
speaker1.connect()

# Output:
# Playing music.
# The voice assistant is responding.
# The smart speaker is connected.

# Explanation:
# SmartSpeaker inherits from MusicPlayer and VoiceAssistant.
# It can use methods from both parent classes and define
# additional methods of its own.


# Display the Method Resolution Order (MRO).

print([cls.__name__ for cls in SmartSpeaker.mro()])

# Output:
# ['SmartSpeaker', 'MusicPlayer', 'VoiceAssistant', 'object']

# Explanation:
# Python follows the MRO when searching for methods.
# If multiple parent classes define the same method,
# the MRO determines which implementation is found first.


# ============================================================
# 21.2.9.4 - Method Overriding and super()
# ============================================================

# A child class can override a parent method and use super()
# to reuse the parent's implementation.


class DeliveryService:
    def show_details(self):
        print("Service: Parcel delivery.")


class ExpressDelivery(DeliveryService):
    def show_details(self):
        super().show_details()
        print("Speed: Express delivery in 1-2 business days.")


delivery1 = ExpressDelivery()
delivery1.show_details()

# Output:
# Service: Parcel delivery.
# Speed: Express delivery in 1-2 business days.

# Explanation:
# ExpressDelivery overrides show_details().
#
# super().show_details() calls the next implementation in
# the MRO, which is DeliveryService.show_details() here.
#
# After the parent method finishes, the child method
# prints its additional information.
#
# Without the super() call, only the child's message
# would be printed by this implementation.

# ============================================================
# 21.2.9.6 - Summary
# ============================================================

# 1. A child class can inherit attributes and methods from
#    its parent class.
#
# 2. If a child class does not define __init__(), it can
#    use an inherited initializer.
#
# 3. super() can reuse initialization and other methods
#    in the inheritance hierarchy.
#
# 4. Multiple inheritance allows a child class to inherit
#    from multiple parent classes.
#
# 5. Method overriding lets a child class customize an
#    inherited method.
#
# 6. MRO determines the order in which Python searches
#    classes for methods.