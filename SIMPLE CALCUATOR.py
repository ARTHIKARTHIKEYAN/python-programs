import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def calculator():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("0. Exit")

    while True:
        choice = input("Enter choice (0-6): ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            if choice in ('5', '6'):
                num1 = float(input("Enter the number: "))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                exponent = float(input("Enter the exponent: "))
                print("Result:", exponentiate(num1, exponent))
            elif choice == '6':
                if num1 >= 0:
                    print("Result:", square_root(num1))
                else:
                    print("Error: Cannot calculate square root of a negative number.")
        else:
            print("Invalid input. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    calculator()
