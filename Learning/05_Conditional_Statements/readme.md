# 🐍 Day 05 - Conditional Statements

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

Conditional statements allow a program to make decisions based on specific conditions. They enable Python to execute different blocks of code depending on whether a condition evaluates to `True` or `False`.

In this lesson, you'll learn how to use `if`, `if-else`, and `if-elif-else` statements to build decision-making logic in your Python programs.

---

## Table of Contents

- What are Conditional Statements?
- The `if` Statement
- The `if-else` Statement
- The `if-elif-else` Statement
- Nested `if` Statement
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What are Conditional Statements?

A **conditional statement** is used to make decisions in a program. It checks whether a condition is **True** or **False** and executes the appropriate block of code.

Python provides the following conditional statements:

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`

> [!NOTE]
> Conditional statements are the foundation of decision-making in programming.

---

# 2. The `if` Statement

The `if` statement executes a block of code only when the given condition is `True`.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

**Output**

```text
Eligible to Vote
```

### Example – Check Even Number

```python
number = 14

if number % 2 == 0:
    print("Even Number")
```

**Output**

```text
Even Number
```

---

# 3. The `if-else` Statement

The `if-else` statement executes one block of code if the condition is `True` and another block if it is `False`.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
```

**Output**

```text
Not Eligible to Vote
```

### Example – Positive or Negative Number

```python
number = -8

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")
```

**Output**

```text
Negative Number
```

---

# 4. The `if-elif-else` Statement

The `if-elif-else` statement is used when there are multiple conditions to evaluate.

### Syntax

```python
if condition:
    statement
elif condition:
    statement
else:
    statement
```

### Example – Grade Calculator

```python
marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

**Output**

```text
Grade B
```

### Example – Traffic Signal

```python
signal = "Green"

if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Get Ready")
else:
    print("Go")
```

**Output**

```text
Go
```

---

# 5. Nested `if` Statement

A **Nested `if`** is an `if` statement inside another `if` statement.

It is used when one condition depends on another.

### Syntax

```python
if condition:
    if condition:
        statement
```

### Example

```python
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

**Output**

```text
Eligible to Vote
```

---

# Best Practices

- Use meaningful conditions.
- Keep nesting to a minimum.
- Use `elif` instead of multiple independent `if` statements when checking related conditions.
- Maintain proper indentation.
- Write readable conditions using logical operators.

---

# Common Mistakes

- Forgetting the colon (`:`) after `if`, `elif`, or `else`.
- Incorrect indentation.
- Using `=` instead of `==` in conditions.
- Writing unnecessary nested `if` statements.
- Forgetting to handle all possible cases.

> [!WARNING]
> Python uses indentation to define code blocks. Incorrect indentation results in an `IndentationError`.

---

# Interview Questions

### What is a conditional statement?

A conditional statement allows a program to make decisions based on whether a condition is `True` or `False`.

### What is the difference between `if` and `if-else`?

`if` executes code only when the condition is `True`, whereas `if-else` executes one block for `True` and another for `False`.

### When should you use `if-elif-else`?

Use `if-elif-else` when there are multiple conditions to evaluate.

### What is a Nested `if` statement?

A Nested `if` is an `if` statement placed inside another `if` statement.

### Why is indentation important in Python?

Indentation defines code blocks and determines which statements belong to each condition.

---

# Data Engineering Perspective

Conditional statements are used extensively in Data Engineering.

Some common use cases include:

- Validating incoming data.
- Filtering invalid records.
- Checking whether files exist before processing.
- Applying business rules during ETL pipelines.
- Triggering alerts when data quality checks fail.
- Routing data based on specific conditions.

Decision-making is one of the core building blocks of every data pipeline.

---

# Summary

After completing this lesson, you should be able to:

- ✅ Explain what conditional statements are.
- ✅ Write programs using `if`.
- ✅ Use `if-else` for two-way decisions.
- ✅ Use `if-elif-else` for multiple conditions.
- ✅ Write simple Nested `if` statements.
- ✅ Apply decision-making in real-world programs.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 04 - Operators](../Day_04_Operators/README.md)

➡️ **Next:** [Day 06 - Multiple if and Nested if](../Day_06_Multiple_if_and_Nested_if/README.md)