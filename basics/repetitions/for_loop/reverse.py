# Ask user for phrase = sucoP sucoH
print("What phrase do you see?")
phrase = input()

# Identify markings
print("\nReversing...\n")
print("The phrase is ", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")