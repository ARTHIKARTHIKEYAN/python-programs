def minimize_lateness(tasks):
    tasks.sort(key=lambda x: x[1])  # Sort tasks by their deadlines
    current_time = 0
    total_lateness = 0

    for task in tasks:
        start_time, deadline = task
        lateness = max(0, current_time + start_time - deadline)  # Calculate lateness
        total_lateness += lateness
        current_time += start_time  # Update current time

    return total_lateness

# Example usage:
tasks = [(2, 4), (1, 7), (3, 5), (5, 10)]  # Each task represented by a tuple (start_time, deadline)
minimized_lateness = minimize_lateness(tasks)
print("Total Lateness:", minimized_lateness)
