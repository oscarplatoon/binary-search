# sort list
# find middle of list
# see if num_to_find matches number in middle of list
# if num_to_find matches number in middle of list; return index of number in middle of list.
# if num_to_match does not match number in middle of list, assess whether num_to_match is > or < in regards to number in middle of list.
# eliminate the half of the list that the num_to_match is not on and pick number in middle of new list; list that is not 1/2 length of original list.
# repeat until number is found.  However, if length of list is reduced to 1 and num_to_match still isn't found, return -1 and exit function.


def binary_search(num_to_find, list):
    sorted_list = sorted(list)
    index_to_find = None
    counter = 0
    
    while index_to_find == None and counter < 5:
        middle_number_index = (len(sorted_list) - 1) // 2
        middle_number = sorted_list[middle_number_index]
        print(sorted_list)
        print(f"middle number index: {middle_number_index}")
        print(f"middle number: {middle_number}")
        
        if num_to_find == middle_number:
            index_to_find = sorted_list[middle_number]
            break
        elif num_to_find > middle_number:
            sorted_list = sorted_list[middle_number_index:]
        elif num_to_find < middle_number:
            sorted_list = sorted_list[:middle_number_index]
        else:
            index_to_find = -1
        counter += 1
        
    return index_to_find
        
# # super_big_array = [1,5,7,2,3,8,4,9]
print(binary_search(8, [1,5,7,2,3,8,4,9]))
# # print(binary_search(6, super_big_array) == -1)