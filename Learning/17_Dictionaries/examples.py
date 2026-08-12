# 🐍 Day 17 - Dictionaries | Examples

# ============================================================
# 1. Creating a Dictionary
# ============================================================

# Create a dictionary containing student information.
student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}

# Print the complete dictionary.
print(student)


# ============================================================
# 2. Empty Dictionary
# ============================================================

# Curly braces without key-value pairs create an empty dictionary.
empty = {}

# Print the empty dictionary.
print(empty)


# ============================================================
# 3. Accessing a Value
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# Use the key "name" to retrieve its associated value.
print(student["name"])


# ============================================================
# 4. get() with a Missing Key
# ============================================================

student = {
    "name": "Onkar"
}

# get() returns None instead of raising KeyError when the key is missing.
print(student.get("age"))

# The second argument provides a default value when the key is missing.
print(student.get("age", 0))


# ============================================================
# 5. Adding a New Key
# ============================================================

student = {
    "name": "Onkar"
}

# "age" does not exist, so this creates a new key-value pair.
student["age"] = 22

# Print the updated dictionary.
print(student)


# ============================================================
# 6. Updating an Existing Key
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# "age" already exists, so its value is replaced.
student["age"] = 23

# Print the updated dictionary.
print(student)


# ============================================================
# 7. update()
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# update() can change existing keys and add new keys.
student.update({
    "age": 23,
    "city": "Pune"
})

# Print the updated dictionary.
print(student)


# ============================================================
# 8. pop()
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# Remove the "age" key and store its removed value.
age = student.pop("age")

# Print the removed value.
print(age)

# Print the remaining dictionary.
print(student)


# ============================================================
# 9. popitem()
# ============================================================

student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}

# Remove and return the last inserted key-value pair.
item = student.popitem()

# Print the removed key-value pair.
print(item)

# Print the remaining dictionary.
print(student)


# ============================================================
# 10. del
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# Delete the key-value pair whose key is "age".
del student["age"]

# Print the dictionary after deletion.
print(student)


# ============================================================
# 11. clear()
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# Remove all key-value pairs from the dictionary.
student.clear()

# Print the now-empty dictionary.
print(student)


# ============================================================
# 12. Checking Keys with in
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# The in operator checks dictionary keys by default.
print("name" in student)

# "city" is not a key in the dictionary.
print("city" in student)


# ============================================================
# 13. Checking Values
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# values() gives access to dictionary values.
print("Onkar" in student.values())

# 22 is also stored as a value.
print(22 in student.values())


# ============================================================
# 14. len()
# ============================================================

student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}

# len() returns the number of key-value pairs.
print(len(student))


# ============================================================
# 15. Iterating Through Keys
# ============================================================

student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}

# Direct iteration over a dictionary gives its keys.
for key in student:
    # Print the current key.
    print(key)


# ============================================================
# 16. Iterating Through Values
# ============================================================

student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}

# values() gives the values one by one.
for value in student.values():
    # Print the current value.
    print(value)


# ============================================================
# 17. Iterating Through Keys and Values
# ============================================================

student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}

# items() returns each key-value pair as a two-element tuple.
for key, value in student.items():
    # Print both parts of the current pair.
    print(key, value)


# ============================================================
# 18. Nested Dictionary
# ============================================================

# Create a dictionary containing another dictionary as a value.
employee = {
    "id": 101,
    "name": "Onkar",
    "address": {
        "city": "Pune",
        "state": "Maharashtra"
    }
}

# First access "address", then access "city" inside it.
print(employee["address"]["city"])


# ============================================================
# 19. setdefault()
# ============================================================

student = {
    "name": "Onkar"
}

# The key "age" does not exist, so setdefault() creates it with 22.
age = student.setdefault("age", 22)

# Print the returned value.
print(age)

# Print the updated dictionary.
print(student)


# ============================================================
# 20. copy()
# ============================================================

student = {
    "name": "Onkar",
    "age": 22
}

# Create a shallow copy of the dictionary.
student_copy = student.copy()

# Change the copy.
student_copy["age"] = 23

# The original dictionary remains unchanged.
print(student)

# The copied dictionary contains the new value.
print(student_copy)


# ============================================================
# 21. Assignment vs Copy
# ============================================================

student = {
    "name": "Onkar"
}

# y refers to the same dictionary object as student.
y = student

# Modify the dictionary through y.
y["name"] = "Rahul"

# Both variables now show the changed value.
print(student)
print(y)


# ============================================================
# 22. Dictionary Unpacking and Merging
# ============================================================

first = {
    "name": "Onkar",
    "age": 22
}

second = {
    "city": "Pune",
    "role": "Data Engineer"
}

# **unpacks both dictionaries into a new dictionary.
combined = {
    **first,
    **second
}

# Print the merged dictionary.
print(combined)


# ============================================================
# 23. Dictionary Union Operator
# ============================================================

first = {"name": "Onkar"}
second = {"city": "Pune"}

# | creates a new dictionary containing both dictionaries.
combined = first | second

# Print the result.
print(combined)


# ============================================================
# 24. Dictionary Comprehension
# ============================================================

numbers = [1, 2, 3, 4]

# Create a dictionary where each number is mapped to its square.
squares = {number: number ** 2 for number in numbers}

# Print the resulting dictionary.
print(squares)


# ============================================================
# 25. Dictionary Comprehension with Condition
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Include only even numbers and map each one to its square.
even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

# Print the resulting dictionary.
print(even_squares)


# ============================================================
# 26. Tuple as a Dictionary Key
# ============================================================

# A tuple containing hashable values can be used as a dictionary key.
locations = {
    (18.52, 73.85): "Pune",
    (19.07, 72.87): "Mumbai"
}

# Use the coordinate tuple to retrieve the city.
print(locations[(18.52, 73.85)])


# ============================================================
# 27. Data Engineering Example - Configuration
# ============================================================

# Store pipeline configuration as key-value pairs.
config = {
    "database": "sales_db",
    "host": "localhost",
    "port": 3306,
    "batch_size": 1000
}

# Read the database name using its key.
print(config["database"])

# Read the batch size using its key.
print(config["batch_size"])


# ============================================================
# 28. Data Engineering Example - Record Transformation
# ============================================================

# Create a source record represented by a dictionary.
record = {
    "first_name": "Onkar",
    "last_name": "Jadhav"
}

# Create a derived full_name field using existing values.
record["full_name"] = (
    record["first_name"] + " " + record["last_name"]
)

# Print the transformed record.
print(record)


# ============================================================
# 29. Data Engineering Example - Frequency Count
# ============================================================

words = ["sql", "python", "sql", "python", "sql"]

# Create an empty dictionary to store word counts.
counts = {}

# Process each word one at a time.
for word in words:
    # Get the current count or use 0 when the word is new, then add 1.
    counts[word] = counts.get(word, 0) + 1

# Print the final frequency dictionary.
print(counts)


# ============================================================
# 30. Data Engineering Example - Records
# ============================================================

# Store multiple records as dictionaries inside a list.
records = [
    {"id": 101, "name": "Onkar", "city": "Pune"},
    {"id": 102, "name": "Rahul", "city": "Mumbai"}
]

# Process each record one at a time.
for record in records:
    # Retrieve the customer ID using its key.
    customer_id = record["id"]

    # Retrieve the customer name using its key.
    name = record["name"]

    # Print the selected fields.
    print(customer_id, name)
