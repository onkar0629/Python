"""
==========================================================
Day 05 : Conditional Statements
Topic  : Examples

Description:
This file contains runnable examples demonstrating the
concepts covered in Day 05.

Topics Covered:
1. if Statement
2. if-else Statement
3. if-elif-else Statement
4. Nested if Statement
==========================================================
"""

# ==========================================================
# 1. if Statement
# ==========================================================

print("========== if Statement ==========\n")

age = 20

if age >= 18:
    print("Eligible to Vote")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Check Even Number
# ==========================================================

number = 18

if number % 2 == 0:
    print(number, "is an Even Number")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Positive Number
# ==========================================================

number = 25

if number > 0:
    print(number, "is a Positive Number")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. if-else Statement
# ==========================================================

print("========== if-else Statement ==========\n")

age = 16

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Even or Odd
# ==========================================================

number = 17

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Positive or Negative
# ==========================================================

number = -12

if number >= 0:
    print(number, "is Positive")
else:
    print(number, "is Negative")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 3. if-elif-else Statement
# ==========================================================

print("========== if-elif-else Statement ==========\n")

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Traffic Signal
# ==========================================================

signal = "Yellow"

if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Get Ready")
elif signal == "Green":
    print("Go")
else:
    print("Invalid Signal")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Example - Largest of Two Numbers
# ==========================================================

num1 = 25
num2 = 40

if num1 > num2:
    print(num1, "is Larger")
else:
    print(num2, "is Larger")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 4. Nested if Statement
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
        print("Enter a Valid Amount")
else:
    print("Insufficient Balance")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# Real-World Example - Data Validation
# ==========================================================

print("========== Data Validation ==========\n")

records = 1500
missing_records = 0

if records > 0:
    if missing_records == 0:
        print("Data Validation Passed")
    else:
        print("Missing Records Found")
else:
    print("Dataset is Empty")

print("\n" + "=" * 50)

print("\nEnd of Day 05 Examples 🚀")