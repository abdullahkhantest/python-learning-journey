# Python Dictionaries

# This file demonstrates dictionary operations in Python

# ==========================================
# PART 1: Creating and Accessing Dictionaries
# ==========================================

# Creating dictionaries
empty_dict = {}  # Empty dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}  # Basic dictionary
graded_test = {"Alice": 95, "Bob": 82, "Charlie": 88}  # Names as keys
mixed_dict = {1: "one", "two": 2, (3, 4): "tuple key"}  # Different types of keys

print("Dictionaries:")
print(f"Empty dictionary: {empty_dict}")
print(f"Person dictionary: {person}")
print(f"Graded test dictionary: {graded_test}")
print(f"Mixed dictionary: {mixed_dict}")

# Accessing dictionary values
print("\nAccessing dictionary values:")
print(f"Name: {person['name']}")
print(f"Bob's grade: {graded_test['Bob']}")
print(f"Value for tuple key: {mixed_dict[(3, 4)]}")

# Using get() to safely access keys
print("\nSafely accessing keys with get():")
print(f"Age: {person.get('age')}")
print(f"Phone: {person.get('phone')}")
# Providing a default value if key doesn't exist
print(f"Phone with default: {person.get('phone', 'Not available')}")

# ==========================================
# PART 2: Modifying Dictionaries
# ==========================================

# Adding or modifying key-value pairs
print("\nModifying dictionaries:")
person["job"] = "Developer"  # Add a new key-value pair
print(f"After adding job: {person}")

person["age"] = 31  # Modify an existing value
print(f"After updating age: {person}")

# Removing key-value pairs
removed_value = person.pop("city")  # Remove and return a value
print(f"Removed city: {removed_value}")
print(f"After pop: {person}")

# Remove the last inserted item (Python 3.7+ preserves insertion order)
last_key, last_value = person.popitem()
print(f"Removed last item: {last_key} = {last_value}")
print(f"After popitem: {person}")

# Clear all items
person_copy = person.copy()  # Make a copy first
person_copy.clear()
print(f"After clear: {person_copy}")

# ==========================================
# PART 3: Dictionary Methods and Operations
# ==========================================

# Dictionary methods
person = {"name": "Alice", "age": 30, "city": "New York"}
print("\nDictionary methods:")

# Get all keys
print(f"Keys: {list(person.keys())}")

# Get all values
print(f"Values: {list(person.values())}")

# Get all key-value pairs as tuples
print(f"Items: {list(person.items())}")

# Update dictionary with another dictionary
person.update({"job": "Developer", "age": 31, "country": "USA"})
print(f"After update: {person}")

# Dictionary comprehensions
print("\nDictionary comprehensions:")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(f"Name lengths: {name_lengths}")

# ==========================================
# PART 4: Nested Dictionaries
# ==========================================

# Creating nested dictionaries
print("\nNested dictionaries:")
users = {
    "alice": {
        "name": "Alice Smith",
        "age": 30,
        "contact": {
            "email": "alice@example.com",
            "phone": "555-1234"
        }
    },
    "bob": {
        "name": "Bob Johnson",
        "age": 25,
        "contact": {
            "email": "bob@example.com",
            "phone": "555-5678"
        }
    }
}

# Accessing nested dictionary values
print(f"Alice's email: {users['alice']['contact']['email']}")
print(f"Bob's phone: {users['bob']['contact']['phone']}")

# Modifying nested dictionaries
users["alice"]["contact"]["phone"] = "555-9876"
print(f"Alice's updated phone: {users['alice']['contact']['phone']}")

# ==========================================
# PART 5: Common Dictionary Use Cases
# ==========================================

print("\nCommon dictionary use cases:")

# Counting occurrences
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f"Word counts: {word_counts}")

# Alternative using Counter from collections
from collections import Counter
word_counter = Counter(words)
print(f"Word counter: {dict(word_counter)}")

# Using dictionaries for mappings
grades_to_letters = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F"
}

def get_letter_grade(score):
    for min_score in sorted(grades_to_letters.keys(), reverse=True):
        if score >= min_score:
            return grades_to_letters[min_score]

print(f"Grade 85 is letter: {get_letter_grade(85)}")
print(f"Grade 72 is letter: {get_letter_grade(72)}")
print(f"Grade 50 is letter: {get_letter_grade(50)}")

# ==========================================
# PRACTICE EXERCISES
# ==========================================

# Exercise 1: Create a dictionary of favorite books with authors as keys and titles as values

# Exercise 2: Create a nested dictionary representing a simple shopping cart with products,
# quantities, and prices

# Exercise 3: Write a function that takes a sentence and returns a dictionary with words as keys
# and their frequency as values
