def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    # Calculate the value per unit weight for each item
    value_per_weight = [(values[i] / weights[i], weights[i]) for i in range(n)]
    # Sort items by value per unit weight in descending order
    value_per_weight.sort(reverse=True)

    max_value = 0

    for value_per_unit, weight in value_per_weight:
        if capacity >= weight:
            max_value += value_per_unit * weight
            capacity -= weight
        else:
            max_value += value_per_unit * capacity
            break

    return max_value

# Example usage:
weights = [10, 20, 30]  # Weights of the items
values = [60, 100, 120]  # Corresponding values of the items
capacity = 50  # Capacity of the knapsack

max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value that can be obtained:", max_value)
