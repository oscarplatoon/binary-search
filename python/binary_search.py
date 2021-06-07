
def middle_index(start_index, end_index):
    i = (end_index+1 - start_index)//2
    return (i if (end_index+1 - start_index)%2 == 0 else i + 1)

def binary_search(number_to_find, sorted_values):
   
    start_index = 0
    end_index = len(sorted_values) - 1

    while True:
        middle_i = middle_index(start_index, end_index)-1+start_index
        middle_value = sorted_values[middle_i]

        if number_to_find == middle_value:
            return middle_i
        elif start_index == end_index:
            return -1
        elif number_to_find < middle_value:
            end_index = middle_i - 1
        else:
            start_index = middle_i + 1

