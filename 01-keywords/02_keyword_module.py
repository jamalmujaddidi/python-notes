
"""
TOPIC: PYTHON KEYWORD MODULE
============================

1. Introduction
---------------

The keyword module is a built-in Python module that provides
tools for working with Python keywords.

It allows us to:
    - Retrieve the list of reserved keywords.
    - Check whether a string is a reserved keyword.
    - Retrieve and check soft keywords.

Importing the module:

    import keyword


2. The kwlist Attribute
-----------------------

Definition:
    kwlist is an attribute of the keyword module that contains
    a list of Python's reserved keywords.

Syntax:
    keyword.kwlist

Example:
"""

import keyword

print(keyword.kwlist)
# Output: A list of Python's reserved keywords.
# The exact list depends on the Python version.


# ------------------------------------------------------------
# 3. Counting the Reserved Keywords
# ------------------------------------------------------------

# len() returns the number of elements in the keyword list.

print(len(keyword.kwlist))
# Output: The number of reserved keywords in the current
# Python version.


# ------------------------------------------------------------
# 4. The iskeyword() Function
# ------------------------------------------------------------

# Definition:
# iskeyword() checks whether a given string is a reserved
# Python keyword.
#
# Syntax:
# keyword.iskeyword(string)


# Example 1: Checking a reserved keyword

print(keyword.iskeyword("if"))
# Output: True


# Example 2: Checking a non-keyword

print(keyword.iskeyword("hello"))
# Output: False


# Example 3: Checking another reserved keyword

print(keyword.iskeyword("lambda"))
# Output: True


# ------------------------------------------------------------
# 5. The softkwlist Attribute
# ------------------------------------------------------------

# Definition:
# softkwlist is an attribute that contains the list of
# soft keywords recognized by the current Python version.
#
# Soft keywords have special meaning only in specific
# syntactic contexts and can be used as identifiers elsewhere.
#
# Syntax:
# keyword.softkwlist


print(keyword.softkwlist)
# Output: A list of soft keywords in the current Python version.


# ------------------------------------------------------------
# 6. The issoftkeyword() Function
# ------------------------------------------------------------

# Definition:
# issoftkeyword() checks whether a given string is a
# soft keyword in the current Python version.
#
# Syntax:
# keyword.issoftkeyword(string)


# Example 1: Checking a soft keyword

print(keyword.issoftkeyword("match"))
# Output: True in Python versions where match is a soft keyword.


# Example 2: Checking an ordinary identifier

print(keyword.issoftkeyword("hello"))
# Output: False


# ------------------------------------------------------------
# 7. Summary
# ------------------------------------------------------------

# keyword.kwlist:
#     Returns the list of reserved keywords.
#
# keyword.iskeyword():
#     Checks whether a string is a reserved keyword.
#
# keyword.softkwlist:
#     Returns the list of soft keywords.
#
# keyword.issoftkeyword():
#     Checks whether a string is a soft keyword.
#
# Note:
#     The available keywords depend on the Python version.