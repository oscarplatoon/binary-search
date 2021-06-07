
def middle_index(start_index, end_index):
    i = (end_index+1 - start_index)//2
    return (i if (end_index+1 - start_index)%2 == 0 else i + 1)

def binary_search(number_to_find, sorted_values):
   
    start_index = 0
    end_index = len(sorted_values) - 1

    while True:
        middle_i = middle_index(start_index, end_index)-1
        middle_value = sorted_values[middle_i]

        if number_to_find == middle_value:
            return middle_i
        elif start_index == end_index:
            return -1
        elif number_to_find < middle_value:
            end_index = middle_i - 1
        elif number_to_find > middle_value:
            start_index = middle_i + 1
        
    # print(middle_value)
    # if number_to_find == sorted_values[middle_i]:
    #     print(f"Number found {middle_i}")
    #     return middle_i
    # elif len(sorted_values) == 1:
    #     print("Number not found")
    #     return -1
    # elif number_to_find < middle_value:
    #     print("Number smaller than middle value")
    #     return binary_search(number_to_find, sorted_values[0:middle_i])
    # elif number_to_find > middle_value:
    #     print("Number larger than middle value")
    #     return binary_search(number_to_find, sorted_values[middle_i+1:])

