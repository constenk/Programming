###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import csv

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
    # Open the file and output the data as a dictionary
    with open(filename, 'r') as data:
        return dict(csv.reader(data))

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
    # Extract the cow names (keys) and cow weights(values)
    names = list(cows.keys())
    weights_str = list(cows.values())
    
    # Convert the weights to integers
    weights = [int(i) for i in weights_str]
    
    # Initialize the parameters for the loop
    trip_idx = 0    # Index of current trip
    trip_weight = 0 # Total weight of the cows in the current trip
    trips = [[]]    # List to contain lists of the cows in each trip
    
    # Loop through and add each cow to a trip
    for i in range(len(weights)):
        # Go to the next trip all cows would exceed the weight limit
        if min(weights) + trip_weight > limit:
            trip_idx += 1
            trip_weight = 0
            trips.append([])
        
        # Sort the weights in reverse order and iterate until an acceptable
        # weight is found
        for weight in sorted(weights, reverse=True):
            if weight + trip_weight <= limit:
                break
        
        # Add the weight to the trip_weight
        trip_weight += weight
            
        # Get the index for the chosen weight
        weight_idx = weights.index(weight)
        
        # Remove the current weight from the list
        del weights[weight_idx]
        
        # Pop out the name for the current weight and assign it to 'trips'
        trips[trip_idx].append(names.pop(weight_idx))
        
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
    # Initialize variable to keep track of the best option
    best_partition = []
    
    # Extract the cow names (keys) and cow weights(values)
    names = list(cows.keys())
    weights_str = list(cows.values())
    
    # Convert the weights to integers
    weights = [int(i) for i in weights_str]
    
    # Partition the cow weights
    for partition in get_partitions(range(len(cows))):
        # If the length of this partition is not shorter than the best option
        # then continue onto the next one. Ensure the best partition isn't
        # empty
        if len(partition) >= len(best_partition) and len(best_partition) > 0:
            continue
        
        # Check that each trip meets the weight limit requirement
        partition_is_valid = True
        for trip_partition in partition:
            # Set the starting trip weight to zero
            trip_weight = 0
            
            # Loop through each cow and add the weight to the trip weight
            for cow_idx in trip_partition:
                trip_weight += weights[cow_idx]
            
            # If the trip weight exceeds the limit then the entire partition is
            # invalid
            if trip_weight > limit:
                partition_is_valid = False
                break
        
        # Update the best partition if the current partition is valid
        if partition_is_valid:
            best_partition = []
            # Assemble the nested lists containing the best names
            for trip in partition:
                best_partition.append([])
                for cow_idx in trip:
                    best_partition[-1].append(names[cow_idx])
                    
    return best_partition
                
        
# Problem 4
def compare_cow_transport_algorithms(filename):
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
    # Load the specified file data as a dictionary
    cows = load_cows(filename)
    
    # Run and time the greedy algorithm
    start = time.time()
    trips_greedy = greedy_cow_transport(cows)
    end = time.time()
    print(trips_greedy)
    print(end - start)
    
    # Run and time the brute force algorithm
    start = time.time()
    trips_brute = brute_force_cow_transport(cows)
    end = time.time()
    print(trips_brute)
    print(end - start)
