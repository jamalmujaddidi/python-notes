'''
Generators in Python:

A generator function is a special type of function that produces values one at a time,
on demand,instead of creating and storing all the values in memory at once.

A function containing the yield keyword is called a generator function.
 When called, it returns a generator object, which is an iterator.
'''

# simple Example

# A normal function could create a list:
def get_numbers ():
    return [1, 2, 3, 4, 5]

numbers = get_numbers ()

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# Generator function example

# We can use yield instead:

def get_numbers():
    yield 1
    yield 2
    yield 3


numbers = get_numbers()

# doesn't create a list containing all five values.
# Instead, numbers is a generator object.
# Values can then be requested one at a time:

print(next(numbers))
print(next(numbers))
print(next(numbers))
# ________________________________________
# Output:
# 1
# 2
# 3

# another usful example
def test ():
    number = 10
    yield number

    number += 5
    yield number
    return
generator = test()
print(next(generator))
print (next(generator))
