from datetime import datetime

def days_difference(date1, date2):
    date_format = "%Y-%m-%d"

    try:
        # Parse the input strings into datetime objects
        date1_obj = datetime.strptime(date1, date_format)
        date2_obj = datetime.strptime(date2, date_format)

        # Calculate the difference in days
        difference = abs((date2_obj - date1_obj).days)

        return difference
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Get user input for the two dates
try:
    date1_input = input("Enter the first date (YYYY-MM-DD): ")
    date2_input = input("Enter the second date (YYYY-MM-DD): ")

    # Calculate and print the difference in days
    result = days_difference(date1_input, date2_input)
    print(f"The difference between {date1_input} and {date2_input} is {result} days.")
except Exception as e:
    print(f"Error: {e}")
