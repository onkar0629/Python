# 🐍 Day 24 - Decorators | Examples

from functools import wraps, lru_cache
from time import perf_counter

# ============================================================
# 1. Functions Are Objects
# ============================================================

def greet():
    # Print a simple greeting.
    print("Hello")


# Store the function object in another variable.
message = greet

# Call the function through the new variable.
message()


# ============================================================
# 2. Passing a Function as an Argument
# ============================================================

def execute(function):
    # Call the function received as an argument.
    function()


def welcome():
    # Print a welcome message.
    print("Welcome")


# Pass the function object without calling it here.
execute(welcome)


# ============================================================
# 3. Returning a Function
# ============================================================

def outer():
    def inner():
        # This function is returned by outer().
        print("Inside inner")

    # Return the function object.
    return inner


# Store the returned function.
function = outer()

# Call the returned function.
function()


# ============================================================
# 4. Basic Decorator - Manual Syntax
# ============================================================

def log_call(function):
    def wrapper():
        # Run additional behavior before the original function.
        print("Before function")

        # Call the original function.
        function()

        # Run additional behavior after the original function.
        print("After function")

    # Return the wrapper function.
    return wrapper


def greet_user():
    # This is the original business logic.
    print("Hello Onkar")


# Replace greet_user with the wrapped function.
greet_user = log_call(greet_user)

# Calling greet_user now executes the wrapper.
greet_user()


# ============================================================
# 5. @ Decorator Syntax
# ============================================================

def log_execution(function):
    def wrapper():
        # Log before the original function.
        print("Starting")

        # Execute the original function.
        function()

        # Log after the original function.
        print("Finished")

    # Return the wrapper.
    return wrapper


@log_execution
def process_data():
    # Simulate the actual business operation.
    print("Processing data")


# Execute the decorated function.
process_data()


# ============================================================
# 6. Decorator with Function Arguments
# ============================================================

def log_arguments(function):
    def wrapper(*args, **kwargs):
        # Print positional arguments received by the function.
        print("args:", args)

        # Print keyword arguments received by the function.
        print("kwargs:", kwargs)

        # Call the original function with all arguments.
        result = function(*args, **kwargs)

        # Return the original result.
        return result

    # Return the wrapper.
    return wrapper


@log_arguments
def add(a, b):
    # Return the sum of two numbers.
    return a + b


# Call the decorated function with positional arguments.
print(add(10, 20))

# Call it again with keyword arguments.
print(add(a=5, b=7))


# ============================================================
# 7. Preserving Return Values
# ============================================================

def double_call(function):
    def wrapper(*args, **kwargs):
        # Call the original function.
        result = function(*args, **kwargs)

        # Return its result so callers receive the expected value.
        return result

    return wrapper


@double_call
def multiply(a, b):
    # Return the multiplication result.
    return a * b


# The decorated function still returns 50.
print(multiply(5, 10))


# ============================================================
# 8. functools.wraps
# ============================================================

def logging_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Print the function name before execution.
        print("Running:", function.__name__)

        # Execute the original function and preserve its result.
        return function(*args, **kwargs)

    return wrapper


@logging_decorator
def calculate_total(a, b):
    """Return the total of two values."""
    return a + b


# Call the decorated function.
print(calculate_total(10, 15))

# Because wraps() was used, the original function name is preserved.
print(calculate_total.__name__)

# The original docstring is also preserved.
print(calculate_total.__doc__)


# ============================================================
# 9. Timing Decorator
# ============================================================

def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Record the start time immediately before execution.
        start = perf_counter()

        try:
            # Run the original function and return its result.
            return function(*args, **kwargs)
        finally:
            # Calculate elapsed time even if the function raises an error.
            elapsed = perf_counter() - start

            # Display the execution time.
            print(f"{function.__name__}: {elapsed:.6f} seconds")

    return wrapper


@measure_time
def slow_operation():
    # Perform a simple loop to demonstrate timing.
    total = 0

    for number in range(1_000_000):
        total += number

    # Return the calculated total.
    return total


# Execute the timed function.
print(slow_operation())


# ============================================================
# 10. Decorator with Its Own Arguments
# ============================================================

def repeat(times):
    # This outer function receives the decorator configuration.
    def decorator(function):
        # This function receives the original function.
        @wraps(function)
        def wrapper(*args, **kwargs):
            # Run the original function the requested number of times.
            for _ in range(times):
                function(*args, **kwargs)

        # Return the configured wrapper.
        return wrapper

    # Return the actual decorator.
    return decorator


@repeat(3)
def say_hello(name):
    # Print the supplied name.
    print(f"Hello {name}")


# Call the function; the decorator executes it three times.
say_hello("Onkar")


# ============================================================
# 11. Multiple Decorators
# ============================================================

def first(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Run before the inner decorated function.
        print("First - before")

        # Continue to the next wrapper.
        result = function(*args, **kwargs)

        # Run after the inner decorated function.
        print("First - after")

        return result

    return wrapper


def second(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Run before the original function.
        print("Second - before")

        # Continue execution.
        result = function(*args, **kwargs)

        # Run after the original function.
        print("Second - after")

        return result

    return wrapper


@first
@second
def show_message():
    # This is the original function.
    print("Original function")


# Observe the order in which wrappers execute.
show_message()


# ============================================================
# 12. Validation Decorator
# ============================================================

def require_positive(function):
    @wraps(function)
    def wrapper(number):
        # Reject invalid input before calling the business logic.
        if number <= 0:
            raise ValueError("Number must be positive")

        # Execute the original function for valid input.
        return function(number)

    return wrapper


@require_positive
def square(number):
    # Return the square of a valid number.
    return number * number


# Execute with valid input.
print(square(5))


# ============================================================
# 13. Class Decorator
# ============================================================

def add_category(cls):
    # Add a class attribute to the decorated class.
    cls.category = "Data Engineering"

    # Return the modified class.
    return cls


@add_category
class Pipeline:
    # Define a simple pipeline class.
    pass


# Access the attribute added by the class decorator.
print(Pipeline.category)


# ============================================================
# 14. @staticmethod
# ============================================================

class Math:
    @staticmethod
    def add(a, b):
        # Return the sum without needing an instance.
        return a + b


# Call the static method directly from the class.
print(Math.add(10, 20))


# ============================================================
# 15. @classmethod
# ============================================================

class User:
    count = 0

    def __init__(self, name):
        # Store the user's name on the instance.
        self.name = name

        # Increment the shared class-level counter.
        User.count += 1

    @classmethod
    def get_count(cls):
        # Access class-level state through cls.
        return cls.count


# Create two user instances.
User("Onkar")
User("Rahul")

# Retrieve the number of created users.
print(User.get_count())


# ============================================================
# 16. @property
# ============================================================

class Customer:
    def __init__(self, name):
        # Store the original name.
        self.name = name

    @property
    def normalized_name(self):
        # Return a computed value as if it were an attribute.
        return self.name.strip().title()


customer = Customer(" onkar jadhav ")

# Access the property without calling it like a method.
print(customer.normalized_name)


# ============================================================
# 17. @lru_cache
# ============================================================

@lru_cache(maxsize=None)
def fibonacci(number):
    # Return the base cases directly.
    if number <= 1:
        return number

    # Cached recursive calls avoid repeating previous calculations.
    return fibonacci(number - 1) + fibonacci(number - 2)


# Calculate Fibonacci efficiently using the cache.
print(fibonacci(20))


# ============================================================
# 18. Data Engineering - Retry Decorator
# ============================================================

def retry(attempts):
    # Receive the maximum number of attempts.
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            # Try the operation up to the configured number of times.
            for attempt in range(1, attempts + 1):
                try:
                    # Return immediately if the operation succeeds.
                    return function(*args, **kwargs)
                except ConnectionError:
                    # Re-raise after the final attempt instead of hiding failure.
                    if attempt == attempts:
                        raise

                    # Report that another attempt will be made.
                    print(f"Attempt {attempt} failed; retrying...")

        return wrapper

    return decorator


call_count = 0


@retry(attempts=3)
def load_api_data():
    global call_count

    # Track how many times this simulated API call has run.
    call_count += 1

    # Simulate a transient connection problem on the first two attempts.
    if call_count < 3:
        raise ConnectionError("Temporary API failure")

    # Return data after the transient failures disappear.
    return "API data loaded"


# Run the retry-enabled operation.
print(load_api_data())
