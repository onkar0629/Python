"""
==========================================================
Day 09 : Loop Control Statements
Topic  : Examples

Description:
This file contains runnable examples demonstrating the
concepts covered in Day 09.

Topics Covered:
1. break Statement
2. continue Statement
3. pass Statement
4. else with Loops
5. break in while Loop
6. continue in while Loop
7. Nested Loops with break
8. Real-World Examples
==========================================================
"""

# ==========================================================
# 1. break Statement
# ==========================================================

print("========== break Statement ==========\n")

for number in range(1, 11):

    if number == 6:
        break

    print(number)

print("\nLoop Terminated using break")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 2. continue Statement
# ==========================================================

print("========== continue Statement ==========\n")

for number in range(1, 11):

    if number == 5:
        continue

    print(number)

print("\nNumber 5 was skipped.")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 3. pass Statement
# ==========================================================

print("========== pass Statement ==========\n")

for number in range(1, 6):

    if number == 3:
        pass

    print(number)

print("\npass does nothing; it simply acts as a placeholder.")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 4. else with for Loop
# ==========================================================

print("========== else with for Loop ==========\n")

for number in range(1, 6):
    print(number)

else:
    print("Loop Completed Successfully!")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 5. else with break
# ==========================================================

print("========== break prevents else ==========\n")

for number in range(1, 6):

    if number == 3:
        break

    print(number)

else:
    print("Loop Completed")

print("Loop exited using break.")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 6. break in while Loop
# ==========================================================

print("========== break in while Loop ==========\n")

count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1

print("Exited the while loop.")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 7. continue in while Loop
# ==========================================================

print("========== continue in while Loop ==========\n")

count = 0

while count < 10:

    count += 1

    if count % 2 == 0:
        continue

    print(count)

print("\nOnly odd numbers are displayed.")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 8. Nested Loop with break
# ==========================================================

print("========== Nested Loop with break ==========\n")

for row in range(1, 4):

    for column in range(1, 4):

        if column == 2:
            break

        print(f"Row {row}, Column {column}")

print()

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 9. Real-World Example - Skip Invalid Records
# ==========================================================

print("========== Skip Invalid Records ==========\n")

records = [101, 102, None, 104, None, 106]

for record in records:

    if record is None:
        continue

    print(f"Processing Record: {record}")

print("\nProcessing Completed!")

print("\n" + "=" * 50 + "\n")


# ==========================================================
# 10. Real-World Example - Stop on Critical Error
# ==========================================================

print("========== Stop on Critical Error ==========\n")

status = ["Success", "Success", "Error", "Success"]

for result in status:

    if result == "Error":
        print("Critical Error Found!")
        break

    print(result)

print("\nPipeline Stopped.")

print("\n" + "=" * 50)

print("\nEnd of Day 09 Examples 🚀")