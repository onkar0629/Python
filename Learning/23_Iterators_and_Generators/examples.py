# 🐍 Day 23 - Iterators and Generators | Examples

# ============================================================
# 1. Iterable and Iterator
# ============================================================

numbers = [10, 20, 30]

# Convert the list into an iterator.
iterator = iter(numbers)

# Request the first value from the iterator.
print(next(iterator))

# Request the second value.
print(next(iterator))

# Request the third value.
print(next(iterator))


# ============================================================
# 2. next() with a Default Value
# ============================================================

numbers = [100, 200]
iterator = iter(numbers)

# Consume the first value.
print(next(iterator))

# Consume the second value.
print(next(iterator))

# Return the default instead of raising StopIteration.
print(next(iterator, "No more values"))


# ============================================================
# 3. for Loop Uses Iteration
# ============================================================

numbers = [1, 2, 3]

# The for loop obtains an iterator internally and consumes it.
for number in numbers:
    print(number)


# ============================================================
# 4. Manual Iterator Loop
# ============================================================

numbers = [5, 10, 15]
iterator = iter(numbers)

while True:
    try:
        # Ask the iterator for the next value.
        number = next(iterator)

        # Process the current value.
        print(number)
    except StopIteration:
        # Stop when the iterator has no more values.
        break


# ============================================================
# 5. Custom Iterator
# ============================================================

class CountUpTo:
    def __init__(self, limit):
        # Store the maximum value.
        self.limit = limit

        # Start counting from one.
        self.current = 1

    def __iter__(self):
        # An iterator returns itself from __iter__().
        return self

    def __next__(self):
        # Stop when the current value exceeds the limit.
        if self.current > self.limit:
            raise StopIteration

        # Save the current value before changing the state.
        value = self.current

        # Move the iterator to the next value.
        self.current += 1

        # Return the saved value.
        return value


counter = CountUpTo(3)

# Consume the custom iterator with a for loop.
for number in counter:
    print(number)


# ============================================================
# 6. Basic Generator
# ============================================================

def generate_numbers():
    # Produce the first value and pause execution.
    yield 1

    # Resume here when next() is called again.
    yield 2

    # Produce the final value.
    yield 3


# Calling a generator function creates a generator object.
generator = generate_numbers()

# Request the first generated value.
print(next(generator))

# Resume the generator and request the second value.
print(next(generator))

# Resume the generator and request the third value.
print(next(generator))


# ============================================================
# 7. Generator with a Loop
# ============================================================

def squares(limit):
    # Generate numbers from zero up to limit - 1.
    for number in range(limit):
        # Calculate the square only when the value is requested.
        yield number * number


# Create a lazy generator.
generator = squares(5)

# Consume generated values one at a time.
for value in generator:
    print(value)


# ============================================================
# 8. Generator Execution State
# ============================================================

def demo():
    # This message is printed when execution reaches the first yield.
    print("Step 1")

    # Pause the generator and return 10.
    yield 10

    # This runs only when the generator is resumed.
    print("Step 2")

    # Pause again and return 20.
    yield 20


# Create the generator without executing its body completely.
generator = demo()

# Resume execution until the first yield.
print(next(generator))

# Resume execution until the second yield.
print(next(generator))


# ============================================================
# 9. Generator Expression
# ============================================================

# Create a generator expression instead of a list.
squares = (number * number for number in range(5))

# Consume the generator lazily.
for square in squares:
    print(square)


# ============================================================
# 10. List Comprehension vs Generator Expression
# ============================================================

# This creates all values immediately.
list_values = [number * number for number in range(5)]

# This produces values lazily.
generator_values = (number * number for number in range(5))

# Show the list object.
print(list_values)

# Show the generator object.
print(generator_values)


# ============================================================
# 11. yield from
# ============================================================

def first_numbers():
    # Yield the first group of values.
    yield 1
    yield 2


def second_numbers():
    # Yield the second group of values.
    yield 3
    yield 4


def combined_numbers():
    # Delegate iteration to the first generator.
    yield from first_numbers()

    # Delegate iteration to the second generator.
    yield from second_numbers()


# Consume both generators through one combined generator.
for number in combined_numbers():
    print(number)


# ============================================================
# 12. Generator for File Processing
# ============================================================

def read_lines(file_path):
    # Open the file safely using a context manager.
    with open(file_path, "r", encoding="utf-8") as file:
        # Read one line at a time.
        for line in file:
            # Remove surrounding whitespace and yield the cleaned line.
            yield line.strip()


# Consume lines only when they are requested.
# Uncomment after creating data.txt.
# for line in read_lines("data.txt"):
#     print(line)


# ============================================================
# 13. Generator for Data Cleaning
# ============================================================

def clean_names(names):
    # Process one name at a time.
    for name in names:
        # Remove surrounding whitespace and normalize capitalization.
        cleaned_name = name.strip().title()

        # Produce the cleaned name lazily.
        yield cleaned_name


names = [" onkar ", " rahul ", " amit "]

# Consume cleaned names one at a time.
for name in clean_names(names):
    print(name)


# ============================================================
# 14. Generator with Filtering
# ============================================================

def even_numbers(numbers):
    # Examine each input number.
    for number in numbers:
        # Produce only even numbers.
        if number % 2 == 0:
            yield number


numbers = range(1, 11)

# Process only the values produced by the generator.
for number in even_numbers(numbers):
    print(number)


# ============================================================
# 15. Generator Expression with sum()
# ============================================================

numbers = range(1, 1_000_001)

# Generate each square only as sum() consumes it.
total = sum(number * number for number in numbers)

# Print the final result.
print(total)


# ============================================================
# 16. Generator Exception Handling
# ============================================================

def safe_numbers():
    # Generate values until an invalid value is reached.
    for number in range(5):
        if number == 3:
            # Raise a domain error when the invalid value is reached.
            raise ValueError("3 is not allowed")

        # Yield valid values.
        yield number


try:
    # Consume the generator.
    for number in safe_numbers():
        print(number)
except ValueError as error:
    # Handle the generator's exception.
    print("Generator error:", error)


# ============================================================
# 17. Generator Receiving a Value with send()
# ============================================================

def receiver():
    # Pause immediately and wait for a value from send().
    value = yield

    # Process the value sent into the generator.
    print("Received:", value)


# Create the generator object.
generator = receiver()

# Start the generator and move it to the first yield.
next(generator)

# Send a value into the paused generator.
generator.send(100)


# ============================================================
# 18. Data Engineering Pipeline Generator
# ============================================================

def extract_records(records):
    # Produce each source record one at a time.
    for record in records:
        yield record


def transform_records(records):
    # Consume records from the previous stage one at a time.
    for record in records:
        # Create a transformed record without storing all results.
        transformed = record.upper()

        # Pass the transformed record to the next stage.
        yield transformed


def load_records(records):
    # Consume transformed records one at a time.
    for record in records:
        # Simulate loading the record into a destination.
        print("Loading:", record)


source_records = ["customer_a", "customer_b", "customer_c"]

# Build the lazy extraction stage.
extracted = extract_records(source_records)

# Build the lazy transformation stage.
transformed = transform_records(extracted)

# Consume the pipeline and load records as they are produced.
load_records(transformed)
