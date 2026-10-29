"""
TOPIC: IDENTIFIERS IN PYTHON
============================

1. Definition
-------------

An identifier is a name used to identify a variable, function,
class, module, or other named entity in Python.

Identifiers allow us to refer to objects and access them by name
instead of working directly with their memory locations.

Example:
"""

name = "John Smith"
age = 25

print(name)
print(age)

# Output:
# John Smith
# 25


# ------------------------------------------------------------
# 2. Why Do We Need Identifiers?
# ------------------------------------------------------------

# Identifiers give meaningful names to objects and make programs
# easier to read, understand, and maintain.

student_name = "John Smith"
student_age = 25

print(student_name)
print(student_age)

# Output:
# John Smith
# 25


# ------------------------------------------------------------
# 3. Rules for Naming Identifiers
# ------------------------------------------------------------

# Rule 1:
# Identifiers can contain letters, digits, and underscores (_).
#
# Valid examples:
# student
# student_name
# student1
# _age
#
# Invalid examples:
# student-name
# student@name
# student#1


# Rule 2:
# An identifier cannot start with a digit.
#
# Valid:
age1 = 20

# Invalid:
# 1age = 20
# SyntaxError


# Rule 3:
# Identifiers cannot contain spaces.
#
# Valid:
student_name = "John Smith"

# Invalid:
# student name = "John Smith"
# SyntaxError


# Rule 4:
# Reserved Python keywords cannot be used as identifiers.
#
# Invalid:
# class = 5
# if = 10
# SyntaxError


# Rule 5:
# Identifiers are case-sensitive.

name = "John"
Name = "Smith"
NAME = "Alex"

print(name)
print(Name)
print(NAME)

# Output:
# John
# Smith
# Alex

# name, Name, and NAME are three different identifiers.


# ------------------------------------------------------------
# 4. Valid and Invalid Identifiers
# ------------------------------------------------------------

# Valid identifiers:
student_name = "John Smith"
student1 = "Alex"
_age = 25
price = 19.99
myVariable = 100
EmployeeSalary = 50000

# These are valid identifiers, although naming conventions
# recommend different styles for different purposes.


# Invalid identifiers:
#
# 1name       -> Starts with a digit
# student-name -> Contains a hyphen
# student name -> Contains a space
# @name       -> Contains an invalid character
# class       -> A reserved Python keyword


# ------------------------------------------------------------
# 5. Identifiers vs. Python Keywords
# ------------------------------------------------------------

# Identifiers are names used in a program.
#
# Keywords are reserved words with special meanings in Python.
#
# A keyword cannot be used as an ordinary identifier.

import keyword

print(keyword.iskeyword("class"))
print(keyword.iskeyword("student_name"))

# Output:
# True
# False

# Note:
# A name may have a valid identifier spelling but still be
# prohibited as an ordinary identifier because it is a keyword.


# ------------------------------------------------------------
# 6. Checking Identifier Validity
# ------------------------------------------------------------

# The str.isidentifier() method checks whether a string has
# valid Python identifier syntax.
#
# Syntax:
# string.isidentifier()


print("student_name".isidentifier())
print("student1".isidentifier())
print("_age".isidentifier())
print("1student".isidentifier())
print("student-name".isidentifier())
print("student name".isidentifier())
print("class".isidentifier())

# Output:
# True
# True
# True
# False
# False
# False
# True

# Important:
# isidentifier() checks identifier syntax, not whether the
# string is a reserved keyword.
#
# Therefore, "class".isidentifier() returns True, even though
# class cannot be used as an ordinary identifier.
#
# Use keyword.iskeyword() when you also need to check whether
# a name is a reserved Python keyword.

# ------------------------------------------------------------
# 7. Naming Conventions (PEP 8)
# ------------------------------------------------------------

# PEP 8 stands for Python Enhancement Proposal 8.
#
# It is the widely used Python style guide.
#
# Naming conventions are recommendations, not generally
# mandatory syntax rules.


# Variables: snake_case
student_name = "John Smith"
total_price = 100


# Functions: snake_case
def calculate_total(price, quantity):
    return price * quantity


print(calculate_total(10, 3))

# Output:
# 30


# Classes: CapWords (also called PascalCase)
class StudentRecord:
    pass


student = StudentRecord()

print(type(student).__name__)

# Output:
# StudentRecord


# Constants: UPPER_CASE
MAX_SIZE = 100
PI = 3.14159

print(MAX_SIZE)
print(PI)

# Output:
# 100
# 3.14159

# Note:
# Python does not enforce constants through uppercase names.
# UPPER_CASE is a naming convention indicating that a value
# is intended to remain constant.


# ------------------------------------------------------------
# 8. Best Practices for Naming Identifiers
# ------------------------------------------------------------

# Use meaningful names that describe the purpose of a value.

# Good:
employee_salary = 50000
total_price = 250
student_name = "John Smith"


# Less descriptive:
# x = 50000
# a = 250
# n = "John Smith"


# Avoid using names that hide Python built-ins.

# Avoid:
# list = [1, 2, 3]
# str = "Hello"
# int = 10
# sum = 100

# These assignments are allowed, but they hide the built-in
# names within the current scope and can cause confusion.


# ------------------------------------------------------------
# 9. Understanding Underscores in Identifiers
# ------------------------------------------------------------

# A single leading underscore is a convention indicating
# that a name is intended for internal use.

_internal_value = 10


# Double leading underscores in class attributes can trigger
# name mangling. This helps avoid certain naming conflicts
# in subclasses; it does not make an attribute truly private.

# Names such as __init__ are special method names defined
# by Python and are often called dunder (double-underscore)
# methods.


# ------------------------------------------------------------
# 10. Identifier vs. Object
# ------------------------------------------------------------

# An identifier is a name; an object is the entity to which
# that name refers.

first_name = "John Smith"
second_name = first_name

first_name = "Alex"

print(first_name)
print(second_name)

# Output:
# Alex
# John Smith

# Explanation:
# Initially, both names refer to the same string object.
# Reassigning first_name makes it refer to a different string.
# second_name still refers to the original string object.
#
# An object can have multiple names referring to it, and
# a name can be reassigned to refer to another object.


# ------------------------------------------------------------
# 11. Summary
# ------------------------------------------------------------

# 1. Identifiers are names used for variables, functions,
#    classes, modules, and other named entities.
#
# 2. Identifiers can contain letters, digits, and underscores.
#
# 3. An identifier cannot start with a digit.
#
# 4. Identifiers cannot contain spaces or hyphens.
#
# 5. Reserved Python keywords cannot be used as ordinary names.
#
# 6. Identifiers are case-sensitive.
#
# 7. str.isidentifier() checks identifier syntax.
#
# 8. keyword.iskeyword() checks reserved Python keywords.
#
# 9. PEP 8 recommends snake_case for variables and functions,
#    CapWords for classes, and UPPER_CASE for constants.
#
# 10. Avoid shadowing Python built-ins with your own names.
#
# 11. An identifier is a name, while an object is the entity
#     to which that name refers.
