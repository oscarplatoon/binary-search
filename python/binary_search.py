def binary_search(num, array):
    array.sort()
    return_index = -1
    current_array = array
    index_start = 0
    while len(current_array) > 1:
        middle_index = round((len(current_array))/2)
        middle_num = current_array[round((len(current_array))/2)]
        if num == middle_num:
            return_index = middle_index + index_start
            return return_index
        elif num > middle_num:
            index_start += middle_index
            current_array = current_array[middle_index:]
        elif num < middle_num:
            current_array = current_array[:middle_index]
    if current_array[0] == num:
        return 0 + index_start
    else:
        return return_index
