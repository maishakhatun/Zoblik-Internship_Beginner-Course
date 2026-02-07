# grade_calculator.py

from utils import calculate_average, assign_letter_grade, validate_grade, find_class_extremes

def main():
    students = {}

    while True:
        name = input("Enter student name (or press Enter to finish): ").strip()

        if name == "":
            break

        grades = []

        for i in range(1, 4):
            while True:
                try:
                    score_input = input(f"Enter grade {i} for {name}: ").strip()
                    score = validate_grade(score_input)
                    grades.append(score)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

        students[name] = grades

    if not students:
        print("\nNo data entered.")
        return

    # Generate Report
    print("\nFinal Grade Report")
    print("-" * 40)
    print(f"{'Name':<15}{'Average':<12}{'Letter Grade'}")
    print("-" * 40)

    for name, grades in students.items():
        avg = calculate_average(grades)
        letter = assign_letter_grade(avg)
        print(f"{name:<15}{avg:<12.2f}{letter}")

    print("-" * 40)

    # Bonus: Find class extremes
    highest, lowest = find_class_extremes(students)
    print(f"\nHighest Class Average: {max(calculate_average(grades) for grades in students.values()):.2f}")
    print(f"\nLowest Class Average: {min(calculate_average(grades) for grades in students.values()):.2f}")
'''
    print(f"\nHighest Performer(s):", ", ".join(highest))
    print(f"Lowest Performer(s):", ", ".join(lowest))
'''

if __name__ == "__main__":
    main()