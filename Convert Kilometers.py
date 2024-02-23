# Function to convert kilometers to miles
def km_to_miles(kilometers):
    conversion_factor = 0.621371  # 1 kilometer is approximately 0.621371 miles
    miles = kilometers * conversion_factor
    return miles

# Input: Get the distance in kilometers from the user
kilometers = float(input("Enter distance in kilometers: "))

# Convert kilometers to miles
miles = km_to_miles(kilometers)

# Display the converted distance
print(f"{kilometers} kilometers is equal to {miles:.2f} miles")
