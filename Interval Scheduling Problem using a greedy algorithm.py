def interval_scheduling(intervals):
    # Sort intervals by their end times
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    # Initialize the result list with the first interval
    result = [sorted_intervals[0]]
    
    # Iterate through the sorted intervals
    for interval in sorted_intervals[1:]:
        # If the start time of the current interval is greater than or equal to 
        # the end time of the last interval in the result list, add it to the result list
        if interval[0] >= result[-1][1]:
            result.append(interval)
    
    return result

# Example usage:
intervals = [(1, 3), (2, 4), (3, 6), (5, 7), (8, 9), (9, 10)]
scheduled_intervals = interval_scheduling(intervals)
print("Scheduled Intervals:", scheduled_intervals)
