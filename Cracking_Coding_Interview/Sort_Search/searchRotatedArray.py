#ben isenberg 10/16/2016

#search a rotated sorted array for an item, use a form of binary search
#uses recursion
def searchRotatedArray(my_array, left, right, item):

	middle = (left + right) / 2

	#base case
	if (my_array[middle] == item):
		print(middle)
		return
	#base case
	if ((right - left) == 1 and my_array[right] == item):
		print(right)
		return

	#item is on left side of array
	if (my_array[middle] > item):
		searchRotatedArray(my_array,left,middle-1,item)
	#item is on right side of array
	elif (my_array[left] > item):
		searchRotatedArray(my_array,middle+1,right,item)
	#item is closer to middle
	elif ((item - my_array[middle]) < (item - my_array[left])):
		searchRotatedArray(my_array,middle+1,right,item)
	else:
		searchRotatedArray(my_array,left,middle-1,item)



def main():
	list1 = [15,16,20,25,1,3,4,5,7,10,14]

	searchRotatedArray(list1,0,len(list1),5)

	searchRotatedArray(list1,0,len(list1),20)

main()