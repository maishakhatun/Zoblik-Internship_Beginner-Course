print("Enter 1 to start a game:")
print("Enter 2 to open settings:")
print("Enter 3 to exit the program.")

try:
    user_input = input("Enter your choice: ")
    data = int(user_input)  # may raise ValueError

    if data < 1 or data > 3:
        raise ValueError("Out of range")  # force error for invalid range

    if data == 1:
        print("You chose to start a game!")
    elif data == 2:
        print("You chose to open settings!")
    else:
        print("You chose to exit the program. Goodbye!")

except ValueError:
    if user_input.strip() == "":
        print("Your input must not be empty. Please try again!")
    elif user_input.isalpha():
        print("Your input must be a number, not letters. Please try again!")
    elif user_input.isdigit() and (int(user_input) < 1 or int(user_input) > 3):
        print("Your input must be within 1 to 3. Please try again!")
    else:
        print("Invalid input. Please try again!")