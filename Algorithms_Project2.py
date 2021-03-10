# Algorithms Project 2
# Sorting
# Group Members
#       Kile Adams
#       Monique Dashner
#       Kathryn Villarreal

import time
import math
import random as rn
import statistics as st

# Bubble Sort
def bubble(numbers):
    # Best Case (Already Sorted lowest to highest)
    # Average Case (Not Sorted)
    # Worst Case (Already Sorted highest to lowest)

    # traverse through all array elements
    for i in range(len(numbers)-1):
    # range(n) also work but outer loop will repeat one more time than needed.
        for j in range(0, len(numbers)-i-1):
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
    emptylist = list()
    return emptylist

# Partition function for quick sort
def partition(arr, start, end): 
    i = (start-1)
    pivot = arr[end]
    for j in range(start,end): 
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[end] = arr[end], arr[i+1] 
    return (i+1)

def quick(arr, start, end):
    if len(arr) == 1: 
        return arr 
    if start < end: 
        pi = partition(arr, start,end) 
        quick(arr, start, pi-1) 
        quick(arr, pi+1, end) 
    return arr

# Partition function for quick sort
def best_part(arr, start, end): 
    i = (start-1)
    pivot = st.median(arr)
    for j in range(start,end): 
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[end] = arr[end], arr[i+1] 
    return (i+1)

def best_quick(arr, start, end):
    if len(arr) == 1: 
        return arr 
    if start < end: 
        pi = best_part(arr, start,end) 
        best_quick(arr, start, pi-1) 
        best_quick(arr, pi+1, end) 
    return arr

# Counting sort function for radix sort
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
    for i in range(0, len(numbers)):
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
    length = rn.randint(100000, 10000000)
    # Fill the array with random integers
    rand_array = [rn.randint(0, 1000000) for i in range(length)]
    # return the generated array
    return rand_array

def ascending():
    # Generate an array with length between 100000 to 1000000
    length = rn.randint(100000, 10000000)
    # have the array be filled with numbers in ascending order
    asc_array = [i for i in range(length)]
    # return generated array
    return asc_array

def descending():
    # Generate an array with length between 100000 to 1000000
    length = rn.randint(100000, 10000000)
    # have the array be filled with numbers in descending order
    desc_array = [(length-i) for i in range(length)]
    # return generated array
    return desc_array

def write_file(file, sort, sorted, time):
    # Open the file
    f = open(file, "a")
    # Write to the file the sorting algorithm, 
    #       the sorted array and array length,
    #       the time it took to sort
    f.write(sort + " Sort Time: " + str(time) + "\n")
    f.write("Array Length: " + str(len(sorted))+ "\n")
    f.write("Sorted Array: " + str(sorted) + "\n\n")

    f.close()

def average_case(numbers, file_name):
    f = open(file_name, "a")
    f.write("Average Case for Algorithms\n")
    f.close()

    srt = time.time()
    # Test Bubble sort with random array
    sorted = bubble(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Bubble", sorted, t)

    srt = time.time()
    # Test Merge sort with random array
    sorted = merge(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Merge", sorted, t)

    srt = time.time()
    # Test Quick sort with random array
    sorted = quick(numbers, 0, (len(numbers)-1))
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Quick", sorted, t)

    srt = time.time()
    # Test Radix sort with random array
    sorted = radix(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Radix", sorted, t)

    return 0

def best_case(numbers, file_name):
    f = open(file_name, "a")
    f.write("Best Case for Algorithms\n")
    f.close()

    srt = time.time()
    # Test Bubble sort with ascending array
    sorted = bubble(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Bubble", sorted, t)

    srt = time.time()
    # Test Merge sort with (doesn't matter) array
    sorted = merge(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Merge", sorted, t)

    srt = time.time()
    # Test Quick sort with an array that the pivot chosen is always the middle
    sorted = best_quick(numbers, 0, len(numbers)-1)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Quick", sorted, t)

    srt = time.time()
    # Test Radix sort with (????) array
    sorted = radix(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Radix", sorted, t)

    return 0

def worst_case(numbers, file_name):
    f = open(file_name, "a")
    f.write("Worst Case for Algorithms\n")
    f.close()

    srt = time.time()
    # Test Bubble sort with descending array
    sorted = bubble(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Bubble", sorted, t)

    srt = time.time()
    # Test Merge sort with (doesn't matter) array
    sorted = merge(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Merge", sorted, t)

    srt = time.time()
    # Test Quick sort with an array that the pivot chosen is always the lowest or highest
    sorted = quick(numbers, 0, len(numbers)-1)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Quick", sorted, t)

    srt = time.time()
    # Test Radix sort with (??????) array
    sorted = radix(numbers)
    t = time.time()-srt
    # Write to file
    write_file(file_name, "Radix", sorted, t)

    return 0

if __name__ == "__main__":
    # Generate a random array
    rand = rand_array()
    # Generate ascending array
    ascend = ascending()
    # Generate descending array
    descend = descending()
    # Generate any other neccesary arrays

    # Test best case
    best_case(ascend, "test.txt")
    # Test worst case
    worst_case(descend, "test.txt")
    # test average case
    average_case(rand, "test.txt")