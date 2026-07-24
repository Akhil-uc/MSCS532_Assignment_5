# Import the required libraries
import random      # Used for selecting a random pivot in Randomized Quicksort
import time        # Used to measure the execution time of the algorithms


# Partition Function
# This function rearranges the elements in the array so that:
# - Elements smaller than or equal to the pivot are placed on the left.
# - Elements greater than the pivot are placed on the right.
# The pivot is chosen as the last element of the current subarray.
def split_section(numbers, start, end):

    # Select the last element as the pivot
    pivot_value = numbers[end]

    # boundary keeps track of the position where the next smaller element
    # should be placed.
    boundary = start - 1

    # Traverse all elements except the pivot
    current = start

    while current < end:

        # If the current element is smaller than or equal to the pivot
        if numbers[current] <= pivot_value:

            # Move the boundary of smaller elements forward
            boundary += 1

            # Swap the current element with the smaller element position
            numbers[boundary], numbers[current] = (
                numbers[current],
                numbers[boundary]
            )

        current += 1

    # Place the pivot in its correct sorted position
    numbers[boundary + 1], numbers[end] = (
        numbers[end],
        numbers[boundary + 1]
    )

    # Return the pivot index
    return boundary + 1


# Deterministic Quicksort
# This version always chooses the LAST element as the pivot.
def fixed_quicksort(numbers, start=0, end=None):

    # If high is not provided, use the last index of the array
    if end is None:
        end = len(numbers) - 1

    # Continue only if there is more than one element
    if start < end:

        # Partition the array and get the pivot position
        pivot_location = split_section(numbers, start, end)

        # Recursively sort the left subarray
        fixed_quicksort(numbers, start, pivot_location - 1)

        # Recursively sort the right subarray
        fixed_quicksort(numbers, pivot_location + 1, end)

    # Return the sorted array
    return numbers


# Randomized Partition
# Instead of always choosing the last element as pivot,
# this function selects a random element and swaps it with
# the last element before partitioning.
def random_split(numbers, start, end):

    # Select a random index between low and high
    chosen = random.randint(start, end)

    # Swap the randomly selected element with the last element
    numbers[chosen], numbers[end] = numbers[end], numbers[chosen]

    # Perform normal partitioning
    return split_section(numbers, start, end)


# Randomized Quicksort
# This version uses a randomly selected pivot to reduce
# the probability of worst-case performance.
def random_quicksort(numbers, start=0, end=None):

    # If high is not provided, use the last index
    if end is None:
        end = len(numbers) - 1

    # Continue only if there is more than one element
    if start < end:

        # Partition the array using a random pivot
        pivot_location = random_split(numbers, start, end)

        # Recursively sort the left part
        random_quicksort(numbers, start, pivot_location - 1)

        # Recursively sort the right part
        random_quicksort(numbers, pivot_location + 1, end)

    # Return the sorted array
    return numbers


# Benchmark Function
# This function compares the execution time of
# Deterministic Quicksort and Randomized Quicksort.
def run_benchmark():

    # Print table heading
    print("Size\tDet(ms)\tRand(ms)")

    # Test different input sizes
    test_sizes = [1000, 2000, 5000]

    index = 0

    while index < len(test_sizes):

        current_size = test_sizes[index]

        # Generate a list of random integers
        values = []

        for _ in range(current_size):
            values.append(random.randint(1, 100000))

        # Create separate copies so both algorithms
        # sort identical data
        first_list = list(values)
        second_list = values.copy()

        # Measure execution time of Deterministic Quicksort
        begin = time.perf_counter()
        fixed_quicksort(first_list)
        fixed_time = (time.perf_counter() - begin) * 1000

        # Measure execution time of Randomized Quicksort
        begin = time.perf_counter()
        random_quicksort(second_list)
        random_time = (time.perf_counter() - begin) * 1000

        # Display the results
        print("{}\t{:.2f}\t{:.2f}".format(
            current_size,
            fixed_time,
            random_time
        ))

        index += 1


# Main Program
# The benchmark function is executed only when this file
# is run directly.
if __name__ == "__main__":
    run_benchmark()