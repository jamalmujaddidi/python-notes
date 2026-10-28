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


