# 🐍 Day 18 - List Comprehension | Examples

# ============================================================
# 1. Basic List Comprehension
# ============================================================

numbers = [1, 2, 3, 4]

# For every number, calculate its square and store the result in a new list.
squares = [number ** 2 for number in numbers]

# Print the new list.
print(squares)


# ============================================================
# 2. Normal Loop Equivalent
# ============================================================

numbers = [1, 2, 3, 4]

# Create an empty list to store the results.
squares = []

# Process every number one at a time.
for number in numbers:
    # Calculate the square and add it to the result list.
    squares.append(number ** 2)

# Print the result.
print(squares)


# ============================================================
# 3. Multiplication Transformation
# ============================================================

numbers = [1, 2, 3, 4]

# Multiply every number by 10 and create a new list.
doubled = [number * 10 for number in numbers]

# Print the transformed values.
print(doubled)


# ============================================================
# 4. String Transformation
# ============================================================

names = ["onkar", "rahul", "amit"]

# Convert every name to uppercase.
uppercase_names = [name.upper() for name in names]

# Print the transformed names.
print(uppercase_names)


# ============================================================
# 5. Character Extraction
# ============================================================

text = "Python"

# Take every character from the string and store it in a list.
letters = [character for character in text]

# Print the characters.
print(letters)


# ============================================================
# 6. Filtering Even Numbers
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# Include only numbers that are divisible by 2.
even_numbers = [number for number in numbers if number % 2 == 0]

# Print the filtered list.
print(even_numbers)


# ============================================================
# 7. Filtering Positive Numbers
# ============================================================

numbers = [-3, -2, -1, 0, 1, 2, 3]

# Include only values greater than zero.
positive_numbers = [number for number in numbers if number > 0]

# Print the result.
print(positive_numbers)


# ============================================================
# 8. Conditional if-else
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Return the word "even" for even numbers and "odd" otherwise.
labels = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]

# Print the labels.
print(labels)


# ============================================================
# 9. Square Positive Numbers
# ============================================================

numbers = [-3, -2, -1, 0, 1, 2, 3]

# Keep only positive numbers and square them.
positive_squares = [
    number ** 2
    for number in numbers
    if number > 0
]

# Print the result.
print(positive_squares)


# ============================================================
# 10. Nested Loops
# ============================================================

numbers = [1, 2]
letters = ["A", "B"]

# Create every combination of a number and a letter.
pairs = [
    (number, letter)
    for number in numbers
    for letter in letters
]

# Print all combinations.
print(pairs)


# ============================================================
# 11. Flatten a Nested List
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Visit every row and then every number inside that row.
flattened = [number for row in matrix for number in row]

# Print the flattened list.
print(flattened)


# ============================================================
# 12. Dictionary Keys
# ============================================================

student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}

# Create a list containing every dictionary key.
keys = [key for key in student]

# Print the keys.
print(keys)


# ============================================================
# 13. Dictionary Values
# ============================================================

# Create a list containing every dictionary value.
values = [value for value in student.values()]

# Print the values.
print(values)


# ============================================================
# 14. Dictionary Items
# ============================================================

# Convert the dictionary's key-value pairs into a list.
items = [item for item in student.items()]

# Print the list of tuples.
print(items)


# ============================================================
# 15. Calling a Function
# ============================================================

def square(number):
    # Return the square of the supplied number.
    return number ** 2


numbers = [1, 2, 3, 4]

# Call square() for every number.
squares = [square(number) for number in numbers]

# Print the results.
print(squares)


# ============================================================
# 16. Filtering Strings
# ============================================================

words = ["sql", "python", "spark", "hi"]

# Keep only words containing more than two characters.
long_words = [word for word in words if len(word) > 2]

# Print the filtered words.
print(long_words)


# ============================================================
# 17. Converting Strings to Integers
# ============================================================

values = ["10", "20", "30"]

# Convert each string value into an integer.
numbers = [int(value) for value in values]

# Print the converted values.
print(numbers)


# ============================================================
# 18. Using range()
# ============================================================

# Create squares for numbers from 1 through 5.
squares = [number ** 2 for number in range(1, 6)]

# Print the result.
print(squares)


# ============================================================
# 19. Even Squares
# ============================================================

# Generate even numbers from 1 through 10 and square them.
even_squares = [
    number ** 2
    for number in range(1, 11)
    if number % 2 == 0
]

# Print the result.
print(even_squares)


# ============================================================
# 20. Data Engineering Example - Clean Names
# ============================================================

names = [" onkar ", " rahul ", " amit "]

# Remove surrounding spaces and convert each name to title case.
clean_names = [name.strip().title() for name in names]

# Print cleaned values.
print(clean_names)


# ============================================================
# 21. Data Engineering Example - Active Records
# ============================================================

records = [
    {"id": 101, "status": "active"},
    {"id": 102, "status": "inactive"},
    {"id": 103, "status": "active"}
]

# Keep only records whose status is active.
active_records = [
    record
    for record in records
    if record["status"] == "active"
]

# Print the selected records.
print(active_records)


# ============================================================
# 22. Data Engineering Example - Extract IDs
# ============================================================

# Extract the customer ID from every record.
customer_ids = [record["id"] for record in records]

# Print the IDs.
print(customer_ids)


# ============================================================
# 23. Generator Expression Comparison
# ============================================================

numbers = range(1, 6)

# List comprehension creates all values immediately.
squares_list = [number ** 2 for number in numbers]

# Generator expression produces values lazily.
squares_generator = (number ** 2 for number in numbers)

# Print the complete list.
print(squares_list)

# Consume the generator one value at a time and print each value.
for square_value in squares_generator:
    print(square_value)
