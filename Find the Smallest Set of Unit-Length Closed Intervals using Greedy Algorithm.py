def smallest_set_of_intervals(points):
    # Sort points in ascending order
    points.sort()
    intervals = []
    i = 0

    while i < len(points):
        start = points[i]
        end = start + 1
        intervals.append((start, end))

        # Skip all points covered by the current interval
        while i < len(points) and points[i] <= end:
            i += 1

    return intervals

# Example usage:
points = [0.2, 0.8, 1.1, 2.2, 3.0, 3.7, 4.5, 5.5, 6.2, 7.3, 8.0, 9.0]
intervals = smallest_set_of_intervals(points)
print("Smallest Set of Unit-Length Closed Intervals:", intervals)
