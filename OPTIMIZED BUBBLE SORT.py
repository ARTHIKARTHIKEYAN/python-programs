def optimized_bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Set a flag to check if any swaps are made in this pass
        swapped = False

        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swaps were made in this pass, the array is already sorted
        if not swapped:
            break

# Example usage:
my_list = [64, 25, 12, 22, 11]
optimized_bubble_sort(my_list)

print("Sorted array:", my_list)
