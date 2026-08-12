# 🐍 Day 15 - Tuples | Examples

# ============================================================
# 1. Creating a Tuple
# ============================================================

# Create a tuple containing three numbers.
numbers = (10, 20, 30)

# Print the complete tuple.
print(numbers)


# ============================================================
# 2. Tuple Without Parentheses
# ============================================================

# Python creates a tuple from comma-separated values.
values = 10, 20, 30

# Print the tuple.
print(values)


# ============================================================
# 3. Empty Tuple
# ============================================================

# Create an empty tuple using parentheses.
empty = ()

# Print the empty tuple.
print(empty)


# ============================================================
# 4. Single-Element Tuple
# ============================================================

# Parentheses alone do not create a tuple for one value.
value = (10)

# Print the data type; this is an integer.
print(type(value))

# The trailing comma creates a one-element tuple.
single = (10,)

# Print the data type; this is a tuple.
print(type(single))


# ============================================================
# 5. Creating a Tuple with tuple()
# ============================================================

# Convert a list into a tuple.
numbers = tuple([10, 20, 30])

# Print the converted tuple.
print(numbers)


# ============================================================
# 6. Indexing
# ============================================================

numbers = (10, 20, 30, 40)

# Index 0 represents the first element.
print(numbers[0])

# Index 2 represents the third element.
print(numbers[2])


# ============================================================
# 7. Negative Indexing
# ============================================================

numbers = (10, 20, 30, 40)

# Index -1 represents the last element.
print(numbers[-1])

# Index -2 represents the second-last element.
print(numbers[-2])


# ============================================================
# 8. Slicing
# ============================================================

numbers = (10, 20, 30, 40, 50)

# Start at index 1 and stop before index 4.
print(numbers[1:4])

# Reverse the tuple using a negative step.
print(numbers[::-1])


# ============================================================
# 9. Immutability
# ============================================================

numbers = (10, 20, 30)

# This line would raise TypeError because tuples are immutable.
# numbers[0] = 100

# Print the original tuple because no modification was performed.
print(numbers)


# ============================================================
# 10. Tuple Containing a Mutable List
# ============================================================

# The tuple contains a list, and the list itself is mutable.
items = ([1, 2], "Python")

# Modify the list stored inside the tuple.
items[0].append(3)

# The outer tuple remains the same structure, but the nested list changed.
print(items)


# ============================================================
# 11. Tuple Packing
# ============================================================

# Multiple comma-separated values are packed into one tuple.
student = 101, "Onkar", "Data Engineer"

# Print the packed tuple.
print(student)


# ============================================================
# 12. Tuple Unpacking
# ============================================================

# Store three values inside a tuple.
student = (101, "Onkar", "Data Engineer")

# Unpack the tuple into three variables.
student_id, name, role = student

# Print each unpacked value.
print(student_id)
print(name)
print(role)


# ============================================================
# 13. Extended Unpacking
# ============================================================

# Create a tuple containing five values.
numbers = (10, 20, 30, 40, 50)

# Store the first value, remaining middle values, and last value separately.
first, *middle, last = numbers

# Print the unpacked values.
print(first)
print(middle)
print(last)


# ============================================================
# 14. count()
# ============================================================

numbers = (10, 20, 20, 30, 20)

# count() returns how many times 20 occurs.
print(numbers.count(20))


# ============================================================
# 15. index()
# ============================================================

numbers = (10, 20, 30, 20)

# index() returns the position of the first occurrence of 20.
print(numbers.index(20))


# ============================================================
# 16. Searching with in
# ============================================================

languages = ("Python", "SQL", "Snowflake")

# Check whether Python exists in the tuple.
print("Python" in languages)

# Check whether Java exists in the tuple.
print("Java" in languages)


# ============================================================
# 17. Traversing a Tuple
# ============================================================

languages = ("Python", "SQL", "Snowflake")

# Visit each tuple element one by one.
for language in languages:
    # Print the current element.
    print(language)


# ============================================================
# 18. Traversing with Indexes
# ============================================================

languages = ("Python", "SQL", "Snowflake")

# range(len(languages)) creates indexes from 0 to 2.
for index in range(len(languages)):
    # Use the index to access the corresponding tuple element.
    print(index, languages[index])


# ============================================================
# 19. Nested Tuples
# ============================================================

# Store two coordinate pairs inside an outer tuple.
coordinates = (
    (18.52, 73.85),
    (19.07, 72.87)
)

# Select the second coordinate pair and then its latitude.
print(coordinates[1][0])


# ============================================================
# 20. List to Tuple
# ============================================================

# Create a list of numbers.
numbers_list = [10, 20, 30]

# Convert the list into a tuple.
numbers_tuple = tuple(numbers_list)

# Print the converted tuple.
print(numbers_tuple)


# ============================================================
# 21. Tuple to List
# ============================================================

# Create a tuple of numbers.
numbers_tuple = (10, 20, 30)

# Convert the tuple into a list so it can be modified.
numbers_list = list(numbers_tuple)

# Add another value to the list.
numbers_list.append(40)

# Print the modified list.
print(numbers_list)


# ============================================================
# 22. sort() Alternative for Tuples
# ============================================================

# Create an unsorted tuple.
numbers = (30, 10, 20)

# sorted() returns a new list in sorted order.
sorted_list = sorted(numbers)

# Convert the sorted list back into a tuple.
sorted_tuple = tuple(sorted_list)

# Print the sorted tuple.
print(sorted_tuple)


# ============================================================
# 23. Tuple Assignment and Identity
# ============================================================

# Create one tuple object.
x = (10, 20, 30)

# Make y refer to the same tuple object.
y = x

# Check whether x and y refer to the same object.
print(x is y)

# Check whether the tuples contain the same values.
print(x == y)


# ============================================================
# 24. Multiple Return Values
# ============================================================

# Define a function that returns two values.
def get_min_max(numbers):
    # Return two values; Python packs them into a tuple.
    return min(numbers), max(numbers)


# Call the function and store the returned tuple.
result = get_min_max([10, 40, 20, 30])

# Print the returned tuple.
print(result)

# Unpack the returned tuple into two variables.
minimum, maximum = get_min_max([10, 40, 20, 30])

# Print the two values separately.
print(minimum)
print(maximum)


# ============================================================
# 25. Data Engineering Example - Records
# ============================================================

# Store database-like records as tuples inside a list.
records = [
    (101, "Onkar", "onkar@example.com"),
    (102, "Rahul", "rahul@example.com")
]

# Process each fixed record one at a time.
for record in records:
    # Print the current record.
    print(record)
