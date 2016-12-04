#ben isenberg 10/22/2016

#sort an array so that values are peaks and valleys
def sortPeaksValleys(my_array):
	sorted_array = sorted(my_array)

	#skip by two
	for i in range(1,len(sorted_array),2):
		temp = sorted_array[i-1]
		sorted_array[i-1] = sorted_array[i]
		sorted_array[i] = temp

	print(sorted_array)

def main():
	list1 = [9,1,0,4,8,7]

	sortPeaksValleys(list1)


main()