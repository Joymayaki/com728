def observed():
    observations = []
    for count in range(7):
        print("Please enter an observation:")
        observation = input()
        observations.append(observation)
    return observations


def run():
    print("Counting observations...")
    observations_list = observed()
    observations_set = set()


    for observation in observations_list:
        observation_tuple = (observation, observations_list.count(observation))
        observations_set.add(observation_tuple)

    print(observations_set)


if __name__ == "__main__":
    run()