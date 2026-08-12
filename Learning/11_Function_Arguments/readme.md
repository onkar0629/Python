# 🐍 Day 11 - Function Arguments

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![IDE](https://img.shields.io/badge/IDE-PyCharm-green?logo=pycharm)
![Level](https://img.shields.io/badge/Level-Beginner-success)

---

## Overview

Functions become more flexible when we can pass different values to them.

The values supplied to a function when it is called are known as **arguments**.

Python provides several ways to pass arguments to functions, including positional arguments, keyword arguments, default arguments, and variable-length arguments.

In this lesson, we'll learn how these different argument types work and when to use them.

---

## Table of Contents

- Parameters vs Arguments
- Positional Arguments
- Keyword Arguments
- Default Arguments
- Variable-Length Positional Arguments (`*args`)
- Variable-Length Keyword Arguments (`**kwargs`)
- Combining Different Argument Types
- Argument Ordering Rules
- Best Practices
- Common Mistakes
- Interview Questions
- Data Engineering Perspective
- Summary

---

# 1. Parameters vs Arguments

Parameters and arguments are closely related, but they are not the same thing.

A **parameter** is a variable defined in the function definition.

An **argument** is the actual value passed when calling the function.

### Example

```python
def greet(name):
    print(f"Hello, {name}")

greet("Onkar")
```

Here:

```text
name       → Parameter
"Onkar"    → Argument
```

---

# 2. Positional Arguments

Positional arguments are assigned to parameters according to their **position**.

### Example

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Rahul", 22)
```

**Output**

```text
Name: Rahul
Age: 22
```

Python assigns:

```text
"Rahul" → name
22      → age
```

The order is important.

### Example

```python
def subtract(a, b):
    print(a - b)

subtract(20, 5)
```

**Output**

```text
15
```

Changing the order changes the result:

```python
subtract(5, 20)
```

**Output**

```text
-15
```

> [!IMPORTANT]
> With positional arguments, values are assigned based on their position.

---

# 3. Keyword Arguments

Keyword arguments specify the parameter name when calling the function.

### Example

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(name="Rahul", age=22)
```

Keyword arguments allow us to change the order:

```python
student(age=22, name="Rahul")
```

**Output**

```text
Name: Rahul
Age: 22
```

Because the parameter names are specified, Python knows where each value belongs.

---

# 4. Default Arguments

A default argument provides a predefined value for a parameter.

### Example

```python
def greet(name, message="Welcome"):
    print(f"{message}, {name}")

greet("Rahul")
```

**Output**

```text
Welcome, Rahul
```

The default value can be overridden:

```python
greet("Rahul", "Good Morning")
```

**Output**

```text
Good Morning, Rahul
```

### Another Example

```python
def calculate_price(price, quantity=1):
    return price * quantity

print(calculate_price(500))
print(calculate_price(500, 4))
```

**Output**

```text
500
2000
```

> [!NOTE]
> Default arguments are useful when a parameter commonly uses the same value.

---

# 5. Variable-Length Positional Arguments (`*args`)

Sometimes we don't know how many positional arguments will be passed to a function.

Python provides `*args` for this situation.

### Syntax

```python
def function_name(*args):
    statements
```

### Example

```python
def display_numbers(*numbers):
    print(numbers)

display_numbers(10, 20, 30, 40)
```

**Output**

```text
(10, 20, 30, 40)
```

The values are collected into a **tuple**.

### Example – Sum Multiple Numbers

```python
def calculate_total(*numbers):
    return sum(numbers)

print(calculate_total(10, 20))
print(calculate_total(10, 20, 30))
print(calculate_total(10, 20, 30, 40))
```

**Output**

```text
30
60
100
```

> [!NOTE]
> `args` is a naming convention. The `*` is what provides the variable-length positional argument behavior.

---

# 6. Variable-Length Keyword Arguments (`**kwargs`)

`**kwargs` allows a function to receive an arbitrary number of keyword arguments.

### Syntax

```python
def function_name(**kwargs):
    statements
```

### Example

```python
def student_details(**details):
    print(details)

student_details(
    name="Rahul",
    age=22,
    city="Pune"
)
```

**Output**

```text
{'name': 'Rahul', 'age': 22, 'city': 'Pune'}
```

The arguments are collected into a **dictionary**.

### Accessing Values

```python
def student_details(**details):
    print("Name:", details["name"])
    print("Age:", details["age"])

student_details(name="Rahul", age=22)
```

**Output**

```text
Name: Rahul
Age: 22
```

> [!NOTE]
> `kwargs` stands for keyword arguments by convention. The `**` syntax is what provides the behavior.

---

# 7. Combining Different Argument Types

Python allows different types of arguments to be used together.

### Example

```python
def employee(name, department="IT", *skills):
    print("Name:", name)
    print("Department:", department)
    print("Skills:", skills)

employee(
    "Rahul",
    "Data Engineering",
    "Python",
    "SQL",
    "Spark"
)
```

**Output**

```text
Name: Rahul
Department: Data Engineering
Skills: ('Python', 'SQL', 'Spark')
```

Another example:

```python
def profile(name, **details):
    print("Name:", name)

    for key, value in details.items():
        print(key, ":", value)

profile(
    "Rahul",
    city="Pune",
    role="Data Engineer"
)
```

---

# 8. Argument Ordering Rules

Argument ordering is important in Python.

A common function-definition order is:

```python
def function_name(
    required_parameter,
    default_parameter=value,
    *args,
    **kwargs
):
    pass
```

For example:

```python
def employee(name, department="IT", *skills, **details):
    pass
```

When calling functions, positional arguments generally come before keyword arguments.

Correct:

```python
def student(name, age):
    print(name, age)

student("Rahul", age=22)
```

Incorrect:

```python
student(name="Rahul", 22)
```

This produces a `SyntaxError`.

---

# Best Practices

- Use positional arguments when the meaning of values is obvious.
- Use keyword arguments when they improve readability.
- Use sensible default values.
- Avoid functions with too many parameters.
- Use `*args` only when the number of positional arguments can vary.
- Use `**kwargs` when flexible keyword-based configuration is required.
- Use descriptive parameter names.

### Good

```python
def calculate_salary(base_salary, bonus=0):
    return base_salary + bonus
```

### Avoid

```python
def calc(a, b=0):
    return a + b
```

Meaningful parameter names make functions easier to understand.

---

# Common Mistakes

### Incorrect Number of Arguments

```python
def add(a, b):
    return a + b

add(10)
```

This raises a `TypeError` because `b` was not provided.

---

### Incorrect Positional Order

```python
def employee(name, age):
    print(name, age)

employee(22, "Rahul")
```

Python accepts this call, but the values are assigned to the wrong parameters.

---

### Default Parameter Before Required Parameter

Incorrect:

```python
def employee(department="IT", name):
    pass
```

Correct:

```python
def employee(name, department="IT"):
    pass
```

---

### Confusing `*args` and `**kwargs`

Remember:

```text
*args    → Multiple positional arguments → Tuple
**kwargs → Multiple keyword arguments    → Dictionary
```

> [!WARNING]
> `*args` and `**kwargs` provide flexibility, but using them unnecessarily can make function interfaces harder to understand.

---

# Interview Questions

### What is the difference between a parameter and an argument?

A parameter is defined in the function definition, while an argument is the actual value supplied when calling the function.

### What are positional arguments?

Arguments assigned to parameters according to their position.

### What are keyword arguments?

Arguments passed using parameter names.

### What is a default argument?

A parameter with a predefined value that is used when the caller does not provide that argument.

### What is `*args`?

`*args` allows a function to receive a variable number of positional arguments. They are collected into a tuple.

### What is `**kwargs`?

`**kwargs` allows a function to receive a variable number of keyword arguments. They are collected into a dictionary.

### What is the difference between `*args` and `**kwargs`?

```text
*args    → Positional arguments → Tuple
**kwargs → Keyword arguments    → Dictionary
```

### Are the names `args` and `kwargs` mandatory?

No. They are conventions.

For example, this is valid:

```python
def total(*numbers):
    return sum(numbers)
```

The `*` and `**` operators provide the special behavior.

---

# Data Engineering Perspective

Function arguments are particularly useful in Data Engineering because reusable pipeline functions often need different configurations.

For example:

```python
def load_data(file_path, file_type="csv"):
    print("File:", file_path)
    print("Type:", file_type)

load_data("customers.csv")
load_data("orders.json", file_type="json")
```

Default arguments provide sensible pipeline defaults while still allowing customization.

Keyword arguments can make configuration clearer:

```python
def process_data(source, destination, batch_size=1000):
    print("Source:", source)
    print("Destination:", destination)
    print("Batch Size:", batch_size)

process_data(
    source="raw/customers.csv",
    destination="processed/customers.csv",
    batch_size=5000
)
```

`**kwargs` can also support flexible configuration:

```python
def pipeline_config(**config):
    for key, value in config.items():
        print(f"{key}: {value}")

pipeline_config(
    source="Azure Blob Storage",
    format="CSV",
    batch_size=5000
)
```

Function arguments are commonly used for:

- File paths
- Database connections
- Table names
- Batch sizes
- Pipeline configuration
- API parameters
- Transformation settings
- Environment-specific values

Understanding arguments allows us to build functions that are reusable instead of hardcoding values inside them.

---

# Summary

After completing this lesson, you should be able to:

- Explain the difference between parameters and arguments.
- Use positional arguments.
- Use keyword arguments.
- Define default arguments.
- Use `*args` for variable-length positional arguments.
- Use `**kwargs` for variable-length keyword arguments.
- Explain how `*args` creates a tuple.
- Explain how `**kwargs` creates a dictionary.
- Combine different argument types.
- Follow argument-ordering rules.
- Use function arguments in practical programs.

---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](../README.md)

⬅️ **Previous:** [Day 10 - Functions](../Day_10_Functions/README.md)

➡️ **Next:** [Day 12 - Recursion](../Day_12_Recursion/README.md)