def print_square(rows, cols):
    for i in range(rows):
        print("*" * cols)

# Example usage:
rows_to_print = int(input("Enter the number of rows for the square: "))
cols_to_print = int(input("Enter the number of columns for the square: "))
print_square(rows_to_print, cols_to_print)
