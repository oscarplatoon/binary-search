
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

print(binary_search(2, [1,5,7,2,3,8,4,9]))
            
         