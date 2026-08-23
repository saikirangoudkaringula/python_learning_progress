
# 🐍 Python Practice - Dictionaries
# Today I practiced Dictionaries,
# Key-Value Pairs, Accessing Values,
# and Adding New Data.


# -----------------------------
# 1. Creating a Dictionary
# -----------------------------

student = {
    "name": "Sai",
    "age": 22,
    "course": "Data Science",
    "city": "Hyderabad"
}

print(student)


# -----------------------------
# 2. Accessing Values
# -----------------------------

print(student["age"])
print(student["city"])


# -----------------------------
# 3. Adding New Key-Value Pair
# -----------------------------

student["skills"] = ("Python", "SQL", "Pandas")

print(student)


# -----------------------------
# 4. Updating a Value
# -----------------------------

student["age"] = 23

print(student)


# -----------------------------
# 5. Adding More Data
# -----------------------------

student["experience"] = "Python Practice"

print(student)


# -----------------------------
# ⭐ Key Takeaways
# -----------------------------

"""
Dictionaries store data as:
key : value

Example:

"name" : "Sai"
"age"  : 22

Important concepts practiced:
- Creating dictionaries
- Key-value pairs
- Accessing values using keys
- Adding new key-value pairs
- Updating existing values

Next topic:
Dictionary Methods
Dictionary Loops
Dictionary Comprehension
"""