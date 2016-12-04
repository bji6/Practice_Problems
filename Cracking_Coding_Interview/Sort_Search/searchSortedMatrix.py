#ben isenberg 10/22/2016

#search an MxN matrix where all columns and rows are sorted
def searchSortedMatrix(my_matrix, rows, cols, item):

	col_index = -1
	for i in range(cols):
		if (my_matrix[0][i] > item):
			break
		col_index = col_index + 1

	if (col_index < 0):
		print("Error item not found")
		return

	temp_array = []
	for i in range(rows):
		temp_array.append(my_matrix[i][col_index])

	row_index = binarySearch(temp_array,0,len(temp_array),item)

	if (row_index < 0):
		print("Error item not found")
	else:
		print("%d at Matrix[%d][%d]" % (item,row_index,col_index))


def binarySearch(my_array,left,right,item):
	
	if ((left-right) == 1 and my_array[0] != item):
		return -1

	middle = (left+right) / 2

	#base case
	if (my_array[middle] == item):
		return middle

	right_index = -1
	left_index = -1

	#item is on left side of array
	if (my_array[middle] > item):
		left_index = binarySearch(my_array, 0,middle-1,item)
	#item is on right side of array
	elif (my_array[middle] < item):
		right_index = binarySearch(my_array, middle+1,right,item)

	if (right_index > left_index):
		return right_index
	else:
		return left_index



def main():
	matrix = [[2,20,34,56,89],
			  [7,23,38,60,91],
			  [11,25,43,61,99],
			  [16,29,47,75,118]]

	searchSortedMatrix(matrix,4,5,61)

	searchSortedMatrix(matrix,4,5,110)

	searchSortedMatrix(matrix,4,5,7)
	searchSortedMatrix(matrix,4,5,118)

main()