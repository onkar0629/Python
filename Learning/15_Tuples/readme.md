# 🐍 Day 15 - Tuples

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

A **tuple** is an ordered collection of values in Python.

Tuples are similar to lists because they can store multiple values, support indexing and slicing, and can contain duplicate values. The most important difference is that **tuples are immutable**.

For example:

```python
student = (101, "Onkar", "Data Engineer")
```

Once this tuple has been created, its individual elements cannot be changed.

Tuples are useful when we want to represent a collection of values that should remain fixed. They are also commonly used for records, coordinates, configuration values, dictionary keys, and returning multiple values from a function.

> [!IMPORTANT]
> The most important interview point for Day 15 is: **list = mutable, tuple = immutable**.

---

## Table of Contents

- [1. What is a Tuple?](#1-what-is-a-tuple)
- [2. Creating Tuples](#2-creating-tuples)
- [3. The Single-Element Tuple](#3-the-single-element-tuple)
- [4. Tuple Indexing](#4-tuple-indexing)
- [5. Negative Indexing](#5-negative-indexing)
- [6. Tuple Slicing](#6-tuple-slicing)
- [7. Tuple Immutability](#7-tuple-immutability)
- [8. What Can and Cannot Be Changed?](#8-what-can-and-cannot-be-changed)
- [9. Tuple Packing](#9-tuple-packing)
- [10. Tuple Unpacking](#10-tuple-unpacking)
- [11. Extended Unpacking](#11-extended-unpacking)
- [12. Tuple Methods](#12-tuple-methods)
- [13. Searching in a Tuple](#13-searching-in-a-tuple)
- [14. Looping Through a Tuple](#14-looping-through-a-tuple)
- [15. Nested Tuples](#15-nested-tuples)
- [16. Converting Between List and Tuple](#16-converting-between-list-and-tuple)
- [17. Tuple Assignment and References](#17-tuple-assignment-and-references)
- [18. Tuple vs List](#18-tuple-vs-list)
- [19. When Should You Use a Tuple?](#19-when-should-you-use-a-tuple)
- [20. Common Mistakes](#20-common-mistakes)
- [21. Interview Follow-up Questions](#21-interview-follow-up-questions)
- [22. Data Engineering Perspective](#22-data-engineering-perspective)

---

# 1. What is a Tuple?

A tuple is an **ordered, immutable collection** of values.

Tuples are usually written using parentheses `()`:

```python
numbers = (10, 20, 30, 40)
```

Here, `numbers` contains four elements.

Like lists, tuples:

- Maintain order
- Use zero-based indexing
- Support negative indexing
- Support slicing
- Allow duplicate values
- Can contain different data types
- Are iterable

The major difference is mutability.

| List | Tuple |
|---|---|
| Mutable | Immutable |
| `[]` | `()` |
| Can be changed | Cannot change existing elements |
| More suitable for changing collections | More suitable for fixed collections |

Consider:

```python
student = (101, "Onkar", "Data Engineer")
```

The tuple can be read and processed, but its existing elements cannot be replaced.

> [!IMPORTANT]
> **Ordered does not mean mutable.** A tuple is ordered, but immutable.

---

# 2. Creating Tuples

## 2.1 Tuple with Multiple Elements

```python
numbers = (10, 20, 30)
```

The parentheses make the tuple easy to identify.

## 2.2 Tuple Without Parentheses

Python also allows tuple creation through **commas**:

```python
numbers = 10, 20, 30
```

Python interprets this as a tuple:

```text
(10, 20, 30)
```

This is important because the comma, not the parentheses alone, is what creates the tuple in many tuple-assignment situations.

## 2.3 Empty Tuple

An empty tuple is created using:

```python
empty = ()
```

## 2.4 Using `tuple()`

The `tuple()` constructor converts an iterable into a tuple.

```python
numbers = tuple([10, 20, 30])
```

The list is converted to:

```text
(10, 20, 30)
```

A string can also be converted:

```python
letters = tuple("Python")
```

Result:

```text
('P', 'y', 't', 'h', 'o', 'n')
```

> [!NOTE]
> `tuple()` consumes an iterable and creates a tuple containing its elements.

---

# 3. The Single-Element Tuple

This is one of the most important tuple syntax rules.

A single value inside parentheses is **not automatically a tuple**.

```python
value = (10)
```

Here `value` is an integer, not a tuple.

To create a one-element tuple, we need a **trailing comma**:

```python
value = (10,)
```

Now `value` is a tuple.

We can verify this using `type()`:

```python
print(type((10)))
print(type((10,)))
```

Output:

```text
<class 'int'>
<class 'tuple'>
```

> [!IMPORTANT]
> Remember: **`(10)` is an integer; `(10,)` is a tuple.**

---

# 4. Tuple Indexing

Tuples are ordered, so every element has an index.

Python uses zero-based indexing.

```text
Value:  10   20   30   40
Index:   0    1    2    3
```

Example:

```python
numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

The syntax is the same as list indexing:

```text
tuple[index]
```

The difference is that indexing a tuple gives us a value, but we cannot use indexing to modify that value.

For example:

```python
numbers[0] = 100
```

raises `TypeError` because tuples are immutable.

---

# 5. Negative Indexing

Negative indexing starts from the end of the tuple.

```text
Value:      10    20    30    40
Positive:    0     1     2     3
Negative:   -4    -3    -2    -1
```

The last element is always at `-1`.

```python
numbers = (10, 20, 30, 40)

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

Negative indexing works the same way for lists and tuples.

---

# 6. Tuple Slicing

Tuples support slicing because they are ordered sequences.

### Syntax

```text
 tuple[start : stop : step]
```

Example:

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

The stop index is excluded.

We can omit the start:

```python
print(numbers[:3])
```

Output:

```text
(10, 20, 30)
```

We can omit the stop:

```python
print(numbers[2:])
```

Output:

```text
(30, 40, 50)
```

We can reverse a tuple using a negative step:

```python
print(numbers[::-1])
```

Output:

```text
(50, 40, 30, 20, 10)
```

> [!IMPORTANT]
> Tuple slicing returns a **new tuple**. It does not modify the original tuple.

---

# 7. Tuple Immutability

**Immutable** means the existing object cannot be changed after creation.

Consider:

```python
numbers = (10, 20, 30)
```

This is not allowed:

```python
numbers[0] = 100
```

Python raises:

```text
TypeError: 'tuple' object does not support item assignment
```

Why?

Because tuple elements cannot be reassigned after the tuple is created.

A list behaves differently:

```python
numbers = [10, 20, 30]
numbers[0] = 100
```

This works because a list is mutable.

> [!IMPORTANT]
> Tuple immutability applies to the tuple structure and its element references. It does not automatically make every object stored inside the tuple immutable.

---

# 8. What Can and Cannot Be Changed?

Consider a tuple containing a list:

```python
items = ([1, 2], "Python")
```

We cannot replace the first element:

```python
items[0] = [3, 4]
```

This raises `TypeError` because we are trying to change the tuple.

However, the list stored inside the tuple is itself mutable:

```python
items[0].append(3)

print(items)
```

Output:

```text
([1, 2, 3], 'Python')
```

The tuple still contains the same list object. We changed the **contents of the nested list**, not the tuple's element reference.

This is an important distinction between **tuple immutability** and **object mutability**.

---

# 9. Tuple Packing

**Packing** means putting multiple values into one tuple.

```python
student = 101, "Onkar", "Data Engineer"
```

Python packs these values into:

```text
(101, 'Onkar', 'Data Engineer')
```

The parentheses are optional here because the commas define the tuple structure.

Packing is commonly seen when returning multiple values from a function.

```python
def get_user():
    return 101, "Onkar"
```

The function returns a tuple containing two values.

---

# 10. Tuple Unpacking

**Unpacking** means taking values from a tuple and assigning them to separate variables.

```python
student = (101, "Onkar", "Data Engineer")

student_id, name, role = student
```

Now:

```text
student_id = 101
name       = "Onkar"
role       = "Data Engineer"
```

The number of variables normally needs to match the number of tuple elements.

For example:

```python
numbers = (10, 20, 30)
a, b, c = numbers
```

This works.

But:

```python
a, b = numbers
```

raises `ValueError` because there are three values but only two variables.

---

# 11. Extended Unpacking

Python allows one variable to collect multiple remaining values using `*`.

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers
```

Now:

```text
first  = 10
middle = [20, 30, 40]
last   = 50
```

Notice that `middle` becomes a **list**, even though the original object was a tuple.

We can also collect everything after the first value:

```python
first, *remaining = numbers
```

Result:

```text
first     = 10
remaining = [20, 30, 40, 50]
```

Extended unpacking is useful when we know some positions but want to collect an unknown number of middle values.

---

# 12. Tuple Methods

Tuples have fewer methods than lists because tuples cannot be modified.

The two main tuple methods are:

- `count()`
- `index()`

## `count()`

`count()` returns the number of times a value occurs.

```python
numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))
```

Output:

```text
3
```

## `index()`

`index()` returns the index of the first matching value.

```python
numbers = (10, 20, 30, 20)

print(numbers.index(20))
```

Output:

```text
1
```

If the value does not exist, `index()` raises `ValueError`.

> [!IMPORTANT]
> Lists have many mutation methods such as `append()`, `remove()`, and `sort()`. Tuples do not because tuples are immutable.

---

# 13. Searching in a Tuple

The `in` operator checks whether a value exists.

```python
languages = ("Python", "SQL", "Snowflake")

print("Python" in languages)
print("Java" in languages)
```

Output:

```text
True
False
```

We can also use `not in`:

```python
print("Java" not in languages)
```

Output:

```text
True
```

This works the same way for lists, tuples, strings, and other containers.

---

# 14. Looping Through a Tuple

Tuples are iterable, so we can process their values using a `for` loop.

```python
languages = ("Python", "SQL", "Snowflake")

for language in languages:
    print(language)
```

Output:

```text
Python
SQL
Snowflake
```

We can also use indexes:

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

In most cases, direct iteration is simpler when we do not need the index.

---

# 15. Nested Tuples

A tuple can contain other tuples.

```python
coordinates = (
    (18.52, 73.85),
    (19.07, 72.87)
)
```

To access the latitude of the second location:

```python
print(coordinates[1][0])
```

Output:

```text
19.07
```

The first index selects the inner tuple, and the second index selects the value inside it.

Tuples can also contain lists, dictionaries, or other mutable objects. The mutability of those nested objects is separate from the immutability of the outer tuple.

---

# 16. Converting Between List and Tuple

Sometimes we need to change the collection type.

## List to Tuple

```python
numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
```

Output:

```text
(10, 20, 30)
```

## Tuple to List

```python
numbers_tuple = (10, 20, 30)

numbers_list = list(numbers_tuple)

print(numbers_list)
```

Output:

```text
[10, 20, 30]
```

This is useful when we need to temporarily modify data that is currently stored in a tuple.

For example:

```python
numbers = (10, 20, 30)

numbers = list(numbers)
numbers.append(40)
numbers = tuple(numbers)

print(numbers)
```

Output:

```text
(10, 20, 30, 40)
```

We did not directly modify the original tuple. We created a list, changed the list, and then created a new tuple.

---

# 17. Tuple Assignment and References

Like other Python objects, a tuple variable stores a reference to a tuple object.

```python
x = (10, 20, 30)
y = x
```

Both variables refer to the same immutable tuple.

Because tuples cannot be modified, this does not create the same mutation problem that we saw with lists.

For example:

```python
x = (10, 20, 30)
y = x

print(x is y)
```

Output:

```text
True
```

However, remember that `is` checks **object identity**, not value equality.

Use `==` when the question is whether two tuples contain the same values:

```python
x = (10, 20, 30)
y = (10, 20, 30)

print(x == y)
```

Output:

```text
True
```

---

# 18. Tuple vs List

This is one of the most common Python interview topics.

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[]` | `()` |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicate values | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| `append()` | Yes | No |
| `remove()` | Yes | No |
| `sort()` | Yes | No |
| `count()` | Yes | Yes |
| `index()` | Yes | Yes |
| Typical use | Changing collections | Fixed collections |

### Example

Use a list when values need to change:

```python
pipeline_files = ["customers.csv", "orders.csv"]
pipeline_files.append("products.csv")
```

Use a tuple when the values represent a fixed structure:

```python
record = (101, "Onkar", "Pune")
```

The choice should be based on the behavior you need, not simply on which syntax is shorter.

---

# 19. When Should You Use a Tuple?

Use a tuple when the collection represents a **fixed or logically immutable group of values**.

### Example 1: Coordinates

```python
point = (18.52, 73.85)
```

The latitude and longitude together represent one fixed point.

### Example 2: Database Record

```python
record = (101, "Onkar", "Data Engineer")
```

A tuple can represent one row-like record when the structure is fixed.

### Example 3: Configuration Values

```python
connection_config = ("localhost", 3306, "sales_db")
```

The values represent a fixed configuration structure.

### Example 4: Multiple Return Values

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)
```

The function returns two values packed into a tuple.

> [!NOTE]
> In real Data Engineering code, the decision between list and tuple should consider readability, mutability requirements, APIs, and downstream behavior. Do not assume that tuples are always better simply because they are immutable.

---

# 20. Common Mistakes

## Mistake 1: Forgetting the Comma in a One-Element Tuple

```python
value = (10)
```

This is an integer.

Correct:

```python
value = (10,)
```

This is a tuple.

---

## Mistake 2: Trying to Modify a Tuple

```python
numbers = (10, 20, 30)
numbers[0] = 100
```

This raises `TypeError`.

If modification is required, create a list:

```python
numbers = list(numbers)
numbers[0] = 100
```

---

## Mistake 3: Wrong Number of Variables During Unpacking

```python
numbers = (10, 20, 30)
a, b = numbers
```

This raises `ValueError` because the number of variables does not match the number of values.

---

## Mistake 4: Assuming Tuple Means Everything Inside It Is Immutable

```python
items = ([1, 2], "Python")
items[0].append(3)
```

This is valid because the tuple contains a mutable list.

The tuple structure remains unchanged, while the nested list changes.

---

## Mistake 5: Confusing `==` and `is`

Use `==` to compare values:

```python
x = (1, 2)
y = (1, 2)

print(x == y)
```

Use `is` when you specifically want to test whether two variables refer to the same object.

---

# 21. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. Why would you choose a tuple instead of a list?

<details>
<summary><strong>Answer</strong></summary>

Choose a tuple when the collection represents a **fixed structure** and should not be modified through tuple operations.

For example:

```python
record = (101, "Onkar", "Data Engineer")
```

The tuple communicates that these values form one fixed group.

A list would be more appropriate when the collection is expected to change:

```python
files = ["customers.csv", "orders.csv"]
files.append("products.csv")
```

The important point is not simply that tuples are faster or smaller. The main design reason is the intended **immutability and semantics of the data**.

</details>

---

### Q2. What is the difference between `(10)` and `(10,)`?

<details>
<summary><strong>Answer</strong></summary>

`(10)` is just the integer `10` surrounded by parentheses.

```python
print(type((10)))
```

Output:

```text
<class 'int'>
```

`(10,)` contains a trailing comma, so Python creates a one-element tuple:

```python
print(type((10,)))
```

Output:

```text
<class 'tuple'>
```

The comma is the important part.

</details>

---

### Q3. A tuple is immutable. Can a tuple contain a mutable object?

<details>
<summary><strong>Answer</strong></summary>

Yes.

```python
items = ([1, 2], "Python")

items[0].append(3)

print(items)
```

Output:

```text
([1, 2, 3], 'Python')
```

The tuple still points to the same list object. We did not replace the tuple element; we changed the contents of the mutable list stored inside it.

This is an important distinction between **container immutability** and **mutability of nested objects**.

</details>

---

### Q4. What happens if you try to unpack a 4-element tuple into 3 variables?

<details>
<summary><strong>Answer</strong></summary>

Python raises `ValueError` because the number of values does not match the number of variables.

```python
values = (10, 20, 30, 40)
a, b, c = values
```

The solution can be extended using starred unpacking:

```python
values = (10, 20, 30, 40)
a, b, *remaining = values

print(a)
print(b)
print(remaining)
```

Output:

```text
10
20
[30, 40]
```

</details>

---

### Q5. A function returns three values. What data structure is Python actually returning?

<details>
<summary><strong>Answer</strong></summary>

When a function returns multiple comma-separated values, Python packs them into a tuple.

```python
def get_user():
    return 101, "Onkar", "Pune"

result = get_user()

print(result)
print(type(result))
```

Output:

```text
(101, 'Onkar', 'Pune')
<class 'tuple'>
```

The returned tuple can then be unpacked:

```python
user_id, name, city = get_user()
```

</details>

---

### Q6. Can you sort a tuple directly using `tuple.sort()`?

<details>
<summary><strong>Answer</strong></summary>

No.

Tuples do not have a `sort()` method because sorting in place would require modifying the tuple.

If a sorted tuple is required, use `sorted()` and then convert the result back to a tuple:

```python
numbers = (30, 10, 20)

sorted_numbers = tuple(sorted(numbers))

print(sorted_numbers)
```

Output:

```text
(10, 20, 30)
```

`sorted()` returns a list first, so `tuple()` is used to create the final tuple.

</details>

---

### Q7. If two tuples contain the same values, should you use `==` or `is` to compare them?

<details>
<summary><strong>Answer</strong></summary>

Use `==` when you want to compare values.

```python
x = (10, 20, 30)
y = (10, 20, 30)

print(x == y)
```

Output:

```text
True
```

`is` checks whether both variables refer to the same object. It should not be used as a general value-comparison operator.

</details>

---

### Q8. You receive a tuple from an API, but one value needs to be changed before loading the record into a database. What would you do?

<details>
<summary><strong>Answer</strong></summary>

Because the tuple is immutable, do not try to modify it directly.

Convert it to a list, make the change, and convert it back if a tuple is required downstream.

```python
record = (101, "Onkar", "Pune")

record = list(record)
record[2] = "Mumbai"
record = tuple(record)

print(record)
```

Output:

```text
(101, 'Onkar', 'Mumbai')
```

In production code, the better choice depends on the interface you are working with. If the record is intended to be mutable during transformation, using a list or another appropriate record structure may be clearer.

</details>

---

# 22. Data Engineering Perspective

Tuples appear frequently in Python-based Data Engineering code because they are useful for representing **fixed groups of related values**.

## 22.1 Database Records

A database record can be represented as a tuple:

```python
record = (101, "Onkar", "onkar@example.com")
```

A batch of records can be stored as a list of tuples:

```python
records = [
    (101, "Onkar", "onkar@example.com"),
    (102, "Rahul", "rahul@example.com")
]
```

This pattern is commonly seen when preparing rows for database operations.

## 22.2 Multiple Values from Functions

Data Engineering utilities often need to return multiple related values:

```python
def get_file_metadata():
    return "customers.csv", 1024, "2026-08-12"
```

The returned values are packed into a tuple.

They can be unpacked like this:

```python
file_name, file_size, load_date = get_file_metadata()
```

## 22.3 Fixed Configuration

A tuple can represent a small fixed configuration:

```python
connection = ("localhost", 3306, "sales_db")
```

The tuple communicates that these values belong together as one fixed structure.

## 22.4 Dictionary Keys

Tuples containing hashable elements can be used as dictionary keys.

For example, a geographic coordinate can be represented as:

```python
locations = {
    (18.52, 73.85): "Pune",
    (19.07, 72.87): "Mumbai"
}
```

The tuple represents a fixed pair of coordinates.

## 22.5 ETL and Batch Processing

A common pattern is:

```text
Source data
    ↓
Read records
    ↓
Represent individual records
    ↓
Transform records
    ↓
Load records
```

Tuples can be useful for individual fixed records, while lists can hold collections of those records.

> [!IMPORTANT]
> As a Data Engineer, focus on the **behavior and purpose** of the data structure. Use tuples when immutability and fixed structure are useful; use lists when the collection needs to change.

---

## Navigation

⬅️ **Previous:** [Day 14 - Lists](../Day_14_Lists/readme.md)

➡️ **Next:** [Day 16 - Sets](../Day_16_Sets/readme.md)
