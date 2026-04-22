# Using Lomuto Partition

def quick_sort(arr):

	def _quick_sort(arr, left, right):
		'''
		Breaks up quicksort around a pivot
		'''
		if left < right:
			# pi is the partition return index of pivot
			pivotIndex = yield from partition(arr, left, right)
			
			# Sorts elements smaller than pivot
			yield from _quick_sort(arr, left, pivotIndex - 1)
			# Sorts elements greater than pivot location
			yield from _quick_sort(arr, pivotIndex + 1, right)

	def partition(arr, left, right):
		'''
		Get a pivot (using Lomuto partition, so pivot is rightmost element) and sort array around pivot.
		Then return upwards
		'''
		pivot = arr[right]

		i = left - 1

		for j in range(left, right):
			yield arr, j, right, "comparison"
			if arr[j] < pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
				yield arr, i, j, "swap"

		# move pivot after smaller elements and
		# return its position
		arr[right], arr[i + 1] = arr[i+1], arr[right];
		yield arr, i+1, right, "swap"
		return i + 1

    # Begin the quick sort, makes cleaner main function
	yield from _quick_sort(arr, 0, len(arr) - 1)