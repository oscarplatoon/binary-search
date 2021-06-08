def binary_search(object, array):
    array.sort()
    lo = 0
    hi = len(array) -1
    while True:
        index = lo + ((hi - lo) // 2)
        if array[index] == object:
            return index
        elif lo >= hi:
            return -1
        elif  object < array[index]:
            hi = index -1
        else:
            lo = index +1
