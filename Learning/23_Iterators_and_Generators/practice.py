# 🐍 Day 23 - Iterators and Generators | Practice

# Solve each problem yourself before checking the README.

# ============================================================
# Practice 1 - Iterable
# ============================================================
# Create a list of five numbers and iterate over it using a for loop.


# ============================================================
# Practice 2 - Create an Iterator
# ============================================================
# Convert the list below into an iterator using iter().
# Call next() three times.

numbers = [10, 20, 30]


# ============================================================
# Practice 3 - StopIteration
# ============================================================
# Create an iterator containing two values.
# Call next() three times and observe what happens.


# ============================================================
# Practice 4 - Default Value
# ============================================================
# Use next(iterator, default) so that an exhausted iterator
# returns "Done" instead of raising StopIteration.


# ============================================================
# Practice 5 - Iterable vs Iterator
# ============================================================
# Determine which of these are iterables and which are iterators:
# list
# tuple
# string
# list_iterator
# generator
#
# Explain your answer.


# ============================================================
# Practice 6 - Manual for Loop
# ============================================================
# Recreate the behavior of a simple for loop using:
# iter()
# next()
# try
# except StopIteration


# ============================================================
# Practice 7 - Custom Iterator
# ============================================================
# Create a CountDown iterator that produces:
# 5, 4, 3, 2, 1
# and then raises StopIteration.


# ============================================================
# Practice 8 - Generator Function
# ============================================================
# Create a generator that yields:
# 10
# 20
# 30


# ============================================================
# Practice 9 - Generator with range()
# ============================================================
# Create a generator that yields numbers from 1 to 10.


# ============================================================
# Practice 10 - Generator Execution
# ============================================================
# Predict the output before running:
#
# def demo():
#     print("A")
#     yield 1
#     print("B")
#     yield 2
#
# generator = demo()
# print("C")
# print(next(generator))
# print(next(generator))


# ============================================================
# Practice 11 - Generator Expression
# ============================================================
# Create a generator expression that produces the squares of
# numbers from 1 to 10.


# ============================================================
# Practice 12 - List vs Generator
# ============================================================
# Create both:
# 1. A list of squares from 1 to 1,000,000.
# 2. A generator expression for the same values.
#
# Explain which one stores all values immediately.


# ============================================================
# Practice 13 - Even Number Generator
# ============================================================
# Create a generator that receives a collection and yields only
# even numbers.


# ============================================================
# Practice 14 - Filter Generator
# ============================================================
# Create a generator that receives numbers and yields only values
# greater than 50.


# ============================================================
# Practice 15 - yield from
# ============================================================
# Create two generators:
# first() → 1, 2, 3
# second() → 4, 5, 6
#
# Create a third generator using yield from to combine them.


# ============================================================
# Practice 16 - File Generator
# ============================================================
# Create read_lines(file_path) that opens a text file and yields
# one cleaned line at a time.


# ============================================================
# Practice 17 - CSV Generator
# ============================================================
# Create a generator that reads a CSV file with csv.DictReader
# and yields one dictionary row at a time.


# ============================================================
# Practice 18 - Data Cleaning Generator
# ============================================================
# Given:

names = [" onkar ", " RAHUL ", " amit "]

# Create a generator that cleans every name using strip() and title().


# ============================================================
# Practice 19 - Transformation Pipeline
# ============================================================
# Create three generator stages:
#
# extract()
# transform()
# filter()
#
# Connect them so that records flow through the pipeline one at a time.


# ============================================================
# Practice 20 - Large Dataset
# ============================================================
# Assume you have 50 million IDs.
# Explain why this can be problematic:
#
# ids = [i for i in range(50_000_000)]
#
# Then design a generator-based alternative.


# ============================================================
# Practice 21 - Generator Exhaustion
# ============================================================
# Create a generator, consume it completely, and then try to
# consume it again.
# Explain why the second attempt produces no values.


# ============================================================
# Practice 22 - Generator and Exceptions
# ============================================================
# Create a generator that raises ValueError when it encounters
# a negative number.
# Handle the exception while consuming the generator.


# ============================================================
# Practice 23 - send()
# ============================================================
# Create a generator that waits for a value using yield and
# receives a value using send().
#
# Demonstrate the correct initialization sequence.


# ============================================================
# Practice 24 - Interview Question
# ============================================================
# Explain:
#
# Every iterator is iterable, but every iterable is not an iterator.
#
# Give a Python example proving the statement.


# ============================================================
# Practice 25 - Interview Challenge
# ============================================================
# Build a generator-based mini ETL pipeline:
#
# 1. Extract records from a list.
# 2. Clean the records.
# 3. Filter invalid records.
# 4. Transform valid records.
# 5. Print the final records.
#
# Do not create a list containing all intermediate results.
