# Exercise 2: Using Dictionary Methods for Student Grades

student_grades = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78
}

# Add new student Eve
student_grades["Eve"] = 95

# 1. Safely retrieve Bob's grade using get()
bobs_grade = student_grades.get("Bob")
print(f"Bob's grade: {bobs_grade}")

# Change default value to numeric 0
dianas_grade = student_grades.get("Diana", 0)
print(f"Diana's grade: {dianas_grade}")

print("-" * 20)  # Separator

# 2. Print all student names (keys)
print("All student names:")
for student_name in student_grades.keys():
    print(student_name)

print("-" * 20)  # Separator

# 3. Print all grades (values)
print("All grades:")
for grade in student_grades.values():
    print(grade)