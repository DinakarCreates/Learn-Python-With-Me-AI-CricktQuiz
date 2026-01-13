"""\nDay 2: For Loops - Iterating Through Data\nLearning how to repeat actions efficiently\n"""

# Basic for loop with range
print("Basic For Loop (1 to 5):")
for i in range(1, 6):
    print(f"Number: {i}")

# Loop through a list
print("\n" + "="*40)
print("Loop Through a List:")
fruits = ["Apple", "Banana", "Orange", "Mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Loop with index using enumerate
print("\n" + "="*40)
print("Loop with Index (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Loop through range with step
print("\n" + "="*40)
print("Even Numbers (0 to 10):")
for num in range(0, 11, 2):
    print(num, end=" ")
print()  # New line

# Nested loops
print("\n" + "="*40)
print("Multiplication Table (2 to 4):")
for i in range(2, 5):
    for j in range(1, 6):
        print(f"{i}×{j}={i*j}", end="  ")
    print()  # New line after each row

# Loop with break
print("\n" + "="*40)
print("Loop with Break (find first even number):")
for num in range(1, 20):
    if num % 2 == 0:
        print(f"First even number: {num}")
        break

# Loop with continue
print("\n" + "="*40)
print("Loop with Continue (skip odd numbers):")
for num in range(1, 11):
    if num % 2 == 1:  # Skip odd numbers
        continue
    print(f"Even: {num}")

print("\n✅ Day 2 Complete! Mastered For Loops!")
print("Next: While Loops & Loop Control")
