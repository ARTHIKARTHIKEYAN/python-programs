def find_factors(number):
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors

def main():
    try:
        # Get input from the user
        number = int(input("Enter a positive integer: "))
        
        # Validate the input
        if number <= 0:
            raise ValueError("Please enter a positive integer.")

        # Find the factors of the number
        factors = find_factors(number)

        # Display the factors
        print(f"The factors of {number} are: {factors}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
