# 🐍 Day 19 - Advanced Functions | Practice

# Solve each problem yourself before checking the README.

# ============================================================
# Practice 1 - Positional Arguments
# ============================================================
# Create a function called introduce(name, age) and call it
# using positional arguments.


# ============================================================
# Practice 2 - Keyword Arguments
# ============================================================
# Call the same function using keyword arguments in reverse order.


# ============================================================
# Practice 3 - Default Arguments
# ============================================================
# Create a function called greet(name, message="Hello").
# Call it once using the default and once with a custom message.


# ============================================================
# Practice 4 - *args
# ============================================================
# Create a function that accepts any number of numbers and
# returns their total.


# ============================================================
# Practice 5 - **kwargs
# ============================================================
# Create a function that accepts any number of keyword arguments
# and prints every key and value.


# ============================================================
# Practice 6 - *args and **kwargs
# ============================================================
# Create a function that receives both positional and keyword
# arguments and prints them separately.


# ============================================================
# Practice 7 - Positional Unpacking
# ============================================================
# Given the list below, call add(a, b, c) using * unpacking.

numbers = [10, 20, 30]


def add(a, b, c):
    return a + b + c


# ============================================================
# Practice 8 - Keyword Unpacking
# ============================================================
# Call connect(host, port) using ** unpacking.

config = {
    "host": "localhost",
    "port": 3306
}


def connect(host, port):
    print(host, port)


# ============================================================
# Practice 9 - Scope
# ============================================================
# Create a local variable inside a function and explain why
# it cannot normally be accessed outside that function.


# ============================================================
# Practice 10 - global
# ============================================================
# Create a global counter and a function that increments it
# using the global keyword.


# ============================================================
# Practice 11 - nonlocal
# ============================================================
# Create a counter using an outer function and inner function.
# Use nonlocal so repeated calls remember the count.


# ============================================================
# Practice 12 - Function as an Object
# ============================================================
# Create a function and assign it to another variable.
# Call the function using the new variable.


# ============================================================
# Practice 13 - Functions in a List
# ============================================================
# Create add() and multiply() functions.
# Store both functions in a list and call them from the list.


# ============================================================
# Practice 14 - Function as an Argument
# ============================================================
# Create apply_operation(a, b, operation).
# Pass add() and multiply() into it.


# ============================================================
# Practice 15 - Return a Function
# ============================================================
# Create create_multiplier(factor) that returns an inner
# function capable of multiplying a number by factor.


# ============================================================
# Practice 16 - Lambda
# ============================================================
# Create a lambda that returns the square of a number.


# ============================================================
# Practice 17 - Lambda with sorted()
# ============================================================
# Sort the following records by score using a lambda.

students = [
    {"name": "Onkar", "score": 85},
    {"name": "Rahul", "score": 92},
    {"name": "Amit", "score": 78}
]


# ============================================================
# Practice 18 - map()
# ============================================================
# Use map() and a lambda to create squares of these numbers.

numbers = [1, 2, 3, 4, 5]


# ============================================================
# Practice 19 - filter()
# ============================================================
# Use filter() and a lambda to keep only even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# ============================================================
# Practice 20 - Closure
# ============================================================
# Create a function that returns a closure remembering a prefix.
# Example:
# add_prefix = create_prefix("DE")
# add_prefix("Python") → "DE Python"


# ============================================================
# Practice 21 - Recursion
# ============================================================
# Write a recursive factorial function.
# factorial(5) should return 120.


# ============================================================
# Practice 22 - Recursive Sum
# ============================================================
# Write a recursive function that calculates the sum of numbers
# from 1 to n.
# Example: recursive_sum(5) → 15


# ============================================================
# Practice 23 - Basic Decorator
# ============================================================
# Create a decorator that prints:
# "Function started"
# before the function runs and
# "Function finished"
# after it runs.


# ============================================================
# Practice 24 - Decorator with Arguments
# ============================================================
# Modify the decorator so the wrapper accepts *args and **kwargs.
# Make sure the original function's return value is preserved.


# ============================================================
# Practice 25 - Data Engineering Scenario
# ============================================================
# Create a generic transform_records(records, transform_function)
# function.
#
# Given records containing customer_id and name, create separate
# transformation functions to:
# 1. Extract customer IDs.
# 2. Extract names.
#
# Pass each function into transform_records().

records = [
    {"customer_id": 101, "name": "Onkar"},
    {"customer_id": 102, "name": "Rahul"},
    {"customer_id": 103, "name": "Amit"}
]


# ============================================================
# Practice 26 - Data Engineering Scenario
# ============================================================
# Create load_data(data, **config).
#
# The function should read:
# batch_size → default 1000
# target     → default "sales"
#
# Call it with custom values.


# ============================================================
# Practice 27 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

x = 10


def test():
    x = 20
    print(x)


test()
print(x)


# ============================================================
# Practice 28 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))

print(result)


# ============================================================
# Practice 29 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

x = 10


def outer():
    x = 20

    def inner():
        print(x)

    inner()


outer()


# ============================================================
# Practice 30 - Interview Challenge
# ============================================================
# Explain the difference between these two calls:
#
# apply_operation(10, 20, add)
# apply_operation(10, 20, add())
#
# Write a small example that demonstrates the difference.
