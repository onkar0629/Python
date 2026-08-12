# 🐍 Day 20 - Modules and Packages | Examples

# ============================================================
# 1. Standard Library Module
# ============================================================

import math

# math.sqrt() calculates the square root using the math module.
result = math.sqrt(25)

# Print the calculated square root.
print(result)


# ============================================================
# 2. Module Alias
# ============================================================

import datetime as dt

# Create an object representing the current date.
today = dt.date.today()

# Print today's date.
print(today)


# ============================================================
# 3. Import a Specific Name
# ============================================================

from math import factorial

# Calculate the factorial of 5 directly through the imported name.
result = factorial(5)

# Print the result.
print(result)


# ============================================================
# 4. Import Multiple Names
# ============================================================

from math import ceil, floor

# ceil() rounds upward to the nearest integer.
print(ceil(4.2))

# floor() rounds downward to the nearest integer.
print(floor(4.8))


# ============================================================
# 5. Module Namespace
# ============================================================

import json

# JSON text represents a record received from an external source.
record_text = '{"id": 101, "name": "Onkar"}'

# json.loads() converts JSON text into a Python dictionary.
record = json.loads(record_text)

# Access the name from the resulting dictionary.
print(record["name"])


# ============================================================
# 6. __name__
# ============================================================

# __name__ contains the current module's name.
print(__name__)


# ============================================================
# 7. __main__ Pattern
# ============================================================

def main():
    # This function contains the code we want to execute as a script.
    print("Script executed directly")


# This condition is true only when this file is run directly.
if __name__ == "__main__":
    # Execute the main function only during direct execution.
    main()


# ============================================================
# 8. os Module
# ============================================================

import os

# Read the current working directory from the operating system.
current_directory = os.getcwd()

# Print the current working directory.
print(current_directory)


# ============================================================
# 9. pathlib Module
# ============================================================

from pathlib import Path

# Create a Path object for a data directory.
data_path = Path("data")

# Check whether the path currently exists.
print(data_path.exists())


# ============================================================
# 10. Environment Variables
# ============================================================

import os

# Read an environment variable if it exists.
# The second argument returns "development" when ENVIRONMENT is missing.
environment = os.getenv("ENVIRONMENT", "development")

# Print the selected environment.
print(environment)


# ============================================================
# 11. CSV Module
# ============================================================

import csv

# This example demonstrates the CSV module without requiring a file.
rows = [
    ["id", "name"],
    [101, "Onkar"],
    [102, "Rahul"]
]

# Convert each row into a comma-separated string.
for row in rows:
    print(",".join(map(str, row)))


# ============================================================
# 12. Custom Module Example
# ============================================================

# Imagine this function is defined in a separate file named math_utils.py.
def add(a, b):
    # Return the sum of two values.
    return a + b


# Call the reusable function.
print(add(10, 20))


# ============================================================
# 13. Simulating a Utility Module
# ============================================================

def clean_name(name):
    # Remove whitespace and normalize capitalization.
    return name.strip().title()


def clean_names(names):
    # Apply clean_name() to every value.
    return [clean_name(name) for name in names]


names = [" onkar ", " rahul ", " amit "]

# Use the utility function to clean all names.
print(clean_names(names))


# ============================================================
# 14. Package-Style Import Example
# ============================================================

# In a real project, a package could expose a function like this:
# from utils.cleaning import clean_name
#
# The following local function demonstrates the same idea without
# requiring another repository file to be imported.

def validate_id(value):
    # Return True when the value is a positive integer.
    return isinstance(value, int) and value > 0


# Test the validation function.
print(validate_id(101))
print(validate_id(-1))


# ============================================================
# 15. Data Engineering Configuration Example
# ============================================================

# Store configuration values in one structure that could live in config.py.
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "database": "sales"
}

# Read the database host from the configuration.
print(DATABASE_CONFIG["host"])

# Read the database name from the configuration.
print(DATABASE_CONFIG["database"])


# ============================================================
# 16. Dependency Check Example
# ============================================================

# The standard library's sys module provides information about Python.
import sys

# Print the Python version used to run this script.
print(sys.version)

# Print the interpreter executable path.
print(sys.executable)


# ============================================================
# 17. Import Path
# ============================================================

import sys

# sys.path contains locations where Python searches for modules.
for path in sys.path:
    # Print each location checked by the import system.
    print(path)


# ============================================================
# 18. Logging Module
# ============================================================

import logging

# Configure a basic logging setup for this example.
logging.basicConfig(level=logging.INFO)

# Create a module-level logger.
logger = logging.getLogger(__name__)

# Write an informational log message.
logger.info("Pipeline started")


# ============================================================
# 19. Data Engineering Pipeline Structure
# ============================================================

def extract_data():
    # Simulate extracting records from a source.
    return [101, 102, 103]


def transform_data(records):
    # Simulate a transformation by doubling every record ID.
    return [record * 2 for record in records]


def load_data(records):
    # Simulate loading transformed records into a destination.
    print("Loading:", records)


# Execute the extraction step.
raw_data = extract_data()

# Pass the extracted data to the transformation step.
transformed_data = transform_data(raw_data)

# Pass transformed data to the loading step.
load_data(transformed_data)
