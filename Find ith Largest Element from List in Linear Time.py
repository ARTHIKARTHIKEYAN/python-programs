import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def random_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]
    return partition(arr, low, high)

def quick_select(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = random_partition(arr, low, high)
    
    if pivot_index == k:
        return arr[pivot_index]
    elif pivot_index < k:
        return quick_select(arr, pivot_index + 1, high, k)
    else:
        return quick_select(arr, low, pivot_index - 1, k)

# Example usage:
arr = [3, 2, 1, 5, 6, 4]
i = 2  # Find the 2nd largest element
ith_largest = quick_select(arr, 0, len(arr) - 1, len(arr) - i)
print(f"{i}nd largest element:", ith_largest)
