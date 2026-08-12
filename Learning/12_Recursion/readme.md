# 🐍 Day 12 - Recursion

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

**Recursion** is a programming technique in which a function calls itself to solve a problem.

A recursive function breaks a larger problem into smaller versions of the same problem until it reaches a condition where no further recursive calls are required.

That stopping condition is known as the **base case**.

Recursion is commonly used for problems involving hierarchical structures, tree traversal, directory traversal, mathematical calculations, and divide-and-conquer algorithms.

---

## Table of Contents

- What is Recursion?
- How Recursion Works
- Base Case
- Recursive Case
- Simple Recursive Function
- Factorial Using Recursion
- Sum of Natural Numbers
- Countdown Using Recursion
- Recursion vs Loops
- Recursion Limit
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What is Recursion?

Recursion occurs when a function calls itself.

### Basic Structure

```python
def function():
    function()
```

However, the above function would continue calling itself indefinitely.

A recursive function therefore requires a **base case** to stop the recursion.

### Correct Structure

```python
def function(value):

    if stopping_condition:
        return

    function(smaller_value)
```

A recursive function generally contains:

1. Base Case
2. Recursive Case

---

# 2. How Recursion Works

Consider the following countdown:

```python
def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)
```

**Output**

```text
5
4
3
2
1
```

The function calls happen like this:

```text
countdown(5)
    ↓
countdown(4)
    ↓
countdown(3)
    ↓
countdown(2)
    ↓
countdown(1)
    ↓
countdown(0)
    ↓
STOP
```

Each recursive call works with a smaller version of the original problem.

---

# 3. Base Case

The **base case** is the condition that stops recursion.

Without a base case, the function would continue calling itself until Python raises an error.

### Example

```python
def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)
```

Here:

```python
if number == 0:
    return
```

is the base case.

> [!IMPORTANT]
> Every recursive function must have a reachable stopping condition.

---

# 4. Recursive Case

The **recursive case** is the part of the function where it calls itself with a modified value.

```python
countdown(number - 1)
```

The input must move toward the base case.

For example:

```text
5 → 4 → 3 → 2 → 1 → 0
```

Once `0` is reached, recursion stops.

---

# 5. Simple Recursive Function

Let's print numbers from 5 to 1.

```python
def display_numbers(number):

    if number == 0:
        return

    print(number)

    display_numbers(number - 1)


display_numbers(5)
```

**Output**

```text
5
4
3
2
1
```

---

# 6. Factorial Using Recursion

Factorial is a common example used to understand recursion.

The factorial of `5` is:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Therefore:

```text
5! = 120
```

### Recursive Formula

```text
n! = n × (n - 1)!
```

Base case:

```text
0! = 1
```

### Python Program

```python
def factorial(number):

    if number == 0:
        return 1

    return number * factorial(number - 1)


result = factorial(5)

print(result)
```

**Output**

```text
120
```

### Execution

```text
factorial(5)
= 5 × factorial(4)

= 5 × 4 × factorial(3)

= 5 × 4 × 3 × factorial(2)

= 5 × 4 × 3 × 2 × factorial(1)

= 5 × 4 × 3 × 2 × 1 × factorial(0)

= 5 × 4 × 3 × 2 × 1 × 1

= 120
```

---

# 7. Sum of Natural Numbers

We can calculate the sum of natural numbers recursively.

For example:

```text
1 + 2 + 3 + 4 + 5 = 15
```

### Program

```python
def calculate_sum(number):

    if number == 0:
        return 0

    return number + calculate_sum(number - 1)


print(calculate_sum(5))
```

**Output**

```text
15
```

The recursive calls are:

```text
calculate_sum(5)
= 5 + calculate_sum(4)
= 5 + 4 + calculate_sum(3)
= 5 + 4 + 3 + calculate_sum(2)
= 5 + 4 + 3 + 2 + calculate_sum(1)
= 5 + 4 + 3 + 2 + 1 + calculate_sum(0)
= 15
```

---

# 8. Countdown Using Recursion

```python
def countdown(number):

    if number == 0:
        print("Done")
        return

    print(number)

    countdown(number - 1)


countdown(5)
```

**Output**

```text
5
4
3
2
1
Done
```

---

# 9. Recursion vs Loops

Many problems that can be solved recursively can also be solved using loops.

### Using a Loop

```python
for number in range(5, 0, -1):
    print(number)
```

### Using Recursion

```python
def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)
```

### Comparison

| Recursion | Loop |
|---|---|
| Function calls itself | Repeats a block of code |
| Requires a base case | Requires a loop condition or iterable |
| Uses the call stack | Usually uses less memory |
| Useful for naturally recursive problems | Efficient for simple repetition |
| Can be easier for trees and nested structures | Usually simpler for sequential processing |

> [!NOTE]
> Recursion is not automatically better than loops. The correct approach depends on the problem being solved.

---

# 10. Recursion Limit

Python places a limit on recursion depth.

This prevents uncontrolled recursion from consuming excessive memory.

For example:

```python
def infinite_recursion():
    infinite_recursion()


infinite_recursion()
```

Eventually Python raises:

```text
RecursionError: maximum recursion depth exceeded
```

You can inspect the current recursion limit using:

```python
import sys

print(sys.getrecursionlimit())
```

The exact value depends on the Python implementation and environment.

> [!WARNING]
> Do not increase the recursion limit simply to fix poorly designed recursive logic. First check whether recursion is appropriate for the problem.

---

# Best Practices

- Always define a reachable base case.
- Ensure every recursive call moves toward the base case.
- Keep recursive functions simple.
- Use meaningful function and parameter names.
- Prefer loops for straightforward repetitive operations.
- Use recursion when the problem naturally has a recursive structure.
- Consider memory usage when working with deep recursion.

### Good

```python
def factorial(number):

    if number == 0:
        return 1

    return number * factorial(number - 1)
```

The function clearly moves toward the base case.

---

# Common Mistakes

### Missing Base Case

```python
def countdown(number):
    print(number)
    countdown(number - 1)
```

There is no stopping condition.

---

### Recursive Call Does Not Approach Base Case

```python
def countdown(number):

    if number == 0:
        return

    countdown(number + 1)
```

If `number` starts positive, it moves away from `0`.

---

### Forgetting `return`

Incorrect:

```python
def factorial(number):

    if number == 0:
        return 1

    number * factorial(number - 1)
```

Correct:

```python
def factorial(number):

    if number == 0:
        return 1

    return number * factorial(number - 1)
```

---

### Using Recursion When a Loop is Simpler

For something like:

```text
Print numbers from 1 to 100
```

a loop is generally simpler:

```python
for number in range(1, 101):
    print(number)
```

> [!WARNING]
> Recursion should solve a problem more naturally or clearly. Avoid using it simply because it is available.

---

# Interview Questions

### What is recursion?

Recursion is a programming technique in which a function calls itself.

### What is a base case?

A base case is the stopping condition of a recursive function.

### What is a recursive case?

The recursive case is the part of the function that calls itself with a modified input.

### What happens if recursion has no base case?

The function continues making recursive calls until Python raises a `RecursionError`.

### What is the difference between recursion and iteration?

Recursion uses repeated function calls, while iteration generally uses loops such as `for` and `while`.

### Can every recursive problem be solved using loops?

Many recursive algorithms can be rewritten iteratively, although recursive solutions can be more natural for certain problems.

### What data structure manages function calls during recursion?

The **call stack**.

### What is `RecursionError`?

It is an exception raised when the maximum recursion depth is exceeded.

### Is recursion always more efficient than loops?

No. Recursion introduces function-call overhead and uses stack memory for each active call.

---

# Data Engineering Perspective

Recursion is less common in everyday ETL transformations than loops, functions, SQL, or DataFrame operations.

However, it becomes useful when working with **hierarchical or nested data**.

For example, imagine nested data:

```python
data = {
    "customer": {
        "name": "Rahul",
        "address": {
            "city": "Pune",
            "country": "India"
        }
    }
}
```

A recursive function can traverse nested dictionaries:

```python
def display_data(data):

    for key, value in data.items():

        if isinstance(value, dict):
            display_data(value)
        else:
            print(key, ":", value)


display_data(data)
```

**Output**

```text
name : Rahul
city : Pune
country : India
```

Recursion can be useful for:

- Nested JSON processing
- Directory traversal
- Hierarchical datasets
- Tree structures
- Dependency trees
- Recursive file structures

For most ordinary row-by-row data processing, loops or vectorized DataFrame operations are generally more appropriate.

---

# Summary

After completing this lesson, you should be able to:

- Explain recursion.
- Create a recursive function.
- Identify the base case.
- Identify the recursive case.
- Understand how recursive calls move toward the base case.
- Calculate factorial using recursion.
- Calculate sums recursively.
- Compare recursion with loops.
- Understand Python's recursion limit.
- Recognize common recursion mistakes.
- Understand where recursion can appear in Data Engineering.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 11 - Function Arguments](../Day_11_Function_Arguments/README.md)

➡️ **Next:** [Day 13 - Strings](../Day_13_Strings/README.md)