def find_max_min_k_elements(input_tuple, k):
    # Sort the tuple in ascending order
    sorted_tuple = sorted(input_tuple)

    # Find the maximum K elements
    max_k_elements = sorted_tuple[-k:]

    # Find the minimum K elements
    min_k_elements = sorted_tuple[:k]

    return max_k_elements, min_k_elements

# Example usage
input_tuple = (10, 5, 8, 2, 7, 3, 1)
k = 3

max_k_elements, min_k_elements = find_max_min_k_elements(input_tuple, k)

print(f"Original Tuple: {input_tuple}")
print(f"Maximum {k} elements: {max_k_elements}")
print(f"Minimum {k} elements: {min_k_elements}")
