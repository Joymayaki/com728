import csv


# The function with a single parameter named 'file_path'
def run(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{headings}")

        print("Values:")
        for values in csv_reader:
            print(values)


# call to function
def run():
    def run():
        read("bots.csv")


if __name__ == "__main__":
    run()
