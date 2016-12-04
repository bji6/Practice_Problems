#ben isenberg 10/30/2016

#find items to swap in 2 arrays so their sum is equal
def sumSwap(array1, array2):
	sum1 = 0
	sum2 = 0
	for i in range(len(array1)):
		sum1 = sum1 + array1[i]
	for i in range(len(array2)):
		sum2 = sum2 + array2[i]

	diff = abs(sum1 - sum2)

	# sort arrays
	sorted1 = sorted(array1)
	sorted2 = sorted(array2)
	num_to_find = None
	num1 = None
	print(sum2)
	print(sum1)

	for i in range(len(array1)):
		num1 = array1[i]
		newsum2 = sum2 + array1[i]
		newsum1 = sum1 - array1[i]
		if ((newsum2 - newsum1) % 2 == 0):
			num_to_find = (newsum2 - newsum1) / 2
			print("num to find %d" % num_to_find)
			index = binarySearch(sorted2,0,len(sorted2)-1,num_to_find)
			if (index is not None):
				break

	print("%d,%d" % (num1,num_to_find))

#search a list of strings using binary search, with empty strings in the list
def binarySearch(my_array, left, right, item):

	middle = (left + right) / 2

	#base case
	#item not found
	if (left < 0 or right < 0 or middle >= len(my_array)):
		return None
	if (my_array[middle] == item):
		#print(middle)
		return middle
	if (my_array[right] == item):
		return right
	if (my_array[left] == item):
		return left


	#item is on left side of array
	if (my_array[middle] > item):
		binarySearch(my_array,left,middle-1,item)
	#item is on right side of array
	else:
		binarySearch(my_array,middle+1,right,item)
	
def main():
	
	sumSwap([4,1,2,1,1,2],[3,6,3,3])
	sumSwap([5,3],[4,2])

main()