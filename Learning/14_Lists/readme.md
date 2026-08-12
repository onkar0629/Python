# 🐍 Day 14 - Lists

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

A **list** is a collection used to store multiple values inside a single variable.

Instead of creating separate variables:

```python
student_1 = "Onkar"
student_2 = "Rahul"
student_3 = "Amit"
```

we can store the values together:

```python
students = ["Onkar", "Rahul", "Amit"]
```

A Python list is **ordered, mutable, indexed, iterable, and allows duplicate values**. A list can also contain different data types.

Lists are important in Data Engineering because Python programs frequently work with collections such as file names, column names, validation errors, API results, and batches of records.

---

## Table of Contents

- [1. What is a List?](#1-what-is-a-list)
- [2. Creating Lists](#2-creating-lists)
- [3. Indexing](#3-indexing)
- [4. Negative Indexing](#4-negative-indexing)
- [5. Slicing](#5-slicing)
- [6. Mutability](#6-mutability)
- [7. Adding Elements](#7-adding-elements)
- [8. Removing Elements](#8-removing-elements)
- [9. Useful Functions](#9-useful-functions)
- [10. Traversing Lists](#10-traversing-lists)
- [11. Searching Lists](#11-searching-lists)
- [12. Nested Lists](#12-nested-lists)
- [13. Copying Lists](#13-copying-lists)
- [14. Sorting Lists](#14-sorting-lists)
- [15. Reversing Lists](#15-reversing-lists)
- [16. List Unpacking](#16-list-unpacking)
- [17. List vs Tuple](#17-list-vs-tuple)
- [18. Common Mistakes](#18-common-mistakes)
- [19. Interview Follow-up Questions](#19-interview-follow-up-questions)
- [20. Data Engineering Perspective](#20-data-engineering-perspective)

---

# 1. What is a List?

A list stores multiple values inside square brackets `[]`.

```python
numbers = [10, 20, 30, 40]
```

Here, `numbers` refers to one list containing four elements.

### Important Properties

| Property | Meaning |
|---|---|
| Ordered | Elements maintain their position |
| Mutable | Elements can be changed after creation |
| Indexed | Elements can be accessed using positions |
| Iterable | Elements can be processed one by one |
| Duplicates allowed | The same value can appear multiple times |
| Different types allowed | A list can contain different Python objects |

Example:

```python
values = [10, "Python", 3.14, True]
```

This is valid Python.

> [!IMPORTANT]
> For interviews, remember the two most important properties first: **lists are ordered and mutable**.

---

# 2. Creating Lists

## 2.1 List with Values

```python
numbers = [10, 20, 30]
```

The list contains three elements.

## 2.2 Empty List

```python
numbers = []
```

An empty list contains zero elements. We commonly create one when values will be added later.

```python
numbers = []
numbers.append(10)
numbers.append(20)
```

Result:

```text
[10, 20]
```

## 2.3 Using `list()`

`list()` creates a list from an iterable.

```python
letters = list("Python")
```

Result:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

The string is processed character by character.

> [!NOTE]
> `list()` is commonly used when we need to convert an iterable into an actual list.

---

# 3. Indexing

Because lists are ordered, every element has an **index**.

Python uses **zero-based indexing**.

```text
Value:  10   20   30   40
Index:   0    1    2    3
```

Given:

```python
numbers = [10, 20, 30, 40]
```

we can access an element using:

```python
print(numbers[0])
```

Output:

```text
10
```

`numbers[0]` means: get the element at index `0`.

Similarly:

```python
print(numbers[2])
```

Output:

```text
30
```

> [!WARNING]
> Accessing an index that does not exist raises `IndexError`.

---

# 4. Negative Indexing

Negative indexes start from the right side.

```text
Value:      10    20    30    40
Positive:    0     1     2     3
Negative:   -4    -3    -2    -1
```

The last element is always at `-1`.

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

Negative indexing is useful when we want elements from the end without calculating the length of the list.

---

# 5. Slicing

Slicing extracts a portion of a list.

### Syntax

```text
list[start : stop : step]
```

- `start` → starting index
- `stop` → ending boundary, **not included**
- `step` → number of positions to move

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

Index `4` is not included.

### Omitting Start

```python
print(numbers[:3])
```

Output:

```text
[10, 20, 30]
```

### Omitting Stop

```python
print(numbers[2:])
```

Output:

```text
[30, 40, 50]
```

### Using Step

```python
print(numbers[0:5:2])
```

Output:

```text
[10, 30, 50]
```

### Reverse Using Slicing

```python
print(numbers[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

> [!IMPORTANT]
> The `stop` position in slicing is exclusive.

---

# 6. Mutability

**Mutable** means an object can be changed after it has been created.

Lists are mutable.

```python
numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)
```

Output:

```text
[10, 200, 30]
```

We changed the existing element at index `1`.

### List vs String

A string is immutable:

```python
text = "Python"
```

This raises `TypeError`:

```python
text[0] = "J"
```

But a list can be changed:

```python
letters = ["P", "y", "t", "h", "o", "n"]
letters[0] = "J"
```

Result:

```text
['J', 'y', 't', 'h', 'o', 'n']
```

> [!IMPORTANT]
> **List = mutable. String = immutable. Tuple = immutable.**

---

# 7. Adding Elements

The three important methods are `append()`, `insert()`, and `extend()`.

## 7.1 `append()`

`append()` adds **one object** to the end of the list.

### Syntax

```python
list.append(value)
```

Example:

```python
numbers = [10, 20]
numbers.append(30)
print(numbers)
```

Output:

```text
[10, 20, 30]
```

If we append another list:

```python
numbers.append([40, 50])
```

the result is:

```text
[10, 20, 30, [40, 50]]
```

The entire `[40, 50]` is added as **one element**.

---

## 7.2 `insert()`

`insert()` adds an element at a specific index.

### Syntax

```python
list.insert(index, value)
```

Example:

```python
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)
```

Output:

```text
[10, 15, 20, 30]
```

The existing elements shift to the right.

---

## 7.3 `extend()`

`extend()` adds elements from another iterable individually.

```python
numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

### `append()` vs `extend()`

```text
append([3, 4]) → [1, 2, [3, 4]]
extend([3, 4]) → [1, 2, 3, 4]
```

> [!TIP]
> Interview rule: `append()` adds one object; `extend()` adds elements from an iterable.

---

# 8. Removing Elements

Python provides `remove()`, `pop()`, `del`, and `clear()`.

## 8.1 `remove()`

`remove()` removes the **first matching value**.

```python
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)
```

Output:

```text
[10, 30, 20]
```

Only the first `20` is removed.

If the value does not exist, Python raises `ValueError`.

## 8.2 `pop()`

`pop()` removes an element by index and **returns the removed value**.

```python
numbers = [10, 20, 30]
value = numbers.pop(1)

print(value)
print(numbers)
```

Output:

```text
20
[10, 30]
```

Without an index, `pop()` removes the last element.

## 8.3 `del`

`del` removes an element or a slice using an index.

```python
numbers = [10, 20, 30]
del numbers[1]
print(numbers)
```

Output:

```text
[10, 30]
```

## 8.4 `clear()`

`clear()` removes all elements from the list.

```python
numbers = [10, 20, 30]
numbers.clear()
print(numbers)
```

Output:

```text
[]
```

### Comparison

| Operation | Removes by | Returns removed value? |
|---|---|---|
| `remove(value)` | Value | No |
| `pop(index)` | Index | Yes |
| `del list[index]` | Index/slice | No |
| `clear()` | Everything | No |

---

# 9. Useful Functions

## `len()`

Returns the number of elements.

```python
numbers = [10, 20, 30, 40]
print(len(numbers))
```

Output:

```text
4
```

## `max()` and `min()`

```python
numbers = [10, 50, 20, 40]

print(max(numbers))
print(min(numbers))
```

Output:

```text
50
10
```

## `sum()`

Adds numeric elements.

```python
numbers = [10, 20, 30]
print(sum(numbers))
```

Output:

```text
60
```

---

# 10. Traversing Lists

**Traversing** means visiting each element one by one.

The most common approach is a `for` loop:

```python
languages = ["Python", "SQL", "Snowflake"]

for language in languages:
    print(language)
```

Output:

```text
Python
SQL
Snowflake
```

Python automatically assigns each element to `language` during each iteration.

We can also traverse using indexes:

```python
for index in range(len(languages)):
    print(index, languages[index])
```

Output:

```text
0 Python
1 SQL
2 Snowflake
```

---

# 11. Searching Lists

Use `in` when we want to check whether a value exists.

```python
languages = ["Python", "SQL", "Snowflake"]

print("Python" in languages)
print("Java" in languages)
```

Output:

```text
True
False
```

`not in` checks that a value does not exist:

```python
print("Java" not in languages)
```

Output:

```text
True
```

### `index()`

`index()` returns the position of the first matching value.

```python
print(languages.index("SQL"))
```

Output:

```text
1
```

If the value is not found, `index()` raises `ValueError`.

---

# 12. Nested Lists

A list can contain other lists. This is called a **nested list**.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

To access `5`:

```python
print(matrix[1][1])
```

Output:

```text
5
```

`matrix[1]` selects `[4, 5, 6]`, and `[1]` then selects `5` from that inner list.

Nested lists can be processed with nested loops:

```python
for row in matrix:
    for value in row:
        print(value)
```

---

# 13. Copying Lists

Because lists are mutable, we need to understand the difference between **assignment and copying**.

## Assignment

```python
x = [1, 2, 3]
y = x
```

This does not create a new list. Both variables refer to the same list.

```text
x ─────┐
       ↓
   [1, 2, 3]
       ↑
       └───── y
```

Therefore:

```python
y.append(4)
print(x)
print(y)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

## Shallow Copy

Use `copy()` when you want a separate outer list:

```python
x = [1, 2, 3]
y = x.copy()

y.append(4)

print(x)
print(y)
```

Output:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

This is called a **shallow copy**. Nested mutable objects require additional care, which will be covered later with Python memory concepts.

---

# 14. Sorting Lists

`sort()` changes the original list and sorts it in place.

```python
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

For descending order:

```python
numbers.sort(reverse=True)
```

### `sort()` Returns `None`

```python
numbers = [3, 1, 2]
result = numbers.sort()
print(result)
```

Output:

```text
None
```

This happens because `sort()` modifies the existing list instead of returning a new list.

### `sorted()`

`sorted()` returns a new sorted result.

```python
numbers = [3, 1, 2]
result = sorted(numbers)

print(result)
print(numbers)
```

Output:

```text
[1, 2, 3]
[3, 1, 2]
```

### `sort()` vs `sorted()`

| `sort()` | `sorted()` |
|---|---|
| List method | Built-in function |
| Changes original list | Returns a new result |
| Returns `None` | Returns sorted result |
| Used on lists | Works with many iterables |

---

# 15. Reversing Lists

## `reverse()`

`reverse()` modifies the original list.

```python
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)
```

Output:

```text
[4, 3, 2, 1]
```

## Slicing

`[::-1]` creates a reversed list.

```python
numbers = [1, 2, 3, 4]
reversed_numbers = numbers[::-1]
print(reversed_numbers)
```

Output:

```text
[4, 3, 2, 1]
```

The important difference is that `reverse()` modifies the original list, while slicing creates another list.

---

# 16. List Unpacking

List unpacking allows us to assign list elements to multiple variables.

```python
numbers = [10, 20, 30]
a, b, c = numbers
```

Now:

```text
a = 10
b = 20
c = 30
```

Python also supports starred unpacking:

```python
numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers
```

Result:

```text
first  = 10
middle = [20, 30, 40]
last   = 50
```

---

# 17. List vs Tuple

Both lists and tuples are ordered collections, but their mutability is different.

| List | Tuple |
|---|---|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Can be modified | Cannot be modified after creation |
| Useful for changing collections | Useful for fixed collections |

Example:

```python
numbers = [10, 20, 30]
numbers[0] = 100
```

This works because the list is mutable.

But:

```python
numbers = (10, 20, 30)
numbers[0] = 100
```

raises `TypeError` because tuples are immutable.

Tuples will be studied in detail in **Day 15**.

---

# 18. Common Mistakes

### Mistake 1: Invalid Index

```python
numbers = [10, 20]
print(numbers[2])
```

Valid indexes are `0` and `1`, so this raises `IndexError`.

### Mistake 2: Confusing `append()` and `extend()`

```text
append([3, 4]) → [1, 2, [3, 4]]
extend([3, 4]) → [1, 2, 3, 4]
```

### Mistake 3: Assuming `y = x` Creates a Copy

```python
x = [1, 2, 3]
y = x
```

Both variables refer to the same list. Use `x.copy()` for a separate shallow copy.

### Mistake 4: Expecting `sort()` to Return a List

```python
result = numbers.sort()
```

`result` becomes `None`.

Use `sorted(numbers)` when you need a new sorted result.

### Mistake 5: Forgetting that Slice Stop is Exclusive

```python
numbers = [10, 20, 30, 40]
print(numbers[1:3])
```

Output:

```text
[20, 30]
```

Index `3` is not included.

---

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is the difference between `append()` and `extend()`?

<details>
<summary><strong>Answer</strong></summary>

`append()` adds the entire object as **one element**, while `extend()` adds elements from an iterable individually.

```python
numbers = [1, 2]

numbers.append([3, 4])
print(numbers)
```

Output:

```text
[1, 2, [3, 4]]
```

With `extend()`:

```python
numbers = [1, 2]

numbers.extend([3, 4])
print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

The key difference is **one object vs. elements from an iterable**.

</details>

---

### Q2. If `x = [1, 2, 3]` and `y = x`, what happens when you modify `y`?

<details>
<summary><strong>Answer</strong></summary>

`x` and `y` refer to the **same list object**.

```python
x = [1, 2, 3]
y = x

y.append(4)

print(x)
print(y)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

If you need a separate shallow copy:

```python
y = x.copy()
```

This question tests **object references and mutability**.

</details>

---

### Q3. Suppose a list contains 10 million records. Would you always store the entire dataset in a Python list?

<details>
<summary><strong>Answer</strong></summary>

No.

A Python list keeps references to its elements in memory. Loading a very large dataset into one list can create significant memory pressure.

For large-scale Data Engineering workloads, consider:

- Generators
- Iterators
- Streaming
- Batch processing
- DataFrames
- Distributed processing

The correct approach depends on data size, transformation requirements, and available resources.

</details>

---

### Q4. You need to remove every occurrence of `10` from a list. Would `remove()` solve the problem?

<details>
<summary><strong>Answer</strong></summary>

No. `remove()` removes only the **first matching occurrence**.

```python
numbers = [10, 20, 10, 30, 10]

numbers.remove(10)

print(numbers)
```

Output:

```text
[20, 10, 30, 10]
```

To remove all occurrences, one approach is:

```python
numbers = [10, 20, 10, 30, 10]

numbers = [x for x in numbers if x != 10]

print(numbers)
```

Output:

```text
[20, 30]
```

This also introduces list comprehensions, which will be studied later.

</details>

---

### Q5. What is the difference between `sort()` and `sorted()`?

<details>
<summary><strong>Answer</strong></summary>

`sort()` is a list method that changes the original list and returns `None`.

```python
numbers = [3, 1, 2]

result = numbers.sort()

print(numbers)
print(result)
```

Output:

```text
[1, 2, 3]
None
```

`sorted()` creates and returns a new sorted result:

```python
numbers = [3, 1, 2]

result = sorted(numbers)

print(numbers)
print(result)
```

Output:

```text
[3, 1, 2]
[1, 2, 3]
```

</details>

---

### Q6. A list contains nested lists. Is `copy()` a deep copy?

<details>
<summary><strong>Answer</strong></summary>

No. `copy()` creates a **shallow copy**.

The outer list is copied, but nested mutable objects can still be shared.

```python
original = [[1, 2], [3, 4]]
copy_list = original.copy()

copy_list[0].append(99)

print(original)
print(copy_list)
```

Both can show the changed nested list because the inner list is shared.

For a true deep copy of nested structures, Python provides `copy.deepcopy()`.

</details>

---

### Q7. You need both the position and value while traversing a list. Would you use a normal `for value in list` loop?

<details>
<summary><strong>Answer</strong></summary>

A normal loop gives the value directly, but not the index.

You can use `enumerate()` when both are required:

```python
languages = ["Python", "SQL", "Snowflake"]

for index, language in enumerate(languages):
    print(index, language)
```

Output:

```text
0 Python
1 SQL
2 Snowflake
```

`enumerate()` is generally clearer than manually using `range(len(list))`.

</details>

---

### Q8. A pipeline receives a very large file. Why might repeatedly using `append()` to build one huge list be a problem?

<details>
<summary><strong>Answer</strong></summary>

Repeatedly appending records to one large list means the records remain in memory until the list is released.

For a large file, this can lead to high memory consumption and potentially an out-of-memory failure.

A scalable pipeline may instead process the data in **batches**, stream records, or use generators so that the entire dataset does not need to remain in memory at once.

The key Data Engineering consideration is not whether `append()` works, but whether the chosen in-memory data structure scales with the dataset size.

</details>

---

# 20. Data Engineering Perspective

Lists are useful for **small and intermediate collections** in Data Engineering scripts.

## Column Names

```python
columns = [
    "customer_id",
    "customer_name",
    "email",
    "created_at"
]
```

We can iterate through these columns or pass them to another function.

## File Names

```python
files = [
    "customers.csv",
    "orders.csv",
    "products.csv"
]

for file in files:
    print(file)
```

This pattern is useful when a pipeline needs to process a collection of files.

## Validation Errors

```python
errors = []

errors.append("Missing customer_id")
errors.append("Invalid email")
```

The list acts as an accumulator for validation failures.

## Batch of Records

```python
records = [
    (101, "Onkar", "onkar@example.com"),
    (102, "Rahul", "rahul@example.com"),
    (103, "Amit", "amit@example.com")
]
```

Here the list contains multiple tuples, with each tuple representing one record.

## Memory Consideration

A list keeps its elements in memory. Therefore, loading a very large dataset into one Python list can cause high memory usage.

For large-scale processing, Data Engineers may use:

- Generators
- Iterators
- Streaming
- Batch processing
- DataFrames
- Distributed processing

> [!IMPORTANT]
> Learning lists is not only about syntax. As a Data Engineer, you should understand when an in-memory list is appropriate and when the dataset is too large for this approach.

---

## Navigation

⬅️ **Previous:** [Day 13 - Strings](../Day_13_Strings/readme.md)

➡️ **Next:** [Day 15 - Tuples](../Day_15_Tuples/readme.md)
