def merge_sort(arr):
    '''
    Breaks up an array into half, and continues recursively until each array is sorted
    Then it merges each array, working back uptil the entire array is sorted
    '''
    def _merge_sort(arr, left, right):
        '''
        Recursive method to sort the lists, uses merge method to combine
        '''
        if left >= right:
            return
        
        mid = (left + right) // 2
        
        # Sort left half
        yield from _merge_sort(arr, left, mid)
        
        # Sort right half
        yield from _merge_sort(arr, mid + 1, right)
        
        # Merge the two halves
        yield from merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        '''
        Merges two given lists together
        Takes in the array to sort and the left/right values of the portion currently being sorted
        '''
        
        # Creates temporary arrays to rewrite over the main array from
        left_part = arr[left:mid+1]
        right_part = arr[mid+1:right+1]
        
        i = j = 0
        k = left
        
        # Merge back into original array
        while i < len(left_part) and j < len(right_part):
            
            # Compare the fronts of the left and right arrays
            yield arr, left + i, mid + 1 + j, "comparison"
    
            # Adds the smaller of the two to the front of the list
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1

            # Yield the swap step
            yield arr, k, None, "swap"
            k += 1
        
        # Add remaining elements of either list
        while i < len(left_part):
            arr[k] = left_part[i]
            yield arr, k, None, "swap"
            i += 1
            k += 1
        
        while j < len(right_part):
            arr[k] = right_part[j]
            yield arr, k, None, "swap"
            j += 1
            k += 1

    # Begin the mergesort, makes cleaner main function
    yield from _merge_sort(arr, 0, len(arr) - 1)


    '''

    Working merge_sort algorithm but not for my animator

    def merge_sort(arr):
        
        # If the array is length 1, return it
        arr_len = len(arr)
        if len(arr) <= 1:
            return arr
        
        # Split array
        arr_l = arr[:arr_len//2]
        arr_r = arr[arr_len//2:]
        
        # Yields from left then right array
        left = yield from merge_sort(arr_l)
        right = yield from merge_sort(arr_r)

        # Merge Arrays until one is empty, then add the rest of the non-empty list if there is anything
        merged_arr = []
        i=j=0

        while i < len(left) and j < len(right):
             if left[i] < right[j]:
                 merged_arr.append(left[i])
                 i += 1
             else:
                 merged_arr.append(right[j])
                 j += 1

        merged_arr.extend(left[i:])
        merged_arr.extend(right[j:])


        # Yield for animation, return for recursion
        yield merged_arr, i, j, "comparison"
        return merged_arr


    for step in merge_sort([1,2,4,6,7,4,2,3,5]):
        print(step)
    '''