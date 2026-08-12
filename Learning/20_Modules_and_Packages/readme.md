# 🐍 Day 20 - Modules and Packages

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Level](https://img.shields.io/badge/Level-Intermediate-success)

---

## Overview

As Python programs become larger, putting everything into one file becomes difficult to maintain.

Python solves this problem through **modules** and **packages**.

A module is a Python file containing reusable code. A package is a directory used to organize related modules.

For example:

```text
project/
├── main.py
├── database.py
├── transformations.py
└── utils/
    ├── __init__.py
    ├── cleaning.py
    └── validation.py
```

Instead of rewriting the same function in multiple files, we can define it once and import it wherever it is required.

This is extremely important in Data Engineering because production projects commonly separate:

- Configuration
- Database connections
- Extraction logic
- Transformation logic
- Validation
- Logging
- Utility functions
- Pipeline orchestration

> [!IMPORTANT]
> A module is not just a way to "split code into files". Modules create reusable namespaces and help organize dependencies and responsibilities.

---

## Table of Contents

- [1. What Is a Module?](#1-what-is-a-module)
- [2. Why Modules Are Useful](#2-why-modules-are-useful)
- [3. Creating Your Own Module](#3-creating-your-own-module)
- [4. import](#4-import)
- [5. from import](#5-from-import)
- [6. import as](#6-import-as)
- [7. Importing Multiple Names](#7-importing-multiple-names)
- [8. Module Namespace](#8-module-namespace)
- [9. `__name__`](#9-name)
- [10. `if __name__ == "__main__"`](#10-if-name--main)
- [11. What Is a Package?](#11-what-is-a-package)
- [12. `__init__.py`](#12-initpy)
- [13. Absolute and Relative Imports](#13-absolute-and-relative-imports)
- [14. Standard Library Modules](#14-standard-library-modules)
- [15. Third-Party Packages](#15-third-party-packages)
- [16. pip](#16-pip)
- [17. Virtual Environments](#17-virtual-environments)
- [18. requirements.txt](#18-requirementstxt)
- [19. Import Errors](#19-import-errors)
- [20. Circular Imports](#20-circular-imports)
- [21. Common Mistakes](#21-common-mistakes)
- [22. Interview Follow-up Questions](#22-interview-follow-up-questions)
- [23. Data Engineering Perspective](#23-data-engineering-perspective)

---

# 1. What Is a Module?

A **module** is a Python file containing Python code.

Suppose we create:

```text
math_utils.py
```

Inside it:

```python
def add(a, b):
    return a + b
```

Now another file can import that function.

```python
import math_utils

print(math_utils.add(10, 20))
```

The file `math_utils.py` is a module.

A module can contain:

- Functions
- Classes
- Variables
- Constants
- Executable statements

The main purpose is **reusability and organization**.

---

# 2. Why Modules Are Useful

Without modules, a large application can become one huge file:

```text
main.py
    ↓
5000 lines
    ↓
Database code
Cleaning code
Validation code
Logging code
API code
Pipeline code
```

This becomes difficult to understand and test.

Modules allow separation:

```text
main.py
    ↓
Database module
Transformation module
Validation module
Logging module
```

Each module can have a clear responsibility.

### Benefits

- Reusability
- Maintainability
- Better testing
- Clear organization
- Namespace separation
- Easier collaboration
- Easier debugging

---

# 3. Creating Your Own Module

Create a file called:

```text
calculator.py
```

Add:

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b
```

Create another file:

```text
main.py
```

Then:

```python
import calculator

print(calculator.add(10, 20))
print(calculator.multiply(5, 4))
```

Python loads the module and makes its names available through the module namespace.

The dot operator is important:

```python
calculator.add
```

means:

```text
module → calculator
name   → add
```

---

# 4. `import`

The simplest form is:

```python
import math
```

Then use:

```python
print(math.sqrt(25))
```

Why not simply write `sqrt(25)`?

Because `sqrt` belongs to the `math` module namespace.

```text
math
 └── sqrt
```

Using `math.sqrt()` makes the source of the function explicit.

---

# 5. `from import`

We can import a specific name:

```python
from math import sqrt
```

Then:

```python
print(sqrt(25))
```

We no longer need `math.sqrt()` because `sqrt` has been imported directly into the current namespace.

We can import multiple names:

```python
from math import sqrt, ceil, floor
```

This can be convenient, but excessive direct imports can make it harder to see where a name came from.

---

# 6. `import as`

An imported module can be given an alias.

```python
import pandas as pd
```

Then:

```python
df = pd.DataFrame()
```

`pd` is simply another name referring to the imported module.

Common aliases include:

```text
pandas      → pd
numpy       → np
matplotlib.pyplot → plt
```

Aliases are useful when they are conventional and improve readability.

---

# 7. Importing Multiple Names

We can import several names from one module:

```python
from math import sqrt, factorial
```

Then:

```python
print(sqrt(16))
print(factorial(5))
```

Avoid importing everything using:

```python
from math import *
```

This places many names into the current namespace and can cause naming conflicts or make code harder to understand.

> [!TIP]
> Prefer explicit imports because they make dependencies easier to identify.

---

# 8. Module Namespace

A module creates its own namespace.

Suppose `calculator.py` contains:

```python
PI = 3.14159

def area(radius):
    return PI * radius ** 2
```

When imported:

```python
import calculator
```

we access:

```python
calculator.PI
calculator.area(5)
```

The module namespace prevents its names from automatically colliding with names in the importing file.

This is one reason `import module` is often clearer than importing everything directly.

---

# 9. `__name__`

Every Python module has a special variable called `__name__`.

When a file is run directly:

```bash
python script.py
```

Python sets:

```python
__name__ == "__main__"
```

When the same file is imported:

```python
import script
```

its `__name__` is normally the module name:

```text
script
```

This difference is extremely useful.

---

# 10. `if __name__ == "__main__"`

A common Python pattern is:

```python
def main():
    print("Program started")


if __name__ == "__main__":
    main()
```

Why use this?

Because we may want code to run when the file is executed directly, but **not run automatically when the file is imported**.

For example:

```text
python pipeline.py
```

should execute the pipeline.

But:

```python
import pipeline
```

should normally make the functions/classes available without automatically starting the pipeline.

> [!IMPORTANT]
> This pattern is one of the most common Python interview questions.

---

# 11. What Is a Package?

A package organizes related modules into a directory.

Example:

```text
utils/
├── __init__.py
├── cleaning.py
├── validation.py
└── formatting.py
```

Here:

```text
utils → package
cleaning.py → module
validation.py → module
formatting.py → module
```

A package gives a project a hierarchical structure.

For example:

```python
from utils.cleaning import clean_name
```

Read it as:

```text
utils
  ↓
cleaning
  ↓
clean_name
```

---

# 12. `__init__.py`

`__init__.py` is a special file associated with Python packages.

A package can use it to:

- Initialize package-level behavior
- Expose selected names
- Document package-level configuration
- Control what is imported through package APIs

Example:

```text
utils/
├── __init__.py
└── cleaning.py
```

Modern Python also supports **namespace packages** that do not require `__init__.py` in every situation.

However, `__init__.py` remains very common in regular Python packages and is important to understand for interviews and real projects.

---

# 13. Absolute and Relative Imports

Consider:

```text
project/
├── main.py
└── pipeline/
    ├── __init__.py
    ├── extract.py
    └── transform.py
```

An absolute import might be:

```python
from pipeline.extract import extract_data
```

A relative import inside the `pipeline` package can be:

```python
from .extract import extract_data
```

The dot means:

```text
. → current package
```

Two dots mean the parent package:

```python
from ..config import settings
```

Relative imports are useful inside packages, while absolute imports are often easier to understand across larger projects.

---

# 14. Standard Library Modules

Python comes with a large standard library.

Examples:

```python
import os
import sys
import json
import csv
import datetime
import pathlib
import logging
import math
```

No separate `pip install` is normally required for these standard-library modules.

### Example: `json`

```python
import json

record = '{"id": 101, "name": "Onkar"}'

data = json.loads(record)

print(data["name"])
```

The standard library is heavily used in Data Engineering scripts for files, JSON, paths, dates, logging, and system interaction.

---

# 15. Third-Party Packages

Third-party packages are libraries that are not included in Python's standard library.

Examples commonly used in Data Engineering include:

```text
pandas
numpy
requests
SQLAlchemy
PyYAML
boto3
```

They are usually installed from a package repository such as PyPI.

For example:

```bash
pip install pandas
```

Then:

```python
import pandas as pd
```

The important distinction is:

```text
Standard library → included with Python installation
Third-party     → normally installed separately
```

---

# 16. `pip`

`pip` is the standard package installer commonly used with Python.

Install a package:

```bash
pip install pandas
```

Upgrade a package:

```bash
pip install --upgrade pandas
```

Remove a package:

```bash
pip uninstall pandas
```

View installed packages:

```bash
pip list
```

Show package details:

```bash
pip show pandas
```

In practice, using the Python interpreter explicitly can avoid environment confusion:

```bash
python -m pip install pandas
```

On some systems the command is:

```bash
python3 -m pip install pandas
```

The key idea is to make sure `pip` installs into the Python environment you intend to use.

---

# 17. Virtual Environments

Different projects may require different package versions.

For example:

```text
Project A → pandas 2.x
Project B → pandas 1.x
```

Installing everything globally can create dependency conflicts.

A virtual environment isolates project dependencies.

Create one:

```bash
python -m venv .venv
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Then install project dependencies inside it:

```bash
python -m pip install pandas
```

Deactivate:

```bash
deactivate
```

Conceptually:

```text
Operating System
      ↓
Python installation
      ↓
Project virtual environment
      ↓
Project-specific packages
```

> [!IMPORTANT]
> Virtual environments are essential for reproducible Python projects and are a common practical interview topic.

---

# 18. `requirements.txt`

A project can record its Python dependencies in a file called:

```text
requirements.txt
```

Example:

```text
pandas==2.3.1
requests==2.32.4
```

Install everything listed in the file:

```bash
python -m pip install -r requirements.txt
```

Generate a list from the current environment:

```bash
python -m pip freeze > requirements.txt
```

The purpose is reproducibility:

```text
Developer A
    ↓
requirements.txt
    ↓
Developer B
    ↓
same dependency set
```

> [!WARNING]
> `pip freeze` records the packages installed in the current environment, which can include transitive dependencies. For production projects, dependency management should be deliberate rather than blindly copying every installed package.

---

# 19. Import Errors

A common error is:

```text
ModuleNotFoundError: No module named 'something'
```

This usually means Python cannot find the requested module in the current import environment.

Possible causes include:

1. Package is not installed.
2. Wrong virtual environment is active.
3. Module name is misspelled.
4. Project path is incorrect.
5. Import path is incorrect.

For example:

```python
import pandas
```

If pandas is not installed in the active environment, Python may raise `ModuleNotFoundError`.

A useful debugging check is:

```bash
python -m pip show pandas
```

Make sure the Python interpreter and pip environment are the ones being used by the project.

---

# 20. Circular Imports

A circular import occurs when modules depend on each other in a cycle.

Example:

```text
module_a
   ↓
module_b
   ↓
module_a
```

For example:

```python
# a.py
from b import function_b
```

and:

```python
# b.py
from a import function_a
```

This can cause partially initialized modules and import errors.

A common solution is to redesign the dependency structure:

```text
Before:
A → B
↑   ↓
└───┘

After:
A → common
B → common
```

Move shared functionality into a third module instead of making two modules depend directly on each other.

> [!TIP]
> Circular imports are often a design problem, not simply an import syntax problem.

---

# 21. Common Mistakes

## Mistake 1: Naming Your File After a Standard Module

Avoid naming your own file:

```text
json.py
random.py
math.py
```

If you then write:

```python
import json
```

Python may import your local file instead of the standard-library module, depending on the import path.

Use descriptive project-specific names instead.

---

## Mistake 2: Using `from module import *`

Avoid:

```python
from module import *
```

It can pollute the namespace and make dependencies unclear.

Prefer explicit imports.

---

## Mistake 3: Installing into the Wrong Environment

You may run:

```bash
pip install pandas
```

but execute your program with a different Python interpreter.

A safer pattern is:

```bash
python -m pip install pandas
```

using the same `python` command that runs the project.

---

## Mistake 4: Forgetting `__main__`

If executable test code is placed directly in a reusable module, importing that module can unexpectedly execute the code.

Use:

```python
if __name__ == "__main__":
    main()
```

when appropriate.

---

## Mistake 5: Creating Circular Dependencies

If two modules import each other, reconsider the module boundaries and move shared logic into a separate module.

---

# 22. Interview Follow-up Questions

> [!QUESTION]
>
> ## Interview Follow-up Questions

### Q1. What is the difference between a module and a package?

<details>
<summary><strong>Answer</strong></summary>

A **module** is generally a Python file containing reusable code.

Example:

```text
cleaning.py
```

A **package** is a directory that organizes related modules into a logical namespace.

Example:

```text
utils/
├── cleaning.py
├── validation.py
└── formatting.py
```

In modern Python, namespace packages can exist without `__init__.py`, but regular packages commonly contain it.

</details>

---

### Q2. Why do we use `if __name__ == "__main__"`?

<details>
<summary><strong>Answer</strong></summary>

It allows code to run when a file is executed directly but prevents that code from automatically running when the file is imported as a module.

```python
def main():
    print("Running pipeline")


if __name__ == "__main__":
    main()
```

If we execute:

```bash
python pipeline.py
```

`main()` runs.

If another module executes:

```python
import pipeline
```

`main()` does not automatically run.

This allows one file to be both reusable as a module and executable as a script.

</details>

---

### Q3. What is the difference between `import module` and `from module import function`?

<details>
<summary><strong>Answer</strong></summary>

With:

```python
import math
```

we access the function through the module namespace:

```python
math.sqrt(25)
```

With:

```python
from math import sqrt
```

we can call:

```python
sqrt(25)
```

`import module` makes the source namespace explicit. Direct imports can be convenient when only a few names are required.

</details>

---

### Q4. What causes `ModuleNotFoundError`?

<details>
<summary><strong>Answer</strong></summary>

Python raises `ModuleNotFoundError` when it cannot find the requested module in the available import paths.

Common causes include:

- Package is not installed.
- Wrong virtual environment is active.
- Module name is misspelled.
- Incorrect project structure.
- Incorrect import path.

A useful check is:

```bash
python -m pip show package_name
```

The important point is to check the **same Python environment** that runs the application.

</details>

---

### Q5. Why are virtual environments important?

<details>
<summary><strong>Answer</strong></summary>

Virtual environments isolate project dependencies.

Without isolation:

```text
Project A → package version X
Project B → package version Y
```

The projects may conflict when both use the same global environment.

With virtual environments:

```text
Project A → .venv → version X
Project B → .venv → version Y
```

This improves reproducibility and reduces dependency conflicts.

</details>

---

### Q6. What is a circular import and how would you fix it?

<details>
<summary><strong>Answer</strong></summary>

A circular import occurs when modules depend on each other in a cycle.

```text
A → B → A
```

For example, `a.py` imports `b.py` while `b.py` imports `a.py`.

A common fix is to redesign the dependency structure and move shared functionality into a third module:

```text
A → common
B → common
```

Other techniques can sometimes help, but restructuring the dependency graph is usually the cleaner long-term solution.

</details>

---

### Q7. What is the difference between standard-library and third-party modules?

<details>
<summary><strong>Answer</strong></summary>

The **standard library** is distributed with Python.

Examples:

```python
import json
import math
import logging
```

Third-party packages are normally installed separately, often using pip.

Examples:

```bash
pip install pandas
pip install requests
```

Then:

```python
import pandas
import requests
```

This distinction matters when setting up environments and deployment systems.

</details>

---

### Q8. Why is `python -m pip install package` often preferred over just `pip install package`?

<details>
<summary><strong>Answer</strong></summary>

`python -m pip` explicitly runs pip using the selected Python interpreter.

For example:

```bash
python -m pip install pandas
```

This helps reduce confusion when multiple Python installations or virtual environments exist.

The key idea is:

```text
python → interpreter being used
python -m pip → pip associated with that interpreter
```

This is particularly useful when debugging dependency and environment problems.

</details>

---

# 23. Data Engineering Perspective

Modules and packages are essential for structuring real Data Engineering projects.

A simple pipeline might start as:

```text
pipeline.py
```

But as the project grows, it can become:

```text
data_pipeline/
├── __init__.py
├── main.py
├── config.py
├── extract/
│   ├── __init__.py
│   └── source.py
├── transform/
│   ├── __init__.py
│   └── cleaning.py
├── load/
│   ├── __init__.py
│   └── warehouse.py
└── utils/
    ├── __init__.py
    ├── logging_utils.py
    └── validation.py
```

Each component has a clear responsibility.

### Extraction

```python
from extract.source import extract_data
```

Responsible for obtaining data from a source.

### Transformation

```python
from transform.cleaning import clean_data
```

Responsible for cleaning and transforming records.

### Loading

```python
from load.warehouse import load_data
```

Responsible for writing transformed data to the destination.

### Configuration

```python
from config import DATABASE_CONFIG
```

Keeps configuration separate from transformation logic.

This produces a cleaner architecture:

```text
Source
  ↓
extract module
  ↓
transform module
  ↓
validation module
  ↓
load module
  ↓
Warehouse / Lake
```

The main benefit is **separation of concerns**.

If the warehouse changes, you should not need to rewrite your extraction logic.

If a transformation changes, you should not need to rewrite database connection code.

> [!IMPORTANT]
> For a Data Engineer, understanding modules, packages, imports, virtual environments, and dependency management is part of writing production-quality Python—not merely interview knowledge.

---

## Navigation

⬅️ **Previous:** [Day 19 - Advanced Functions](../Day_19_Advanced_Functions/readme.md)

➡️ **Next:** [Day 21 - Exception Handling](../Day_21_Exception_Handling/readme.md)
