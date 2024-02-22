def string_length_recursive(s):
    # Base case: if the string is empty, return 0
    if not s:
        return 0
    # Recursive case: call the function with the substring excluding the first character
    # and add 1 to the result (counting the current character)
    return 1 + string_length_recursive(s[1:])

# Define a string
my_string = "Hello, World!"

# Call the recursive function to find the length of the string
length_of_string = string_length_recursive(my_string)

# Print the length of the string
print("Length of the string:", length_of_string)
