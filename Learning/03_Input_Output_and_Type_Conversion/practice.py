"""
==========================================================
Practice Questions - Day 03
==========================================================
"""
import math

# --------------------------------------------------------
# Basic Practice
# --------------------------------------------------------

# Q1
# Take your name as input and print:
# Hello <name>

name = input("Enter your name: ")
print(f"Hello {name}")

# Q2
# Take your age as input and print it.

age = int(input("Enter your age: "))
print(f"Your age is {age}")

# Q3
# Take two integers and print their sum.

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

c = a + b
print(f"sum {c}")

# Q4
# Take two float numbers and print their product.

a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = a * b
print(f"Product {c}")

# Q5
# Take first name and last name separately
# and print the full name.

# --------------------------------------------------------
# Intermediate Practice
# --------------------------------------------------------

# Q6
# Take marks of three subjects.
# Print total and average.

a = float(input("Enter marks of first subject: "))
b = float(input("Enter marks of second subject: "))
c = float(input("Enter marks of third subject: "))

total = a + b + c
average = total / 3

print(f"Total marks: {total}")
print(f"Average marks: {average}")

# Q7
# Take annual salary.
# Print monthly salary.

annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12
print(f"Monthly salary is {monthly_salary}")

# Q8
# Take length and breadth.
# Print area of rectangle.

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth

print(f"Area of rectangle is {area}")

# Q9
# Take radius of circle.
# Print area.

radius_of_circle = float(input("Enter radius of circle: "))
PI = 3.14159

area = PI * radius_of_circle * radius_of_circle

print(f"Area of circle is {area}")


# Q10
# Take quantity and price.
# Print total bill.

quantity = float(input("Enter quantity: "))
price = float(input("Enter price: "))

total_price = quantity * price

print(f"Total price is ₹{total_price:.2f}")

# --------------------------------------------------------
# Output Prediction
# --------------------------------------------------------

# Predict Output

# age = "22"
# print(age + "5")

# ----------------

# Predict Output

# num = int("50")
# print(num + 10)

# ----------------

# Predict Output

# a = 10
# b = 20
# print(f"{a} + {b} = {a+b}")

# --------------------------------------------------------
# Concept Questions
# --------------------------------------------------------

# 1. Why does input() return a string?



# 2. What is type conversion?

# Type conversion means converting a value from one data type to another.

# 3. Difference between int() and float()?

 # int() creates/converts to a whole number, while float() creates/converts to a decimal-capable number.

# 4. What are f-strings?

# f-strings (formatted string literals) allow you to insert variables or expressions directly inside a string.

# 5. What is variable reassignment?

#Variable reassignment means giving an existing variable a new value.

# --------------------------------------------------------
# Challenge
# --------------------------------------------------------

# Build a Simple Student Result Calculator

# Input:
# Student Name
# Three Subject Marks

# Output:
# Name
# Total
# Average

name = input("Enter your name: ")
a = float(input("Enter your first subject marks: "))
b = float(input("Enter your second subject marks: "))
c = float(input("Enter your third subject marks: "))

total = a + b + c
average = total / 3

print(f"Name of student : {name} \nTotal marks: {total} \nAverage marks: {average}")
