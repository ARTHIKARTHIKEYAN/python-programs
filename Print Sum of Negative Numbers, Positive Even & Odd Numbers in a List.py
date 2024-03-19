def sum_numbers(lst):
    sum_negative = 0
    sum_even = 0
    sum_odd = 0

    for num in lst:
        if num < 0:
            sum_negative += num
        elif num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_negative, sum_even, sum_odd

# Example usage:
my_list = [-2, -1, 0, 1, 2, 3, 4, 5]

negative_sum, even_sum, odd_sum = sum_numbers(my_list)

print("Sum of negative numbers:", negative_sum)
print("Sum of positive even numbers:", even_sum)
print("Sum of positive odd numbers:", odd_sum)
