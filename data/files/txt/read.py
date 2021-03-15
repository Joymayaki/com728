# The function with 2 parameters named file_path, num_chars
def display_chars(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(data)


# The function with a single parameter named 'file_path'
def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)


# The function with a single parameter named 'file_path'
def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


# Call to function
def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()