# Algorithms Project 2
# Sorting
# Group Members
#       Kile Adams
#       Monique Dashner
#       Kathryn Villarreal

import time
import math
import random as rn

# Bubble Sort
def bubble(numbers):
    # Best Case (Already Sorted lowest to highest)
    # Average Case (Not Sorted)
    # Worst Case (Already Sorted highest to lowest)

    # INSERT ALGORITHM HERE
    n = len(numbers)

    # traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one more time than needed.

            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


    # Return sorted array
    return numbers

# Merge Sort
def merge(numbers):
    # No matter what case always the same time complexity 

    # INSERT ALGORITHM HERE

    # Return sorted array
    return 0

# Quick Sort
def quick(numbers):
    # Start at the end and use it as the pivot
    # Average Case 
    # Worst Case (Always picking the greatest or smallest number as a pivot)

    # INSERT ALGORITHM HERE

    # Return sorted array
    return 0

def best_quick(numbers):
    # Best Case
    # Always use the median as the pivot

    # INSERT ALGORITHM HERE

    # Return sorted array
    return 0

#   Counting sort function for radix sort

def countingSort(numbers, exp):
    n = len(numbers)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (numbers[i] / exp)
        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (numbers[i] / exp)
        output[count[int(index % 10)] - 1] = numbers[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        numbers[i] = output[i]

    return numbers

    # Radix Sort
def radix(numbers):
    # Best Case
    # Average Case
    # Worst Case

    # INSERT ALGORITHM HERE
    max1 = max(numbers)

    exp = 1
    while max1 / exp > 0:
        countingSort(numbers, exp)
        exp *= 10

    # Return sorted array
    return numbers

def rand_array():
    # Generate an array with length between 100000 to 1000000
    length = rn.randint(100000, 1000000)
    # Fill the array with random integers
    rand_array = [rn.randint(0, 1000000) for i in range(length)]
    # return the generated array
    return rand_array

def ascending():
    # Generate an array with length between 100000 to 1000000
    length = rn.randint(100000, 1000000)
    # have the array be filled with numbers in ascending order
    asc_array = [i for i in range(length)]
    # return generated array
    return asc_array

def descending():
    # Generate an array with length between 100000 to 1000000
    length = rn.randint(100000, 1000000)
    # have the array be filled with numbers in descending order
    desc_array = [(length-i) for i in range(length)]
    # return generated array
    return desc_array

def write_file(file, sort, sorted_array, time):
    # Open the file
    # Write to the file the sorting algorithm, 
    #       the sorted array and array length,
    #       the time it took to sort

    return 0

def average_case(numbers, file_name):
    f = open(file_name, "a")
    f.write("Average Case for Algorithms")

    srt = time.time()
    # Test Bubble sort with random array
    sorted = bubble(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Bubble Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Merge sort with random array
    sorted = merge(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Merge Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Quick sort with random array
    sorted = quick(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Quick Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Radix sort with random array
    sorted = radix(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Radix Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    return 0

def best_case(numbers, file_name):
    f = open(file_name, "a")
    f.write("Best Case for Algorithms")

    srt = time.time()
    # Test Bubble sort with ascending array
    sorted = bubble(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Bubble Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Merge sort with (doesn't matter) array
    sorted = merge(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Merge Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Quick sort with an array that the pivot chosen is always the middle
    sorted = best_quick(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Quick Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Tree sort with (????) array
    sorted = radix(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Radix Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    return 0

def worst_case(numbers, file_name):
    f = open(file_name, "a")
    f.write("Worst Case for Algorithms")

    srt = time.time()
    # Test Bubble sort with descending array
    sorted = bubble(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Bubble Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Merge sort with (doesn't matter) array
    sorted = merge(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Merge Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Quick sort with an array that the pivot chosen is always the lowest or highest
    sorted = quick(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Quick Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    srt = time.time()
    # Test Tree sort with (??????) array
    sorted = radix(numbers)
    t = time.time()-srt
    # Write to file
    f.write("Radix Sort Time: " + str(t))
    f.write("Array Length: " + str(sorted.len()))
    f.write("Sorted Array: " + sorted + "\n\n")

    return 0

if __name__ == "__main__":
    # Generate a random array
    rand = rand_array()
    # Generate ascending array
    ascend = ascending()
    # Generate descending array
    descend = descending()
    # Generate any other neccesary arrays
    
    print("Oh shit, here we go again")

    # Test best case
    # Test worst case
    # test average case