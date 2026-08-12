"""
==========================================================
Day 12 : Recursion
Topic  : Examples

Description:
This file contains runnable examples demonstrating the
concepts covered in Day 12.

Topics Covered:
1. Basic Recursion
2. Base Case
3. Recursive Case
4. Countdown Using Recursion
5. Counting Up Using Recursion
6. Factorial
7. Sum of Natural Numbers
8. Power Calculation
9. Recursion vs Loop
10. Nested Data Processing
==========================================================
"""

# ==========================================================
# 1. Basic Recursion
# ==========================================================

print("========== Basic Recursion ==========\n")


def greet(number):
    if number == 0:
        return

    print("Hello Python")
    greet(number - 1)


greet(3)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. Base Case
# ==========================================================

print("========== Base Case ==========\n")


def countdown(number):
    if number == 0:
        print("Base Case Reached")
        return

    print(number)
    countdown(number - 1)


countdown(3)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 3. Countdown Using Recursion
# ==========================================================

print("========== Countdown ==========\n")


def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(5)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 4. Counting Up Using Recursion
# ==========================================================

print("========== Counting Up ==========\n")


def count_up(number):
    if number == 0:
        return

    count_up(number - 1)
    print(number)


count_up(5)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 5. Factorial Using Recursion
# ==========================================================

print("========== Factorial ==========\n")


def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


result = factorial(5)

print("Factorial of 5:", result)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 6. Sum of Natural Numbers
# ==========================================================

print("========== Sum of Natural Numbers ==========\n")


def calculate_sum(number):
    if number == 0:
        return 0

    return number + calculate_sum(number - 1)


result = calculate_sum(5)

print("Sum:", result)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 7. Power Calculation
# ==========================================================

print("========== Power Calculation ==========\n")


def calculate_power(base, exponent):
    if exponent == 0:
        return 1

    return base * calculate_power(base, exponent - 1)


result = calculate_power(2, 5)

print("2 raised to power 5:", result)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 8. Multiplication Using Recursion
# ==========================================================

print("========== Multiplication ==========\n")


def multiply(number, times):
    if times == 0:
        return 0

    return number + multiply(number, times - 1)


result = multiply(5, 4)

print("5 x 4 =", result)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 9. Sum of List Elements Using Recursion
# ==========================================================

print("========== Sum of List ==========\n")


def list_sum(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + list_sum(numbers[1:])


numbers = [10, 20, 30, 40]

result = list_sum(numbers)

print("Numbers:", numbers)
print("Total:", result)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 10. Find Maximum Using Recursion
# ==========================================================

print("========== Find Maximum ==========\n")


def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]

    maximum = find_max(numbers[1:])

    if numbers[0] > maximum:
        return numbers[0]

    return maximum


numbers = [25, 80, 15, 95, 40]

print("Maximum:", find_max(numbers))

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 11. Recursion vs Loop
# ==========================================================

print("========== Recursion vs Loop ==========\n")

print("Using Loop:")

for number in range(5, 0, -1):
    print(number)


print("\nUsing Recursion:")


def recursive_countdown(number):
    if number == 0:
        return

    print(number)
    recursive_countdown(number - 1)


recursive_countdown(5)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 12. Recursive Call Before print()
# ==========================================================

print("========== Recursive Call Before print() ==========\n")


def display_numbers(number):
    if number == 0:
        return

    display_numbers(number - 1)
    print(number)


display_numbers(5)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 13. Recursive Call After print()
# ==========================================================

print("========== Recursive Call After print() ==========\n")


def display_reverse(number):
    if number == 0:
        return

    print(number)
    display_reverse(number - 1)


display_reverse(5)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 14. Data Engineering Example - Nested Dictionary
# ==========================================================

print("========== Nested Dictionary Processing ==========\n")


def display_nested_data(data):
    for key, value in data.items():

        if isinstance(value, dict):
            display_nested_data(value)

        else:
            print(f"{key}: {value}")


customer = {
    "customer_id": 1001,
    "name": "Rahul",
    "address": {
        "city": "Pune",
        "state": "Maharashtra",
        "country": "India"
    }
}

display_nested_data(customer)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 15. Data Engineering Example - Nested JSON-like Data
# ==========================================================

print("========== Nested Data Processing ==========\n")


def process_data(data):
    for key, value in data.items():

        if isinstance(value, dict):
            print(f"Entering: {key}")
            process_data(value)

        else:
            print(f"{key} -> {value}")


pipeline_data = {
    "pipeline": {
        "source": {
            "type": "CSV",
            "file": "customers.csv"
        },
        "destination": {
            "type": "Database",
            "table": "customers"
        }
    }
}

process_data(pipeline_data)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 16. Recursion Limit
# ==========================================================

print("========== Recursion Limit ==========\n")

import sys

print("Current Recursion Limit:", sys.getrecursionlimit())

# The following code is intentionally NOT executed because
# it would eventually raise RecursionError.

"""
def infinite_recursion():
    infinite_recursion()


infinite_recursion()
"""

print("\nInfinite recursion example skipped.")

print("\n" + "=" * 50)

print("\nEnd of Day 12 Examples")