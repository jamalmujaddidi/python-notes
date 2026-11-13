"""
NUMBER SYSTEM CONVERSIONS IN PYTHON

This file covers conversions between:
1. Binary (Base 2)
2. Octal (Base 8)
3. Decimal (Base 10)
4. Hexadecimal (Base 16)

Topics:
1. Introduction to Number Systems
2. Non-Decimal to Decimal Conversion
3. Decimal to Non-Decimal Conversion
4. Binary to Octal and Hexadecimal
5. Octal to Binary and Hexadecimal
6. Hexadecimal to Binary and Octal
7. Python Built-in Conversion Functions
"""


# ============================================================
# 1. INTRODUCTION TO NUMBER SYSTEMS
# ============================================================

"""
An integer can be represented in different number systems.

Number System    Base    Digits Used
-------------------------------------
Binary            2       0, 1
Octal             8       0 - 7
Decimal          10       0 - 9
Hexadecimal      16       0 - 9, A - F

Hexadecimal digit values:

Hexadecimal    Decimal
----------------------
    A             10
    B             11
    C             12
    D             13
    E             14
    F             15

Each position in a number represents a power of its base.
"""



# ============================================================
# 2. NON-DECIMAL TO DECIMAL CONVERSION
# ============================================================

"""
Python provides the int() function to convert a number
represented as a string in another base into a decimal integer.

Syntax:

    int("number", base)

The first argument is the number represented as a string.
The second argument specifies the base of that number.

Examples:

    int("1010", 2)     # Binary to Decimal
    int("1010", 8)     # Octal to Decimal
    int("1010", 10)    # Decimal to Decimal
    int("1010", 16)    # Hexadecimal to Decimal
"""

print("\n2. NON-DECIMAL TO DECIMAL CONVERSION")

binary_to_decimal = int("1010", 2)
octal_to_decimal = int("1010", 8)
decimal_to_decimal = int("1010", 10)
hex_to_decimal = int("1010", 16)

print(binary_to_decimal)
print(octal_to_decimal)
print(decimal_to_decimal)
print(hex_to_decimal)

# Output:
# 10
# 520
# 1010
# 4112