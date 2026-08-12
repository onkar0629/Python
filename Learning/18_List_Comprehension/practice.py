# 🐍 Day 18 - List Comprehension | Practice

# Solve each problem yourself before checking the README.

# ============================================================
# Practice 1 - Squares
# ============================================================
# Create a list containing the squares of numbers from 1 to 10.


# ============================================================
# Practice 2 - Double Values
# ============================================================
# Given the list below, create a new list where every value is doubled.

numbers = [2, 4, 6, 8, 10]


# ============================================================
# Practice 3 - Even Numbers
# ============================================================
# Create a list containing only the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# ============================================================
# Practice 4 - Odd Numbers
# ============================================================
# Create a list containing only the odd numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# ============================================================
# Practice 5 - Positive Numbers
# ============================================================
# Keep only positive numbers.

numbers = [-5, -2, 0, 3, 7, -1, 10]


# ============================================================
# Practice 6 - Positive Squares
# ============================================================
# Keep only positive numbers and return their squares.

numbers = [-3, -2, -1, 0, 1, 2, 3]


# ============================================================
# Practice 7 - Uppercase Strings
# ============================================================
# Convert every string to uppercase.

words = ["python", "sql", "snowflake", "spark"]


# ============================================================
# Practice 8 - Long Words
# ============================================================
# Keep only words whose length is greater than 4.

words = ["sql", "python", "spark", "data", "snowflake"]


# ============================================================
# Practice 9 - Convert Strings to Integers
# ============================================================
# Convert every string number into an integer.

values = ["10", "20", "30", "40"]


# ============================================================
# Practice 10 - Conditional Labels
# ============================================================
# Return "even" for even numbers and "odd" for odd numbers.

numbers = [1, 2, 3, 4, 5, 6]


# ============================================================
# Practice 11 - Extract Vowels
# ============================================================
# Extract all vowels from the string.

text = "dataengineering"


# ============================================================
# Practice 12 - Remove Empty Strings
# ============================================================
# Remove empty strings from the list.

values = ["python", "", "sql", "", "snowflake"]


# ============================================================
# Practice 13 - Nested Loop
# ============================================================
# Create all combinations between the numbers and letters.

numbers = [1, 2, 3]
letters = ["A", "B"]

# Expected structure:
# [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]


# ============================================================
# Practice 14 - Flatten a Matrix
# ============================================================
# Convert the nested list into a single list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# ============================================================
# Practice 15 - Dictionary Keys
# ============================================================
# Create a list containing all keys from the dictionary.

student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 16 - Dictionary Values
# ============================================================
# Create a list containing all values from the dictionary.

student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 17 - Function Transformation
# ============================================================
# Create a function called cube(number) that returns number ** 3.
# Use a list comprehension to create cubes for the values below.

numbers = [1, 2, 3, 4, 5]


# ============================================================
# Practice 18 - Data Engineering Scenario
# ============================================================
# Clean these customer names by:
# 1. Removing surrounding whitespace.
# 2. Converting them to title case.

names = [" onkar jadhav ", " rahul patil ", " amit sharma "]


# ============================================================
# Practice 19 - Data Engineering Scenario
# ============================================================
# From the records below, create a list containing only active records.

records = [
    {"id": 101, "status": "active"},
    {"id": 102, "status": "inactive"},
    {"id": 103, "status": "active"},
    {"id": 104, "status": "inactive"}
]


# ============================================================
# Practice 20 - Data Engineering Scenario
# ============================================================
# Extract only customer IDs from the records.

records = [
    {"id": 101, "name": "Onkar"},
    {"id": 102, "name": "Rahul"},
    {"id": 103, "name": "Amit"}
]


# ============================================================
# Practice 21 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

numbers = [1, 2, 3, 4]

result = [x * 2 for x in numbers if x % 2 == 0]

print(result)


# ============================================================
# Practice 22 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

numbers = [1, 2, 3]

result = ["even" if x % 2 == 0 else "odd" for x in numbers]

print(result)


# ============================================================
# Practice 23 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

matrix = [[1, 2], [3, 4]]

result = [x for row in matrix for x in row]

print(result)


# ============================================================
# Practice 24 - Memory Challenge
# ============================================================
# Explain the memory difference between these two expressions:

numbers = range(1, 1_000_001)

result_list = [x * 2 for x in numbers]
result_generator = (x * 2 for x in numbers)

# Do not just state the answer.
# Explain when you would choose each one in a Data Engineering pipeline.


# ============================================================
# Practice 25 - Interview Challenge
# ============================================================
# Rewrite this normal loop as a list comprehension.

numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number ** 2)

print(result)
