"""
==========================================================
Day 11 : Function Arguments
Topic  : Practice Questions

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 11.

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

# Q1. Create a function named introduce().
#
# Parameters:
# - name
# - age
#
# Call the function using positional arguments.
#
# Example:
# introduce("Rahul", 22)
#
# Output:
# Name: Rahul
# Age: 22

# Your code here


# ==========================================================

# Q2. Create a function named employee().
#
# Parameters:
# - name
# - department
#
# Call the function using keyword arguments.
#
# Example:
# employee(
#     department="Data Engineering",
#     name="Aman"
# )

# Your code here


# ==========================================================

# Q3. Create a function named greet().
#
# Parameters:
# - name
# - message with default value "Welcome"
#
# Test the function:
#
# greet("Rahul")
# greet("Rahul", "Good Morning")

# Your code here


# ==========================================================

# Q4. Create a function named calculate_price().
#
# Parameters:
# - price
# - quantity with default value 1
#
# Return the total price.
#
# Example:
# calculate_price(500)
#
# Output:
# 500
#
# Example:
# calculate_price(500, 4)
#
# Output:
# 2000

# Your code here


# ==========================================================

# Q5. Create a function named display_numbers().
#
# Use *args to accept any number of values.
#
# Example:
# display_numbers(10, 20, 30, 40)
#
# Output:
# 10
# 20
# 30
# 40

# Your code here


# ==========================================================
# Intermediate Practice
# ==========================================================

# Q6. Create a function named calculate_total().
#
# Use *args to accept multiple numbers and return their sum.
#
# Example:
# calculate_total(10, 20, 30)
#
# Output:
# 60

# Your code here


# ==========================================================

# Q7. Create a function named find_largest().
#
# Use *args to accept multiple numbers.
# Return the largest number.
#
# Example:
# find_largest(15, 42, 8, 91, 27)
#
# Output:
# 91

# Your code here


# ==========================================================

# Q8. Create a function named display_profile().
#
# Use **kwargs to accept:
#
# name
# age
# city
#
# Print each key and value.

# Your code here


# ==========================================================

# Q9. Create a function named employee_skills().
#
# The first parameter should be:
# name
#
# Use *args to accept multiple skills.
#
# Example:
#
# employee_skills(
#     "Rahul",
#     "Python",
#     "SQL",
#     "Spark"
# )
#
# Output:
#
# Employee: Rahul
# Python
# SQL
# Spark

# Your code here


# ==========================================================

# Q10. Create a function named employee_profile().
#
# Required parameter:
# name
#
# Use **kwargs for additional employee information.
#
# Example:
#
# employee_profile(
#     "Aman",
#     department="Data Engineering",
#     city="Pune",
#     experience=2
# )

# Your code here


# ==========================================================
# Output Prediction
# ==========================================================

# Q11. Predict the output.

def student(name, age):
    print(name, age)


student("Rahul", 22)

# Your Answer:
# __________________


# ==========================================================

# Q12. Predict the output.

def student(name, age):
    print(name, age)


student(age=22, name="Rahul")

# Your Answer:
# __________________


# ==========================================================

# Q13. Predict the output.

def greet(name, message="Hello"):
    print(message, name)


greet("Aman")

# Your Answer:
# __________________


# ==========================================================

# Q14. Predict the output.

def greet(name, message="Hello"):
    print(message, name)


greet("Aman", "Welcome")

# Your Answer:
# __________________


# ==========================================================

# Q15. Predict the output.

def total(*numbers):
    print(numbers)


total(10, 20, 30)

# Your Answer:
# __________________


# ==========================================================

# Q16. Predict the output.

def profile(**details):
    print(details)


profile(name="Rahul", city="Pune")

# Your Answer:
# __________________


# ==========================================================

# Q17. Predict the output.

def calculate(price, quantity=2):
    return price * quantity


print(calculate(500))

# Your Answer:
# __________________


# ==========================================================
# Concept Questions
# ==========================================================

# Q18. What is the difference between a parameter
# and an argument?


# ==========================================================

# Q19. What are positional arguments?


# ==========================================================

# Q20. What are keyword arguments?


# ==========================================================

# Q21. What is a default argument?


# ==========================================================

# Q22. What is *args?


# ==========================================================

# Q23. Which data type is used to store values received
# through *args?


# ==========================================================

# Q24. What is **kwargs?


# ==========================================================

# Q25. Which data type is used to store values received
# through **kwargs?


# ==========================================================

# Q26. What is the difference between *args and **kwargs?


# ==========================================================

# Q27. Are the names args and kwargs mandatory?
# Explain your answer.


# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Shopping Bill
#
# Create a function named calculate_bill().
#
# Parameters:
# - price
# - quantity with default value 1
#
# Return the total bill.
#
# Example:
#
# calculate_bill(750, 4)
#
# Output:
# Total Bill = ₹3000


# ==========================================================

# Challenge 2
#
# Student Marks
#
# Create a function named calculate_average().
#
# Use *args to accept any number of marks.
#
# Calculate and return the average.
#
# Example:
#
# calculate_average(80, 75, 90, 85)
#
# Output:
# Average = 82.5


# ==========================================================

# Challenge 3
#
# Employee Profile
#
# Create a function using **kwargs.
#
# Pass:
#
# name="Rahul"
# role="Data Engineer"
# city="Pune"
# experience=1
#
# Display all the employee information.


# ==========================================================

# Challenge 4
#
# Product Order
#
# Create a function:
#
# order_product(product, quantity=1, **details)
#
# Example:
#
# order_product(
#     "Laptop",
#     quantity=2,
#     customer="Rahul",
#     city="Pune"
# )
#
# Display:
# Product
# Quantity
# Customer
# City


# ==========================================================

# Challenge 5
#
# Data Engineering Challenge - Process Multiple Files
#
# Create a function named process_files().
#
# Use *args to accept multiple file names.
#
# Example:
#
# process_files(
#     "customers.csv",
#     "orders.csv",
#     "products.csv"
# )
#
# Expected Output:
#
# Processing customers.csv
# Processing orders.csv
# Processing products.csv
# All Files Processed Successfully!


# ==========================================================

# Challenge 6
#
# Data Engineering Challenge - Pipeline Configuration
#
# Create a function named pipeline_config().
#
# Use **kwargs to accept pipeline configuration.
#
# Example:
#
# pipeline_config(
#     source="Azure Blob Storage",
#     destination="Data Warehouse",
#     file_format="CSV",
#     batch_size=5000
# )
#
# Print every configuration key and value.


# ==========================================================

# Challenge 7
#
# Flexible Data Loader
#
# Create a function:
#
# load_data(file_name, file_type="csv", **config)
#
# The function should display:
#
# - File name
# - File type
# - Additional configuration
#
# Example:
#
# load_data(
#     "customers.csv",
#     batch_size=1000,
#     validate_schema=True
# )


# ==========================================================

print("\nCongratulations! You have completed Day 11 Practice.")