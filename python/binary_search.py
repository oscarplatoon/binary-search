# sort list
# find middle of list
# see if num_to_find matches number in middle of list
# if num_to_find matches number in middle of list; return index of number in middle of list.
# if num_to_match does not match number in middle of list, assess whether num_to_match is > or < in regards to number in middle of list.
# eliminate the half of the list that the num_to_match is not on and pick number in middle of new list; list that is not 1/2 length of original list.
# repeat until number is found.  However, if length of list is reduced to 1 and num_to_match still isn't found, return -1 and exit function.


def binary_search(num_to_find, list):
    sorted_list = sorted(list)
    
    starting_index = 0
    ending_index = (len(sorted_list) - 1)
    target_index = 0
        
    while starting_index <= ending_index:
        target_index = (ending_index + starting_index) // 2
        if sorted_list[target_index] < num_to_find:
            starting_index = target_index + 1
            
            
        elif sorted_list[target_index] > num_to_find:
            ending_index = target_index - 1
            
        else:
            return target_index
         
    return -1

print(binary_search(11, [1,5,7,2,3,8,4,9]))
            
         