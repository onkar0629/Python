# 🐍 Day 02 - Python Tokens and Variables

Programming languages are built using a set of fundamental building blocks known as **tokens**. Every Python program you write is made up of different types of tokens such as keywords, identifiers, literals, operators, and variables.

In this lesson, you'll learn how Python understands your code, how variables store data, the rules for naming identifiers, and how arithmetic operations are performed.

---

## Table of Contents

- What are Tokens?
- Types of Tokens
- Literals
- Constants
- Operators
- Arithmetic Operators
- Keywords
- Identifiers
- Rules for Naming Identifiers
- Variables
- Assignment Operator
- Best Practices
- Common Mistakes
- Interview Questions
- Why It Matters
- Key Takeaways

---

# 1. What are Tokens?

A **token** is the smallest meaningful unit of a Python program.

Just as English sentences are made of words, Python programs are made of tokens.

Every Python statement contains one or more tokens.

For example:

```python
age = 22
```

This statement contains:

| Token | Description |
|--------|-------------|
| age | Identifier |
| = | Assignment Operator |
| 22 | Integer Literal |

> [!NOTE]
> Every Python program is constructed using tokens.

---

# 2. Types of Tokens

Python tokens are broadly classified into five categories:

1. Literals
2. Constants
3. Operators
4. Keywords
5. Identifiers

Let's understand each one in detail.

---

# 3. Literals

A **literal** is a fixed value written directly in the program.

Python supports several types of literals.

## Integer Literals

Whole numbers without a decimal point.

```python
age = 22
roll_number = 101
```

Examples:

- 10
- 250
- -15

---

## Floating-Point Literals

Numbers containing a decimal point.

```python
height = 5.8
price = 499.99
```

Examples:

- 4.5
- 10.75
- 100.00

---

## String Literals

A string is a sequence of characters enclosed within single or double quotes.

```python
name = "Onkar"

college = 'MIT'
```

Examples:

- "Python"
- "Data Engineering"
- 'Hello'

---

## Boolean Literals

Boolean literals represent logical values.

There are only two Boolean values in Python:

```python
True
False
```

These values are commonly used in conditions.

```python
age = 20

age >= 18
```

The above expression evaluates to:

```python
True
```

> [!TIP]
> Boolean values are widely used with `if` statements, loops, and comparison operations.

---

# 4. Constants

A constant is a value that is intended not to change during program execution.

Example:

```python
PI = 3.14159

MONTHS_IN_YEAR = 12
```

> [!IMPORTANT]
> Python does not have built-in constants. By convention, constant names are written in **UPPERCASE**.

---

# 5. Operators

Operators are symbols that perform operations on values or variables.

Example:

```python
10 + 5
```

Here,

- `+` is an operator.
- `10` and `5` are operands.

Python provides several categories of operators.

- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Membership Operators
- Identity Operators
- Bitwise Operators

In this lesson, we'll focus on Arithmetic Operators.

---

# 6. Arithmetic Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| + | Addition | 7 + 2 | 9 |
| - | Subtraction | 7 - 2 | 5 |
| * | Multiplication | 7 * 2 | 14 |
| / | Division | 7 / 2 | 3.5 |
| // | Floor Division | 7 // 2 | 3 |
| % | Modulus | 7 % 2 | 1 |
| ** | Exponent | 7 ** 2 | 49 |

Example:

```python
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 4)
```

---

# 7. Keywords

Keywords are reserved words that have predefined meanings in Python.

Examples include:

```python
if
else
for
while
class
import
return
True
False
None
```

Keywords cannot be used as variable names.

```python
if = 10
```

The above code generates an error.

---

# 8. Identifiers

Identifiers are user-defined names used to identify variables, functions, classes, and objects.

Examples:

```python
student_name

total_marks

calculate_salary()
```

An identifier should clearly describe its purpose.

---

# 9. Rules for Naming Identifiers

Python identifiers must follow these rules.

### Rule 1

Do not use spaces.

❌

```python
student name
```

✅

```python
student_name
```

---

### Rule 2

Only letters, digits, and underscores are allowed.

❌

```python
student@name
```

✅

```python
student_name
```

---

### Rule 3

Keywords cannot be used as identifiers.

❌

```python
class = 10
```

✅

```python
class_name = "Python"
```

---

### Rule 4

The first character must be a letter or underscore.

❌

```python
2marks
```

✅

```python
marks2

_marks
```

---

# 10. Variables

A variable is a named memory location used to store data.

Variables make it possible to reuse and modify values throughout a program.

Example:

```python
name = "Onkar"

age = 22

salary = 45000
```

Each variable stores a different value.

---

# 11. Assignment Operator

The assignment operator (`=`) assigns a value to a variable.

Syntax:

```python
variable_name = value
```

Examples:

```python
a = 10

b = a

c = a + b
```

Here,

- `a` stores 10
- `b` stores the value of `a`
- `c` stores the result of `a + b`

---

# Best Practices

- Use meaningful variable names.
- Follow the snake_case naming convention.
- Use UPPERCASE for constants.
- Keep identifiers descriptive.
- Avoid single-letter variable names unless appropriate.

---

# Common Mistakes

- Using keywords as variable names.
- Starting identifiers with numbers.
- Using spaces in variable names.
- Confusing variables with literals.
- Forgetting the difference between `/` and `//`.

> [!WARNING]
> A variable stores a value, while a literal **is** the value itself.

---

# Python Interview Questions -- Tokens & Operators

## 1. What is a token?

A **token** is the smallest meaningful unit in a Python program that the
interpreter recognizes.

**Example:**

``` python
age = 25
```

Tokens: - `age` → Identifier - `=` → Operator - `25` → Literal

------------------------------------------------------------------------

## 2. What are the five types of tokens?

  -------------------------------------------------------------------------
  Token Type                 Description                 Example
  -------------------------- --------------------------- ------------------
  Keywords                   Reserved words with         `if`, `for`,
                             predefined meanings         `while`, `True`

  Identifiers                Names given to variables,   `age`,
                             functions, classes, etc.    `student_name`

  Literals                   Fixed values                `100`, `"Hello"`,
                                                         `3.14`, `True`

  Operators                  Symbols that perform        `+`, `-`, `*`,
                             operations                  `/`, `%`

  Delimiters                 Symbols used to separate    `()`, `[]`, `{}`,
  (Separators/Punctuators)   code elements               `:`, `,`
  -------------------------------------------------------------------------

------------------------------------------------------------------------

## 3. What is the difference between a literal and a variable?

  -----------------------------------------------------------------------
  Literal                             Variable
  ----------------------------------- -----------------------------------
  A fixed value written directly in   A named location that stores a
  the code.                           value.

  Cannot change by itself.            Its value can change during program
                                      execution.

  Examples: `10`, `"Python"`, `True`  Examples: `x`, `name`, `price`
  -----------------------------------------------------------------------

**Example:**

``` python
age = 21
```

-   `21` → Literal
-   `age` → Variable

------------------------------------------------------------------------

## 4. What is an identifier?

An **identifier** is the name used to identify variables, functions,
classes, modules, and other objects in Python.

**Examples:**

``` python
name = "Onkar"
marks = 90

def calculate_sum():
    pass
```

Identifiers: - `name` - `marks` - `calculate_sum`

------------------------------------------------------------------------

## 5. What are the rules for naming identifiers?

1.  Must begin with a letter (`A-Z`, `a-z`) or underscore (`_`).
2.  Cannot begin with a digit.
3.  Can contain letters, digits, and underscores.
4.  Cannot contain spaces.
5.  Cannot contain special characters like `@`, `#`, `$`, `%`.
6.  Cannot be a Python keyword.
7.  Python identifiers are **case-sensitive**.

### Valid identifiers

``` python
student
student_name
_marks
age1
```

### Invalid identifiers

``` python
1student      # Starts with digit
student-name  # Hyphen not allowed
class         # Keyword
student name  # Space not allowed
```

------------------------------------------------------------------------

## 6. What is the assignment operator?

The **assignment operator (`=`)** is used to assign a value to a
variable.

**Syntax:**

``` python
variable = value
```

**Example:**

``` python
x = 10
name = "Onkar"
```

------------------------------------------------------------------------

## 7. What is the difference between `/` and `//`?

  -----------------------------------------------------------------------
  `/`                              `//`
  -------------------------------- --------------------------------------
  Performs floating-point          Performs floor (integer) division.
  division.                        

  Returns a float.                 Returns the quotient rounded down.
  -----------------------------------------------------------------------

**Example:**

``` python
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3
print(9 // 2)   # 4
```

------------------------------------------------------------------------

## 8. What is the difference between `%` and `//`?

  `%` (Modulo)             `//` (Floor Division)
  ------------------------ --------------------------------------------
  Returns the remainder.   Returns the quotient after floor division.

**Example:**

``` python
print(10 % 3)   # 1
print(10 // 3)  # 3
```

Explanation:

    10 = (3 × 3) + 1

-   `//` → Quotient = **3**
-   `%` → Remainder = **1**

------------------------------------------------------------------------

# Quick Interview Revision

  -----------------------------------------------------------------------
  Question                      Short Answer
  ----------------------------- -----------------------------------------
  What is a token?              The smallest meaningful unit of a Python
                                program.

  Five types of tokens?         Keywords, Identifiers, Literals,
                                Operators, Delimiters.

  Literal vs Variable           Literal is a fixed value; a variable
                                stores values.

  Identifier                    Name given to variables, functions,
                                classes, etc.

  Identifier rules              Start with letter/\_; no keywords; no
                                spaces; case-sensitive.

  Assignment operator           `=` assigns a value to a variable.

  `/` vs `//`                   `/` returns float division; `//` returns
                                floor division.

  `%` vs `//`                   `%` returns remainder; `//` returns
                                quotient (floor).
  -----------------------------------------------------------------------

---

## Navigation

🏠 **Home:** [Python Roadmap](https://github.com/onkar0629/my-data-engineering-journey/tree/main/Python/Daily-Learning)

⬅️ **Previous:** [Day 01 - Introduction to Python](https://github.com/onkar0629/my-data-engineering-journey/blob/main/Python/Daily-Learning/Day_01_Introduction_to_Python/README.md)

➡️ **Next:** [Day 03 - Input, Output and Type Conversion](https://github.com/onkar0629/my-data-engineering-journey/blob/main/Python/Daily-Learning/Day_03_Input_Output_and_Type_Conversion/README.md)