# 🐍 Day 10 - Functions

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

A **function** is a reusable block of code designed to perform a specific task.

Instead of writing the same logic repeatedly, we can define the logic once inside a function and call that function whenever it is required.

Functions help make Python programs more organized, reusable, readable, and easier to maintain.

---

## Table of Contents

- What is a Function?
- Why Do We Need Functions?
- Types of Functions
- Creating a Function
- Calling a Function
- Function Parameters
- Function Arguments
- The `return` Statement
- `print()` vs `return`
- Functions with Multiple Parameters
- Calling a Function Multiple Times
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. What is a Function?

A **function** is a named block of reusable code that performs a particular task.

A function runs only when it is called.

### Example

```python
def greet():
    print("Welcome to Python")

greet()
```

**Output**

```text
Welcome to Python
```

Here:

- `def` is the keyword used to define a function.
- `greet` is the function name.
- `()` contains parameters if required.
- `:` marks the beginning of the function body.
- `greet()` calls the function.

---

# 2. Why Do We Need Functions?

Suppose we want to display the same message multiple times.

Without a function:

```python
print("Processing Started")
print("Processing Started")
print("Processing Started")
```

Using a function:

```python
def start_processing():
    print("Processing Started")

start_processing()
start_processing()
start_processing()
```

Functions help us:

- Avoid code repetition.
- Reuse existing logic.
- Organize large programs.
- Improve readability.
- Make debugging easier.
- Make programs easier to maintain.

> [!NOTE]
> The principle of avoiding unnecessary code repetition is commonly known as **DRY — Don't Repeat Yourself**.

---

# 3. Types of Functions

Python functions can broadly be divided into two categories.

### Built-in Functions

These functions are already provided by Python.

Examples:

```python
print("Python")

length = len("Python")

number = int("100")

maximum = max(10, 20, 30)
```

Common built-in functions include:

- `print()`
- `input()`
- `len()`
- `type()`
- `int()`
- `float()`
- `str()`
- `max()`
- `min()`
- `sum()`

### User-Defined Functions

Functions created by the programmer are called **user-defined functions**.

```python
def welcome():
    print("Welcome")

welcome()
```

---

# 4. Creating a Function

The `def` keyword is used to define a function.

### Syntax

```python
def function_name():
    statements
```

### Example

```python
def display_message():
    print("Learning Python Functions")
```

Defining a function does not automatically execute it.

The function must be called.

---

# 5. Calling a Function

A function is executed by writing its name followed by parentheses.

```python
def display_message():
    print("Learning Python Functions")

display_message()
```

**Output**

```text
Learning Python Functions
```

> [!IMPORTANT]
> Creating a function and calling a function are two different operations. The function body executes only when the function is called.

---

# 6. Function Parameters

A **parameter** is a variable specified inside the parentheses when defining a function.

```python
def greet(name):
    print(f"Hello, {name}")
```

Here, `name` is a parameter.

---

# 7. Function Arguments

An **argument** is the actual value passed to a function when calling it.

```python
def greet(name):
    print(f"Hello, {name}")

greet("Onkar")
```

**Output**

```text
Hello, Onkar
```

Here:

```text
name       → Parameter
"Onkar"    → Argument
```

We'll study different types of function arguments in detail in **Day 11**.

---

# 8. The `return` Statement

The `return` statement sends a result back to the code that called the function.

### Example

```python
def add(a, b):
    result = a + b
    return result

answer = add(10, 20)

print(answer)
```

**Output**

```text
30
```

The returned value can be:

- Stored in a variable.
- Printed.
- Used in another calculation.
- Passed to another function.

### Example

```python
def square(number):
    return number ** 2

result = square(5)

print(result)
```

**Output**

```text
25
```

---

# 9. `print()` vs `return`

`print()` and `return` serve different purposes.

| `print()` | `return` |
|---|---|
| Displays a value | Sends a value back |
| Mainly used for output | Used to produce a reusable result |
| Value is displayed on screen | Value can be stored and processed further |

### Using `print()`

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Using `return`

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

The second approach allows us to reuse the result:

```python
final_result = add(10, 20) * 2

print(final_result)
```

**Output**

```text
60
```

---

# 10. Functions with Multiple Parameters

A function can accept multiple parameters.

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 4)

print(total)
```

**Output**

```text
2000
```

Another example:

```python
def student_details(name, marks):
    print("Name:", name)
    print("Marks:", marks)

student_details("Rahul", 85)
```

---

# 11. Calling a Function Multiple Times

One of the main benefits of functions is **reusability**.

```python
def square(number):
    return number ** 2

print(square(2))
print(square(5))
print(square(10))
```

**Output**

```text
4
25
100
```

The same function can process different values without rewriting the logic.

---

# Best Practices

- Use descriptive function names.
- Follow `snake_case` naming conventions.
- Keep each function focused on one task.
- Avoid unnecessary code duplication.
- Use `return` when the result needs to be reused.
- Keep functions small and readable.
- Avoid excessively long functions.

### Good

```python
def calculate_total_price(price, quantity):
    return price * quantity
```

### Avoid

```python
def ctp(p, q):
    return p * q
```

Meaningful names make programs easier to understand and maintain.

---

# Common Mistakes

### Forgetting Parentheses

Incorrect:

```python
greet
```

Correct:

```python
greet()
```

### Forgetting the Colon

Incorrect:

```python
def greet()
    print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

### Incorrect Indentation

```python
def greet():
print("Hello")
```

The function body must be indented.

### Confusing Parameters and Arguments

```python
def greet(name):
    print(name)

greet("Onkar")
```

`name` is the parameter, while `"Onkar"` is the argument.

### Forgetting `return`

```python
def add(a, b):
    result = a + b
```

Calling this function does not return `result`.

Correct:

```python
def add(a, b):
    return a + b
```

> [!WARNING]
> If a function reaches the end without executing a `return` statement, Python returns `None` implicitly.

---

# Interview Questions

### What is a function in Python?

A function is a reusable block of code designed to perform a specific task.

### Which keyword is used to define a function?

The `def` keyword.

### What is the difference between a parameter and an argument?

A parameter is a variable defined in the function definition, while an argument is the actual value supplied when calling the function.

### What is the purpose of `return`?

`return` sends a result from a function back to its caller.

### What happens if a function does not have a `return` statement?

Python implicitly returns `None`.

### What is the difference between `print()` and `return`?

`print()` displays a value, whereas `return` sends a value back to the caller so that it can be reused.

### Can a function be called multiple times?

Yes. Functions are designed to be reusable and can be called as many times as required.

### What is a built-in function?

A built-in function is a function already provided by Python, such as `print()`, `len()`, `type()`, and `sum()`.

---

# Data Engineering Perspective

Functions are extremely important in Data Engineering because data pipelines usually consist of multiple reusable processing steps.

For example, an ETL pipeline can be divided into functions:

```python
def extract_data():
    print("Extracting Data")


def transform_data():
    print("Transforming Data")


def load_data():
    print("Loading Data")


extract_data()
transform_data()
load_data()
```

**Output**

```text
Extracting Data
Transforming Data
Loading Data
```

Instead of writing an entire pipeline as one large script, functions allow us to separate responsibilities.

A more realistic structure might look like:

```python
def validate_record(record):
    return record is not None


def transform_record(record):
    return record * 2


record = 100

if validate_record(record):
    transformed_record = transform_record(record)
    print(transformed_record)
```

Functions are commonly used for:

- Data extraction
- Data validation
- Data transformation
- Data cleaning
- API processing
- File processing
- Database operations
- Pipeline orchestration

Learning to write small, reusable functions is an important step toward writing production-quality Data Engineering code.

---

# Summary

After completing this lesson, you should be able to:

- Define a function using `def`.
- Call user-defined functions.
- Explain built-in and user-defined functions.
- Understand parameters and arguments.
- Pass values into functions.
- Return values from functions.
- Explain the difference between `print()` and `return`.
- Create reusable functions.
- Follow Python function naming conventions.
- Understand how functions are used in Data Engineering.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 09 - Loop Control Statements](../Day_09_Loop_Control_Statements/README.md)

➡️ **Next:** [Day 11 - Function Arguments](../Day_11_Function_Arguments/README.md)