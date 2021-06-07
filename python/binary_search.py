import math

def binary_search(object, array):
    array.sort()
    lo = 0
    hi = len(array) -1
    index = math.floor(hi/2)
    while True:
        if array[index] == object:
            return index
        elif lo > hi:
            return -1
        elif array[index] > object:
            hi = index -1
            index = lo + math.floor((index - lo)/2)
        else:
             lo = index +1
             index = index + math.floor((hi + 1 - index)/ 2)
