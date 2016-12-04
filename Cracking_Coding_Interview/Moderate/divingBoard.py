#ben isenberg 10/24/2016

#permutations recursive
def permsBoard(list1, total):

	if (list1 is not None and len(list1) == total):
		print(list1)
		return

	temp = list(list1) #make copy of list1
	temp.append("shorter")
	permsBoard(temp,total)
	
	temp = list(list1) #make copy of list1 
	temp.append("longer")
	permsBoard(temp,total)


def main():
	my_list = []
	permsBoard(my_list,5)
	permsBoard(my_list,10)
	permsBoard(my_list,2)

main()