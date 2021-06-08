def binary_search(num, array):
    # Pass in a num and an array to search through
    # Find the middle value inside of the array and assign it to a variable
    # Create an if statement to see if num == middle, if true return the index
    # If num == middle is false, split the array in half and repeat the comparison
    # Repeat this step if num == middle is false until true
    # Return the index if found, return a -1 if not found
        count = 0
        for x in array:
            count += 1
        
        middle = count // 2
        
        first_half = array[:middle]
        second_half = array[middle:]

        for i in first_half:
            if i == num:
                return(first_half.index(i))
            else: 
                pass
        
        for y in second_half:
            if y == num:
                print(second_half.index(i))
            else: 
                pass