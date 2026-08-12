"""
==========================================================
Day 06 : Multiple if Statements and Nested if Statements
Topic  : Examples

Description:
This file contains runnable examples demonstrating the
concepts covered in Day 06.

Topics Covered:
1. Multiple if Statements
2. Nested if Statements
3. Real-World Examples
==========================================================
"""

# ==========================================================
# 1. Multiple if Statements
# ==========================================================

print("========== Multiple if Statements ==========\n")

number = 12

if number > 0:
    print("Positive Number")

if number % 2 == 0:
    print("Even Number")

if number < 100:
    print("Less than 100")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Student Eligibility
# ==========================================================

age = 20
marks = 82

if age >= 18:
    print("Eligible by Age")

if marks >= 35:
    print("Passed the Exam")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Employee Eligibility
# ==========================================================

experience = 3
salary = 40000

if experience >= 2:
    print("Experience Requirement Met")

if salary >= 30000:
    print("Salary Requirement Met")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. Nested if Statement
# ==========================================================

print("========== Nested if Statement ==========\n")

age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Citizenship Required")
else:
    print("Not Eligible")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - ATM Withdrawal
# ==========================================================

balance = 10000
withdraw_amount = 3000

if balance >= withdraw_amount:
    if withdraw_amount > 0:
        print("Transaction Successful")
    else:
        print("Enter a Valid Withdrawal Amount")
else:
    print("Insufficient Balance")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Login System
# ==========================================================

username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Scholarship Eligibility
# ==========================================================

marks = 88
attendance = 90

if marks >= 85:
    if attendance >= 75:
        print("Scholarship Approved")
    else:
        print("Attendance Requirement Not Met")
else:
    print("Marks Requirement Not Met")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Real-World Example - Data Validation
# ==========================================================

print("========== Data Validation ==========\n")

file_exists = True
total_records = 1500
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

print("\n" + "=" * 50)

print("\nEnd of Day 06 Examples 🚀")