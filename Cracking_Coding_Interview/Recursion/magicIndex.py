#ben isenberg 10/1/2016

#binary search
#find magic index in sorted distinct array, index = element
def binarySearch(my_list):
	
	if (len(my_list) == 0):
		return

	index = len(my_list) / 2

	if (my_list[index] == index):
		print("Found Magic Index %d" % index)
		return

	if (my_list[index] > index):
		binarySearch(my_list[0:index])

	if (my_list[index] < index):
		binarySearch(list[index:])

	return


def main():
	my_list = [0,1,2,3,4,5,6]

	binarySearch(my_list)

main()