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



# ------------------------------------------------------------
# 2.3 HEXADECIMAL TO DECIMAL
# ------------------------------------------------------------

"""
Hexadecimal is base 16.

It uses digits 0-9 and letters A-F.

Remember:

    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15

Example 1:

    x = int("1F", 16)

    Calculation:

    1 * 16^1 + 15 * 16^0

    = 16 + 15
    = 31

Therefore:

    1F (Hexadecimal) = 31 (Decimal)
"""

hex_number = int("1F", 16)

print("\nHexadecimal to Decimal:")
print(hex_number)

# Output:
# Hexadecimal to Decimal:
# 31


"""
Example 2:

    x = int("2A3F7", 16)

    Remember:
    A = 10
    F = 15

    Calculation:

    2 * 16^4 + 10 * 16^3 + 3 * 16^2
    + 15 * 16^1 + 7 * 16^0

    = 131072 + 40960 + 768 + 240 + 7
    = 173047

Therefore:

    2A3F7 (Hexadecimal) = 173047 (Decimal)
"""

hex_number = int("2A3F7", 16)

print("\nAnother Hexadecimal to Decimal Example:")
print(hex_number)

# Output:
# Another Hexadecimal to Decimal Example:
# 173047



# ============================================================
# 3. DECIMAL TO NON-DECIMAL CONVERSION
# ============================================================

"""
Python provides three built-in functions to convert
decimal integers into other number systems.

Function    Conversion             Example       Result
----------------------------------------------------------
bin()       Decimal to Binary      bin(10)       0b1010
oct()       Decimal to Octal       oct(15)       0o17
hex()       Decimal to Hexadecimal hex(31)       0x1f

The prefixes indicate the number system:

Prefix    Number System    Base
--------------------------------
0b        Binary             2
0o        Octal              8
0x        Hexadecimal       16

Important:

These functions return strings containing the converted
number and its corresponding prefix.
"""

print("\n3. DECIMAL TO NON-DECIMAL CONVERSION")

print(bin(25))
print(oct(83))
print(hex(439))

# Output:
# 0b11001
# 0o123
# 0x1b7



# ------------------------------------------------------------
# 3.1 DECIMAL TO BINARY
# ------------------------------------------------------------

"""
Binary is base 2.

To convert decimal into binary manually:

1. Divide the decimal number by 2.
2. Record the remainder.
3. Divide the quotient by 2 again.
4. Continue until the quotient becomes 0.
5. Read the remainders from bottom to top.

Example: Convert 25 to Binary.

Division       Quotient       Remainder
----------------------------------------
25 / 2             12              1
12 / 2              6              0
6 / 2               3              0
3 / 2               1              1
1 / 2               0              1

Read the remainders from bottom to top:

    11001

Therefore:

    25 (Decimal) = 11001 (Binary)

Python:

    bin(25)
"""

binary_number = bin(25)

print("\nDecimal to Binary:")
print(binary_number)

# Output:
# Decimal to Binary:
# 0b11001



# ------------------------------------------------------------
# 3.2 DECIMAL TO OCTAL
# ------------------------------------------------------------

"""
Octal is base 8.

To convert decimal into octal manually, repeatedly divide
the decimal number by 8 and record the remainders.

Example: Convert 83 to Octal.

Division       Quotient       Remainder
----------------------------------------
83 / 8             10              3
10 / 8              1              2
1 / 8               0              1

Read the remainders from bottom to top:

    123

Therefore:

    83 (Decimal) = 123 (Octal)

Python:

    oct(83)
"""

octal_number = oct(83)

print("\nDecimal to Octal:")
print(octal_number)

# Output:
# Decimal to Octal:
# 0o123



# ------------------------------------------------------------
# 3.3 DECIMAL TO HEXADECIMAL
# ------------------------------------------------------------

"""
Hexadecimal is base 16.

To convert decimal into hexadecimal manually, repeatedly
divide the decimal number by 16 and record the remainders.

Example: Convert 439 to Hexadecimal.

Division       Quotient       Remainder
----------------------------------------
439 / 16           27              7
27 / 16             1              11 = B
1 / 16              0              1

Read the remainders from bottom to top:

    1B7

Therefore:

    439 (Decimal) = 1B7 (Hexadecimal)

Python:

    hex(439)

Note: Python's hex() function displays hexadecimal letters
in lowercase by default.
"""

hex_number = hex(439)

print("\nDecimal to Hexadecimal:")
print(hex_number)

# Output:
# Decimal to Hexadecimal:
# 0x1b7


"""
Main Rule:

When converting decimal to another base:

    1. Divide the decimal number by the target base.
    2. Record the remainder.
    3. Divide again.
    4. Continue until the quotient becomes 0.
    5. Read the remainders from bottom to top.

Decimal to Binary       -> Divide by 2
Decimal to Octal        -> Divide by 8
Decimal to Hexadecimal  -> Divide by 16
"""



# ============================================================
# 4. BINARY TO OCTAL AND HEXADECIMAL
# ============================================================

"""
Binary can be converted directly into octal or hexadecimal
by grouping its digits.

Binary to Octal:

    Group binary digits into sets of 3, starting from the right.

    Reason:
    8 = 2^3

Binary to Hexadecimal:

    Group binary digits into sets of 4, starting from the right.

    Reason:
    16 = 2^4

Important:

If the leftmost group contains fewer than 3 or 4 digits,
add leading zeros to complete that group.
"""


# ------------------------------------------------------------
# 4.1 BINARY TO OCTAL
# ------------------------------------------------------------

"""
Example:

    Convert 10110110 (Binary) to Octal.

Step 1: Group into sets of 3, starting from the right.

    10110110
    010 110 110

Step 2: Convert each group into its octal equivalent.

    Binary Group       Octal Value
    --------------------------------
       010                  2
       110                  6
       110                  6

Step 3: Combine the octal digits.

    266

Therefore:

    10110110 (Binary) = 266 (Octal)

Python:

    oct(int("10110110", 2))

First int() converts the binary string into a decimal integer.
Then oct() converts that integer into an octal representation.
"""

binary_number = "10110110"
octal_number = oct(int(binary_number, 2))

print("\nBinary to Octal:")
print(octal_number)

# Output:
# Binary to Octal:
# 0o266



# ------------------------------------------------------------
# 4.2 BINARY TO HEXADECIMAL
# ------------------------------------------------------------

"""
Example:

    Convert 10110110 (Binary) to Hexadecimal.

Step 1: Group binary digits into sets of 4.

    10110110
    1011 0110

Step 2: Convert each group into its hexadecimal equivalent.

    Binary Group       Hexadecimal Value
    -------------------------------------
       1011                    B
       0110                    6

Step 3: Combine the hexadecimal digits.

    B6

Therefore:

    10110110 (Binary) = B6 (Hexadecimal)

Python:

    hex(int("10110110", 2))
"""

binary_number = "10110110"
hex_number = hex(int(binary_number, 2))

print("\nBinary to Hexadecimal:")
print(hex_number)

# Output:
# Binary to Hexadecimal:
# 0xb6