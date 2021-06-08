def binary_search(num, arr, min_index=0, max_index=None, center_index=None):

    arr.sort()
    if max_index == None:
        max_index = len(arr)
    center_index = ((max_index + min_index) // 2)
    print(center_index)
    

    if arr[center_index]==num:
        # print(arr[center_index])
        # print (min_index, max_index)
        return ("Got it!")
    elif arr[center_index]<num:
        min_index = center_index
        center_index += (max_index - min_index) // 2
        
        binary_search(num, arr, min_index, max_index)
    elif (min_index == mad_index):
        return -1
    else:
        max_index = center_index
        binary_search(num, arr, min_index, max_index)
        center_index -= (max_index - min_index) // 2

    
binary_search(17,[3,5,9,8,2,1,10,14,17,19,11])