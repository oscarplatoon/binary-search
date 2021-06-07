import random

values = random.sample(list(range(1, 10000)), 1000)
values.sort()

def binary_search(value_to_find, array_to_search, start, end):
    result = -1

    middle_index = len(array_to_search)//2
    print(f"The middle index is: {middle_index}")
    if value_to_find == (array_to_search[middle_index]):
        return middle_index
    if len(array_to_search) == 1:
        return result

    if value_to_find < (array_to_search[middle_index]):
        binary_list = array_to_search[:middle_index]
        print(binary_list)
        binary_search(value_to_find, binary_list)
    elif value_to_find > (array_to_search[middle_index]):
        binary_list = array_to_search[middle_index:]
        print(binary_list)
        binary_search(value_to_find, binary_list)


    return result

# Assumptions, list is sorted when passed in, use recursion
# array_to_search[middle_index] < val to find
# array_to_search[middle_index] > val to find
# # array_to_search[middle_index] == val to find
# Base case is when the middle_index is the value to find. Return middle index
# Exit condition, if the value to find is not in the list is when the length of the list is 1
# How to track the halving of the arrays between recursions. counter? 


super_big_array = [1, 5, 7, 2, 3, 8, 4, 9]
super_big_array.sort()
# print(binary_search(3, [1, 2, 3, 4]))
# print(binary_search(6, super_big_array))
print(binary_search(7, super_big_array))
