#defining function for addition
def addition(num1,num2):
    add = num1 + num2
    return add

#defining function for subtraction
def subtraction(num1,num2):
    sub = num1-num2
    return sub

#defining function for multiplication
def multiplication(num1,num2):
    mul = num1*num2
    return mul

#taking user input for numbers and operations
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))
operation = input("\n1 for Addition\n2 for Subtraction\n3 for Multiplication\nChoose the operation to perform: ")

#conditions
if operation == "1":
    print (f"Sum of {num1} and {num2} is {addition(num1,num2)}")
elif operation == "2":
    print(f"Difference of {num1} and {num2} is {subtraction(num1, num2)}")
elif operation =="3":
    print (f"Product of {num1} and {num2} is {multiplication(num1,num2)}")
else:
    print("Enter a valid input. Please try again")