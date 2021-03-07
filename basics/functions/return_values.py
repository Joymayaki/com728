# The function
def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = sum_weights(beep_weight, bop_weight) / 2
    return avg_weight

def run():
    # retrieve required user data
    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("\nWhat is the weight of Beep?")
    beep_weight = float(input())

    print("\nWhat would you like to calculate (sum or average)?")
    action = input()

    # determine and carry out action
    if action == "sum":
        answer = sum_weights(beep_weight, bop_weight)
        print(f"\nThe sum of Beep's and Bop's weight is {answer:.2f}")
    elif action == "average":
        answer = calc_avg_weight(beep_weight, bop_weight)
        print(f"\nThe average of Beep's and Bop's weight is {answer:.2f}")
    else:
        print("I am not sure what you would like to do.")

# call to function
run()