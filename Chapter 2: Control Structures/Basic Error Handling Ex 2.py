# Exercise 2: Catching Multiple Errors
#Details and example:
#Create a simple function that attempts to divide two numbers. 
# Use multiple except blocks to specifically catch ValueError (if inputs aren't numbers) 
# and ZeroDivisionError (if the second number is zero).

# Exercise 2: Divide two numbers, handle multiple errors

print("\n--- Smart Division Calculator ---")

def smart_divide():
    """
    Attempts to divide two numbers provided by the user,
    handling ValueError, ZeroDivisionError, and TypeError.
    """
    try:
        # Get numerator input and attempt conversion
        num1_str = input("Enter the first number (numerator): ")
        num1 = float(num1_str)  # Potential ValueError

        # Get denominator input and attempt conversion
        num2_str = input("Enter the second number (denominator): ")
        num2 = float(num2_str)  # Potential ValueError

        # Perform division
        result = num1 / num2  # Potential ZeroDivisionError or TypeError (in rare cases)

        print(f"Result: {num1} divided by {num2} is {result}")

    except ValueError:
        # Handles cases where input strings cannot be converted to float
        print("Invalid input! Please ensure both inputs are numeric.")
    except ZeroDivisionError:
        # Handles division by zero
        print("Error: Cannot divide by zero. Please provide a non-zero second number.")
    except TypeError:
        # Handles operations involving incompatible types
        print("Type error encountered! Please ensure you're entering proper numerical values.")
    except Exception as e:
        # A general catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")

smart_divide()
print("\nDivision process completed.")