#ben isenberg 10/23/2016

#find smallest diff between pair of values from each list
#assume same size arrays
def smallestDifference(list1,list2):
	sorted1 = sorted(list1)
	sorted2 = sorted(list2)

	min_diff = 1000000
	new_array = []
	min_pair = []

	prev_from1 = False
	j = 0
	k = 0
	while(j < len(sorted2) or k < len(sorted1)):
		if (k < len(sorted1) and sorted1[k] <= sorted2[j]):
			#check if last value was from other array
			if (prev_from1 == False and len(new_array) > 0):
				diff = sorted1[k] - new_array[-1]
				if (diff > -1 and diff < min_diff):
					min_diff = diff
					min_pair = [new_array[-1],sorted1[k]]
			new_array.append(sorted1[k])
			prev_from1 = True
			k = k + 1
		elif (j < len(sorted2)):
			#check if last value was from other array
			if (prev_from1 == True and len(new_array) > 0):
				diff = sorted2[j] - new_array[-1]
				if (diff > -1 and diff < min_diff):
					min_diff = diff
					min_pair = [new_array[-1], sorted2[j]]
			new_array.append(sorted2[j])
			prev_from1 = False
			j = j + 1

	print(min_diff)
	return min_pair

def main():
	list1 = [1,3,15,11,2]
	list2 = [23,127,235,19,8]
	
	print(smallestDifference(list1,list2))

	list1 = [1,3,15,11,2]
	list2 = [2890,127,235,190,876]
	
	print(smallestDifference(list1,list2))	
	
main()