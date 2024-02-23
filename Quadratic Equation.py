import math

def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is non-negative
    if discriminant >= 0:
        # Calculate the two solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    else:
        # If the discriminant is negative, there are no real solutions
        return None

# Input: Get coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate and display the solutions
solutions = solve_quadratic_equation(a, b, c)

if solutions:
    print(f"Solutions: {solutions[0]} and {solutions[1]}")
else:
    print("No real solutions (discriminant is negative)")
