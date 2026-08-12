# 🐍 Day 24 - Decorators

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Level](https://img.shields.io/badge/Level-Intermediate-success)

---

## Overview

A **decorator** is a Python feature that allows us to add or modify the behavior of a function or class without changing its original source code.

Decorators are built on an important Python concept:

> **Functions are first-class objects.**

That means a function can be:

- Stored in a variable
- Passed as an argument
- Returned from another function
- Stored inside a data structure

Decorators are heavily used in real Python applications and libraries.

Common examples include:

- Logging
- Timing functions
- Authentication and authorization
- Validation
- Caching
- Retry logic
- Monitoring
- Web frameworks
- API frameworks

The most important concepts for this day are:

- First-class functions
- Higher-order functions
- Nested functions
- Closures
- `@decorator` syntax
- `*args` and `**kwargs`
- `functools.wraps`
- Stacking decorators
- Decorators with arguments
- Class decorators
- Practical Data Engineering use cases

> [!IMPORTANT]
> A decorator **wraps existing behavior**. It lets us add behavior before, after, or around a function call without modifying the function's original implementation.

---

## Table of Contents

- [1. What Is a Decorator?](#1-what-is-a-decorator)
- [2. Functions Are First-Class Objects](#2-functions-are-first-class-objects)
- [3. Passing Functions as Arguments](#3-passing-functions-as-arguments)
- [4. Returning Functions](#4-returning-functions)
- [5. Higher-Order Functions](#5-higher-order-functions)
- [6. Nested Functions](#6-nested-functions)
- [7. Closures](#7-closures)
- [8. Building a Simple Decorator](#8-building-a-simple-decorator)
- [9. Decorator Syntax](#9-decorator-syntax)
- [10. Decorators with Arguments](#10-decorators-with-arguments)
- [11. `*args` and `**kwargs`](#11-args-and-kwargs)
- [12. `functools.wraps`](#12-functoolswraps)
- [13. Returning the Wrapped Function Result](#13-returning-the-wrapped-function-result)
- [14. Decorator Execution vs Function Execution](#14-decorator-execution-vs-function-execution)
- [15. Stacking Multiple Decorators](#15-stacking-multiple-decorators)
- [16. Decorators with Their Own Arguments](#16-decorators-with-their-own-arguments)
- [17. Class Decorators](#17-class-decorators)
- [18. Built-in and Standard Library Decorators](#18-built-in-and-standard-library-decorators)
- [19. Practical Decorator Patterns](#19-practical-decorator-patterns)
- [20. Common Mistakes](#20-common-mistakes)
- [21. Interview Follow-up Questions](#21-interview-follow-up-questions)
- [22. Data Engineering Perspective](#22-data-engineering-perspective)

---

# 1. What Is a Decorator?

A decorator is a callable that takes another function and returns a modified or enhanced callable.

Basic idea:

```text
Original Function
       ↓
   Decorator
       ↓
Wrapped Function
       ↓
Additional Behavior
```

For example, suppose we have:

```python
def greet():
    print("Hello")
```

We can create a decorator that prints a message before and after `greet()` executes.

The original `greet()` function does not need to be changed.

This gives us a clean separation between:

```text
Business logic
      +
Cross-cutting behavior
```

Examples of cross-cutting behavior include logging, timing, validation, retries, and authorization.

---

# 2. Functions Are First-Class Objects

Before understanding decorators, understand this concept.

In Python, functions are objects.

We can assign a function to a variable:

```python
def greet():
    print("Hello")

message = greet
message()
```

`message` now refers to the same function object.

We can also put functions in a list:

```python
def add():
    print("Add")


def subtract():
    print("Subtract")

operations = [add, subtract]
```

Then:

```python
for operation in operations:
    operation()
```

This works because functions can be treated like other Python objects.

That property makes decorators possible.

---

# 3. Passing Functions as Arguments

A function can receive another function as an argument.

Example:

```python
def execute(function):
    function()
```

Now:

```python
def greet():
    print("Hello")

execute(greet)
```

Execution flow:

```text
greet
  ↓
passed into execute()
  ↓
function()
  ↓
Hello
```

This is one of the foundations of decorators.

---

# 4. Returning Functions

A function can also return another function.

Example:

```python
def outer():
    def inner():
        print("Inside inner")

    return inner
```

Now:

```python
function = outer()
function()
```

The returned object is the `inner` function.

This is another important building block for decorators:

```text
Decorator
    ↓
takes a function
    ↓
creates wrapper
    ↓
returns wrapper
```

---

# 5. Higher-Order Functions

A **higher-order function** is a function that does at least one of these:

1. Takes a function as an argument.
2. Returns a function.

Example:

```python
def apply_operation(function, value):
    return function(value)
```

Then:

```python
def square(number):
    return number * number

print(apply_operation(square, 5))
```

Output:

```text
25
```

Decorators are a practical application of higher-order functions.

---

# 6. Nested Functions

A function defined inside another function is called a nested function.

Example:

```python
def outer():
    def inner():
        print("Hello")

    inner()
```

`inner()` exists inside the scope of `outer()`.

Nested functions are useful when implementing decorators because the wrapper function can live inside the decorator.

Typical decorator structure:

```python
def decorator(function):
    def wrapper():
        # Additional behavior
        function()

    return wrapper
```

---

# 7. Closures

A **closure** occurs when an inner function remembers values from its enclosing scope even after the outer function has finished executing.

Example:

```python
def multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply
```

Now:

```python
double = multiplier(2)

print(double(10))
```

Output:

```text
20
```

Why does `multiply()` know that `factor` is `2`?

Because the inner function closes over the variable from the enclosing scope.

Closures are closely related to decorators because the wrapper often remembers the original function.

---

# 8. Building a Simple Decorator

Let's build one step by step.

Original function:

```python
def greet():
    print("Hello")
```

Decorator:

```python
def log_call(function):
    def wrapper():
        print("Function started")
        function()
        print("Function finished")

    return wrapper
```

Apply it manually:

```python
greet = log_call(greet)
```

Now:

```python
greet()
```

Output:

```text
Function started
Hello
Function finished
```

Notice what happened:

```text
greet
  ↓
log_call(greet)
  ↓
wrapper returned
  ↓
greet now refers to wrapper
```

This is the core mechanism of a decorator.

---

# 9. Decorator Syntax

Python provides `@` syntax to make decorators easier to read.

Instead of:

```python
def greet():
    print("Hello")

greet = log_call(greet)
```

we can write:

```python
@log_call
def greet():
    print("Hello")
```

This is equivalent to:

```python
def greet():
    print("Hello")

greet = log_call(greet)
```

The `@decorator` line is placed immediately above the function definition.

---

# 10. Decorators with Arguments

Real functions often accept arguments.

For example:

```python
def greet(name):
    print(f"Hello {name}")
```

A wrapper that accepts no arguments would fail:

```python
def decorator(function):
    def wrapper():
        function()

    return wrapper
```

We need a flexible wrapper.

---

# 11. `*args` and `**kwargs`

Use `*args` and `**kwargs` when the decorator should support functions with different signatures.

Example:

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before function")

        result = function(*args, **kwargs)

        print("After function")

        return result

    return wrapper
```

Now it can work with:

```python
def greet(name):
    print(f"Hello {name}")
```

and:

```python
def add(a, b):
    return a + b
```

The wrapper forwards:

```text
*args
→ positional arguments

**kwargs
→ keyword arguments
```

This is one of the most important patterns to remember when writing decorators.

---

# 12. `functools.wraps`

A decorator can replace the original function with a wrapper.

This can cause metadata such as the original function's name and documentation to be lost.

Example:

```python
from functools import wraps
```

Then:

```python
def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

`@wraps(function)` copies important metadata from the original function to the wrapper.

For example:

```python
print(function.__name__)
```

can remain meaningful after decoration.

> [!IMPORTANT]
> In production-quality decorators, `functools.wraps` is generally the right default because it preserves useful introspection metadata and improves debugging and documentation behavior.

---

# 13. Returning the Wrapped Function Result

Suppose the original function returns a value:

```python
@decorator
def add(a, b):
    return a + b
```

The wrapper must return the result:

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper
```

If we forget:

```python
return result
```

the decorated function may return `None` even though the original function returned a value.

This is a very common decorator mistake.

---

# 14. Decorator Execution vs Function Execution

There are two different moments to understand.

When Python processes:

```python
@decorator
def greet():
    print("Hello")
```

the decoration occurs when the function definition is executed.

Conceptually:

```python
def greet():
    print("Hello")

greet = decorator(greet)
```

Later, when we call:

```python
greet()
```

the wrapper executes.

So:

```text
Function definition
       ↓
Decorator applied
       ↓
Decorated function stored
       ↓
Function call
       ↓
Wrapper executes
       ↓
Original function executes
```

This distinction is frequently tested in interviews.

---

# 15. Stacking Multiple Decorators

We can apply multiple decorators to one function.

Example:

```python
@decorator_one
@decorator_two
def greet():
    print("Hello")
```

This is conceptually equivalent to:

```python
greet = decorator_one(decorator_two(greet))
```

Therefore, decorators are applied from the bottom upward during decoration.

But when the decorated function is called, the outer wrapper executes first.

Think:

```text
Decoration:

greet
 ↓
decorator_two
 ↓
decorator_one

Call:

decorator_one wrapper
 ↓
decorator_two wrapper
 ↓
greet
```

Understanding this ordering is an important interview topic.

---

# 16. Decorators with Their Own Arguments

Sometimes the decorator itself needs configuration.

Example:

```python
@repeat(3)
def greet():
    print("Hello")
```

Now we need three levels:

```text
repeat(3)
   ↓
decorator
   ↓
wrapper
   ↓
original function
```

Example implementation:

```python
def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)

        return wrapper

    return decorator
```

The outer function receives the decorator configuration.

The middle function receives the original function.

The inner function executes when the decorated function is called.

---

# 17. Class Decorators

A decorator can also be applied to a class.

Example:

```python
def add_attribute(cls):
    cls.category = "Data Engineering"
    return cls
```

Then:

```python
@add_attribute
class Pipeline:
    pass
```

Now:

```python
print(Pipeline.category)
```

returns:

```text
Data Engineering
```

Class decorators can modify or register classes, although function decorators are more common in everyday Python code.

---

# 18. Built-in and Standard Library Decorators

Python and its standard library provide useful decorators.

### `@staticmethod`

Defines a method that does not receive an implicit instance or class reference.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

### `@classmethod`

Defines a method that receives the class as `cls`.

```python
class User:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

### `@property`

Allows a method to be accessed like an attribute.

```python
class User:
    def __init__(self, name):
        self.name = name

    @property
    def username(self):
        return self.name.lower()
```

### `@functools.lru_cache`

Caches function results.

```python
from functools import lru_cache

@lru_cache
 def square(number):
    return number * number
```

These examples show that decorators are deeply integrated into Python itself.

---

# 19. Practical Decorator Patterns

Decorators are particularly useful for cross-cutting behavior.

## Logging

```python
@log_execution
def process_data():
    ...
```

The decorator can record when the function starts, finishes, or fails.

## Timing

```python
@measure_time
def transform_data():
    ...
```

Useful for identifying slow pipeline stages.

## Retry

```python
@retry(attempts=3)
def call_api():
    ...
```

Useful for transient failures when retrying is appropriate.

## Validation

```python
@validate_record
def load_record(record):
    ...
```

Can enforce preconditions before business logic runs.

## Authorization

```python
@requires_permission("admin")
def delete_data():
    ...
```

Common in web applications and service layers.

> [!TIP]
> In Data Engineering, decorators can centralize repetitive operational behavior while keeping the actual transformation or business logic focused.

---

# 20. Common Mistakes

## Mistake 1: Forgetting `return wrapper`

Incorrect:

```python
def decorator(function):
    def wrapper():
        function()
```

The decorator does not return the wrapper.

Correct:

```python
def decorator(function):
    def wrapper():
        function()

    return wrapper
```

---

## Mistake 2: Not Forwarding Arguments

This fails for functions that accept parameters:

```python
def wrapper():
    function()
```

Prefer:

```python
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

---

## Mistake 3: Forgetting the Return Value

If the original function returns a result, the wrapper should usually return it too.

```python
result = function(*args, **kwargs)
return result
```

---

## Mistake 4: Forgetting `functools.wraps`

Without `wraps`, debugging and introspection can become less informative because the wrapper may replace metadata from the original function.

---

## Mistake 5: Confusing Decoration with Execution

This:

```python
@decorator
def greet():
    ...
```

applies the decorator during function definition.

The function body does not run merely because the decorator is applied, unless the decorator itself calls the function.

---

## Mistake 6: Overusing Decorators

Decorators are powerful, but too many layers can make control flow difficult to understand.

Use them when the behavior is genuinely reusable and cross-cutting.

---

# 21. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is a decorator in Python?

<details>
<summary><strong>Answer</strong></summary>

A decorator is a callable that takes another function or class and returns a modified or enhanced callable.

Example:

```python
def log_call(function):
    def wrapper(*args, **kwargs):
        print("Before")
        result = function(*args, **kwargs)
        print("After")
        return result

    return wrapper
```

It can then be used as:

```python
@log_call
def greet():
    print("Hello")
```

The decorator adds behavior without modifying the original function's source code.

</details>

---

### Q2. What is the difference between a decorator and a higher-order function?

<details>
<summary><strong>Answer</strong></summary>

A higher-order function is any function that takes a function as an argument or returns a function.

A decorator is a specific pattern that uses this capability to wrap or modify another callable.

So:

```text
Higher-order function
        ↓
General concept

Decorator
        ↓
Specific function/class wrapping pattern
```

A decorator is therefore built using higher-order-function behavior.

</details>

---

### Q3. Why do we use `*args` and `**kwargs` inside decorators?

<details>
<summary><strong>Answer</strong></summary>

A decorator should often work with functions that have different parameters.

```python
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

`*args` captures positional arguments and `**kwargs` captures keyword arguments.

This allows the wrapper to forward the original function's arguments without hard-coding a particular signature.

</details>

---

### Q4. Why is `functools.wraps` important?

<details>
<summary><strong>Answer</strong></summary>

When a decorator replaces the original function with a wrapper, metadata such as the function name and docstring can otherwise refer to the wrapper.

Using:

```python
from functools import wraps

@wraps(function)
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

preserves important metadata from the wrapped function.

This improves debugging, introspection, documentation, and compatibility with tooling.

</details>

---

### Q5. In what order are multiple decorators applied?

<details>
<summary><strong>Answer</strong></summary>

Given:

```python
@decorator_one
@decorator_two
def greet():
    pass
```

Python conceptually creates:

```python
greet = decorator_one(decorator_two(greet))
```

So `decorator_two` is applied to the original function first, and `decorator_one` wraps that result.

When `greet()` is called, the outer `decorator_one` wrapper executes first.

</details>

---

### Q6. What is the difference between a closure and a decorator?

<details>
<summary><strong>Answer</strong></summary>

A closure is an inner function that retains access to variables from an enclosing scope after that enclosing function has returned.

A decorator is a pattern for wrapping or modifying a callable.

They are related because decorators commonly use closures:

```python
def decorator(function):
    def wrapper():
        function()

    return wrapper
```

Here `wrapper` retains access to `function` from the enclosing `decorator` scope.

So a decorator can use a closure, but the concepts are not identical.

</details>

---

### Q7. How would you create a retry decorator for an API call?

<details>
<summary><strong>Answer</strong></summary>

I would create a parameterized decorator that retries only the exceptions known to be transient.

A simplified structure is:

```python
def retry(attempts):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return function(*args, **kwargs)
                except ConnectionError:
                    if attempt == attempts - 1:
                        raise
        return wrapper
    return decorator
```

In production, I would also consider exponential backoff, jitter, timeout behavior, idempotency, and which failures are actually safe to retry.

</details>

---

### Q8. Where could decorators be useful in a Data Engineering project?

<details>
<summary><strong>Answer</strong></summary>

Decorators can centralize cross-cutting pipeline behavior such as:

- Logging
- Execution-time measurement
- Retry handling
- Validation
- Metrics collection
- Audit information
- Error reporting

For example:

```python
@log_execution
@measure_time
@retry(attempts=3)
def load_data():
    ...
```

The exact order should be chosen carefully because different decorator orderings can change behavior.

The main benefit is keeping operational concerns separate from the core transformation logic.

</details>

---

# 22. Data Engineering Perspective

Data Engineering applications often contain repeated operational logic around pipeline functions.

Suppose we have:

```python
def extract_data():
    ...


def transform_data():
    ...


def load_data():
    ...
```

We may want every stage to have:

- Logging
- Execution timing
- Error reporting
- Metrics

Without decorators, we may repeatedly write the same code around every function.

With decorators:

```python
@log_execution
@measure_time
def extract_data():
    ...


@log_execution
@measure_time
def transform_data():
    ...


@log_execution
@measure_time
def load_data():
    ...
```

The pipeline functions remain focused on their actual responsibilities.

A simplified architecture is:

```text
                Pipeline Function
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Logging      Timing       Retry
          │            │            │
          └────────────┼────────────┘
                       ↓
                 Business Logic
```

### Example: Timing a Transformation

```python
from functools import wraps
from time import perf_counter


def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        try:
            return function(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            print(f"{function.__name__}: {elapsed:.4f}s")

    return wrapper
```

Then:

```python
@measure_time
def transform_records(records):
    return [record.upper() for record in records]
```

The transformation code does not need to know how timing is implemented.

> [!IMPORTANT]
> For interviews, remember the core chain:
>
> ```text
> Function is an object
>        ↓
> Can pass function as argument
>        ↓
> Can return function
>        ↓
> Higher-order function
>        ↓
> Decorator
>        ↓
> Wrapper adds behavior
> ```
>
> The most important practical use in Data Engineering is separating **cross-cutting operational behavior** such as logging, timing, retries, and validation from the core pipeline logic.

---

## Navigation

⬅️ **Previous:** [23 - Iterators and Generators](../23_Iterators_and_Generators/readme.md)

➡️ **Next:** [25 - Context Managers](../25_Context_Managers/readme.md)
