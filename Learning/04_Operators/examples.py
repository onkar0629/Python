"""
==========================================================
Day 04 : Operators
Topic  : Python Operators
Author : Onkar Jadhav

Description:
This file contains examples of different types of
operators in Python.

Topics Covered:
1. Arithmetic Operators
2. Relational Operators
3. Logical Operators
4. Assignment Operator
5. Shorthand Assignment Operators
6. Membership Operators
==========================================================
"""

# ==========================================================
# 1. Arithmetic Operators
# ==========================================================

print("========== Arithmetic Operators ==========\n")

a = 20
b = 6

print("a =", a)
print("b =", b)
print()

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** 2)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Practical Example 1 - Remove Last Digit
# ==========================================================

print("Remove Last Digit")

number = 4567

print("Original Number :", number)
print("After Removing Last Digit :", number // 10)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Practical Example 2 - Extract Last Digit
# ==========================================================

print("Extract Last Digit")

number = 4567

print("Original Number :", number)
print("Last Digit :", number % 10)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. Relational Operators
# ==========================================================

print("========== Relational Operators ==========\n")

x = 15
y = 10

print("x =", x)
print("y =", y)
print()

print("x > y  :", x > y)
print("x < y  :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)
print("x == y :", x == y)
print("x != y :", x != y)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Check Even Number
# ==========================================================

number = 18

print("Number :", number)
print("Is Even?", number % 2 == 0)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 3. Logical Operators
# ==========================================================

print("========== Logical Operators ==========\n")

age = 22
salary = 30000

print("Age :", age)
print("Salary :", salary)
print()

print("AND :", age >= 18 and salary >= 25000)
print("OR  :", age >= 25 or salary >= 25000)
print("NOT :", not (age < 18))

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 4. Assignment Operator
# ==========================================================

print("========== Assignment Operator ==========\n")

name = "Onkar"

print("Name :", name)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 5. Shorthand Assignment Operators
# ==========================================================

print("========== Shorthand Assignment ==========\n")

count = 10

print("Initial Value :", count)

count += 5
print("After += 5 :", count)

count -= 3
print("After -= 3 :", count)

count *= 2
print("After *= 2 :", count)

count //= 4
print("After //= 4 :", count)

count %= 3
print("After %= 3 :", count)

count **= 2
print("After **= 2 :", count)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 6. Membership Operators
# ==========================================================

print("========== Membership Operators ==========\n")

courses = ["Python", "SQL", "Azure", "Spark"]

print(courses)
print()

print("'Python' in courses      :", "Python" in courses)
print("'Java' in courses        :", "Java" in courses)
print("'Java' not in courses    :", "Java" not in courses)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Membership Example with String
# ==========================================================

email = "onkar@gmail.com"

print("Email :", email)

print("'@' in email :", "@" in email)
print("'#' in email :", "#" in email)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Real-World Example
# ==========================================================

print("========== Real-World Example ==========\n")

total_records = 1250
processed_records = 1200

print("Total Records     :", total_records)
print("Processed Records :", processed_records)

print()

print("Remaining Records :", total_records - processed_records)
print("All Records Processed?",
      total_records == processed_records)

print("\n" + "=" * 50)

print("\nEnd of Day 04 Examples 🚀")