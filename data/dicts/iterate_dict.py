# The function
def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


# The function with a single parameter named 'data'
def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)
    print()


# The function with a single parameter named 'data'
def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)
    print()


# The function with a single parameter named 'data'
def display_pairs(data):
    print("Key-Value Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")
    print()


def run():
    data = pattern()
    print(f"Dictionary:\n{data}")

    display_keys(data)
    display_values(data)
    display_pairs(data)

if __name__ == "__main__":
    run()
