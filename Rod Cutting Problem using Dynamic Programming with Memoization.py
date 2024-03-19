def rod_cutting(lengths, prices, rod_length):
    memo = {}

    def max_revenue(length):
        if length == 0:
            return 0
        if length in memo:
            return memo[length]
        
        max_val = -1
        for i in range(1, min(length, len(lengths)) + 1):
            max_val = max(max_val, prices[i - 1] + max_revenue(length - i))
        
        memo[length] = max_val
        return max_val

    return max_revenue(rod_length)

# Example usage:
lengths = [1, 2, 3, 4, 5, 6, 7, 8]  # Lengths of different rod pieces
prices = [1, 5, 8, 9, 10, 17, 17, 20]  # Corresponding prices of rod pieces
rod_length = 4  # Total length of the rod

max_revenue = rod_cutting(lengths, prices, rod_length)
print("Maximum revenue:", max_revenue)
