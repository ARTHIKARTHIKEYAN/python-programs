def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get user input for the desired Fibonacci sequence length
try:
    length = int(input("Enter the length of the Fibonacci sequence: "))
    if length < 0:
        print("Please enter a non-negative integer.")
    else:
        fib_sequence = [fibonacci(i) for i in range(1, length + 1)]
        print("Fibonacci sequence:", fib_sequence)
except ValueError:
    print("Please enter a valid integer.")
