# Ben Isenberg 9/10/2016

def checkforpermutation(string1, string2):

	if (len(string1) != len(string2)):
		print("Not permutations of eachother\n")
		return

	#sort lists
	sorted_list1 = sortlist(string1)
	sorted_list2 = 	sortlist(string2)


	for x in range(len(sorted_list1)):
		if (sorted_list1[x] != sorted_list2[x]):
			print("Not permutations of eachother\n")
			return
	
	print("Permutations of eachother")

#implemented selection sort  O(n^2) runtime worstcase
def sortlist(list1):
	sorted_list = list(list1)

	for x in range(len(sorted_list)):
		item = sorted_list[x]
		for y in range(x,len(sorted_list)):
			if (ord(sorted_list[y]) < ord(item)):
				sorted_list[x] = sorted_list[y]
				sorted_list[y] = item
				item = sorted_list[x]
	
	return sorted_list

def main():
	string1 = "bannana"
	string2 = "apple"
	string3 = "aaabnnn"

	checkforpermutation(string1, string2)
	checkforpermutation(string3, string1)

main()