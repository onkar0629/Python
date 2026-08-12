# 🐍 Day 16 - Sets

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

A **set** is an unordered collection of **unique elements** in Python.

Sets are especially useful when we care about **uniqueness** rather than the position of each value.

For example, suppose we have:

```python
skills = ["Python", "SQL", "Python", "SQL", "Snowflake"]
```

The list contains duplicate values.

If we convert it to a set:

```python
skills = set(skills)
```

we get only the unique values.

Sets are useful for tasks such as:

- Removing duplicate values
- Checking membership
- Finding common values between collections
- Finding values that exist in one collection but not another
- Comparing groups of values

> [!IMPORTANT]
> The three most important properties to remember are: **sets are unordered, mutable, and contain unique elements**.

---

## Table of Contents

- [1. What is a Set?](#1-what-is-a-set)
- [2. Creating a Set](#2-creating-a-set)
- [3. The Empty Set](#3-the-empty-set)
- [4. Duplicate Values](#4-duplicate-values)
- [5. Unordered Collection](#5-unordered-collection)
- [6. Set Membership](#6-set-membership)
- [7. Adding Elements](#7-adding-elements)
- [8. Updating a Set](#8-updating-a-set)
- [9. Removing Elements](#9-removing-elements)
- [10. Set Operations](#10-set-operations)
- [11. Union](#11-union)
- [12. Intersection](#12-intersection)
- [13. Difference](#13-difference)
- [14. Symmetric Difference](#14-symmetric-difference)
- [15. Subset and Superset](#15-subset-and-superset)
- [16. Disjoint Sets](#16-disjoint-sets)
- [17. Looping Through a Set](#17-looping-through-a-set)
- [18. Converting Between List and Set](#18-converting-between-list-and-set)
- [19. Frozen Sets](#19-frozen-sets)
- [20. Set Comprehension](#20-set-comprehension)
- [21. Set vs List vs Tuple](#21-set-vs-list-vs-tuple)
- [22. When Should You Use a Set?](#22-when-should-you-use-a-set)
- [23. Common Mistakes](#23-common-mistakes)
- [24. Interview Follow-up Questions](#24-interview-follow-up-questions)
- [25. Data Engineering Perspective](#25-data-engineering-perspective)

---

# 1. What is a Set?

A set is a collection of unique elements.

```python
numbers = {10, 20, 30, 40}
```

Unlike a list, a set does not use indexes to access individual elements.

A set has these important properties:

| Property | Meaning |
|---|---|
| Unordered | Elements do not have a user-facing positional order |
| Unique | Duplicate values are automatically removed |
| Mutable | Elements can be added or removed |
| Iterable | We can loop through the elements |
| No indexing | `set[0]` is not supported |

For example:

```python
numbers = {10, 20, 30, 20, 10}

print(numbers)
```

The duplicates are removed, leaving only the unique values.

The exact display order of a set should not be relied upon.

> [!IMPORTANT]
> Use a set when **membership and uniqueness** matter more than element position.

---

# 2. Creating a Set

## 2.1 Set with Values

```python
numbers = {10, 20, 30}
```

The curly braces `{}` are commonly used to create a set containing values.

## 2.2 Set with Different Data Types

A set can contain different hashable data types:

```python
values = {10, "Python", 3.14, True}
```

However, the elements themselves must be **hashable**. For example, a list cannot be a direct set element.

This will fail:

```python
values = {[1, 2], [3, 4]}
```

because lists are mutable and therefore unhashable.

## 2.3 Using `set()`

The `set()` constructor creates a set from an iterable.

```python
numbers = set([10, 20, 30, 20])

print(numbers)
```

The duplicate `20` is removed.

A string can also be converted to a set:

```python
letters = set("Python")
```

The result contains unique characters, but its display order should not be relied upon.

> [!NOTE]
> `set()` is especially useful when converting an existing iterable into a collection of unique elements.

---

# 3. The Empty Set

This is an important syntax rule.

```python
empty = {}
```

This does **not** create an empty set. It creates an empty dictionary.

To create an empty set, use:

```python
empty = set()
```

We can verify the types:

```python
print(type({}))
print(type(set()))
```

Output:

```text
<class 'dict'>
<class 'set'>
```

> [!IMPORTANT]
> **`{}` = empty dictionary**
>
> **`set()` = empty set**

---

# 4. Duplicate Values

One of the main purposes of a set is storing unique values.

Consider:

```python
numbers = {10, 20, 20, 30, 30, 30}

print(numbers)
```

The set contains only one copy of each value.

Conceptually:

```text
Input values:
10  20  20  30  30  30

Unique values:
10  20  30
```

This makes sets useful for removing duplicates from data.

For example:

```python
customer_ids = [101, 102, 101, 103, 102]

unique_customer_ids = set(customer_ids)

print(unique_customer_ids)
```

The result contains each customer ID once.

> [!NOTE]
> Converting a list to a set removes duplicates, but it also removes the original positional ordering information.

---

# 5. Unordered Collection

Sets are not sequence types like lists and tuples.

Consider:

```python
numbers = {10, 20, 30}
```

You cannot reliably say that `10` is at index `0` in a set.

This is invalid:

```python
print(numbers[0])
```

Python raises `TypeError` because sets do not support indexing.

If you need positional access, use a list or tuple.

> [!WARNING]
> Do not write code that depends on the order in which a set happens to print or iterate. Set ordering is not a contract you should rely on.

---

# 6. Set Membership

Sets are particularly useful for checking whether a value exists.

Use the `in` operator:

```python
skills = {"Python", "SQL", "Snowflake"}

print("Python" in skills)
print("Java" in skills)
```

Output:

```text
True
False
```

We can also use `not in`:

```python
print("Java" not in skills)
```

Output:

```text
True
```

Membership checks are one of the most common reasons to use a set.

> [!IMPORTANT]
> Set membership is generally very efficient because sets are implemented using hash-table-based lookup.

---

# 7. Adding Elements

Sets are mutable, so we can add elements after creation.

## 7.1 `add()`

`add()` inserts one element into a set.

```python
numbers = {10, 20}

numbers.add(30)

print(numbers)
```

The set now contains `30`.

If we add a value that already exists:

```python
numbers.add(20)
```

the set still contains only one `20`.

`add()` does not create duplicates.

## 7.2 `update()`

`update()` adds multiple elements from an iterable.

```python
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)
```

The elements `30`, `40`, and `50` are added individually.

### `add()` vs `update()`

```text
add(30)
→ adds one element

update([30, 40])
→ adds elements from the iterable
```

> [!TIP]
> This is similar to the `append()` vs `extend()` distinction for lists, but the behavior is based on set insertion and uniqueness.

---

# 8. Updating a Set

Sets can be changed using methods such as `add()`, `update()`, and the set operation methods.

For example:

```python
skills = {"Python", "SQL"}

skills.update(["Snowflake", "Linux"])

print(skills)
```

The resulting set contains all unique skills.

If a value already exists, it is not duplicated.

```python
skills.update(["Python", "SQL"])
```

The set remains a collection of unique values.

---

# 9. Removing Elements

Python provides several ways to remove elements from a set.

## 9.1 `remove()`

`remove()` deletes a specified element.

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

If the value does not exist, `remove()` raises `KeyError`.

## 9.2 `discard()`

`discard()` also removes a specified element, but it does **not** raise an error if the element does not exist.

```python
numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)
```

The set remains unchanged.

### `remove()` vs `discard()`

| `remove()` | `discard()` |
|---|---|
| Removes an element | Removes an element |
| Raises `KeyError` if missing | Does nothing if missing |

## 9.3 `pop()`

`pop()` removes and returns an arbitrary element from the set.

```python
numbers = {10, 20, 30}

value = numbers.pop()

print(value)
print(numbers)
```

Because sets are unordered, you should **not assume which element** `pop()` will remove.

## 9.4 `clear()`

`clear()` removes all elements.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

Output:

```text
set()
```

---

# 10. Set Operations

Set operations are one of the most important reasons sets are useful.

Suppose we have two sets:

```python
python_skills = {"Python", "SQL", "Git"}

data_engineering_skills = {"SQL", "Python", "Snowflake"}
```

We can compare these sets using mathematical set operations.

The main operations are:

- Union
- Intersection
- Difference
- Symmetric difference

These operations are extremely useful when comparing groups of values.

---

# 11. Union

**Union** returns all unique elements from both sets.

Mathematically:

```text
A ∪ B
```

Python syntax:

```python
A | B
```

Example:

```python
python_skills = {"Python", "SQL", "Git"}
data_engineering_skills = {"SQL", "Python", "Snowflake"}

all_skills = python_skills | data_engineering_skills

print(all_skills)
```

The result contains:

```text
Python, SQL, Git, Snowflake
```

The duplicate `Python` and `SQL` values appear only once.

We can also use the method:

```python
all_skills = python_skills.union(data_engineering_skills)
```

---

# 12. Intersection

**Intersection** returns only the elements that exist in both sets.

Mathematically:

```text
A ∩ B
```

Python syntax:

```python
A & B
```

Example:

```python
python_skills = {"Python", "SQL", "Git"}
data_engineering_skills = {"SQL", "Python", "Snowflake"}

common_skills = python_skills & data_engineering_skills

print(common_skills)
```

The common values are:

```text
Python, SQL
```

We can also use:

```python
common_skills = python_skills.intersection(data_engineering_skills)
```

---

# 13. Difference

**Difference** returns elements that exist in the first set but not in the second set.

Mathematically:

```text
A − B
```

Python syntax:

```python
A - B
```

Example:

```python
python_skills = {"Python", "SQL", "Git"}
data_engineering_skills = {"SQL", "Python", "Snowflake"}

only_python_set = python_skills - data_engineering_skills

print(only_python_set)
```

The result contains `Git` because `Git` is in the first set but not the second.

The direction matters.

```python
data_engineering_skills - python_skills
```

returns `Snowflake`.

> [!IMPORTANT]
> `A - B` and `B - A` are generally different results.

---

# 14. Symmetric Difference

Symmetric difference returns elements that exist in **either set but not both**.

Mathematically:

```text
A △ B
```

Python syntax:

```python
A ^ B
```

Example:

```python
python_skills = {"Python", "SQL", "Git"}
data_engineering_skills = {"SQL", "Python", "Snowflake"}

unique_to_each = python_skills ^ data_engineering_skills

print(unique_to_each)
```

The result contains:

```text
Git, Snowflake
```

`Python` and `SQL` are removed because they exist in both sets.

---

# 15. Subset and Superset

A set is a **subset** of another set when every element of the first set exists in the second set.

Example:

```python
small = {"Python", "SQL"}
large = {"Python", "SQL", "Snowflake"}

print(small.issubset(large))
```

Output:

```text
True
```

We can also use the operator:

```python
print(small <= large)
```

A **superset** contains all elements of another set:

```python
print(large.issuperset(small))
```

Output:

```text
True
```

Operator form:

```python
print(large >= small)
```

---

# 16. Disjoint Sets

Two sets are **disjoint** when they have no common elements.

```python
set_a = {1, 2, 3}
set_b = {4, 5, 6}

print(set_a.isdisjoint(set_b))
```

Output:

```text
True
```

If the sets share even one element, they are not disjoint.

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a.isdisjoint(set_b))
```

Output:

```text
False
```

---

# 17. Looping Through a Set

Sets are iterable, so we can use a `for` loop.

```python
skills = {"Python", "SQL", "Snowflake"}

for skill in skills:
    print(skill)
```

The loop visits each element.

However, because sets are unordered, do not build logic that depends on a particular iteration order.

If you need stable positional access, convert the set to a list:

```python
skills = {"Python", "SQL", "Snowflake"}

skills_list = list(skills)

print(skills_list[0])
```

The resulting list order should not be assumed to match a specific set order.

---

# 18. Converting Between List and Set

Converting a list to a set is a common way to remove duplicates.

```python
numbers = [10, 20, 10, 30, 20]

unique_numbers = set(numbers)

print(unique_numbers)
```

The result contains only unique values.

To convert the set back to a list:

```python
unique_numbers = list(unique_numbers)
```

> [!WARNING]
> Converting a list to a set is not an ordering-preserving deduplication technique. If the original order matters, use another approach such as `dict.fromkeys()`.

For example:

```python
numbers = [10, 20, 10, 30, 20]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
```

Output:

```text
[10, 20, 30]
```

This removes duplicates while preserving the first-seen order.

---

# 19. Frozen Sets

A **frozenset** is an immutable version of a set.

```python
numbers = frozenset([10, 20, 30])
```

We can perform set operations on a frozenset, but we cannot add or remove elements.

For example:

```python
numbers.add(40)
```

is invalid because a frozenset has no `add()` method.

Frozensets are useful when we need a set-like collection that must remain immutable.

A frozenset can also be used as an element of another set because it is hashable.

```python
roles = {
    frozenset({"read", "write"}),
    frozenset({"read"})
}
```

---

# 20. Set Comprehension

A **set comprehension** provides a concise way to create a set from an iterable.

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = {number * number for number in numbers}

print(squares)
```

The expression:

```python
number * number
```

is evaluated for every value in `numbers`.

The resulting values are stored in a set, so duplicates are automatically removed.

We can also add a condition:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {number for number in numbers if number % 2 == 0}

print(even_numbers)
```

Output contains the unique even values.

> [!NOTE]
> Set comprehensions use `{}` with an expression. A dictionary comprehension also uses `{}`, but includes `key: value` pairs.

---

# 21. Set vs List vs Tuple

Understanding when to use each collection is important.

| Feature | List | Tuple | Set |
|---|---|---|---|
| Ordered sequence | Yes | Yes | No positional order |
| Mutable | Yes | No | Yes |
| Duplicates | Allowed | Allowed | Not allowed |
| Indexing | Yes | Yes | No |
| Slicing | Yes | Yes | No |
| Membership | Yes | Yes | Yes |
| Main strength | Flexible collection | Fixed collection | Uniqueness and membership |

### Example

Use a **list** when order and modification matter:

```python
files = ["customers.csv", "orders.csv"]
files.append("products.csv")
```

Use a **tuple** when the values form a fixed structure:

```python
record = (101, "Onkar", "Pune")
```

Use a **set** when uniqueness or membership is the main requirement:

```python
customer_ids = {101, 102, 103}
```

---

# 22. When Should You Use a Set?

Use a set when you primarily need **unique values** or **fast membership checks**.

### Example 1: Remove Duplicates

```python
customer_ids = [101, 102, 101, 103, 102]

unique_ids = set(customer_ids)
```

### Example 2: Check Allowed Values

```python
allowed_status = {"ACTIVE", "INACTIVE", "PENDING"}

status = "ACTIVE"

if status in allowed_status:
    print("Valid status")
```

### Example 3: Compare Two Data Sources

```python
source_ids = {101, 102, 103, 104}
target_ids = {101, 102, 104}

missing_ids = source_ids - target_ids
```

Here `missing_ids` identifies values present in the source but absent from the target.

This type of comparison is useful in data validation and reconciliation.

---

# 23. Common Mistakes

## Mistake 1: Expecting `{}` to Create an Empty Set

```python
empty = {}
```

This creates a dictionary.

Correct:

```python
empty = set()
```

---

## Mistake 2: Trying to Access a Set by Index

```python
numbers = {10, 20, 30}

print(numbers[0])
```

This raises `TypeError` because sets do not support indexing.

---

## Mistake 3: Expecting Duplicate Values to Remain

```python
numbers = {10, 10, 20}
```

The duplicate `10` is not stored twice.

---

## Mistake 4: Assuming Set Order

Do not write code that assumes the first element of a set is a particular value.

Sets are intended for membership and uniqueness, not positional access.

---

## Mistake 5: Using `remove()` When the Value May Not Exist

```python
numbers = {10, 20, 30}
numbers.remove(50)
```

This raises `KeyError`.

If the value may not exist and no exception is required:

```python
numbers.discard(50)
```

---

## Mistake 6: Putting a List Inside a Set

```python
values = {[1, 2], [3, 4]}
```

This raises `TypeError` because lists are unhashable.

A tuple can be used when its elements are hashable:

```python
values = {(1, 2), (3, 4)}
```

---

# 24. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. Why would you use a set instead of a list for membership checking?

<details>
<summary><strong>Answer</strong></summary>

A set is generally preferred when we perform many membership checks because set lookup is hash-table based and is typically **O(1) average-case**.

For a list, membership checking generally requires scanning elements and is **O(n)** in the worst case.

Example:

```python
allowed_users = {101, 102, 103, 104}

if 103 in allowed_users:
    print("User is allowed")
```

For large collections with frequent membership checks, the set can be significantly more appropriate than repeatedly searching a list.

</details>

---

### Q2. You convert a list to a set to remove duplicates, but the original order must be preserved. Would you use `set()`?

<details>
<summary><strong>Answer</strong></summary>

Not if preserving the original order is a requirement.

A set is not the right structure when we need positional ordering.

A common approach is:

```python
numbers = [10, 20, 10, 30, 20]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
```

Output:

```text
[10, 20, 30]
```

This removes duplicates while preserving the first-seen order.

The important interview point is that **deduplication and order preservation are separate requirements**.

</details>

---

### Q3. What is the difference between `remove()` and `discard()` for sets?

<details>
<summary><strong>Answer</strong></summary>

Both attempt to remove a specified element.

`remove()` raises `KeyError` when the value does not exist:

```python
numbers = {10, 20, 30}

numbers.remove(50)
```

`discard()` silently does nothing when the value is absent:

```python
numbers = {10, 20, 30}

numbers.discard(50)
```

Use `discard()` when missing values are expected and should not cause an exception.

</details>

---

### Q4. A set is mutable, so why can a list not be stored inside a set?

<details>
<summary><strong>Answer</strong></summary>

Set elements must be **hashable** because the set uses hashing to store and locate elements.

Lists are mutable, so they are unhashable and cannot be set elements.

This fails:

```python
values = {[1, 2], [3, 4]}
```

A tuple containing hashable values can be used:

```python
values = {(1, 2), (3, 4)}
```

This works because those tuples are hashable.

</details>

---

### Q5. You have customer IDs from two systems. How would you find customers present in System A but missing from System B?

<details>
<summary><strong>Answer</strong></summary>

Represent the IDs as sets and use set difference.

```python
system_a = {101, 102, 103, 104}
system_b = {101, 102, 104}

missing_from_b = system_a - system_b

print(missing_from_b)
```

The result contains `103`.

The operation is conceptually:

```text
System A - System B
```

This is a common data reconciliation pattern.

</details>

---

### Q6. What is the difference between union, intersection, difference, and symmetric difference?

<details>
<summary><strong>Answer</strong></summary>

Suppose:

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

**Union** returns everything from both sets:

```python
A | B
```

Result: `{1, 2, 3, 4, 5}`

**Intersection** returns common elements:

```python
A & B
```

Result: `{3}`

**Difference** returns elements in the first set but not the second:

```python
A - B
```

Result: `{1, 2}`

**Symmetric difference** returns elements that belong to exactly one of the sets:

```python
A ^ B
```

Result: `{1, 2, 4, 5}`

</details>

---

### Q7. You need to compare two datasets containing millions of IDs. What Python data structure could help with existence checks, and what trade-off should you consider?

<details>
<summary><strong>Answer</strong></summary>

A set can provide efficient average-case membership checks:

```python
valid_ids = set(valid_customer_ids)

if customer_id in valid_ids:
    ...
```

The trade-off is memory: the set keeps its elements in memory and has hashing-related overhead.

For very large datasets, loading millions or billions of values into a Python set may not be appropriate. A Data Engineer should consider database-side joins, distributed processing, Bloom filters where appropriate, or other scalable approaches depending on the workload.

</details>

---

### Q8. What is the difference between a set and a frozenset?

<details>
<summary><strong>Answer</strong></summary>

A `set` is mutable:

```python
numbers = {1, 2, 3}
numbers.add(4)
```

A `frozenset` is immutable:

```python
numbers = frozenset([1, 2, 3])
```

A frozenset does not provide mutation methods such as `add()` or `remove()`.

Because a frozenset is immutable and hashable, it can be used in places where a normal set cannot, such as as an element of another set.

</details>

---

# 25. Data Engineering Perspective

Sets are especially useful in Data Engineering for **data validation, deduplication, reconciliation, and membership checks**.

## 25.1 Finding Duplicate IDs

Suppose a source contains customer IDs:

```python
customer_ids = [101, 102, 101, 103, 102]
```

We can identify the unique IDs:

```python
unique_ids = set(customer_ids)
```

This is useful for checking whether duplicate identifiers exist.

## 25.2 Comparing Source and Target Data

Suppose we have IDs from a source system and a warehouse table:

```python
source_ids = {101, 102, 103, 104}
target_ids = {101, 102, 104}
```

Find records missing from the target:

```python
missing_ids = source_ids - target_ids
```

Find records that exist in both:

```python
common_ids = source_ids & target_ids
```

Find records that exist in the target but not in the source:

```python
unexpected_ids = target_ids - source_ids
```

This is a simple example of **source-to-target reconciliation**.

## 25.3 Data Validation

Sets can represent allowed values:

```python
allowed_status = {"ACTIVE", "INACTIVE", "PENDING"}
```

Then validate incoming records:

```python
status = "ACTIVE"

if status not in allowed_status:
    print("Invalid status")
```

This makes membership validation clear and efficient.

## 25.4 Comparing File Names

Suppose one system produced a set of files and another system received a set of files:

```python
produced = {"customers.csv", "orders.csv", "products.csv"}
received = {"customers.csv", "orders.csv"}
```

Find missing files:

```python
missing_files = produced - received
```

Result:

```text
products.csv
```

This pattern can be useful in ETL monitoring and pipeline validation.

## 25.5 Important Scalability Consideration

Sets are efficient for in-memory membership checks, but they are still **Python in-memory data structures**.

If the data contains millions or billions of records, do not automatically load everything into a set.

Consider whether the operation should instead happen using:

- SQL joins
- Database indexes
- Spark transformations
- Distributed processing
- Streaming techniques
- Approximate membership structures such as Bloom filters when appropriate

> [!IMPORTANT]
> As a Data Engineer, the goal is not simply to know that a set is fast. You should understand **when an in-memory set is appropriate and when the data volume requires a scalable distributed or database-side solution**.

---

## Navigation

⬅️ **Previous:** [Day 15 - Tuples](../Day_15_Tuples/readme.md)

➡️ **Next:** [Day 17 - Dictionaries](../Day_17_Dictionaries/readme.md)
