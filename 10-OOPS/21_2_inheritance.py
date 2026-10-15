

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



