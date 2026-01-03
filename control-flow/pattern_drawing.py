# Get the pattern size from the user
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing the row
    print()
    # Increment the row counter
    row += 1
