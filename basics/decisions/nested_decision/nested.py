# Ask user for book details
print("What type of cover does this book have?")
cover_type = input()

# Display appropriate message
if cover_type == "soft":
    print("\nIs the book perfect-bound?")
    perfect_bound = input()

    if perfect_bound == "yes":
        print("\nSoft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")


