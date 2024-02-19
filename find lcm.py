def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    gcd = find_gcd(x, y)
    lcm = (x * y) // gcd
    return lcm

def main():
    try:
        # Get input from the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        # Validate the input
        if num1 <= 0 or num2 <= 0:
            raise ValueError("Please enter positive integers.")

        # Find the LCM of the two numbers
        lcm = find_lcm(num1, num2)

        # Display the result
        print(f"The LCM of {num1} and {num2} is: {lcm}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
