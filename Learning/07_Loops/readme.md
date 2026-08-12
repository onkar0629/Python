# 🐍 Day 07 - Loops

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

Loops allow us to execute a block of code repeatedly without writing the same code multiple times. They make programs shorter, more efficient, and easier to maintain.

Python provides two types of loops:

- `for` loop
- `while` loop

In this lesson, we'll focus on the **`for` loop**, which is commonly used to iterate over a sequence or repeat a task a fixed number of times.

---

## Table of Contents

- What are Loops?
- Why Do We Need Loops?
- The `for` Loop
- The `range()` Function
- Types of `range()`
- Practical Examples
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What are Loops?

A **loop** is a programming construct that repeatedly executes a block of code until a condition is met or a sequence has been completely processed.

Without loops, repetitive tasks would require writing the same code multiple times.

### Example (Without Loop)

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

### Example (With Loop)

```python
for i in range(5):
    print("Hello")
```

Both programs produce the same output, but the loop is shorter, cleaner, and easier to maintain.

---

# 2. Why Do We Need Loops?

Loops help us:

- Reduce code duplication.
- Automate repetitive tasks.
- Process collections of data efficiently.
- Improve code readability.
- Save development time.

---

# 3. The `for` Loop

The `for` loop repeats a block of code for each item in a sequence.

### Syntax

```python
for variable in sequence:
    statement
```

### Example

```python
for i in range(5):
    print(i)
```

**Output**

```text
0
1
2
3
4
```

---

# 4. The `range()` Function

The `range()` function generates a sequence of numbers.

### `range(stop)`

```python
range(5)
```

Output:

```text
0 1 2 3 4
```

---

### `range(start, stop)`

```python
range(3, 8)
```

Output:

```text
3 4 5 6 7
```

---

### `range(start, stop, step)`

```python
range(2, 11, 2)
```

Output:

```text
2 4 6 8 10
```

---

# 5. Practical Examples

### Print Numbers

```python
for i in range(1, 6):
    print(i)
```

---

### Print Even Numbers

```python
for i in range(2, 11, 2):
    print(i)
```

---

### Print Multiplication Table of 5

```python
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
```

---

# Best Practices

- Use meaningful loop variable names.
- Use `range()` appropriately.
- Avoid unnecessary nested loops.
- Keep loop bodies simple.
- Use comments for complex logic.

---

# Common Mistakes

- Forgetting that `range(stop)` starts from `0`.
- Incorrect indentation.
- Infinite loops (with `while`).
- Incorrect step values.

> [!WARNING]
> `range(5)` generates numbers from **0 to 4**, not **1 to 5**.

---

# Interview Questions

### What is a loop?

A loop repeatedly executes a block of code.

### What are the two types of loops in Python?

- `for` loop
- `while` loop

### What does `range(5)` return?

Numbers from `0` to `4`.

### What is the difference between `range(5)` and `range(1, 6)`?

`range(5)` starts from `0`, whereas `range(1, 6)` starts from `1`.

### Why are loops important?

They automate repetitive tasks and reduce code duplication.

---

# Data Engineering Perspective

Loops are fundamental in Data Engineering.

Common use cases include:

- Reading CSV files row by row.
- Processing millions of records.
- Validating datasets.
- Loading data into databases.
- Automating ETL pipelines.
- Iterating through API responses.

Almost every data pipeline uses loops in some form.

---

# Summary

After completing this lesson, you should be able to:

- ✅ Explain what loops are.
- ✅ Write `for` loops.
- ✅ Use the `range()` function.
- ✅ Generate number sequences.
- ✅ Build simple repetitive programs.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 06 - Multiple if and Nested if](../Day_06_Multiple_if_and_Nested_if/README.md)

➡️ **Next:** [Day 08 - while Loop](../Day_08_While_Loop/README.md)