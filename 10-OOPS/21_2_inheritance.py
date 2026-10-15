

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


# another Example--> -->

class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am also a student.")


student1 = Student()
student1.introduce()

# Output:
# I am a person.
# I am also a student.

'''
Here, Student overrides the inherited introduce() method but uses super().
introduce() to call the parent implementation before executing its own 
additional statement.
This is useful when a child class wants to reuse the parent's behavior 
and extend it rather than replace it completely.

'''
