# The function
def observed():
    observations = []

    for count in range(5):
        print("Please enter an observation")
        observations.append(input())
    return observations


# The function with a single parameter named "observations"
def remove_observations(observations):
    is_looping = True
    while is_looping:
        print("Do you wish to remove an observation?")
        response = input()
        if response.lower() == "yes":
            print("Please enter the observation you wish to remove")
            observation = input()
            observations.remove(observation)
        else:
            is_looping = False


# The function
def run():
    observations_list = observed()
    remove_observations(observations_list)

    # populate set
    observations_set = set()

    for observation in observations_list:
        observation_tuple = (observation, observations_list.count(observation))
        observations_set.add(observation_tuple)

    # display set
    print(sorted(observations_set))


if __name__ == "__main__":
    run()


