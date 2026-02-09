#Creating basic calculator
First_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

#arithmetic operations
addition = First_number + second_number
subtraction = First_number - second_number
multiplication = First_number * second_number

#printing the output
print("-------RESULT-------")
print(f"Sum of {First_number} + {second_number} = {addition}")
print(f"Difference of {First_number} - {second_number} = {subtraction}")
print(f"Product of {First_number} * {second_number} = {multiplication}")