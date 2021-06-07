import random

values = random.sample(list(range(1, 10000)), 1000)
values.sort()


def binary_search(value_to_find, array_to_search, start, end):
    result = -1
    #Have to catch unsorted arrays, as they are included in the test cases.
    array_to_search.sort()
    #Base cases: The start/end pointers will catch the case of no more array to search, and return False/-1/None case.
    if end - start + 1 <= 0:
        return result
    #If the middle index is the value, it'll return the index.
    middle_index = start + (end-start)//2
    if array_to_search[middle_index] == value_to_find:
        return middle_index

    # This logic checks the target against the array and if lower, 
    # recurses to the lower half of the searched array, and if higher, 
    # to the upper half using manipulation of the middle index, start, 
    # and end pointers as they are passed back into the function.
    if value_to_find < (array_to_search[middle_index]):
        return(binary_search(value_to_find, array_to_search, start, middle_index-1))
    elif value_to_find > (array_to_search[middle_index]):
        return(binary_search(value_to_find, array_to_search, middle_index+1, end))
