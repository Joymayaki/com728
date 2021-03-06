# Ask user for markings  = '♯☼⌂╝ℓ'
print("What strange markings do you see?")
markings = input() # input require value

# Identify markings
print("\nIdentifying...\n")

for index in range(len(markings)): # for loop to count the range of index in the inputed value
    value = markings[index] # each character in the input value
    print(f"index {index}:", value) # print requested result

print("\nDone!")
