def sort_by_length(lst):
    return sorted(lst, key=len)

# Example usage:
my_list = ["apple", "banana", "kiwi", "orange", "grape"]
sorted_list = sort_by_length(my_list)
print("Sorted list according to length:", sorted_list)
