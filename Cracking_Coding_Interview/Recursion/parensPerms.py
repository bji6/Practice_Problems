#ben isenberg 10/2/2016


#recursive method to produce all permutations of n pairs of parens
def parensPerms(number_of_pairs):
	#base case
	if (number_of_pairs == 1):
		return ["()"]

	parensList = parensPerms(number_of_pairs - 1)

	new_parensList = []
	
	for x in parensList:
		temp1 = "()" + x
		new_parensList.append(temp1)
		temp2 = "(" + x + ")"
		new_parensList.append(temp2)
		temp3 =	x + "()" 
		if (temp1 != temp3):  #don't add duplicates
			new_parensList.append(temp3)

	return new_parensList

def main():
	print(parensPerms(3))
	print(len(parensPerms(5)))

main()