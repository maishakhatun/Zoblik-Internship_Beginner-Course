# Exercise 2: Zoblik Employee Bonus System
# The Zoblik HR department wants a simple system to determine employee bonuses.

#taking inputs
employee_performance_score=float(input("Enter your performance score: "))
years_at_company=float(input("How long have you been working in Zoblik: "))

#displaying the inputs
print(f"Evaluating bonus for employee with performance score of {employee_performance_score} and working for {years_at_company} years...")

print("-----Evaluation Started-----")

#applying conditions
if employee_performance_score >=90:
    print("Excellent Performance!")
    if years_at_company >= 5:
        print("Bonus: $1000 - High Performer & Long Term Zoblik employee!")
    else:
        print("Bonus: $700 - High Performer!")

elif employee_performance_score >= 80:
    print("Great Performer!")
    if years_at_company >= 5:
        print("Bonus: $800 - Great Performer & Long Term Zoblik employee!")
    else:
        print("Bonus: $650")

elif employee_performance_score >= 70:
    print("Good Performance!")
    if years_at_company >= 5:
        print("Bonus: $500 - Solid Performer & Long Term Zoblik employee!")
    else:
        print("Bonus: $250 - Solid Performer!")
else:
    print("Performance needs improvement. No Bonus this quarter!")

print("-----Evaluation Completed-----")