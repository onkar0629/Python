# 🐍 Day 16 - Sets | Examples

# ============================================================
# 1. Creating a Set
# ============================================================

# Create a set containing three numbers.
numbers = {10, 20, 30}

# Print the complete set.
print(numbers)


# ============================================================
# 2. Creating a Set with set()
# ============================================================

# Convert a list into a set.
numbers = set([10, 20, 30, 20])

# Print the set; duplicate 20 is stored only once.
print(numbers)


# ============================================================
# 3. Empty Set vs Empty Dictionary
# ============================================================

# Curly braces without elements create an empty dictionary.
empty_dictionary = {}

# Print its type.
print(type(empty_dictionary))

# Use set() to create an empty set.
empty_set = set()

# Print its type.
print(type(empty_set))


# ============================================================
# 4. Duplicate Values
# ============================================================

# Create a set containing duplicate values.
numbers = {10, 20, 20, 30, 30}

# Print the set; duplicates are automatically removed.
print(numbers)


# ============================================================
# 5. Membership Checking
# ============================================================

# Create a set of skills.
skills = {"Python", "SQL", "Snowflake"}

# Check whether Python exists in the set.
print("Python" in skills)

# Check whether Java exists in the set.
print("Java" in skills)


# ============================================================
# 6. add()
# ============================================================

# Create a set with two values.
numbers = {10, 20}

# Add one new value to the set.
numbers.add(30)

# Print the updated set.
print(numbers)

# Adding an existing value does not create a duplicate.
numbers.add(20)

# Print the set again.
print(numbers)


# ============================================================
# 7. update()
# ============================================================

# Create a set with two values.
numbers = {10, 20}

# Add multiple values from a list.
numbers.update([30, 40, 50])

# Print the updated set.
print(numbers)


# ============================================================
# 8. remove()
# ============================================================

# Create a set of numbers.
numbers = {10, 20, 30}

# Remove the value 20.
numbers.remove(20)

# Print the updated set.
print(numbers)


# ============================================================
# 9. discard()
# ============================================================

# Create a set of numbers.
numbers = {10, 20, 30}

# Try to remove 50; no error occurs because 50 is absent.
numbers.discard(50)

# Print the unchanged set.
print(numbers)


# ============================================================
# 10. pop()
# ============================================================

# Create a set of numbers.
numbers = {10, 20, 30}

# Remove and return an arbitrary element.
value = numbers.pop()

# Print the removed value.
print(value)

# Print the remaining set.
print(numbers)


# ============================================================
# 11. clear()
# ============================================================

# Create a set of numbers.
numbers = {10, 20, 30}

# Remove all elements from the set.
numbers.clear()

# Print the empty set.
print(numbers)


# ============================================================
# 12. Union
# ============================================================

# Create two sets.
A = {1, 2, 3}
B = {3, 4, 5}

# Combine all unique values from both sets.
union_result = A | B

# Print the union.
print(union_result)

# The union() method produces the same logical result.
print(A.union(B))


# ============================================================
# 13. Intersection
# ============================================================

# Find values that exist in both sets.
intersection_result = A & B

# Print the common values.
print(intersection_result)

# The intersection() method produces the same result.
print(A.intersection(B))


# ============================================================
# 14. Difference
# ============================================================

# Find values that exist in A but not B.
difference_result = A - B

# Print the difference.
print(difference_result)

# Reverse the operation to show that direction matters.
reverse_difference = B - A

# Print the reverse difference.
print(reverse_difference)


# ============================================================
# 15. Symmetric Difference
# ============================================================

# Find values that exist in exactly one of the sets.
symmetric_result = A ^ B

# Print the symmetric difference.
print(symmetric_result)


# ============================================================
# 16. Subset and Superset
# ============================================================

# Create a smaller and larger set.
small = {1, 2}
large = {1, 2, 3, 4}

# Check whether small is a subset of large.
print(small.issubset(large))

# Check whether large is a superset of small.
print(large.issuperset(small))


# ============================================================
# 17. Disjoint Sets
# ============================================================

# Create two sets with no common values.
set_a = {1, 2, 3}
set_b = {4, 5, 6}

# Check whether they have no common elements.
print(set_a.isdisjoint(set_b))


# ============================================================
# 18. Looping Through a Set
# ============================================================

# Create a set of skills.
skills = {"Python", "SQL", "Snowflake"}

# Visit each element in the set.
for skill in skills:
    # Print the current skill.
    print(skill)


# ============================================================
# 19. List to Set - Remove Duplicates
# ============================================================

# Create a list containing duplicate IDs.
customer_ids = [101, 102, 101, 103, 102]

# Convert the list to a set to keep unique IDs.
unique_customer_ids = set(customer_ids)

# Print the unique IDs.
print(unique_customer_ids)


# ============================================================
# 20. Order-Preserving Deduplication
# ============================================================

# Create a list containing duplicate values.
numbers = [10, 20, 10, 30, 20]

# dict.fromkeys() removes duplicates while preserving first-seen order.
unique_numbers = list(dict.fromkeys(numbers))

# Print the ordered unique values.
print(unique_numbers)


# ============================================================
# 21. Frozenset
# ============================================================

# Create an immutable set.
numbers = frozenset([10, 20, 30])

# Print the frozenset.
print(numbers)

# numbers.add(40) would raise AttributeError because frozensets are immutable.


# ============================================================
# 22. Set Comprehension
# ============================================================

# Create a list of numbers.
numbers = [1, 2, 3, 4, 5]

# Create a set containing the square of each number.
squares = {number * number for number in numbers}

# Print the resulting set.
print(squares)


# ============================================================
# 23. Set Comprehension with Condition
# ============================================================

# Create a list containing numbers from 1 to 6.
numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers in the set.
even_numbers = {number for number in numbers if number % 2 == 0}

# Print the unique even numbers.
print(even_numbers)


# ============================================================
# 24. Data Engineering - Source vs Target IDs
# ============================================================

# Store IDs received from the source system.
source_ids = {101, 102, 103, 104}

# Store IDs currently available in the target system.
target_ids = {101, 102, 104}

# Find IDs that exist in the source but are missing from the target.
missing_ids = source_ids - target_ids

# Print the missing IDs.
print(missing_ids)

# Find IDs that exist in both systems.
common_ids = source_ids & target_ids

# Print the common IDs.
print(common_ids)

# Find IDs that unexpectedly exist in the target but not the source.
unexpected_ids = target_ids - source_ids

# Print the unexpected IDs.
print(unexpected_ids)


# ============================================================
# 25. Data Validation - Allowed Status
# ============================================================

# Define the allowed status values.
allowed_status = {"ACTIVE", "INACTIVE", "PENDING"}

# Define an incoming status value.
status = "ACTIVE"

# Check whether the incoming status is valid.
if status in allowed_status:
    # Print a message when the status is valid.
    print("Valid status")
else:
    # Print a message when the status is invalid.
    print("Invalid status")
