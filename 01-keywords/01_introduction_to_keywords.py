
"""
PYTHON KEYWORDS
===============

1. Definition
-------------

Keywords are reserved words in Python that have special
meanings and purposes in the language's syntax.

They are used to define the structure and behavior of
Python programs.

2. Important Characteristics
----------------------------

- Keywords have predefined meanings in Python.
- They are part of Python's syntax.
- Keywords cannot be used as ordinary identifiers,
  such as variable names or function names.
- Python keywords are case-sensitive.

3. Examples of Python Keywords
------------------------------

if, else, elif, for, while, def, class, return,
import, from, True, False, None, lambda, and, or, not

4. Keywords vs. Identifiers
---------------------------

Keywords:
    Reserved words with special meanings in Python.

Identifiers:
    Names given to variables, functions, classes,
    and other objects.

Example:

"""

# Valid identifier
name = "John Smith"
print(name)
# Output: John Smith

# Invalid: 'if' is a Python keyword
# if = 10
# SyntaxError

# Valid: 'if' used as a keyword in Python syntax
if True:
    print("This is valid syntax.")
# Output: This is valid syntax.