# Ask user for phrase = sucoP sucoH
print("What phrase do you see?")
phrase = input()

# Identify markings
print("\nReversing...\n")
print("The phrase is: ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)