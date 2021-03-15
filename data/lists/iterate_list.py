# The function
def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

# The function
def menu():
    print("Please select a direction:")
    dirs = directions()

  # With index-based Loop
    for index in range(len(dirs)):
        direction = dirs[index]
        print(f"{index}: {direction}")


# Call to function
def run():
    menu()


if __name__ == "__main__":
    run()