# 11. Scope of Variables
# 11.1 Local Scope


# Example 1: Local variable

def sub():
    interest = "I Love Python"
    print(interest)


sub()

# Output:
# I Love Python


# Example 2: Trying to access a local variable outside its function

def test():
    x = 20
    print(x)


test()

# Output:
# 20

# If we uncomment the following line:
# print(x)

# Output:
# NameError: name 'x' is not defined


# Example 3: Local and global variables can have the same name

x = 100


def example():
    x = 20
    print(x)


example()
print(x)

# Output:
# 20
# 100