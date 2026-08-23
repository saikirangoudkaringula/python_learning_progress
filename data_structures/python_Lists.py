# 🐍 Python Practice - Lists
# Today I practiced Lists, List Methods, Indexing,
# Slicing, enumerate(), and List Comprehension.


# -----------------------------
# 1. Creating a List
# -----------------------------

skills = ["Python", "SQL", "Pandas", "Machine Learning"]

print(skills)


# -----------------------------
# 2. enumerate()
# -----------------------------

for i, skill in enumerate(skills):
    print(f"{i}: {skill}")


# -----------------------------
# 3. List with Conditions
# -----------------------------

marks = [75, 32, 90, 25, 88, 40]

for i, mark in enumerate(marks):
    if mark >= 40:
        print(f"student{i}: {mark} - Pass")
    else:
        print(f"student{i}: {mark} - Fail")


# -----------------------------
# 4. Even and Odd Numbers
# -----------------------------

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even:", even_numbers)
print("Odd:", odd_numbers)


# -----------------------------
# 5. List Methods
# -----------------------------

languages = ["Python", "Java"]

languages.append("C++")
languages.extend(["JavaScript", "SQL"])
languages.insert(1, "C")

print(languages)


# -----------------------------
# 6. Remove Elements
# -----------------------------

skills = ["Python", "SQL", "Java", "Pandas", "C++"]

skills.remove("Java")
skills.pop()
del skills[1]

print(skills)


# -----------------------------
# 7. Sorting
# -----------------------------

marks = [45, 89, 32, 76, 95, 60]

marks.sort()
print("Ascending:", marks)

marks.sort(reverse=True)
print("Descending:", marks)

print("Length:", len(marks))


# -----------------------------
# 8. Indexing and Slicing
# -----------------------------

skills = [
    "Python",
    "SQL",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow"
]

print(skills[2])
print(skills[-1])
print(skills[:3])
print(skills[-3:])
print(skills[::-1])


# -----------------------------
# 9. List Comprehension
# -----------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print("Squares:", squares)


# -----------------------------
# 10. Multiply Using Comprehension
# -----------------------------

number_2 = [number * 2 for number in numbers]

print("Doubled:", number_2)


# -----------------------------
# 11. Even Numbers
# -----------------------------

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = [
    number for number in numbers
    if number % 2 == 0
]

print("Even Numbers:", even_numbers)


# -----------------------------
# 12. Greater Than 50
# -----------------------------

numbers = [25, 60, 45, 80, 30, 90]

greater_num = [
    number for number in numbers
    if number > 50
]

print("Greater than 50:", greater_num)


# -----------------------------
# 13. Even Squares
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print("Even Squares:", even_squares)


# -----------------------------
# 14. Pass / Fail
# -----------------------------

marks = [35, 78, 42, 90, 25, 60]

result = [
    "Pass" if mark >= 40 else "Fail"
    for mark in marks
]

print("Result:", result)


# -----------------------------
# 15. Uppercase Names
# -----------------------------

names = ["sai", "rahul", "ravi", "anil"]

uppercased_names = [
    name.upper() for name in names
]

print(uppercased_names)


# -----------------------------
# 16. Filter Adults
# -----------------------------

ages = [12, 18, 25, 16, 30, 14, 22]

adult_list = [
    age for age in ages
    if age >= 18
]

print("Adults:", adult_list)


# -----------------------------
# ⭐ Key Takeaways
# -----------------------------

"""
Lists are:
- Ordered
- Mutable
- Allow duplicate values
- Support indexing and slicing

Important methods:
append()
extend()
insert()
remove()
pop()
sort()

enumerate() gives:
index + value

List comprehension is useful for:
- Filtering
- Transforming
- Creating new lists
"""