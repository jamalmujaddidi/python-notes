# Parameters and Arguments
from doctest import Example
# ======================================================================


# Example
def greet(name):
    print(f"Hello Mr, {name}.")


greet("John")
# ======================================================================
# Output
# Hello Mr, John.
# ======================================================================


# Example
def test (x,y):
    print(x + y)
    print (x * y)
    print (x - y)
    print (x // y)


test (60 , 40)
# ======================================================================
# output
# 100
# 2400
# 20
# 1
# ======================================================================



# Keyword Arguments
# ======================================================================
# First Example
# ======================================================================
def name (first_name , last_name ):
    return f"My full name is {first_name} {last_name}"


full_name = name (first_name= "Jhon", last_name= "Smith" )
print(full_name)
# ======================================================================
# output
# My full name is Jhon Smith
# ======================================================================


#Second Example
def introduce(name, age):
    print(f"This is {name} and he is {age} years old.")


introduce(name="John", age=26)
# =====================================================================
# output
# This is John and he is 26 years old.
# =====================================================================