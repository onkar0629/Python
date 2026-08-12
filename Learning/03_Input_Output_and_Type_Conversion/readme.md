# 🐍 Day 03 - Input, Output and Type Conversion

Writing a program is more than just storing values in variables. A program should be able to **display information**, **accept user input**, and **process data** to produce meaningful results.

In this lesson, you'll learn how to display output using the `print()` function, accept input from the user using the `input()` function, convert data from one type to another, and build simple real-world programs.

---

## Table of Contents

- Variable Reassignment
- Multiple Variable Assignment
- The `print()` Function
- String Concatenation
- Formatted Output (f-Strings)
- The `input()` Function
- Type Conversion
- Real-World Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Why It Matters
- Key Takeaways

---

# 1. Variable Reassignment

A variable can store **only one value at a time**.

If a new value is assigned to the same variable, the previous value is replaced.

### Example

```python
age = 22

print(age)

age = 25

print(age)
```

**Output**

```text
22
25
```

---

# 2. Multiple Variable Assignment

Python allows assigning values to multiple variables in a single statement.

### Syntax

```python
variable1, variable2 = value1, value2
```

### Example

```python
name, age = "Onkar", 22

print(name)
print(age)
```

**Output**

```text
Onkar
22
```

> [!IMPORTANT]
> The number of variables and values must be the same.

---

# 3. The `print()` Function

The `print()` function is used to display information on the screen.

### Printing Text

```python
print("Hello, World!")
```

**Output**

```text
Hello, World!
```

### Printing Variables

```python
name = "Onkar"

print(name)
```

**Output**

```text
Onkar
```

### Printing Multiple Values

```python
name = "Onkar"
age = 22

print(name, age)
```

**Output**

```text
Onkar 22
```

---

# 4. String Concatenation

Concatenation means joining two or more strings together.

### Example

```python
first_name = "Onkar"

last_name = "Jadhav"

full_name = first_name + " " + last_name

print(full_name)
```

**Output**

```text
Onkar Jadhav
```

---

# 5. Formatted Output (f-Strings)

Python provides **f-strings** to create readable output.

### Example

```python
name = "Onkar"

print(f"Welcome, {name}")
```

**Output**

```text
Welcome, Onkar
```

Another example:

```python
marks = 95

print(f"Your marks are {marks}")
```

---

# 6. The `input()` Function

The `input()` function is used to accept input from the user.

### Syntax

```python
variable = input("Enter a value: ")
```

### Example

```python
name = input("Enter your name: ")

print("Hello,", name)
```

**Sample Output**

```text
Enter your name: Onkar
Hello, Onkar
```

> [!NOTE]
> The `input()` function always returns data as a **string**.

---

# 7. Type Conversion

Sometimes user input must be converted into another data type before performing calculations.

## Integer Conversion

```python
age = int(input("Enter your age: "))

print(age)
```

---

## Floating-Point Conversion

```python
salary = float(input("Enter your salary: "))

print(salary)
```

---

## Why Type Conversion?

Without conversion:

```python
num1 = input("Enter first number: ")

num2 = input("Enter second number: ")

print(num1 + num2)
```

If the user enters:

```text
10
20
```

Output:

```text
1020
```

With conversion:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

Output:

```text
30
```

---

# 8. Real-World Programs

## Program 1 – Calculate Monthly Salary

```python
annual_salary = float(input("Enter annual salary: "))

monthly_salary = annual_salary / 12

print(f"Monthly Salary: {monthly_salary}")
```

---

## Program 2 – Calculate Pizza Bill

```python
pizza_price = 300

quantity = int(input("Enter quantity: "))

bill_amount = pizza_price * quantity

print(f"Bill Amount: {bill_amount}")
```

---

## Program 3 – Student Marks

```python
subject1 = 95
subject2 = 90
subject3 = 94

total = subject1 + subject2 + subject3

average = total / 3

print("Total:", total)

print("Average:", average)
```

---

# Best Practices

- Use meaningful variable names.
- Use f-strings for formatted output.
- Convert user input before calculations.
- Keep prompts clear and descriptive.
- Follow the snake_case naming convention.

---

# Common Mistakes

- Forgetting that `input()` returns a string.
- Performing arithmetic without type conversion.
- Mismatch between variables and assigned values.
- Using unclear variable names.
- Forgetting spaces while concatenating strings.

> [!WARNING]
> Never assume that values returned by `input()` are integers or floats. Convert them explicitly using `int()` or `float()` whenever needed.

---

# Interview Questions

### What is the purpose of the `print()` function?

### What is the purpose of the `input()` function?

### Why does `input()` always return a string?

### What is type conversion?

### What is the difference between `int()` and `float()`?

### What is string concatenation?

### What are f-strings?

### How do you assign values to multiple variables?

---
---

## Navigation

🏠 **Home:** [Python Daily Learning Journey](https://github.com/onkar0629/my-data-engineering-journey/tree/main/Python/Daily-Learning)

⬅️ **Previous:** [Day 02 - Python Tokens and Variables](https://github.com/onkar0629/my-data-engineering-journey/blob/main/Python/Daily-Learning/Day_02_Python_Tokens_and_Variables/readme.md)

➡️ **Next:** [Day 04 - Conditional Statements](https://github.com/onkar0629/my-data-engineering-journey/blob/main/Python/Daily-Learning/Day_04_Conditional_Statements/README.md)
