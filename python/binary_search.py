
def middle_index(sorted_values):
    i = len(sorted_values)//2
    return (i if len(sorted_values)%2 == 0 else i + 1)

def binary_search(number_to_find, sorted_values):
    middle_i = middle_index(sorted_values)
    middle_value = sorted_values[middle_i]
    print(middle_value)
    if number_to_find == sorted_values[middle_i]:
        print("Number found")
        return middle_i
    elif len(sorted_values) == 1:
        print("Number not found")
        return -1
    elif number_to_find < middle_value:
        print("Number smaller than middle value")
        return binary_search(number_to_find, sorted_values[0:middle_i])
    elif number_to_find > middle_value:
        print("Number larger than middle value")
        return binary_search(number_to_find, sorted_values[middle_i+1:])

