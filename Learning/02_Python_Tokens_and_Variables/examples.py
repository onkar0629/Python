"""
============================================================
Day 02 : Python Tokens and Variables
File   : examples.py
============================================================

Description:
This file contains examples of the concepts covered in Day 02.

Topics Covered:
1. Literals
2. Constants
3. Operators
4. Keywords
5. Identifiers
6. Variables
7. Assignment Operator

Author : Onkar Jadhav
"""

# ============================================================
# Example 1 : Integer Literals
# ============================================================

age = 22
employee_id = 101

print("Age:", age)
print("Employee ID:", employee_id)


# ============================================================
# Example 2 : Floating-Point Literals
# ============================================================

height = 5.8
price = 499.99

print("Height:", height)
print("Price:", price)


# ============================================================
# Example 3 : String Literals
# ============================================================

name = "Onkar"
course = 'Data Engineering'

print("Name:", name)
print("Course:", course)


# ============================================================
# Example 4 : Boolean Literals
# ============================================================

is_student = True
is_placed = False

print("Is Student:", is_student)
print("Is Placed:", is_placed)


# ============================================================
# Example 5 : Constants (Naming Convention)
# ============================================================

PI = 3.14159
MONTHS_IN_YEAR = 12

print("PI:", PI)
print("Months:", MONTHS_IN_YEAR)

# Note:
# Python doesn't enforce constants.
# UPPERCASE is a naming convention.


# ============================================================
# Example 6 : Arithmetic Operators
# ============================================================

a = 10
b = 3

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponent       :", a ** b)


# ============================================================
# Example 7 : Operands and Operators
# ============================================================

result = 25 + 15

print("Result:", result)

# '+' is the operator.
# 25 and 15 are operands.


# ============================================================
# Example 8 : Keywords
# ============================================================

import keyword

print("Is 'for' a keyword?      :", keyword.iskeyword("for"))
print("Is 'class' a keyword?    :", keyword.iskeyword("class"))
print("Is 'student' a keyword?  :", keyword.iskeyword("student"))


# ============================================================
# Example 9 : Valid Identifiers
# ============================================================

student_name = "Onkar"
_marks = 95
employee2 = 5001

print(student_name)
print(_marks)
print(employee2)


# ============================================================
# Example 10 : Invalid Identifiers
# ============================================================

# The following are INVALID identifiers.

# 2marks = 90
# student name = "Onkar"
# class = "Python"
# employee@id = 101

# Uncommenting any of the above lines will produce a SyntaxError.


# ============================================================
# Example 11 : Variables
# ============================================================

city = "Pune"
temperature = 29.5

print("City:", city)
print("Temperature:", temperature)


# ============================================================
# Example 12 : Assignment Operator
# ============================================================

x = 10
y = x
z = x + y

print("x =", x)
print("y =", y)
print("z =", z)


# ============================================================
# Example 13 : Updating Variable Values
# ============================================================

count = 5

print("Before:", count)

count = count + 1

print("After :", count)


# ============================================================
# Example 14 : Multiple Variables
# ============================================================

name = "Onkar"
age = 22
salary = 45000

print(name)
print(age)
print(salary)


# ============================================================
# Example 15 : Combining Variables
# ============================================================

first_name = "Onkar"
last_name = "Jadhav"

full_name = first_name + " " + last_name

print("Full Name:", full_name)
