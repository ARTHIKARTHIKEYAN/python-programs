# Dictionary to store student information (roll number as key, name as value)
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    # Add more students as needed
}

# Function to display student information
def display_student_info(roll_number):
    if roll_number in students:
        print(f"Roll Number: {roll_number}, Name: {students[roll_number]}")
    else:
        print(f"Student with Roll Number {roll_number} not found.")

# Example usage:
display_student_info(102)
display_student_info(103)
