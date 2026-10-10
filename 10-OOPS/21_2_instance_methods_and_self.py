
# ============================================================
# Topic 21.2 - Instance Methods and the self Parameter
# ============================================================


# ============================================================
# 21.2.1 What Is an Instance Method?
# ============================================================

# An instance method is a function defined inside a class that
# operates on a particular instance (object) of that class.
#
# Instance methods are commonly used to perform actions using
# an object's attributes or to modify its state.


class Student:
    def study(self):
        print("The student is studying.")


student1 = Student()
student1.study()

# Output:
# The student is studying.


# ------------------------------------------------------------
# 21.2.2 Instance Methods Accessing Object Attributes
# ------------------------------------------------------------

# An instance method can access an object's attributes through
# self and use their values to perform an action.


class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


student1 = Student("John Smith")
student2 = Student("Alice")

student1.introduce()
student2.introduce()

# Output:
# My name is John Smith.
# My name is Alice.


# ------------------------------------------------------------
# 21.2.3 Instance Methods Modifying Object Attributes
# ------------------------------------------------------------

# An instance method can modify an object's attributes.
# Changing an attribute changes the object's state.


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount


account1 = BankAccount("John Smith", 1000)

print(account1.balance)

account1.deposit(500)

print(account1.balance)

# Output:
# 1000
# 1500


# How deposit() works:
# 1. self refers to account1.
# 2. amount receives the value 500.
# 3. self.balance accesses the current balance (1000).
# 4. The amount is added to the current balance.
# 5. The result (1500) is assigned to self.balance.


# ============================================================
# 21.2.4 How the self Parameter Works
# ============================================================

# self refers to the particular instance on which an instance
# method is called.
#
# Python automatically passes the instance as the first
# argument when an instance method is called through an object.


class Student:
    def introduce(self):
        print(f"My name is {self.name}.")


student1 = Student()
student2 = Student()

student1.name = "John Smith"
student2.name = "Alice"

student1.introduce()
student2.introduce()

# Output:
# My name is John Smith.
# My name is Alice.


# When we call:
# student1.introduce()
#
# Python effectively calls:
# Student.introduce(student1)
#
# Therefore, inside the method, self refers to student1.
# self.name accesses student1.name.
#
# When we call student2.introduce(), self refers to student2.


# ------------------------------------------------------------
# 21.2.5 self Is Not a Python Keyword
# ------------------------------------------------------------

# self is not a Python keyword. It is the conventional name
# for the first parameter of an instance method.
#
# Although another name technically works, using self is the
# standard Python convention.


class Example:
    def show(this):
        print("Hello!")


example1 = Example()
example1.show()

# Output:
# Hello!

# ============================================================
# Example
# ============================================================
class Mobile:
    def __init__(self, brand, model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print (f"This is {self.brand}")
        print(f"Its model is {self.model}")
        print(f"{self.brand} {self.model} will cost you {self.price}")

iphone = Mobile("iphne" , "18 Pro Max", "1500$")
print (iphone.brand)
print (iphone.model)
print(iphone.price)
iphone.display_info()
print ("====================================")
samsung = Mobile ("Samsung" , "S24" ,"1000$")
print(samsung.brand)
print(samsung.model)
print(samsung.price)
samsung.display_info()





# ============================================================
# Summary
# ============================================================

# 1. An instance method is defined inside a class and operates
#    on a particular instance.
#
# 2. Instance methods can access attributes and modify an
#    object's state.
#
# 3. self refers to the instance on which the method is called.
#
# 4. Python automatically passes the instance when a method
#    is called through an object.
#
# 5. self is a convention, not a Python keyword.
#
# 6. When calling a method through an object, we do not
#    normally pass self explicitly.