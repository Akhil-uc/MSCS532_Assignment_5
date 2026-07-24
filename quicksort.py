# Import the required libraries
import random      # Used for selecting a random pivot in Randomized Quicksort
import time        # Used to measure the execution time of the algorithms


# Partition Function
# This function rearranges the elements in the array so that:
# - Elements smaller than or equal to the pivot are placed on the left.
# - Elements greater than the pivot are placed on the right.
# The pivot is chosen as the last element of the current subarray.
def partition(arr, low, high):

    # Select the last element as the pivot
    pivot = arr[high]

    # i keeps track of the position where the next smaller element
    # should be placed.
    i = low - 1

    # Traverse all elements except the pivot
    for j in range(low, high):

        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:

            # Move the boundary of smaller elements forward
            i += 1

            # Swap the current element with the smaller element position
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the pivot index
    return i + 1


# Deterministic Quicksort
# This version always chooses the LAST element as the pivot.
def quicksort(arr, low=0, high=None):

    # If high is not provided, use the last index of the array
    if high is None:
        high = len(arr) - 1

    # Continue only if there is more than one element
    if low < high:

        # Partition the array and get the pivot position
        pi = partition(arr, low, high)

        # Recursively sort the left subarray
        quicksort(arr, low, pi - 1)

        # Recursively sort the right subarray
        quicksort(arr, pi + 1, high)

    # Return the sorted array
    return arr


# Randomized Partition
# Instead of always choosing the last element as pivot,
# this function selects a random element and swaps it with
# the last element before partitioning.
def randomized_partition(arr, low, high):

    # Select a random index between low and high
    idx = random.randint(low, high)

    # Swap the randomly selected element with the last element
    arr[idx], arr[high] = arr[high], arr[idx]

    # Perform normal partitioning
    return partition(arr, low, high)


# Randomized Quicksort
# This version uses a randomly selected pivot to reduce
# the probability of worst-case performance.
def randomized_quicksort(arr, low=0, high=None):

    # If high is not provided, use the last index
    if high is None:
        high = len(arr) - 1

    # Continue only if there is more than one element
    if low < high:

        # Partition the array using a random pivot
        pi = randomized_partition(arr, low, high)

        # Recursively sort the left part
        randomized_quicksort(arr, low, pi - 1)

        # Recursively sort the right part
        randomized_quicksort(arr, pi + 1, high)

    # Return the sorted array
    return arr


# Benchmark Function
# This function compares the execution time of
# Deterministic Quicksort and Randomized Quicksort.
def benchmark():

    # Print table heading
    print("Size\tDet(ms)\tRand(ms)")

    # Test different input sizes
    for n in [1000, 2000, 5000]:

        # Generate a list of random integers
        data = [random.randint(1, 100000) for _ in range(n)]

        # Create separate copies so both algorithms
        # sort identical data
        a = data.copy()
        b = data.copy()

        # Measure execution time of Deterministic Quicksort
        start = time.perf_counter()
        quicksort(a)
        deterministic_time = (time.perf_counter() - start) * 1000

        # Measure execution time of Randomized Quicksort
        start = time.perf_counter()
        randomized_quicksort(b)
        randomized_time = (time.perf_counter() - start) * 1000

        # Display the results
        print(f"{n}\t{deterministic_time:.2f}\t{randomized_time:.2f}")


# Main Program
# The benchmark function is executed only when this file
# is run directly.
if __name__ == "__main__":
    benchmark()