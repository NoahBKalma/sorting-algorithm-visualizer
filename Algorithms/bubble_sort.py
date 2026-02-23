def bubble_sort(arr):

	arr_limit = len(arr)-1

	while arr_limit > 0:
	
		last_swap = 0

		for j in range(arr_limit):

			yield arr.copy(), j, j+1, "comparison"


			if arr[j+1] < arr[j]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				last_swap = j
				yield arr.copy(), j, j+1, "swap"

		arr_limit = last_swap
