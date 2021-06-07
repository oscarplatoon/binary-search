# sort numbers and set as sorted_list
# note that proportion of covered list => k == 1 / (2**k); k == number of guesses
# consider setting initial start_num as sorted_list[0];
# consider setting initial end_num as sorted_list[len(sorted_list) - 1].
# look for target_num; number exactly 1/2 way between start_num and end_num.  
# if num_to_find < target_num, then end_num = target_num and start_num doesn't change.
# if num_to_find > taget_num, then start_num = target_num and end_num doesn't change.
# if the num_to_find isn't found in the sorted_list, return -1.  
# otherwise, return index_to_find (index of num_to_find) in sorted_list.

def binary_search(num_to_find, list):
    sorted_list = sorted(list)
    index_to_find = 0
    counter = 1
    target_index = round(((len(sorted_list) - 1) / (counter ** 2))

    while index_to_find = 0:
        try:
            if sorted_list[target_index] == num_to_find:
                index_to_find = target_index
            elif num_to_find < sorted_list[target_index]:
                counter += 1
                target_index -= target_index
            elif num_to_find > sorted_list[target_index]:
                counter += 1
                target_index += target_index
        except:
              index_to_find = -1
         
    return index_to_find

print(binary_search(7, [1,5,7,2,3,8,4,9]))
            
            
        


    # for x in sorted_list:
        # print(i)
    
        # print(target_num)
       
        
        
        # if x == num_to_find:
        #     index = x
        # elif 
    
    # print(sorted_list)
    # print(sorted_list[len(sorted_list) - 1])
    # print(len(sorted_list) - 1)

    # print(sorted_list)
    # print(i)
    # print(target_num)
    
# super_big_array = [1,5,7,2,3,8,4,9]
print(binary_search(7, [1,5,7,2,3,8,4,9]))
# print(binary_search(6, super_big_array) == -1)