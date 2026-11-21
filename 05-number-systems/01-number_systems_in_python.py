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


# ============================================================
# 5. OCTAL TO BINARY AND HEXADECIMAL
# ============================================================


# ------------------------------------------------------------
# 5.1 OCTAL TO BINARY
# ------------------------------------------------------------

"""
Octal is base 8.

Since:

    8 = 2^3

Each octal digit is represented by exactly 3 binary digits.

Octal to Binary Reference Table:

Octal       Binary
------------------
  0          000
  1          001
  2          010
  3          011
  4          100
  5          101
  6          110
  7          111

The Rule:

Replace each octal digit with its 3-bit binary equivalent.

Example 1:

    (527)₈

    5 -> 101
    2 -> 010
    7 -> 111

    Combine:

    101 010 111

    Therefore:

    (527)₈ = (101010111)₂

Example 2:

    (5)₈ = (101)₂

Example 3:

    (27)₈

    2 -> 010
    7 -> 111

    Combine:

    010111

    Remove the unnecessary leading zero:

    (27)₈ = (10111)₂

Example 4:

    (436)₈

    4 -> 100
    3 -> 011
    6 -> 110

    Combine:

    100011110

    Therefore:

    (436)₈ = (100011110)₂
"""

octal_number = bin(int("527", 8))
print("\nOctal to Binary:")
print(octal_number)

octal_number = bin(int("5", 8))
print(octal_number)

octal_number = bin(int("27", 8))
print(octal_number)

octal_number = bin(int("436", 8))
print(octal_number)

# Output:
# Octal to Binary:
# 0b101010111
# 0b101
# 0b10111
# 0b100011110


# ------------------------------------------------------------
# 5.2 OCTAL TO HEXADECIMAL
# ------------------------------------------------------------

"""
To convert octal to hexadecimal:

    First convert Octal to Binary.
    Then convert Binary to Hexadecimal.

    Octal -> Binary -> Hexadecimal

Example 1:

    Convert (56)₈ to Hexadecimal.

Step 1: Octal to Binary

    5 -> 101
    6 -> 110

    Therefore:

    56₈ = 101110₂

Step 2: Group into sets of 4, starting from the right.

    101110
    10 1110

Step 3: Add leading zeros to complete the first group.

    0010 1110

Step 4: Convert each group to hexadecimal.

    0010 -> 2
    1110 -> E

Therefore:

    (56)₈ = (2E)₁₆


Example 2:

    Convert (347)₈ to Hexadecimal.

Step 1: Octal to Binary

    3 -> 011
    4 -> 100
    7 -> 111

    Therefore:

    347₈ = 011100111₂

Step 2: Group into sets of 4, starting from the right.

    011100111
    0 1110 0111

Step 3: Add leading zeros.

    0000 1110 0111

Step 4: Convert each group.

    0000 -> 0
    1110 -> E
    0111 -> 7

Ignore the unnecessary leading zero.

Therefore:

    (347)₈ = (E7)₁₆


Example 3:

    Convert (625)₈ to Hexadecimal.

Step 1: Octal to Binary

    6 -> 110
    2 -> 010
    5 -> 101

    Therefore:

    625₈ = 110010101₂

Step 2: Group into sets of 4.

    110010101
    1 1001 0101

Step 3: Add leading zeros.

    0001 1001 0101

Step 4: Convert each group.

    0001 -> 1
    1001 -> 9
    0101 -> 5

Therefore:

    (625)₈ = (195)₁₆

Python:

    hex(int("56", 8))
    hex(int("347", 8))
    hex(int("625", 8))
"""

print("\nOctal to Hexadecimal:")

print(hex(int("56", 8)))
print(hex(int("347", 8)))
print(hex(int("625", 8)))

# Output:
# Octal to Hexadecimal:
# 0x2e
# 0xe7
# 0x195


# ============================================================
# 6. HEXADECIMAL TO BINARY AND OCTAL
# ============================================================


# ------------------------------------------------------------
# 6.1 HEXADECIMAL TO BINARY
# ------------------------------------------------------------

"""
Hexadecimal is base 16.

Since:

    16 = 2^4

Each hexadecimal digit is represented by exactly 4 binary bits.

Hexadecimal to Binary Reference Table:

Hexadecimal       Binary
------------------------
     0             0000
     1             0001
     2             0010
     3             0011
     4             0100
     5             0101
     6             0110
     7             0111
     8             1000
     9             1001
     A             1010
     B             1011
     C             1100
     D             1101
     E             1110
     F             1111

The Rule:

Replace each hexadecimal digit with its 4-bit binary equivalent.

Example 1:

    Convert (A6)₁₆ to Binary.

    A -> 1010
    6 -> 0110

    Combine:

    10100110

    Therefore:

    (A6)₁₆ = (10100110)₂


Example 2:

    Convert (3F)₁₆ to Binary.

    3 -> 0011
    F -> 1111

    Combine:

    00111111

    Therefore:

    (3F)₁₆ = (00111111)₂


Example 3:

    Convert (5A)₁₆ to Binary.

    5 -> 0101
    A -> 1010

    Combine:

    01011010

     Therefore:

    (5A)₁₆ = (01011010)₂

Important:

When converting a hexadecimal number manually, each digit
must initially be represented using exactly 4 bits.

Python's bin() function removes unnecessary leading zeros
from the resulting binary representation.
"""

print("\nHexadecimal to Binary:")

print(bin(int("A6", 16)))
print(bin(int("3F", 16)))

# Output:
# Hexadecimal to Binary:
# 0b10100110
# 0b111111



# ------------------------------------------------------------
# 6.2 HEXADECIMAL TO OCTAL
# ------------------------------------------------------------

"""
To convert hexadecimal to octal:

    First convert Hexadecimal to Binary.
    Then convert Binary to Octal.

    Hexadecimal -> Binary -> Octal

Example 1:

    Convert (A6)₁₆ to Octal.

Step 1: Hexadecimal to Binary.

    A -> 1010
    6 -> 0110

    Therefore:

    A6₁₆ = 10100110₂

Step 2: Group binary digits into sets of 3,
starting from the right.

    10100110
    10 100 110

Step 3: Add leading zeros to complete the first group.

    010 100 110

Step 4: Convert each group into octal.

    010 -> 2
    100 -> 4
    110 -> 6

Therefore:

    (A6)₁₆ = (246)₈
"""