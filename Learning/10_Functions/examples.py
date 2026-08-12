"""
==========================================================
Day 10 : Functions
Topic  : Examples

Description:
This file contains runnable examples demonstrating the
concepts covered in Day 10.

Topics Covered:
1. Basic Functions
2. Calling Functions
3. Functions with Parameters
4. Functions with Multiple Parameters
5. return Statement
6. print() vs return
7. Calling Functions Multiple Times
8. Practical Examples
9. Data Engineering Examples
==========================================================
"""

# ==========================================================
# 1. Basic Function
# ==========================================================

print("========== Basic Function ==========\n")


def greet():
    print("Hello, Python!")


greet()

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. Calling a Function Multiple Times
# ==========================================================

print("========== Calling Function Multiple Times ==========\n")


def welcome():
    print("Welcome to Python")


welcome()
welcome()
welcome()

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 3. Function with a Parameter
# ==========================================================

print("========== Function with Parameter ==========\n")


def greet_user(name):
    print(f"Hello, {name}")


greet_user("Onkar")
greet_user("Rahul")
greet_user("Priya")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 4. Function with Multiple Parameters
# ==========================================================

print("========== Multiple Parameters ==========\n")


def add_numbers(num1, num2):
    print("Addition:", num1 + num2)


add_numbers(10, 20)
add_numbers(50, 25)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 5. Function to Calculate Total Price
# ==========================================================

print("========== Calculate Total Price ==========\n")


def calculate_total(price, quantity):
    total = price * quantity
    print("Total Price:", total)


calculate_total(500, 4)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 6. return Statement
# ==========================================================

print("========== return Statement ==========\n")


def add(a, b):
    return a + b


result = add(20, 30)

print("Result:", result)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 7. Reusing a Returned Value
# ==========================================================

print("========== Reusing Returned Value ==========\n")


def square(number):
    return number ** 2


result = square(5)

print("Square:", result)
print("Double of Square:", result * 2)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 8. print() vs return
# ==========================================================

print("========== print() vs return ==========\n")


def add_and_print(a, b):
    print(a + b)


def add_and_return(a, b):
    return a + b


add_and_print(10, 20)

returned_value = add_and_return(10, 20)

print("Returned Value:", returned_value)
print("Returned Value x 2:", returned_value * 2)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 9. Check Even or Odd
# ==========================================================

print("========== Even or Odd ==========\n")


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("10 is", check_even_odd(10))
print("17 is", check_even_odd(17))

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 10. Check Voting Eligibility
# ==========================================================

print("========== Voting Eligibility ==========\n")


def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to Vote"
    else:
        return "Not Eligible to Vote"


print(check_voting_eligibility(22))
print(check_voting_eligibility(16))

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 11. Calculate Student Result
# ==========================================================

print("========== Student Result ==========\n")


def check_result(marks):
    if marks >= 35:
        return "Pass"
    else:
        return "Fail"


print("Marks: 78 ->", check_result(78))
print("Marks: 28 ->", check_result(28))

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 12. Function with a Loop
# ==========================================================

print("========== Function with Loop ==========\n")


def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


multiplication_table(5)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 13. Data Engineering Example - Validate Record
# ==========================================================

print("========== Record Validation ==========\n")


def validate_record(record):
    if record is None:
        return False
    else:
        return True


record = 1001

if validate_record(record):
    print("Valid Record")
else:
    print("Invalid Record")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 14. Data Engineering Example - Transform Record
# ==========================================================

print("========== Record Transformation ==========\n")


def transform_record(value):
    return value * 2


records = [10, 20, 30, 40]

for record in records:
    transformed_record = transform_record(record)
    print(f"{record} -> {transformed_record}")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 15. Data Engineering Example - ETL Functions
# ==========================================================

print("========== Simple ETL Pipeline ==========\n")


def extract_data():
    print("Extracting Data")


def transform_data():
    print("Transforming Data")


def load_data():
    print("Loading Data")


extract_data()
transform_data()
load_data()

print("\n" + "=" * 50)

print("\nEnd of Day 10 Examples")