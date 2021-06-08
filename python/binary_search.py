
# 1. Say you're searching for a value 'number_to_find' in a search set of sorted_values
# 2. Find the middle value in 'sorted_values' we'll call 'middle_value'
# 3. If 'number_to_find' is equal to 'middle_value' then your target is found
# 4. If 'number_to_find' is less than 'middle_value', split your 'sorted_values' in half and repeat the algorithm on your new subset (the half of 'sorted_values' before 'middle_value')
# 5. If 'number_to_find' is greater than 'middle_value', repeat step but with the half of 'sorted_values' values after 'middle_value'
# 6. Repeat until you find 'number_to_find' or return -1 if it doesn't exist

def binary_search(tgt, arr):
    # Built in python sort method because I am lazy
    sort_array = sorted(arr)
    print('sorted array:', sort_array)
    low = 0
    high = len(sort_array) - 1

    # iterative approach set arr length low and high
    while low <= high:
        # mid will be our split
        mid = (low + high) // 2

        # if our target equal to our mid value return the index of that value
        if tgt == sort_array[mid]:
            print('new mid:', mid)
            return mid

        # if our tgt is less than the lower half of the array
        elif tgt < sort_array[mid]:
            high = mid - 1
            print('high', high)

        # if our tgt is greater than lower half
        else:
            low = mid + 1
            print('low', low)
    return -1

# super_big_array = [1,5,7,2,3,8,4,9]
super_array = [12,43,55,65,68,90,35,69,22,25,29,31,50,100,101,110]

print(binary_search(6, super_array))