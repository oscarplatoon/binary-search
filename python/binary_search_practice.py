
# def binary_search(num_to_find, list):
#     sorted_list = sorted(list)
#     index_to_find = 0
#     print(sorted_list)
    
#     starting_index = 0
#     ending_index = (len(sorted_list) - 1)
#     target_index = (ending_index - starting_index) // 2
#     loop_counter = 0
        
#     while index_to_find == 0 and loop_counter < 10:
#         print(f"starting index is: {starting_index}")
#         print(f"index to find: {index_to_find}")
#         loop_counter += 1
        
#         try:
#             if sorted_list[target_index] == num_to_find:
#                 index_to_find = target_index
#                 print(f"the if block target index: {target_index}")
                
#             elif num_to_find < sorted_list[target_index]:
#                 ending_index = target_index
#                 length_of_mini_list = ending_index - starting_index
#                 target_index = ((length_of_mini_list) // 2)
#                 # - (length_of_mini_list % 2 > 0)
#                 print(f"starting index at elif1 is: {starting_index}")
#                 print(f"ending index at elif1 is: {ending_index}")
#                 print(f"target index at elif1 is: {target_index}")
                
#             elif num_to_find > sorted_list[target_index]:
#                 starting_index = target_index
#                 target_index = starting_index + ((ending_index - starting_index) // 2) + (ending_index % starting_index > 0)
#                 print(f"starting index at elif2 is: {starting_index}")
#                 print(f"ending index at elif2 is: {ending_index}")
#                 print(f"target index at elif2 is: {target_index}")
                
#         except:
#               index_to_find = -1
         
#     return index_to_find

# print(binary_search(2, [1,5,7,2,3,8,4,9]))
            
            
        


#     # for x in sorted_list:
#         # print(i)
    
#         # print(target_num)
       
        
        
#         # if x == num_to_find:
#         #     index = x
#         # elif 
    
#     # print(sorted_list)
#     # print(sorted_list[len(sorted_list) - 1])
#     # print(len(sorted_list) - 1)

#     # print(sorted_list)
#     # print(i)
#     # print(target_num)
    
# # super_big_array = [1,5,7,2,3,8,4,9]
# # print(binary_search(7, [1,5,7,2,3,8,4,9]))
# # print(binary_search(6, super_big_array) == -1)