"""
==========================================================
Day 03 : Input, Output and Type Conversion
Author : Onkar Jadhav
==========================================================
"""

# --------------------------------------------------------
# Example 1 : Variable Reassignment
# --------------------------------------------------------

age = 22
print(age)

age = 23
print(age)

print("-" * 40)

# --------------------------------------------------------
# Example 2 : Multiple Variable Assignment
# --------------------------------------------------------

name, city, age = "Onkar", "Pune", 22

print(name)
print(city)
print(age)

print("-" * 40)

# --------------------------------------------------------
# Example 3 : print() Function
# --------------------------------------------------------

print("Welcome to Python!")

language = "Python"

print(language)

print("Learning", language)

print("-" * 40)

# --------------------------------------------------------
# Example 4 : String Concatenation
# --------------------------------------------------------

first_name = "Onkar"
last_name = "Jadhav"

full_name = first_name + " " + last_name

print(full_name)

print("-" * 40)

# --------------------------------------------------------
# Example 5 : Formatted Output
# --------------------------------------------------------

marks = 95

print(f"Your marks are {marks}")

name = "Onkar"
age = 22

print(f"My name is {name} and I am {age} years old.")

print("-" * 40)

# --------------------------------------------------------
# Example 6 : User Input
# --------------------------------------------------------

name = input("Enter your name: ")

print(f"Welcome, {name}!")

print("-" * 40)

# --------------------------------------------------------
# Example 7 : Integer Input
# --------------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", num1 + num2)

print("-" * 40)

# --------------------------------------------------------
# Example 8 : Float Input
# --------------------------------------------------------

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

bill = price * quantity

print(f"Total Bill = {bill}")

print("-" * 40)

# --------------------------------------------------------
# Example 9 : Student Percentage
# --------------------------------------------------------

maths = int(input("Maths: "))
science = int(input("Science: "))
english = int(input("English: "))

total = maths + science + english

percentage = total / 3

print(f"Total = {total}")
print(f"Percentage = {percentage:.2f}%")