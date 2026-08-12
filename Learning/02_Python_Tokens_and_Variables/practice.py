"""
============================================================
Day 02 : Python Tokens and Variables
File   : practice.py
============================================================

Instructions:
1. Solve every question on your own.
2. Predict the output before running the program.
3. Follow Python naming conventions.
4. Execute your code in PyCharm.
"""
import math
from unittest.loader import VALID_MODULE_NAME

# ============================================================
# Section 1 : Literals
# ============================================================

# Q1.
# Create an integer literal and print it.

a = 15
print(a)

# Q2.
# Create a floating-point literal and print it.

a = 15.567
print(float(a))

# Q3.
# Store your name in a string variable and print it.

a = "onkar Jadhav"
print(a)

# Q4.
# Create a Boolean variable named is_student
# and assign it an appropriate value.


is_student = True
print("Is Student", is_student)

# Q5.
# Create variables for:
# - Your age
# - Your height
# - Your city
# Print all three values.

a = 22
b = 173
c = "Ahmednagar"

print(a, b, c)

# ============================================================
# Section 2 : Variables
# ============================================================

# Q6.
# Create a variable named college
# and store your college name.

college = "Dy Patil university"
print(college)


# Q7.
# Create variables:
#
# price = 250
# quantity = 4
#
# Print both variables.

price = 250
quantity = 4
print(price, quantity)

# Q8.
# Create three variables:
#
# first_name
# last_name
# full_name
#
# Store your full name and print it.

first_name = "Onkar"
last_name = "Jadhav"
full_name = (first_name + " " + last_name)
print(full_name)

# Q9.
# Create a variable named marks
# Assign any value and print it.

marks = 45
print(marks)

# Q10.
# Change the value of marks
# and print it again.

marks = 55
print(marks)

# ============================================================
# Section 3 : Assignment Operator
# ============================================================

# Q11.
#
# a = 15
# b = a
#
# Print both variables.

a = 15
b = a
print(a , b)

# Q12.
#
# x = 20
# y = 30
#
# Create a third variable that stores the sum.

x = 20
y = 30
z = x + y
print(z)

# Q13.
#
# Create:
#
# length = 12
# width = 5
#
# Calculate the area of a rectangle.

length = 12
width = 5
print("Area of rectangle :",length * width)

# Q14.
#
# Create:
#
# radius = 7
#
# Use PI = 3.14
#
# Calculate the area of a circle.

radius = 7
PI = 3.14
print("Area of circle :",PI * radius ** 2)

# ============================================================
# Section 4 : Arithmetic Operators
# ============================================================

# Q15.
#
# num1 = 20
# num2 = 6
#
# Perform:
#
# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Exponentiation

num1 = 20
num2 = 6

print("Addition of two numbers :",num1 + num2)
print("Subtraction of two numbers :",num1 - num2)
print("Multiplication of two numbers :",num1 * num2)
print("Division of two numbers :",num1 / num2)
print("floor division of two numbers :",num1 // num2)
print("Modulo of two numbers :",num1 % num2)
print("exponentiation of two numbers :",num1 ** num2)

# Q16.
#
# Find the remainder when
# 125 is divided by 8.

print(125 % 8)

# Q17.
#
# Find the quotient using floor division:
#
# 100 // 9

print(100 // 9)

# Q18.
#
# Calculate:
#
# (15 + 5) * 2

print((15 +5) * 2)

# Q19.
#
# Calculate:
#
# 3 ** 4

print(3 ** 4)

# ============================================================
# Section 5 : Identifiers
# ============================================================

# Write VALID or INVALID.
#
# # Q20.
# #
# # student_name
# VALID_
# # Q21.
# #
# # totalMarks
# valid
# # Q22.
# #
# # 2student
# invalid
# # Q23.
# #
# # employee-id
# invalid
# # Q24.
# #
# # _salary
# valid
# # Q25.
# #
# # class
# invalid
# # Q26.
# #
# # employee2
# valid
# # Q27.
# #
# # first name
# invalid
# # Q28.
# #
# # __count
# valid
# # Q29.
# #
# # while
# invalid

# ============================================================
# Section 6 : Output Prediction
# ============================================================

# Predict the output before running.

# Q30.

print(10 + 20)

# Output:
# 30

# Q31.

print(20 / 5)

# Output:
# 4

# Q32.

print(20 // 6)

# Output:
# 3

# Q33.

print(20 % 6)

# Output:
# 2

# Q34.

print(2 ** 5)

# Output:
# 32

# Q35.

name = "Python"

print(name)

# Output:
# Python


# ============================================================
# Section 7 : Think Like a Programmer
# ============================================================

# Q36.
#
# Explain the difference between:
#
# Literal  are the fixed values
# Variable : are the named memory location in which we store data
# Identifier : identifiers are the given names to variables , classes , functions

# Q37.
#
# Why can't Python keywords be used
# as variable names?

# because python will read variable as keyword and may perform the operation as keyword which will through and error

# Q38.
#
# What is the difference between:
#
# /
#
# and
#
# //

# / will return answer in decimal
# // will return value in integer

# Q39.
#
# Explain the difference between:
#
# 20 / 3
#
# and
#
# 20 % 3

# 20 / 3 returns the quotient as a floating-point number.
# Output: 6.666666666666667

# 20 % 3 returns the remainder after division.
# Output: 2

# Q40.
#
# Why should variable names be meaningful?

#because we call variable in the program

# ============================================================
# Section 8 : Self-Learning
# ============================================================

# Search and learn:
#
# 1. How many keywords are available
#    in the latest version of Python?
#
# 2. What is snake_case naming convention?
#
# 3. Why is True a keyword but "True"
#    is a string?
#
# 4. What does the keyword module do?
#
# 5. What is the difference between
#    == and = ?

