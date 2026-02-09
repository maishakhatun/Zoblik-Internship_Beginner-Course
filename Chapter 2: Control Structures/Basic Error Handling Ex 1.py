# Exercise 1: Handling Invalid Numbers
#Details and example:
#Write a Python program that asks the user for a number and calculates its square. 
# Use a try-except block to catch ValueError if the user enters something that can't be converted into a number.

# Exercise 1: Calculate square, handle ValueError

print("--- Square Calculator ---")
try:
    # Prompt user for input and try to convert to a float
    user_input = input("Enter a number to find its square: ")
    number = float(user_input) # This might raise a ValueError

    # If conversion is successful, calculate the square
    square = number * number
    print(f"The square of {number} is: {square}")

except ValueError:
    # If a ValueError occurs (e.g., non-numeric input), handle it
    print("Oops! That wasn't a number, but don't worry—you can try again! Please enter a numeric value like 5 or 3.14.")

print("\nCalculation attempt finished.")