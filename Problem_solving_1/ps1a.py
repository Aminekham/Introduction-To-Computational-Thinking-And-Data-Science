###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:Mohammed Amine Khammassi
# Collaborators:
# Time:25/06/2023

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    #My code:
    cows_dic = {}
    with open (filename, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            formated_line = lines[i].split(",")
            final_line = formated_line[1].split("\n")
            cows_dic[formated_line[0]] = final_line[0]
    return(cows_dic)
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #My code:
    if not cows:  # Check if the dictionary is empty
        return []

    trips = []
    mutation = cows.copy()

    while mutation:
        this_sum = 0
        trip = []

        for cow in list(mutation.keys()):
            if this_sum + int(mutation[cow]) <= limit:
                this_sum += int(mutation[cow])
                trip.append(cow)
                del mutation[cow]

        trips.append(trip)

    return trips



        
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # My code :
    all_possibilities = get_partitions(cows)
    valid_trips = []
    inf = float('inf')
    for possibility in all_possibilities:
        trips = []
        valid = True
        for trip in possibility:
            weight = 0
            for cow in trip:
                weight += int(cows[cow])
                if weight > 10:
                    valid = False
                    break
            trips.append(trip)
        if valid and len(trips) < inf:
            inf = len(trips)
            valid_trips = trips
    return(valid_trips)
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # My code:
    cows = load_cows("ps1_cow_data.txt")
    start_greedy = time.time()
    greedy = greedy_cow_transport(cows)
    end_greedy = time.time()
    print(f"it took for the greedy algorithm : {end_greedy - start_greedy}")
    print(greedy)
    start_brute = time.time()
    brute = brute_force_cow_transport(cows)
    end_brute = time.time()
    print(f"it took for the brute force algorithm : {end_brute - start_brute}")
    print(brute)
if __name__ == "__main__":
    compare_cow_transport_algorithms()
