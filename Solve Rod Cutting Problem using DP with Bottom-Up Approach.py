def rod_cutting(lengths, prices, rod_length):
    n = len(lengths)
    # Create a table to store the maximum revenue for rod lengths from 0 to rod_length.
    dp_table = [0] * (rod_length + 1)

    for i in range(1, rod_length + 1):
        max_revenue = -1
        for j in range(1, min(i, n) + 1):
            max_revenue = max(max_revenue, prices[j - 1] + dp_table[i - j])
        dp_table[i] = max_revenue

    return dp_table[rod_length]

# Example usage:
lengths = [1, 2, 3, 4, 5, 6, 7, 8]  # Lengths of different rod pieces
prices = [1, 5, 8, 9, 10, 17, 17, 20]  # Corresponding prices of rod pieces
rod_length = 4  # Total length of the rod

max_revenue = rod_cutting(lengths, prices, rod_length)
print("Maximum revenue:", max_revenue)
