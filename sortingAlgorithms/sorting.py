#bubble sort
def bubble_sort(array):
    n = len(array)
    #traverse through all array elements
    for i in range(n):
        #last i elements are already sorted
        for j in range(0, n-i-1):
            #swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


#selection sort
def selection_sort(array):
    n = len(array)
    #traverse through all array elements
    for i in range(n):
        #find the min element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
            #swap the found min element with the first element
        array[i], array[min_index] = array[min_index], array[i]
        
    return array


#insertion sort
def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
            
        array[j+1] = key
    return array


#merge helper function
def merge(array1, array2):
    result = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1
    while i < len(array1):
        result.append(array1[i])
        i+=1
    while j < len(array2):
        result.append(array2[j])
        j+=1
    return result

#merge sort
def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return merge(merge_sort(left), merge_sort(right))


#swap function
def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

#pivot function
def pivot(array, pivotIndex=0, endIndex=None):
    if endIndex is None:
        endIndex = len(array) - 1
    swapIndex = pivotIndex
    for i in range(pivotIndex + 1, endIndex + 1):
        if array[i] < array[pivotIndex]:
            swapIndex +=1
            swap(array, i, swapIndex)
    swap(array, pivotIndex, swapIndex)
    return swapIndex


#quick sort
def quick_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left < right:
        pivotIndex = pivot(array, left, right)
        quick_sort(array, left, pivotIndex - 1)
        quick_sort(array, pivotIndex + 1, right)
    return array


myArray = [5,2,9,1,5]
print(bubble_sort(myArray))
print(selection_sort(myArray))
print(insertion_sort(myArray))
print(merge_sort(myArray))
print(quick_sort(myArray))
