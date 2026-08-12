# 🐍 Day 06 - Multiple `if` Statements and Nested `if` Statements

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

Conditional statements help a program make decisions. In the previous lesson, you learned how to use `if`, `if-else`, and `if-elif-else`.

In this lesson, you'll learn two important concepts:

- Multiple `if` Statements
- Nested `if` Statements

These concepts are widely used in real-world applications where multiple conditions need to be evaluated independently or one condition depends on another.

---

## Table of Contents

- What are Multiple `if` Statements?
- Multiple `if` Example
- Nested `if` Statement
- Nested `if` Example
- Difference Between Multiple `if` and Nested `if`
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What are Multiple `if` Statements?

Multiple `if` statements are independent conditions. Every condition is checked, regardless of whether previous conditions are `True` or `False`.

### Syntax

```python
if condition1:
    statement

if condition2:
    statement

if condition3:
    statement
```

### Example

```python
number = 12

if number > 0:
    print("Positive")

if number % 2 == 0:
    print("Even")

if number < 100:
    print("Less than 100")
```

**Output**

```text
Positive
Even
Less than 100
```

---

# 2. Nested `if` Statement

A Nested `if` is an `if` statement inside another `if`.

The inner condition is checked only if the outer condition is `True`.

### Syntax

```python
if condition1:
    if condition2:
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

# 3. Difference Between Multiple `if` and Nested `if`

| Multiple `if` | Nested `if` |
|---------------|-------------|
| Conditions are independent. | One condition depends on another. |
| Every `if` is evaluated. | Inner `if` runs only if outer `if` is `True`. |
| Easier for unrelated checks. | Best for dependent conditions. |

---

# Best Practices

- Use Multiple `if` for independent conditions.
- Use Nested `if` only when conditions depend on each other.
- Avoid deep nesting whenever possible.
- Maintain proper indentation.
- Keep conditions simple and readable.

---

# Common Mistakes

- Using Nested `if` when Multiple `if` is sufficient.
- Incorrect indentation.
- Forgetting the colon (`:`).
- Writing unnecessary nested conditions.

> [!WARNING]
> Too many nested `if` statements make code difficult to read and maintain.

---

# Interview Questions

### What is a Multiple `if` statement?

Multiple `if` statements are independent conditions, and each one is evaluated separately.

### What is a Nested `if` statement?

A Nested `if` is an `if` statement inside another `if`.

### When should you use Nested `if`?

Use it when one condition should only be checked after another condition is satisfied.

### Which is easier to read?

Multiple `if` statements are generally easier to read when conditions are independent.

---

# Data Engineering Perspective

Decision-making is a critical part of ETL pipelines.

Examples include:

- Validate whether a file exists.
- Check if the file is empty.
- Verify required columns.
- Ensure no null values exist.
- Process data only after all validations pass.

Nested conditions are commonly used in data validation pipelines.

---

# Summary

After completing this lesson, you should be able to:

- ✅ Write Multiple `if` statements.
- ✅ Understand when to use Nested `if`.
- ✅ Differentiate between Multiple `if` and Nested `if`.
- ✅ Apply decision-making in practical programs.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 05 - Conditional Statements](../Day_05_Conditional_Statements/README.md)

➡️ **Next:** [Day 07 - Loops](../Day_07_Loops/README.md)