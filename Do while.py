# Example of a do-while loop in Python

while True:
    # Code to be executed at least once
    user_input = input("Enter 'yes' to continue or 'no' to exit: ").lower()

    if user_input == 'no':
        break  # Exit the loop if the user enters 'no'
    
    # Code to be executed as long as the condition is True
    print("Doing something...")

print("Exited the loop.")
