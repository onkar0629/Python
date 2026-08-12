"""
==========================================================
Day 09 : Loop Control Statements
Topic  : Practice Questions

Description:
This file contains practice questions to help reinforce
the concepts covered in Day 09.

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

# Q1. Print numbers from 1 to 10.
# Stop the loop when the number becomes 6 using break.

# Your code here


# ==========================================================

# Q2. Print numbers from 1 to 10.
# Skip printing the number 5 using continue.

# Your code here


# ==========================================================

# Q3. Write a loop that prints numbers from 1 to 5.
# Use pass when the number is 3.

# Your code here


# ==========================================================

# Q4. Use a for loop with an else block.
# Print numbers from 1 to 5 and then display:
#
# Loop Finished Successfully

# Your code here


# ==========================================================

# Q5. Use a while loop to print numbers from 1 to 10.
# Stop when the number reaches 7.

# Your code here


# ==========================================================
# Intermediate Practice
# ==========================================================

# Q6. Print all odd numbers from 1 to 20.
# Use continue to skip even numbers.

# Your code here


# ==========================================================

# Q7. Search for the number 15 in the list below.
#
# numbers = [4, 8, 10, 15, 18, 20]
#
# If found, display:
#
# Number Found
#
# Otherwise display:
#
# Number Not Found
#
# (Hint: Use break and else.)

# Your code here


# ==========================================================

# Q8. Keep asking the user to enter "yes".
# Stop only when the correct input is entered.

# Your code here


# ==========================================================

# Q9. Print the multiplication table of 7.
# Stop printing after reaching 7 × 5.

# Your code here


# ==========================================================

# Q10. Print numbers from 1 to 20.
# Skip all multiples of 3.

# Your code here


# ==========================================================
# Output Prediction
# ==========================================================

# Q11. Predict the output.

for i in range(5):
    if i == 2:
        break
    print(i)

# Your Answer:
# __________________


# ==========================================================

# Q12. Predict the output.

for i in range(1, 6):
    if i == 4:
        continue
    print(i)

# Your Answer:
# __________________


# ==========================================================

# Q13. Predict the output.

for i in range(3):
    pass
    print(i)

# Your Answer:
# __________________


# ==========================================================

# Q14. Predict the output.

for i in range(3):
    print(i)
else:
    print("Done")

# Your Answer:
# __________________


# ==========================================================

# Q15. Predict the output.

for i in range(5):

    if i == 3:
        break

    print(i)

else:
    print("Completed")

# Your Answer:
# __________________


# ==========================================================
# Concept Questions
# ==========================================================

# Q16. What is the purpose of the break statement?


# ==========================================================

# Q17. What is the difference between break and continue?


# ==========================================================

# Q18. What does the pass statement do?


# ==========================================================

# Q19. When is the else block of a loop executed?


# ==========================================================

# Q20. Can break terminate both inner and outer loops at once?
# Explain your answer.


# ==========================================================
# Coding Challenges
# ==========================================================

# Challenge 1
#
# Create a number guessing game.
#
# Secret Number = 8
#
# Keep asking the user until the correct number is entered.
#
# Display:
# Correct Guess!


# ==========================================================

# Challenge 2
#
# Print numbers from 1 to 50.
#
# Skip every multiple of 5 using continue.


# ==========================================================

# Challenge 3
#
# Search for a student's name in a list.
#
# students = ["Aman", "Priya", "Rahul", "Sneha", "Rohan"]
#
# If found:
# Student Found
#
# Otherwise:
# Student Not Found
#
# (Hint: Use for-else.)


# ==========================================================

# Challenge 4
#
# Data Validation
#
# records = [1001, 1002, None, 1004, None, 1006]
#
# Skip invalid records (None) and process only valid ones.
#
# Expected Output:
#
# Processing Record: 1001
# Processing Record: 1002
# Processing Record: 1004
# Processing Record: 1006


# ==========================================================

# Challenge 5
#
# Data Engineering Challenge
#
# Simulate a data pipeline processing batches.
#
# batches = ["Batch-1", "Batch-2", "ERROR", "Batch-4"]
#
# Process each batch.
#
# If "ERROR" is encountered:
# - Display "Pipeline Stopped!"
# - Exit the loop immediately using break.
#
# Otherwise:
# - Display "Processing <batch>"

# ==========================================================

print("\n🎉 Congratulations! You have completed Day 09 Practice.")