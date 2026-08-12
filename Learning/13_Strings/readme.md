# 🐍 Day 13 — Strings

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

A **string** is an ordered sequence of characters enclosed inside quotes.

Strings are one of the most commonly used data types in Python. As a Data Engineer, you will work with strings constantly when cleaning data, processing files, parsing JSON, handling logs, transforming columns, and preparing data for databases.

This lesson covers strings from fundamentals to interview-level concepts.

---

## Table of Contents

- What is a String?
- Creating Strings
- Types of String Quotes
- String Indexing
- Positive Indexing
- Negative Indexing
- String Slicing
- String Immutability
- String Concatenation
- String Repetition
- `len()`
- Membership Operators
- Traversing a String
- Common String Methods
- String Formatting
- Escape Characters
- Raw Strings
- Common Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What is a String?

A string is a sequence of characters.

```python
name = "Onkar"
```

Here:

```text
"Onkar" → String
```

Each character has a position called an **index**.

```text
 O   n   k   a   r
 ↓   ↓   ↓   ↓   ↓
 0   1   2   3   4
```

Therefore:

```python
name = "Onkar"

print(name[0])
print(name[2])
print(name[4])
```

Output:

```text
O
k
r
```

> [!IMPORTANT]
> Python strings are ordered sequences, so every character has a position.

---

# 2. Creating Strings

Strings can be created using single or double quotes.

```python
name = 'Onkar'
city = "Pune"
```

Both are valid strings.

```python
print(name)
print(city)
```

You can also create an empty string:

```python
text = ""
```

---

# 3. Types of String Quotes

## Single Quotes

```python
text = 'Python'
```

## Double Quotes

```python
text = "Python"
```

## Triple Quotes

Triple quotes can be used for multi-line strings.

```python
text = """Python
is useful
for Data Engineering."""

print(text)
```

Triple quotes are also commonly used for **docstrings**.

```python
def greet():
    """This function prints a greeting."""
    print("Hello")
```

---

# 4. String Indexing

Indexing is used to access individual characters.

```python
text = "Python"
```

The indexes are:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
```

Example:

```python
print(text[0])
print(text[3])
print(text[5])
```

Output:

```text
P
h
n
```

> [!NOTE]
> Python uses **zero-based indexing**, meaning the first character is at index `0`.

---

# 5. Negative Indexing

Python also supports negative indexes.

```text
 P    y    t    h    o    n
-6   -5   -4   -3   -2   -1
```

Example:

```python
text = "Python"

print(text[-1])
print(text[-2])
print(text[-6])
```

Output:

```text
n
o
P
```

The most common use is:

```python
text[-1]
```

which returns the **last character**.

---

# 6. String Slicing

Slicing extracts a portion of a string.

### Syntax

```text
string[start:stop:step]
```

The `stop` index is **excluded**.

Example:

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

Because indexes `0`, `1`, and `2` are included, but index `3` is excluded.

### More Examples

```python
text = "Python"

print(text[:3])
print(text[2:])
print(text[:])
```

Output:

```text
Pyt
thon
Python
```

### Step

```python
text = "Python"

print(text[::2])
```

Output:

```text
Pto
```

### Reverse a String

```python
text = "Python"

print(text[::-1])
```

Output:

```text
nohtyP
```

---

# 7. Strings are Immutable

One of the most important Python interview concepts is **string immutability**.

Once a string object is created, its characters cannot be changed in place.

This is invalid:

```python
text = "Python"

text[0] = "J"
```

Python raises:

```text
TypeError: 'str' object does not support item assignment
```

Instead, create a new string:

```python
text = "Python"

text = "J" + text[1:]

print(text)
```

Output:

```text
Jython
```

> [!IMPORTANT]
> String methods such as `upper()` and `replace()` return a **new string**. They do not modify the original string in place.

Example:

```python
text = "python"

new_text = text.upper()

print(text)
print(new_text)
```

Output:

```text
python
PYTHON
```

---

# 8. String Concatenation

Concatenation means joining strings together.

```python
first_name = "Onkar"
last_name = "Jadhav"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Onkar Jadhav
```

> [!WARNING]
> You cannot directly concatenate a string and an integer using `+`.

Incorrect:

```python
age = 22

print("Age: " + age)
```

Correct:

```python
age = 22

print("Age: " + str(age))
```

---

# 9. String Repetition

The `*` operator can repeat a string.

```python
text = "Hi "

print(text * 3)
```

Output:

```text
Hi Hi Hi
```

---

# 10. `len()` Function

`len()` returns the number of characters in a string.

```python
text = "Python"

print(len(text))
```

Output:

```text
6
```

Spaces are also counted.

```python
text = "Hello World"

print(len(text))
```

Output:

```text
11
```

---

# 11. Membership Operators

Use `in` and `not in` to check whether a substring or character exists.

```python
text = "Python"

print("P" in text)
print("Java" in text)
print("Java" not in text)
```

Output:

```text
True
False
True
```

---

# 12. Traversing a String

A string can be traversed character by character using a `for` loop.

```python
text = "Python"

for character in text:
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

This is very useful for character-level processing.

---

# 13. Common String Methods

## `lower()`

Converts characters to lowercase.

```python
text = "PYTHON"

print(text.lower())
```

Output:

```text
python
```

---

## `upper()`

Converts characters to uppercase.

```python
text = "python"

print(text.upper())
```

Output:

```text
PYTHON
```

---

## `capitalize()`

Capitalizes the first character.

```python
text = "python programming"

print(text.capitalize())
```

Output:

```text
Python programming
```

---

## `title()`

Capitalizes the first character of each word.

```python
text = "python data engineering"

print(text.title())
```

Output:

```text
Python Data Engineering
```

---

## `strip()`

Removes leading and trailing whitespace.

```python
text = "   Python   "

print(text.strip())
```

Output:

```text
Python
```

This is extremely common in data cleaning.

---

## `lstrip()`

Removes whitespace from the left side.

```python
text = "   Python"

print(text.lstrip())
```

---

## `rstrip()`

Removes whitespace from the right side.

```python
text = "Python   "

print(text.rstrip())
```

---

## `replace()`

Replaces part of a string.

```python
text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)
```

Output:

```text
I like Python
```

Remember that the original string is unchanged unless you assign the result.

---

## `split()`

Splits a string into a list.

```python
text = "Python SQL Azure"

result = text.split()

print(result)
```

Output:

```text
['Python', 'SQL', 'Azure']
```

You can provide a delimiter:

```python
text = "Python,SQL,Azure"

print(text.split(","))
```

Output:

```text
['Python', 'SQL', 'Azure']
```

---

## `join()`

`join()` combines elements into a string.

```python
languages = ["Python", "SQL", "Azure"]

result = " | ".join(languages)

print(result)
```

Output:

```text
Python | SQL | Azure
```

### Important Difference

```text
split() → String → List
join()  → List/iterable of strings → String
```

---

## `find()`

Returns the index of the first occurrence.

```python
text = "Python"

print(text.find("t"))
```

Output:

```text
2
```

If the substring is not found, `find()` returns `-1`.

```python
print(text.find("z"))
```

Output:

```text
-1
```

---

## `index()`

Similar to `find()`, but raises an exception if the substring is not found.

```python
text = "Python"

print(text.index("t"))
```

Output:

```text
2
```

For a missing value:

```python
text.index("z")
```

raises:

```text
ValueError
```

### `find()` vs `index()`

| Method | Found | Not Found |
|---|---|---|
| `find()` | Index | `-1` |
| `index()` | Index | `ValueError` |

---

## `count()`

Counts occurrences of a substring.

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

## `startswith()`

Checks whether a string starts with a specific value.

```python
text = "Python Programming"

print(text.startswith("Python"))
```

Output:

```text
True
```

---

## `endswith()`

Checks whether a string ends with a specific value.

```python
filename = "sales.csv"

print(filename.endswith(".csv"))
```

Output:

```text
True
```

This is useful when processing files.

---

# 14. String Formatting

## f-Strings

f-strings are the preferred modern approach for most Python code.

```python
name = "Onkar"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Onkar and I am 22 years old.
```

Expressions can also be used:

```python
price = 100
quantity = 3

print(f"Total = {price * quantity}")
```

Output:

```text
Total = 300
```

---

## `.format()`

```python
name = "Onkar"
age = 22

print("My name is {} and I am {} years old.".format(name, age))
```

---

## `%` Formatting

Older Python code may use `%` formatting.

```python
name = "Onkar"
age = 22

print("My name is %s and I am %d years old." % (name, age))
```

> [!NOTE]
> Know `%` formatting for interviews and legacy code, but prefer f-strings for modern Python code.

---

# 15. Escape Characters

Escape characters allow special characters to be represented inside strings.

### New Line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

### Tab

```python
print("Python\tSQL")
```

### Quote Characters

```python
text = "He said \"Hello\""

print(text)
```

Common escape sequences:

| Escape | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

---

# 16. Raw Strings

A raw string treats backslashes mostly as literal characters.

```python
path = r"C:\Users\Onkar\Documents"

print(path)
```

Raw strings are particularly useful when working with **regular expressions** and Windows-style paths.

---

# 17. Important String Concepts for Interviews

### Strings are ordered

```python
text = "Python"

print(text[0])
```

### Strings are immutable

```python
text[0] = "J"  # TypeError
```

### Strings support indexing

```python
text[2]
```

### Strings support slicing

```python
text[1:4]
```

### Strings support iteration

```python
for char in text:
    print(char)
```

### Strings support membership testing

```python
"Py" in text
```

---

# 18. Common Interview Questions

### Q1. Are strings mutable or immutable in Python?

Strings are **immutable**. Once a string object is created, its characters cannot be modified in place.

---

### Q2. What is the difference between `find()` and `index()`?

`find()` returns `-1` when the substring is not found, while `index()` raises `ValueError`.

---

### Q3. What does `[::-1]` do?

It creates a reversed version of the string using a slice with a step of `-1`.

```python
text = "Python"

print(text[::-1])
```

Output:

```text
nohtyP
```

---

### Q4. What is the difference between `split()` and `join()`?

`split()` converts a string into a list of substrings, while `join()` combines an iterable of strings into one string.

---

### Q5. How do you get the last character of a string?

Use negative indexing:

```python
text[-1]
```

---

### Q6. What does `len()` return for a string?

It returns the number of characters in the string, including whitespace.

---

### Q7. Can we modify a character of a string directly?

No.

```python
text = "Python"
text[0] = "J"
```

This raises `TypeError` because strings are immutable.

---

### Q8. Why is `strip()` useful in Data Engineering?

It helps remove unwanted leading and trailing whitespace from raw data, which can prevent matching and data-quality problems.

---

# 19. Data Engineering Perspective

Strings are everywhere in data pipelines.

Examples include:

- CSV columns
- JSON values
- File paths
- File names
- Log messages
- Customer names
- Email addresses
- Product descriptions
- SQL queries
- API responses
- Configuration values

### Example: Cleaning Raw Data

Suppose a CSV contains:

```text
"  Onkar  "
"  Rahul"
"Priya   "
```

We can clean the values using:

```python
name = "  Onkar  "

clean_name = name.strip()

print(clean_name)
```

Output:

```text
Onkar
```

### Example: Checking File Type

```python
filename = "sales_2026.csv"

if filename.endswith(".csv"):
    print("CSV file")
```

### Example: Parsing a Delimited Value

```python
record = "101,Onkar,Data Engineer"

fields = record.split(",")

print(fields)
```

Output:

```text
['101', 'Onkar', 'Data Engineer']
```

> [!TIP]
> String manipulation is a fundamental skill for ETL and data-cleaning workflows.

---

# 20. Summary

After completing Day 13, you should be able to:

- Explain what a string is.
- Create strings using different quote styles.
- Use positive and negative indexing.
- Slice strings using `start:stop:step`.
- Explain string immutability.
- Concatenate and repeat strings.
- Use `len()`, `in`, and `not in`.
- Traverse strings with loops.
- Use common string methods.
- Explain `find()` vs `index()`.
- Explain `split()` vs `join()`.
- Use f-strings.
- Work with escape characters and raw strings.
- Solve common string interview problems.
- Apply string operations to Data Engineering scenarios.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 12 - Recursion](../Day_12_Recursion/readme.md)

➡️ **Next:** [Day 14 - Lists](../Day_14_Lists/readme.md)
