def list_to_string_with_while_loop(lst):
    result_string = "["
    i = 0  # Index variable

    # Use a while loop to iterate through the list elements
    while i < len(lst):
        # Convert the element to a string and append it to the result string
        result_string += str(lst[i]) + ", "
        i += 1

    # Remove the trailing comma and space if the list is not empty
    if len(result_string) > 1:
        result_string = result_string[:-2]

    result_string += "]"

    return result_string

# Example usage:
my_list = [1, 2, "hello", [3, 4]]

result_string = list_to_string_with_while_loop(my_list)

print("List as a string:", result_string)
