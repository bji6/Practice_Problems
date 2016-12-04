#ben isenberg 10/30/2016

#find range in array that must be sorted for entire array to be sorted
def subSort(my_array):

	min_index = -1
	max_index = -1
	max_number = my_array[0]
	min_unsorted_number = 99999

	# find last index that needs to be sorted
	for i in range(len(my_array)-1):
		if (my_array[i] < max_number):
			max_index = i
			if (my_array[i] < min_unsorted_number):
				min_unsorted_number = my_array[i]
		else:
			max_number = my_array[i]

	# find first index that needs to be sorted
	for i in range(max_index):
		if (my_array[i] > min_unsorted_number):
			min_index = i
			break


	print("%d, %d" % (min_index,max_index))

def main():
	
	subSort([1,2,4,7,10,11,7,12,6,7,16,18,19])

main()