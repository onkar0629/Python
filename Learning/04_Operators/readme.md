# 🐍 Day 04 - Operators

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

Operators are special symbols in Python that perform operations on variables and values. They are essential for writing programs because they allow us to perform calculations, compare values, assign data, and make decisions.

In this lesson, you'll learn the different types of operators in Python and how to use them through practical examples.

---

## Table of Contents

- What are Operators?
- Arithmetic Operators
- Relational Operators
- Logical Operators
- Assignment Operator
- Shorthand Assignment Operators
- Membership Operators
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What are Operators?

An **operator** is a special symbol that performs an operation on one or more operands (values or variables).

For example:

```python
a = 10
b = 5

print(a + b)
```

**Output**

```text
15
```

Here,

- `a` and `b` are operands.
- `+` is the operator.

Python provides different categories of operators:

| Operator Type | Purpose |
|--------------|---------|
| Arithmetic | Perform mathematical calculations |
| Relational | Compare values |
| Logical | Combine conditions |
| Assignment | Assign values to variables |
| Shorthand Assignment | Update variable values efficiently |
| Membership | Check whether a value exists in a sequence |

> [!NOTE]
> Operators are used in almost every Python program, from simple calculations to complex decision-making.

---

# 2. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor Division | `10 // 3` |
| `%` | Modulus (Remainder) | `10 % 3` |
| `**` | Exponent | `2 ** 3` |

### Example

```python
a = 20
b = 6

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Exponent :", a ** 2)
```

**Output**

```text
Addition : 26
Subtraction : 14
Multiplication : 120
Division : 3.3333333333333335
Floor Division : 3
Modulus : 2
Exponent : 400
```

### Practical Example – Remove Last Digit

```python
number = 4567

print(number // 10)
```

**Output**

```text
456
```

### Practical Example – Get Last Digit

```python
number = 4567

print(number % 10)
```

**Output**

```text
7
```

---

# 3. Relational Operators

Relational operators compare two values and always return either **True** or **False**.

| Operator | Description |
|----------|-------------|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or Equal to |
| `<=` | Less than or Equal to |
| `==` | Equal to |
| `!=` | Not Equal to |

### Example

```python
age = 20

print(age >= 18)
print(age == 25)
```

**Output**

```text
True
False
```

### Example – Even Number

```python
number = 18

print(number % 2 == 0)
```

**Output**

```text
True
```

---

# 4. Logical Operators

Logical operators combine multiple conditions.

| Operator | Description |
|----------|-------------|
| `and` | Returns True if both conditions are True |
| `or` | Returns True if at least one condition is True |
| `not` | Reverses the Boolean value |

### Example

```python
age = 22
salary = 30000

print(age >= 18 and salary >= 25000)
```

**Output**

```text
True
```

### Example

```python
city = "Pune"

print(city == "Mumbai" or city == "Pune")
```

**Output**

```text
True
```

### Example

```python
status = True

print(not status)
```

**Output**

```text
False
```

---

# 5. Assignment Operator

The assignment operator (`=`) assigns a value to a variable.

```python
name = "Onkar"
age = 22
```

---

# 6. Shorthand Assignment Operators

Shorthand assignment operators make code shorter and easier to read.

| Operator | Equivalent |
|----------|------------|
| `+=` | `x = x + value` |
| `-=` | `x = x - value` |
| `*=` | `x = x * value` |
| `/=` | `x = x / value` |
| `//=` | `x = x // value` |
| `%=` | `x = x % value` |
| `**=` | `x = x ** value` |

### Example

```python
count = 10

count += 5

print(count)
```

**Output**

```text
15
```

---

# 7. Membership Operators

Membership operators check whether a value exists in a sequence.

| Operator | Description |
|----------|-------------|
| `in` | Returns True if the value exists |
| `not in` | Returns True if the value does not exist |

### Example

```python
languages = ["Python", "SQL", "Java"]

print("Python" in languages)
print("C++" not in languages)
```

**Output**

```text
True
True
```

### Example

```python
email = "onkar@gmail.com"

print("@" in email)
```

**Output**

```text
True
```

---

# Best Practices

- Use meaningful variable names.
- Use `==` for comparison and `=` for assignment.
- Use shorthand assignment operators where appropriate.
- Keep logical conditions simple and readable.
- Use parentheses when writing complex logical expressions.

---

# Common Mistakes

- Confusing `=` with `==`.
- Using `/` instead of `//` when integer division is required.
- Forgetting that `%` returns the remainder.
- Writing complex logical conditions without parentheses.
- Misusing membership operators with unsupported data types.

> [!WARNING]
> `=` assigns a value, whereas `==` compares two values. Mixing them up is one of the most common beginner mistakes.

---

# Interview Questions

### What is an operator in Python?

An operator is a special symbol that performs an operation on one or more operands.

### What are the different types of operators in Python?

Arithmetic, Relational, Logical, Assignment, Shorthand Assignment, and Membership operators.

### What is the difference between `/` and `//`?

`/` returns the exact division result as a float, whereas `//` returns the floor (integer) quotient.

### What does the modulus (`%`) operator do?

It returns the remainder after division.

### What is the difference between `=` and `==`?

`=` assigns a value to a variable, whereas `==` compares two values.

### What are membership operators?

Membership operators (`in` and `not in`) are used to check whether a value exists in a sequence.

---

# Data Engineering Perspective

Operators are used extensively in Data Engineering.

Some common use cases include:

- Calculating metrics and aggregations.
- Comparing values while validating data.
- Filtering records during ETL processes.
- Writing conditional logic for data pipelines.
- Checking whether values exist in datasets.
- Performing arithmetic transformations on numerical data.

A strong understanding of operators is essential before learning conditional statements, loops, and functions.

---

# Summary

After completing this lesson, you should be able to:

- ✅ Explain what operators are.
- ✅ Perform arithmetic calculations.
- ✅ Compare values using relational operators.
- ✅ Combine conditions using logical operators.
- ✅ Use assignment and shorthand assignment operators.
- ✅ Check membership using `in` and `not in`.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 03 - Input, Output and Type Conversion](../Day_03_Input_Output_and_Type_Conversion/README.md)

➡️ **Next:** [Day 05 - Conditional Statements](../Day_05_Conditional_Statements/README.md)