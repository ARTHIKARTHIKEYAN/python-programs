import math

# Method 1: Using the math module
def square_root_math(number):
    return math.sqrt(number)

# Method 2: Using the ** operator
def square_root_operator(number):
    return number ** 0.5

# Input: Get a number from the user
num = float(input("Enter a number: "))

# Calculate square root using both methods
result_math = square_root_math(num)
result_operator = square_root_operator(num)

# Display the results
print(f"Square root using math module: {result_math}")
print(f"Square root using ** operator: {result_operator}")
