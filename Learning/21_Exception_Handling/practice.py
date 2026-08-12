# 🐍 Day 21 - Exception Handling | Practice

# Solve each problem yourself before checking the README.

# ============================================================
# Practice 1 - ValueError
# ============================================================
# Convert the string below into an integer.
# Handle the ValueError if conversion fails.

value = "abc"


# ============================================================
# Practice 2 - ZeroDivisionError
# ============================================================
# Divide 100 by the value below.
# Handle division by zero.

number = 0


# ============================================================
# Practice 3 - Multiple Exceptions
# ============================================================
# Write a program that converts user input to an integer and
# divides 100 by it.
# Handle both ValueError and ZeroDivisionError.


# ============================================================
# Practice 4 - Exception Object
# ============================================================
# Catch the exception as error and print its message.

try:
    number = int("hello")
except ValueError as error:
    pass


# ============================================================
# Practice 5 - else
# ============================================================
# Write a try/except/else structure.
# Print "Success" only when conversion succeeds.


# ============================================================
# Practice 6 - finally
# ============================================================
# Write a try/except/finally structure and prove that finally
# executes whether an exception occurs or not.


# ============================================================
# Practice 7 - raise
# ============================================================
# Create validate_age(age).
# Raise ValueError when age is less than 18.


# ============================================================
# Practice 8 - Custom Exception
# ============================================================
# Create InvalidEmailError(Exception).
# Raise it when an email does not contain "@".


# ============================================================
# Practice 9 - Multiple Exception Types
# ============================================================
# Catch ValueError and TypeError using one except block.


# ============================================================
# Practice 10 - FileNotFoundError
# ============================================================
# Try to open "sales.csv".
# Handle FileNotFoundError without crashing the program.


# ============================================================
# Practice 11 - Exception Hierarchy
# ============================================================
# Explain why FileNotFoundError can be caught by OSError.
# Write a small example demonstrating this.


# ============================================================
# Practice 12 - Exception Chaining
# ============================================================
# Write a function that converts a value to int.
# If ValueError occurs, raise RuntimeError("Parsing failed")
# from the original exception.


# ============================================================
# Practice 13 - Assertion
# ============================================================
# Use assert to verify that the following batch size is positive.

batch_size = 1000


# ============================================================
# Practice 14 - Logging
# ============================================================
# Use logging.exception() inside an exception handler.
# Trigger a ZeroDivisionError for testing.


# ============================================================
# Practice 15 - Data Engineering Scenario
# ============================================================
# Validate that every record contains:
# customer_id
# email
#
# Raise a custom MissingFieldError when a field is missing.

records = [
    {"customer_id": 101, "email": "onkar@example.com"},
    {"customer_id": 102},
    {"email": "amit@example.com"}
]


# ============================================================
# Practice 16 - Data Engineering Scenario
# ============================================================
# Convert record["amount"] to float.
# Handle:
# - missing amount field
# - invalid amount value
#
# Convert low-level errors into a meaningful ValueError.


# ============================================================
# Practice 17 - Record-Level Error Handling
# ============================================================
# Process the records below one at a time.
# Valid records should be transformed.
# Invalid records should be printed and processing should continue.

records = [
    {"id": 101, "amount": "100"},
    {"id": 102, "amount": "abc"},
    {"id": 103, "amount": "250"},
    {"id": 104}
]


# ============================================================
# Practice 18 - Retry Scenario
# ============================================================
# Create a function that raises ConnectionError twice and then
# succeeds on the third call.
# Retry a maximum of three times.


# ============================================================
# Practice 19 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

try:
    print("A")
    raise ValueError("Problem")
except ValueError:
    print("B")
finally:
    print("C")


# ============================================================
# Practice 20 - Interview Output Prediction
# ============================================================
# Predict the output before running the code.

try:
    number = int("10")
except ValueError:
    print("Error")
else:
    print("Success")
finally:
    print("Done")


# ============================================================
# Practice 21 - Interview Concept
# ============================================================
# Explain why this is dangerous:
#
# try:
#     process_data()
# except:
#     pass
#
# What could happen in a Data Engineering pipeline?


# ============================================================
# Practice 22 - Interview Concept
# ============================================================
# Explain the difference between:
#
# raise ValueError("Invalid")
#
# and:
#
# assert value > 0


# ============================================================
# Practice 23 - Interview Concept
# ============================================================
# Explain the difference between:
#
# except Exception:
#
# and:
#
# except BaseException:
#
# Why is catching BaseException usually discouraged?


# ============================================================
# Practice 24 - Data Engineering Scenario
# ============================================================
# Design an error-handling strategy for:
#
# 1. API timeout
# 2. Malformed JSON record
# 3. Missing required column
# 4. Database connection failure
# 5. Programming bug
#
# Decide whether each should be retried, quarantined, or fail the job.


# ============================================================
# Practice 25 - Interview Challenge
# ============================================================
# Build a small pipeline with:
#
# extract_data()
# transform_data()
# load_data()
#
# Add exception handling so that:
# - extraction errors are logged
# - invalid records are identified
# - load failures are not silently ignored
# - the pipeline reports a clear final status
