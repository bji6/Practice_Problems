#ben isenberg 10/2/2016


#recursive method to produce all permutations of a string
def stringPerms(my_string):
	#base case
	if (len(my_string) < 2):
		return my_string
	#base case
	if (len(my_string) == 2):
		temp = my_string[1] + my_string[0]
		
		if (my_string[0] == my_string[1]):  #remove duplicate chars
			return [my_string[0]]
		
		return [my_string, temp]

	first_char = my_string[0]

	permutations = stringPerms(my_string[1:])

	permutations2 = []

	for x in permutations:
		for i in range(len(x)+1):  #need +1 so we insert at end of string as well
			new_str = x[:i] + first_char + x[i:] #insert char at index i

			permutations2.append(new_str)

	return permutations2

def main():
	print(stringPerms("ab"))
	print(stringPerms("abc"))
	#BEWARE: number of permutations is factorial string length
	#grows very fast, kills computer
	print(len(stringPerms("abcdefg")))
	print(len(stringPerms("abcd")))
	print(len(stringPerms("abcdefgg")))

main()