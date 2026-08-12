# 🐍 Day 18 - List Comprehension

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

A **list comprehension** is a concise way to create a new list from an existing iterable.

Instead of writing several lines with a `for` loop and `append()`, we can often express the same transformation in a single readable expression.

For example, the traditional approach is:

```python
numbers = [1, 2, 3, 4]

squares = []

for number in numbers:
    squares.append(number ** 2)
```

The same transformation can be written as:

```python
squares = [number ** 2 for number in numbers]
```

Both produce:

```text
[1, 4, 9, 16]
```

The important thing is not memorizing the one-line syntax. You should understand **what the loop is doing, what value is being produced, and when a condition is applied**.

> [!IMPORTANT]
> List comprehension is a tool for expressing a transformation or filtering operation concisely. It does not make a solution automatically better just because it uses one line.

---

## Table of Contents

- [1. Why List Comprehension?](#1-why-list-comprehension)
- [2. Basic Syntax](#2-basic-syntax)
- [3. Simple Transformation](#3-simple-transformation)
- [4. Understanding the Execution Order](#4-understanding-the-execution-order)
- [5. List Comprehension with Strings](#5-list-comprehension-with-strings)
- [6. Filtering with `if`](#6-filtering-with-if)
- [7. `if-else` in List Comprehension](#7-if-else-in-list-comprehension)
- [8. Nested Loops](#8-nested-loops)
- [9. Nested List Comprehension](#9-nested-list-comprehension)
- [10. Working with Dictionaries and Sets](#10-working-with-dictionaries-and-sets)
- [11. Calling Functions](#11-calling-functions)
- [12. Conditional Transformation](#12-conditional-transformation)
- [13. List Comprehension vs `map()`](#13-list-comprehension-vs-map)
- [14. Readability and When Not to Use It](#14-readability-and-when-not-to-use-it)
- [15. Performance and Memory](#15-performance-and-memory)
- [16. Common Mistakes](#16-common-mistakes)
- [17. Interview Follow-up Questions](#17-interview-follow-up-questions)
- [18. Data Engineering Perspective](#18-data-engineering-perspective)

---

# 1. Why List Comprehension?

Suppose we want the squares of numbers from 1 to 5.

Using a normal loop:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)
```

The loop does three things:

1. Takes one number at a time.
2. Calculates its square.
3. Adds the result to a new list.

A list comprehension expresses the same logic directly:

```python
squares = [number ** 2 for number in numbers]
```

Read it approximately as:

> "Create a list containing `number ** 2` for every `number` in `numbers`."

This is the main idea behind list comprehensions.

---

# 2. Basic Syntax

The basic syntax is:

```text
[expression for item in iterable]
```

For example:

```python
squares = [number ** 2 for number in numbers]
```

Break it into parts:

```text
[ expression     for     item       in      iterable ]
       ↓                  ↓                  ↓
   what to store     current value       source data
```

For the example:

```text
expression → number ** 2
item       → number
iterable   → numbers
```

The expression is evaluated once for each item.

> [!TIP]
> When reading a list comprehension, first identify the **`for` loop**. Then identify the **expression being added to the result list**.

---

# 3. Simple Transformation

A common use is transforming every element.

```python
numbers = [1, 2, 3, 4]

squares = [number ** 2 for number in numbers]
```

Execution conceptually looks like:

```text
number = 1 → 1 ** 2 → 1
number = 2 → 2 ** 2 → 4
number = 3 → 3 ** 2 → 9
number = 4 → 4 ** 2 → 16
```

Final list:

```text
[1, 4, 9, 16]
```

Another example:

```python
numbers = [1, 2, 3, 4]

doubled = [number * 2 for number in numbers]
```

Result:

```text
[2, 4, 6, 8]
```

The original list is not modified. A **new list** is created.

---

# 4. Understanding the Execution Order

Consider:

```python
result = [number * 10 for number in [1, 2, 3]]
```

Do not read it from left to right as ordinary English.

Conceptually, Python performs:

```python
result = []

for number in [1, 2, 3]:
    result.append(number * 10)
```

So:

```text
number = 1 → append(10)
number = 2 → append(20)
number = 3 → append(30)
```

Final result:

```text
[10, 20, 30]
```

Understanding this relationship between the normal loop and the comprehension is more important than memorizing the syntax.

---

# 5. List Comprehension with Strings

Strings are iterable, so we can use them in list comprehensions.

```python
text = "Python"

letters = [character for character in text]
```

Result:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

We can transform each character:

```python
uppercase = [character.upper() for character in text]
```

Result:

```text
['P', 'Y', 'T', 'H', 'O', 'N']
```

We can also extract only specific characters:

```python
vowels = [
    character
    for character in text
    if character.lower() in "aeiou"
]
```

Result:

```text
['o']
```

---

# 6. Filtering with `if`

A list comprehension can contain a condition that decides which elements should be included.

Syntax:

```text
[expression for item in iterable if condition]
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]
```

Result:

```text
[2, 4, 6]
```

The logic is equivalent to:

```python
result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number)
```

The `if` here is a **filter**.

It decides whether the current item should enter the result list.

> [!IMPORTANT]
> In `[expression for item in iterable if condition]`, the `if` at the end is a **filter**, not an `if-else` expression.

---

# 7. `if-else` in List Comprehension

Sometimes we want to include **every item**, but transform it differently depending on a condition.

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]
```

Result:

```text
['odd', 'even', 'odd', 'even', 'odd']
```

Notice the position of `if-else`:

```text
[expression_if_true if condition else expression_if_false for item in iterable]
```

This is different from a filter.

### Filter

```python
[number for number in numbers if number % 2 == 0]
```

Only even numbers appear.

### Conditional transformation

```python
["even" if number % 2 == 0 else "odd" for number in numbers]
```

Every number appears, but its output is transformed.

> [!IMPORTANT]
> **Filter:** `for ... if condition`
>
> **Conditional expression:** `value_if_true if condition else value_if_false`

---

# 8. Nested Loops

List comprehensions can represent nested loops.

Suppose we have:

```python
numbers = [1, 2]
letters = ["A", "B"]
```

A normal nested loop is:

```python
result = []

for number in numbers:
    for letter in letters:
        result.append((number, letter))
```

Result:

```text
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

The equivalent comprehension is:

```python
result = [
    (number, letter)
    for number in numbers
    for letter in letters
]
```

The order of the `for` clauses matches the nesting order of the normal loops.

> [!WARNING]
> Nested comprehensions can become difficult to read. If the logic becomes complicated, use normal loops instead.

---

# 9. Nested List Comprehension

A common example is flattening a nested list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

Normal loops:

```python
result = []

for row in matrix:
    for number in row:
        result.append(number)
```

Result:

```text
[1, 2, 3, 4, 5, 6]
```

List comprehension:

```python
result = [number for row in matrix for number in row]
```

The order matters:

```text
for row in matrix
    ↓
for number in row
    ↓
number
```

This is a useful pattern, but for deeply nested data, explicit loops are usually easier to maintain.

---

# 10. Working with Dictionaries and Sets

List comprehensions can iterate over dictionary keys, values, or items.

### Dictionary Keys

```python
student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}

keys = [key for key in student]
```

Result:

```text
['id', 'name', 'city']
```

### Dictionary Values

```python
values = [value for value in student.values()]
```

### Dictionary Items

```python
items = [item for item in student.items()]
```

A list comprehension can also be used with a set:

```python
numbers = {1, 2, 3, 4}

squares = [number ** 2 for number in numbers]
```

The source can be any iterable, not just a list.

---

# 11. Calling Functions

The expression can call a function for every item.

```python
names = ["onkar", "rahul", "amit"]

uppercase_names = [name.upper() for name in names]
```

Result:

```text
['ONKAR', 'RAHUL', 'AMIT']
```

We can also call our own function:

```python
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4]

squares = [square(number) for number in numbers]
```

Result:

```text
[1, 4, 9, 16]
```

This can be useful when the transformation has already been given a meaningful function name.

---

# 12. Conditional Transformation

We can combine transformation and filtering.

Example: square only positive numbers.

```python
numbers = [-3, -2, -1, 0, 1, 2, 3]

positive_squares = [
    number ** 2
    for number in numbers
    if number > 0
]
```

Result:

```text
[1, 4, 9]
```

The process is:

```text
Take number
    ↓
Check number > 0
    ↓
If true
    ↓
Calculate number ** 2
    ↓
Add result to new list
```

This is a very common pattern in data transformation.

---

# 13. List Comprehension vs `map()`

Some transformations can be written using `map()`.

List comprehension:

```python
numbers = [1, 2, 3, 4]

squares = [number ** 2 for number in numbers]
```

Using `map()`:

```python
squares = list(map(lambda number: number ** 2, numbers))
```

Both produce:

```text
[1, 4, 9, 16]
```

For simple transformations, list comprehension is often easier to read.

However, `map()` returns an iterator in Python 3, so converting it to a list creates the final list.

Do not treat one approach as universally better. Choose based on readability, the surrounding code, and whether lazy iteration is useful.

---

# 14. Readability and When Not to Use It

A list comprehension should remain easy to understand.

Good:

```python
even_numbers = [number for number in numbers if number % 2 == 0]
```

Less readable:

```python
result = [f(x) if condition(x) else g(x) for x in data if valid(x) and other_condition(x)]
```

If a comprehension requires complicated conditions, nested loops, multiple function calls, or difficult side effects, a normal loop may be better.

For example, do not use a comprehension just to perform side effects:

```python
[print(number) for number in numbers]
```

This creates a list of `None` values and uses a comprehension for something it was not designed for.

Prefer:

```python
for number in numbers:
    print(number)
```

> [!IMPORTANT]
> **Readable code is more important than short code.**

---

# 15. Performance and Memory

A list comprehension creates the entire result list in memory.

For example:

```python
numbers = range(1, 1_000_001)

squares = [number ** 2 for number in numbers]
```

The resulting list contains one million values.

This can consume significant memory.

If you only need to process values one at a time, a **generator expression** can be more memory-efficient:

```python
squares = (number ** 2 for number in numbers)
```

The generator produces values lazily instead of creating the entire result list immediately.

Conceptually:

```text
List comprehension
→ create all results now
→ store them in memory

Generator expression
→ produce values when requested
→ do not store all results at once
```

This distinction is especially important in Data Engineering, where datasets can be very large.

> [!TIP]
> For large data streams, do not assume that replacing a loop with a list comprehension solves memory problems. The resulting list still has to fit in memory.

---

# 16. Common Mistakes

## Mistake 1: Confusing Filter with `if-else`

Filter:

```python
[x for x in numbers if x > 0]
```

Only matching values are included.

Conditional transformation:

```python
["positive" if x > 0 else "non-positive" for x in numbers]
```

Every value produces an output.

---

## Mistake 2: Forgetting the Expression

This is invalid:

```python
[x for x in numbers]
```

Actually, this is valid and simply copies the values. The common mistake is misunderstanding that `x` before `for` is the expression that becomes an element in the result list.

For example:

```python
[x * 2 for x in numbers]
```

stores `x * 2`, not the original `x`.

---

## Mistake 3: Accidentally Creating a Huge List

```python
result = [process(x) for x in huge_dataset]
```

This stores every processed result in memory.

For large data, consider whether streaming, a generator, batching, or a DataFrame/distributed processing approach is more appropriate.

---

## Mistake 4: Making a Comprehension Too Complicated

A one-line expression is not automatically better.

If the logic is difficult to explain, use a normal loop or a named function.

---

## Mistake 5: Using Comprehension for Side Effects

Avoid:

```python
[print(x) for x in numbers]
```

Use a normal loop when the goal is a side effect such as printing, logging, or modifying an external object.

---

# 17. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is the difference between a normal `for` loop and a list comprehension?

<details>
<summary><strong>Answer</strong></summary>

Both can create a new list from an iterable.

Normal loop:

```python
numbers = [1, 2, 3, 4]

squares = []

for number in numbers:
    squares.append(number ** 2)
```

List comprehension:

```python
squares = [number ** 2 for number in numbers]
```

The list comprehension is more concise, but the normal loop can be clearer when the logic becomes complicated.

The important point is that list comprehension is primarily a concise syntax for expressing iteration and list construction.

</details>

---

### Q2. What is the difference between `[x for x in numbers if x > 5]` and `[x if x > 5 else 0 for x in numbers]`?

<details>
<summary><strong>Answer</strong></summary>

The first is a **filter**:

```python
[x for x in numbers if x > 5]
```

Only values greater than 5 are included.

The second is a **conditional transformation**:

```python
[x if x > 5 else 0 for x in numbers]
```

Every input value produces an output. Values greater than 5 remain unchanged; all others become `0`.

This distinction is frequently tested in Python interviews.

</details>

---

### Q3. How would you flatten a two-dimensional list using list comprehension?

<details>
<summary><strong>Answer</strong></summary>

Given:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

Use:

```python
flattened = [number for row in matrix for number in row]
```

Result:

```text
[1, 2, 3, 4, 5, 6]
```

The first `for` selects each row. The second `for` selects each value from that row.

</details>

---

### Q4. Does a list comprehension modify the original list?

<details>
<summary><strong>Answer</strong></summary>

Normally, no. A list comprehension creates a **new list**.

```python
numbers = [1, 2, 3]

squares = [number ** 2 for number in numbers]

print(numbers)
print(squares)
```

Output:

```text
[1, 2, 3]
[1, 4, 9]
```

The original list remains unchanged.

However, if the expression itself mutates an object, that mutation can still occur. The comprehension syntax does not make nested objects immutable.

</details>

---

### Q5. Would you use a list comprehension to process 100 million records?

<details>
<summary><strong>Answer</strong></summary>

Not automatically.

A list comprehension creates and stores the entire result list in memory. With 100 million records, this can cause severe memory pressure or an out-of-memory failure.

For large Data Engineering workloads, consider:

- Generators
- Iterators
- Batch processing
- Streaming
- DataFrames
- Distributed processing

The correct approach depends on the workload and where the data resides.

The key interview point is: **concise syntax does not remove memory requirements**.

</details>

---

### Q6. Can a list comprehension contain multiple `for` clauses?

<details>
<summary><strong>Answer</strong></summary>

Yes.

For example:

```python
pairs = [
    (x, y)
    for x in [1, 2]
    for y in ["A", "B"]
]
```

Result:

```text
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

The clauses represent nested loops.

However, multiple nested loops can reduce readability. Use normal loops if the comprehension becomes difficult to understand.

</details>

---

### Q7. What happens if you use `map()` instead of a list comprehension for a transformation?

<details>
<summary><strong>Answer</strong></summary>

`map()` returns an iterator in Python 3.

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

The output is a map object rather than a list.

To materialize the results as a list:

```python
result = list(map(lambda x: x * 2, numbers))
```

Both approaches can be useful. Choose based on readability and whether lazy iteration is useful.

</details>

---

### Q8. What is the difference between a list comprehension and a generator expression?

<details>
<summary><strong>Answer</strong></summary>

A list comprehension creates the complete list immediately:

```python
squares = [x ** 2 for x in range(10)]
```

A generator expression produces values lazily:

```python
squares = (x ** 2 for x in range(10))
```

The list stores all results in memory, while the generator calculates values as they are requested.

For large or streaming workloads, generators can significantly reduce memory usage.

</details>

---

# 18. Data Engineering Perspective

List comprehensions are useful in Data Engineering for **small to moderate in-memory transformations**.

## 18.1 Cleaning Values

For example, normalize column-like values:

```python
names = [" onkar ", " rahul ", " amit "]

clean_names = [name.strip().title() for name in names]
```

Result:

```text
['Onkar', 'Rahul', 'Amit']
```

This is useful when preparing data before loading it into another system.

## 18.2 Filtering Records

Suppose we have records represented by dictionaries:

```python
records = [
    {"id": 101, "status": "active"},
    {"id": 102, "status": "inactive"},
    {"id": 103, "status": "active"}
]
```

We can select active records:

```python
active_records = [
    record
    for record in records
    if record["status"] == "active"
]
```

Result:

```text
[
    {'id': 101, 'status': 'active'},
    {'id': 103, 'status': 'active'}
]
```

## 18.3 Extracting Fields

If only customer IDs are required:

```python
customer_ids = [record["id"] for record in records]
```

This is a simple projection from one structure to another.

## 18.4 File Processing

Suppose we have file names:

```python
files = [
    "customers.csv",
    "orders.csv",
    "products.json",
    "sales.csv"
]
```

We can select CSV files:

```python
csv_files = [file for file in files if file.endswith(".csv")]
```

Result:

```text
['customers.csv', 'orders.csv', 'sales.csv']
```

## 18.5 Important Scalability Lesson

For a small collection:

```python
cleaned = [clean(record) for record in records]
```

can be perfectly reasonable.

For hundreds of millions of records, however, you should not automatically load everything into a Python list and process it with a list comprehension.

A production Data Engineering pipeline may instead use:

```text
Source
  ↓
Streaming / Batch ingestion
  ↓
Distributed or columnar processing
  ↓
Transformation
  ↓
Data Warehouse / Data Lake
```

The correct abstraction depends on data volume and architecture.

> [!IMPORTANT]
> **List comprehension is a Python language feature, not a replacement for a scalable Data Processing Engine.**

---

## Navigation

⬅️ **Previous:** [Day 17 - Dictionaries](../Day_17_Dictionaries/readme.md)

➡️ **Next:** [Day 19 - Advanced Functions](../Day_19_Advanced_Functions/readme.md)
