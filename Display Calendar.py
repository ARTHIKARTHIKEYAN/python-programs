import calendar

def display_calendar(year, month):
    try:
        # Generate the calendar for the specified year and month
        cal = calendar.month(year, month)

        # Display the calendar
        print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
        print(cal)

    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        # Get input from the user
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        
        # Validate the input
        if not (1 <= month <= 12):
            raise ValueError("Invalid month. Please enter a number between 1 and 12.")

        # Display the calendar
        display_calendar(year, month)

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
