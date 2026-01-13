"""\nDay 3: Lists - Working with Collections\nLists are fundamental Python data structures\n"""

# Creating lists
print("Creating Lists:")
fruits = ["Apple", "Banana", "Orange", "Mango"]
print(f"Fruits: {fruits}")

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

mixed = ["Python", 3, 3.14, True, None]
print(f"Mixed list: {mixed}")

# Accessing elements
print("\n" + "="*40)
print("Accessing List Elements:")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# List methods
print("\n" + "="*40)
print("List Methods:")
fruits.append("Grapes")
print(f"After append: {fruits}")

fruits.insert(1, "Papaya")
print(f"After insert at 1: {fruits}")

fruits.remove("Papaya")
print(f"After remove: {fruits}")

# List length and operations
print("\n" + "="*40)
print(f"Length of fruits: {len(fruits)}")
print(f"Is 'Apple' in list? {'Apple' in fruits}")

# List comprehension
print("\n" + "="*40)
print("List Comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares 1-5: {squares}")

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {even_numbers}")

print("\n✅ Day 3 Complete! Lists Mastered!")
print("Next: Dictionaries & Tuples")
