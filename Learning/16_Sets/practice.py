# 🐍 Day 16 - Sets | Practice

# Solve each problem yourself before checking your notes.

# ============================================================
# Practice 1 - Create a Set
# ============================================================
# Create a set containing five numbers and print it.


# ============================================================
# Practice 2 - Remove Duplicates
# ============================================================
# Convert the list below into a set so that only unique values remain.

numbers = [10, 20, 10, 30, 20, 40, 30]


# ============================================================
# Practice 3 - Empty Set
# ============================================================
# Create an empty set and verify its type using type().


# ============================================================
# Practice 4 - Membership
# ============================================================
# Check whether "Python" exists in the set.
# Also check whether "Java" does not exist.

skills = {"Python", "SQL", "Snowflake"}


# ============================================================
# Practice 5 - add()
# ============================================================
# Add "Linux" to the following set.

skills = {"Python", "SQL"}


# ============================================================
# Practice 6 - update()
# ============================================================
# Add the values "Snowflake", "Hadoop", and "Linux" using update().

skills = {"Python", "SQL"}


# ============================================================
# Practice 7 - remove() vs discard()
# ============================================================
# Remove 20 using remove().
# Then try to discard 50 without causing an exception.

numbers = {10, 20, 30}


# ============================================================
# Practice 8 - Union
# ============================================================
# Find all unique skills across both sets.

set_a = {"Python", "SQL", "Git"}
set_b = {"SQL", "Snowflake", "Python"}


# ============================================================
# Practice 9 - Intersection
# ============================================================
# Find the skills that exist in both sets.

set_a = {"Python", "SQL", "Git"}
set_b = {"SQL", "Snowflake", "Python"}


# ============================================================
# Practice 10 - Difference
# ============================================================
# Find values that exist in set_a but not set_b.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}


# ============================================================
# Practice 11 - Symmetric Difference
# ============================================================
# Find values that exist in exactly one of the two sets.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}


# ============================================================
# Practice 12 - Subset
# ============================================================
# Check whether the smaller set is a subset of the larger set.

small = {1, 2}
large = {1, 2, 3, 4, 5}


# ============================================================
# Practice 13 - Superset
# ============================================================
# Check whether the larger set is a superset of the smaller set.

small = {1, 2}
large = {1, 2, 3, 4, 5}


# ============================================================
# Practice 14 - Disjoint Sets
# ============================================================
# Check whether the two sets have no common elements.

set_a = {1, 2, 3}
set_b = {4, 5, 6}


# ============================================================
# Practice 15 - Loop Through a Set
# ============================================================
# Print every value in the following set using a for loop.

skills = {"Python", "SQL", "Snowflake", "Linux"}


# ============================================================
# Practice 16 - Set Comprehension
# ============================================================
# Create a set containing the squares of numbers from 1 to 10.


# ============================================================
# Practice 17 - Even Numbers with Set Comprehension
# ============================================================
# Create a set containing unique even numbers from the list.

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]


# ============================================================
# Practice 18 - Data Engineering Reconciliation
# ============================================================
# Find customer IDs that exist in the source but not in the target.

source_ids = {101, 102, 103, 104, 105}
target_ids = {101, 102, 104}


# ============================================================
# Practice 19 - Data Engineering Reconciliation
# ============================================================
# Find customer IDs that exist in the target but not in the source.

source_ids = {101, 102, 103, 104, 105}
target_ids = {101, 102, 104, 106}


# ============================================================
# Practice 20 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

numbers = {10, 20, 20, 30, 30}

print(len(numbers))
print(20 in numbers)


# ============================================================
# Practice 21 - Interview Output Prediction
# ============================================================
# Predict what happens before running the code.

numbers = {10, 20, 30}

print(numbers[0])


# ============================================================
# Practice 22 - Interview Challenge
# ============================================================
# Explain the difference between these two operations:
#
# numbers.remove(50)
# numbers.discard(50)
#
# What happens if 50 does not exist?

numbers = {10, 20, 30}


# ============================================================
# Practice 23 - Interview Challenge
# ============================================================
# A list contains customer IDs with duplicates.
# Remove duplicates while preserving the original order.

customer_ids = [101, 102, 101, 103, 102, 104]


# ============================================================
# Practice 24 - Interview Challenge
# ============================================================
# Given two sets of skills:
# 1. Find common skills.
# 2. Find skills only in the first set.
# 3. Find skills only in the second set.
# 4. Find skills unique to each set.

skills_a = {"Python", "SQL", "Git", "Linux"}
skills_b = {"SQL", "Python", "Snowflake", "Spark"}


# ============================================================
# Practice 25 - Data Engineering Challenge
# ============================================================
# You receive IDs from a source system and a warehouse.
# Determine:
# 1. Missing IDs in the warehouse.
# 2. Unexpected IDs in the warehouse.
# 3. IDs present in both systems.
#
# Then explain which set operation you used for each result.

source_ids = {1001, 1002, 1003, 1004, 1005}
warehouse_ids = {1001, 1002, 1004, 1006}
