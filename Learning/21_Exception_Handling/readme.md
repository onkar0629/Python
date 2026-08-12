# 🐍 Day 21 - Exception Handling

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Level](https://img.shields.io/badge/Level-Intermediate-success)

---

## Overview

Programs do not always receive valid input or interact with systems that always behave correctly.

A file may not exist. A database connection may fail. A value may have the wrong type. An API may return unexpected data.

Python provides **exception handling** so that programs can detect, handle, and report runtime problems in a controlled way.

The main tools are:

- `try`
- `except`
- `else`
- `finally`
- `raise`
- Custom exceptions
- Exception hierarchy
- Exception chaining
- Logging exceptions

A simple example:

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
```

Instead of allowing the program to terminate unexpectedly, we explicitly handle the known failure.

> [!IMPORTANT]
> Exception handling should make a program **more reliable and observable**. It should not be used to hide bugs or silently ignore failures.

---

## Table of Contents

- [1. What Is an Exception?](#1-what-is-an-exception)
- [2. Syntax Errors vs Exceptions](#2-syntax-errors-vs-exceptions)
- [3. Common Built-in Exceptions](#3-common-built-in-exceptions)
- [4. try and except](#4-try-and-except)
- [5. Handling Specific Exceptions](#5-handling-specific-exceptions)
- [6. Multiple except Blocks](#6-multiple-except-blocks)
- [7. Exception Object](#7-exception-object)
- [8. else](#8-else)
- [9. finally](#9-finally)
- [10. Complete try/except/else/finally Flow](#10-complete-tryexceptelsefinally-flow)
- [11. raise](#11-raise)
- [12. Custom Exceptions](#12-custom-exceptions)
- [13. Exception Hierarchy](#13-exception-hierarchy)
- [14. Catching Multiple Exceptions](#14-catching-multiple-exceptions)
- [15. Bare except](#15-bare-except)
- [16. Exception Chaining](#16-exception-chaining)
- [17. Assertions](#17-assertions)
- [18. Logging Exceptions](#18-logging-exceptions)
- [19. File Handling Example](#19-file-handling-example)
- [20. Data Pipeline Error Handling](#20-data-pipeline-error-handling)
- [21. Common Mistakes](#21-common-mistakes)
- [22. Interview Follow-up Questions](#22-interview-follow-up-questions)
- [23. Data Engineering Perspective](#23-data-engineering-perspective)

---

# 1. What Is an Exception?

An **exception** is an event raised during program execution that interrupts the normal flow of instructions.

Example:

```python
number = 10
result = number / 0
```

Python raises:

```text
ZeroDivisionError
```

The program cannot continue normally from that operation unless the exception is handled or allowed to propagate.

Another example:

```python
number = int("abc")
```

This raises:

```text
ValueError
```

The value is a string, but it cannot be converted to an integer.

---

# 2. Syntax Errors vs Exceptions

These are different problems.

## Syntax Error

A syntax error means Python cannot parse the code correctly.

Example:

```python
if True
    print("Hello")
```

The colon is missing.

Python cannot execute this program normally.

## Exception

The code is syntactically valid, but something goes wrong during execution.

```python
number = 10
print(number / 0)
```

The syntax is valid, but the operation raises `ZeroDivisionError`.

Think of it as:

```text
Syntax Error
→ Python cannot understand the program structure.

Exception
→ Python understands the program, but execution encounters a problem.
```

> [!IMPORTANT]
> `try/except` is primarily for runtime exceptions. It does not fix invalid Python syntax in the surrounding program.

---

# 3. Common Built-in Exceptions

Python provides many built-in exception types.

### `ValueError`

The type may be appropriate, but the value is invalid for the operation.

```python
int("abc")
```

### `TypeError`

An operation is applied to an inappropriate type.

```python
"10" + 5
```

### `ZeroDivisionError`

Division by zero.

```python
10 / 0
```

### `IndexError`

A sequence index does not exist.

```python
numbers = [1, 2, 3]
numbers[10]
```

### `KeyError`

A dictionary key does not exist.

```python
student = {"name": "Onkar"}
student["age"]
```

### `FileNotFoundError`

A requested file does not exist.

```python
open("missing.txt")
```

### `AttributeError`

An object does not have the requested attribute.

```python
number = 10
number.upper()
```

Understanding the exception type helps determine the appropriate recovery strategy.

---

# 4. `try` and `except`

The basic structure is:

```python
try:
    # Code that may fail
except SomeException:
    # Code that handles the failure
```

Example:

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
```

Execution flow:

```text
try block
   ↓
exception occurs
   ↓
matching except block
   ↓
handler executes
```

If no exception occurs, the `except` block is skipped.

---

# 5. Handling Specific Exceptions

Prefer catching the exception you actually expect.

Good:

```python
try:
    number = int(user_input)
except ValueError:
    print("Please enter a valid number")
```

This tells the reader exactly what failure is being handled.

Avoid using a broad exception when a specific one is known.

Why?

Because broad handlers can hide programming bugs.

---

# 6. Multiple `except` Blocks

A single `try` block can have multiple exception handlers.

```python
try:
    number = int(value)
    result = 100 / number
except ValueError:
    print("Value is not a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Python checks the handlers and executes the first matching one.

This lets us handle different failure types differently.

---

# 7. Exception Object

We can capture the exception object using `as`.

```python
try:
    number = int("abc")
except ValueError as error:
    print(error)
```

`error` contains the exception instance.

This is useful for logging or displaying diagnostic information.

For example:

```python
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print("Error:", error)
```

Output may be:

```text
Error: division by zero
```

> [!TIP]
> In production systems, exception details are usually sent to logs rather than printed directly to users.

---

# 8. `else`

The `else` block runs only when the `try` block completes successfully.

Syntax:

```python
try:
    # risky operation
except SomeException:
    # failure handling
else:
    # successful execution
```

Example:

```python
try:
    number = int("100")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful")
```

Why use `else`?

It separates **successful logic** from the code that may raise the expected exception.

---

# 9. `finally`

The `finally` block is used for cleanup code that should run whether an exception occurs or not.

```python
try:
    print("Working")
except Exception:
    print("Error")
finally:
    print("Cleanup")
```

The cleanup section can be useful for:

- Closing resources
- Releasing locks
- Cleaning temporary state
- Closing connections when manually managed

For many files, Python's `with` statement is preferable because it manages resource cleanup automatically.

---

# 10. Complete `try/except/else/finally` Flow

All four blocks can appear together:

```python
try:
    number = int("100")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion succeeded")
finally:
    print("Operation finished")
```

Execution when conversion succeeds:

```text
try
 ↓
else
 ↓
finally
```

Execution when conversion fails:

```text
try
 ↓
except
 ↓
finally
```

The `finally` block is intended for cleanup that should happen regardless of success or failure.

---

# 11. `raise`

We can intentionally raise an exception using `raise`.

Example:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount
```

If:

```python
withdraw(100, 200)
```

the function raises a `ValueError`.

`raise` is useful when input violates a business rule.

For example, a Data Engineering validation function could raise an exception when a required field is missing.

---

# 12. Custom Exceptions

For domain-specific errors, we can define our own exception classes.

Example:

```python
class InvalidRecordError(Exception):
    pass
```

Then:

```python
raise InvalidRecordError("Customer ID is missing")
```

Handle it:

```python
try:
    raise InvalidRecordError("Customer ID is missing")
except InvalidRecordError as error:
    print(error)
```

Custom exceptions make application-specific failures easier to identify and handle.

A good custom exception usually inherits from `Exception` or an appropriate subclass.

---

# 13. Exception Hierarchy

Python exceptions form a hierarchy.

A simplified view is:

```text
BaseException
├── KeyboardInterrupt
├── SystemExit
└── Exception
    ├── ValueError
    ├── TypeError
    ├── OSError
    │   └── FileNotFoundError
    └── RuntimeError
```

Because `FileNotFoundError` inherits from `OSError`, a handler for `OSError` can also catch it.

Example:

```python
try:
    open("missing.txt")
except OSError:
    print("Operating system error")
```

However, catching the most specific exception that matches the intended recovery is generally clearer.

> [!IMPORTANT]
> `Exception` is a broad application-level base class. `BaseException` also includes control-flow exceptions such as `KeyboardInterrupt` and `SystemExit`, so broad `BaseException` handlers are usually inappropriate.

---

# 14. Catching Multiple Exceptions

We can handle multiple exception types with a tuple.

```python
try:
    value = int(user_input)
except (ValueError, TypeError):
    print("Invalid input")
```

This is useful when the recovery behavior is identical for multiple exception types.

If different errors require different actions, separate `except` blocks are usually clearer.

---

# 15. Bare `except`

This is possible:

```python
try:
    risky_operation()
except:
    print("Something went wrong")
```

But it is usually a bad practice.

A bare `except` can catch exceptions you may not intend to intercept, including control-flow exceptions derived directly from `BaseException`.

Prefer:

```python
except Exception as error:
    logger.exception("Unexpected application error")
```

when a broad application-level fallback is genuinely required.

Even then, do not use it to silently continue without logging or a recovery strategy.

---

# 16. Exception Chaining

Sometimes one exception occurs while handling another.

Python allows us to explicitly preserve the original cause using `from`.

Example:

```python
try:
    number = int("abc")
except ValueError as error:
    raise RuntimeError("Failed to parse customer ID") from error
```

The resulting exception communicates both:

```text
High-level failure
        ↓
Original cause
```

This is useful when lower-level implementation details need to be converted into a domain-specific error while preserving the original cause for debugging.

---

# 17. Assertions

An assertion checks a condition that the programmer expects to be true.

```python
age = 22

assert age >= 18
```

If the condition is false:

```python
assert age >= 18, "Age must be at least 18"
```

Python raises `AssertionError`.

Assertions are useful for internal invariants and debugging.

> [!WARNING]
> Do not use assertions as the primary mechanism for validating untrusted external input. Assertions can be disabled with Python optimization settings. Use explicit validation and `raise` for business or input validation.

---

# 18. Logging Exceptions

In production applications, logging is generally more useful than `print()`.

```python
import logging

logger = logging.getLogger(__name__)

try:
    number = 10 / 0
except ZeroDivisionError:
    logger.exception("Division failed")
```

`logger.exception()` is especially useful inside an exception handler because it records the exception traceback.

Conceptually:

```text
Exception
   ↓
Logger
   ↓
Timestamp + message + traceback
   ↓
Monitoring / log system
```

For Data Engineering pipelines, this is critical for diagnosing failed jobs.

---

# 19. File Handling Example

Suppose we need to read a file.

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File does not exist")
```

Notice two concepts:

```text
try/except → handles expected failure
with       → manages the file resource
```

The `with` statement closes the file automatically when the block exits.

We should not manually use `finally` just to close a file when a context manager already handles it.

---

# 20. Data Pipeline Error Handling

Consider a simple pipeline:

```text
Extract
  ↓
Transform
  ↓
Validate
  ↓
Load
```

Each stage can fail for different reasons.

For example:

```python
def transform(record):
    try:
        amount = float(record["amount"])
        return amount * 1.18
    except KeyError as error:
        raise ValueError("Required field is missing") from error
    except (TypeError, ValueError) as error:
        raise ValueError("Invalid amount") from error
```

This converts low-level exceptions into an error meaningful to the transformation layer.

A production pipeline may then log the failure and decide whether to:

- Reject the record
- Send it to a dead-letter/quarantine location
- Retry the operation
- Fail the task
- Continue processing other records

The correct strategy depends on whether the error is **recoverable, transient, or data-quality related**.

---

# 21. Common Mistakes

## Mistake 1: Catching Everything

Avoid:

```python
try:
    process_data()
except:
    pass
```

This can hide serious problems.

---

## Mistake 2: Empty Exception Handler

Avoid:

```python
except Exception:
    pass
```

If an exception is intentionally ignored, there should be a strong reason and usually some form of observability.

---

## Mistake 3: Catching the Wrong Exception

If the operation can raise `ValueError`, do not catch an unrelated exception and assume the problem is handled.

Know what operations can fail and which exception types they raise.

---

## Mistake 4: Using Exceptions for Normal Control Flow

Exceptions should represent exceptional conditions, not ordinary branching that could be handled more clearly with normal conditions.

---

## Mistake 5: Losing the Original Error

When converting an exception, preserve the original cause when useful:

```python
raise RuntimeError("Transformation failed") from error
```

This keeps the traceback chain.

---

## Mistake 6: Using `print()` Instead of Logging in Production

A production pipeline should generally use structured logging and monitoring rather than relying on console output.

---

# 22. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is the difference between `try`, `except`, `else`, and `finally`?

<details>
<summary><strong>Answer</strong></summary>

`try` contains code that may raise an exception.

`except` handles a matching exception.

`else` executes when the `try` block completes successfully.

`finally` is intended for cleanup that should happen regardless of whether an exception occurred.

Example:

```python
try:
    result = int("100")
except ValueError:
    print("Invalid value")
else:
    print("Success")
finally:
    print("Finished")
```

</details>

---

### Q2. Why should we catch specific exceptions instead of using `except Exception` everywhere?

<details>
<summary><strong>Answer</strong></summary>

Specific exceptions make the recovery behavior precise.

For example:

```python
try:
    number = int(value)
except ValueError:
    print("Invalid number")
```

This clearly communicates that the code expects a conversion problem.

A broad handler such as:

```python
except Exception:
    ...
```

can catch unexpected programming errors and make debugging harder if used indiscriminately.

A broad handler can still be appropriate at a well-defined application boundary for logging and controlled failure handling.

</details>

---

### Q3. What is the purpose of the `finally` block?

<details>
<summary><strong>Answer</strong></summary>

`finally` is used for cleanup that should happen whether the operation succeeds or fails.

```python
try:
    resource = acquire_resource()
except Exception:
    handle_error()
finally:
    cleanup()
```

For files and many other resources, context managers such as `with open(...)` are preferable because they manage cleanup automatically.

</details>

---

### Q4. What is the difference between `raise` and `assert`?

<details>
<summary><strong>Answer</strong></summary>

`raise` explicitly raises an exception as part of program logic.

```python
if amount < 0:
    raise ValueError("Amount cannot be negative")
```

`assert` checks a condition that should be true for an internal assumption or invariant.

```python
assert amount >= 0
```

Assertions can be disabled with optimization, so they should not be used as the primary validation mechanism for external or business-critical input.

</details>

---

### Q5. What is exception chaining and why is `raise ... from ...` useful?

<details>
<summary><strong>Answer</strong></summary>

Exception chaining preserves the original exception when a lower-level failure is converted into a higher-level error.

```python
try:
    value = int("abc")
except ValueError as error:
    raise RuntimeError("Failed to parse record") from error
```

The caller sees the high-level `RuntimeError`, while the original `ValueError` remains available as the cause.

This is useful for layered applications and Data Engineering pipelines because each layer can expose meaningful domain-level errors without losing debugging information.

</details>

---

### Q6. What happens if an exception is not handled?

<details>
<summary><strong>Answer</strong></summary>

The exception propagates up the call stack looking for a matching exception handler.

If no handler catches it, Python terminates the current execution and prints a traceback.

Conceptually:

```text
function C
   ↑
function B
   ↑
function A
   ↑
main
```

An exception raised in `C` can propagate through `B` and `A` until a matching handler is found.

If none exists, the exception reaches the top-level execution context.

</details>

---

### Q7. How would you handle errors in a Data Engineering pipeline?

<details>
<summary><strong>Answer</strong></summary>

First classify the error.

Examples:

```text
Transient infrastructure error
→ retry may be appropriate

Invalid source record
→ quarantine/reject the record

Missing required configuration
→ fail the job clearly

Programming bug
→ log traceback and fix the code
```

I would avoid blindly catching all exceptions and continuing because that can produce incomplete or incorrect data.

A production pipeline should combine exception handling with:

- Logging
- Monitoring
- Retry policies
- Data-quality checks
- Dead-letter/quarantine handling where appropriate
- Clear job failure semantics

</details>

---

### Q8. Why is `except: pass` dangerous?

<details>
<summary><strong>Answer</strong></summary>

```python
try:
    process_data()
except:
    pass
```

This catches the failure and then silently ignores it.

The pipeline may appear successful even though important work failed.

That can be especially dangerous in Data Engineering because a job might produce incomplete or corrupted downstream data without an obvious failure signal.

A better approach is to catch expected exceptions, log useful context, and apply an explicit recovery strategy.

</details>

---

# 23. Data Engineering Perspective

Exception handling is especially important in Data Engineering because pipelines interact with external systems.

Typical failure points include:

```text
Source API
   ↓
Network failure
   ↓
Raw ingestion
   ↓
Malformed record
   ↓
Transformation
   ↓
Data type error
   ↓
Warehouse
   ↓
Connection / constraint error
```

A robust pipeline should distinguish between failure categories.

### Transient Errors

Examples:

- Temporary network failure
- Service unavailable
- Temporary database connection issue
- Rate limiting

These may be suitable for retry with backoff.

### Permanent Data Errors

Examples:

- Required column missing
- Invalid date format
- Invalid numeric value
- Broken business rule

These may need record-level rejection or quarantine rather than repeatedly retrying the same bad record.

### Programming Errors

Examples:

- Incorrect variable name
- Wrong function call
- Unexpected `None`
- Logic bug

These generally should not be silently swallowed. They should fail clearly and be fixed in the application.

### Production Pattern

A simplified pipeline can follow:

```text
Extract
  ↓
Try operation
  ↓
Success ──────────────→ Continue
  ↓
Failure
  ↓
Classify exception
  ├── transient → retry
  ├── data error → quarantine
  └── programming/config error → fail + alert
```

This is much stronger than:

```python
try:
    run_pipeline()
except:
    pass
```

> [!IMPORTANT]
> In Data Engineering, the goal of exception handling is not simply to keep the program running. The goal is to ensure that **failures are detected, classified, observable, and handled without silently compromising data correctness**.

---

## Navigation

⬅️ **Previous:** [Day 20 - Modules and Packages](../Day_20_Modules_and_Packages/readme.md)

➡️ **Next:** [Day 22 - File Handling](../Day_22_File_Handling/readme.md)
