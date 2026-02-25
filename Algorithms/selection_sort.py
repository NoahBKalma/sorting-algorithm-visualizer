def selection_sort(arr):
    
    for i in range(len(arr)-1):
        
        min_index = i
        # Iterates through list, finds min
        for j in range(i+1, len(arr)):
            
            yield arr.copy(), j, j+1, "comparison"

            if arr[j] <= arr[min_index]:
                min_index = j
                
        # Swaps the smallest value to the end of the sorted portion
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]       
            yield arr.copy(), i, min_index, "swap"