print("CALCULATOR APPLICATION") # Title for application
number1 = float(input("What is the first number? ")) # Get users numbers, float incase of decimals/division
number2 = float(input("What is the first number? "))
print("Select an operation:")
print("1 - Addition")
print("2 - Subtraction") # User choices
print("3 - Multiplication")
print("4 - Division")
userinput = int(input("Enter your choice (1-4): ")) # Get user input to decide an operation in the following match case
match userinput:
    case 1:
        print("Here is the result: ",number1 + number2)
    case 2:
        print("Here is the result: ",number1 - number2)
    case 3:
        print("Here is the result: ",number1 * number2)
    case 4:
        print("Here is the result: ",number1 / number2)
    case _: #if the user doesnt iunput 1-4
        print("Please enter a number(1-4) to select an operation")