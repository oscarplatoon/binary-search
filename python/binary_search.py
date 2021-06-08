def binary_search(num,arr,low=0):
    arr = sorted(arr)
    if len(arr) == 0 or (len(arr)==1 and arr[0]!=num):
        return -1
        
    midpoint = len(arr)//2

    if arr[midpoint] == num:
        return midpoint + low
    elif arr[midpoint] < num:
        low += midpoint
        return binary_search(num,arr[midpoint:],low)
    elif arr[midpoint] > num:
        return binary_search(num,arr[:midpoint],low)


