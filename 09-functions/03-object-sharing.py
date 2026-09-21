# Object Sharing in Python


# Example 1 — Immutable Object: Same Object

def show(a):
    print(f"Value of a inside function: {a}")
    print(f"ID of a inside function: {id(a)}")


x = 10

print("Value of x in main:", x)
print("ID of x in main:", id(x))

show(x)


# Example 2 — Immutable Object: Rebinding

def change(a):
    print(f"\nValue of a before operation: {a}")
    print(f"ID of a before operation: {id(a)}")

    a = a + 20

    print(f"Value of a after operation: {a}")
    print(f"ID of a after operation: {id(a)}")


x = 10

print("\nValue of x before function call:", x)
print("ID of x before function call:", id(x))

change(x)

print("Value of x after function call:", x)
print("ID of x after function call:", id(x))


# Example 3 — Mutable Object: Modification in Place

def modify(a):
    print(f"\nValue of a before modification: {a}")
    print(f"ID of a before modification: {id(a)}")

    a.append(40)

    print(f"Value of a after modification: {a}")
    print(f"ID of a after modification: {id(a)}")


numbers = [10, 20, 30]

print("\nValue of numbers before function call:", numbers)
print("ID of numbers before function call:", id(numbers))

modify(numbers)

print("Value of numbers after function call:", numbers)
print("ID of numbers after function call:", id(numbers))