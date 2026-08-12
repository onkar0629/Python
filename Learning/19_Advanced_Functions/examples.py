# 🐍 Day 19 - Advanced Functions | Examples

# ============================================================
# 1. Positional Arguments
# ============================================================

def introduce(name, age):
    # Print the name received by the first parameter.
    print(name)

    # Print the age received by the second parameter.
    print(age)


# The first argument goes to name and the second goes to age.
introduce("Onkar", 22)


# ============================================================
# 2. Keyword Arguments
# ============================================================

def introduce_person(name, age):
    # Print the person's name.
    print(name)

    # Print the person's age.
    print(age)


# Keyword arguments identify parameters explicitly.
introduce_person(age=22, name="Onkar")


# ============================================================
# 3. Default Arguments
# ============================================================

def greet(name, message="Hello"):
    # Use the supplied message or the default "Hello".
    print(message, name)


# No message is supplied, so the default is used.
greet("Onkar")

# This call overrides the default message.
greet("Onkar", "Welcome")


# ============================================================
# 4. *args
# ============================================================

def total(*numbers):
    # numbers contains all positional arguments as a tuple.
    print(numbers)

    # Add all values stored in the tuple.
    return sum(numbers)


# Pass any number of positional arguments.
print(total(10, 20, 30))


# ============================================================
# 5. **kwargs
# ============================================================

def show_details(**details):
    # details contains keyword arguments as a dictionary.
    print(details)


# Pass multiple named arguments.
show_details(name="Onkar", role="Data Engineer", city="Pune")


# ============================================================
# 6. *args and **kwargs Together
# ============================================================

def process(*args, **kwargs):
    # args stores positional arguments in a tuple.
    print(args)

    # kwargs stores keyword arguments in a dictionary.
    print(kwargs)


# Pass both positional and keyword arguments.
process(10, 20, name="Onkar", city="Pune")


# ============================================================
# 7. Unpacking a List with *
# ============================================================

def add(a, b, c):
    # Return the sum of the three parameters.
    return a + b + c


numbers = [10, 20, 30]

# *numbers unpacks the list into three positional arguments.
print(add(*numbers))


# ============================================================
# 8. Unpacking a Dictionary with **
# ============================================================

def connect(host, port):
    # Print the connection settings received by the function.
    print(host, port)


config = {
    "host": "localhost",
    "port": 3306
}

# **config matches dictionary keys with function parameter names.
connect(**config)


# ============================================================
# 9. Local Scope
# ============================================================

def local_example():
    # This variable exists only inside this function.
    message = "Hello from local scope"

    # Print the local variable.
    print(message)


# Call the function so the local variable can be used.
local_example()


# ============================================================
# 10. Global Scope
# ============================================================

message = "Hello from global scope"


def global_example():
    # The function can read the global variable.
    print(message)


# Call the function.
global_example()


# ============================================================
# 11. global Keyword
# ============================================================

count = 0


def increment():
    # Tell Python that count refers to the global variable.
    global count

    # Increase the global value.
    count += 1


# Modify the global value through the function.
increment()

# Print the updated global value.
print(count)


# ============================================================
# 12. nonlocal Keyword
# ============================================================

def create_counter():
    # This variable belongs to the enclosing function.
    count = 0

    def increment():
        # Tell Python to modify the enclosing count variable.
        nonlocal count

        # Increase the enclosing variable.
        count += 1

        # Return the updated count.
        return count

    # Return the inner function.
    return increment


counter = create_counter()

# The first call changes the remembered count to 1.
print(counter())

# The second call changes the remembered count to 2.
print(counter())


# ============================================================
# 13. Function as an Object
# ============================================================

def greet_user():
    # Print a greeting.
    print("Hello Onkar")


# Store the function object in another variable.
say_hello = greet_user

# Call the function through the new variable.
say_hello()


# ============================================================
# 14. Functions Stored in a List
# ============================================================

def add_numbers(a, b):
    # Return the sum.
    return a + b


def multiply_numbers(a, b):
    # Return the product.
    return a * b


# Store both function objects inside a list.
operations = [add_numbers, multiply_numbers]

# Call the first function from the list.
print(operations[0](2, 3))

# Call the second function from the list.
print(operations[1](2, 3))


# ============================================================
# 15. Passing a Function as an Argument
# ============================================================

def apply_operation(a, b, operation):
    # Call the supplied function with a and b.
    return operation(a, b)


def subtract_numbers(a, b):
    # Return the difference.
    return a - b


# Pass the function object, not the result of calling it.
print(apply_operation(20, 5, subtract_numbers))


# ============================================================
# 16. Returning a Function
# ============================================================

def create_multiplier(factor):
    # Define an inner function that uses factor.
    def multiply(number):
        # Multiply the supplied number by the remembered factor.
        return number * factor

    # Return the inner function object.
    return multiply


# Create a function that doubles values.
double = create_multiplier(2)

# Call the returned function.
print(double(10))


# ============================================================
# 17. Lambda Function
# ============================================================

# Create a small anonymous function that squares a number.
square = lambda number: number ** 2

# Call the lambda function.
print(square(5))


# ============================================================
# 18. Lambda with sorted()
# ============================================================

students = [
    {"name": "Onkar", "score": 85},
    {"name": "Rahul", "score": 92},
    {"name": "Amit", "score": 78}
]

# Sort records using the score field as the sorting key.
sorted_students = sorted(
    students,
    key=lambda student: student["score"]
)

# Print the sorted records.
print(sorted_students)


# ============================================================
# 19. map()
# ============================================================

numbers = [1, 2, 3, 4]

# map() applies the lambda function to every number.
squared_values = map(lambda number: number ** 2, numbers)

# Convert the map iterator into a list.
squared_values = list(squared_values)

# Print the resulting list.
print(squared_values)


# ============================================================
# 20. filter()
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# Keep values for which the lambda returns True.
even_numbers = filter(lambda number: number % 2 == 0, numbers)

# Convert the filter iterator into a list.
even_numbers = list(even_numbers)

# Print the filtered values.
print(even_numbers)


# ============================================================
# 21. Closure
# ============================================================

def create_multiplier_closure(factor):
    # factor belongs to the enclosing function.
    def multiply(number):
        # The inner function remembers factor.
        return number * factor

    # Return the inner function.
    return multiply


# Create a multiplier that remembers factor = 3.
triple = create_multiplier_closure(3)

# Use the remembered factor.
print(triple(10))


# ============================================================
# 22. Recursion
# ============================================================

def factorial(number):
    # Stop recursion when number reaches zero.
    if number == 0:
        return 1

    # Call the function with a smaller value.
    return number * factorial(number - 1)


# Calculate 4!.
print(factorial(4))


# ============================================================
# 23. Basic Decorator
# ============================================================

def logger(function):
    # Define a wrapper around the original function.
    def wrapper():
        # Run code before the original function.
        print("Function started")

        # Call the original function.
        function()

        # Run code after the original function.
        print("Function finished")

    # Return the wrapper function.
    return wrapper


@logger
def greet():
    # Print the original function's message.
    print("Hello")


# The decorator causes wrapper() to run when greet() is called.
greet()


# ============================================================
# 24. Decorator with *args and **kwargs
# ============================================================

def log_call(function):
    # Create a wrapper that can accept any arguments.
    def wrapper(*args, **kwargs):
        # Print a message before the function runs.
        print("Starting function")

        # Execute the original function and store its result.
        result = function(*args, **kwargs)

        # Print a message after execution.
        print("Finished function")

        # Return the original result to the caller.
        return result

    # Return the wrapper function.
    return wrapper


@log_call
def add_values(a, b):
    # Return the sum.
    return a + b


# Call the decorated function and print its returned result.
print(add_values(10, 20))


# ============================================================
# 25. Data Engineering Example - Reusable Transformation
# ============================================================

def clean_name(name):
    # Remove surrounding whitespace and normalize capitalization.
    return name.strip().title()


names = [" onkar ", " rahul ", " amit "]

# Apply the reusable transformation to every name.
cleaned_names = [clean_name(name) for name in names]

# Print the cleaned values.
print(cleaned_names)


# ============================================================
# 26. Data Engineering Example - Configurable Function
# ============================================================

def load_data(data, **config):
    # Read batch_size from config or use 1000 as the default.
    batch_size = config.get("batch_size", 1000)

    # Read target from config or use "sales" as the default.
    target = config.get("target", "sales")

    # Print the configuration used by the load operation.
    print("Batch size:", batch_size)
    print("Target:", target)
    print("Records:", len(data))


records = [101, 102, 103]

# Pass optional configuration as keyword arguments.
load_data(records, batch_size=5000, target="orders")


# ============================================================
# 27. Data Engineering Example - Higher-Order Transformation
# ============================================================

def transform_records(records, transform_function):
    # Apply the supplied transformation to every record.
    return [transform_function(record) for record in records]


def get_customer_id(record):
    # Extract the customer_id field from one record.
    return record["customer_id"]


records = [
    {"customer_id": 101, "name": "Onkar"},
    {"customer_id": 102, "name": "Rahul"}
]

# Pass the transformation function to the generic processor.
ids = transform_records(records, get_customer_id)

# Print the extracted IDs.
print(ids)
