# 🐍 Day 09 - Loop Control Statements

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

Loop control statements allow us to change the normal execution flow of loops.

Python provides four important loop control statements:

- `break`
- `continue`
- `pass`
- `else` with loops

These statements help us terminate loops, skip iterations, create placeholders, and execute code after a loop finishes successfully.

---

## Table of Contents

- What are Loop Control Statements?
- `break` Statement
- `continue` Statement
- `pass` Statement
- `else` with Loops
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What are Loop Control Statements?

Loop control statements modify the normal execution of a loop.

They help us:

- Stop a loop.
- Skip specific iterations.
- Create placeholders for future code.
- Execute code after successful loop completion.

---

# 2. break Statement

The `break` statement immediately terminates the nearest loop.

### Syntax

```python
for item in sequence:
    if condition:
        break
```

### Example

```python
for i in range(1, 11):
    if i == 6:
        break

    print(i)
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

# 3. continue Statement

The `continue` statement skips the current iteration and moves to the next one.

### Example

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

**Output**

```text
1
2
4
5
```

---

# 4. pass Statement

The `pass` statement does nothing.

It is used as a placeholder when code will be written later.

### Example

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

---

# 5. else with Loops

The `else` block executes only if the loop finishes normally.

It is **not executed** if the loop exits using `break`.

### Example

```python
for i in range(5):
    print(i)
else:
    print("Loop Completed")
```

Output

```text
0
1
2
3
4
Loop Completed
```

---

# Best Practices

- Use `break` only when necessary.
- Avoid excessive `continue`.
- Use `pass` as a temporary placeholder.
- Understand when loop `else` executes.

---

# Common Mistakes

- Confusing `break` and `continue`.
- Expecting loop `else` to behave like `if-else`.
- Forgetting that `break` skips the `else` block.

> [!WARNING]
> The `else` block of a loop executes **only if the loop is not terminated using `break`**.

---

# Interview Questions

### What is the difference between `break` and `continue`?

`break` terminates the loop completely, whereas `continue` skips only the current iteration.

### What does `pass` do?

It acts as a placeholder and performs no action.

### When does a loop `else` execute?

It executes only if the loop finishes normally without a `break`.

### Can `break` be used inside nested loops?

Yes. It only exits the nearest enclosing loop.

---

# Data Engineering Perspective

Loop control statements are frequently used while processing data.

Examples include:

- Stop processing when corrupted data is found (`break`).
- Skip invalid records (`continue`).
- Build pipeline templates (`pass`).
- Execute cleanup after processing completes (`else`).

---

# Summary

After completing this lesson, you should be able to:

- ✅ Use `break`.
- ✅ Use `continue`.
- ✅ Use `pass`.
- ✅ Understand loop `else`.
- ✅ Control loop execution efficiently.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 08 - while Loop](../Day_08_While_Loop/README.md)

➡️ **Next:** [Day 10 - Functions](../Day_10_Functions/README.md)