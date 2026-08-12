# 🐍 Day 22 - File Handling | Practice

# Solve each problem yourself before checking the README.

# ============================================================
# Practice 1 - Create and Write
# ============================================================
# Create a file called notes.txt and write three lines to it.


# ============================================================
# Practice 2 - Read Entire File
# ============================================================
# Read notes.txt using read() and print the content.


# ============================================================
# Practice 3 - readline()
# ============================================================
# Read the first two lines of notes.txt using readline().


# ============================================================
# Practice 4 - readlines()
# ============================================================
# Read all lines into a list using readlines().


# ============================================================
# Practice 5 - File Iteration
# ============================================================
# Iterate through notes.txt line by line and print each line
# without its newline character.


# ============================================================
# Practice 6 - Append
# ============================================================
# Append a fourth line to notes.txt without deleting existing data.


# ============================================================
# Practice 7 - File Modes
# ============================================================
# Explain the difference between:
# r
# w
# a
# x
# rb
# r+


# ============================================================
# Practice 8 - with Statement
# ============================================================
# Rewrite this code using with:
#
# file = open("notes.txt", "r")
# content = file.read()
# file.close()


# ============================================================
# Practice 9 - Encoding
# ============================================================
# Read notes.txt using UTF-8 encoding.


# ============================================================
# Practice 10 - pathlib
# ============================================================
# Create this path using pathlib:
# data/raw/sales.csv
#
# Print:
# - complete path
# - file name
# - suffix
# - parent directory


# ============================================================
# Practice 11 - Path Checks
# ============================================================
# Check whether data/raw/sales.csv exists.
# Check whether it is a file.
# Check whether data/raw is a directory.


# ============================================================
# Practice 12 - Create Directories
# ============================================================
# Create this directory structure if it does not already exist:
# data/raw
# data/processed
#
# Use pathlib and mkdir().


# ============================================================
# Practice 13 - CSV Writing
# ============================================================
# Create customers.csv with these records:
#
# id,name,city
# 101,Onkar,Pune
# 102,Rahul,Mumbai
# 103,Amit,Nashik
#
# Use csv.DictWriter.


# ============================================================
# Practice 14 - CSV Reading
# ============================================================
# Read customers.csv using csv.DictReader.
# Print each customer's name and city.


# ============================================================
# Practice 15 - JSON Writing
# ============================================================
# Create customer.json containing:
# id
# name
# skills
#
# Use json.dump().


# ============================================================
# Practice 16 - JSON Reading
# ============================================================
# Read customer.json using json.load().
# Print the customer's name and first skill.


# ============================================================
# Practice 17 - load vs loads
# ============================================================
# Explain the difference between:
# json.load()
# json.loads()
# json.dump()
# json.dumps()


# ============================================================
# Practice 18 - Missing File
# ============================================================
# Try to read missing.csv.
# Handle FileNotFoundError.


# ============================================================
# Practice 19 - File Size
# ============================================================
# Use pathlib to print the size of notes.txt in bytes.


# ============================================================
# Practice 20 - Large File Processing
# ============================================================
# Assume large.log contains millions of lines.
# Write code that processes one line at a time.
# Do not use read() or readlines().


# ============================================================
# Practice 21 - Data Cleaning
# ============================================================
# Read names.txt line by line.
# Remove surrounding whitespace.
# Write cleaned names to cleaned_names.txt.


# ============================================================
# Practice 22 - Data Engineering Scenario
# ============================================================
# You receive daily CSV files in:
# incoming/
#
# Write a program that:
# 1. Checks whether the file exists.
# 2. Reads it using csv.DictReader.
# 3. Counts records.
# 4. Prints the count.
# 5. Handles FileNotFoundError.


# ============================================================
# Practice 23 - Data Engineering Scenario
# ============================================================
# A source file contains an amount column.
# Process it line by line and identify records where amount
# cannot be converted to float.
# Do not crash the complete processing loop.


# ============================================================
# Practice 24 - Interview Output Prediction
# ============================================================
# Assume example.txt initially contains:
# Hello
# World
#
# What will the file contain after this code?
#
# with open("example.txt", "w") as file:
#     file.write("Python")


# ============================================================
# Practice 25 - Interview Challenge
# ============================================================
# Design a file-ingestion function that accepts a file path and:
# 1. Validates that the path is a file.
# 2. Reads the file incrementally.
# 3. Handles missing files.
# 4. Handles decoding errors.
# 5. Counts successfully processed lines.
# 6. Returns the final count.
