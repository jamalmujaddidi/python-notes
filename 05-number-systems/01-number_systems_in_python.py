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



# ------------------------------------------------------------
# 2.1 BINARY TO DECIMAL
# ------------------------------------------------------------

"""
Binary is base 2.

Each position represents a power of 2.

Example:

    Binary: 1010

    Position values:  8    4    2    1
    Powers:           2^3  2^2  2^1  2^0
    Binary digits:     1    0    1    0

    Calculation:

    1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0

    = 8 + 0 + 2 + 0
    = 10

Therefore:

    1010 (Binary) = 10 (Decimal)
"""

binary_number = int("1010", 2)

print("\nBinary to Decimal:")
print(binary_number)

# Output:
# Binary to Decimal:
# 10



# ------------------------------------------------------------
# 2.2 OCTAL TO DECIMAL
# ------------------------------------------------------------

"""
Octal is base 8.

Each position represents a power of 8.

Example 1:

    x = int("17", 8)

    Calculation:

    1 * 8^1 + 7 * 8^0

    = 8 + 7
    = 15

Therefore:

    17 (Octal) = 15 (Decimal)
"""

octal_number = int("17", 8)

print("\nOctal to Decimal:")
print(octal_number)

# Output:
# Octal to Decimal:
# 15


"""
Example 2:

    x = int("2457", 8)

    Calculation:

    2 * 8^3 + 4 * 8^2 + 5 * 8^1 + 7 * 8^0

    = 1024 + 256 + 40 + 7
    = 1327

Therefore:

    2457 (Octal) = 1327 (Decimal)
"""

octal_number = int("2457", 8)

print("\nAnother Octal to Decimal Example:")
print(octal_number)

# Output:
# Another Octal to Decimal Example:
# 1327