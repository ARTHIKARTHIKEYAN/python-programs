def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        # Find the largest number
        largest = find_largest(num1, num2, num3)

        # Display the result
        print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
