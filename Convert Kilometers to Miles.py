def km_to_miles(kilometers):
    # Conversion factor: 1 kilometer is approximately 0.621371 miles
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles

def main():
    try:
        # Get input from the user
        kilometers = float(input("Enter distance in kilometers: "))
        
        # Check if the input is non-negative
        if kilometers < 0:
            raise ValueError("Please enter a non-negative distance.")

        # Convert kilometers to miles
        miles = km_to_miles(kilometers)

        # Display the result
        print(f"{kilometers} kilometers is approximately equal to {miles:.2f} miles.")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
