# 🐍 Day 22 - File Handling | Examples

from pathlib import Path
import csv
import json

# ============================================================
# 1. Write a Text File
# ============================================================

with open("example.txt", "w", encoding="utf-8") as file:
    # Write one line to the file.
    file.write("Python File Handling\n")

    # Write another line to the file.
    file.write("Data Engineering\n")


# ============================================================
# 2. Read the Entire File
# ============================================================

with open("example.txt", "r", encoding="utf-8") as file:
    # Read the entire file into one string.
    content = file.read()

# Print the complete file content.
print(content)


# ============================================================
# 3. Read One Line at a Time
# ============================================================

with open("example.txt", "r", encoding="utf-8") as file:
    # Read the first line.
    first_line = file.readline()

    # Read the second line.
    second_line = file.readline()

# strip() removes surrounding whitespace including the newline.
print(first_line.strip())
print(second_line.strip())


# ============================================================
# 4. Read All Lines
# ============================================================

with open("example.txt", "r", encoding="utf-8") as file:
    # Store every remaining line in a list.
    lines = file.readlines()

# Print the list of lines.
print(lines)


# ============================================================
# 5. Iterate Through a File
# ============================================================

with open("example.txt", "r", encoding="utf-8") as file:
    # Read the file incrementally, one line at a time.
    for line in file:
        # Remove the newline before printing.
        print(line.strip())


# ============================================================
# 6. Append to a File
# ============================================================

with open("example.txt", "a", encoding="utf-8") as file:
    # Append new content without replacing the existing content.
    file.write("Snowflake\n")


# ============================================================
# 7. pathlib Path
# ============================================================

# Create a path object representing a CSV file.
path = Path("data") / "sales.csv"

# Print the complete path.
print(path)

# Print only the file name.
print(path.name)

# Print the file extension.
print(path.suffix)

# Print the parent directory.
print(path.parent)


# ============================================================
# 8. Check Path Information
# ============================================================

path = Path("example.txt")

# Check whether the path exists.
print(path.exists())

# Check whether the path points to a regular file.
print(path.is_file())

# Check whether the path points to a directory.
print(path.is_dir())


# ============================================================
# 9. Create Directories
# ============================================================

output_path = Path("output/raw")

# Create missing parent directories and avoid an error if they exist.
output_path.mkdir(parents=True, exist_ok=True)

# Confirm that the directory now exists.
print(output_path.exists())


# ============================================================
# 10. Write Multiple Lines
# ============================================================

lines = [
    "Python\n",
    "SQL\n",
    "Snowflake\n"
]

with open("skills.txt", "w", encoding="utf-8") as file:
    # Write all strings exactly as supplied.
    file.writelines(lines)


# ============================================================
# 11. CSV Writing
# ============================================================

rows = [
    {"id": 101, "name": "Onkar", "amount": 500},
    {"id": 102, "name": "Rahul", "amount": 700}
]

with open("customers.csv", "w", newline="", encoding="utf-8") as file:
    # Define the CSV columns.
    fieldnames = ["id", "name", "amount"]

    # Create a dictionary-based CSV writer.
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row.
    writer.writeheader()

    # Write all customer records.
    writer.writerows(rows)


# ============================================================
# 12. CSV Reading
# ============================================================

with open("customers.csv", "r", newline="", encoding="utf-8") as file:
    # Read each CSV row as a dictionary.
    reader = csv.DictReader(file)

    # Process one record at a time.
    for row in reader:
        # Print the customer name.
        print(row["name"])


# ============================================================
# 13. JSON Writing
# ============================================================

customer = {
    "id": 101,
    "name": "Onkar",
    "skills": ["SQL", "Python", "Snowflake"]
}

with open("customer.json", "w", encoding="utf-8") as file:
    # Serialize the Python dictionary into JSON and write it to the file.
    json.dump(customer, file, indent=4)


# ============================================================
# 14. JSON Reading
# ============================================================

with open("customer.json", "r", encoding="utf-8") as file:
    # Convert JSON file content into a Python object.
    data = json.load(file)

# Access a field from the resulting dictionary.
print(data["name"])


# ============================================================
# 15. JSON String vs JSON File
# ============================================================

json_text = '{"id": 101, "name": "Onkar"}'

# loads() converts a JSON string into a Python object.
record = json.loads(json_text)

# Print the converted dictionary.
print(record)

# dumps() converts a Python object into a JSON string.
json_output = json.dumps(record, indent=4)

# Print the JSON string.
print(json_output)


# ============================================================
# 16. Handle Missing File
# ============================================================

try:
    # Try to open a file that may not exist.
    with open("missing.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    # Handle the missing input file.
    print("missing.txt was not found")


# ============================================================
# 17. Handle Encoding Problems
# ============================================================

try:
    # Explicitly request UTF-8 while reading text.
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
except UnicodeDecodeError:
    # Handle data that cannot be decoded using the selected encoding.
    print("File encoding could not be decoded as UTF-8")


# ============================================================
# 18. File Size
# ============================================================

path = Path("example.txt")

if path.exists():
    # stat().st_size returns the file size in bytes.
    print("Size:", path.stat().st_size)


# ============================================================
# 19. Large File Pattern
# ============================================================

with open("example.txt", "r", encoding="utf-8") as file:
    # Iterate through the file instead of loading everything into memory.
    for line in file:
        # Process each line independently.
        cleaned_line = line.strip()

        # Print the processed line.
        print(cleaned_line)


# ============================================================
# 20. Data Engineering - Simple Pipeline
# ============================================================

input_path = Path("input.txt")
output_path = Path("cleaned_output.txt")

# Create sample input data for the demonstration.
with open(input_path, "w", encoding="utf-8") as file:
    file.write("  Onkar  \n")
    file.write("  Rahul  \n")
    file.write("  Amit  \n")

# Open the input and output files together.
with open(input_path, "r", encoding="utf-8") as source:
    with open(output_path, "w", encoding="utf-8") as target:
        # Process each source line independently.
        for line in source:
            # Remove surrounding whitespace.
            cleaned = line.strip()

            # Write the cleaned value to the destination.
            target.write(cleaned + "\n")

# Confirm the output file exists.
print(output_path.exists())
