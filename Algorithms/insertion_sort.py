def insertion_sort(arr):
    
    # Iterates through the array
    for i in range(1, len(arr)):
        
        # Yields the beginning comparison step
        yield arr.copy(), i, i+1, "comparison"
        
        j=i
        
        # Moves smallest elements to the front
        while arr[j] < arr [j-1] and j > 0:
            yield arr.copy(), j, j-1, "comparison"
            
            arr[j], arr[j-1] = arr[j-1], arr[j]
            
            yield arr.copy(), j, j-1, "swap"

            
            j -= 1
        
        
    return arr