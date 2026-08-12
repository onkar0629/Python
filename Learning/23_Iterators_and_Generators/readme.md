# 🐍 Day 23 - Iterators and Generators

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Level](https://img.shields.io/badge/Level-Intermediate-success)

---

## Overview

Python provides **iterators and generators** for processing values one at a time instead of requiring all values to exist in memory at once.

This concept is especially important for Data Engineering because data pipelines often process:

- Large files
- Database result sets
- API responses
- Streaming data
- Large collections
- ETL records

The key concepts are:

- Iterable
- Iterator
- `iter()`
- `next()`
- `StopIteration`
- Iterator protocol
- Generator functions
- `yield`
- Generator expressions
- `yield from`
- Lazy evaluation
- Memory efficiency

> [!IMPORTANT]
> The main idea is **lazy processing**: produce or consume values when they are needed rather than creating the complete result immediately.

---

## Table of Contents

- [1. Iterable vs Iterator](#1-iterable-vs-iterator)
- [2. What Is an Iterable?](#2-what-is-an-iterable)
- [3. What Is an Iterator?](#3-what-is-an-iterator)
- [4. `iter()`](#4-iter)
- [5. `next()`](#5-next)
- [6. `StopIteration`](#6-stopiteration)
- [7. Iterator Protocol](#7-iterator-protocol)
- [8. Creating a Custom Iterator](#8-creating-a-custom-iterator)
- [9. Why Iterators Matter](#9-why-iterators-matter)
- [10. Generator Functions](#10-generator-functions)
- [11. `yield`](#11-yield)
- [12. Generator Execution](#12-generator-execution)
- [13. Generator vs Normal Function](#13-generator-vs-normal-function)
- [14. Generator Expressions](#14-generator-expressions)
- [15. Memory Efficiency](#15-memory-efficiency)
- [16. `yield from`](#16-yield-from)
- [17. Sending Values to a Generator](#17-sending-values-to-a-generator)
- [18. Generator Exceptions](#18-generator-exceptions)
- [19. Common Mistakes](#19-common-mistakes)
- [20. Interview Follow-up Questions](#20-interview-follow-up-questions)
- [21. Data Engineering Perspective](#21-data-engineering-perspective)

---

# 1. Iterable vs Iterator

This distinction is one of the most important interview concepts.

### Iterable

An **iterable** is an object that can provide its values one at a time.

Examples:

```python
list
string
tuple
set
dictionary
```

For example:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

The list is iterable.

### Iterator

An **iterator** is an object that keeps track of its current position and produces the next value when requested.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)
```

Now `iterator` can produce values using `next()`.

Think of it as:

```text
Iterable
   ↓ iter()
Iterator
   ↓ next()
Value
   ↓ next()
Value
   ↓ next()
Value
```

> [!TIP]
> A useful interview sentence is: **Every iterator is iterable, but not every iterable is an iterator.**

---

# 2. What Is an Iterable?

An iterable is an object that Python can iterate over.

Examples:

```python
numbers = [1, 2, 3]
name = "Onkar"
values = (10, 20, 30)
```

We can use them in a `for` loop:

```python
for number in numbers:
    print(number)
```

Python internally obtains an iterator from the iterable and repeatedly asks it for the next value.

Conceptually, the `for` loop behaves like:

```python
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
```

This is a very important connection between `for`, `iter()`, and `next()`.

---

# 3. What Is an Iterator?

An iterator implements the iterator protocol.

It provides:

```python
__iter__()
__next__()
```

Example:

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

The iterator remembers where it is.

After the third value, there are no more values.

---

# 4. `iter()`

`iter()` obtains an iterator from an iterable.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)
```

Now:

```python
print(next(iterator))
```

returns:

```text
10
```

Calling `next()` again returns the next value.

```python
print(next(iterator))
```

returns:

```text
20
```

`iter()` does not normally create a copy of the complete data structure. It obtains an iterator that manages traversal.

---

# 5. `next()`

`next()` requests the next value from an iterator.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

Once the iterator is exhausted, calling `next()` raises `StopIteration`.

You can provide a default value:

```python
print(next(iterator, "No more values"))
```

The default prevents `StopIteration` from being raised for that particular call.

---

# 6. `StopIteration`

`StopIteration` signals that an iterator has no more values.

Example:

```python
numbers = [10, 20]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

The third `next()` raises:

```text
StopIteration
```

A `for` loop handles this internally, which is why we normally do not see the exception when using:

```python
for number in numbers:
    print(number)
```

Conceptually:

```text
next()
 ↓
value exists → return value

next()
 ↓
no value → StopIteration
```

---

# 7. Iterator Protocol

Python's iterator protocol is based on two methods:

```python
__iter__()
__next__()
```

`__iter__()` returns an iterator.

`__next__()` returns the next value or raises `StopIteration` when exhausted.

A simplified protocol is:

```text
iter(iterable)
     ↓
iterator
     ↓
next(iterator)
     ↓
next value
     ↓
next(iterator)
     ↓
next value
     ↓
StopIteration
```

This protocol is what allows objects to work naturally with `for` loops.

---

# 8. Creating a Custom Iterator

We can create our own iterator class.

```python
class CountUpTo:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value
```

Usage:

```python
counter = CountUpTo(3)

for number in counter:
    print(number)
```

Output:

```text
1
2
3
```

The iterator stores its state in `self.current`.

Generators provide a simpler way to create many such stateful iterators.

---

# 9. Why Iterators Matter

Imagine a list containing 10 million records.

A list stores all records immediately:

```python
records = [create_record(i) for i in range(10_000_000)]
```

This can consume substantial memory.

An iterator can produce records as needed:

```text
Request record
     ↓
Generate / retrieve record
     ↓
Process record
     ↓
Request next record
```

This is called **lazy evaluation**.

It can reduce memory usage because the entire result does not have to be materialized at once.

> [!IMPORTANT]
> Iterators improve memory behavior, but they do not automatically make every operation faster. They can introduce repeated computation or I/O depending on how they are implemented.

---

# 10. Generator Functions

A generator function is a function that contains `yield`.

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Calling it:

```python
generator = numbers()
```

does not immediately execute all three statements.

It returns a generator object.

Values are produced when requested.

```python
print(next(generator))
print(next(generator))
print(next(generator))
```

Output:

```text
1
2
3
```

---

# 11. `yield`

`yield` produces a value and pauses the generator.

Example:

```python
def generate_numbers():
    yield 1
    yield 2
    yield 3
```

Execution works like:

```text
Call generator
     ↓
Pause at yield 1
     ↓ next()
Return 1
     ↓ next()
Resume
     ↓
Pause at yield 2
     ↓ next()
Return 2
```

The generator retains its execution state between calls.

This is different from `return`, which ends a normal function immediately.

---

# 12. Generator Execution

Consider:

```python
def demo():
    print("Step 1")
    yield 10
    print("Step 2")
    yield 20
```

When we create the generator:

```python
generator = demo()
```

the function body does not execute yet.

When we call:

```python
next(generator)
```

Python executes until the first `yield`.

Output:

```text
Step 1
```

The returned value is `10`.

Calling `next(generator)` again resumes execution after the first `yield`.

Then:

```text
Step 2
```

and the generator yields `20`.

> [!IMPORTANT]
> A generator function executes lazily. Creating the generator object does not execute the function body in the same way a normal function call does.

---

# 13. Generator vs Normal Function

Normal function:

```python
def get_numbers():
    return [1, 2, 3]
```

The complete list is created before the function returns.

Generator:

```python
def get_numbers():
    yield 1
    yield 2
    yield 3
```

Values are produced one at a time.

Comparison:

| Normal Function | Generator |
|---|---|
| Uses `return` | Uses `yield` |
| Usually produces result immediately | Produces values lazily |
| May store complete result | Can avoid materializing complete result |
| Function call completes before result is consumed | Generator pauses and resumes |
| Useful for complete collections | Useful for streaming/sequential processing |

---

# 14. Generator Expressions

A generator expression looks similar to a list comprehension but uses parentheses.

List comprehension:

```python
squares = [x * x for x in range(10)]
```

Generator expression:

```python
squares = (x * x for x in range(10))
```

The list comprehension creates the values immediately.

The generator expression produces them lazily.

Example:

```python
squares = (x * x for x in range(5))

for value in squares:
    print(value)
```

This is useful when the complete collection does not need to be stored.

---

# 15. Memory Efficiency

Consider:

```python
numbers = [x * x for x in range(1_000_000)]
```

The complete list is materialized.

Compare:

```python
numbers = (x * x for x in range(1_000_000))
```

The generator produces values as they are requested.

Conceptually:

```text
List comprehension
→ create 1,000,000 values
→ store them
→ process them

Generator
→ create one value
→ process it
→ create next value
```

This can dramatically reduce peak memory usage.

> [!WARNING]
> A generator is single-use in the normal case. If you need random access or repeated iteration, materializing a collection may be more appropriate.

---

# 16. `yield from`

`yield from` delegates iteration to another iterable or generator.

Example:

```python
def numbers():
    yield from [1, 2, 3]
```

This is roughly equivalent to yielding each value from the iterable.

It becomes particularly useful when composing generators.

Example:

```python
def first():
    yield 1
    yield 2


def second():
    yield 3
    yield 4


def combined():
    yield from first()
    yield from second()
```

Now:

```python
for number in combined():
    print(number)
```

produces:

```text
1
2
3
4
```

---

# 17. Sending Values to a Generator

Generators can also receive values using `send()`.

Example:

```python
def receiver():
    value = yield
    print("Received:", value)
```

First prime the generator:

```python
generator = receiver()
next(generator)
```

Then send a value:

```python
generator.send(100)
```

Output:

```text
Received: 100
```

This is an advanced generator feature.

For beginner Data Engineering work, focus first on:

```text
iter()
next()
yield
for
```

Then learn `send()` when you are comfortable with generator state and execution.

---

# 18. Generator Exceptions

Generators can raise exceptions like normal Python code.

Example:

```python
def numbers():
    for number in range(5):
        if number == 3:
            raise ValueError("Invalid number")
        yield number
```

When iteration reaches `3`, the generator raises `ValueError`.

We can handle it normally:

```python
try:
    for number in numbers():
        print(number)
except ValueError as error:
    print(error)
```

Generators therefore work naturally with the exception-handling concepts learned on Day 21.

---

# 19. Common Mistakes

## Mistake 1: Confusing Iterable and Iterator

A list is iterable but is not itself an iterator.

```python
numbers = [1, 2, 3]

iter(numbers)
```

returns an iterator.

---

## Mistake 2: Calling `next()` on a List

This is invalid:

```python
numbers = [1, 2, 3]
next(numbers)
```

A list is not an iterator.

Correct:

```python
iterator = iter(numbers)
next(iterator)
```

---

## Mistake 3: Expecting a Generator to Restart

```python
generator = (x for x in range(3))

for x in generator:
    print(x)

for x in generator:
    print(x)
```

The second loop produces nothing because the generator has already been exhausted.

If you need another pass, create another generator.

---

## Mistake 4: Converting a Generator to a List Immediately

```python
values = list(generator)
```

This materializes the complete result and removes much of the memory benefit of lazy iteration.

That may be completely valid when a list is actually required, but it should be intentional.

---

## Mistake 5: Using a Generator When Random Access Is Required

A generator does not support list-style indexing:

```python
generator[0]
```

If you need random access, a list or another suitable data structure may be better.

---

# 20. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is the difference between an iterable and an iterator?

<details>
<summary><strong>Answer</strong></summary>

An iterable is an object that can provide an iterator.

Examples include:

```python
list
string
tuple
set
```

An iterator maintains traversal state and provides the next value using `__next__()`.

```python
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))
```

The key relationship is:

```text
Iterable → iter() → Iterator → next() → Values
```

A useful interview statement is:

**Every iterator is iterable, but not every iterable is an iterator.**

</details>

---

### Q2. What happens internally when a `for` loop runs?

<details>
<summary><strong>Answer</strong></summary>

Python obtains an iterator from the iterable and repeatedly requests the next value.

Conceptually:

```python
iterator = iter(values)

while True:
    try:
        value = next(iterator)
    except StopIteration:
        break
```

So a `for` loop is closely connected to the iterator protocol.

</details>

---

### Q3. What is the difference between `return` and `yield`?

<details>
<summary><strong>Answer</strong></summary>

`return` ends a normal function and returns a result.

```python
def get_values():
    return [1, 2, 3]
```

`yield` produces a value from a generator and pauses its execution so that it can resume later.

```python
def get_values():
    yield 1
    yield 2
    yield 3
```

`yield` therefore supports lazy, stateful iteration.

</details>

---

### Q4. Why are generators useful for Data Engineering?

<details>
<summary><strong>Answer</strong></summary>

Generators can process data incrementally instead of materializing the complete result in memory.

For example, instead of creating a list containing millions of records, a generator can produce one record at a time:

```python
def read_records(records):
    for record in records:
        yield record
```

This can reduce peak memory usage and fits naturally with streaming or sequential ETL processing.

However, the actual architecture matters. A generator does not turn a single-machine pipeline into a distributed system by itself.

</details>

---

### Q5. What happens when a generator is exhausted?

<details>
<summary><strong>Answer</strong></summary>

When the generator has no more values, calling `next()` causes `StopIteration`.

```python
def numbers():
    yield 1

iterator = numbers()

print(next(iterator))
print(next(iterator))
```

The second call raises `StopIteration`.

A `for` loop handles this internally.

</details>

---

### Q6. What is the difference between a list comprehension and a generator expression?

<details>
<summary><strong>Answer</strong></summary>

List comprehension:

```python
squares = [x * x for x in range(1_000_000)]
```

creates the complete list immediately.

Generator expression:

```python
squares = (x * x for x in range(1_000_000))
```

produces values lazily.

Therefore, the generator expression generally has lower peak memory usage when the complete result does not need to be stored.

</details>

---

### Q7. Can you iterate over the same generator twice?

<details>
<summary><strong>Answer</strong></summary>

Normally, no.

A generator is an iterator and becomes exhausted after its values are consumed.

```python
generator = (x for x in range(3))

print(list(generator))
print(list(generator))
```

The second conversion produces an empty list.

If repeated iteration is required, create a new generator or use a reusable iterable such as a list when appropriate.

</details>

---

### Q8. When would you choose a list instead of a generator?

<details>
<summary><strong>Answer</strong></summary>

I would choose a list when I need:

- Random access
- Multiple iterations
- The complete dataset available at once
- Operations that require a materialized collection

I would consider a generator when:

- Data is processed sequentially
- The dataset is large
- I want lazy evaluation
- I want lower peak memory usage
- Values can be consumed once

The decision depends on the access pattern and memory requirements, not simply on the assumption that generators are always better.

</details>

---

# 21. Data Engineering Perspective

Iterators and generators are important because Data Engineering frequently involves sequential processing of large datasets.

Consider a simplified pipeline:

```text
Large Source
    ↓
Read One Record
    ↓
Validate
    ↓
Transform
    ↓
Load
    ↓
Read Next Record
```

A generator can represent the source stage:

```python
def generate_records(records):
    for record in records:
        yield record
```

Then downstream processing can consume records one at a time.

### Example

```python
def clean_records(records):
    for record in records:
        # Create a cleaned copy of the current record.
        cleaned = record.strip()

        # Produce the cleaned record immediately.
        yield cleaned
```

Then:

```python
for record in clean_records(records):
    load(record)
```

The complete cleaned dataset does not need to be stored before loading begins.

### Real-World Use Cases

Generators and iterators are useful concepts when working with:

- Large text files
- CSV processing
- Database cursors
- API pagination
- Log processing
- Batch ETL
- Streaming-style transformations
- Incremental processing

However, in production Data Engineering, memory efficiency is only one concern. You also need to consider:

- Fault tolerance
- Parallelism
- Retry behavior
- Data partitioning
- Checkpointing
- Backpressure
- Serialization
- Distributed execution

For example, a Python generator can process a large file efficiently on one machine, but it does not automatically provide the distributed processing capabilities of systems such as Spark.

> [!IMPORTANT]
> For interviews, remember this simple chain:
>
> ```text
> Iterable
>    ↓ iter()
> Iterator
>    ↓ next()
> Value
>    ↓
> Generator
>    ↓ yield
> Lazy processing
>    ↓
> Lower peak memory usage
> ```
>
> The most important practical takeaway is that **generators allow you to build pipelines that produce and consume data incrementally**.

---

## Navigation

⬅️ **Previous:** [Day 22 - File Handling](../Day_22_File_Handling/readme.md)

➡️ **Next:** [Day 24 - Decorators](../Day_24_Decorators/readme.md)
