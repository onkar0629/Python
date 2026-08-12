"""
==========================================================
Day 11 : Function Arguments
Topic  : Examples

Description:
This file contains runnable examples demonstrating the
concepts covered in Day 11.

Topics Covered:
1. Parameters and Arguments
2. Positional Arguments
3. Keyword Arguments
4. Default Arguments
5. Variable-Length Positional Arguments (*args)
6. Variable-Length Keyword Arguments (**kwargs)
7. Combining Argument Types
8. Practical Examples
9. Data Engineering Examples
==========================================================
"""

# ==========================================================
# 1. Parameters and Arguments
# ==========================================================

print("========== Parameters and Arguments ==========\n")


def greet(name):
    print(f"Hello, {name}")


greet("Onkar")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. Positional Arguments
# ==========================================================

print("========== Positional Arguments ==========\n")


def student_details(name, age):
    print("Name:", name)
    print("Age:", age)


student_details("Rahul", 22)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 3. Position of Arguments Matters
# ==========================================================

print("========== Argument Position ==========\n")


def subtract(a, b):
    return a - b


print("subtract(20, 5):", subtract(20, 5))
print("subtract(5, 20):", subtract(5, 20))

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 4. Keyword Arguments
# ==========================================================

print("========== Keyword Arguments ==========\n")


def employee(name, department):
    print("Name:", name)
    print("Department:", department)


employee(name="Aman", department="Data Engineering")

print()

employee(department="Analytics", name="Priya")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 5. Default Arguments
# ==========================================================

print("========== Default Arguments ==========\n")


def greet_user(name, message="Welcome"):
    print(f"{message}, {name}")


greet_user("Rahul")
greet_user("Priya", "Good Morning")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 6. Default Argument - Calculate Price
# ==========================================================

print("========== Calculate Price ==========\n")


def calculate_price(price, quantity=1):
    return price * quantity


print("Total Price:", calculate_price(500))
print("Total Price:", calculate_price(500, 4))

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 7. Variable-Length Positional Arguments (*args)
# ==========================================================

print("========== *args ==========\n")


def display_numbers(*numbers):
    print(numbers)


display_numbers(10, 20)
display_numbers(10, 20, 30, 40, 50)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 8. Iterate Through *args
# ==========================================================

print("========== Iterating Through *args ==========\n")


def display_skills(*skills):
    for skill in skills:
        print(skill)


display_skills("Python", "SQL", "Azure", "Spark")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 9. Calculate Total Using *args
# ==========================================================

print("========== Calculate Total with *args ==========\n")


def calculate_total(*numbers):
    return sum(numbers)


print("Total:", calculate_total(10, 20))
print("Total:", calculate_total(10, 20, 30))
print("Total:", calculate_total(10, 20, 30, 40))

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 10. Variable-Length Keyword Arguments (**kwargs)
# ==========================================================

print("========== **kwargs ==========\n")


def display_profile(**details):
    print(details)


display_profile(
    name="Rahul",
    age=22,
    city="Pune"
)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 11. Access Values from **kwargs
# ==========================================================

print("========== Accessing **kwargs ==========\n")


def student_profile(**details):
    print("Name:", details["name"])
    print("Course:", details["course"])
    print("City:", details["city"])


student_profile(
    name="Aman",
    course="Data Engineering",
    city="Pune"
)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 12. Iterate Through **kwargs
# ==========================================================

print("========== Iterating Through **kwargs ==========\n")


def show_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


show_details(
    name="Priya",
    role="Data Engineer",
    experience=1
)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 13. Combining Regular and Default Arguments
# ==========================================================

print("========== Regular + Default Arguments ==========\n")


def employee_details(name, department="IT"):
    print("Name:", name)
    print("Department:", department)


employee_details("Rahul")

print()

employee_details("Aman", "Data Engineering")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 14. Combining Regular Arguments and *args
# ==========================================================

print("========== Regular Arguments + *args ==========\n")


def employee_skills(name, *skills):
    print("Employee:", name)
    print("Skills:")

    for skill in skills:
        print("-", skill)


employee_skills(
    "Rahul",
    "Python",
    "SQL",
    "Spark"
)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 15. Combining Regular Arguments and **kwargs
# ==========================================================

print("========== Regular Arguments + **kwargs ==========\n")


def employee_profile(name, **details):
    print("Name:", name)

    for key, value in details.items():
        print(f"{key}: {value}")


employee_profile(
    "Aman",
    department="Data Engineering",
    city="Pune",
    experience=2
)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 16. Practical Example - Shopping Bill
# ==========================================================

print("========== Shopping Bill ==========\n")


def calculate_bill(price, quantity=1):
    return price * quantity


bill = calculate_bill(750, 4)

print("Total Bill: ₹", bill)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 17. Data Engineering Example - File Processing
# ==========================================================

print("========== File Processing ==========\n")


def process_file(file_name, file_type="csv"):
    print("File Name:", file_name)
    print("File Type:", file_type)
    print("Processing Started")


process_file("customers.csv")

print()

process_file(
    file_name="orders.json",
    file_type="json"
)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 18. Data Engineering Example - Pipeline Configuration
# ==========================================================

print("========== Pipeline Configuration ==========\n")


def pipeline_config(**config):
    for key, value in config.items():
        print(f"{key}: {value}")


pipeline_config(
    source="Raw Data",
    destination="Processed Data",
    batch_size=5000,
    file_format="CSV"
)

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 19. Data Engineering Example - Multiple Files
# ==========================================================

print("========== Process Multiple Files ==========\n")


def process_files(*file_names):
    for file_name in file_names:
        print(f"Processing: {file_name}")


process_files(
    "customers.csv",
    "orders.csv",
    "products.csv"
)

print("\nAll Files Processed Successfully!")

print("\n" + "=" * 50)

print("\nEnd of Day 11 Examples")