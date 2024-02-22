def list_to_string_with_for_loop(lst):
    result_string = "["

    for element in lst:
        # Convert the element to a string and append it to the result string
        result_string += str(element) + ", "

    # Remove the trailing comma and space, if the list is not empty
    if len(result_string) > 1:
        result_string = result_string[:-2]

    result_string += "]"

    return result_string

# Example usage:
my_list = [1, 2, "hello", [3, 4]]

result_string = list_to_string_with_for_loop(my_list)

print("List as a string:", result_string)
