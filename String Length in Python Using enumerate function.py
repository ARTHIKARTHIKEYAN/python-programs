# Define a string
my_string = "Hello, World!"

# Use enumerate() with a loop to find the length of the string
length_of_string = 0
for index, char in enumerate(my_string):
    length_of_string = index + 1

# Print the length of the string
print("Length of the string:", length_of_string)
