#ben isenberg 10/1/2016

#recursive method
# find all subsets of a set
def powerSets(my_set):
	#base case
	if (len(my_set) == 0):
		return

	print(my_set)

	for x in my_set:
		powerSets(my_set.difference(set([x])))

	return


def main():
	powerSets(set([1,2,3,4]))

main()