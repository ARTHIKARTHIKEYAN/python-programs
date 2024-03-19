import sys

def matrix_chain_order(p):
    n = len(p) - 1
    memo = [[-1] * n for _ in range(n)]

    def matrix_multiply_chain(i, j):
        if i == j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        memo[i][j] = sys.maxsize
        for k in range(i, j):
            memo[i][j] = min(memo[i][j], matrix_multiply_chain(i, k) + matrix_multiply_chain(k + 1, j) + p[i] * p[k + 1] * p[j + 1])

        return memo[i][j]

    return matrix_multiply_chain(0, n - 1)

# Example usage:
matrix_dimensions = [10, 30, 5, 60]  # Dimensions of matrices: A1(10x30), A2(30x5), A3(5x60)
minimum_operations = matrix_chain_order(matrix_dimensions)
print("Minimum number of operations needed for matrix-chain multiplication:", minimum_operations)
