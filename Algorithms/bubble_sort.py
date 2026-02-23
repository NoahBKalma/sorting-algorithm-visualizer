def bubble_sort(arr):
	'''
		Bubble sort works by comparing adjacent elements and swapping them if they are in the wrong order.
		The algorithm repeats this process until the entire list is sorted.
	'''

	# Set the upper bound for the unsorted portion of the list
	arr_limit = len(arr)-1

	while arr_limit > 0:
	
		# Keep track of the last swap position to optimize the sorting process
		last_swap = 0

		for j in range(arr_limit):

			yield arr.copy(), j, j+1, "comparison"

			# If the current element is greater than the next element, swap them
			if arr[j+1] < arr[j]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				last_swap = j
				yield arr.copy(), j, j+1, "swap"
		# Update the upper bound for the unsorted portion of the list to the last swap position
		arr_limit = last_swap
