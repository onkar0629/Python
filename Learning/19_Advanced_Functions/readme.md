# 🐍 Day 19 - Advanced Functions

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Level](https://img.shields.io/badge/Level-Intermediate-success)

---

## Overview

Functions are one of the most important building blocks in Python.

In the earlier Python lessons, we learned how to create and call functions. Now we move beyond basic functions and learn how Python treats functions as **first-class objects**.

This means a function can be:

- Stored in a variable
- Passed as an argument
- Returned from another function
- Stored inside a collection

We will also learn important topics used frequently in interviews and real Data Engineering code:

- Positional arguments
- Keyword arguments
- Default arguments
- `*args`
- `**kwargs`
- Argument unpacking
- Scope
- `global` and `nonlocal`
- Lambda functions
- Higher-order functions
- Functions returning functions
- Closures
- Recursion
- Decorators
- Practical pipeline examples

> [!IMPORTANT]
> The goal is not to memorize advanced syntax. The goal is to understand **how data moves into functions, how functions behave as objects, and how functions can be composed into reusable Data Engineering logic**.

---

## Table of Contents

- [1. Function Arguments](#1-function-arguments)
- [2. Positional Arguments](#2-positional-arguments)
- [3. Keyword Arguments](#3-keyword-arguments)
- [4. Default Arguments](#4-default-arguments)
- [5. Positional and Keyword Arguments Together](#5-positional-and-keyword-arguments-together)
- [6. `*args`](#6-args)
- [7. `**kwargs`](#7-kwargs)
- [8. Combining `*args` and `**kwargs`](#8-combining-args-and-kwargs)
- [9. Argument Unpacking](#9-argument-unpacking)
- [10. Scope](#10-scope)
- [11. `global`](#11-global)
- [12. `nonlocal`](#12-nonlocal)
- [13. Functions Are First-Class Objects](#13-functions-are-first-class-objects)
- [14. Passing Functions as Arguments](#14-passing-functions-as-arguments)
- [15. Returning Functions](#15-returning-functions)
- [16. Lambda Functions](#16-lambda-functions)
- [17. Higher-Order Functions](#17-higher-order-functions)
- [18. Closures](#18-closures)
- [19. Recursion](#19-recursion)
- [20. Decorators](#20-decorators)
- [21. Common Mistakes](#21-common-mistakes)
- [22. Interview Follow-up Questions](#22-interview-follow-up-questions)
- [23. Data Engineering Perspective](#23-data-engineering-perspective)

---

# 1. Function Arguments

A function can receive data through **parameters**.

```python
def greet(name):
    print("Hello", name)
```

Here:

```text
name → parameter
```

When we call:

```python
greet("Onkar")
```

`"Onkar"` is the argument passed to the function.

A useful distinction is:

```text
Parameter → variable defined in the function
Argument  → actual value supplied during the call
```

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

`a` and `b` are parameters.

`10` and `20` are arguments.

---

# 2. Positional Arguments

With positional arguments, values are assigned according to their position.

```python
def introduce(name, age):
    print(name)
    print(age)
```

Call:

```python
introduce("Onkar", 22)
```

Python assigns:

```text
name → "Onkar"
age  → 22
```

If the order changes:

```python
introduce(22, "Onkar")
```

the values are assigned differently.

> [!IMPORTANT]
> Positional arguments depend on **argument order**.

---

# 3. Keyword Arguments

Keyword arguments explicitly specify which parameter receives the value.

```python
def introduce(name, age):
    print(name)
    print(age)
```

We can call:

```python
introduce(age=22, name="Onkar")
```

The order does not matter because the parameter names identify the values.

This improves readability when a function has several parameters.

---

# 4. Default Arguments

A function parameter can have a default value.

```python
def greet(name, message="Hello"):
    print(message, name)
```

If we provide only `name`:

```python
greet("Onkar")
```

Python uses the default:

```text
Hello Onkar
```

We can override it:

```python
greet("Onkar", "Welcome")
```

Output:

```text
Welcome Onkar
```

### Important Rule

A non-default parameter cannot normally appear after a default parameter.

Invalid:

```python
def example(a=10, b):
    pass
```

This causes a `SyntaxError`.

Valid:

```python
def example(a, b=10):
    pass
```

---

# 5. Positional and Keyword Arguments Together

We can combine argument styles, but positional arguments must come before keyword arguments in a function call.

Valid:

```python
def connect(host, port, database):
    print(host, port, database)

connect("localhost", port=3306, database="sales")
```

Invalid:

```python
connect(host="localhost", 3306, database="sales")
```

Once Python starts receiving keyword arguments, you cannot place a positional argument after them.

> [!TIP]
> Keyword arguments make configuration-heavy functions easier to read.

---

# 6. `*args`

Sometimes we do not know how many positional arguments a function will receive.

`*args` collects extra positional arguments into a **tuple**.

```python
def total(*args):
    print(args)
```

Call:

```python
total(10, 20, 30)
```

Inside the function:

```text
args = (10, 20, 30)
```

We can process the tuple:

```python
def total(*args):
    return sum(args)
```

Then:

```python
print(total(10, 20, 30))
```

Output:

```text
60
```

`args` is only a conventional name. The important part is the `*`.

This is valid too:

```python
def total(*numbers):
    return sum(numbers)
```

---

# 7. `**kwargs`

`**kwargs` collects extra keyword arguments into a **dictionary**.

```python
def show_details(**kwargs):
    print(kwargs)
```

Call:

```python
show_details(name="Onkar", role="Data Engineer", city="Pune")
```

Inside the function:

```text
{
    'name': 'Onkar',
    'role': 'Data Engineer',
    'city': 'Pune'
}
```

The important distinction is:

```text
*args   → tuple of positional arguments
**kwargs → dictionary of keyword arguments
```

---

# 8. Combining `*args` and `**kwargs`

A function can accept both.

```python
def process(*args, **kwargs):
    print(args)
    print(kwargs)
```

Call:

```python
process(10, 20, name="Onkar", city="Pune")
```

Inside the function:

```text
args   → (10, 20)
kwargs → {'name': 'Onkar', 'city': 'Pune'}
```

A common function definition order is:

```text
normal parameters
*args
keyword-only parameters
**kwargs
```

For example:

```python
def example(a, b=10, *args, **kwargs):
    pass
```

The exact placement rules become important when designing flexible APIs.

---

# 9. Argument Unpacking

The `*` and `**` operators can also be used when **calling** functions.

## 9.1 List/Tuple Unpacking with `*`

Suppose:

```python
numbers = [10, 20, 30]
```

And:

```python
def add(a, b, c):
    return a + b + c
```

Instead of:

```python
add(numbers[0], numbers[1], numbers[2])
```

we can write:

```python
add(*numbers)
```

Python unpacks the sequence:

```text
*numbers
   ↓
10, 20, 30
```

## 9.2 Dictionary Unpacking with `**`

Suppose:

```python
config = {
    "host": "localhost",
    "port": 3306
}
```

And:

```python
def connect(host, port):
    print(host, port)
```

Call:

```python
connect(**config)
```

Python matches dictionary keys to parameter names.

```text
host → "localhost"
port → 3306
```

> [!IMPORTANT]
> `*` unpacks positional values. `**` unpacks keyword values.

---

# 10. Scope

**Scope** determines where a variable can be accessed.

Python commonly deals with these levels:

```text
Local
Enclosing
Global
Built-in
```

This is often remembered as **LEGB**.

### Local

A variable created inside a function is local to that function.

```python
def example():
    message = "Hello"
    print(message)
```

`message` normally cannot be accessed outside the function.

### Global

A variable created outside functions is global within the module.

```python
message = "Hello"

def example():
    print(message)
```

The function can read the global variable.

### Enclosing

When functions are nested, an inner function can access variables from its enclosing function.

This becomes especially important for **closures**.

### Built-in

Python provides built-in names such as:

```python
len
sum
print
max
```

If Python cannot find a name in local, enclosing, or global scope, it checks the built-in scope.

---

# 11. `global`

Normally, assigning to a variable inside a function creates a local variable.

```python
count = 0

def increment():
    count = 1
```

The `count` inside the function is local; it does not modify the global `count`.

If we explicitly want to assign to the global variable:

```python
count = 0

def increment():
    global count
    count += 1
```

Then:

```python
increment()
print(count)
```

Output:

```text
1
```

> [!WARNING]
> Excessive use of `global` can make code harder to reason about. Prefer passing data into functions and returning results when practical.

---

# 12. `nonlocal`

`nonlocal` is used inside a nested function when we want to modify a variable belonging to the **enclosing function**.

Example:

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner
```

Then:

```python
counter = outer()

print(counter())
print(counter())
```

Output:

```text
1
2
```

The inner function remembers the enclosing variable.

This behavior is closely connected to **closures**.

---

# 13. Functions Are First-Class Objects

In Python, functions are objects.

That means we can assign a function to a variable.

```python
def greet():
    print("Hello")

say_hello = greet
```

Now:

```python
say_hello()
```

calls the same function.

The function object can also be stored in a list:

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b

operations = [add, multiply]
```

We can call them through the list:

```python
print(operations[0](2, 3))
print(operations[1](2, 3))
```

Output:

```text
5
6
```

This is the foundation of higher-order functions and decorators.

---

# 14. Passing Functions as Arguments

A function can receive another function as an argument.

```python
def apply_operation(a, b, operation):
    return operation(a, b)
```

Define operations:

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b
```

Now:

```python
print(apply_operation(10, 20, add))
print(apply_operation(10, 20, multiply))
```

Output:

```text
30
200
```

The function `apply_operation()` does not need to know exactly which operation it will perform.

This is a powerful abstraction.

---

# 15. Returning Functions

A function can also return another function.

```python
def create_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply
```

Create a function:

```python
double = create_multiplier(2)
```

Then:

```python
print(double(10))
```

Output:

```text
20
```

The returned function remembers the `factor` supplied to `create_multiplier()`.

This leads directly to the concept of closures.

---

# 16. Lambda Functions

A lambda is a small anonymous function.

Normal function:

```python
def square(number):
    return number ** 2
```

Lambda equivalent:

```python
square = lambda number: number ** 2
```

Then:

```python
print(square(5))
```

Output:

```text
25
```

Syntax:

```text
lambda parameters: expression
```

A lambda contains one expression and automatically returns its result.

### Useful Example

```python
numbers = [5, 2, 9, 1]

numbers.sort(key=lambda number: number)
```

For dictionaries:

```python
students = [
    {"name": "Onkar", "score": 85},
    {"name": "Rahul", "score": 92}
]

students.sort(key=lambda student: student["score"])
```

The lambda tells `sort()` which value should be used as the sorting key.

> [!TIP]
> Use lambdas for small, simple expressions. If the logic needs multiple statements or a meaningful explanation, use `def` instead.

---

# 17. Higher-Order Functions

A **higher-order function** is a function that either:

1. Accepts another function as an argument, or
2. Returns a function.

Examples include:

```python
map()
filter()
sorted()
```

For example:

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, numbers))
```

Here:

```text
map() → higher-order function
lambda → function passed to map()
```

Another example:

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

`filter()` receives a function and uses it to decide which values should remain.

---

# 18. Closures

A closure occurs when an inner function remembers variables from its enclosing function even after the enclosing function has finished executing.

Example:

```python
def create_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply
```

Create two functions:

```python
double = create_multiplier(2)
triple = create_multiplier(3)
```

Now:

```python
print(double(10))
print(triple(10))
```

Output:

```text
20
30
```

Each returned function remembers its own `factor`.

Conceptually:

```text
create_multiplier(2)
        ↓
   factor = 2
        ↓
   returned function
        ↓
   remembers factor
```

Closures are useful for creating configurable functions and are an important foundation for decorators.

---

# 19. Recursion

Recursion occurs when a function calls itself.

A recursive function needs a **base case** so that recursion eventually stops.

Example: factorial.

```python
def factorial(number):

    if number == 0:
        return 1

    return number * factorial(number - 1)
```

For:

```python
factorial(4)
```

The calls conceptually become:

```text
4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1)
4 * 3 * 2 * 1 * factorial(0)
4 * 3 * 2 * 1 * 1
```

Result:

```text
24
```

Every recursive function should have a clearly defined stopping condition.

> [!WARNING]
> Python has a recursion depth limit. Recursion is not automatically the best approach for large iterative workloads.

---

# 20. Decorators

A decorator is a function that modifies or extends the behavior of another function without changing its original source code.

Basic example:

```python
def logger(function):

    def wrapper():
        print("Function started")
        function()
        print("Function finished")

    return wrapper
```

Apply it using `@`:

```python
@logger
def greet():
    print("Hello")
```

Calling:

```python
greet()
```

produces:

```text
Function started
Hello
Function finished
```

What happened?

```text
greet()
   ↓
wrapper()
   ↓
logging
   ↓
original greet()
```

The decorator replaced the original function reference with the wrapper function.

### Decorators with Arguments

Real functions often accept arguments, so a production-style decorator commonly uses `*args` and `**kwargs`:

```python
def logger(function):

    def wrapper(*args, **kwargs):
        print("Function started")
        result = function(*args, **kwargs)
        print("Function finished")
        return result

    return wrapper
```

This allows the decorator to work with functions having different signatures.

> [!IMPORTANT]
> Decorators combine several concepts from this chapter: **functions as objects, nested functions, `*args`, `**kwargs`, closures, and function replacement**.

---

# 21. Common Mistakes

## Mistake 1: Confusing `*args` and `**kwargs`

Remember:

```text
*args    → tuple
**kwargs → dictionary
```

---

## Mistake 2: Calling a Function Instead of Passing It

Correct:

```python
apply_operation(10, 20, add)
```

Here `add` is passed as a function object.

Different:

```python
apply_operation(10, 20, add())
```

`add()` calls the function immediately and passes its result.

---

## Mistake 3: Forgetting the Base Case in Recursion

Without a stopping condition, a recursive function keeps calling itself until Python raises a recursion-related error.

---

## Mistake 4: Using `global` Unnecessarily

Global mutable state can make programs difficult to test and reason about.

Prefer explicit inputs and outputs when possible.

---

## Mistake 5: Overusing Lambda

This:

```python
lambda x: x * 2
```

is readable.

A very complicated lambda is not.

Use a named function when the transformation deserves a meaningful name.

---

## Mistake 6: Forgetting to Return from a Wrapper

A decorator wrapper often needs to return the original function's result:

```python
result = function(*args, **kwargs)
return result
```

Without the return statement, the caller may unexpectedly receive `None`.

---

# 22. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is the difference between `*args` and `**kwargs`?

<details>
<summary><strong>Answer</strong></summary>

`*args` collects extra **positional arguments** into a tuple.

```python
def example(*args):
    print(args)

example(10, 20, 30)
```

Inside the function:

```text
args = (10, 20, 30)
```

`**kwargs` collects extra **keyword arguments** into a dictionary.

```python
def example(**kwargs):
    print(kwargs)

example(name="Onkar", city="Pune")
```

Inside the function:

```text
kwargs = {'name': 'Onkar', 'city': 'Pune'}
```

</details>

---

### Q2. What is the difference between passing `add` and passing `add()` to another function?

<details>
<summary><strong>Answer</strong></summary>

`add` refers to the function object itself.

```python
apply_operation(10, 20, add)
```

The receiving function can call `add` later.

`add()` immediately executes the function and passes its returned value:

```python
apply_operation(10, 20, add())
```

So:

```text
add  → function object
add() → result of executing the function
```

This distinction is fundamental to higher-order functions and decorators.

</details>

---

### Q3. What is a closure in Python?

<details>
<summary><strong>Answer</strong></summary>

A closure is an inner function that retains access to variables from its enclosing function even after the enclosing function has returned.

```python
def create_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply


double = create_multiplier(2)

print(double(10))
```

Output:

```text
20
```

The returned `multiply` function remembers `factor = 2`.

</details>

---

### Q4. What is the difference between `global` and `nonlocal`?

<details>
<summary><strong>Answer</strong></summary>

`global` refers to a variable in the module/global scope.

```python
count = 0

def increment():
    global count
    count += 1
```

`nonlocal` refers to a variable in an enclosing function scope.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
```

In short:

```text
global   → global/module scope
nonlocal → enclosing function scope
```

</details>

---

### Q5. What is a higher-order function?

<details>
<summary><strong>Answer</strong></summary>

A higher-order function accepts another function as an argument, returns a function, or does both.

Example:

```python
def apply_operation(a, b, operation):
    return operation(a, b)
```

Here `operation` is a function passed into another function.

Built-in examples include:

- `map()`
- `filter()`
- `sorted()` through its `key` function

</details>

---

### Q6. Why are decorators useful in Data Engineering?

<details>
<summary><strong>Answer</strong></summary>

Decorators allow cross-cutting behavior to be added without duplicating the same code across many functions.

Examples include:

- Logging
- Timing
- Retry handling
- Validation
- Access control
- Monitoring

For example, a pipeline function can be wrapped to record its execution time without changing the transformation logic itself.

```python
@timer

def transform_data(data):
    return clean(data)
```

This separates the transformation logic from operational concerns such as observability.

</details>

---

### Q7. What happens if a decorator wrapper does not return the original function's result?

<details>
<summary><strong>Answer</strong></summary>

The decorated function may unexpectedly return `None`.

For example:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        # Missing: return result

    return wrapper
```

Even if `function()` returns a value, `wrapper()` does not return it.

The safer pattern is:

```python
def wrapper(*args, **kwargs):
    result = function(*args, **kwargs)
    return result
```

This is a common decorator interview mistake.

</details>

---

### Q8. When would you use a normal function instead of a lambda?

<details>
<summary><strong>Answer</strong></summary>

Use a lambda for a small, simple one-expression transformation.

```python
numbers.sort(key=lambda x: x)
```

Use `def` when the logic is complex, reused, needs documentation, contains multiple statements, or deserves a meaningful name.

For example:

```python
def calculate_customer_score(customer):
    # Complex business rules can be explained here.
    ...
```

The interview principle is **readability and maintainability**, not simply reducing the number of lines.

</details>

---

# 23. Data Engineering Perspective

Advanced functions become useful when building reusable pipeline components.

## 23.1 Reusable Transformations

Instead of writing transformation logic repeatedly:

```python
def clean_name(name):
    return name.strip().title()
```

Then apply it consistently:

```python
names = [" onkar ", " rahul ", " amit "]

cleaned = [clean_name(name) for name in names]
```

This keeps the business rule in one place.

## 23.2 Configurable Pipeline Functions

`**kwargs` can be useful for passing optional configuration.

```python
def load_data(data, **config):
    batch_size = config.get("batch_size", 1000)
    target = config.get("target", "sales")

    print(batch_size)
    print(target)
```

Call:

```python
load_data(
    data,
    batch_size=5000,
    target="orders"
)
```

The function can accept optional configuration without requiring every possible option to become a separate parameter.

For production APIs, however, explicit parameters are often preferable when the expected configuration is stable and well-defined.

## 23.3 Generic Transformation Functions

Higher-order functions allow transformation behavior to be supplied dynamically.

```python
def transform_records(records, transform_function):
    return [
        transform_function(record)
        for record in records
    ]
```

Then:

```python
def get_customer_id(record):
    return record["customer_id"]
```

We can pass the function:

```python
ids = transform_records(records, get_customer_id)
```

This creates reusable pipeline components.

## 23.4 Logging and Timing with Decorators

A decorator can add operational behavior around a pipeline step:

```text
Pipeline function
      ↓
Decorator
      ↓
Start timestamp
      ↓
Run transformation
      ↓
End timestamp
      ↓
Log duration
```

The transformation code does not need to contain timing logic itself.

## 23.5 Retry Logic

A decorator can also be used conceptually for retry behavior:

```text
Function call
     ↓
Try operation
     ↓
Success ─────→ return result
     ↓
Failure
     ↓
Retry
     ↓
Failure threshold reached
     ↓
Raise error
```

This pattern is common in ingestion pipelines where external systems can temporarily fail.

> [!IMPORTANT]
> Advanced Python functions are not just interview syntax. They provide the abstraction mechanisms needed to build **reusable, configurable, observable, and maintainable pipeline code**.

---

## Navigation

⬅️ **Previous:** [Day 18 - List Comprehension](../Day_18_List_Comprehension/readme.md)

➡️ **Next:** [Day 20 - Modules and Packages](../Day_20_Modules_and_Packages/readme.md)
