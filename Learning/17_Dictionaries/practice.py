# 🐍 Day 17 - Dictionaries | Practice

# Solve each problem yourself before checking your learning notes.

# ============================================================
# Practice 1 - Create a Dictionary
# ============================================================
# Create a dictionary containing:
# id, name, city, role
# Print the dictionary.


# ============================================================
# Practice 2 - Access Values
# ============================================================
# Given the dictionary below, print the name and city.

student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 3 - get()
# ============================================================
# Use get() to retrieve "age" from the dictionary.
# Return 0 if the key does not exist.

student = {
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 4 - Add a Key
# ============================================================
# Add an "age" key with value 22.

student = {
    "name": "Onkar"
}


# ============================================================
# Practice 5 - Update a Value
# ============================================================
# Change the value of "city" from Pune to Mumbai.

student = {
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 6 - update()
# ============================================================
# Add "role" and update "age" using update().

student = {
    "name": "Onkar",
    "age": 22
}


# ============================================================
# Practice 7 - Remove with pop()
# ============================================================
# Remove the "age" key using pop() and print the removed value.

student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}


# ============================================================
# Practice 8 - popitem()
# ============================================================
# Use popitem() to remove the last inserted key-value pair.
# Print the removed pair and the remaining dictionary.

student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}


# ============================================================
# Practice 9 - Membership
# ============================================================
# Check whether "email" is a key in the dictionary.

student = {
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 10 - Check a Value
# ============================================================
# Check whether "Pune" exists as a value.

student = {
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 11 - Loop Through Keys
# ============================================================
# Print every key using a loop.

student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 12 - Loop Through Values
# ============================================================
# Print every value using a loop.

student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 13 - Loop Through items()
# ============================================================
# Print each key and value together.

student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}


# ============================================================
# Practice 14 - Nested Dictionary
# ============================================================
# Print the city from the nested dictionary.

employee = {
    "id": 101,
    "name": "Onkar",
    "address": {
        "city": "Pune",
        "state": "Maharashtra"
    }
}


# ============================================================
# Practice 15 - setdefault()
# ============================================================
# Add an "age" key with default value 22 using setdefault().
# If the key already exists, do not replace its value.

student = {
    "name": "Onkar"
}


# ============================================================
# Practice 16 - Copy
# ============================================================
# Create a shallow copy of the dictionary.
# Change the copy and prove that the original is unchanged.

student = {
    "name": "Onkar",
    "age": 22
}


# ============================================================
# Practice 17 - Assignment vs Copy
# ============================================================
# Predict what happens before running the code.
# Explain why changing y also affects x.

x = {"name": "Onkar"}
y = x

y["name"] = "Rahul"

print(x)
print(y)


# ============================================================
# Practice 18 - Dictionary Comprehension
# ============================================================
# Create a dictionary mapping numbers 1-5 to their squares.


# ============================================================
# Practice 19 - Conditional Dictionary Comprehension
# ============================================================
# Create a dictionary containing only even numbers from 1-10
# and map each number to its square.


# ============================================================
# Practice 20 - Tuple as Key
# ============================================================
# Create a dictionary where geographic coordinates are keys
# and city names are values.


# ============================================================
# Practice 21 - Frequency Counter
# ============================================================
# Count how many times each word appears.

words = ["sql", "python", "sql", "snowflake", "python", "sql"]


# ============================================================
# Practice 22 - Data Engineering Scenario
# ============================================================
# You receive these records:
#
# records = [
#     {"id": 101, "name": "Onkar", "city": "Pune"},
#     {"id": 102, "name": "Rahul", "city": "Mumbai"},
#     {"id": 103, "name": "Amit", "city": "Pune"}
# ]
#
# Create a dictionary that counts how many customers belong
# to each city.


# ============================================================
# Practice 23 - Data Engineering Scenario
# ============================================================
# Given the configuration dictionary below, print all keys
# whose values are numeric.

config = {
    "database": "sales_db",
    "port": 3306,
    "batch_size": 1000,
    "host": "localhost"
}


# ============================================================
# Practice 24 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

x = {"a": 1, "b": 2}
y = x.copy()

y["a"] = 100

print(x)
print(y)


# ============================================================
# Practice 25 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

x = {
    "a": 1,
    "b": 2,
    "a": 100
}

print(x)
