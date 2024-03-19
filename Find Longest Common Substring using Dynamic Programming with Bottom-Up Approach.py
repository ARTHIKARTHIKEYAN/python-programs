def longest_common_substring(string1, string2):
    m = len(string1)
    n = len(string2)

    # Create a table to store lengths of longest common suffixes of substrings.
    # Initialize all values in the table to 0.
    dp_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length of the longest common substring and its ending position.
    max_length = 0
    max_length_end_pos = 0

    # Fill the dp_table using bottom-up dynamic programming approach.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                if dp_table[i][j] > max_length:
                    max_length = dp_table[i][j]
                    max_length_end_pos = i
            else:
                dp_table[i][j] = 0

    # Extract the longest common substring using its ending position and length.
    longest_substring = string1[max_length_end_pos - max_length:max_length_end_pos]

    return longest_substring

# Example usage:
string1 = "abcdefg"
string2 = "xbcdyz"
print("Longest common substring:", longest_common_substring(string1, string2))
