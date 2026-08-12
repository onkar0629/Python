"""
==========================================================
Day 10 : Functions
Topic  : Practice Questions

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 10.

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

# Q1. Create a function named greet().
#
# The function should print:
# Hello, Python!

# Your code here


# ==========================================================

# Q2. Create a function named welcome().
#
# The function should print:
# Welcome to Python Functions
#
# Call the function three times.

# Your code here


# ==========================================================

# Q3. Create a function named greet_user().
#
# The function should accept a name as a parameter.
#
# Example:
# greet_user("Onkar")
#
# Output:
# Hello, Onkar

# Your code here


# ==========================================================

# Q4. Create a function named add_numbers().
#
# It should accept two numbers and print their sum.
#
# Example:
# add_numbers(10, 20)
#
# Output:
# 30

# Your code here


# ==========================================================

# Q5. Create a function named square().
#
# It should accept a number and return its square.
#
# Example:
# square(5)
#
# Output:
# 25

# Your code here


# ==========================================================
# Intermediate Practice
# ==========================================================

# Q6. Create a function named calculate_total().
#
# Parameters:
# - price
# - quantity
#
# Return the total price.
#
# Example:
# calculate_total(500, 4)
#
# Output:
# 2000

# Your code here


# ==========================================================

# Q7. Create a function named check_even_odd().
#
# The function should accept a number and return:
#
# "Even" if the number is even.
# "Odd" if the number is odd.
#
# Example:
# check_even_odd(17)
#
# Output:
# Odd

# Your code here


# ==========================================================

# Q8. Create a function named check_voting_eligibility().
#
# The function should accept age as a parameter.
#
# Age >= 18:
# Eligible to Vote
#
# Otherwise:
# Not Eligible to Vote

# Your code here


# ==========================================================

# Q9. Create a function named find_largest().
#
# The function should accept two numbers and return
# the larger number.
#
# Example:
# find_largest(25, 40)
#
# Output:
# 40

# Your code here


# ==========================================================

# Q10. Create a function named multiplication_table().
#
# The function should accept a number and print its
# multiplication table from 1 to 10.
#
# Example:
# multiplication_table(5)
#
# Output:
# 5 x 1 = 5
# ...
# 5 x 10 = 50

# Your code here


# ==========================================================
# Output Prediction
# ==========================================================

# Q11. Predict the output.

def greet():
    print("Hello")


greet()

# Your Answer:
# __________________


# ==========================================================

# Q12. Predict the output.

def add(a, b):
    return a + b


result = add(10, 5)

print(result)

# Your Answer:
# __________________


# ==========================================================

# Q13. Predict the output.

def square(number):
    return number ** 2


print(square(4))

# Your Answer:
# __________________


# ==========================================================

# Q14. Predict the output.

def multiply(a, b):
    print(a * b)


result = multiply(5, 4)

print(result)

# Your Answer:
# __________________


# ==========================================================

# Q15. Predict the output.

def check_number(number):
    if number > 0:
        return "Positive"

    return "Not Positive"


print(check_number(-5))

# Your Answer:
# __________________


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What is a function in Python?


# ==========================================================

# Q17. Which keyword is used to define a function?


# ==========================================================

# Q18. What is the difference between a parameter
# and an argument?


# ==========================================================

# Q19. What is the purpose of the return statement?


# ==========================================================

# Q20. What is the difference between print() and return?


# ==========================================================

# Q21. What happens if a function does not contain
# a return statement?


# ==========================================================

# Q22. What is the difference between a built-in function
# and a user-defined function?


# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Simple Calculator
#
# Create four functions:
#
# add()
# subtract()
# multiply()
# divide()
#
# Each function should accept two numbers and return
# the appropriate result.
#
# Example:
#
# add(20, 10)       -> 30
# subtract(20, 10)  -> 10
# multiply(20, 10)  -> 200
# divide(20, 10)    -> 2.0


# ==========================================================

# Challenge 2
#
# Student Result
#
# Create a function named check_result().
#
# The function should accept marks and return:
#
# 90+ -> Grade A
# 75+ -> Grade B
# 60+ -> Grade C
# 35+ -> Pass
# Below 35 -> Fail


# ==========================================================

# Challenge 3
#
# Shopping Bill
#
# Create a function named calculate_bill().
#
# Parameters:
# - price
# - quantity
#
# Return the total bill.
#
# Example:
#
# Price    = ₹750
# Quantity = 4
#
# Output:
# Total Bill = ₹3000


# ==========================================================

# Challenge 4
#
# Data Validation
#
# Create a function named validate_record().
#
# The function should accept a record.
#
# If the record is None:
# return False
#
# Otherwise:
# return True
#
# Test the function using:
#
# records = [1001, None, 1003, None, 1005]
#
# Print only valid records.


# ==========================================================

# Challenge 5
#
# Data Transformation
#
# Create a function named transform_record().
#
# The function should accept a number and return
# the number multiplied by 10.
#
# Given:
#
# records = [10, 20, 30, 40]
#
# Process every record using the function.
#
# Expected Output:
#
# 10 -> 100
# 20 -> 200
# 30 -> 300
# 40 -> 400


# ==========================================================

# Challenge 6
#
# Simple ETL Pipeline
#
# Create three functions:
#
# extract_data()
# transform_data()
# load_data()
#
# Expected Output:
#
# Extracting Data...
# Transforming Data...
# Loading Data...
# ETL Pipeline Completed!


# ==========================================================

print("\nCongratulations! You have completed Day 10 Practice.")