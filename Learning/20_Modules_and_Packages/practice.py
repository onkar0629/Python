# 🐍 Day 20 - Modules and Packages | Practice

# Solve each problem yourself before checking the README.

# ============================================================
# Practice 1 - Standard Library Import
# ============================================================
# Import the math module and calculate the square root of 144.


# ============================================================
# Practice 2 - from import
# ============================================================
# Import factorial directly from math and calculate 6!.


# ============================================================
# Practice 3 - Module Alias
# ============================================================
# Import datetime using an alias called dt.
# Print today's date.


# ============================================================
# Practice 4 - JSON
# ============================================================
# Import json and convert the following JSON string into a Python dictionary.

record_text = '{"id": 101, "name": "Onkar", "role": "Data Engineer"}'


# ============================================================
# Practice 5 - __name__
# ============================================================
# Print the value of __name__.
# Explain what it means when the file is run directly.


# ============================================================
# Practice 6 - __main__
# ============================================================
# Create a main() function and make it execute only when this
# file is run directly.


# ============================================================
# Practice 7 - Custom Module
# ============================================================
# Create a separate module called calculator.py containing:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
#
# Import the module into another file and use all three functions.


# ============================================================
# Practice 8 - from Module import
# ============================================================
# Import only the add() function from calculator.py.
# Call it without using calculator.add().


# ============================================================
# Practice 9 - Package Structure
# ============================================================
# Design the following package structure:
#
# utils/
# ├── __init__.py
# ├── cleaning.py
# └── validation.py
#
# Put clean_name() in cleaning.py and validate_id() in validation.py.


# ============================================================
# Practice 10 - Package Import
# ============================================================
# Import clean_name() from utils.cleaning and use it on:
# " onkar jadhav "


# ============================================================
# Practice 11 - pathlib
# ============================================================
# Use pathlib.Path to create a Path object for "data/raw".
# Check whether the path exists.


# ============================================================
# Practice 12 - Environment Variable
# ============================================================
# Use os.getenv() to read ENVIRONMENT.
# Return "development" if it does not exist.


# ============================================================
# Practice 13 - pip
# ============================================================
# Without running the command, write the command you would use
# to install pandas using the current Python interpreter.


# ============================================================
# Practice 14 - Virtual Environment
# ============================================================
# Write the commands needed to:
# 1. Create a virtual environment named .venv.
# 2. Activate it on macOS/Linux.
# 3. Deactivate it.


# ============================================================
# Practice 15 - requirements.txt
# ============================================================
# Write the command that installs all dependencies listed in
# requirements.txt.


# ============================================================
# Practice 16 - Module Namespace
# ============================================================
# Explain the difference between:
#
# import math
# math.sqrt(25)
#
# and:
#
# from math import sqrt
# sqrt(25)


# ============================================================
# Practice 17 - Import Error
# ============================================================
# You receive:
#
# ModuleNotFoundError: No module named 'pandas'
#
# List at least three possible causes and explain how you would debug it.


# ============================================================
# Practice 18 - Circular Import
# ============================================================
# Explain why the following structure can cause problems:
#
# a.py → imports b.py
# b.py → imports a.py
#
# Suggest a better project structure.


# ============================================================
# Practice 19 - Data Engineering Scenario
# ============================================================
# Design modules for a pipeline with these responsibilities:
#
# 1. Extract data from a source.
# 2. Clean and transform data.
# 3. Validate records.
# 4. Load data into a warehouse.
# 5. Store configuration.
#
# Write an appropriate directory structure.


# ============================================================
# Practice 20 - Data Engineering Scenario
# ============================================================
# Create a config.py module containing:
# DATABASE_HOST
# DATABASE_PORT
# DATABASE_NAME
#
# Import these values into another Python file.


# ============================================================
# Practice 21 - Data Engineering Scenario
# ============================================================
# Create a reusable cleaning module with:
# clean_name()
# clean_email()
# clean_phone()
#
# Import and use the functions from another module.


# ============================================================
# Practice 22 - Data Engineering Scenario
# ============================================================
# Create a pipeline.py containing:
# extract_data()
# transform_data()
# load_data()
#
# Use if __name__ == "__main__" so the pipeline executes only
# when pipeline.py is run directly.


# ============================================================
# Practice 23 - Interview Output Prediction
# ============================================================
# Predict the output when this file is run directly.

print(__name__)


# ============================================================
# Practice 24 - Interview Concept
# ============================================================
# Explain why this is generally preferred:
#
# import math
# math.sqrt(25)
#
# over:
#
# from math import *
# sqrt(25)


# ============================================================
# Practice 25 - Interview Challenge
# ============================================================
# A production pipeline works on your laptop but fails with:
#
# ModuleNotFoundError
#
# Build a debugging checklist covering:
# - Python interpreter
# - virtual environment
# - installed packages
# - pip
# - project structure
# - import path
# - dependency file
