"""
==========================================================
Day 04 : Operators
Topic  : Practice Questions

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 04.

Instructions:
- Solve each question before referring to examples.py.
- Write clean and readable code.
- Run your program to verify the output.
- Experiment with different inputs whenever possible.
==========================================================
"""

# ==========================================================
# Basic Practice
# ==========================================================

# Q1. Create two variables num1 and num2.
# Display their:
# - Addition
# - Subtraction
# - Multiplication
# - Division

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)


# ==========================================================

# Q2. Find the floor division of 25 by 4.

# Expected Output:
# 6

n1 = 25
n2 = 4

floor_division = n1 // n2
print("Floor division: ", floor_division)

# ==========================================================

# Q3. Find the remainder when 25 is divided by 4.

# Expected Output:
# 1

n1 = 25
n2 = 4

remainder = n1 % n2
print("Remainder: ", remainder)

# ==========================================================

# Q4. Find the square of 9 using the exponent operator.

# Expected Output:
# 81

n = 9
square = n ** 2
print("Square: ", square)


# ==========================================================

# Q5. Remove the last digit from the number 5678.

# Expected Output:
# 567

n = 5678
remove_last_digit = n // 10
print("Number after last digit removed ", remove_last_digit)

# ==========================================================

# Q6. Extract the last digit from the number 5678.

# Expected Output:
# 8

n = 5678
print_last_digit = n % 10
print("last digit ", print_last_digit)

# ==========================================================
# Intermediate Practice
# ==========================================================

# Q7. Check whether 25 is greater than 18.

# Expected Output:
# True

n = 25
print(n > 18)

# ==========================================================

# Q8. Check whether the number 36 is even.

# Expected Output:
# True

n = 36
print(n % 2==0)

# ==========================================================

# Q9. Create the following variables:
#
# age = 22
# salary = 35000
#
# Check whether the person:
# - is at least 18 years old
# - earns at least 30000

# Expected Output:
# True

age = 22
salary = 35000

print(age >= 18 and salary >= 30000)


# ==========================================================

# Q10. Create a variable count = 10.
#
# Perform the following operations:
#
# += 5
# -= 2
# *= 3

# Display the final value.

count = 10
count += 5
count -= 2
count *= 3
print(count)


# ==========================================================
# Membership Operators
# ==========================================================

# Q11. Create the following list.

# courses = ["Python", "SQL", "Azure", "Spark"]

# Check whether:
#
# "Python" exists.
# "Java" exists.
# "SQL" does not exist.

courses = ["Python", "SQL", "Azure", "Spark"]

print("Python" in courses)
print("Java" in courses)
print("SQL" not in courses)

# ==========================================================

# Q12. Check whether '@' exists in the email below.

# email = "onkar@gmail.com"

email = "onkar@gmail.com"
print("@" in email)


# ==========================================================
# Output Prediction
# ==========================================================

# Q13. Predict the output.

print(20 // 3)

# Your Answer:
# 6


# ==========================================================

# Q14. Predict the output.

print(20 % 3)

# Your Answer:
# 2


# ==========================================================

# Q15. Predict the output.

print(5 ** 2)

# Your Answer:
# 25


# ==========================================================

# Q16. Predict the output.

x = 10
x += 8

print(x)

# Your Answer:
# 18


# ==========================================================

# Q17. Predict the output.

print(10 > 5 and 8 < 3)

# Your Answer:
# True
# false


# ==========================================================
# Concept Questions
# ==========================================================

# Q18. What is an operator?

# operator is a special symbol in python which ferform operations

# ==========================================================

# Q19. What is the difference between '/' and '//'?

# /  → Normal division. Returns the division result, usually as a float.
# // → Floor division. Returns the result rounded down to the nearest whole value.

# ==========================================================

# Q20. What is the difference between '=' and '=='?

# =  is an assignment operator used to assign a value to a variable.
# == is a comparison operator used to check whether two values are equal.
# ==========================================================

# Q21. What does the modulus (%) operator return?

# The modulus (%) operator returns the remainder after division.

# ==========================================================

# Q22. Name any six types of operators in Python.

# Six types of operators in Python:
#
# 1. Arithmetic operators
# 2. Comparison operators
# 3. Logical operators
# 4. Assignment operators
# 5. Membership operators
# 6. Identity operators

# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Input a three-digit number.
#
# Display:
# - Last digit
# - Number after removing the last digit
#
# Example:
#
# Input:
# 458
#
# Output:
# Last Digit : 8
# Remaining Number : 45

num = int(input("Enter a number: "))

last_digit = num % 10
remaining_number = num // 10

print("Last Digit:", last_digit)
print("Remaining Number:", remaining_number)
# ==========================================================

# Challenge 2
#
# Create a simple calculator that displays:
#
# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Exponent
#
# using two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulo = num1 % num2
exponent = num1 ** num2

print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
print("Floor division: ", floor_division)
print("Modulo: ", modulo)
print("Exponent: ", exponent)


# ==========================================================

# Challenge 3
#
# Create the following variables:
#
# marks = 78
# attendance = 82
#
# A student passes if:
#
# - marks >= 35
# - attendance >= 75
#
# Display whether the student passed.

marks = 78
attendance = 82

if marks >= 35 and attendance >= 75:
    print("Pass")

# ==========================================================

print("\n🎉 Congratulations! You have completed Day 04 Practice.")