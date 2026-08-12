"""
==========================================================
Day 05 : Conditional Statements
Topic  : Practice Questions with Answers

Description:
This file contains practice questions and  to help reinforce
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

age = int(input("What is your age? "))

if age >= 18:
    print("Eligible to Vote")

# ==========================================================

# Q2. Check whether a number is positive.
#
# Example:
# number = 15
#
# Output:
# Positive Number

num = int(input("What is your number? "))

if num > 0:
    print("Positive Number")

# ==========================================================

# Q3. Check whether a number is even or odd.
#
# Example:
# number = 19
#
# Output:
# Odd Number

num = int(input("What is your number? "))
if num % 2 != 0:
    print("Odd Number")

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

marks = int(input("What is your marks? "))
if marks >= 35:
    print("Pass")

# ==========================================================

# Q5. Check whether a number is divisible by 5.
#
# Example:
# number = 45
#
# Output:
# Divisible by 5

num = int(input("What is your number? "))
if num / 5 :
    print("Divisible by 5")

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

num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

# ==========================================================

# Q7. Find the smallest of two numbers.
#
# Example:
# num1 = 45
# num2 = 32
#
# Output:
# 32 is Smaller

num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))

if num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num2} is smaller than {num1}")

# ==========================================================

# Q8. Create a Grade Calculator.
#
# Marks:
# 90+  -> Grade A
# 75+  -> Grade B
# 60+  -> Grade C
# 35+  -> Grade D
# else -> Fail

marks = int(input("What is your marks? "))

if marks >= 90:
    print("Pass With Grade A")
elif marks >= 75:
    print("Pass With Grade B")
elif marks >= 60:
    print("Pass With Grade C")
elif marks >= 35:
    print("Pass With Grade D")
else:
    print("Fail")

# ==========================================================

# Q9. Create a Traffic Signal Program.
#
# Red    -> Stop
# Yellow -> Get Ready
# Green  -> Go

signal_colour = input("Enter signal colour (Red/Yellow/Green): ").lower()

if signal_colour == "red":
    print("Stop")
elif signal_colour == "yellow":
    print("Get Ready")
elif signal_colour == "green":
    print("Go")
else:
    print("Invalid Signal Colour")

# ==========================================================

# Q10. Check whether a person is eligible for a driving license.
#
# Condition:
# Age >= 18

age = int(input("What is your age? "))
if age >= 18:
    print("Eligible for driving licenses")
else:
    print("Not Eligible for driving licenses")

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
# Not Eligible

# ==========================================================

# Q12. Predict the output.

number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Your Answer:
#Even

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
# C


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
# B


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
# Citizen Required


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What is a conditional statement?

# A conditional statement executes different code
# depending on whether a condition is True or False.

# ==========================================================

# Q17. What is the purpose of the if statement?

# The if statement checks a condition.
# If the condition is True, it executes the code inside the if block.

# ==========================================================

# Q18. What is the difference between if and if-else?

# if is used when we want to execute code only when
# a condition is True.

# if-else is used when we want one block to execute
# when the condition is True and another when it is False.

# ==========================================================

# Q19. When should you use if-elif-else?

# if-elif-else is used when we need to check
# multiple conditions and execute code based on
# the first condition that is True.

# ==========================================================

# Q20. What is a Nested if statement?

# A nested if is an if statement inside another if statement.
# It is used when a second condition should be checked
# only after the first condition is True.

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

age = int(input("What is your age? "))

if age >= 0:
    if age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior Citizen")
else:
    print("Please enter a valid age")

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

user_name = input("Enter your user name: ")
password = input("Enter your password: ")

if user_name == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Login Failed")

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

purchase_amount = int(input("Enter purchase amount: "))

if purchase_amount >= 5000:
    print("20% Discount")
elif purchase_amount >= 3000:
    print("10% Discount")
else:
    print("No Discount")

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

balance = 10000
withdrawal_amount = int(input("Enter withdrawal amount: "))
remaining_amount = balance - withdrawal_amount

if withdrawal_amount <= 0:
    print("Invalid withdrawal amount")
elif withdrawal_amount <= balance:
    print(f"Remaining amount: {remaining_amount}")
else:
    print("Insufficient balance")

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

records = int(input("Enter number of records: "))
missing_records = int(input("Enter missing records: "))

if missing_records == 0:
    print("Dataset Ready")
else:
    print("Data Cleaning Required")

# ==========================================================

print("\n🎉 Congratulations! You have completed Day 05 Practice.")