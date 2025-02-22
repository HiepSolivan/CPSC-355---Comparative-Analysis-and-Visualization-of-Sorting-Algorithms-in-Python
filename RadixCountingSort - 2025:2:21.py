# Radix Sort

import random

def CountingSort(array, exp):
    n = len(array)
    output = [0] * n # Construct array of n number of zerores
    bucket_count = [0] * 10

    # Count occurences of each digit in the current place value
    for i in range(n):
        index = (array[i] // exp) % 10
        bucket_count[index] += 1

    # Update count[i] so that it contains the actual position in the output[]
    for i in range(1, 10):
        bucket_count[i] += bucket_count[i - 1] # Cumulative sum for stable sorting

    # Build the output array by placing the elements in correct order
    for i in range(n - 1, -1, -1):
        index = (array[i] // exp) % 10
        output[bucket_count[index] - 1] = array[i]
        bucket_count[index] -= 1 # Decrement count to handle duplicates

    # Copy sorted array back into the array
    for i in range(n):
        array[i] = output[i] # Overwrite original array with sorted values

def RadixSort(array):
    # Least Significant Digit (LSD) approach
    # Find the maximum number to determine the number of digits
    max_num = max(array)
    exp = 1

    # Continue sorting for each digit place value
    while max_num // exp > 0:
        CountingSort(array, exp)
        exp *= 10
    return array

#Generate a random list of numbers
random_list = [random.randint(10, 9999) for _ in range(10)]

print("Original Array: ", random_list)
sorted_array = RadixSort(random_list)
print("Sorted Array: ", sorted_array)
