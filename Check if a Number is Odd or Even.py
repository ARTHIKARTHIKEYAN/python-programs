def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    try:
        # Get input from the user
        number = int(input("Enter a number: "))
        
        # Check if the number is odd or even
        result = check_odd_or_even(number)

        # Display the result
        print(f"The number {number} is {result}.")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
