def binary_search(target, array):
    #sort array then enter our recursive helper function
    array.sort()
    return binary_search_helper(target,array,0,len(array)-1)

#check middle index and adjust left or right pointer depending on if
#target is lesser or greater than middle index
#return -1 to exit if left crosses right
def binary_search_helper(target, array, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    if target == potential_match:
        return middle
    elif target < potential_match:
        return binary_search_helper(target, array, left, middle-1)
    else:
        return binary_search_helper(target, array, middle+1, right)