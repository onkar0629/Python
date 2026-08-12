"""
==========================================================
Day 12 : Recursion
Topic  : Practice Questions

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 12.

Instructions:
- Solve each question before referring to examples.py.
- Write clean and readable code.
- Identify the base case before writing recursive logic.
- Make sure each recursive call moves toward the base case.
- Run your program and verify the output.
==========================================================
"""

# ==========================================================
# Basic Practice
# ==========================================================

# Q1. Create a recursive function named countdown().
#
# The function should accept a number and print numbers
# from that number down to 1.
#
# Example:
# countdown(5)
#
# Output:
# 5
# 4
# 3
# 2
# 1

# Your code here


# ==========================================================

# Q2. Create a recursive function named print_numbers().
#
# Print numbers from 1 to the given number.
#
# Example:
# print_numbers(5)
#
# Output:
# 1
# 2
# 3
# 4
# 5

# Your code here


# ==========================================================

# Q3. Create a recursive function named greet().
#
# It should print "Hello Python" the given number of times.
#
# Example:
# greet(3)
#
# Output:
# Hello Python
# Hello Python
# Hello Python

# Your code here


# ==========================================================

# Q4. Create a recursive function to calculate the
# sum of natural numbers from 1 to n.
#
# Example:
# calculate_sum(5)
#
# Output:
# 15

# Your code here


# ==========================================================

# Q5. Create a recursive function to calculate factorial.
#
# Example:
# factorial(5)
#
# Calculation:
# 5 x 4 x 3 x 2 x 1
#
# Output:
# 120

# Your code here


# ==========================================================
# Intermediate Practice
# ==========================================================

# Q6. Create a recursive function named calculate_power().
#
# Parameters:
# - base
# - exponent
#
# Example:
# calculate_power(2, 5)
#
# Output:
# 32

# Your code here


# ==========================================================

# Q7. Create a recursive function to multiply two
# non-negative integers using repeated addition.
#
# Do not use the * operator for the multiplication itself.
#
# Example:
# multiply(5, 4)
#
# Calculation:
# 5 + 5 + 5 + 5
#
# Output:
# 20

# Your code here


# ==========================================================

# Q8. Create a recursive function named sum_list().
#
# Given:
# numbers = [10, 20, 30, 40]
#
# Calculate the sum without using sum().
#
# Output:
# 100

# Your code here


# ==========================================================

# Q9. Create a recursive function named count_elements().
#
# Count the number of elements in a list without
# using len() to calculate the final count.
#
# Given:
# values = [10, 20, 30, 40, 50]
#
# Output:
# 5

# Your code here


# ==========================================================

# Q10. Create a recursive function named find_max().
#
# Find the largest value in a non-empty list.
#
# Given:
# numbers = [25, 80, 15, 95, 40]
#
# Output:
# 95

# Your code here


# ==========================================================
# Output Prediction
# ==========================================================

# Q11. Predict the output.

def countdown(number):
    if number == 0:
        return

    print(number)
    countdown(number - 1)


countdown(3)

# Your Answer:
# __________________


# ==========================================================

# Q12. Predict the output.

def display(number):
    if number == 0:
        return

    display(number - 1)
    print(number)


display(3)

# Your Answer:
# __________________


# ==========================================================

# Q13. Predict the output.

def calculate(number):
    if number == 0:
        return 0

    return number + calculate(number - 1)


print(calculate(4))

# Your Answer:
# __________________


# ==========================================================

# Q14. Predict the output.

def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


print(factorial(4))

# Your Answer:
# __________________


# ==========================================================

# Q15. Predict the output.

def test(number):
    if number == 0:
        print("Stop")
        return

    print("Before:", number)

    test(number - 1)

    print("After:", number)


test(2)

# Your Answer:
# __________________


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What is recursion?


# ==========================================================

# Q17. What is a base case?


# ==========================================================

# Q18. What is a recursive case?


# ==========================================================

# Q19. Why is a base case necessary in recursion?


# ==========================================================

# Q20. What happens if a recursive function does not
# have a reachable base case?


# ==========================================================

# Q21. What is the difference between recursion
# and iteration?


# ==========================================================

# Q22. What is the call stack?


# ==========================================================

# Q23. What is RecursionError in Python?


# ==========================================================

# Q24. Is recursion always better than using a loop?
# Explain your answer.


# ==========================================================

# Q25. Why must the input usually change during
# every recursive call?


# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Sum of Even Numbers
#
# Create a recursive function that calculates the sum
# of all even numbers from 2 to n.
#
# Example:
# n = 10
#
# Calculation:
# 2 + 4 + 6 + 8 + 10
#
# Output:
# 30


# ==========================================================

# Challenge 2
#
# Reverse a String
#
# Create a recursive function named reverse_string().
#
# Example:
# reverse_string("Python")
#
# Output:
# nohtyP


# ==========================================================

# Challenge 3
#
# Count Digits
#
# Create a recursive function that counts the number
# of digits in a positive integer.
#
# Example:
# count_digits(45879)
#
# Output:
# 5


# ==========================================================

# Challenge 4
#
# Sum of Digits
#
# Create a recursive function named sum_digits().
#
# Example:
# sum_digits(458)
#
# Calculation:
# 4 + 5 + 8
#
# Output:
# 17


# ==========================================================

# Challenge 5
#
# Data Engineering Challenge - Nested Dictionary
#
# Given:
#
# customer = {
#     "customer_id": 1001,
#     "name": "Rahul",
#     "address": {
#         "city": "Pune",
#         "state": "Maharashtra",
#         "country": "India"
#     }
# }
#
# Create a recursive function that processes nested
# dictionaries and prints every final key-value pair.
#
# Expected Output:
#
# customer_id: 1001
# name: Rahul
# city: Pune
# state: Maharashtra
# country: India


# ==========================================================

# Challenge 6
#
# Data Engineering Challenge - Nested Pipeline Configuration
#
# Given:
#
# pipeline = {
#     "source": {
#         "type": "CSV",
#         "location": {
#             "folder": "raw",
#             "file": "customers.csv"
#         }
#     },
#     "destination": {
#         "type": "Database",
#         "table": "customers"
#     }
# }
#
# Write a recursive function that traverses the entire
# configuration and prints every final key-value pair.


# ==========================================================

# Challenge 7
#
# Recursive File Counter Simulation
#
# Imagine the following nested folder structure:
#
# folders = {
#     "raw": {
#         "customers.csv": None,
#         "orders.csv": None
#     },
#     "processed": {
#         "customers_clean.csv": None,
#         "archive": {
#             "old_customers.csv": None
#         }
#     }
# }
#
# Create a recursive function that counts how many files
# exist in the complete nested structure.
#
# Expected Output:
# Total Files = 4


# ==========================================================

print("\nCongratulations! You have completed Day 12 Practice.")