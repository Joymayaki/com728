# Display message
print("Program Started!")

# Ask user to enter a code
print("Please enter an ASCII code:")
code = abs( int(input()) )

# Determine which message to display
if code in range(32, 127):
    character = chr(code)
    print(f"The character represented by the ASCII value code {code} is: {character}.")
else:
    print("Invalid value")

# Display message
print("Program Ended!")