# 🐍 Day 15 - Tuples | Practice

# Solve each problem yourself before checking your notes.

# ============================================================
# Practice 1 - Create a Tuple
# ============================================================
# Create a tuple containing five numbers and print it.


# ============================================================
# Practice 2 - Access Elements
# ============================================================
# Given the tuple below, print the first, third, and last elements.

numbers = (10, 20, 30, 40, 50)


# ============================================================
# Practice 3 - Negative Indexing
# ============================================================
# Print the last two elements using negative indexing.

numbers = (10, 20, 30, 40, 50)


# ============================================================
# Practice 4 - Slicing
# ============================================================
# Extract elements from index 1 through index 3.
# Remember that the stop index is not included.

numbers = (10, 20, 30, 40, 50)


# ============================================================
# Practice 5 - Reverse a Tuple
# ============================================================
# Reverse the tuple using slicing.

numbers = (10, 20, 30, 40, 50)


# ============================================================
# Practice 6 - Single-Element Tuple
# ============================================================
# Create a tuple containing only the value 100.
# Verify its type using type().


# ============================================================
# Practice 7 - Count Values
# ============================================================
# Count how many times 20 appears in the tuple.

numbers = (10, 20, 30, 20, 40, 20, 50)


# ============================================================
# Practice 8 - Find an Index
# ============================================================
# Find the index of the first occurrence of "SQL".

skills = ("Python", "SQL", "Snowflake", "SQL")


# ============================================================
# Practice 9 - Membership Check
# ============================================================
# Check whether "Python" and "Java" exist in the tuple.

skills = ("Python", "SQL", "Snowflake")


# ============================================================
# Practice 10 - Tuple Unpacking
# ============================================================
# Unpack the following tuple into three variables and print them.

student = (101, "Onkar", "Data Engineer")


# ============================================================
# Practice 11 - Extended Unpacking
# ============================================================
# Use starred unpacking to store:
# first value -> first
# middle values -> middle
# last value -> last

numbers = (10, 20, 30, 40, 50)


# ============================================================
# Practice 12 - List to Tuple
# ============================================================
# Convert the following list into a tuple.

numbers = [10, 20, 30, 40]


# ============================================================
# Practice 13 - Tuple to List
# ============================================================
# Convert the tuple into a list, add 50, and print the result.

numbers = (10, 20, 30, 40)


# ============================================================
# Practice 14 - Sort a Tuple
# ============================================================
# Create a new tuple containing the values in ascending order.
# Do not try to use tuple.sort().

numbers = (50, 10, 40, 20, 30)


# ============================================================
# Practice 15 - Nested Tuple
# ============================================================
# Print the city name "Pune" from the nested tuple.

locations = (
    (18.52, 73.85, "Pune"),
    (19.07, 72.87, "Mumbai")
)


# ============================================================
# Practice 16 - Mutable Object Inside Tuple
# ============================================================
# Add the value 30 to the list stored inside the tuple.

items = ([10, 20], "Python")


# ============================================================
# Practice 17 - Function Returning Multiple Values
# ============================================================
# Create a function that accepts a list of numbers and returns:
# 1. minimum value
# 2. maximum value
# 3. total
# Store the returned values using tuple unpacking.


# ============================================================
# Practice 18 - Data Engineering Scenario
# ============================================================
# You receive database records as tuples:
# (customer_id, customer_name, city)
#
# 1. Store at least three records in a list.
# 2. Loop through the records.
# 3. Print the customer_id and city for each record.


# ============================================================
# Practice 19 - Interview Challenge
# ============================================================
# Predict the output before running the code:

x = (1, 2, 3)
y = x

print(x is y)
print(x == y)


# ============================================================
# Practice 20 - Interview Challenge
# ============================================================
# Predict the output before running the code:

value = (10)
other_value = (10,)

print(type(value))
print(type(other_value))
