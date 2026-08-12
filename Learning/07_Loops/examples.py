"""
==========================================================
Day 07 : Loops
Topic  : Examples

Description:
This file contains runnable examples demonstrating the
concepts covered in Day 07.

Topics Covered:
1. for Loop
2. range() Function
3. range(start, stop)
4. range(start, stop, step)
5. Practical Examples
==========================================================
"""

# ==========================================================
# 1. Basic for Loop
# ==========================================================

print("========== Basic for Loop ==========\n")

for i in range(5):
    print(i)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. Print Numbers from 1 to 10
# ==========================================================

print("========== Numbers from 1 to 10 ==========\n")

for number in range(1, 11):
    print(number)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 3. Print Even Numbers
# ==========================================================

print("========== Even Numbers ==========\n")

for number in range(2, 21, 2):
    print(number)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 4. Print Odd Numbers
# ==========================================================

print("========== Odd Numbers ==========\n")

for number in range(1, 20, 2):
    print(number)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 5. Countdown
# ==========================================================

print("========== Countdown ==========\n")

for number in range(10, 0, -1):
    print(number)

print("Blast Off! 🚀")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 6. Multiplication Table
# ==========================================================

print("========== Multiplication Table of 5 ==========\n")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 7. Calculate Sum of Numbers
# ==========================================================

print("========== Sum of Numbers ==========\n")

total = 0

for number in range(1, 6):
    total += number

print("Sum =", total)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 8. Iterate Through a String
# ==========================================================

print("========== Iterate Through String ==========\n")

name = "Python"

for letter in name:
    print(letter)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 9. Iterate Through a List
# ==========================================================

print("========== Iterate Through List ==========\n")

courses = ["Python", "SQL", "Azure", "Spark"]

for course in courses:
    print(course)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 10. Real-World Example - Process Dataset
# ==========================================================

print("========== Dataset Processing ==========\n")

records = ["Record-1", "Record-2", "Record-3", "Record-4"]

for record in records:
    print(f"Processing {record}")

print("\nDataset Processed Successfully!")

print("\n" + "=" * 50)

print("\nEnd of Day 07 Examples 🚀")