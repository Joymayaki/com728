# Display message
print("Program Started!")

# Ask user to enter a letter
print("Please enter a standard character:")
letter = input()

# Determine which message to display
if len(letter) == 1:
    value = ord(letter)
    print(f"The ASCII code for {letter} is: {value}")
else:
    print(" A single character was expected")

# Display message
print("Program Ended!")
