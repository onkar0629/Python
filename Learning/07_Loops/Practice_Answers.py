"""
==========================================================
Day 07 : Loops
Topic  : Practice Questions

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 07.

Instructions:
- Solve each question before referring to examples.py.
- Write clean and readable code.
- Run your program to verify the output.
- Experiment with different inputs whenever possible.
==========================================================
"""
from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
from itertools import count

# ==========================================================
# Basic Practice
# ==========================================================

# Q1. Print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

# ==========================================================

# Q2. Print numbers from 10 to 1 in reverse order.

for i in range(10,0,-1):
    print(i)

# ==========================================================

# Q3. Print all even numbers from 2 to 20.

for i in range(2,20):
    if i % 2 == 0:
        print(i)

# ==========================================================

# Q4. Print all odd numbers from 1 to 19.

for i in range(1,19):
    if i % 3 == 0:
        print(i)

# ==========================================================

# Q5. Print your name 5 times using a loop.

for i in range(5):
    print("Onkar")

# ==========================================================
# Intermediate Practice
# ==========================================================

# Q6. Print the multiplication table of 7.

# Expected Output:
#
# 7 x 1 = 7
# ...
# 7 x 10 = 70

for i in range(1 , 11):
    a = i * 7
    print(f"7 * {i} = {a}")

# ==========================================================

# Q7. Find the sum of numbers from 1 to 100.

# Expected Output:
# Sum = 5050

total = 0

for i in range(1, 101):
    total += i
print("Sum =", total)


# ==========================================================

# Q8. Find the sum of all even numbers from 1 to 50.

total = 0
for i in range(1,51):
    if i % 2 == 0:
         total += i
print(f"sum = {total}")

# ==========================================================

# Q9. Print each character of the string below using a loop.
#
# language = "Python"

language = "PYTHON"

for a in language:
    print(a)

# ==========================================================

# Q10. Print each course from the list below.
#
courses = ["Python", "SQL", "Azure", "Spark"]

for course in courses:
    print(course)

# ==========================================================
# Output Prediction
# ==========================================================

# Q11. Predict the output.

for i in range(5):
    print(i)

# Your Answer:
# __________________


# ==========================================================

# Q12. Predict the output.

for i in range(2, 11, 2):
    print(i)

# Your Answer:
# __________________


# ==========================================================

# Q13. Predict the output.

total = 0

for i in range(1, 4):
    total += i

print(total)

# Your Answer:
# __________________


# ==========================================================

# Q14. Predict the output.

for letter in "SQL":
    print(letter)

# Your Answer:
# __________________


# ==========================================================

# Q15. Predict the output.

for i in range(5, 0, -2):
    print(i)

# Your Answer:
# __________________


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What is a loop?
# A loop is a programming construct used to execute the same block of code multiple times.

# ==========================================================

# Q17. What is the purpose of the for loop?
# A for loop is used to iterate over a sequence or collection and execute the same block
# of code for each item. It automates repetitive tasks and improves code readability by
# avoiding repeated code.

# ==========================================================

# Q18. What does range(5) return?
#range(5) returns a range object that represents the sequence of numbers 0, 1, 2, 3, 4.

# ==========================================================

# Q19. Explain the difference between:
#
# range(5)
# range(1, 6)
# range(2, 11, 2)

#range 5 will return 0,1,2,3,4,
# range(1, 6) will return 1,2,3,4,5
# range(2, 11, 2) will return 2,4,6,8,10

# ==========================================================

# Q20. Why are loops important in programming?


# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Print the multiplication tables from 1 to 10.
#
# Example:
#
# 1 x 1 = 1
# ...
# 10 x 10 = 100

for i in range(1,11):
    a = i * i
    print(f"{i} * {i} = {a}")

# ==========================================================

# Challenge 2
#
# Count how many numbers between 1 and 100 are divisible by 3.

count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count += 1

print(count)

# ==========================================================

# Challenge 3
#
# Print the square of every number from 1 to 20.
#
# Example:
# 1 -> 1
# 2 -> 4
# ...
# 20 -> 400

for i in range(1, 21):
    a = i * i
    print(a)

# ==========================================================

# Challenge 4
#
# Given the following list:
#
# marks = [85, 72, 91, 64, 58]
#
# Print each mark and display whether it is Pass or Fail.
#
# Passing Marks = 35

marks = [85, 72, 91, 64, 58]

for i in marks:
    if i >= 35:
        print(f"Pass Marks : {i}")
    else:
        print(f"Fail Marks : {i}")


# ==========================================================

# Challenge 5
#
# Data Engineering Challenge
#
# A dataset contains the following records:
#
# records = [
#     "Record-1",
#     "Record-2",
#     "Record-3",
#     "Record-4",
#     "Record-5"
# ]
#
# Write a program to process each record one by one and print:
#
# Processing Record-1
# Processing Record-2
# ...
#
# Finally print:
#
# Dataset Processed Successfully!

records = [
    "Record-1",
    "Record-2",
    "Record-3",
    "Record-4",
    "Record-5"
]

for i in records:
    print(f"Processing : {i}")

print("Dataset Processed Successfully!")


# ==========================================================

print("\n🎉 Congratulations! You have completed Day 07 Practice.")