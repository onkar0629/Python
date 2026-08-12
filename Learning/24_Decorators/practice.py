# 🐍 Day 24 - Decorators | Practice

# Solve each problem yourself before checking the README.

# ============================================================
# Practice 1 - Function as an Object
# ============================================================
# Create a function greet() and assign it to another variable.
# Call the function through the new variable.


# ============================================================
# Practice 2 - Function as an Argument
# ============================================================
# Create execute(function) that receives a function and calls it.


# ============================================================
# Practice 3 - Return a Function
# ============================================================
# Create outer() with an inner() function.
# Return inner from outer and call the returned function.


# ============================================================
# Practice 4 - Higher-Order Function
# ============================================================
# Create apply_operation(function, value) that returns
# function(value).


# ============================================================
# Practice 5 - Basic Decorator
# ============================================================
# Create a decorator that prints:
# Before
# After
# around the execution of a function.


# ============================================================
# Practice 6 - @ Syntax
# ============================================================
# Apply your decorator using @decorator instead of manually
# replacing the function.


# ============================================================
# Practice 7 - Decorator with Arguments
# ============================================================
# Decorate a function greet(name).
# Make sure the wrapper can receive the name argument.


# ============================================================
# Practice 8 - *args and **kwargs
# ============================================================
# Write a decorator that can wrap both:
#
# add(a, b)
#
# and:
#
# greet(name, city="Pune")
#
# without changing the decorator.


# ============================================================
# Practice 9 - Preserve Return Value
# ============================================================
# Decorate a function that returns a number.
# Make sure the decorated function still returns that number.


# ============================================================
# Practice 10 - functools.wraps
# ============================================================
# Create a decorator using @wraps.
# Print the decorated function's __name__ and __doc__.


# ============================================================
# Practice 11 - Logging Decorator
# ============================================================
# Create @log_execution that prints the function name before
# executing it.


# ============================================================
# Practice 12 - Timing Decorator
# ============================================================
# Create @measure_time using time.perf_counter().
# Print how long the decorated function takes to execute.


# ============================================================
# Practice 13 - Validation Decorator
# ============================================================
# Create @positive_only.
# The decorated function should raise ValueError when its
# numeric argument is zero or negative.


# ============================================================
# Practice 14 - Decorator with Configuration
# ============================================================
# Create:
#
# @repeat(3)
# def greet():
#     print("Hello")
#
# The function should execute three times.


# ============================================================
# Practice 15 - Multiple Decorators
# ============================================================
# Create two decorators and apply both to one function.
# Predict the execution order before running the code.


# ============================================================
# Practice 16 - Decorator Order
# ============================================================
# Explain why:
#
# @decorator_one
# @decorator_two
# def test():
#     pass
#
# is equivalent to:
#
# test = decorator_one(decorator_two(test))


# ============================================================
# Practice 17 - Closure
# ============================================================
# Create multiplier(factor) that returns a function which
# multiplies its argument by factor.


# ============================================================
# Practice 18 - Class Decorator
# ============================================================
# Create a class decorator that adds:
# category = "Data Engineering"
# to a class.


# ============================================================
# Practice 19 - @staticmethod
# ============================================================
# Create a class with a static method add(a, b).
# Call it without creating an object.


# ============================================================
# Practice 20 - @classmethod
# ============================================================
# Create a class-level counter using @classmethod.
# Track how many objects have been created.


# ============================================================
# Practice 21 - @property
# ============================================================
# Create a Customer class with a name attribute and a property
# normalized_name that returns the stripped and title-cased name.


# ============================================================
# Practice 22 - Retry Decorator
# ============================================================
# Create @retry(attempts=3).
# Retry only ConnectionError.
# Re-raise the exception after the final attempt.


# ============================================================
# Practice 23 - Data Engineering Scenario
# ============================================================
# Create @log_pipeline_stage that logs:
#
# START <function_name>
# END <function_name>
#
# Apply it to extract_data(), transform_data(), and load_data().


# ============================================================
# Practice 24 - Interview Output Prediction
# ============================================================
# Predict the output before running:
#
# def decorator(function):
#     def wrapper():
#         print("A")
#         function()
#         print("B")
#     return wrapper
#
# @decorator
# def test():
#     print("C")
#
# test()


# ============================================================
# Practice 25 - Interview Challenge
# ============================================================
# Build a reusable Data Engineering decorator system with:
#
# @log_execution
# @measure_time
# @retry(attempts=3)
#
# Apply it to a simulated load_data() function.
#
# Requirements:
# - Preserve function metadata with functools.wraps.
# - Support *args and **kwargs.
# - Retry only transient ConnectionError failures.
# - Do not silently swallow the final exception.
# - Return the original function's result.
# - Explain the decorator execution order.
