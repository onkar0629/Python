# 🐍 Day 08 - while Loop

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

The `while` loop repeatedly executes a block of code **as long as a given condition remains `True`**.

Unlike the `for` loop, which is generally used when the number of iterations is known, the `while` loop is ideal when the number of iterations depends on a condition that changes during program execution.

---

## Table of Contents

- What is a `while` Loop?
- Why Use a `while` Loop?
- Syntax
- Flow of Execution
- Counter-Controlled `while` Loop
- Infinite Loop
- Practical Examples
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What is a `while` Loop?

A `while` loop executes a block of code repeatedly **until its condition becomes `False`**.

If the condition is initially `False`, the loop body is never executed.

> [!NOTE]
> A `while` loop is also known as a **condition-controlled loop**.

---

# 2. Why Use a `while` Loop?

Use a `while` loop when:

- The number of iterations is unknown.
- You need to wait until a condition changes.
- Taking user input until valid input is received.
- Processing data until no more records remain.

---

# 3. Syntax

```python
while condition:
    statement
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

**Output**

```text
1
2
3
4
5
```

---

# 4. Flow of Execution

1. Check the condition.
2. If `True`, execute the loop body.
3. Update the condition (usually by changing a variable).
4. Repeat until the condition becomes `False`.

---

# 5. Counter-Controlled `while` Loop

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

---

# 6. Infinite Loop

```python
while True:
    print("Hello")
```

> [!WARNING]
> An infinite loop never stops unless it contains a `break` statement or the program is manually terminated.

---

# 7. Practical Examples

### Print Even Numbers

```python
i = 2

while i <= 20:
    print(i)
    i += 2
```

---

### Multiplication Table

```python
number = 5
i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
```

---

# Best Practices

- Always update the loop variable.
- Keep conditions simple.
- Avoid unnecessary infinite loops.
- Use meaningful variable names.

---

# Common Mistakes

- Forgetting to update the loop variable.
- Creating accidental infinite loops.
- Incorrect indentation.
- Using the wrong loop type.

---

# Interview Questions

### What is a `while` loop?

A `while` loop repeatedly executes code as long as its condition is `True`.

### What is an infinite loop?

An infinite loop never ends because its condition always remains `True`.

### When should you use a `while` loop instead of a `for` loop?

Use a `while` loop when the number of iterations is unknown beforehand.

### Why is updating the loop variable important?

Without updating it, the condition may never become `False`, resulting in an infinite loop.

---

# Data Engineering Perspective

`while` loops are useful in Data Engineering for:

- Reading streaming data.
- Polling APIs until data is available.
- Waiting for files to arrive.
- Monitoring pipeline execution.
- Retrying failed operations.

---

# Summary

After completing this lesson, you should be able to:

- ✅ Explain the `while` loop.
- ✅ Write counter-controlled loops.
- ✅ Identify infinite loops.
- ✅ Use `while` for condition-based repetition.
- ✅ Apply `while` loops to practical problems.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 07 - Loops](../Day_07_Loops/README.md)

➡️ **Next:** [Day 09 - break, continue and pass](../Day_09_Break_Continue_Pass/README.md)