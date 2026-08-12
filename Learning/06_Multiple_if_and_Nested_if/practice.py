"""
==========================================================
Day 06 : Multiple if Statements and Nested if Statements
Topic  : Practice Questions

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

# Your code here


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

# Your code here


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

# Your code here


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

# Your code here


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

# Your code here


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

# Your code here


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

# Your code here


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

# Your code here


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

# Your code here


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

# Your code here


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
# __________________


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
# __________________


# ==========================================================

# Q13. Predict the output.

experience = 5

if experience >= 2:
    print("Experienced")

if experience >= 5:
    print("Senior Level")

# Your Answer:
# __________________


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
# __________________


# ==========================================================

# Q15. Predict the output.

file_exists = False

if file_exists:
    print("Processing Started")

print("Program Finished")

# Your Answer:
# __________________


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What are Multiple if statements?


# ==========================================================

# Q17. What is a Nested if statement?


# ==========================================================

# Q18. What is the difference between Multiple if and Nested if?


# ==========================================================

# Q19. When should you use Multiple if statements?


# ==========================================================

# Q20. When should you use Nested if statements?


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