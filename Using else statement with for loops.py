# Example: Checking if a number is prime using a for loop with an else statement
num = 11

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
else:
    print(f"{num} is a prime number.")
