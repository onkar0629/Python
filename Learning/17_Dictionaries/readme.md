# 🐍 Day 17 - Dictionaries

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

A **dictionary** is a collection that stores data as **key-value pairs**.

Unlike lists and tuples, which are mainly accessed using numeric positions, dictionaries allow us to retrieve a value using a meaningful **key**.

For example:

```python
student = {
    "id": 101,
    "name": "Onkar",
    "role": "Data Engineer"
}
```

Here:

```text
Key       → Value
-------------------------
id        → 101
name      → "Onkar"
role      → "Data Engineer"
```

If we want the student's name, we do not need to remember its numeric position. We use the key:

```python
print(student["name"])
```

Output:

```text
Onkar
```

Dictionaries are one of the most important Python data structures for Data Engineers because they naturally represent structured records, configuration, JSON-like data, API responses, metadata, and lookup tables.

> [!IMPORTANT]
> The key idea for dictionaries is: **key → value**.

---

## Table of Contents

- [1. What is a Dictionary?](#1-what-is-a-dictionary)
- [2. Creating a Dictionary](#2-creating-a-dictionary)
- [3. Dictionary Keys and Values](#3-dictionary-keys-and-values)
- [4. Accessing Values](#4-accessing-values)
- [5. `get()` vs Square Brackets](#5-get-vs-square-brackets)
- [6. Adding and Updating Values](#6-adding-and-updating-values)
- [7. Removing Items](#7-removing-items)
- [8. Checking Whether a Key Exists](#8-checking-whether-a-key-exists)
- [9. Dictionary Length](#9-dictionary-length)
- [10. Iterating Through a Dictionary](#10-iterating-through-a-dictionary)
- [11. `keys()`, `values()`, and `items()`](#11-keys-values-and-items)
- [12. Nested Dictionaries](#12-nested-dictionaries)
- [13. Dictionary Methods](#13-dictionary-methods)
- [14. Copying Dictionaries](#14-copying-dictionaries)
- [15. Dictionary Assignment vs Copy](#15-dictionary-assignment-vs-copy)
- [16. Dictionary Unpacking and Merging](#16-dictionary-unpacking-and-merging)
- [17. Dictionary Comprehension](#17-dictionary-comprehension)
- [18. Keys Must Be Hashable](#18-keys-must-be-hashable)
- [19. Dictionary vs List](#19-dictionary-vs-list)
- [20. Common Mistakes](#20-common-mistakes)
- [21. Interview Follow-up Questions](#21-interview-follow-up-questions)
- [22. Data Engineering Perspective](#22-data-engineering-perspective)

---

# 1. What is a Dictionary?

A dictionary stores data in **key-value pairs**.

The basic structure is:

```text
{
    key: value
}
```

Example:

```python
employee = {
    "id": 101,
    "name": "Onkar",
    "department": "Data Engineering"
}
```

The dictionary contains three key-value pairs.

```text
"id"         → 101
"name"       → "Onkar"
"department" → "Data Engineering"
```

The key identifies the data, while the value stores the actual information.

### Important Properties

| Property | Meaning |
|---|---|
| Key-value based | Data is stored as key-value pairs |
| Mutable | Values can be added, changed, and removed |
| Keys are unique | A key can appear only once in the final dictionary |
| Ordered | Modern Python preserves insertion order |
| Iterable | We can loop through dictionaries |
| Dynamic | Key-value pairs can be added or removed |

> [!NOTE]
> Python dictionaries preserve insertion order as part of the language specification. This does **not** mean dictionaries should be treated like lists where position is the primary way of accessing data.

---

# 2. Creating a Dictionary

## 2.1 Dictionary with Values

```python
student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}
```

Each key is followed by a colon `:` and its value.

The general syntax is:

```text
{key: value, key: value}
```

## 2.2 Empty Dictionary

An empty dictionary is created using:

```python
student = {}
```

> [!WARNING]
> `{}` creates an empty dictionary, **not** an empty set. An empty set is created using `set()`.

## 2.3 Using `dict()`

Python provides the `dict()` constructor:

```python
student = dict(name="Onkar", age=22)
```

Result:

```text
{'name': 'Onkar', 'age': 22}
```

We can also convert suitable key-value pairs into a dictionary:

```python
pairs = [("name", "Onkar"), ("age", 22)]
student = dict(pairs)
```

Result:

```text
{'name': 'Onkar', 'age': 22}
```

---

# 3. Dictionary Keys and Values

A dictionary has two main parts:

```text
Key → Value
```

Example:

```python
student = {
    "id": 101,
    "name": "Onkar"
}
```

Here:

```text
"id"   → key
101     → value

"name" → key
"Onkar" → value
```

### Keys Must Be Unique

Consider:

```python
student = {
    "name": "Onkar",
    "name": "Rahul"
}
```

The second `"name"` replaces the first value.

The final dictionary is:

```text
{'name': 'Rahul'}
```

Therefore, a dictionary cannot retain two separate values under the same key.

### Values Can Be Duplicated

Different keys can have the same value:

```python
students = {
    "student_1": "Pune",
    "student_2": "Pune"
}
```

This is completely valid.

> [!IMPORTANT]
> **Keys must be unique; values do not have to be unique.**

---

# 4. Accessing Values

The most common way to access a dictionary value is by using its key.

```python
student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}

print(student["name"])
```

Output:

```text
Onkar
```

Python looks for the key `"name"` and returns its associated value.

The syntax is:

```text
dictionary[key]
```

### Accessing a Missing Key

If the key does not exist:

```python
print(student["age"])
```

Python raises:

```text
KeyError
```

This behavior is important because it differs from lists, where an invalid numeric position raises `IndexError`.

---

# 5. `get()` vs Square Brackets

Dictionaries provide the `get()` method for retrieving values.

```python
student = {
    "name": "Onkar"
}

print(student.get("name"))
```

Output:

```text
Onkar
```

The important difference appears when the key does not exist.

### Square Brackets

```python
print(student["age"])
```

This raises:

```text
KeyError
```

### `get()`

```python
print(student.get("age"))
```

Output:

```text
None
```

We can also provide a default value:

```python
print(student.get("age", 0))
```

Output:

```text
0
```

This is useful when a missing key is expected or should not cause the program to fail.

> [!TIP]
> Use `dictionary[key]` when the key is required. Use `get()` when the key may be missing and you want controlled behavior.

---

# 6. Adding and Updating Values

Dictionaries are mutable, so we can add new key-value pairs and change existing values.

## 6.1 Adding a New Key

```python
student = {
    "name": "Onkar"
}

student["age"] = 22
```

Now:

```text
{'name': 'Onkar', 'age': 22}
```

If the key does not already exist, Python creates a new key-value pair.

## 6.2 Updating an Existing Key

```python
student["age"] = 23
```

The existing value is replaced.

Now:

```text
{'name': 'Onkar', 'age': 23}
```

The same syntax is therefore used for both:

```text
New key       → add
Existing key  → update
```

## 6.3 Updating Multiple Values with `update()`

```python
student = {
    "name": "Onkar",
    "age": 22
}

student.update({
    "age": 23,
    "city": "Pune"
})
```

Result:

```text
{'name': 'Onkar', 'age': 23, 'city': 'Pune'}
```

Existing keys are updated, while new keys are added.

---

# 7. Removing Items

There are several ways to remove dictionary entries.

## 7.1 `pop()`

`pop(key)` removes the specified key and returns its value.

```python
student = {
    "name": "Onkar",
    "age": 22
}

age = student.pop("age")

print(age)
print(student)
```

Output:

```text
22
{'name': 'Onkar'}
```

If the key does not exist, `pop()` raises `KeyError` unless a default value is supplied.

```python
student.pop("age", None)
```

## 7.2 `del`

`del` removes a specific key-value pair:

```python
student = {
    "name": "Onkar",
    "age": 22
}

del student["age"]
```

Now:

```text
{'name': 'Onkar'}
```

## 7.3 `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

```python
student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}

item = student.popitem()

print(item)
print(student)
```

Output:

```text
('city', 'Pune')
{'name': 'Onkar', 'age': 22}
```

## 7.4 `clear()`

`clear()` removes all key-value pairs:

```python
student.clear()
```

Result:

```text
{}
```

### Removal Comparison

| Method | Purpose | Returns removed value? |
|---|---|---|
| `pop(key)` | Remove a specific key | Yes |
| `del` | Delete a specific key | No |
| `popitem()` | Remove last inserted pair | Yes |
| `clear()` | Remove everything | No |

---

# 8. Checking Whether a Key Exists

The `in` operator checks dictionary **keys**.

```python
student = {
    "name": "Onkar",
    "age": 22
}

print("name" in student)
print("city" in student)
```

Output:

```text
True
False
```

This checks keys, not values.

```python
print("Onkar" in student)
```

Output:

```text
False
```

To check values, use `values()`:

```python
print("Onkar" in student.values())
```

Output:

```text
True
```

> [!IMPORTANT]
> `value in dictionary` checks **keys by default**.

---

# 9. Dictionary Length

`len()` returns the number of key-value pairs.

```python
student = {
    "id": 101,
    "name": "Onkar",
    "city": "Pune"
}

print(len(student))
```

Output:

```text
3
```

There are three key-value pairs, so the length is `3`.

---

# 10. Iterating Through a Dictionary

Dictionaries are iterable.

If we loop directly over a dictionary, Python gives us the **keys**.

```python
student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}

for key in student:
    print(key)
```

Output:

```text
name
age
city
```

If we need values, use `values()`.

If we need both keys and values, use `items()`.

---

# 11. `keys()`, `values()`, and `items()`

These three methods are fundamental for dictionary iteration.

## 11.1 `keys()`

Returns a dynamic view of the dictionary's keys.

```python
student = {
    "name": "Onkar",
    "age": 22
}

for key in student.keys():
    print(key)
```

Output:

```text
name
age
```

## 11.2 `values()`

Returns a view of the values.

```python
for value in student.values():
    print(value)
```

Output:

```text
Onkar
22
```

## 11.3 `items()`

Returns key-value pairs as two-element tuples.

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Onkar
age 22
```

This is usually the cleanest approach when both the key and value are needed.

---

# 12. Nested Dictionaries

A dictionary can contain another dictionary as a value.

Example:

```python
employee = {
    "id": 101,
    "name": "Onkar",
    "address": {
        "city": "Pune",
        "state": "Maharashtra"
    }
}
```

To access the city:

```python
print(employee["address"]["city"])
```

Output:

```text
Pune
```

The first key gives us the nested dictionary:

```text
employee["address"]
```

Then the second key accesses the value inside it:

```text
employee["address"]["city"]
```

Nested dictionaries are common when working with JSON and API responses.

---

# 13. Dictionary Methods

Important dictionary methods include:

| Method | Purpose |
|---|---|
| `get()` | Retrieve a value safely |
| `keys()` | Get keys |
| `values()` | Get values |
| `items()` | Get key-value pairs |
| `update()` | Add/update multiple pairs |
| `pop()` | Remove a specific key |
| `popitem()` | Remove the last inserted pair |
| `setdefault()` | Get a value and optionally create a missing key |
| `clear()` | Remove all pairs |
| `copy()` | Create a shallow copy |

### `setdefault()`

`setdefault()` returns the value for a key. If the key does not exist, it creates the key with the supplied default.

```python
student = {
    "name": "Onkar"
}

age = student.setdefault("age", 22)

print(age)
print(student)
```

Output:

```text
22
{'name': 'Onkar', 'age': 22}
```

If the key already exists, `setdefault()` does not replace its value.

```python
student = {"age": 25}

student.setdefault("age", 22)

print(student)
```

Output:

```text
{'age': 25}
```

---

# 14. Copying Dictionaries

Dictionaries are mutable, so copying them correctly is important.

```python
student = {
    "name": "Onkar",
    "age": 22
}

student_copy = student.copy()
```

Now the two dictionaries are separate outer objects.

```python
student_copy["age"] = 23

print(student)
print(student_copy)
```

Output:

```text
{'name': 'Onkar', 'age': 22}
{'name': 'Onkar', 'age': 23}
```

This is a **shallow copy**.

As with lists, nested mutable objects require additional care.

---

# 15. Dictionary Assignment vs Copy

Consider:

```python
x = {
    "name": "Onkar"
}

y = x
```

`y = x` does not create a new dictionary.

Both variables refer to the same dictionary object.

```text
x ─────┐
       ↓
   {"name": "Onkar"}
       ↑
       └───── y
```

Therefore:

```python
y["name"] = "Rahul"

print(x)
print(y)
```

Output:

```text
{'name': 'Rahul'}
{'name': 'Rahul'}
```

Use:

```python
y = x.copy()
```

when you need a separate shallow copy.

> [!IMPORTANT]
> This is the same reference-vs-copy concept you saw with lists, but dictionaries are especially important because accidental mutation can affect configuration, records, or transformation state.

---

# 16. Dictionary Unpacking and Merging

Python provides the `**` operator for dictionary unpacking.

Consider:

```python
first = {
    "name": "Onkar",
    "age": 22
}

second = {
    "city": "Pune",
    "role": "Data Engineer"
}
```

We can merge them into a new dictionary:

```python
combined = {
    **first,
    **second
}
```

Result:

```text
{
    'name': 'Onkar',
    'age': 22,
    'city': 'Pune',
    'role': 'Data Engineer'
}
```

### Duplicate Keys During Merging

If both dictionaries contain the same key, the value appearing later wins:

```python
first = {"city": "Pune"}
second = {"city": "Mumbai"}

combined = {**first, **second}
```

Result:

```text
{'city': 'Mumbai'}
```

The second dictionary overwrote the first value.

Modern Python also supports the dictionary union operator:

```python
combined = first | second
```

This creates a new dictionary.

For an in-place merge:

```python
first |= second
```

---

# 17. Dictionary Comprehension

Dictionary comprehension provides a concise way to create dictionaries from an iterable.

### Basic Example

Suppose we have numbers:

```python
numbers = [1, 2, 3, 4]
```

We want a dictionary where each number maps to its square.

```python
squares = {number: number ** 2 for number in numbers}
```

Result:

```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

The general syntax is:

```text
{key_expression: value_expression for item in iterable}
```

We can also add a condition:

```python
squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}
```

Result:

```text
{2: 4, 4: 16}
```

Dictionary comprehensions are useful, but readability should come first. Avoid creating extremely complicated comprehensions.

---

# 18. Keys Must Be Hashable

Dictionary keys must be **hashable**.

Common hashable types include:

- `int`
- `float`
- `str`
- `bool`
- `tuple` containing hashable elements

For example:

```python
student = {
    101: "Onkar",
    "city": "Pune"
}
```

This is valid.

A list cannot be used as a dictionary key:

```python
student = {
    [1, 2]: "value"
}
```

This raises:

```text
TypeError: unhashable type: 'list'
```

Why?

Because dictionary keys must have a stable hash value while they are used by the dictionary's hash table.

A tuple can be a key if all of its elements are hashable:

```python
locations = {
    (18.52, 73.85): "Pune"
}
```

This is valid.

But a tuple containing a list cannot be a key:

```python
key = ([1, 2], 3)
```

because the list inside it is unhashable.

> [!IMPORTANT]
> A common interview question is: **Why can a tuple be a dictionary key but a list cannot?** The answer is related to hashability and immutability.

---

# 19. Dictionary vs List

Lists and dictionaries solve different problems.

| List | Dictionary |
|---|---|
| Stores values in sequence | Stores key-value pairs |
| Access by index | Access by key |
| Best when position/order is central | Best when named lookup is central |
| `data[0]` | `data["name"]` |
| Duplicate values allowed | Keys must be unique |
| Mutable | Mutable |

### Example

Use a list when you have a sequence:

```python
skills = ["Python", "SQL", "Snowflake"]
```

Use a dictionary when each value has a meaningful label:

```python
student = {
    "name": "Onkar",
    "age": 22,
    "city": "Pune"
}
```

The correct choice depends on how the data needs to be accessed.

---

# 20. Common Mistakes

## Mistake 1: Using `{}` for an Empty Set

```python
data = {}
```

This creates a dictionary.

For an empty set:

```python
data = set()
```

---

## Mistake 2: Confusing Keys and Values

```python
student = {"name": "Onkar"}

print("name" in student)
```

This checks the key and returns `True`.

But:

```python
print("Onkar" in student)
```

checks keys by default and returns `False`.

Use:

```python
print("Onkar" in student.values())
```

when checking values.

---

## Mistake 3: Accessing a Missing Key with `[]`

```python
student["age"]
```

raises `KeyError` if `"age"` does not exist.

Use `get()` when a missing key is acceptable:

```python
student.get("age")
```

---

## Mistake 4: Assuming `y = x` Creates a Copy

```python
x = {"name": "Onkar"}
y = x
```

Both variables refer to the same dictionary.

Use:

```python
y = x.copy()
```

for a shallow copy.

---

## Mistake 5: Assuming Duplicate Keys Are Preserved

```python
student = {
    "name": "Onkar",
    "name": "Rahul"
}
```

The final value is:

```text
{'name': 'Rahul'}
```

The second assignment overwrites the first.

---

# 21. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is the difference between `dictionary[key]` and `dictionary.get(key)`?

<details>
<summary><strong>Answer</strong></summary>

Both can retrieve a value, but they behave differently when the key does not exist.

```python
student = {"name": "Onkar"}

print(student["name"])
print(student.get("name"))
```

Both return:

```text
Onkar
```

But:

```python
student["age"]
```

raises `KeyError`, while:

```python
student.get("age")
```

returns `None`.

You can also provide a default:

```python
student.get("age", 0)
```

which returns `0`.

Use square brackets when a missing key should be treated as an error. Use `get()` when the key may legitimately be absent.

</details>

---

### Q2. What happens if a dictionary contains the same key twice?

<details>
<summary><strong>Answer</strong></summary>

The later value replaces the earlier value.

```python
student = {
    "name": "Onkar",
    "name": "Rahul"
}

print(student)
```

Output:

```text
{'name': 'Rahul'}
```

A dictionary cannot retain two separate values under the same key.

</details>

---

### Q3. Why can a tuple be used as a dictionary key but a list cannot?

<details>
<summary><strong>Answer</strong></summary>

Dictionary keys must be **hashable**.

A tuple containing only hashable elements is hashable because its contents cannot be changed.

```python
locations = {
    (18.52, 73.85): "Pune"
}
```

A list is mutable, so it is unhashable:

```python
locations = {
    [18.52, 73.85]: "Pune"
}
```

This raises `TypeError`.

The important interview concept is **hashability**, not simply the syntax of the data structure.

</details>

---

### Q4. What is the difference between `pop()`, `popitem()`, and `del` for dictionaries?

<details>
<summary><strong>Answer</strong></summary>

`pop(key)` removes a specific key and returns its value.

```python
value = data.pop("name")
```

`popitem()` removes and returns the last inserted key-value pair.

```python
item = data.popitem()
```

`del` removes a specified key but does not return the removed value.

```python
del data["name"]
```

The choice depends on whether you need the removed value and how you identify the item.

</details>

---

### Q5. You need to count how many times each word appears in a large list. Would a dictionary be appropriate?

<details>
<summary><strong>Answer</strong></summary>

Yes. A dictionary can map each word to its count.

```python
words = ["sql", "python", "sql", "python", "sql"]

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
```

Output:

```text
{'sql': 3, 'python': 2}
```

`get(word, 0)` provides `0` when the word has not been seen before.

For production Python, `collections.Counter` is another specialized option for frequency counting, but understanding the dictionary approach is fundamental.

</details>

---

### Q6. If `x = {"a": 1}` and `y = x`, what happens when `y["a"] = 100`?

<details>
<summary><strong>Answer</strong></summary>

Both variables refer to the same dictionary object.

```python
x = {"a": 1}
y = x

y["a"] = 100

print(x)
print(y)
```

Output:

```text
{'a': 100}
{'a': 100}
```

If an independent shallow copy is required:

```python
y = x.copy()
```

This tests understanding of **references, mutability, and copying**.

</details>

---

### Q7. You receive a JSON response containing nested dictionaries. How would you access a value three levels deep?

<details>
<summary><strong>Answer</strong></summary>

Use the appropriate key at each level.

For example:

```python
response = {
    "data": {
        "customer": {
            "name": "Onkar"
        }
    }
}

name = response["data"]["customer"]["name"]

print(name)
```

Output:

```text
Onkar
```

In production code, if any intermediate key may be missing, blindly chaining `[]` can raise `KeyError`. In that case, validation or controlled access using `get()` may be more appropriate.

</details>

---

### Q8. A dictionary contains 10 million records. Is dictionary lookup still useful, and what should you consider?

<details>
<summary><strong>Answer</strong></summary>

Dictionary lookup is generally very efficient because dictionaries are implemented using hash-table-based lookup. Average-case key lookup is approximately **O(1)**.

However, a dictionary with 10 million entries can consume substantial memory.

For a Data Engineering workload, consider:

- Whether the entire mapping must be in memory.
- Whether a database lookup is more appropriate.
- Whether the data can be processed in batches.
- Whether a distributed key-value or data-processing system is required.
- Whether the lookup data can be reduced to only the required keys.

The key interview point is that **algorithmic lookup efficiency does not eliminate memory constraints**.

</details>

---

# 22. Data Engineering Perspective

Dictionaries are extremely important in Data Engineering because many real-world data formats naturally map to key-value structures.

## 22.1 JSON and API Responses

JSON objects map naturally to Python dictionaries.

Example:

```python
customer = {
    "customer_id": 101,
    "name": "Onkar",
    "email": "onkar@example.com"
}
```

API responses commonly contain nested dictionaries and lists.

```text
API Response
    ↓
Python dictionary
    ↓
Extract fields
    ↓
Transform data
    ↓
Load into database / warehouse
```

## 22.2 Configuration

Dictionaries are useful for storing configuration values:

```python
config = {
    "database": "sales_db",
    "host": "localhost",
    "port": 3306,
    "batch_size": 1000
}
```

The keys make each configuration value easy to identify.

## 22.3 Data Transformation

Suppose we receive a record and want to transform it:

```python
record = {
    "first_name": "Onkar",
    "last_name": "Jadhav"
}

record["full_name"] = (
    record["first_name"] + " " + record["last_name"]
)
```

The dictionary makes it straightforward to add derived fields.

## 22.4 Lookup Tables

A dictionary can act as a small in-memory lookup table:

```python
country_codes = {
    "IN": "India",
    "US": "United States",
    "UK": "United Kingdom"
}
```

Then:

```python
print(country_codes.get("IN"))
```

Output:

```text
India
```

This can be useful when the lookup dataset is small enough to keep in memory.

## 22.5 Data Validation

A dictionary can store validation results:

```python
validation = {
    "customer_id_valid": True,
    "email_valid": True,
    "age_valid": False
}
```

The named keys make the validation state easy to understand and process.

## 22.6 Grouping and Aggregation

Dictionaries can also be used to build simple aggregations:

```python
sales = {
    "Pune": 150000,
    "Mumbai": 230000,
    "Delhi": 180000
}
```

For larger analytical workloads, however, Python dictionaries should not automatically replace databases, DataFrames, or distributed processing systems.

> [!IMPORTANT]
> A dictionary is an excellent in-memory data structure, but **10 million records in memory is still 10 million records in memory**. Always consider memory usage and scalability when designing Data Engineering pipelines.

---

## Navigation

⬅️ **Previous:** [Day 16 - Sets](../Day_16_Sets/readme.md)

➡️ **Next:** [Day 18 - Dictionary Practice](../Day_18_Dictionary-Practice/readme.md)
