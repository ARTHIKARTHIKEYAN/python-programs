# Input: Get values from the user
a = input("Enter the value of variable a: ")
b = input("Enter the value of variable b: ")

print(f"Before swapping: a = {a}, b = {b}")

# Swap the values using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")
