"""
==========================================================
Day 08 : while Loop
Topic  : Examples

Description:
This file contains runnable examples demonstrating the
concepts covered in Day 08.

Topics Covered:
1. Basic while Loop
2. Counter-Controlled while Loop
3. Print Even Numbers
4. Print Odd Numbers
5. Multiplication Table
6. Sum of Numbers
7. User Input with while Loop
8. Infinite Loop (Example)
9. Real-World Example
==========================================================
"""

# ==========================================================
# 1. Basic while Loop
# ==========================================================

print("========== Basic while Loop ==========\n")

count = 1

while count <= 5:
    print(count)
    count += 1

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. Print Numbers from 1 to 10
# ==========================================================

print("========== Numbers from 1 to 10 ==========\n")

number = 1

while number <= 10:
    print(number)
    number += 1

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 3. Print Even Numbers
# ==========================================================

print("========== Even Numbers ==========\n")

number = 2

while number <= 20:
    print(number)
    number += 2

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 4. Print Odd Numbers
# ==========================================================

print("========== Odd Numbers ==========\n")

number = 1

while number <= 19:
    print(number)
    number += 2

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 5. Countdown
# ==========================================================

print("========== Countdown ==========\n")

count = 10

while count >= 1:
    print(count)
    count -= 1

print("Blast Off! 🚀")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 6. Multiplication Table
# ==========================================================

print("========== Multiplication Table of 5 ==========\n")

table = 5
i = 1

while i <= 10:
    print(f"{table} x {i} = {table * i}")
    i += 1

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 7. Sum of Numbers
# ==========================================================

print("========== Sum of Numbers ==========\n")

i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Sum =", total)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 8. User Input Example
# ==========================================================

print("========== User Input Validation ==========\n")

password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted!")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 9. Infinite Loop Example
# ==========================================================

print("========== Infinite Loop Example ==========\n")

print("Example only (commented to avoid infinite execution).")

"""
while True:
    print("This loop runs forever!")
"""

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 10. Real-World Example - Process Records
# ==========================================================

print("========== Dataset Processing ==========\n")

records_remaining = 5

while records_remaining > 0:
    print(f"Processing Record {records_remaining}")
    records_remaining -= 1

print("\nDataset Processed Successfully!")

print("\n" + "=" * 50)

print("\nEnd of Day 08 Examples 🚀")