def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if target is found
    return -1  # Return -1 if target is not found

# Example usage:
arr = [5, 10, 15, 20, 25]
target = 15
index = linear_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found.")
