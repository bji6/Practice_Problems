#ben isenberg 10/16/2016

#insertion sort algo
# inserts items in B into A, which is already sorted
def insertionSort(array_A, array_B):
	start_index = len(array_A) - len(array_B)

	#insert contents of B into end of A
	counter = 0
	for i in range(start_index, len(array_A)):
		array_A[i] = array_B[counter]
		counter = counter + 1

	#sort A
	for i in range(start_index, len(array_A)):
		j = i
		while (j > 0 and array_A[j-1] > array_A[j]):
			temp = array_A[j - 1]
			array_A[j - 1] = array_A[j]
			array_A[j] = temp
			j = j - 1

	return array_A


def main():
	list1 = [1,2,4,6,8,10,14,16,23,39,0,0,0,0]
	list2 = [18,7,0,11]

	print(insertionSort(list1,list2))

main()