"""
==========================================================
Day 08 : while Loop
Topic  : Practice Questions Answer

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 08.

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

# Q1. Print numbers from 1 to 10 using a while loop.

number = 1
while number <= 10:
    print(number)
    number += 1

# ==========================================================

# Q2. Print numbers from 10 to 1 using a while loop.

number = 10
while number >= 1:
    print(number)
    number -= 1

# ==========================================================

# Q3. Print all even numbers from 2 to 20.

number = 2
while number <= 20:
    print(number)
    number += 2

# ==========================================================

number = 2

while number <= 20:
    if number % 2 == 0:
        print(number)
    number += 2

# ==========================================================

# Q4. Print all odd numbers from 1 to 19.

number = 1
while number <= 19:
    if number % 2 != 0:
        print(number)
    number += 1

# ==========================================================

number = 1
while number <= 19:
    print(number)
    number += 2

# ==========================================================

# Q5. Print your name 5 times using a while loop.

count = 1

while count <= 5:
    print("Onkar")
    count += 1

# ==========================================================
# Intermediate Practice
# ==========================================================

# Q6. Print the multiplication table of 8.

# Expected Output:
#
# 8 x 1 = 8
# ...
# 8 x 10 = 80

number = 8
i = 1
while i <= 10:
    print(f"{number} * {i} = {number * i}")
    i += 1

# ==========================================================

# Q7. Find the sum of numbers from 1 to 100.

# Expected Output:
# Sum = 5050

total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

# ==========================================================

# Q8. Find the sum of all odd numbers from 1 to 50.

total = 0
i = 1
while i <= 50:
    if i % 2 != 0:
        total += i
    i += 1

print(total)

# ==========================================================

total = 0
i = 1

while i <= 50:
    total += i
    i += 2

print(total)

# ==========================================================

# Q9. Display the following pattern.
#
# *
# **
# ***
# ****
# *****

star = "*"
i = 1
while i <= 5:
    print("*" * i)
    i += 1

# ==========================================================

# Q10. Keep asking the user to enter the correct password.
#
# Password = "python123"
#
# Display "Access Granted!" once the correct password is entered.

password = "python123"

user_password = ""

while user_password != password:
    user_password = input("Enter password: ")

print("Access Granted!")

# ==========================================================
# Output Prediction
# ==========================================================

# Q11. Predict the output.

count = 1

while count <= 3:
    print(count)
    count += 1

# Your Answer:
# __________________


# ==========================================================

# Q12. Predict the output.

number = 2

while number <= 6:
    print(number)
    number += 2

# Your Answer:
# __________________


# ==========================================================

# Q13. Predict the output.

i = 5

while i >= 1:
    print(i)
    i -= 2

# Your Answer:
# __________________


# ==========================================================

# Q14. Predict the output.

total = 0
i = 1

while i <= 3:
    total += i
    i += 1

print(total)

# Your Answer:
# __________________


# ==========================================================

# Q15. Predict the output.

count = 5

while count < 5:
    print(count)
    count += 1

print("Done")

# Your Answer:
# __________________


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What is a while loop?

# A while loop executes a block of code repeatedly as long as the specified condition
# remains True. It is mainly used when the number of iterations is not known beforehand.

# ==========================================================

# Q17. What is the difference between a for loop and a while loop?

# while loop is executes a block of code repeatedly as long as the condition is met.
# for loop is executed repeatedly as long as the condition is true

# ==========================================================

# Q18. What is an infinite loop?


# ==========================================================

# Q19. Why is it important to update the loop variable?


# ==========================================================

# Q20. When should you use a while loop instead of a for loop?


# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Print the multiplication tables from 1 to 10
# using only while loops.

table = 1

while table <= 10:
    i = 1

    while i <= 10:
        print(f"{table} x {i} = {table * i}")
        i += 1

    print()
    table += 1

# ==========================================================

# Challenge 2
#
# Reverse Countdown
#
# Print numbers from 20 to 1 using a while loop.

i = 20
while i >= 1:
    print(i)
    i -= 1

# ==========================================================

# Challenge 3
#
# Create a simple ATM PIN verification system.
#
# Correct PIN = 1234
#
# Keep asking the user until the correct PIN is entered.
# Then display:
#
# Access Granted!

correct_pin = 1234

pin = int(input("Enter PIN: "))

while pin != correct_pin:
    print("Incorrect PIN. Try Again!")
    pin = int(input("Enter PIN: "))

print("Access Granted!")

# ==========================================================

# Challenge 4
#
# Count the number of digits in a given number.
#
# Example:
#
# Input:
# 45879
#
# Output:
# Total Digits = 5

number = int(input("Enter a number: "))

count = 0

while number > 0:
    number = number // 10
    count += 1

print("Total Digits =", count)

# ==========================================================

# Challenge 5
#
# Data Engineering Challenge
#
# A data pipeline has 5 batches remaining.
#
# Use a while loop to process each batch.
#
# Expected Output:
#
# Processing Batch 1
# Processing Batch 2
# ...
# Processing Batch 5
#
# Finally display:
#
# All batches processed successfully!

batch = 1

while batch <= 10:
    print(f"Processing Batch {batch}")
    batch += 1

print("All batches processed successfully!")

# ==========================================================

print("\n🎉 Congratulations! You have completed Day 08 Practice.")