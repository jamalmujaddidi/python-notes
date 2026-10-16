

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


# practical Examples

class Animal:
    def display(self):
        print("This is an animal")

class Dog(Animal):
    def display(self):
        print("This is a dog")

obj = Dog()
obj.display()

# Output
# This is a dog




# practical 2


class Employee:
    def __init__(self):
        self.role = "Employee"

    def display(self):
        print("Role:", self.role)

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.role = "Manager"

    def display(self):
        print("Role:", self.role)

e1 = Employee()
e2 = Manager()
e1.display()
e2.display()

# Output
# Role: Employee
# Role: Manager


# another Example:
class Animal ():
    def sound (self):
        print("all animals makes sound")

class Dog(Animal):
    def sound(self):
        print ("Dogs always Barks")

class Cat (Animal):
    def sound(self):
        print("Cats always do meow meow")

dog = Dog ()
dog.sound()
a = Animal()
a.sound()
