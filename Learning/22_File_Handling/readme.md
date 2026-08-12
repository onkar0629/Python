# 🐍 Day 22 - File Handling

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Level](https://img.shields.io/badge/Level-Intermediate-success)

---

## Overview

Data Engineers work with files constantly.

Data can arrive as:

- CSV files
- Text files
- JSON files
- Log files
- Configuration files
- Temporary files
- Exported reports

Python provides built-in tools for reading, writing, updating, and managing files.

The most important concepts are:

- `open()`
- File modes
- Reading files
- Writing files
- Appending files
- `with` statement
- File paths
- `pathlib`
- CSV handling
- JSON handling
- File existence checks
- Exceptions during file operations
- Large-file processing

> [!IMPORTANT]
> In Data Engineering, file handling is not just about opening a file. You also need to think about **resource management, encoding, file paths, scalability, error handling, and data quality**.

---

## Table of Contents

- [1. What Is File Handling?](#1-what-is-file-handling)
- [2. Opening a File](#2-opening-a-file)
- [3. File Modes](#3-file-modes)
- [4. Reading a File](#4-reading-a-file)
- [5. read()](#5-read)
- [6. readline()](#6-readline)
- [7. readlines()](#7-readlines)
- [8. Iterating Through a File](#8-iterating-through-a-file)
- [9. Writing a File](#9-writing-a-file)
- [10. Appending to a File](#10-appending-to-a-file)
- [11. The with Statement](#11-the-with-statement)
- [12. File Encoding](#12-file-encoding)
- [13. File Paths](#13-file-paths)
- [14. pathlib](#14-pathlib)
- [15. Checking File Existence](#15-checking-file-existence)
- [16. Creating Directories](#16-creating-directories)
- [17. CSV Files](#17-csv-files)
- [18. JSON Files](#18-json-files)
- [19. File Exceptions](#19-file-exceptions)
- [20. Large Files](#20-large-files)
- [21. File Metadata](#21-file-metadata)
- [22. Common Mistakes](#22-common-mistakes)
- [23. Interview Follow-up Questions](#23-interview-follow-up-questions)
- [24. Data Engineering Perspective](#24-data-engineering-perspective)

---

# 1. What Is File Handling?

File handling means interacting with files stored on disk.

Typical operations are:

```text
Create
  ↓
Open
  ↓
Read / Write
  ↓
Close
```

Python provides the `open()` function for file access.

Example:

```python
file = open("data.txt", "r")
```

This opens `data.txt` in read mode.

However, manually managing the file is usually not the best approach. The preferred pattern is the `with` statement, which automatically closes the file.

---

# 2. Opening a File

Basic syntax:

```python
open(file, mode)
```

Example:

```python
file = open("data.txt", "r")
```

Here:

```text
data.txt → file path
r         → read mode
```

To read the content:

```python
content = file.read()
```

Then close it:

```python
file.close()
```

Again, in normal application code prefer:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

---

# 3. File Modes

The most important modes are:

| Mode | Meaning |
|---|---|
| `r` | Read |
| `w` | Write / overwrite |
| `a` | Append |
| `x` | Create a new file, fail if it exists |
| `b` | Binary mode |
| `t` | Text mode |
| `+` | Read and write |

Common combinations:

```text
rb → read binary
wb → write binary
r+ → read and write
w+ → write and read, truncating first
```

### Important Difference

`w` can destroy existing content.

Example:

```python
with open("data.txt", "w") as file:
    file.write("New data")
```

If `data.txt` already contains information, its existing content is replaced.

`a` preserves existing content and adds new content at the end.

---

# 4. Reading a File

Suppose `data.txt` contains:

```text
Python
SQL
Snowflake
```

We can read it using:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

Then:

```python
print(content)
```

The entire file is loaded into memory as a string.

This is convenient for small files.

For very large files, loading everything at once may consume too much memory.

---

# 5. `read()`

`read()` returns file content as a string in text mode.

```python
with open("data.txt", "r") as file:
    content = file.read()
```

We can also specify the number of characters to read:

```python
with open("data.txt", "r") as file:
    content = file.read(10)
```

This reads up to 10 characters from the current file position.

---

# 6. `readline()`

`readline()` reads one line at a time.

```python
with open("data.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
```

This can be useful when processing records line by line.

However, for normal iteration over a large text file, simply using:

```python
for line in file:
    ...
```

is generally clearer and memory-efficient.

---

# 7. `readlines()`

`readlines()` reads the remaining lines and returns them as a list.

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
```

If the file contains:

```text
Python
SQL
Snowflake
```

we get approximately:

```python
["Python\n", "SQL\n", "Snowflake\n"]
```

The newline character is part of each line when present in the file.

> [!WARNING]
> `readlines()` stores all lines in memory. Avoid it for very large files when you can process the file incrementally.

---

# 8. Iterating Through a File

A common scalable pattern is:

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

Python reads the file incrementally rather than creating a list containing the entire file.

This is useful for large log files and line-oriented data.

Conceptually:

```text
Large file
   ↓
Read one line
   ↓
Process line
   ↓
Read next line
   ↓
Process line
```

This is much more memory-friendly than:

```python
lines = file.readlines()
```

for very large files.

---

# 9. Writing a File

Use `w` mode:

```python
with open("output.txt", "w") as file:
    file.write("Hello Python")
```

If the file does not exist, Python creates it.

If it exists, `w` truncates the existing content before writing.

To write multiple lines:

```python
lines = ["Python\n", "SQL\n", "Snowflake\n"]

with open("output.txt", "w") as file:
    file.writelines(lines)
```

`writelines()` does not automatically add newline characters, so the strings need `\n` where appropriate.

---

# 10. Appending to a File

Use `a` mode when we want to preserve existing content.

```python
with open("log.txt", "a") as file:
    file.write("Pipeline completed\n")
```

If the file already contains:

```text
Pipeline started
```

the new content is added after it.

This is commonly useful for simple text logs, although production systems normally use Python's `logging` module or centralized logging rather than manually appending log messages to files.

---

# 11. The `with` Statement

The recommended file-handling pattern is:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

Why?

Because the context manager handles cleanup automatically.

Without `with`:

```python
file = open("data.txt", "r")
try:
    content = file.read()
finally:
    file.close()
```

With `with`, Python manages the closing operation for us.

This is safer and cleaner.

> [!IMPORTANT]
> The `with` statement is not specific to files. It is a general context-manager mechanism used to acquire and release resources safely.

---

# 12. File Encoding

Text files have an encoding.

A common choice is UTF-8:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

When writing:

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello")
```

Explicitly specifying encoding makes behavior more predictable across machines and environments.

This becomes important when processing international text.

---

# 13. File Paths

A file path identifies where a file is located.

Relative path:

```text
data/sales.csv
```

Absolute path examples vary by operating system:

```text
macOS/Linux:
/home/user/data/sales.csv

Windows:
C:\data\sales.csv
```

Hard-coding machine-specific absolute paths can make projects difficult to move between environments.

Prefer configurable or relative paths where appropriate.

---

# 14. `pathlib`

`pathlib` provides an object-oriented way to work with paths.

```python
from pathlib import Path

path = Path("data") / "sales.csv"
```

This is preferable to manually concatenating strings:

```python
"data/" + "sales.csv"
```

`Path` handles platform-specific path separators appropriately.

Useful methods include:

```python
path.exists()
path.is_file()
path.is_dir()
path.name
path.suffix
path.parent
```

Example:

```python
path = Path("data/sales.csv")

print(path.name)
print(path.suffix)
print(path.parent)
```

---

# 15. Checking File Existence

Using `pathlib`:

```python
from pathlib import Path

path = Path("data.txt")

if path.exists():
    print("File exists")
else:
    print("File does not exist")
```

We can specifically check whether it is a file:

```python
if path.is_file():
    print("This is a file")
```

And a directory:

```python
if path.is_dir():
    print("This is a directory")
```

> [!TIP]
> Existence checks can still race with filesystem changes. If the next operation is the real operation you need to perform, often it is better to perform it and handle the relevant exception rather than relying only on a prior existence check.

---

# 16. Creating Directories

Create a directory with `Path.mkdir()`:

```python
from pathlib import Path

path = Path("data/raw")
path.mkdir(parents=True, exist_ok=True)
```

Meaning:

```text
parents=True
→ create missing parent directories

exist_ok=True
→ do not fail if the directory already exists
```

This is useful for preparing pipeline output directories.

---

# 17. CSV Files

CSV means **Comma-Separated Values**.

Example:

```text
id,name,amount
101,Onkar,500
102,Rahul,700
```

Python provides the `csv` module.

Reading:

```python
import csv

with open("sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

`DictReader` represents each row as a dictionary using the header names as keys.

Writing:

```python
import csv

rows = [
    {"id": 101, "name": "Onkar"},
    {"id": 102, "name": "Rahul"}
]

with open("customers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name"])

    writer.writeheader()
    writer.writerows(rows)
```

For larger production workflows, specialized tools such as pandas or distributed processing frameworks may be more appropriate depending on data volume and architecture.

---

# 18. JSON Files

JSON is common in APIs and configuration/data exchange.

Example JSON:

```json
{
    "id": 101,
    "name": "Onkar",
    "skills": ["SQL", "Python"]
}
```

Python's `json` module can read it.

```python
import json

with open("customer.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

Now `data` is a Python object, typically a dictionary.

To write JSON:

```python
with open("customer.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
```

Important distinction:

```text
json.load(file)
→ JSON file → Python object

json.loads(text)
→ JSON string → Python object

json.dump(data, file)
→ Python object → JSON file

json.dumps(data)
→ Python object → JSON string
```

---

# 19. File Exceptions

File operations can fail.

Example:

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

Other possible exceptions include:

- `PermissionError`
- `IsADirectoryError`
- `NotADirectoryError`
- `UnicodeDecodeError`
- `OSError`

Handle only the failures you can meaningfully recover from.

For example, if a required source file is missing, silently continuing may cause downstream data problems. The correct response may be to fail the pipeline and alert the operator.

---

# 20. Large Files

Suppose a file is 20 GB.

This approach may be problematic:

```python
with open("large.log", "r") as file:
    data = file.read()
```

The entire file is requested at once.

A better approach for line-oriented processing is:

```python
with open("large.log", "r", encoding="utf-8") as file:
    for line in file:
        process(line)
```

The processing model becomes:

```text
20 GB file
   ↓
One line / chunk
   ↓
Process
   ↓
Next line / chunk
```

This reduces peak memory usage.

For truly large datasets, however, local Python file iteration may still not be enough. Data Engineers may use object storage, distributed processing, columnar formats, streaming systems, or warehouse-native ingestion depending on the architecture.

---

# 21. File Metadata

`pathlib` can also inspect file metadata.

```python
from pathlib import Path

path = Path("data.txt")

if path.exists():
    print(path.stat().st_size)
```

`stat()` provides filesystem metadata.

Other useful information can include:

- File size
- Modification time
- Access time
- Metadata supported by the operating system

This can be useful for pipeline checks such as detecting unexpectedly empty files.

---

# 22. Common Mistakes

## Mistake 1: Forgetting to Close a File

Manual pattern:

```python
file = open("data.txt")
```

If you manage the file manually, you need to close it.

Prefer:

```python
with open("data.txt") as file:
    ...
```

---

## Mistake 2: Using `w` When You Need `a`

`w` overwrites existing content.

`a` appends to existing content.

Always verify the required behavior before writing.

---

## Mistake 3: Loading Huge Files with `read()`

For large files, process incrementally when possible.

---

## Mistake 4: Ignoring Encoding

A file may work on one machine and fail on another because of encoding differences.

Prefer explicit encoding such as:

```python
encoding="utf-8"
```

when appropriate.

---

## Mistake 5: Hard-Coding Absolute Paths

Avoid paths such as:

```text
/Users/onkar/Desktop/project/data.csv
```

inside reusable production code.

Use configuration, environment variables, or project-relative paths as appropriate.

---

## Mistake 6: Checking Existence and Assuming the File Cannot Change

A file may be removed or changed after an existence check.

For critical operations, handle the actual operation's exceptions too.

---

# 23. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is the difference between `r`, `w`, and `a` file modes?

<details>
<summary><strong>Answer</strong></summary>

`r` opens a file for reading. The file normally must already exist.

```python
open("data.txt", "r")
```

`w` opens a file for writing. It creates the file if necessary and truncates existing content.

```python
open("data.txt", "w")
```

`a` opens a file for appending. Existing content is preserved and new writes are added at the end.

```python
open("data.txt", "a")
```

The key interview point is:

```text
r → read
w → write / overwrite
 a → append
```

</details>

---

### Q2. Why is the `with open(...)` pattern preferred?

<details>
<summary><strong>Answer</strong></summary>

The `with` statement uses a context manager to ensure the file resource is released when the block exits, including when an exception occurs.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

This is safer and cleaner than manually opening and closing the file.

It also demonstrates an important Python concept: context managers provide controlled resource acquisition and cleanup.

</details>

---

### Q3. What is the difference between `read()`, `readline()`, and `readlines()`?

<details>
<summary><strong>Answer</strong></summary>

`read()` reads content from the current position and returns a string in text mode.

```python
content = file.read()
```

`readline()` reads one line.

```python
line = file.readline()
```

`readlines()` reads the remaining lines and returns them as a list.

```python
lines = file.readlines()
```

For large line-oriented files, iterating directly over the file is usually more memory-efficient than loading all lines into a list.

</details>

---

### Q4. How would you process a 20 GB text file using Python?

<details>
<summary><strong>Answer</strong></summary>

I would avoid loading the entire file into memory with `read()`.

For line-oriented processing:

```python
with open("large.log", "r", encoding="utf-8") as file:
    for line in file:
        process(line)
```

This processes the file incrementally and keeps peak memory usage much lower.

For truly large production workloads, I would also consider whether the data should be processed through distributed systems, object-storage-native tools, streaming infrastructure, or a warehouse ingestion mechanism rather than a single-machine Python process.

</details>

---

### Q5. Why would you use `pathlib` instead of string concatenation for file paths?

<details>
<summary><strong>Answer</strong></summary>

`pathlib` provides an object-oriented and platform-aware way to work with paths.

```python
from pathlib import Path

path = Path("data") / "sales.csv"
```

It avoids manually handling path separators and provides useful methods such as:

```python
path.exists()
path.is_file()
path.suffix
path.parent
```

This makes path-related code cleaner and more portable.

</details>

---

### Q6. What is the difference between `json.load()` and `json.loads()`?

<details>
<summary><strong>Answer</strong></summary>

`json.load()` reads JSON from a file-like object.

```python
with open("data.json", "r") as file:
    data = json.load(file)
```

`json.loads()` parses a JSON string.

```python
data = json.loads('{"id": 101}')
```

Similarly:

```text
load   → file → Python object
loads  → string → Python object

dump   → Python object → file
dumps  → Python object → string
```

</details>

---

### Q7. How would you handle a missing input file in a production pipeline?

<details>
<summary><strong>Answer</strong></summary>

It depends on the business requirement.

If the file is optional, I may log the condition and continue.

If it is a required input, I would generally fail the relevant pipeline task clearly rather than silently continuing with incomplete data.

For example:

```python
try:
    with open("sales.csv", "r", encoding="utf-8") as file:
        process(file)
except FileNotFoundError as error:
    logger.exception("Required input file is missing")
    raise
```

The key is to make the failure observable and prevent downstream systems from treating incomplete data as successful processing.

</details>

---

### Q8. How would you safely write a large output file?

<details>
<summary><strong>Answer</strong></summary>

I would avoid building the entire output in memory first.

Instead, write incrementally:

```python
with open("output.txt", "w", encoding="utf-8") as file:
    for record in records:
        file.write(format_record(record))
```

For structured data, I would use an appropriate streaming writer or serialization library.

In larger Data Engineering systems, I would also consider partitioning, compression, object storage, and columnar formats such as Parquet depending on downstream requirements.

</details>

---

# 24. Data Engineering Perspective

File handling is a foundation for batch ingestion pipelines.

A common flow is:

```text
Source System
     ↓
CSV / JSON / Log File
     ↓
File Validation
     ↓
Python Ingestion
     ↓
Transformation
     ↓
Warehouse / Data Lake
```

For example:

```text
incoming/
├── sales_2026_08_12.csv
├── customers_2026_08_12.csv
└── products_2026_08_12.csv
```

A Python pipeline can:

1. Detect incoming files.
2. Validate that files exist.
3. Read records incrementally.
4. Validate required columns.
5. Transform values.
6. Write clean output.
7. Move or archive processed files.
8. Log failures.

### Example Architecture

```text
              ┌──────────────┐
              │ Incoming CSV │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │ File Check   │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │ Read Chunks  │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │ Validate     │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │ Transform    │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │ Load         │
              └──────────────┘
```

The important engineering considerations are:

```text
Correctness
   +
Memory efficiency
   +
Error handling
   +
Encoding
   +
Portability
   +
Observability
```

> [!IMPORTANT]
> File handling is one of the places where Python fundamentals directly connect to Data Engineering. You should be comfortable explaining not only **how to read a file**, but also **how to process large files safely, handle failures, and avoid unnecessary memory usage**.

---

## Navigation

⬅️ **Previous:** [Day 21 - Exception Handling](../Day_21_Exception_Handling/readme.md)

➡️ **Next:** [Day 23 - Iterators and Generators](../Day_23_Iterators_and_Generators/readme.md)
