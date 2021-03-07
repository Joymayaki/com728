# The function
def identify():

    # Ask user for what lies ahead
    print("what lies before us?")
    response = input()

    # Determine which message to display
    if response == "a large boulder":
        print("\nIt's time to run!")
    else:
        print("We will be fine.")

# Call to function
identify()