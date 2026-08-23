# 🐍 Python Practice - Sets
# Today I practiced Sets, Set Methods,
# Set Operations, and Set Comprehension.


# -----------------------------
# 1. Creating a Set
# -----------------------------

skills = {"Python", "SQL", "Pandas", "NumPy"}

print(skills)


# -----------------------------
# 2. Remove Duplicates
# -----------------------------

skills = ["Python", "SQL", "Python", "Pandas", "SQL", "NumPy"]

unique_skills = set(skills)

print("Unique Skills:", unique_skills)


# -----------------------------
# 3. Empty Set
# -----------------------------

empty = set()

print("Empty Set:", empty)


# -----------------------------
# 4. add()
# -----------------------------

skills = {"Python", "SQL"}

skills.add("Pandas")

print(skills)


# -----------------------------
# 5. update()
# -----------------------------

skills.update(["NumPy", "Matplotlib"])

print(skills)


# -----------------------------
# 6. remove()
# -----------------------------

skills.remove("SQL")

print(skills)


# -----------------------------
# 7. discard()
# -----------------------------

skills.discard("Java")

print(skills)


# -----------------------------
# 8. pop()
# -----------------------------

removed_skill = skills.pop()

print("Removed:", removed_skill)
print("Remaining:", skills)


# -----------------------------
# 9. Set Operations
# -----------------------------

A = {"Python", "SQL", "Pandas", "NumPy"}

B = {"SQL", "Pandas", "Power BI", "Excel"}

union = A | B
intersection = A & B
difference = A - B
symmetric_difference = A ^ B

print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Symmetric Difference:", symmetric_difference)


# -----------------------------
# 10. Loop Through Set
# -----------------------------

skills = {
    "Python",
    "SQL",
    "Pandas",
    "NumPy",
    "Power BI"
}

for skill in skills:
    if len(skill) > 5:
        print(skill)


# -----------------------------
# 11. Set Comprehension
# -----------------------------

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

squares = {
    number ** 2
    for number in numbers
}

print("Squares:", squares)


# -----------------------------
# ⭐ Key Takeaways
# -----------------------------

"""
Sets are:
- Unordered collections
- Mutable
- Store unique values
- Useful for removing duplicates

Important methods:
add()
update()
remove()
discard()
pop()

Set operations:
|  Union
&  Intersection
-  Difference
^  Symmetric Difference

Set comprehension:
Creates a set using a compact expression.
Duplicate results are automatically removed.
"""