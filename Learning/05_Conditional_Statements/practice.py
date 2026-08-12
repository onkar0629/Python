"""
==========================================================
Day 05 : Conditional Statements
Topic  : Practice Questions

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 05.

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

# Q1. Check whether a person is eligible to vote.
#
# Condition:
# Age >= 18
#
# Example:
# Input:
# age = 20
#
# Output:
# Eligible to Vote

# Your code here


# ==========================================================

# Q2. Check whether a number is positive.
#
# Example:
# number = 15
#
# Output:
# Positive Number

# Your code here


# ==========================================================

# Q3. Check whether a number is even or odd.
#
# Example:
# number = 19
#
# Output:
# Odd Number

# Your code here


# ==========================================================

# Q4. Check whether a student has passed.
#
# Passing Marks = 35
#
# Example:
# marks = 72
#
# Output:
# Pass

# Your code here


# ==========================================================

# Q5. Check whether a number is divisible by 5.
#
# Example:
# number = 45
#
# Output:
# Divisible by 5

# Your code here


# ==========================================================
# Intermediate Practice
# ==========================================================

# Q6. Find the largest of two numbers.
#
# Example:
# num1 = 45
# num2 = 32
#
# Output:
# 45 is Larger

# Your code here


# ==========================================================

# Q7. Find the smallest of two numbers.
#
# Example:
# num1 = 45
# num2 = 32
#
# Output:
# 32 is Smaller

# Your code here


# ==========================================================

# Q8. Create a Grade Calculator.
#
# Marks:
# 90+  -> Grade A
# 75+  -> Grade B
# 60+  -> Grade C
# 35+  -> Grade D
# else -> Fail

# Your code here


# ==========================================================

# Q9. Create a Traffic Signal Program.
#
# Red    -> Stop
# Yellow -> Get Ready
# Green  -> Go

# Your code here


# ==========================================================

# Q10. Check whether a person is eligible for a driving license.
#
# Condition:
# Age >= 18

# Your code here


# ==========================================================
# Output Prediction
# ==========================================================

# Q11. Predict the output.

age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Your Answer:
# __________________


# ==========================================================

# Q12. Predict the output.

number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Your Answer:
# __________________


# ==========================================================

# Q13. Predict the output.

marks = 65

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

# Your Answer:
# __________________


# ==========================================================

# Q14. Predict the output.

x = 10

if x > 20:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")

# Your Answer:
# __________________


# ==========================================================

# Q15. Predict the output.

age = 22
citizen = False

if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Citizen Required")

# Your Answer:
# __________________


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What is a conditional statement?


# ==========================================================

# Q17. What is the purpose of the if statement?


# ==========================================================

# Q18. What is the difference between if and if-else?


# ==========================================================

# Q19. When should you use if-elif-else?


# ==========================================================

# Q20. What is a Nested if statement?


# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Write a program to check whether a person is:
#
# - Child (0-12)
# - Teenager (13-19)
# - Adult (20-59)
# - Senior Citizen (60+)
#
# Input:
# age = 25
#
# Output:
# Adult


# ==========================================================

# Challenge 2
#
# Create a Login System.
#
# username = "admin"
# password = "python123"
#
# If both are correct:
# Login Successful
#
# Otherwise:
# Invalid Credentials


# ==========================================================

# Challenge 3
#
# Write a Discount Calculator.
#
# Purchase Amount:
#
# >= 5000  -> 20% Discount
# >= 3000  -> 10% Discount
# Otherwise -> No Discount


# ==========================================================

# Challenge 4
#
# Create an ATM Withdrawal Program.
#
# Balance = 10000
#
# Check:
# - Withdrawal amount must be greater than 0.
# - Balance should be sufficient.
#
# Display the appropriate message.


# ==========================================================

# Challenge 5
#
# Data Engineering Challenge
#
# A dataset contains:
#
# total_records = 5000
# missing_records = 12
#
# Write a program to:
#
# - Print "Dataset Ready" if there are no missing records.
# - Otherwise print "Data Cleaning Required".


# ==========================================================

print("\n🎉 Congratulations! You have completed Day 05 Practice.")