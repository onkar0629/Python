"""
==========================================================
Day 06 : Multiple if Statements and Nested if Statements
Topic  : Practice Question Answers

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 06.

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

# Q1. Write a program using multiple if statements.
#
# Given:
# number = 24
#
# Check whether:
# - The number is positive.
# - The number is even.
# - The number is less than 100.

number = 23
if number % 2 == 0:
    print("Even")
if number > 0:
    print("Positive")
if number < 100:
    print("The Number is less than 100")

# ==========================================================

# Q2. Write a program to check a student's eligibility.
#
# Given:
# age = 19
# marks = 72
#
# Conditions:
# - Age should be at least 18.
# - Marks should be at least 35.
#
# Use multiple if statements.

age = 19
marks = 72

if age >= 18:
    print("Age requirement satisfied")

if marks >= 35:
    print("Marks requirement satisfied")

# ==========================================================

# Q3. Write a program to check an employee's eligibility.
#
# Given:
# experience = 4
# salary = 45000
#
# Conditions:
# - Experience >= 2 years
# - Salary >= 30000
#
# Use multiple if statements.

experience = 4
salary = 45000

if experience >= 2:
    print("Experience Criteria Matched")

if salary >= 30000:
    print("Salary Requirement Satisfied")

# ==========================================================

# Q4. Write a program to check:
#
# number = 50
#
# Display:
# - Divisible by 5
# - Divisible by 10
#
# Use multiple if statements.

number = 50

if number % 5 == 0:
    print("Number is divisible by 5")

if number % 10 == 0:
    print("Number is divisible by 10")

# ==========================================================

# Q5. Write a program to check:
#
# age = 65
#
# Display:
# - Adult (Age >= 18)
# - Senior Citizen (Age >= 60)
#
# Use multiple if statements.

age = 65

if age >= 18:
    print("Adult")

if age >= 60:
    print("Senior Citizen")

# ==========================================================
# Intermediate Practice
# ==========================================================

# Q6. Write a Nested if program for voting eligibility.
#
# Given:
# age = 20
# citizen = True
#
# Conditions:
# - Age must be at least 18.
# - Person must be a citizen.

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("You are not eligible")

# ==========================================================

# Q7. Create an ATM Withdrawal program.
#
# Given:
# balance = 10000
# withdraw_amount = 2500
#
# Conditions:
# - Withdrawal amount should be greater than 0.
# - Balance should be sufficient.

balance = 10000
withdraw_amount = 2500

if withdraw_amount > 0:
    if withdraw_amount <= balance:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Withdrawal Amount")

# ==========================================================

# Q8. Create a Login System.
#
# Given:
# username = "admin"
# password = "python123"
#
# Display:
# - Login Successful
# - Incorrect Password
# - Invalid Username

username = "admin"
password = "python123"
if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

# ==========================================================

# Q9. Scholarship Eligibility
#
# Given:
# marks = 92
# attendance = 85
#
# Conditions:
# - Marks >= 85
# - Attendance >= 75

marks = 92
attendance = 85

if marks >= 85:
    if attendance >= 75:
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("You are not eligible")

# ==========================================================

# Q10. Dataset Validation
#
# Given:
# file_exists = True
# total_records = 1200
# missing_records = 0
#
# Display:
# - File Not Found
# - Dataset is Empty
# - Data Cleaning Required
# - Dataset Ready for Processing

file_exists = True
total_records = 1200
missing_records = 0

if file_exists:
    if total_records > 0:
        if missing_records == 0:
            print("Dataset Ready for Processing")
        else:
            print("Data Cleaning Required")
    else:
        print("Dataset is Empty")
else:
    print("File Not Found")

# ==========================================================
# Output Prediction
# ==========================================================

# Q11. Predict the output.

number = 18

if number > 0:
    print("Positive")

if number % 2 == 0:
    print("Even")

# Your Answer:
#Positive
#Even


# ==========================================================

# Q12. Predict the output.

age = 20
citizen = False

if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Citizen Required")

# Your Answer:
# Citizen Required


# ==========================================================

# Q13. Predict the output.

experience = 5

if experience >= 2:
    print("Experienced")

if experience >= 5:
    print("Senior Level")

# Your Answer:
# Senior Level

# ==========================================================

# Q14. Predict the output.

username = "admin"
password = "java123"

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")

# Your Answer:
# Incorrect Password

# ==========================================================

# Q15. Predict the output.

file_exists = False

if file_exists:
    print("Processing Started")

print("Program Finished")

# Your Answer:
# Program Finished


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What are Multiple if statements?

# Multiple if statements are used when we want to check
# multiple conditions independently.
# Each if condition is checked separately.
# If a condition is True, its block is executed.

# ==========================================================

# Q17. What is a Nested if statement?

# A Nested if means writing an if statement inside
# another if statement.
#
# The inner if condition is checked only when the
# outer if condition is True.

# ==========================================================

# Q18. What is the difference between Multiple if and Nested if?

# Multiple if:
# - Conditions are independent.
# - Every if condition is checked.
# - One condition does not depend on another.
#
# Nested if:
# - One if statement is inside another if statement.
# - The inner condition depends on the outer condition.
# - The inner if is checked only if the outer if is True.

# ==========================================================

# Q19. When should you use Multiple if statements?

# Use Multiple if statements when you need to check
# several independent conditions.

# ==========================================================

# Q20. When should you use Nested if statements?

# Use Nested if statements when one condition should
# be checked only after another condition is True.

# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Create a Bank Loan Eligibility Program.
#
# Conditions:
# - Age >= 21
# - Salary >= 30000
# - Credit Score >= 700
#
# Display whether the loan is approved.


# ==========================================================

# Challenge 2
#
# Create a College Admission Program.
#
# Conditions:
# - Marks >= 60
# - Entrance Exam Qualified
#
# Display whether admission is granted.


# ==========================================================

# Challenge 3
#
# Create a Secure Login System.
#
# Conditions:
# - Username is correct.
# - Password is correct.
# - OTP is verified.
#
# Display the appropriate message.


# ==========================================================

# Challenge 4
#
# Create an Online Shopping Checkout Program.
#
# Conditions:
# - Cart is not empty.
# - Payment is successful.
# - Address is available.
#
# Display whether the order is placed successfully.


# ==========================================================

# Challenge 5
#
# Data Engineering Challenge
#
# Given:
# file_exists = True
# schema_valid = True
# null_values = 0
#
# Process the dataset only if:
# - File exists.
# - Schema is valid.
# - There are no null values.
#
# Otherwise, display an appropriate validation message.


# ==========================================================

print("\n🎉 Congratulations! You have completed Day 06 Practice.")