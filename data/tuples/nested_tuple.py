# The function
def steps():
    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4)
    ]

    return likelihoods


def run():
    data = steps()
    good_steps = []
    bad_steps = []

    # Determine which message to display
    for item in data:
        if item[1] >= 50:
            bad_steps.append(item)
        else:
            good_steps.append(item)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

# Call to function
if __name__ == "__main__":
    run()