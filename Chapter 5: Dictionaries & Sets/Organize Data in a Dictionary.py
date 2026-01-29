#Exercise: Organize Data in a Dictionary

data_students = {}

while True:
    choice = input("Add another student? (yes/no): ").strip().lower()
    
    if choice == "no":
        break

    # Validate name input (letters only)
    while True:
        name = input("Enter student first name: ").strip()
        surname = input(f"Enter surname of {name}: ").strip()
        full_name = f"{name} {surname}"

        if name.replace(" ", "").isalpha() and surname.replace(" ", "").isalpha():
            break
        else:
            print("Names must contain only letters. Try again.")
    
    # Validate grade input
    while True:
        grade_input = input(f"Enter grade for {full_name}: ").strip()
        try:
            grade = int(grade_input)
            break
        except ValueError:
            print("Invalid grade. Please enter a numeric value.")

    # Add or update dictionary entry
    data_students[full_name] = grade
    print(f"{full_name}, grade: {grade} added/updated successfully.")
    print("-" * 35)

# Display student list
print("\n===== Student Grades =====")
if not data_students:
    print("No students added yet.")
else:
    for student in data_students.keys():
        print(f"Student: {student:<20} Grade: {data_students[student]}")
        
print("\nEnd ")