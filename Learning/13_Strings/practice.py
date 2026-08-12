# 🐍 Day 13 - Strings | Practice

# ============================================================
# Practice Instructions
# ============================================================
# Try to solve each problem yourself before checking any solution.
# Do not use advanced methods unless the question asks for them.
# Focus on understanding string indexing, slicing, methods,
# traversal, formatting, and immutability.


# ============================================================
# Level 1 - String Basics
# ============================================================

# Question 1
# Create a variable named `name` containing your name.
# Print the value.


# Question 2
# Create the string:
# "Data Engineer"
# Print its length.


# Question 3
# Given:
text = "Python"
# Print the first character and the last character.


# Question 4
# Given:
text = "Python"
# Print the characters at index 1, 3, and 5.


# Question 5
# Given:
text = "Python"
# Print the string using negative indexing to get:
# y, h, n


# ============================================================
# Level 2 - Slicing
# ============================================================

# Question 6
# Given:
text = "Python"
# Print:
# Pyt


# Question 7
# Given:
text = "Python Programming"
# Extract only "Python" using slicing.


# Question 8
# Given:
text = "Python"
# Reverse the string using slicing.


# Question 9
# Given:
text = "DataEngineering"
# Extract every second character.


# Question 10
# Given:
text = "Python"
# Print the string from index 1 up to, but not including, index 5.


# ============================================================
# Level 3 - String Operators
# ============================================================

# Question 11
# Given:
first_name = "Onkar"
last_name = "Jadhav"
# Combine them into:
# "Onkar Jadhav"


# Question 12
# Print "Python" five times using the repetition operator.


# Question 13
# Check whether "SQL" exists inside:
text = "SQL and Python are important for Data Engineering"
# Print True or False.


# Question 14
# Check whether the word "Java" does NOT exist in the same string.


# ============================================================
# Level 4 - String Methods
# ============================================================

# Question 15
# Convert the following string to lowercase:
text = "PYTHON DATA ENGINEERING"


# Question 16
# Convert the following string to title case:
text = "python for data engineering"


# Question 17
# Remove leading and trailing spaces:
text = "   Data Engineer   "


# Question 18
# Replace "Python" with "SQL":
text = "Python is important for Data Engineering"


# Question 19
# Count how many times "a" occurs:
text = "Data Analytics and Data Engineering"


# Question 20
# Check whether this string starts with "Data":
text = "Data Engineering"


# Question 21
# Check whether this string ends with "Engineering":
text = "Data Engineering"


# ============================================================
# Level 5 - split() and join()
# ============================================================

# Question 22
# Split this sentence into individual words:
text = "Python SQL Hadoop Snowflake"


# Question 23
# Given:
words = ["Python", "SQL", "Snowflake"]
# Join them using " | " as the separator.
# Expected:
# Python | SQL | Snowflake


# Question 24
# Given:
text = "data,engineering,python,sql"
# Convert it into a list using split().


# ============================================================
# Level 6 - find(), index(), and count()
# ============================================================

# Question 25
# Find the position of "Python":
text = "I am learning Python for Data Engineering"


# Question 26
# Find how many times "Data" occurs:
text = "Data Engineering uses Data pipelines to process Data"


# Question 27
# What is the difference between find() and index()?
# Demonstrate the difference when the searched text does not exist.


# ============================================================
# Level 7 - String Formatting
# ============================================================

# Question 28
# Given:
name = "Onkar"
role = "Data Engineer"
# Print:
# My name is Onkar and I am preparing for Data Engineer interviews.
# Use an f-string.


# Question 29
# Given:
age = 22
# Print the value using an f-string:
# I am 22 years old.


# Question 30
# Given:
project = "Data Engineering Journey"
status = "In Progress"
# Create a formatted sentence using an f-string.


# ============================================================
# Level 8 - String Traversal
# ============================================================

# Question 31
# Print every character of:
text = "Python"
# using a for loop.


# Question 32
# Count the number of vowels in:
text = "Data Engineering"


# Question 33
# Count the number of consonants in:
text = "Python Programming"
# Ignore spaces.


# Question 34
# Count the number of digits in:
text = "Data2026Engineering123"


# ============================================================
# Level 9 - Interview-Style Problems
# ============================================================

# Question 35
# Reverse a string WITHOUT using slicing.
# Example:
# Input:  Python
# Output: nohtyP


# Question 36
# Check whether a string is a palindrome.
# Example:
# madam -> True
# python -> False


# Question 37
# Find the first non-repeating character in a string.
# Example:
# Input: swiss
# Output: w


# Question 38
# Remove all spaces from a string.
# Example:
# Input: "Data Engineer"
# Output: "DataEngineer"


# Question 39
# Find the longest word in a sentence.
# Example:
# Input: "Python is powerful"
# Output: powerful


# Question 40
# Count the frequency of each character in a string.
# Example:
# Input: "hello"
# Output:
# h -> 1
# e -> 1
# l -> 2
# o -> 1


# ============================================================
# Level 10 - Data Engineering Scenarios
# ============================================================

# Question 41
# A CSV field contains:
# "  Onkar Jadhav  "
# Clean the value so that leading/trailing spaces are removed.


# Question 42
# A pipeline receives this value:
# "PUNE|MAHARASHTRA|INDIA"
# Split it into three separate values.


# Question 43
# A source system sends:
# "ONKAR.JADHAV@EXAMPLE.COM"
# Convert the email address to lowercase.


# Question 44
# Given:
filename = "customer_data_2026.csv"
# Check whether the file is a CSV file using a string method.


# Question 45
# A data source contains:
# "Python,SQL,Hadoop,Snowflake"
# Convert this string into a list of technologies.


# ============================================================
# Interview Challenge
# ============================================================

# Question 46
# Given:
text = "Python SQL Python Hadoop SQL Python"
# Find the most frequently occurring word.
# Expected output:
# Python
#
# Try to solve this using only concepts learned so far.


# Question 47
# Given:
email = "  ONKAR.JADHAV@EXAMPLE.COM  "
# Clean the email and convert it to lowercase.
# Expected:
# onkar.jadhav@example.com


# Question 48
# Given:
text = "Data Engineering"
# Create a new string containing only the vowels.
# Expected:
# a a E e i
#
# Preserve the original order.


# ============================================================
# Final Challenge
# ============================================================

# Question 49
# Write a program that accepts a sentence and prints:
# 1. Number of characters
# 2. Number of words
# 3. Number of vowels
# 4. Number of digits
# 5. The sentence in reverse
#
# Example input:
# "Python 3 is powerful"


# Question 50
# Build a simple username cleaner.
# Input may contain:
# "  ONKAR_JADHAV  "
#
# Your program should:
# 1. Remove leading/trailing spaces.
# 2. Convert the username to lowercase.
# 3. Replace spaces with underscores if any exist.
# 4. Print the cleaned username.
#
# Example:
# "  Onkar Jadhav  "
# Output:
# "onkar_jadhav"
