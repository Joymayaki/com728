print("What are you buying (shoe, bag, dress or trouser)?")
buying = input()
print()
if buying == "shoe":
    print("I am buying a shoe!")
elif buying == "bag":
    print("I am buying a bag!")
elif buying == "dress":
    print("I am buying a dress!")
elif buying == "trouser":
    print("I am buying a trouser!")
else:
    print("I am not sure of what I am buying!")

print()
print("What type of doors are in your house?")
door = input().lower().strip()
print()
if door == "modern":
    print("Is the house newly-built ?")
    built = input().lower().strip()

    if built == "yes":
        print("\nModern door, newly built houses are very expensive!")
    else:
        print("Modern doors with code locks or face recognition are safe to live in")

elif cover == "old":
    print("house with old doors are not common!")

print()
print("What type of party should i have?")
party = input()

if (party == "dinner") or (party == "pool"):
    print("\nnice!")
elif (party == "garden") or (party == "cocktail"):
    print("\ngreat!")
else:
    print("Not sure if it will be fun.")

print()
print("What model is it?")
model = input()
print()
print("What brand is it?")
brand = input()
print()
if (model == "Model S") and (brand == "Tesla"):
    print("It is new. I should get one!")
else:
    print("It's nice but expensive")