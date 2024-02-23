import random

# Input: Get the range of random numbers from the user
lower_limit = int(input("Enter the lower limit of the range: "))
upper_limit = int(input("Enter the upper limit of the range: "))

# Generate a random number within the specified range
random_number = random.randint(lower_limit, upper_limit)

# Display the generated random number
print(f"Random number between {lower_limit} and {upper_limit}: {random_number}")
