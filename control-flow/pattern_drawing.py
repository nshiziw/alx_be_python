# Get the size of the pattern from the user
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for rows
row = 0

# Use a while loop to iterate through rows
while row < size:
    # Use a for loop to print the asterisks in each row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    
    # After printing a row, print a newline to move to the next row
    print()
    
    # Increment the row counter
    row += 1
