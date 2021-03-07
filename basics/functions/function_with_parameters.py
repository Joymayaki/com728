# The function with 2 parameters named steps_remaining, steps_crossed
def climb_ladder(steps_remaining, steps_crossed):

    # Compare and display a suitable message
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


# Call to function
climb_ladder(5, 2)
climb_ladder(2, 5)