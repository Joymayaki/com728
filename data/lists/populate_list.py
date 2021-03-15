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

    selected_option = int(input())
    return dirs[selected_option]


    # Display message
def run():
    route = []
    print("Working out escape route...")

    for count in range(5):
        direction = menu()
        route.append(direction)

    print(f"Escape route: {route}")


# Call to function
if __name__ == "__main__":
    run()
