# Handling invalid conversion (ValueError if the string is not a valid integer)
invalid_string = "abc"
try:
    integer_number = int(invalid_string)
    print(integer_number)
except ValueError as e:
    print(f"Error: {e}")
