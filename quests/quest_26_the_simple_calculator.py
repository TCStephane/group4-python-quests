# Quest 26: The Simple Calculator (Formatted Output Version)
# Author : @gunnogere
#25th February 2026

# Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b


# Main Program
print("=== Simple Calculator - Group 4===")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter the number of the operation (1-4): ")

if choice.isdigit():
    choice = int(choice)

    if choice in [1, 2, 3, 4]:

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = add(num1, num2) 
            sentence = "sum"

        elif choice == 2:
            result = subtract(num1, num2) 
            sentence = "difference"

        elif choice == 3:
            result = multiply(num1, num2) 
            sentence = "product"

        elif choice == 4:
            result = divide(num1, num2) 
            sentence = "quotient"

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
             
            # Format 2: The sum of 1 and 3 is 4
            print(f"The {sentence} of {num1} and {num2} is {result}")

    else:
        print("Function doesn't exist. Choose from available functions (1-4).")

else:
    print("Invalid input. Please enter a number between 1 and 4.")