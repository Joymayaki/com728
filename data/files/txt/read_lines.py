# The function with a single parameter named 'file_path'
def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("Done!")


# call to function
def run():
    search("library.txt")


if __name__ == "__main__":
    run()