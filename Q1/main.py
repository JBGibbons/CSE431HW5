import random
import timeit
import matplotlib.pyplot as plt
# 
# Geeks for Geeks Merge Sort 
# https://www.geeksforgeeks.org/python-program-for-merge-sort/
# 

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
        
        
        


# 
# Geeks for Geeks Insertion Sort implementation 
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
# 

def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
   
def createData(points):
    # Create an array with size n
    lst = []
    for i in range(points):
        lst.append(random.randrange(-100000,100000))

    return lst

random.seed(5)
tests = 1500
mergeSortTime = []
insertionSortTime = []
t = 0
for test in range(150):
    data = createData(t)
    executionTimeM = timeit.timeit(lambda: mergeSort(data, 0, len(data)-1), number=10)
    mergeSortTime.append((len(data), executionTimeM))
    t += 10

t = 0
for test in range(150):
    data = createData(t)
    executionTimeI = timeit.timeit(lambda: insertionSort(data), number = 10)
    insertionSortTime.append((len(data), executionTimeI))
    t += 10

# print(insertionSortTime, mergeSortTime)
dataCountM, timeM = zip(*mergeSortTime)
plt.plot(dataCountM, timeM, marker = 'o', linestyle = '-', label = 'MergeSort')

dataCountI, timeI = zip(*insertionSortTime)
plt.plot(dataCountI, timeI, marker='x', linestyle = '--', label = 'InsertionSort')
plt.show()
