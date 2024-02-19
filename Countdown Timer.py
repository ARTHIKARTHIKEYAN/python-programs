import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

def main():
    try:
        # Get input from the user for the countdown duration
        seconds = int(input("Enter the countdown duration in seconds: "))
        
        # Validate the input
        if seconds <= 0:
            raise ValueError("Please enter a positive duration.")

        # Start the countdown timer
        countdown_timer(seconds)

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
