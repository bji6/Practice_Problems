#ben isenberg 10/16/2016

#search a list of strings using binary search, with empty strings in the list
def searchStringList(my_array, left, right, item):

	middle = (left + right) / 2

	#if middle is empty string, set middle to closest non empty string
	if (my_array[middle] == ""):
		l_index = middle - 1
		r_index = middle + 1
		while(l_index > left or r_index < right):
			if (my_array[l_index] != ""):
				middle = l_index
				break
			if (my_array[r_index] != ""):
				middle = r_index
				break
			l_index = l_index - 1
			r_index = r_index + 1

	#base case
	if (my_array[middle] == item):
		print(middle)
		return

	#item is on left side of array
	if (my_array[middle] > item):
		searchStringList(my_array,left,middle-1,item)
	#item is on right side of array
	elif (my_array[left] > item):
		searchStringList(my_array,middle+1,right,item)



def main():
	list1 = ["at","","","","ball","","","car","","","dad","",""]

	searchStringList(list1,0,len(list1),"ball")

	searchStringList(list1,0,len(list1),"at")

main()