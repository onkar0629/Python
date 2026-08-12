# 🐍 Day 14 - Lists | Examples

# ============================================================
# 1. Creating a List
# ============================================================

# Create a list containing three numbers.
numbers = [10, 20, 30]

# Print the complete list.
print(numbers)


# ============================================================
# 2. List with Different Data Types
# ============================================================

# A list can store values of different data types.
values = [10, "Python", 3.14, True]

# Print the list.
print(values)


# ============================================================
# 3. Indexing
# ============================================================

numbers = [10, 20, 30, 40]

# Index 0 represents the first element.
print(numbers[0])

# Index 2 represents the third element.
print(numbers[2])


# ============================================================
# 4. Negative Indexing
# ============================================================

numbers = [10, 20, 30, 40]

# Index -1 represents the last element.
print(numbers[-1])

# Index -2 represents the second-last element.
print(numbers[-2])


# ============================================================
# 5. Slicing
# ============================================================

numbers = [10, 20, 30, 40, 50]

# Start at index 1 and stop before index 4.
print(numbers[1:4])

# Reverse the list using a negative step.
print(numbers[::-1])


# ============================================================
# 6. Updating an Element
# ============================================================

numbers = [10, 20, 30]

# Replace the value at index 1 with 200.
numbers[1] = 200

# Print the updated list.
print(numbers)


# ============================================================
# 7. append()
# ============================================================

numbers = [10, 20]

# append() adds one object to the end of the list.
numbers.append(30)

print(numbers)


# ============================================================
# 8. insert()
# ============================================================

numbers = [10, 20, 30]

# Insert 15 at index 1.
numbers.insert(1, 15)

print(numbers)


# ============================================================
# 9. extend()
# ============================================================

numbers = [10, 20]

# extend() adds each element from the supplied iterable.
numbers.extend([30, 40])

print(numbers)


# ============================================================
# 10. append() vs extend()
# ============================================================

# append() adds the entire list as one element.
a = [1, 2]
a.append([3, 4])
print(a)

# extend() adds the elements separately.
b = [1, 2]
b.extend([3, 4])
print(b)


# ============================================================
# 11. remove()
# ============================================================

numbers = [10, 20, 30, 20]

# remove() deletes the first matching value.
numbers.remove(20)

print(numbers)


# ============================================================
# 12. pop()
# ============================================================

numbers = [10, 20, 30]

# pop() removes the last element and returns it.
removed_value = numbers.pop()

print(removed_value)
print(numbers)


# ============================================================
# 13. del
# ============================================================

numbers = [10, 20, 30]

# Delete the element at index 0.
del numbers[0]

print(numbers)


# ============================================================
# 14. clear()
# ============================================================

numbers = [10, 20, 30]

# clear() removes every element from the list.
numbers.clear()

print(numbers)


# ============================================================
# 15. len(), min(), max(), sum()
# ============================================================

numbers = [10, 20, 30, 40]

# len() returns the number of elements.
print(len(numbers))

# min() returns the smallest value.
print(min(numbers))

# max() returns the largest value.
print(max(numbers))

# sum() returns the total of numeric elements.
print(sum(numbers))


# ============================================================
# 16. count() and index()
# ============================================================

numbers = [10, 20, 20, 30, 20]

# count() returns how many times 20 occurs.
print(numbers.count(20))

# index() returns the first position of 30.
print(numbers.index(30))


# ============================================================
# 17. sort()
# ============================================================

numbers = [40, 10, 30, 20]

# sort() changes the existing list into ascending order.
numbers.sort()

print(numbers)

# Sort the same list in descending order.
numbers.sort(reverse=True)

print(numbers)


# ============================================================
# 18. reverse()
# ============================================================

numbers = [10, 20, 30]

# reverse() reverses the existing list in place.
numbers.reverse()

print(numbers)


# ============================================================
# 19. Traversing a List
# ============================================================

languages = ["Python", "SQL", "Snowflake"]

# Visit each element one by one.
for language in languages:
    # Print the current element.
    print(language)


# ============================================================
# 20. Traversing with Indexes
# ============================================================

languages = ["Python", "SQL", "Snowflake"]

# range(len(languages)) creates indexes from 0 to 2.
for index in range(len(languages)):
    # Use the index to access the corresponding element.
    print(index, languages[index])


# ============================================================
# 21. Nested Lists
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# First index selects the second inner list.
# Second index selects the second element inside that list.
print(matrix[1][1])


# ============================================================
# 22. Copying a List
# ============================================================

original = [1, 2, 3]

# copy() creates a new outer list.
copy_list = original.copy()

# Change the copied list.
copy_list.append(4)

# The original list remains unchanged.
print(original)
print(copy_list)


# ============================================================
# 23. Same Reference vs Copy
# ============================================================

original = [1, 2]

# Assignment creates another reference to the same list.
same_list = original

# Modify the shared list.
same_list.append(3)

# Both variables now show the changed list.
print(original)
print(same_list)


# ============================================================
# 24. Data Engineering Example
# ============================================================

# Store the names of columns required from a source dataset.
columns = ["customer_id", "name", "email", "created_at"]

# Iterate through the column names.
for column in columns:
    # Print each column name.
    print(column)


# ============================================================
# 25. Records for a Database Load
# ============================================================

# Store multiple records as tuples inside a list.
records = [
    (101, "Onkar", "onkar@example.com"),
    (102, "Rahul", "rahul@example.com")
]

# Process each record one at a time.
for record in records:
    # Print the current record.
    print(record)
