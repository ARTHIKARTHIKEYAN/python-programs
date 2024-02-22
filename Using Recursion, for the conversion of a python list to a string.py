def list_to_string_recursive(lst):
    if not lst:
        return "[]"  # Return an empty list representation if the list is empty

    # Convert the first element to a string
    first_element = str(lst[0])

    # Recursively convert the rest of the list to a string
    rest_of_list = list_to_string_recursive(lst[1:])

    # Combine the first element and the rest of the list representation
    result = f'[{first_element}, {rest_of_list[1:]}' if rest_of_list.startswith("[") else f'[{first_element}{rest_of_list}]'

    return result

# Example usage:
my_list = [1, 2, "hello", [3, 4]]

result_string = list_to_string_recursive(my_list)

print("List as a string:", result_string)
