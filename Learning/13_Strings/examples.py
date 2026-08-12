# 🐍 Day 13 — Strings

# ============================================================
# 1. Creating Strings
# ============================================================

name = "Onkar"
city = 'Pune'
message = "Welcome to Python"

print(name)
print(city)
print(message)


# ============================================================
# 2. String Indexing
# ============================================================

text = "Python"

print(text[0])      # P
print(text[1])      # y
print(text[5])      # n


# ============================================================
# 3. Negative Indexing
# ============================================================

print(text[-1])     # n
print(text[-2])     # o
print(text[-6])     # P


# ============================================================
# 4. String Slicing
# ============================================================

print(text[0:3])    # Pyt
print(text[2:6])    # thon
print(text[:3])     # Pyt
print(text[3:])     # hon
print(text[:])      # Python
print(text[::-1])   # nohtyP


# ============================================================
# 5. String Length
# ============================================================

print(len(text))


# ============================================================
# 6. Concatenation
# ============================================================

first_name = "Onkar"
last_name = "Jadhav"

full_name = first_name + " " + last_name
print(full_name)


# ============================================================
# 7. String Repetition
# ============================================================

print("Python " * 3)


# ============================================================
# 8. Membership Operators
# ============================================================

language = "Python"

print("P" in language)
print("Java" in language)
print("Java" not in language)


# ============================================================
# 9. Traversing a String
# ============================================================

for character in "Python":
    print(character)


# ============================================================
# 10. Common String Methods
# ============================================================

text = "python programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())


# ============================================================
# 11. strip(), lstrip(), rstrip()
# ============================================================

text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# ============================================================
# 12. replace()
# ============================================================

text = "I like Java"

print(text.replace("Java", "Python"))


# ============================================================
# 13. split()
# ============================================================

text = "Python SQL Azure Hadoop"

words = text.split()
print(words)


# ============================================================
# 14. join()
# ============================================================

words = ["Python", "SQL", "Azure"]

result = " | ".join(words)
print(result)


# ============================================================
# 15. find() and index()
# ============================================================

text = "Python Programming"

print(text.find("Python"))
print(text.find("Java"))      # -1 when not found
print(text.index("Python"))


# ============================================================
# 16. count()
# ============================================================

text = "banana"

print(text.count("a"))
print(text.count("an"))


# ============================================================
# 17. startswith() and endswith()
# ============================================================

filename = "sales_data.csv"

print(filename.startswith("sales"))
print(filename.endswith(".csv"))


# ============================================================
# 18. String Formatting — f-string
# ============================================================

name = "Onkar"
age = 22

print(f"My name is {name} and I am {age} years old.")


# ============================================================
# 19. Escape Characters
# ============================================================

print("Hello\nPython")
print("Python\tSQL")
print("He said \"Python is easy\"")


# ============================================================
# 20. Raw String
# ============================================================

path = r"C:\Users\Onkar\Python"
print(path)


# ============================================================
# 21. Strings are Immutable
# ============================================================

text = "Python"

# text[0] = "J"   # TypeError: strings cannot be changed directly

new_text = "J" + text[1:]
print(new_text)


# ============================================================
# 22. Practical Data Engineering Example
# ============================================================

file_name = "customer_sales_2026.csv"

if file_name.endswith(".csv"):
    print("CSV file detected")

parts = file_name.split("_")
print(parts)
