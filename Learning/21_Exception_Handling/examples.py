# 🐍 Day 21 - Exception Handling | Examples

# ============================================================
# 1. Basic try / except
# ============================================================

try:
    # int() cannot convert the text "abc" into an integer.
    number = int("abc")
except ValueError:
    # Handle the specific conversion error.
    print("Invalid number")


# ============================================================
# 2. Handling ZeroDivisionError
# ============================================================

try:
    # Division by zero raises ZeroDivisionError.
    result = 10 / 0
except ZeroDivisionError:
    # Handle the division error.
    print("Cannot divide by zero")


# ============================================================
# 3. Multiple except Blocks
# ============================================================

value = "0"

try:
    # Convert the string to an integer.
    number = int(value)

    # This can raise ZeroDivisionError when number is zero.
    result = 100 / number
except ValueError:
    # Handle invalid integer conversion.
    print("Value is not a valid integer")
except ZeroDivisionError:
    # Handle division by zero.
    print("Cannot divide by zero")


# ============================================================
# 4. Exception Object
# ============================================================

try:
    # Trigger a ValueError.
    number = int("abc")
except ValueError as error:
    # Store the exception object in error.
    print("Error:", error)


# ============================================================
# 5. try / except / else
# ============================================================

try:
    # This conversion succeeds.
    number = int("100")
except ValueError:
    # This block would run if conversion failed.
    print("Invalid number")
else:
    # else runs only when the try block succeeds.
    print("Conversion successful:", number)


# ============================================================
# 6. try / except / finally
# ============================================================

try:
    # Perform a successful calculation.
    result = 10 + 20
except Exception:
    # Handle an unexpected application-level exception.
    print("Calculation failed")
finally:
    # This block runs regardless of success or failure.
    print("Calculation finished")


# ============================================================
# 7. raise
# ============================================================

def withdraw(balance, amount):
    # Reject withdrawals larger than the available balance.
    if amount > balance:
        # Raise a meaningful exception for the invalid business rule.
        raise ValueError("Insufficient balance")

    # Return the remaining balance when the request is valid.
    return balance - amount


try:
    # Attempt a withdrawal larger than the balance.
    print(withdraw(100, 200))
except ValueError as error:
    # Handle the business-rule validation error.
    print(error)


# ============================================================
# 8. Custom Exception
# ============================================================

class InvalidRecordError(Exception):
    # Define an application-specific exception type.
    pass


def validate_record(record):
    # Check whether customer_id exists.
    if "customer_id" not in record:
        # Raise the custom exception when the required field is missing.
        raise InvalidRecordError("customer_id is missing")

    # Return True when validation succeeds.
    return True


try:
    # This record does not contain customer_id.
    validate_record({"name": "Onkar"})
except InvalidRecordError as error:
    # Handle the domain-specific validation error.
    print(error)


# ============================================================
# 9. Multiple Exceptions in One Handler
# ============================================================

value = None

try:
    # This may raise TypeError because value is None.
    number = int(value)
except (ValueError, TypeError):
    # Handle either invalid value or invalid type.
    print("Invalid input")


# ============================================================
# 10. Exception Hierarchy Example
# ============================================================

try:
    # Opening a missing file raises FileNotFoundError.
    file = open("missing_file.txt", "r")
except FileNotFoundError:
    # Catch the specific file-not-found error.
    print("File was not found")


# ============================================================
# 11. File Handling with with
# ============================================================

try:
    # with automatically manages the file resource.
    with open("data.txt", "r") as file:
        # Read the entire file.
        content = file.read()
except FileNotFoundError:
    # Handle the case where the file does not exist.
    print("data.txt does not exist")


# ============================================================
# 12. Exception Chaining
# ============================================================

def parse_customer_id(value):
    try:
        # Attempt to convert the value into an integer.
        return int(value)
    except ValueError as error:
        # Raise a higher-level error while preserving the original cause.
        raise RuntimeError("Customer ID parsing failed") from error


try:
    # Trigger the conversion failure.
    parse_customer_id("ABC")
except RuntimeError as error:
    # Handle the higher-level error.
    print(error)


# ============================================================
# 13. Assertion
# ============================================================

age = 22

# Verify an internal assumption that age is at least 18.
assert age >= 18, "Age must be at least 18"

# Print only if the assertion succeeds.
print("Age validation passed")


# ============================================================
# 14. Logging an Exception
# ============================================================

import logging

# Configure logging so INFO and higher messages are displayed.
logging.basicConfig(level=logging.INFO)

# Create a logger associated with this module.
logger = logging.getLogger(__name__)

try:
    # Trigger an exception for demonstration.
    result = 10 / 0
except ZeroDivisionError:
    # logger.exception() records the message and traceback.
    logger.exception("Calculation failed")


# ============================================================
# 15. Data Engineering - Record Validation
# ============================================================

class MissingFieldError(Exception):
    # Represent a required-field validation failure.
    pass


def validate_customer(record):
    # Define fields that must exist in every customer record.
    required_fields = ["customer_id", "email"]

    # Check each required field.
    for field in required_fields:
        # Raise an exception when a field is absent.
        if field not in record:
            raise MissingFieldError(f"Missing field: {field}")

    # Return the validated record.
    return record


customer = {
    "customer_id": 101,
    "email": "onkar@example.com"
}

try:
    # Validate the customer record.
    validated_customer = validate_customer(customer)

    # Print the validated record.
    print(validated_customer)
except MissingFieldError as error:
    # Handle the data-quality failure.
    print("Invalid record:", error)


# ============================================================
# 16. Data Engineering - Transform with Error Handling
# ============================================================

def transform_amount(record):
    try:
        # Read the amount field from the input record.
        amount = record["amount"]

        # Convert the value into a float.
        amount = float(amount)

        # Apply a simple 18% transformation.
        return amount * 1.18
    except KeyError as error:
        # Convert a missing field into a meaningful transformation error.
        raise ValueError("Required amount field is missing") from error
    except (TypeError, ValueError) as error:
        # Convert invalid amount data into a domain-level error.
        raise ValueError("Amount is invalid") from error


try:
    # Process a valid record.
    print(transform_amount({"amount": "100"}))
except ValueError as error:
    # Handle transformation failure.
    print(error)


# ============================================================
# 17. Retry-Like Pattern
# ============================================================

def unstable_operation(attempt):
    # Simulate a temporary failure for the first two attempts.
    if attempt < 3:
        raise ConnectionError("Temporary connection failure")

    # Return success after the temporary failures.
    return "Success"


# Try the operation a limited number of times.
for attempt in range(1, 4):
    try:
        # Run the operation using the current attempt number.
        result = unstable_operation(attempt)

        # Print the successful result.
        print(result)

        # Stop retrying after success.
        break
    except ConnectionError as error:
        # Report the temporary failure.
        print("Attempt", attempt, "failed:", error)
